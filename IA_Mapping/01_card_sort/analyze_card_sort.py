"""Analyze open card sort results.

Reads card_deck.csv and raw_data/card_sort_results.csv, then writes to analysis_output/:
  similarity_matrix.csv      percent of participants who put each pair of cards together
  similarity_matrix.png/svg  heatmap of that matrix, ordered by cluster
  cluster_dendrogram.png/svg average linkage hierarchical clustering
  consensus_summary.md       clusters, agreement scores, label tables, strongest and weakest pairs

Usage: python3 analyze_card_sort.py [results.csv]
"""
import sys
from itertools import combinations
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, fcluster, leaves_list, linkage
from scipy.spatial.distance import squareform

HERE = Path(__file__).parent
OUT = HERE / "analysis_output"
CLUSTER_CUT = 0.5  # cards join a cluster when at least half of participants paired them

deck = pd.read_csv(HERE / "card_deck.csv")
results_path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "raw_data" / "card_sort_results.csv"
res = pd.read_csv(results_path)
res["group_label"] = res["group_label"].fillna("").astype(str).str.strip()
if (res["group_label"] == "").any():
    sys.exit("Some rows have no group_label. Fill every card for every participant first.")

ids = list(deck["card_id"])
labels = dict(zip(deck["card_id"], deck["card_label"]))
parts = sorted(res["participant_id"].unique())
n = len(parts)
OUT.mkdir(exist_ok=True)

# Similarity matrix
idx = {c: i for i, c in enumerate(ids)}
counts = np.zeros((len(ids), len(ids)))
for p in parts:
    sub = res[res["participant_id"] == p]
    for _, grp in sub.groupby("group_label"):
        cards = list(grp["card_id"])
        for a, b in combinations(cards, 2):
            counts[idx[a], idx[b]] += 1
            counts[idx[b], idx[a]] += 1
np.fill_diagonal(counts, n)
sim = counts / n
sim_pct = pd.DataFrame(np.round(sim * 100).astype(int), index=ids, columns=ids)
sim_pct.to_csv(OUT / "similarity_matrix.csv")

# Clustering
dist = 1 - sim
np.fill_diagonal(dist, 0)
Z = linkage(squareform(dist, checks=False), method="average")
order = [ids[i] for i in leaves_list(Z)]
clusters = fcluster(Z, t=1 - CLUSTER_CUT, criterion="distance")
cluster_of = dict(zip(ids, clusters))

short = [f"{c}  {labels[c]}" for c in ids]

# Dendrogram
fig, ax = plt.subplots(figsize=(10, 8))
dendrogram(Z, labels=short, orientation="right", ax=ax, color_threshold=1 - CLUSTER_CUT,
           above_threshold_color="#555555")
ax.axvline(1 - CLUSTER_CUT, color="#B00020", linestyle="--", linewidth=1)
ax.set_xlabel("Distance (1 minus share of participants who paired the cards)")
ax.set_title(f"Card Sort Cluster Diagram (average linkage, n = {n})", fontsize=13)
ax.legend([ax.lines[-1]], [f"{int(CLUSTER_CUT*100)}% agreement cut"], loc="lower right", fontsize=9)
ax.tick_params(axis="y", labelsize=9)
plt.tight_layout()
for ext in ("png", "svg"):
    fig.savefig(OUT / f"cluster_dendrogram.{ext}", dpi=200)
plt.close(fig)

# Heatmap ordered by cluster
ordered = sim_pct.loc[order, order]
fig, ax = plt.subplots(figsize=(11, 10))
im = ax.imshow(ordered.values, cmap="Blues", vmin=0, vmax=100)
ax.set_xticks(range(len(order)))
ax.set_xticklabels(order, rotation=90, fontsize=9)
ax.set_yticks(range(len(order)))
ax.set_yticklabels([f"{c}  {labels[c]}" for c in order], fontsize=9)
for i in range(len(order)):
    for j in range(len(order)):
        v = ordered.values[i, j]
        if i != j:
            ax.text(j, i, v, ha="center", va="center", fontsize=7,
                    color="white" if v >= 60 else "#1a1a1a")
cb = fig.colorbar(im, ax=ax, fraction=0.04)
cb.set_label("% of participants who grouped the pair together")
ax.set_title(f"Card Sort Similarity Matrix (n = {n})", fontsize=13)
plt.tight_layout()
for ext in ("png", "svg"):
    fig.savefig(OUT / f"similarity_matrix.{ext}", dpi=200)
plt.close(fig)

# Consensus summary
lines = [f"# Card Sort Consensus Summary\n", f"Participants: {n} ({', '.join(parts)})  ",
         f"Cluster cut: cards grouped together by at least {int(CLUSTER_CUT*100)}% of participants\n"]

lines.append("## Groups Each Participant Made\n")
lines.append("| Participant | Number of groups | Group labels |\n| --- | --- | --- |")
for p in parts:
    g = res[res["participant_id"] == p]["group_label"].unique()
    lines.append(f"| {p} | {len(g)} | {'; '.join(g)} |")

lines.append("\n## Clusters\n")
lines.append("Agreement = average pairwise similarity inside the cluster. "
             "Labels = what participants called the group holding most of these cards.\n")
lines.append("| Cluster | Cards | Agreement | Participant labels |\n| --- | --- | --- | --- |")
for k in sorted(set(clusters), key=lambda k: order.index([c for c in ids if cluster_of[c] == k][0])):
    members = [c for c in order if cluster_of[c] == k]
    if len(members) > 1:
        pairs = [sim_pct.loc[a, b] for a, b in combinations(members, 2)]
        agree = f"{round(np.mean(pairs))}%"
    else:
        agree = "single card"
    sub = res[res["card_id"].isin(members)]
    lab = (sub.groupby(["participant_id", "group_label"]).size().reset_index(name="k")
           .sort_values("k", ascending=False).drop_duplicates("participant_id"))
    lab_txt = "; ".join(f"{r.group_label} ({r.participant_id})" for r in lab.itertuples())
    card_txt = "<br>".join(f"{c} {labels[c]}" for c in members)
    lines.append(f"| {k} | {card_txt} | {agree} | {lab_txt} |")

lines.append("\n## Where Each Card Went\n")
lines.append("| Card | " + " | ".join(parts) + " | Strongest partner |")
lines.append("| --- | " + " | ".join("---" for _ in parts) + " | --- |")
for c in order:
    row = [res[(res.participant_id == p) & (res.card_id == c)]["group_label"].iloc[0] for p in parts]
    others = sim_pct.loc[c, [o for o in ids if o != c]]
    best = others.idxmax()
    lines.append(f"| {c} {labels[c]} | " + " | ".join(row) + f" | {best} ({others[best]}%) |")

pairs = [(sim_pct.loc[a, b], a, b) for a, b in combinations(ids, 2)]
strong = sorted([x for x in pairs if x[0] == 100])
lines.append("\n## Pairs Every Participant Put Together\n")
lines.append("\n".join(f"* {a} {labels[a]} + {b} {labels[b]}" for _, a, b in strong) or "None")

split = sorted([c for c in ids if 0 < max(sim_pct.loc[c, [o for o in ids if o != c]]) < 100])
lines.append("\n## Cards With No Stable Home\n")
lines.append("Cards whose strongest partner was paired with them by less than 100% of participants.\n")
for c in split:
    best = sim_pct.loc[c, [o for o in ids if o != c]].idxmax()
    lines.append(f"* {c} {labels[c]} (strongest partner {best}, {sim_pct.loc[c, best]}%)")

(OUT / "consensus_summary.md").write_text("\n".join(lines) + "\n")
print(f"Done. {n} participants, {len(set(clusters))} clusters. Output in {OUT}")

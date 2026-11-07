"""Build current and revised sitemaps (SVG and PNG) with Graphviz.

Notation (based on Garrett's Visual Vocabulary):
  solid box            page or screen
  stacked box          a set of similar pages (one per class or section)
  rounded gray box     content area or panel inside a page (not a separate page)
  dashed box           separate system the student has to leave registration for
  dotted arrow         contextual link (inline link, breadcrumb jump, button)
  [Cxx]                card sort card that this page or panel serves
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
HEAD = """digraph G {
  graph [rankdir=LR, fontname="Inter", fontsize=22, labelloc=t, nodesep=0.22, ranksep=0.55, pad=0.35, bgcolor="white", splines=ortho];
  node  [fontname="Inter", fontsize=12, shape=box, style=filled, fillcolor="white", color="#1a1a1a", penwidth=1.4, margin="0.16,0.07"];
  edge  [color="#1a1a1a", penwidth=1.2, arrowsize=0.7, fontname="Inter", fontsize=10];
"""
def page(i, t, lvl=""): return f'  {i} [label="{t}", fillcolor="{ {"0":"#1a1a1a","1":"#DCE9F7","2":"white"}.get(lvl,"white") }", fontcolor="{"white" if lvl=="0" else "#1a1a1a"}"];\n'
def panel(i, t): return f'  {i} [label="{t}", style="rounded,filled", fillcolor="#EEEEEE", fontsize=11];\n'
def stack(i, t): return f'  {i} [label="{t}", peripheries=2];\n'
def outside(i, t): return f'  {i} [label="{t}", style="dashed,filled", fillcolor="#FFF4CC"];\n'
def util(i, t): return f'  {i} [label="{t}", shape=box, style="rounded,filled", fillcolor="#F3E5F5", fontsize=11];\n'
def e(a, b, ctx=False, lbl=""):
    attrs = []
    if ctx: attrs += ['style=dotted', 'constraint=false', 'color="#555555"']
    if lbl: attrs.append(f'label="{lbl}"')
    return f"  {a} -> {b}" + (f" [{', '.join(attrs)}]" if attrs else "") + ";\n"


def current():
    s = HEAD + '  label="Current IA: Weber State class registration (from Phase 1 audit)\\nDeepest path to a section detail: 7 levels\\n ";\n'
    s += page("portal", "eWeber portal home\\n(app tiles)", "0")
    s += page("reghome", "Registration home\\nL1", "1")
    s += page("sem", "Select the Semester\\n+ tuition agreement\\n(drop rule buried here) L2")
    s += page("term", "Term selection\\nL3")
    s += page("rfc", "Register for Classes\\n(one page, 3 panes) L4")
    s += panel("find", "Find Classes pane\\nsearch form L5")
    s += stack("res", "Search results\\n(codes, gray day boxes) L6")
    s += stack("det", "Section details\\nmeeting times, seats, waitlist L7")
    s += panel("sch", "Schedule pane\\n(weekly calendar)")
    s += panel("sum", "Summary pane\\nAdd = pending only\\nAction dropdown to drop\\nSubmit in far corner")
    s += outside("sb", "Registration\\nSchedule Builder\\n(separate app)")
    s += outside("ct", "CatTracks\\ndegree progress and\\nprerequisites (separate app)")
    s += outside("pay", "Tuition and payment\\n(separate from registration)")
    s += outside("adv", "Advisor\\n(outside the system)")
    s += e("portal", "reghome") + e("reghome", "sem") + e("sem", "term") + e("term", "rfc")
    s += e("rfc", "find") + e("find", "res") + e("res", "det") + e("rfc", "sch") + e("rfc", "sum")
    s += e("portal", "sb") + e("portal", "ct") + e("portal", "pay")
    s += e("det", "ct", True, "student opens new tab to check prereqs") + e("det", "adv", True)
    s += "}\n"
    return s


def revised():
    s = HEAD.replace("rankdir=LR", "rankdir=TB").replace("splines=ortho", "splines=spline").replace("ranksep=0.55", "ranksep=0.5") + '  label="Revised IA: Weber State class registration\\nEvery task is at most 2 levels from Registration Home\\n ";\n'
    # Global elements
    s += page("home", "Registration Home\\nL0", "0")
    s += """  subgraph cluster_global { label="Global navigation (every page)"; fontsize=13; style="rounded,dashed"; color="#7A1FA2";
    hdr [label="Header bar: logo/home link,\\nsemester switcher [C14]", style="rounded,filled", fillcolor="#F3E5F5", fontsize=11];
    u1 [label="Utility nav: Help and Glossary [C20]", style="rounded,filled", fillcolor="#F3E5F5", fontsize=11];
    u2 [label="Utility nav: Contact My Advisor [C19]", style="rounded,filled", fillcolor="#F3E5F5", fontsize=11];
    u3 [label="Utility nav: Sign Out", style="rounded,filled", fillcolor="#F3E5F5", fontsize=11];
    { rank=same; hdr; u1; u2; u3; }
    hdr -> u1 -> u2 -> u3 [style=invis];
  }
"""
    s += """  subgraph cluster_home { label="On Registration Home"; fontsize=12; style="rounded"; color="#888888";
    h1 [label="Registration date [C17]", style="rounded,filled", fillcolor="#EEEEEE", fontsize=11];
    h2 [label="Holds [C16]", style="rounded,filled", fillcolor="#EEEEEE", fontsize=11];
    h3 [label="My classes status\\nand next steps", style="rounded,filled", fillcolor="#EEEEEE", fontsize=11];
  }
  { rank=same; home; h1; h2; h3; }
"""
    s += page("find", "Find Classes\\nL1", "1")
    s += panel("f1", "Search + time/day filters [C01]")
    s += stack("f2", "Section results, plain-text times,\\nseats, conflicts, prereq status\\n[C02 C03 C04 C06 C13]  L2")
    s += panel("f3", "Inline details + Add [C08]\\nor Join waitlist [C05]")
    s += page("sched", "My Schedule\\nL1", "1")
    s += panel("s1", "Pending vs Registered [C12]\\nDrop button [C10]")
    s += panel("s2", "Week view [C11]")
    s += page("s3", "Register for N classes [C09]\\nthen Registration results L2")
    s += page("deg", "My Degree\\nL1", "1")
    s += panel("d1", "Progress by requirement [C07]\\nMissing prerequisites [C06]")
    s += page("money", "Finances\\nL1", "1")
    s += panel("m1", "What I owe + Pay [C18]\\nHolds [C16]")
    s += panel("m2", "Tuition and drop rules [C15]")
    s += '  home -> h1 [style=dotted, arrowhead=none]; h1 -> h2 [style=invis]; h2 -> h3 [style=invis];\n'
    s += e("home", "find") + e("home", "sched") + e("home", "deg") + e("home", "money")
    s += e("find", "f1") + e("find", "f2") + e("f2", "f3")
    s += e("sched", "s1") + e("sched", "s2") + e("sched", "s3")
    s += e("deg", "d1") + e("money", "m1") + e("money", "m2")
    s += '  legend [shape=plaintext, style="", fontsize=11, label="Stacked box = one page per section. Rounded gray = panel on the parent page, not a separate page.\\nContextual links (breadcrumbs, Review and register, Find sections, See other sections) are listed in the report."];\n'
    s += '  m2 -> legend [style=invis];\n'
    s += '  u1 -> home [style=invis];\n'
    s += "}\n"
    return s


for name, src in (("sitemap_current", current()), ("sitemap_revised", revised())):
    (HERE / f"{name}.dot").write_text(src)
    subprocess.run(["dot", "-Tsvg", str(HERE / f"{name}.dot"), "-o", str(HERE / f"{name}.svg")], check=True)
    subprocess.run(["dot", "-Gdpi=170", "-Tpng", str(HERE / f"{name}.dot"), "-o", str(HERE / f"{name}.png")], check=True)
print("sitemaps built")

"""Generate the two user flow diagrams (SVG and PNG) with Graphviz.

Notation: oval = start/end, rectangle = screen (with wireframe ID),
diamond = decision, rounded gray box = system response.
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).parent

HEAD = """digraph G {
  graph [rankdir=TB, fontname="Inter", fontsize=20, labelloc=t, nodesep=0.45, ranksep=0.45, pad=0.3, bgcolor="white"];
  node  [fontname="Inter", fontsize=12, color="#1a1a1a", penwidth=1.4, margin="0.18,0.08"];
  edge  [fontname="Inter", fontsize=11, color="#1a1a1a", penwidth=1.2, arrowsize=0.8];
"""

def start(i, t): return f'  {i} [shape=oval, style=filled, fillcolor="#1a1a1a", fontcolor="white", label="{t}"];\n'
def screen(i, t): return f'  {i} [shape=box, style=filled, fillcolor="#DCE9F7", label="{t}"];\n'
def decide(i, t): return f'  {i} [shape=diamond, style=filled, fillcolor="#FFF4CC", label="{t}", margin="0.05,0.05"];\n'
def system(i, t): return f'  {i} [shape=box, style="rounded,filled,dashed", fillcolor="#EEEEEE", label="{t}"];\n'
def e(a, b, lbl=""): return f'  {a} -> {b}' + (f' [label=" {lbl} "]' if lbl else "") + ";\n"

LEGEND = """  subgraph cluster_legend {
    label="Key"; fontsize=12; style=rounded; color="#888888";
    k1 [shape=oval, style=filled, fillcolor="#1a1a1a", fontcolor="white", label="Start / End", fontsize=10];
    k2 [shape=box, style=filled, fillcolor="#DCE9F7", label="Screen (wireframe ID)", fontsize=10];
    k3 [shape=diamond, style=filled, fillcolor="#FFF4CC", label="Decision", fontsize=10, margin="0.02,0.02"];
    k4 [shape=box, style="rounded,filled,dashed", fillcolor="#EEEEEE", label="System response", fontsize=10];
    k1 -> k2 -> k3 -> k4 [style=invis];
  }
"""

def flow_a():
    s = HEAD + '  label="Flow A: Find a section that fits my schedule\\n ";\n'
    s += start("s", "Student wants a class\\nthat fits around work")
    s += screen("w1", "W1 Registration Home")
    s += screen("w2", "W2 Find Classes\\nEnter subject, pick time of day\\nand days filters")
    s += system("r1", "Results list sections with days and\\ntimes in plain text, open seats,\\nprerequisite status, conflict flags.\\nStatus message announces count.")
    s += decide("d1", "Any section\\nfit my times?")
    s += system("r2", "No results message suggests\\nwidening the time filter")
    s += decide("d2", "Conflict flag\\non section?")
    s += screen("w3", "W3 Section details\\n(Details expanded inline)")
    s += decide("d3", "Seats open?")
    s += system("r3", "Added to My Schedule as\\nPending, not registered yet.\\nSidebar calendar updates.")
    s += decide("d4", "Add another\\nclass?")
    s += start("end", "Go to Flow B:\\nreview and register")
    s += start("wl", "Join waitlist\\n(Flow B, step W5)")
    s += e("s", "w1") + e("w1", "w2", "Find Classes in global nav") + e("w2", "r1", "Search")
    s += e("r1", "d1") + e("d1", "r2", "No") + e("r2", "w2", "Change filters")
    s += e("d1", "d2", "Yes") + e("d2", "r1", "Yes, pick another") + e("d2", "w3", "No")
    s += e("w3", "d3") + e("d3", "wl", "No") + e("d3", "r3", "Yes, Add to my schedule")
    s += e("r3", "d4") + e("d4", "w2", "Yes") + e("d4", "end", "No, Review and register")
    s += LEGEND + "}\n"
    return s

def flow_b():
    s = HEAD + '  label="Flow B: Check eligibility, then register and submit\\n ";\n'
    s += start("s", "Student has classes\\npicked out")
    s += screen("w1", "W1 Registration Home")
    s += decide("d0", "Registration\\nopen and\\nno holds?")
    s += system("r0", "Home shows my registration\\ndate and any holds, with\\nwho to contact")
    s += start("e0", "Come back on\\nregistration date")
    s += screen("w2", "W2 Find Classes\\nresult shows prerequisite status")
    s += decide("d1", "Prerequisites\\nmet?")
    s += screen("w6", "W6 My Degree\\nmissing prerequisite highlighted")
    s += decide("d6", "Take the\\nprerequisite\\ninstead?")
    s += start("e6", "Contact advisor\\n(utility nav)")
    s += system("r1", "Added as Pending,\\nnot registered yet")
    s += screen("w4", "W4 My Schedule review\\nPending and Registered shown\\nseparately, drop rule next to button")
    s += system("r4", "Button reads\\nRegister for 2 classes")
    s += system("r5", "System registers each class.\\nFocus moves to results heading.\\nSummary read as an alert.")
    s += decide("d5", "Every class\\nregistered?")
    s += screen("w5", "W5 Registration results")
    s += decide("d7", "Join\\nwaitlist?")
    s += system("r7", "Waitlist position shown\\nin My Schedule")
    s += start("e1", "Registered.\\nSee My Schedule")
    s += e("s", "w1") + e("w1", "d0") + e("d0", "r0", "No") + e("r0", "e0")
    s += e("d0", "w2", "Yes") + e("w2", "d1") + e("d1", "w6", "No, See my degree progress")
    s += e("w6", "d6") + e("d6", "w2", "Yes, Find classes\\nfor this requirement") + e("d6", "e6", "Unsure")
    s += e("d1", "r1", "Yes, Add") + e("r1", "w4", "Review and register") + e("w4", "r4") + e("r4", "r5", "Activate button")
    s += e("r5", "d5") + e("d5", "e1", "Yes") + e("d5", "w5", "No, a section is full")
    s += e("w5", "d7") + e("d7", "r7", "Yes") + e("d7", "w2", "No, choose another section") + e("r7", "e1")
    s += LEGEND + "}\n"
    return s

for name, src in (("flow_A_find_fitting_section", flow_a()), ("flow_B_eligibility_and_register", flow_b())):
    (HERE / f"{name}.dot").write_text(src)
    for fmt in ("svg", "png"):
        args = ["dot", f"-T{fmt}", str(HERE / f"{name}.dot"), "-o", str(HERE / f"{name}.{fmt}")]
        if fmt == "png":
            args.insert(1, "-Gdpi=170")
        subprocess.run(args, check=True)
print("flows built")

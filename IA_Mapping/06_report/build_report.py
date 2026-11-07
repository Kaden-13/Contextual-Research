"""Assemble Phase2_IA_Blueprint.pdf from the markdown source plus generated assets.

Fills the <!-- PLACEHOLDER --> blocks, converts to HTML with pandoc, and prints a tagged,
bookmarked PDF with headless Chrome.
"""
import asyncio, json, subprocess
from pathlib import Path

HERE = Path(__file__).parent
IA = HERE.parent
md = (HERE / "Phase2_IA_Blueprint.md").read_text()
fills = json.loads((HERE / "fills.json").read_text()) if (HERE / "fills.json").exists() else {}

WF = [
    ("W1", "W1_registration_home", "Registration Home",
     "Answers the three questions students had to hunt for in Phase 1: when can I register, do I have holds, and what is my status. The drop rule appears here in one plain sentence instead of legal text.",
     "Registration Home wireframe with three cards for registration date, holds, and my classes, a Next steps list, and a drop rule notice. Annotations show 20 tab stops and the header, utility navigation, primary navigation, main, and footer landmarks."),
    ("W2", "W2_find_classes", "Find Classes",
     "Each section shows days and times in bold plain text, location, open seats, and prerequisite status in one row. Time of day filters support Flow A. Conflicts are flagged before Add. The My Schedule sidebar always shows what is pending.",
     "Find Classes wireframe with a search form including time of day checkboxes, three section results for CS 2420 showing times, seats, and prerequisite status, one flagged as a time conflict and one full with a Join waitlist button, and a My Schedule sidebar. Annotations show 31 tab stops, the search, region, and complementary landmarks, aria-current on Find Classes, aria-expanded on Details buttons, and a polite status region for the result count."),
    ("W3", "W3_section_details_added", "Find Classes after Add",
     "After Add, a status message says plainly that the class is not registered yet and links to Review and register. Details expand inline with a plain definition of CRN.",
     "Find Classes wireframe after adding Section 001: a status message reads CS 2420 Section 001 added to My Schedule, not registered yet, with a Review and register link. Section 001 details are expanded showing instructor, CRN with a What is this button, linked lab, and credits. Annotations show aria-expanded true and role status with aria-live polite."),
    ("W4", "W4_my_schedule_review", "My Schedule review",
     "Pending and Registered are separate tables with plain headings. The drop rule sits directly above the button, which says exactly what it will do: Register for 2 classes. Drop is a visible button, not a dropdown.",
     "My Schedule wireframe with a Pending, not registered yet table holding two classes with Remove buttons, a dashed drop rule notice, a Register for 2 classes button, a Registered table with a Drop button, and a week view grid. Annotations show 21 tab stops and labelled region landmarks."),
    ("W5", "W5_registration_results", "Registration results",
     "Focus moves to this heading after Register. The alert summarizes the outcome, and the full section error names the problem and offers two ways forward.",
     "Registration results wireframe with an alert reading 1 of 2 classes registered, a Registered section for CS 2420, and a Not registered section explaining that MATH 1210 Section 002 filled up, with Join waitlist and See other MATH 1210 sections buttons. Annotations show role alert."),
    ("W6", "W6_my_degree_prereq", "My Degree",
     "Brings CatTracks style progress into the same navigation. When a prerequisite is missing, the row links straight to sections of the course the student needs.",
     "My Degree wireframe with a status notice that CS 3100 needs CS 2420 first, and a requirements table where the CS 2420 row reads Not started, needed for CS 3100, with a Find sections of CS 2420 link. Annotations show 18 tab stops and a role status notice."),
]

wf_md = []
for i, (sid, f, title, why, alt) in enumerate(WF):
    wf_md.append(f"### {sid}: {title}\n\n{why}\n\n![{alt}](../04_wireframes/exports/{f}_annotated.png)\n\n*Figure {7 + i}. {sid} {title}, annotated.*\n")
md = md.replace("<!-- WIREFRAMES -->", "\n".join(wf_md))

tab = json.loads((IA / "05_semantic_html" / "tab_order_W2.json").read_text())
rows = ["| # | Element | Landmark | ARIA |", "| --- | --- | --- | --- |"]
for n, name, el, land, aria in tab:
    rows.append(f"| {n} | {name} ({el.split('[')[0]}) | {land or 'skip link'} | {('`' + aria + '`') if aria else ''} |")
md = md.replace("<!-- TAB_W2 -->", "*Table: W2 Find Classes, 31 tab stops*\n\n" + "\n".join(rows))

PENDING = '<div class="pending">Waiting on card sort data.</div>'
for key in ("SUMMARY_FINDINGS", "METHOD_PARTICIPANTS", "RESULTS", "REFLECTION_1"):
    md = md.replace(f"<!-- {key} -->", fills.get(key, PENDING))

(HERE / "_build.md").write_text(md)
subprocess.run(["pandoc", str(HERE / "_build.md"), "-s", "--css", "report.css", "--metadata", "title=Phase 2 Information Architecture Blueprint",
                "-o", str(HERE / "_build.html"), "--resource-path", str(HERE)], check=True)
html = (HERE / "_build.html").read_text()
# pandoc adds its own title block; drop it, the cover page carries the title
import re
html = re.sub(r'<header id="title-block-header">.*?</header>', "", html, flags=re.S)
(HERE / "_build.html").write_text(html)


async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page()
        await pg.goto((HERE / "_build.html").resolve().as_uri())
        await pg.wait_for_timeout(300)
        await pg.pdf(path=str(HERE / "Phase2_IA_Blueprint.pdf"), format="Letter", print_background=True,
                     margin={"top": "0.8in", "bottom": "0.8in", "left": "0.85in", "right": "0.85in"},
                     tagged=True, outline=True, display_header_footer=True,
                     header_template="<span></span>",
                     footer_template='<div style="font:10px Inter,Arial;color:#333;width:100%;text-align:center">Phase 2 IA Blueprint, Kaden Donaldson, page <span class="pageNumber"></span> of <span class="totalPages"></span></div>')
        await b.close()

asyncio.run(pdf())
print("built", HERE / "Phase2_IA_Blueprint.pdf")

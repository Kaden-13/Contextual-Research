"""Build the wireframe screens as semantic HTML, then export clean and annotated PNGs.

Navigation labels live in NAV and UTILITY so they can be updated from the card sort results.
Usage: python3 build_wireframes.py
"""
import asyncio
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "src"
OUT = HERE / "exports"
TERM = "Spring 2027"

# Primary (global) navigation: key, label. Labels come from card sort clusters.
NAV = [
    ("home", "Registration Home"),
    ("find", "Find Classes"),
    ("schedule", "My Schedule"),
    ("degree", "My Degree"),
    ("money", "Finances"),
]
UTILITY = ["Help and Glossary", "Contact My Advisor", "Sign Out"]
NAV_HREF = {k: f"{k}.html" for k, _ in NAV}
PENDING = 2


def shell(screen_id, title, active, crumbs, main, aside="", extra_head=""):
    nav_items = []
    for key, label in NAV:
        cur = ' aria-current="page"' if key == active else ""
        badge = f' <span class="badge" aria-hidden="true">{PENDING}</span><span class="sr-only"> ({PENDING} pending)</span>' if key == "schedule" else ""
        nav_items.append(f'<li><a href="{NAV_HREF[key]}"{cur}>{label}{badge}</a></li>')
    util = "".join(f'<li><a href="#">{u}</a></li>' for u in UTILITY)
    crumb_html = ""
    if crumbs:
        items = []
        for i, (label, href) in enumerate(crumbs):
            if i == len(crumbs) - 1:
                items.append(f'<li><a href="{href}" aria-current="page">{label}</a></li>')
            else:
                items.append(f'<li><a href="{href}">{label}</a></li>')
        crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
    aside_html = f'<aside aria-labelledby="aside-h">{aside}</aside>' if aside else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {TERM} Registration | Weber State</title>
<link rel="stylesheet" href="wireframe.css">{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site">
  <div class="logo" aria-hidden="true">LOGO</div>
  <a class="site-title" href="home.html">Weber State Registration</a>
  <button class="term-switch" aria-haspopup="listbox" aria-expanded="false">{TERM} &#9662;</button>
  <nav class="utility" aria-label="Utility"><ul>{util}</ul></nav>
</header>
<nav class="primary" aria-label="Primary"><ul>{"".join(nav_items)}</ul></nav>
{crumb_html}
<div class="layout">
<main id="main" tabindex="-1">
{main}
</main>
{aside_html}
</div>
<footer class="site"><span>Weber State University Registrar</span><a href="#">Accessibility</a><a href="#">Registration deadlines</a><a href="#">Contact the Registrar</a></footer>
<script src="annotate.js"></script>
</body>
</html>
"""


SCHEDULE_ASIDE = f"""
<h2 id="aside-h">My Schedule</h2>
<p class="muted" style="margin:0 0 8px">{PENDING} pending, not registered yet</p>
<ul class="plain">
  <li><strong>CS 2420</strong> Tue/Thu 9:00 to 10:20 AM <span class="flag">Pending</span></li>
  <li><strong>MATH 1210</strong> Mon/Wed 1:30 to 2:20 PM <span class="flag">Pending</span></li>
  <li><strong>ENGL 2010</strong> Online <span class="flag">Registered</span></li>
</ul>
<p style="margin:12px 0 4px"><strong>10 credit hours</strong> (limit 20)</p>
<a class="btn primary" href="schedule.html" style="margin-top:8px">Review and register ({PENDING})</a>
"""


def find_results(expanded=False, toast=False):
    toast_html = ""
    if toast:
        toast_html = ('<div class="toast" role="status" aria-live="polite">CS 2420 Section 001 added to My Schedule. '
                      '<strong>Not registered yet.</strong> <a href="schedule.html">Review and register</a></div>')
    details = ""
    if expanded:
        details = """
      <div class="details" id="det-001">
        <dl class="facts">
          <dt>Instructor</dt><dt>Course number (CRN)</dt><dt>Linked lab</dt><dt>Credits</dt>
          <dd>Placeholder Name</dd><dd>31045 <button aria-describedby="crn-def" style="padding:0 6px;font-size:13px">What is this?</button></dd><dd>CS 2420L Section 001, Fri 10:00 AM</dd><dd>4</dd>
        </dl>
        <p class="hint" id="crn-def">CRN is the 5 digit number the registrar uses for one specific section.</p>
      </div>"""
    added_btn = ('<button aria-disabled="true" style="border-style:dashed">Added (pending)<span class="sr-only">: CS 2420 Section 001, not registered yet</span></button>' if toast else
                 '<button class="primary">Add to my schedule<span class="sr-only">: CS 2420 Section 001</span></button>')
    return f"""
<h1>Find Classes</h1>
{toast_html}
<form role="search" aria-label="Class search" class="card">
  <div class="form-grid">
    <div><label for="subj">Subject</label><select id="subj"><option>Computer Science (CS)</option></select></div>
    <div><label for="num">Course number</label><input id="num" type="text" value="2420" aria-describedby="num-hint"><p class="hint" id="num-hint">For example 2420</p></div>
    <fieldset><legend>Time of day</legend>
      <span class="opt"><input type="checkbox" id="t1" checked><label for="t1">Morning</label></span>
      <span class="opt"><input type="checkbox" id="t2"><label for="t2">Afternoon</label></span>
      <span class="opt"><input type="checkbox" id="t3" checked><label for="t3">Evening</label></span></fieldset>
    <fieldset><legend>Show</legend>
      <span class="opt"><input type="checkbox" id="open" checked><label for="open">Only open sections</label></span></fieldset>
  </div>
  <div class="row" style="margin-top:12px"><button class="primary" type="submit">Search</button><a href="#">More filters (days, campus, online)</a></div>
</form>
<section aria-labelledby="res-h">
  <h2 id="res-h">CS 2420 Data Structures</h2>
  <p role="status" aria-live="polite" class="muted">3 sections found</p>

  <article class="card" aria-labelledby="s1-title">
    <h3 id="s1-title">Section 001</h3>
    <dl class="facts">
      <dt>Days and times</dt><dt>Where</dt><dt>Seats</dt><dt>Prerequisites</dt>
      <dd><strong>Tue/Thu 9:00 to 10:20 AM</strong></dd><dd>Ogden campus, Noorda Engineering 301</dd><dd>12 of 30 open</dd><dd>CS 1410: Met &#10003;</dd>
    </dl>
    <div class="row">{added_btn}
      <button aria-expanded="{'true' if expanded else 'false'}" aria-controls="det-001">{'Hide details' if expanded else 'Details'}<span class="sr-only"> for Section 001</span></button></div>
    {details or '<div id="det-001" hidden></div>'}
  </article>

  <article class="card" aria-labelledby="s2-title">
    <h3 id="s2-title">Section 002 <span class="flag warn" id="s2-conf">Time conflict with MATH 1210</span></h3>
    <dl class="facts">
      <dt>Days and times</dt><dt>Where</dt><dt>Seats</dt><dt>Prerequisites</dt>
      <dd><strong>Mon/Wed 1:30 to 2:50 PM</strong></dd><dd>Ogden campus, Noorda Engineering 210</dd><dd>4 of 30 open</dd><dd>CS 1410: Met &#10003;</dd>
    </dl>
    <div class="row"><button aria-describedby="s2-conf">Add to my schedule<span class="sr-only">: CS 2420 Section 002</span></button><button aria-expanded="false" aria-controls="det-002">Details<span class="sr-only"> for Section 002</span></button></div><div id="det-002" hidden></div>
  </article>

  <article class="card" aria-labelledby="s3-title">
    <h3 id="s3-title">Section 601 <span class="flag">Full</span></h3>
    <dl class="facts">
      <dt>Days and times</dt><dt>Where</dt><dt>Seats</dt><dt>Prerequisites</dt>
      <dd><strong>Online, no set meeting time</strong></dd><dd>Online</dd><dd>0 of 40 open, 3 on waitlist</dd><dd>CS 1410: Met &#10003;</dd>
    </dl>
    <div class="row"><button>Join waitlist<span class="sr-only">: CS 2420 Section 601</span></button><button aria-expanded="false" aria-controls="det-601">Details<span class="sr-only"> for Section 601</span></button></div><div id="det-601" hidden></div>
  </article>
</section>"""


W1 = f"""
<h1>{TERM} Registration</h1>
<div class="grid3">
  <section class="card" aria-labelledby="h-date"><h2 id="h-date">Your registration date</h2><p><strong>Monday, November 9 at 8:00 AM</strong></p><p class="muted">Registration is open for you now.</p></section>
  <section class="card" aria-labelledby="h-holds"><h2 id="h-holds">Holds</h2><p><strong>No holds</strong> on your account.</p><a href="#">What is a hold?</a></section>
  <section class="card" aria-labelledby="h-status"><h2 id="h-status">My classes</h2><p><strong>1 registered, {PENDING} pending</strong></p><a href="schedule.html">Review and register</a></section>
</div>
<section class="card" aria-labelledby="h-next"><h2 id="h-next">Next steps</h2>
  <ol><li><a href="find.html">Find classes</a> and add them to your schedule.</li>
  <li><a href="degree.html">Check your degree progress</a> to see which requirements are left.</li>
  <li><a href="schedule.html">Review and register.</a> Classes are not yours until you register.</li></ol></section>
<div class="notice"><strong>Before you register:</strong> Weber State does not drop you for not paying or not attending. If you won't take a class, drop it yourself. <a href="money.html">Tuition and drop deadlines</a></div>
"""

W4 = f"""
<h1>My Schedule: review and register</h1>
<section aria-labelledby="h-pend" class="card">
  <h2 id="h-pend">Pending: not registered yet ({PENDING})</h2>
  <table><caption class="muted" style="text-align:left;padding-bottom:6px">These classes are saved but you do not have a seat yet.</caption>
    <thead><tr><th scope="col">Class</th><th scope="col">Days and times</th><th scope="col">Seats</th><th scope="col">Action</th></tr></thead>
    <tbody>
      <tr><th scope="row">CS 2420 Data Structures, Section 001</th><td>Tue/Thu 9:00 to 10:20 AM</td><td>12 open</td><td><button aria-label="Remove CS 2420 from pending">Remove</button></td></tr>
      <tr><th scope="row">MATH 1210 Calculus I, Section 002</th><td>Mon/Wed 1:30 to 2:20 PM</td><td>1 open</td><td><button aria-label="Remove MATH 1210 from pending">Remove</button></td></tr>
    </tbody></table>
  <div class="notice" id="drop-rule"><strong>Drop rule:</strong> Weber State does not drop you for not paying or not attending. You will be charged for every class you are registered in until you drop it.</div>
  <div class="row"><button class="primary" aria-describedby="drop-rule">Register for {PENDING} classes</button><a href="find.html">Add another class</a></div>
</section>
<section aria-labelledby="h-reg" class="card">
  <h2 id="h-reg">Registered (1)</h2>
  <table><thead><tr><th scope="col">Class</th><th scope="col">Days and times</th><th scope="col">Action</th></tr></thead>
    <tbody><tr><th scope="row">ENGL 2010 Intermediate Writing, Section 601</th><td>Online</td><td><button aria-label="Drop ENGL 2010">Drop</button></td></tr></tbody></table>
</section>
<section aria-labelledby="h-week" class="card">
  <h2 id="h-week">Week view</h2>
  <table class="cal"><caption class="muted" style="text-align:left;padding-bottom:6px">Striped = pending, solid = registered</caption>
    <thead><tr><th scope="col">Time</th><th scope="col">Mon</th><th scope="col">Tue</th><th scope="col">Wed</th><th scope="col">Thu</th><th scope="col">Fri</th></tr></thead>
    <tbody>
      <tr><th scope="row">9 AM</th><td></td><td class="pend">CS 2420</td><td></td><td class="pend">CS 2420</td><td></td></tr>
      <tr><th scope="row">10 AM</th><td></td><td class="pend">CS 2420</td><td></td><td class="pend">CS 2420</td><td></td></tr>
      <tr><th scope="row">1 PM</th><td class="pend">MATH 1210</td><td></td><td class="pend">MATH 1210</td><td></td><td></td></tr>
      <tr><th scope="row">2 PM</th><td class="pend">MATH 1210</td><td></td><td class="pend">MATH 1210</td><td></td><td></td></tr>
    </tbody></table>
  <p class="muted" style="margin:8px 0 0">Online classes: ENGL 2010 (registered)</p>
</section>
"""

W5 = """
<h1 tabindex="-1">Registration results</h1>
<div class="status" role="alert">1 of 2 classes registered. 1 class needs your attention.</div>
<section aria-labelledby="h-ok" class="card">
  <h2 id="h-ok">Registered</h2>
  <p><strong>CS 2420 Data Structures, Section 001</strong>, Tue/Thu 9:00 to 10:20 AM <span class="flag">Registered</span></p>
</section>
<section aria-labelledby="h-fail" class="card">
  <h2 id="h-fail">Not registered</h2>
  <p><strong>MATH 1210 Calculus I, Section 002</strong>: <span id="full-msg">This section filled up before you registered. You can join the waitlist (you would be number 4) or choose another section.</span></p>
  <div class="row"><button class="primary" aria-describedby="full-msg">Join waitlist for MATH 1210</button><a class="btn" href="find.html">See other MATH 1210 sections</a></div>
</section>
<p><a href="schedule.html">Back to My Schedule</a></p>
"""

W6 = """
<h1>My Degree</h1>
<p class="muted">Bachelor of Science, Computer Science. 64 of 120 credits complete.</p>
<div class="notice" role="status">You can't register for <strong>CS 3100</strong> yet. You still need <strong>CS 2420</strong> first.</div>
<section aria-labelledby="h-core" class="card">
  <h2 id="h-core">Computer Science core</h2>
  <table><thead><tr><th scope="col">Requirement</th><th scope="col">Status</th><th scope="col">Next step</th></tr></thead>
  <tbody>
    <tr><th scope="row">CS 1400 Fundamentals of Programming</th><td>Complete &#10003;</td><td></td></tr>
    <tr><th scope="row">CS 1410 Object Oriented Programming</th><td>Complete &#10003;</td><td></td></tr>
    <tr><th scope="row">CS 2420 Data Structures</th><td><strong>Not started. Needed for CS 3100</strong></td><td><a href="find.html">Find sections of CS 2420</a></td></tr>
    <tr><th scope="row">CS 3100 Operating Systems</th><td>Not started</td><td>Take CS 2420 first</td></tr>
  </tbody></table>
</section>
<section aria-labelledby="h-help" class="card"><h2 id="h-help">Not sure what to take?</h2><a href="#">Contact my advisor</a></section>
"""

SCREENS = [
    ("W1_registration_home", "home", "Registration Home", "home", [], W1, ""),
    ("W2_find_classes", "find", "Find Classes", "find", [("Registration Home", "home.html"), ("Find Classes", "find.html")], find_results(), SCHEDULE_ASIDE),
    ("W3_section_details_added", "find_added", "Find Classes", "find", [("Registration Home", "home.html"), ("Find Classes", "find.html")], find_results(expanded=True, toast=True), SCHEDULE_ASIDE),
    ("W4_my_schedule_review", "schedule", "My Schedule", "schedule", [("Registration Home", "home.html"), ("My Schedule", "schedule.html")], W4, ""),
    ("W5_registration_results", "results", "Registration Results", "schedule", [("Registration Home", "home.html"), ("My Schedule", "schedule.html"), ("Results", "results.html")], W5, ""),
    ("W6_my_degree_prereq", "degree", "My Degree", "degree", [("Registration Home", "home.html"), ("My Degree", "degree.html")], W6, ""),
]


def write_html():
    for name, file_key, title, active, crumbs, main, aside in SCREENS:
        (SRC / f"{file_key}.html").write_text(shell(name, title, active, crumbs, main, aside))


async def export():
    from playwright.async_api import async_playwright
    OUT.mkdir(exist_ok=True)
    counts = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1280, "height": 800})
        for name, file_key, *_ in SCREENS:
            url = (SRC / f"{file_key}.html").resolve().as_uri()
            await pg.goto(url)
            await pg.screenshot(path=str(OUT / f"{name}.png"), full_page=True)
            await pg.goto(url + "?annotate")
            await pg.wait_for_timeout(150)
            counts[name] = await pg.evaluate("window.__tabCount")
            await pg.screenshot(path=str(OUT / f"{name}_annotated.png"), full_page=True)
        await b.close()
    return counts


if __name__ == "__main__":
    write_html()
    print(asyncio.run(export()))

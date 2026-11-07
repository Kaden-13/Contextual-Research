---
title: "Phase 2 Information Architecture Blueprint: Weber State University Class Registration"
author: Kaden Donaldson
date: November 6, 2026
lang: en-US
---

<div class="cover">

# Phase 2 Information Architecture Blueprint {.cover-title}

**Weber State University Class Registration**

Kaden Donaldson
Human Computer Interaction
November 6, 2026

GitHub repository: <https://github.com/Kaden-13/Contextual-Research> (see the `IA_Mapping` directory)

</div>

## 1. Summary

Phase 1 showed that Weber State students do not experience class registration as one system. To register for one class, a student moves through the eWeber portal, a semester and tuition agreement page, a term picker, the three pane Register for Classes page, CatTracks in a separate tab for prerequisites, and often an advisor. The deepest path to a section's details is 7 levels.

This phase tested how students actually group registration tasks with an open card sort, then rebuilt the structure around their groups.

<!-- SUMMARY_FINDINGS -->

**The revised Information Architecture (IA)** puts every task at most 2 levels from Registration Home, under 5 primary navigation items. It brings eligibility and degree progress into the same system, separates pending classes from registered ones, and keeps the tuition and drop rule next to the Register button instead of hiding it before class selection.

Two critical flows from Phase 1 were redesigned and wireframed across 6 screens: **finding a section that fits a schedule** and **checking eligibility, then registering**. Every wireframe is built as semantic HTML and annotated with its exact keyboard tab order and ARIA landmarks, roles, and states.

## 2. Card Sorting Study

### 2.1 Card Deck

I pulled 20 cards from the Phase 1 audit. Each one is a task a student does around registration, and each traces back to a Phase 1 finding (`card_deck.csv`, column `phase1_source`).

Cards use plain student language ("Add a class to my list") instead of system names ("Summary pane," "CRN lookup"), and they avoid repeating keywords, so participants would group by meaning instead of matching words.

| ID | Card | Phase 1 source |
| --- | --- | --- |
| C01 | Search for a class by subject or course number | Task T1, HE09 |
| C02 | Compare sections of the same class | Task T2, HE06 |
| C03 | See what days and times a class meets | Theme 1, HE13 |
| C04 | Check how many seats are open | HE05 |
| C05 | Join a waitlist for a full class | HE02, HE05 |
| C06 | Check if I meet the prerequisites | Theme 2, HE14 |
| C07 | See my progress toward my degree | Theme 2 (CatTracks) |
| C08 | Add a class to my list | Theme 3, HE01 |
| C09 | Submit my registration | Theme 3, HE01, HE04 |
| C10 | Drop a class | HE08 |
| C11 | See my weekly schedule | Weekly calendar (works well) |
| C12 | See which classes I'm actually registered for | HE01, HE10 |
| C13 | Find out if two classes overlap | Time Conflict warning (works well) |
| C14 | Choose a semester | Term selection step |
| C15 | Read the tuition and drop rules | HE03 |
| C16 | Check for holds on my account | Registration home |
| C17 | Find out when I'm allowed to register | Registration home |
| C18 | Pay tuition or see what I owe | HE03, drop policy |
| C19 | Get in touch with my advisor | Theme 4 |
| C20 | Look up what a term means (like CRN) | HE07 |

### 2.2 Method

**Sort type: open.** Participants created and named their own groups. Phase 1 found that students do not think of CatTracks, Register for Classes, and tuition as separate tools, so a closed sort using the current menu names would have assumed the very structure being questioned.

<!-- METHOD_PARTICIPANTS -->

**Analysis.** Results were entered into `raw_data/card_sort_results.csv`, one row per card per participant. A Python script (`analyze_card_sort.py`) builds a similarity matrix showing the percent of participants who placed each pair of cards in the same group. It then runs average linkage hierarchical clustering to produce a cluster diagram, and cuts the tree at 50% agreement to define consensus clusters.

### 2.3 Results

<!-- RESULTS -->

::: landscape
## 3. Revised Sitemap and IA Blueprint

### 3.1 Current Structure

![Current IA of Weber State class registration, drawn from the Phase 1 audit. A chain of 7 levels runs from the eWeber portal through Registration home, Select the Semester with the tuition agreement, Term selection, and the Register for Classes page to the Find Classes pane, search results, and section details. Schedule Builder, CatTracks, tuition and payment, and the advisor sit outside the chain as separate systems.](../02_sitemap/sitemap_current.png)

*Figure 3. Current IA. Dashed yellow boxes are separate systems the student has to leave registration to use.*
:::

::: landscape
### 3.2 Revised Structure

![Revised IA. Registration Home at the top shows registration date, holds, and class status. Below it are 4 primary sections: Find Classes (search and filters, section results, inline details with Add or Join waitlist), My Schedule (pending versus registered with Drop, week view, Register for N classes and results), My Degree (progress and missing prerequisites), and Finances (what I owe and pay, holds, tuition and drop rules). A global navigation band shows the header bar with the semester switcher and utility links for Help and Glossary, Contact My Advisor, and Sign Out. Each box lists the card IDs it serves.](../02_sitemap/sitemap_revised.png)

*Figure 4. Revised IA. Card IDs in brackets show which card sort items each page serves.*
:::

**Notation.** Solid boxes are pages. The double-bordered box is a set of similar pages (one result per section). Rounded gray boxes are panels on their parent page, not separate pages. Purple boxes are global elements on every page.

### 3.3 Navigation Hierarchy

| Level | Element | Items |
| --- | --- | --- |
| Primary (global) | Horizontal nav bar under the header, on every page | Registration Home, Find Classes, My Schedule (with pending count), My Degree, Finances |
| Secondary (in page) | Section headings and panels inside each primary page; no sub-menus | Find Classes: search, results, details. My Schedule: Pending, Registered, Week view. Finances: what I owe, holds, tuition and drop rules |
| Utility (global) | Right side of the header bar | Help and Glossary, Contact My Advisor, Sign Out |
| Global control | Header bar | Semester switcher (replaces the separate term selection page) |

### 3.4 Reducing Depth

| Task | Current depth | Revised depth | How |
| --- | --- | --- | --- |
| See a section's meeting times | 7 (portal, reg home, semester, term, Register for Classes, results, details) | 2 (Find Classes, results with times shown) | Semester moved to a header switcher; times shown in each result instead of a details view |
| Check prerequisites | Leave the system (CatTracks tab or advisor) | 1 to 2 (status on each result; My Degree for detail) | Prerequisite status in results; degree progress is a primary nav item |
| Confirm what I'm registered for | Read the Summary pane's pending vs registered labels | 1 (My Schedule) | Pending and Registered are separate, labelled tables |
| Find the drop rule | Read legal text before choosing classes | 0 (next to the Register button) and 1 (Finances) | Repeated at the moment of decision |

No primary item has a sub-menu. Anything that used to be a pane, tab, or extra page is now a labelled section inside one primary page, which removes the nested levels that caused the novice participant in Phase 1 to ask "Why do I have to click so many buttons."

### 3.5 Global and Contextual Navigation

**Global navigation (every page):**

| Element | Purpose |
| --- | --- |
| Skip link | First tab stop; jumps to `<main>` |
| Header bar | Home link, semester switcher, utility nav |
| Primary nav bar | The 5 top level sections; current page marked with `aria-current="page"` and a thick underline |
| Pending count badge | Shows how many classes are added but not registered, on every page |
| Footer | Accessibility statement, registration deadlines, contact the Registrar |

**Contextual navigation (where it is needed):**

| Element | Where | Goes to |
| --- | --- | --- |
| Breadcrumb | Every page below Home | Back up the path, for example Registration Home / My Schedule / Results |
| My Schedule sidebar with "Review and register (2)" | Find Classes | My Schedule review |
| "Review and register" link in the Add confirmation | Find Classes after Add | My Schedule review |
| "Find sections of CS 2420" | My Degree, missing requirement row | Find Classes filtered to that course |
| "See other MATH 1210 sections" | Registration results, full section | Find Classes for that course |
| "Join waitlist" | Full sections and the results page | Adds to waitlist, shown in My Schedule |
| "What is this?" | Next to CRN in section details | Inline definition |
| "Contact my advisor" | My Degree help section | Advisor contact |

## 4. User Flows

I chose the two flows that caused the most trouble in Phase 1.

**Flow A, finding a section that fits a schedule,** was the only task a participant could not finish alone. The novice needed help finding class times, and the experienced student called it the hardest task.

**Flow B, checking eligibility and then registering,** combines the two costliest problems: prerequisites living in a separate tool, and Add not actually registering the student.

![Flow A diagram. Start: student wants a class that fits around work. W1 Registration Home leads through Find Classes in the global nav to W2 Find Classes, where the student enters a subject and picks time of day and days filters. The system lists sections with plain text times, seats, prerequisite status, and conflict flags, and announces the count. Decision: does any section fit? If no, a no results message suggests widening the filter. If yes, decision: is there a conflict flag? If yes, pick another. If no, W3 section details. Decision: seats open? If no, join waitlist. If yes, Add to my schedule, and the system shows Added as pending, not registered yet, and updates the sidebar calendar. Decision: add another class? Yes loops back to W2; no goes to Flow B.](../03_user_flows/flow_A_find_fitting_section.png)

*Figure 5. Flow A: Find a section that fits my schedule.*

![Flow B diagram. Start: student has classes picked out. W1 Registration Home, decision: registration open and no holds? If no, Home shows the registration date and holds with who to contact; end. If yes, W2 Find Classes shows prerequisite status. Decision: prerequisites met? If no, W6 My Degree highlights the missing prerequisite, then decision: take the prerequisite instead? Yes returns to Find Classes; unsure ends at Contact advisor. If prerequisites are met, Add as pending, then Review and register leads to W4 My Schedule review, where pending and registered are shown separately with the drop rule next to the button. The button reads Register for 2 classes. The system registers each class, moves focus to the results heading, and reads the summary as an alert. Decision: every class registered? Yes ends registered. No, a section is full, leads to W5 Registration results, decision: join waitlist? Yes shows waitlist position in My Schedule; no returns to Find Classes to choose another section.](../03_user_flows/flow_B_eligibility_and_register.png)

*Figure 6. Flow B: Check eligibility, then register and submit.*

### Phase 1 Problems Each Flow Fixes

| Phase 1 finding | Where the flow fixes it |
| --- | --- |
| Theme 1 / HE13: can't find class times | Flow A, W2: days and times are the first, bold fact in every result |
| Theme 2 / HE14: prerequisites live in CatTracks | Flow B, W2 and W6: prerequisite status on each result; My Degree one click away |
| Theme 3 / HE01: Add looks like registering | Both flows: "Added, not registered yet" status; separate Pending table; button names the count |
| HE02: full class error is vague | Flow B, W5: names the full section and offers waitlist or other sections |
| HE03: drop rule buried | Flow B, W4: drop rule right next to the Register button and linked to it with `aria-describedby` |
| A01: keyboard users can't reach Add | All screens: Add is a real `<button>` in normal tab order |

## 5. Wireframes

All 6 screens are medium fidelity grayscale wireframes built in HTML and CSS (`IA_Mapping/04_wireframes/src`). Building them as real HTML means the semantic structure and tab order in Section 6 come straight from the markup instead of being drawn by hand. Clean and annotated exports of every screen are in `04_wireframes/exports`.

**How to read the annotations:**

* **Red numbered circles** show keyboard tab order.
* **Colored dashed outlines** with a tag show each landmark and its role.
* **Yellow tags** show ARIA states and live regions.

<!-- WIREFRAMES -->

## 6. Accessibility First: Semantic Structure and Keyboard Plan

### 6.1 Semantic HTML Skeleton

Every screen shares this landmark structure. Only `<main>` and the optional `<aside>` change.

```html
<body>
  <a class="skip" href="#main">Skip to main content</a>
  <header class="site">                         <!-- banner -->
    <a href="home.html">Weber State Registration</a>
    <button aria-haspopup="listbox" aria-expanded="false">Spring 2027</button>
    <nav aria-label="Utility">...</nav>          <!-- navigation -->
  </header>
  <nav aria-label="Primary">...</nav>            <!-- navigation -->
  <nav aria-label="Breadcrumb"><ol>...</ol></nav><!-- navigation -->
  <main id="main" tabindex="-1">                 <!-- main -->
    <h1>Find Classes</h1>
    <form role="search" aria-label="Class search">...</form>
    <section aria-labelledby="res-h">...</section>   <!-- region -->
  </main>
  <aside aria-labelledby="aside-h">...</aside>   <!-- complementary -->
  <footer class="site">...</footer>              <!-- contentinfo -->
</body>
```

| Screen | Landmarks | Labelled regions |
| --- | --- | --- |
| W1 Registration Home | banner, 2 navigation, main, contentinfo | Registration date, Holds, My classes, Next steps |
| W2 and W3 Find Classes | banner, 3 navigation, search, main, complementary, contentinfo | Search results |
| W4 My Schedule | banner, 3 navigation, main, contentinfo | Pending, Registered, Week view |
| W5 Registration results | banner, 3 navigation, main, contentinfo | Registered, Not registered |
| W6 My Degree | banner, 3 navigation, main, contentinfo | Computer Science core, Help |

Each `<nav>` has a unique `aria-label`, so a screen reader's landmark list reads "Utility, Primary, Breadcrumb" instead of three identical "navigation" entries. Every page has one `<h1>`, and headings never skip levels.

### 6.2 Keyboard Tab Order

Tab order follows DOM order, and no positive `tabindex` values are used, so visual order, reading order, and focus order always match (WCAG 2.4.3). The full sequence for all 6 screens is in `05_semantic_html/tab_order.md`. Here is the sequence for the most complex screen:

<!-- TAB_W2 -->

The sequence keeps every page the same up to stop 13 (skip link, header, utility, primary nav, breadcrumb). A keyboard user learns it once, or skips it with stop 1. Inside `<main>`, the order matches how a student works: filters, then Search, then each result's Add and Details in the order they appear. The My Schedule sidebar comes after the results, so the "Review and register" action is the natural next stop once the student is done adding classes.

### 6.3 ARIA Roles, States, and Properties

| Attribute | Where | Purpose | WCAG |
| --- | --- | --- | --- |
| `aria-current="page"` | Active primary nav link, last breadcrumb | Announces where the user is | 1.3.1, 2.4.8 |
| `aria-expanded` + `aria-controls` | Semester switcher, every Details button | Announces open or closed and what it controls | 4.1.2 |
| `aria-haspopup="listbox"` | Semester switcher | Warns that a list will open | 4.1.2 |
| `role="status"` + `aria-live="polite"` | Result count (W2), "Added, not registered yet" (W3), prerequisite notice (W6) | Announces changes without moving focus | 4.1.3 |
| `role="alert"` | Registration summary (W5) | Immediately announces "1 of 2 classes registered" | 4.1.3, 3.3.1 |
| `aria-describedby` | Course number hint, CRN definition, Register button (drop rule), conflicting Add button (conflict flag), Join waitlist (full message) | Reads the hint or warning with the control | 3.3.2 |
| Visually hidden text in buttons | "Add to my schedule: CS 2420 Section 001", "Details for Section 002" | Every repeated button gets a unique name | 2.4.6, 2.5.3 |
| `aria-disabled="true"` | "Added (pending)" on W3 | Shows the button is used up without dropping keyboard focus | 2.4.3 |
| `tabindex="-1"` | `<main>`, W5 `<h1>` | Target for the skip link and post-submit focus, without adding a tab stop | 2.4.1, 2.4.3 |

### 6.4 Focus Management

| Action | Focus goes to | Screen reader hears |
| --- | --- | --- |
| Skip to main content | `<main>` | The page's `<h1>` |
| Add to my schedule | Stays on the button, now "Added (pending)" | "CS 2420 Section 001 added to My Schedule. Not registered yet." |
| Details | Stays on the button | "expanded" or "collapsed" |
| Register for 2 classes | W5 `<h1>` | "1 of 2 classes registered. 1 class needs your attention." |

I used `aria-disabled` instead of the `disabled` attribute on the "Added" button on purpose. A truly disabled button loses focus, which would throw a keyboard user back to the top of the page right after adding a class. That is the same kind of failure Phase 1 found (A01).

## 7. Post-Mortem Reflection

### 7.1 How did the card sort data challenge my initial assumptions?

<!-- REFLECTION_1 -->

### 7.2 How do the ARIA landmarks and tab sequence give screen reader users the same efficiency as sighted users?

A sighted student glances at the page and knows three things right away: where they are, where the main content starts, and what changed after they clicked something. My annotations are meant to give a screen reader user those same three things without reading every word.

**Where am I?** Sighted users see the underline on the active nav item and the breadcrumb. Screen reader users hear "current page" on that same link, because of `aria-current="page"`. Each `<nav>` has its own label (Utility, Primary, Breadcrumb), so the landmarks list is a real map of the page, not three identical "navigation" entries.

**Getting to the content.** A sighted user skips the header with their eyes. A keyboard or screen reader user gets the same shortcut from the skip link (stop 1) or by jumping straight to the `main` or `search` landmark. Because the revised IA is flat, with 5 primary items and no sub-menus, there are no nested menus to open and close. Any task is at most two landmark or link jumps from wherever the user is. In the current system, a keyboard user could not even reach the Add buttons.

**Knowing what happened.** This was the biggest problem in Phase 1. Sighted students missed that Add only made a class pending, and a screen reader user would have had even less to go on. In the redesign:

* Adding a class triggers a polite status message: "Added to My Schedule. Not registered yet."
* Registering moves focus to the results heading and reads the summary as an alert.
* The drop rule is tied to the Register button with `aria-describedby`, so it is read at the exact moment of decision, not buried in legal text before class selection.

**Repeated controls.** A sighted user can tell which "Add" belongs to which section by position. A screen reader user browsing a list of buttons can't. Visually hidden text gives each button a unique name, like "Add to my schedule: CS 2420 Section 001," so the button list is usable on its own.

**Order.** Because the tab order is the DOM order, and the DOM order matches the visual layout, a screen reader user and a sighted user move through the page in the same sequence. Nobody gets surprised by focus jumping somewhere unexpected.

## 8. Documentation and Repository

All raw data and assets are in the `IA_Mapping` directory of <https://github.com/Kaden-13/Contextual-Research>.

| Folder | Contents |
| --- | --- |
| `01_card_sort` | Card deck (CSV and printable PDF), facilitator protocol, raw participant data, analysis script, similarity matrix, cluster diagram, consensus summary |
| `02_sitemap` | Current and revised sitemaps (SVG, PNG, and Graphviz source) |
| `03_user_flows` | Flow A and Flow B (SVG, PNG, and source) |
| `04_wireframes` | HTML and CSS wireframe source, annotation script, clean and annotated PNG exports |
| `05_semantic_html` | Landmark map, ARIA plan, and full tab order for every screen |
| `06_report` | This report's source and PDF |

Every diagram and table can be rebuilt from the raw data with the scripts in each folder.

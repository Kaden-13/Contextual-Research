# Phase 1 Usability Audit Report: Draft

Final file: `Phase1_Usability_Audit.pdf`

Everything below is written and ready to paste into Word or Google Docs. Text in **[brackets]** still needs your session results. Figure notes in *italics* say which screenshot goes where and give alt text to paste in.

---

## Cover Page

**Phase 1 Usability Audit: Weber State University Class Registration**
Kaden Donaldson
Human Computer Interaction
[Date]
GitHub repository: https://github.com/Kaden-13/Contextual-Research

---

## 1. Executive Summary

This audit evaluated the Register for Classes app in Weber State University's eWeber portal, the tool students use to find, compare, and add classes each semester. Registration is high stakes: a mistake can cost a seat, a semester, or tuition money, yet the interface makes students work around it rather than with it.

The audit combined a contextual inquiry with 2 students (one new to registration, one experienced), an expert review against Nielsen's 10 Usability Heuristics, and a WCAG 2.1 AA accessibility audit using WAVE and manual testing.

**The most serious findings:**
1. **A keyboard only user cannot register.** Pressing Tab skips every listed class and every Add button (WCAG 2.1.1, severity 4).
2. **Clicking Add does not register you.** Add only places a class in a pending list, and nothing is registered until a separate Submit button in the far corner is clicked (H1, H5).
3. **Errors don't explain themselves.** Trying to add a full class produces a vague error that never says the class is full or what to do next (H9, WCAG 3.3.3).
4. **The page where students choose classes is the least accessible page in the flow.** Once search results load, WAVE errors jump from 3 to 23, contrast errors from 1 to 89, and the AIM Score drops from 8.7 to 2.5 out of 10.

[One or two sentences on what the sessions showed, for example how many tasks each participant finished on their own and the biggest theme.]

**Overall accessibility result:** The registration flow **fails** WCAG 2.1 AA.

**Fix first:** Make every Add button reachable and visible by keyboard, and clearly separate "pending" from "registered." Those two changes remove the biggest legal risk and the most costly student mistake.

> **Callout: Key numbers**
> * 12 heuristic issues, 4 rated major (severity 3)
> * 12 WCAG 2.1 AA findings, 1 rated severity 4
> * WAVE AIM Score on the search results page: **2.5 / 10**
> * Lowest measured contrast: **1.07:1** (requirement is 4.5:1)
> * [Task completion: X of 6 tasks completed without help]

---

## 2. Problem Statement and Context of Use

Weber State University students register for classes through the eWeber portal, using either the Register for Classes (Add/Drop) app or the Registration Schedule Builder. This audit focuses on the Register for Classes app: the path a student follows to find a class, compare sections, confirm eligibility, and add a class to their schedule.

The primary users are Weber State undergraduates. Many are traditional students between 18 and 24, but a large share are working, commuting, or returning students who register in short sessions between jobs and other obligations, often on a phone. The system also needs to serve students who rely on screen readers, magnification, or keyboard only navigation.

Registration is time sensitive and high stakes. Seats in popular sections fill quickly, and a wrong choice can delay graduation. Weber State also does not drop students for nonpayment or nonattendance, so a student who believes they dropped or never registered for a class can still be charged. When the interface relies on registrar codes, spreads key information across the page, or explains errors in system terms, students lose time, make costly mistakes, or give up and turn to an advisor or friend. For the university, that means more load on advising and the registrar, slower progress toward degrees, and legal exposure under the ADA and Section 504 if the system is not accessible.

**Core tasks evaluated**
1. Find a class of the participant's choosing
2. Compare sections by time, delivery method, and open seats
3. Confirm eligibility and locate how to add a section
4. Recover from registration errors (evaluator review)

---

## 3. Methodology

This audit combined three methods so that findings from one could be checked against the others.

**Contextual inquiry.** I observed 2 Weber State students using their own devices and accounts: one who was new to the registration system (P1) and one who had registered many times (P2). Choosing opposite ends of experience made it possible to compare what blocks a first time user with what an experienced user has learned to work around. Each participant completed 3 realistic tasks while thinking aloud, then answered short follow up questions. Sessions were not audio or screen recorded. Instead, I took live notes on task completion, time on task, wrong turns, hesitations, workarounds, and word for word quotes, then cleaned them up the same day. So that no one's real schedule changed, sessions were a mock run: participants searched current semester classes and showed how they would add a section, but did not actually add or submit anything. The full script is in `02_user_research/interview_protocol.md`, and notes are in `02_user_research/raw_notes/`.

**Synthesis.** I broke the notes into individual observations and grouped them through affinity mapping into themes, giving the most weight to problems both participants hit or that the heuristic evaluation confirmed (`02_user_research/synthesis/affinity_themes.md`).

**Heuristic evaluation.** I walked through each screen of the flow against Nielsen's 10 Usability Heuristics, used browser DevTools to inspect buttons, styles, and network calls, and rated every issue from 0 (not a problem) to 4 (usability catastrophe) based on frequency, impact, and persistence (`03_heuristic_evaluation/heuristic_evaluation_log.md`).

**Accessibility audit.** I scanned 5 pages of the flow with the WAVE browser extension, then manually tested color contrast (SC 1.4.3), keyboard access and visible focus (SC 2.1.1 and 2.4.7), zoom at 200% and 400% (SC 1.4.4 and 1.4.10), and semantic structure and ARIA support (`04_accessibility_audit/wcag_audit_checklist.md`).

**Limitations.** With only 2 participants, both of whom I know personally, the research shows the kinds of problems students run into, not how often they occur across all students. Participants who know the researcher may also soften criticism, so I emphasized that the system was being tested, not them. The evaluation was done by a single evaluator. Because nothing was actually submitted, the final registration step, system behavior under heavy load, and real seat competition were not observed; the full class error is based on my own past registration experience.

---

## 4. User Research Findings

[Fill in from your session notes. I can write this section once you send them.]

### Participants

| ID | Experience | Year | Device |
| --- | --- | --- | --- |
| P1 | Novice, [registered X times] | [ ] | [ ] |
| P2 | Experienced, [many semesters] | [ ] | [ ] |

### Task Results

| Task | P1 (novice) | P2 (experienced) |
| --- | --- | --- |
| T1: Find a class | [Y / A / N, time] | [ ] |
| T2: Choose a section that fits a schedule | [ ] | [ ] |
| T3: Check eligibility and find how to add | [ ] | [ ] |
| Ease rating (1 to 5) | [ ] | [ ] |

Y = completed alone, A = completed with assist, N = did not complete

### Themes

[3 to 5 themes, each with a heading, a short description, a quote callout, and the mental model mismatch.]

> **Callout: In their words**
> "[quote]" (P1)
> "[quote]" (P2)

---

## 5. Heuristic Evaluation Findings

### The Mental Model Gap

Students approach registration like an online shopping cart or seat reservation: find the class, click Add, and it's yours. The system works differently, and most major issues come from that gap.

| Students expect | What the system actually does |
| --- | --- |
| Clicking Add reserves my seat. | Add only places the class in the Summary as pending. Nothing is registered until Submit. |
| I can quickly see if a section has room. | Seat counts are shown, but every section also shows a waitlist line, even when seats are open. |
| If a class is full, the system tells me and shows my options. | A vague error appears that doesn't say the class is full. |
| Dropping a class is a visible button. | Drops are hidden in an Action dropdown, then confirmed with Submit. |
| Not attending or not paying cancels a class. | Nothing is dropped automatically; the student is still charged. |

### Severity Scale

| Rating | Meaning |
| --- | --- |
| 0 | Not a usability problem |
| 1 | Cosmetic |
| 2 | Minor, low priority |
| 3 | Major, high priority |
| 4 | Usability catastrophe |

### Major Issues (Severity 3)

**HE01: Add looks like registering, but it isn't** (H1 Visibility of system status, H5 Error prevention)
Clicking Add only moves a class into the Summary as pending. DevTools showed Add and Submit call different server endpoints, and nothing is registered until the student clicks Submit in the far bottom right corner of the page. A student can close the page believing they're registered when they're not.
*Recommendation:* Label the list "Pending, not registered yet," and make the button say exactly what it does, such as "Register for 2 classes."

**HE02: The full class error doesn't say the class is full** (H9 Help users recognize, diagnose, and recover from errors)
When I tried to add a full class, the system showed a vague error that never mentioned the class was full. I couldn't tell whether to retry, choose another section, or join a waitlist.
*Recommendation:* "This section is full. Join the waitlist or choose another section."

**HE03: The tuition warning is buried and shown only once** (H5 Error prevention)
Weber State doesn't drop students for nonpayment or nonattendance. That warning appears once, inside several paragraphs of legal text on the Select the Semester page, before the student picks any classes, and isn't repeated near Submit.
*Recommendation:* Repeat a short, plain language drop warning right next to the Submit button.

*Figure: `S2_wave_tuition_agreement.png`, cropped to the text blocks. Alt text: "Select the Semester page showing three long blocks of legal text, including the statement that WSU does not drop courses for nonpayment or nonattendance." Mark the "does not drop courses" sentence with marker 1.*

**HE12: Zooming in hides content and the Add button** (H7 Flexibility and efficiency of use)
At 200% zoom the results table header and many values are clipped. At 400%, seat counts can't be read and the Add button is cut off.
*Recommendation:* Use a layout that stacks on narrow screens.

### Minor Issues (Severity 2)

| ID | Heuristic | Issue | Recommendation |
| --- | --- | --- | --- |
| HE04 | H1, H9 | Submit is disabled with no explanation of why. | "Add a class to enable registration." |
| HE05 | H8 | A waitlist line ("100 of 100 waitlist seats") shows on every section, even ones with open seats. | Show waitlist details only when a section is full. |
| HE06 | H8 | Table text is cut off even on a full screen, while large areas of the page sit empty. | Rebalance panes and let cells wrap. |
| HE07 | H2 | Jargon like CRN, Linked Sections, Attribute, and Schedule Type is never explained. | Use plain labels or inline definitions. |
| HE08 | H6, H4 | Dropping a class is hidden in an Action dropdown. | Use a visible Drop button. |
| HE09 | H10 | No format hints on the search form; help is behind a small info icon. | Add hints under each label. |
| HE10 | H6 | Students must remember CRNs, pending vs. registered status, and outside approval steps. | Keep pending and registered visibly separate. |
| HE11 | H8 | Add is at the top, results at the bottom, and Submit in the far corner, all in 10 to 12 px text. | Confirm next to Add; use 16 px text. |

*Figure: clean screenshot of the Register for Classes page with search results (WAVE off), Summary blurred. Markers: 1 waitlist line on an open section (HE05), 2 jargon column headers (HE07), 3 Add button (HE01), 4 Submit button in the corner (HE01, HE11). Alt text: "Register for Classes search results with numbered markers on the waitlist line, the CRN and Schedule Type column headers, the Add button, and the Submit button in the bottom right corner."*

### What Works

* Green "Registered" labels give clear status after Submit succeeds.
* The weekly calendar shows how classes fit together and makes time conflicts visible.
* The breadcrumb shows where the student is in the process.
* The Total Hours line helps students stay under the 20 credit maximum.

---

## 6. Accessibility Audit Findings

> **Callout: Can a keyboard only user register for a class?**
> **No.** Tab skips every listed class and every Add button.

### Automated Scan (WAVE)

| Page | Errors | Contrast errors | Alerts | AIM Score |
| --- | --- | --- | --- | --- |
| Registration home | 4 | 1 | 1 | 8.5 |
| Select the Semester and tuition agreement | 0 | 0 | 9 | 9.8 |
| Term selection | 3 | 1 | 5 | 8.4 |
| Register for Classes, before searching | 3 | 1 | 71 | 8.7 |
| **Register for Classes, with search results** | **23** | **89** | **282** | **2.5** |

The pages leading up to registration score reasonably well. The moment search results load, accessibility collapses, which is exactly where students make their decisions.

*Figure: `S5_wave_search_results.png`. Marker 1 on the score panel (23 errors, 89 contrast errors, AIM 2.5), marker 2 on the 19 broken ARIA references. Alt text: "WAVE results for the search results page showing 23 errors, 89 contrast errors, 282 alerts, and an AIM Score of 2.5 out of 10. The schedule and summary panes are blurred for privacy."*

### Color Contrast (SC 1.4.3)

| Element | Ratio | Result |
| --- | --- | --- |
| Active "Schedule" tab label (white on #F7F7F7) | 1.07:1 | Fail |
| Primary buttons, light part of gradient | 2.85:1 | Fail |
| Primary buttons, middle of gradient | 4.42:1 | Fail |
| Gray banner headings on the first two screens | Flagged by WAVE | Fail |
| Body text (#333333 on white) | 12.63:1 | Pass |

### Keyboard and Focus (SC 2.1.1, 2.4.7)

Tabbing through search results skips the listed classes and their Add buttons entirely, so a keyboard user can't add a class. There is no focus indicator on those buttons, and where focus does appear, it is faint. The disabled Submit button can't be focused and gives no explanation.

### Zoom and Reflow (SC 1.4.4, 1.4.10)

At 200% zoom, the table header and values are clipped. At 400%, seat counts are unreadable and the Add button is cut off. Results grid text is only 10 to 12 px.

### Semantic Structure and ARIA (SC 1.3.1, 4.1.2)

The page sets a language and uses `<header>`, a labeled breadcrumb `<nav>`, and `<main>`. However, the three working panes have no headings or labels, the search results contain 19 broken ARIA references and 2 empty table headers, broken ARIA menus appear on nearly every page, and many form labels aren't connected to their fields.

### Findings Summary

| ID | WCAG SC | Level | Issue | Severity |
| --- | --- | --- | --- | --- |
| A01 | 2.1.1 Keyboard | A | Add buttons can't be reached by keyboard | 4 |
| A02 | 2.4.7 Focus Visible | AA | No or faint focus indicator | 3 |
| A03 | 1.4.3 Contrast | AA | Schedule tab label at 1.07:1 | 3 |
| A05 | 1.4.10 Reflow, 1.4.4 Resize | AA | Content and Add button clipped when zoomed | 3 |
| A08 | 3.3.3 Error Suggestion | AA | Full class error gives no cause or fix | 3 |
| A09 | 4.1.2, 1.3.1 | A | 19 broken ARIA references, 2 empty table headers | 3 |
| A10 | 1.4.3 Contrast | AA | 89 low contrast items on search results | 3 |
| A04 | 1.4.3 Contrast | AA | Button labels as low as 2.85:1 | 2 |
| A06 | 1.3.1, 2.4.6 | A / AA | Main panes have no headings or labels | 2 |
| A07 | 3.3.2 Labels or Instructions | A | No format hints on search fields | 2 |
| A11 | 1.4.3 Contrast | AA | Gray banner headings fail contrast | 2 |
| A12 | 1.3.1, 4.1.2 | A | Broken ARIA menus, unconnected form labels | 2 |

---

## 7. Prioritized Issues

Issues confirmed by more than one method are listed first. [After the sessions, add "Sessions" to the Source column wherever a participant ran into the issue.]

| Priority | Issue | Source | Severity | Fix |
| --- | --- | --- | --- | --- |
| 1 | Keyboard users can't reach Add buttons, with no focus indicator | Accessibility (A01, A02) | 4 | Real focusable buttons with a thick focus outline |
| 2 | Add looks like registering, but nothing is registered until Submit | Heuristic (HE01, HE04, HE11) [+ Sessions?] | 3 | "Pending" label and a button that says "Register for 2 classes" |
| 3 | Full class error doesn't explain the problem or next step | Heuristic (HE02) + Accessibility (A08) | 3 | Name the cause and next step; announce with `aria-live` |
| 4 | Content and Add button clipped when zoomed | Heuristic (HE12) + Accessibility (A05) | 3 | Responsive layout, 16 px text |
| 5 | Search results page: 19 broken ARIA references, 89 contrast errors | Accessibility (A09, A10) | 3 | Fix ARIA IDs, raise contrast to 4.5:1 |
| 6 | Tuition and drop warning buried in legal text | Heuristic (HE03) | 3 | Plain warning next to Submit |
| 7 | Waitlist noise and unexplained jargon in results | Heuristic (HE05, HE07) [+ Sessions?] | 2 | Plain seat status, plain labels |
| 8 | Hidden drop control, no form hints, unlabeled panes | Heuristic (HE08, HE09) + Accessibility (A06, A07) | 2 | Visible Drop button, hints, labeled sections |

---

## 8. Post Mortem Reflection

*These are drafts. Reword them so they sound like you.*

### Question 1: How did combining qualitative user observations with an expert heuristic evaluation reveal usability flaws that a developer testing their own code would likely overlook?

A developer testing their own code already knows what every button does. They know Add only stages a class and Submit is what registers it, they know what a CRN is, and they know where the drop control is hidden. Because they built the mental model, they can't experience the gap between what the screen shows and what a student expects. [Describe one moment from the sessions, for example: "P1 clicked Add and said '...', assuming she was registered."] Watching someone without that knowledge made the gap visible in a way that reading the code never would.

The heuristic evaluation caught a different set of problems: the ones users work around without saying anything. [Example: "P2 scrolled past the waitlist line without comment, but the evaluation flagged it as noise that slows every decision (HE05)."] Experienced users blame themselves or quietly adapt, so their sessions can look smooth while the interface is still costing them time. Going screen by screen against the heuristics, and testing with a keyboard, zoom, and WAVE, exposed issues no participant would think to mention, like the Add buttons being unreachable by keyboard.

Each method also confirmed the other. [Name the issue both methods found, for example the Add versus Submit split.] Seeing the same problem from a real user and from a structured review gave me much more confidence that it was a real priority and not just my opinion.

### Question 2: Identify one heuristic violation that directly creates a legal or ethical accessibility barrier under WCAG 2.1 AA, and explain how resolving that violation improves the user experience for both disabled users and the general public.

The clearest example is the full class error (HE02), which violates Nielsen's ninth heuristic, help users recognize, diagnose, and recover from errors. When I tried to add a full class, the system showed a vague message that never said the class was full or what to do next. Under WCAG 2.1 AA, this fails SC 3.3.3 Error Suggestion, which requires that when an error is detected and a fix is known, the fix is offered to the user. The system clearly knows the reason, because it rejected the request, but it doesn't share it.

For a screen reader user, this is more than an annoyance. Combined with the missing live region announcements and broken ARIA references on the results page, they may not even notice an error appeared, let alone figure out why. A student with a cognitive disability may not be able to work out the cause on their own. Because Weber State is a public university covered by the ADA and Section 504, a registration process that some students can't complete independently is a legal risk, and ethically, it means those students depend on someone else to do something every other student does alone.

Fixing it helps everyone. An error that says "This section is full. Join the waitlist or choose another section," announced with an `aria-live` region, tells a screen reader user exactly what happened, but it also saves every student from guessing, retrying, or emailing an advisor. Better yet, showing seat status in plain words before the student clicks prevents the error entirely. That's the pattern I saw across this audit: changes made for accessibility, like clear messages, visible focus, and layouts that reflow when zoomed, end up making the system faster and less stressful for all students.

---

## Formatting Checklist for the PDF

The assignment requires the PDF itself to be accessible.

* [ ] Real heading styles (Heading 1, 2, 3), not just bold text
* [ ] Body text at least 11pt, dark text on a light background
* [ ] Callout boxes meet 4.5:1 contrast (for example, dark text on a pale blue box)
* [ ] Every screenshot has alt text (provided above)
* [ ] Screenshot markers use numbers, not just color
* [ ] Tables have header rows marked as headers
* [ ] Document title and language set in file properties
* [ ] Exported as a tagged PDF (Word: File, Save As, PDF, Options, check "Document structure tags for accessibility")
* [ ] GitHub repository link included and the repo is shared with the instructor

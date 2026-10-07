# Phase 1 Usability Audit Report: Outline and Draft

Final file: `Phase1_Usability_Audit.pdf`

Sections marked **[DRAFTED]** are written and ready to edit. Sections marked **[AFTER RESEARCH]** depend on your sessions and audits.

---

## Cover Page [DRAFTED]

**Phase 1 Usability Audit: Weber State University Class Registration**
Kaden Donaldson
Human Computer Interaction
[Date]
GitHub repository: https://github.com/Kaden-13/Contextual-Research

---

## 1. Executive Summary [AFTER RESEARCH]

One page or less. Write this last.

* One sentence on what was audited and why
* How the audit was done (3 users, 10 heuristics, WCAG 2.1 AA)
* The 3 most severe findings, each in one sentence
* Overall accessibility result
* One sentence on what should be fixed first

> **Callout box idea:** "Key numbers" showing task completion rate, average time on Task 2, number of severity 3 and 4 issues, and number of WCAG failures.

---

## 2. Problem Statement and Context of Use [DRAFTED]

Weber State University students register for classes through the eWeber portal, using either the Register for Classes (Add/Drop) app or the Registration Schedule Builder. This audit focuses on the Register for Classes app, the path a student follows to find a course, compare sections, confirm eligibility, and add a class to their schedule.

The primary users are Weber State undergraduates. Many are traditional students between 18 and 24, but a large share are working, commuting, or returning students who register in short sessions between jobs and other obligations, often on a phone. The system also needs to serve students who rely on screen readers, magnification, or keyboard only navigation.

Registration is time sensitive and high stakes. Seats in popular sections fill quickly, and a wrong choice can delay graduation. When the interface relies on registrar codes, spreads key information across screens, or explains errors in system terms, students lose time, register for the wrong section, or give up and turn to an advisor or friend. For the university, that means more load on advising and the registrar, slower progress toward degrees, and legal exposure under the ADA and Section 504 if the system is not accessible.

**Core tasks evaluated**
1. Find a specific course
2. Compare sections by time, delivery method, and open seats
3. Confirm eligibility (prerequisites, restrictions, holds)
4. Locate how to add a section (adding was unavailable during this mock run)
5. Recover from registration errors

---

## 3. Methodology [DRAFTED]

This audit combined three methods so that findings from one could be checked against the others.

**Contextual inquiry.** I observed 2 Weber State students using their own devices and accounts: one who was new to the registration system and one who had registered many times. Choosing opposite ends of experience made it possible to compare what blocks a first time user with what an experienced user has learned to work around. Each participant completed 3 realistic tasks while thinking aloud, then answered short follow up questions. Sessions were not audio or screen recorded. Instead, I took live notes on task completion, time on task, wrong turns, hesitations, workarounds, and word for word quotes, then cleaned them up the same day. Because the study ran outside the registration window, sessions were a mock run: participants searched current semester classes and showed how they would add a section, but the system did not allow adding. The full script is in `02_user_research/interview_protocol.md`, and unedited notes are in `02_user_research/raw_notes/`.

**Synthesis.** I broke the notes into individual observations and grouped them through affinity mapping into themes, giving the most weight to problems both participants hit or that the heuristic evaluation confirmed (`02_user_research/synthesis/affinity_themes.md`).

**Heuristic evaluation.** I walked through each screen of the flow against Nielsen's 10 Usability Heuristics and rated every issue from 0 (not a problem) to 4 (usability catastrophe) based on frequency, impact, and persistence (`03_heuristic_evaluation/heuristic_evaluation_log.md`).

**Accessibility audit.** I scanned each page with axe DevTools and WAVE, then manually tested color contrast (SC 1.4.3), keyboard access and visible focus (SC 2.1.1 and 2.4.7), and semantic structure and ARIA support (`04_accessibility_audit/wcag_audit_checklist.md`).

**Limitations.** With only 2 participants, both of whom I know personally, the research shows the kinds of problems students run into, not how often they occur across all students. Participants who know the researcher may also soften criticism, so I emphasized that the system was being tested, not them. The evaluation was done by a single evaluator, and testing happened outside the registration window, so the final add and submit steps, system behavior under heavy load, and real seat competition could not be observed.

---

## 4. User Research Findings [AFTER RESEARCH]

* Participant overview table (P1 and P2: year, registration experience, device)
* Task results table (completion and time per task)
* 3 to 5 themes, each with:
  * Theme name as a heading
  * Short description
  * 1 or 2 direct quotes in a callout box
  * Mental model mismatch ("expected X, got Y")
  * Annotated screenshot of the breakdown point

---

## 5. Heuristic Evaluation Findings [AFTER RESEARCH]

* Severity scale table
* Summary table: issues per heuristic and highest severity
* Detailed write up of each severity 3 and 4 issue with an annotated screenshot and recommendation
* Short table of the remaining severity 1 and 2 issues

---

## 6. Accessibility Audit Findings [AFTER RESEARCH]

* Automated scan summary table by page
* Color contrast results (include actual ratios)
* Keyboard and focus results
* Semantic structure and ARIA results
* Findings table with WCAG success criterion, who is affected, and recommendation

> **Callout box idea:** "Can a keyboard only user register?" with a clear yes or no.

---

## 7. Prioritized Issues [AFTER RESEARCH]

Combine everything into one table, ordered by severity, showing where each issue came from (user sessions, heuristic evaluation, accessibility audit, or more than one). Issues confirmed by more than one method go at the top.

---

## 8. Post Mortem Reflection [AFTER RESEARCH]

Write these in first person after the research is done. Aim for 1 to 2 solid paragraphs each.

### Question 1
*How did combining qualitative user observations with an expert heuristic evaluation reveal usability flaws that a developer testing their own code would likely overlook?*

Points to cover:
* A developer already knows the codes, the screen order, and what each button does, so they can't experience the confusion a new user has. Name a specific moment where a participant got stuck on something that looks obvious once you know it.
* The heuristic evaluation catches problems users work around without mentioning, because they assume it's their fault. Name one issue you found in the evaluation that participants never complained about but clearly struggled with.
* User sessions catch problems no heuristic predicted, especially ones tied to real context like work schedules or phones. Name one.
* Close with how the two methods confirmed each other on your top issue.

### Question 2
*Identify one heuristic violation that directly creates a legal or ethical accessibility barrier under WCAG 2.1 AA, and explain how resolving that violation improves the user experience for both disabled users and the general public.*

Pick the strongest real example from your audit. Common pairings to look for:
* **H9 (error recovery) and SC 3.3.1 Error Identification:** errors shown only by color or a vague message
* **H1 (visibility of system status) and SC 4.1.3 Status Messages:** "added to cart" feedback that is not announced to screen readers
* **H4 (consistency) or H8 (minimalist design) and SC 2.4.7 Focus Visible:** focus outlines removed for visual style
* **H2 (match real world) and SC 1.4.3 Contrast:** low contrast status labels like "Full" or "Waitlist"

Structure: name the heuristic, name the WCAG criterion, describe exactly what you observed, explain who is blocked and why that is a legal and ethical problem, then explain how the fix also helps everyone (for example, a visible focus ring helps power users and people on laptops without a mouse; a clear error message helps every student, not just screen reader users).

---

## Formatting Checklist for the PDF

The assignment requires the PDF itself to be accessible.

* [ ] Real heading styles (Heading 1, 2, 3), not just bold text
* [ ] Body text at least 11pt, dark text on a light background
* [ ] Callout boxes meet 4.5:1 contrast
* [ ] Every screenshot has alt text
* [ ] Annotations on screenshots don't rely on color alone (use numbers or labels too)
* [ ] Tables have header rows marked as headers
* [ ] Document title and language set in file properties
* [ ] Exported as a tagged PDF (Word: File, Save As, PDF, Options, check "Document structure tags for accessibility")
* [ ] Checked with Adobe Acrobat's Accessibility Checker or a similar tool
* [ ] GitHub repository link included and the repo is shared with the instructor

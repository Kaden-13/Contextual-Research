# Heuristic Evaluation: Nielsen's 10 Usability Heuristics

**Evaluator:** Kaden Donaldson
**Date(s):** October 2026
**System:** eWeber portal, Register for Classes app
**Browser / device:** Desktop browser, full screen, plus 200% and 400% zoom tests
**Term used for testing:** Fall 2026

## Method

I walked through the Register for Classes flow one screen at a time, checking each screen against all 10 heuristics. I also used browser DevTools to inspect buttons and styles, and drew on my own past experience registering. Every issue has an ID and a severity rating, and screenshots are saved in `screenshots/raw/`.

### Page Layout

Register for Classes is one page with three panes: **Find Classes** on top, the weekly **Schedule** on the bottom left, and the **Summary** on the bottom right. Adding a class is a two stage process: **Add** puts the class in the Summary as pending, and nothing is registered until **Submit** is clicked.

### Flow Steps Evaluated

| Step | Screen |
| --- | --- |
| S1 | eWeber portal home, locating the Register for Classes app |
| S2 | Tuition agreement |
| S3 | Term selection |
| S4 | Find Classes search form (subject, course number, keyword, campus, building) |
| S5 | Search results list |
| S6 | Section details (meeting times, seats, waitlist) |
| S7 | Add button and the Summary pane |
| S8 | Submit button |
| S9 | Error messages |

### Severity Scale

| Rating | Meaning |
| --- | --- |
| 0 | Not a usability problem |
| 1 | Cosmetic. Fix only if time allows |
| 2 | Minor. Low priority fix |
| 3 | Major. Important to fix, high priority |
| 4 | Usability catastrophe. Must fix before release |

Severity considers how often the problem happens, how hard it is to overcome, and whether it keeps happening once users know about it.

## Findings Log

| ID | Step | Heuristic(s) | Issue description | Evidence | Severity | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| HE01 | S7, S8 | H1 Visibility of system status, H5 Error prevention | Clicking **Add** only puts the class in the Summary as pending. Nothing is registered until **Submit**, which sits in the far bottom right corner. It feels like a one step shopping cart, so a student can leave thinking they're registered when they aren't. | Summary pane screenshot; DevTools shows Add and Submit call different endpoints | 3 | Label the list "Pending, not registered yet" and make the button say exactly what it does, such as "Register for 2 classes." |
| HE02 | S9 | H9 Error recognition and recovery | Trying to add a full class gave a vague error that never said the class was full. I couldn't tell whether to retry, pick another section, or join a waitlist. | My own past registration attempt (could not reproduce outside registration) | 3 | Name the cause and the next step: "This section is full. Join the waitlist or choose another section." |
| HE03 | S2, S8 | H5 Error prevention | Weber State doesn't drop students for nonpayment or nonattendance, but that warning is in a tuition agreement at the bottom of the page, far from the Submit button. A wrong assumption costs real money. | Tuition agreement text; registrar's Register for Classes page | 3 | Put a short tuition and drop warning right next to the Submit button. |
| HE04 | S8 | H1 Visibility of system status, H9 Error recognition and recovery | The Submit button is disabled until something is pending, but it never says why it's disabled. | Summary pane screenshot; DevTools (button disabled state) | 2 | Show a short message, such as "Add a class to enable registration." |
| HE05 | S5, S6 | H8 Aesthetic and minimalist design | Every section shows a waitlist line (such as "100 of 100 waitlist seats") even when regular seats are open, and part of that line is cut off. It's noise around the one fact the student needs: is there a seat? | CS 4110 results screenshot | 2 | Show seat status in plain words on every result, and only show waitlist details when the section is full. |
| HE06 | S5, S7 | H8 Aesthetic and minimalist design | Text in the results and Summary tables is cut off, even with a full screen browser. Meanwhile, large areas of the page are empty and the calendar and Summary are cramped. | Full screen results and Summary screenshots | 2 | Rebalance pane sizes and let table cells wrap instead of clipping. |
| HE07 | S5, S6 | H2 Match between system and real world | Registrar jargon like **CRN**, **Linked Sections**, **Attribute**, and **Schedule Type** appears with no plain language explanation. | Results screenshot | 2 | Use plain labels ("Class number," "Required lab or discussion") or add inline definitions. |
| HE08 | S7 | H6 Recognition rather than recall, H4 Consistency and standards | Dropping a class is hidden in an **Action** dropdown on each Summary row, then confirmed with Submit, instead of a visible Drop button. | Summary pane screenshot | 2 | Use a visible Drop button on each row. |
| HE09 | S4 | H10 Help and documentation | The search form has no format hints (for example, whether Subject takes a code like "CS" or a name). The only instructions are behind a small info icon. | Search form screenshot | 2 | Add short hints under each label and connect them with `aria-describedby`. |
| HE10 | S5, S7 | H6 Recognition rather than recall | Students have to keep track of CRNs, which classes are pending versus registered, and late add approvals that happen outside the page (instructor or department Special Approval after the sixth business day). | Page review; registrar's Register for Classes page | 2 | Keep pending and registered classes visibly separate, and link to the approval process from the page. |
| HE11 | S4 to S7 | H8 Aesthetic and minimalist design | The action happens at the top (Add), the result shows at the bottom (Schedule and Summary), and the final step (Submit) is in the far bottom right. Confirming one action means scanning three areas, all in very small 10 to 12 px text. | Full page screenshot; CSS values in DevTools | 2 | Show confirmation next to the Add button, and raise body text to 16 px. |
| HE12 | S5, S7 | H7 Flexibility and efficiency of use | At 200% zoom the table header row and many values are clipped. At 400% zoom seat counts can't be read and the Add button is cut off, so anyone who zooms in can't finish the task. | 200% and 400% zoom screenshots | 3 | Use a layout that stacks on narrow screens. (Also logged as accessibility finding A05.) |

## What Works

These parts of the interface support the user and should be kept:

* **Green "Registered" labels** in the Summary give clear status once Submit succeeds (H1).
* **The weekly calendar** shows how classes fit together and makes time conflicts visible (H1, H6).
* **The breadcrumb** at the top shows where the user is in the process (H1).
* **The Total Hours line** helps students stay under the 20 credit hour maximum (H5).

## Summary

| Heuristic | Issues found | Highest severity |
| --- | --- | --- |
| H1 Visibility of system status | 2 (HE01, HE04) | 3 |
| H2 Match between system and real world | 1 (HE07) | 2 |
| H3 User control and freedom | 0 | n/a |
| H4 Consistency and standards | 1 (HE08) | 2 |
| H5 Error prevention | 2 (HE01, HE03) | 3 |
| H6 Recognition rather than recall | 2 (HE08, HE10) | 2 |
| H7 Flexibility and efficiency of use | 1 (HE12) | 3 |
| H8 Aesthetic and minimalist design | 3 (HE05, HE06, HE11) | 2 |
| H9 Error recognition and recovery | 2 (HE02, HE04) | 3 |
| H10 Help and documentation | 1 (HE09) | 2 |

**Top issues by severity:**
1. **HE01:** The Add then Submit split makes students think they're registered when they aren't.
2. **HE02:** The full class error never says the class is full or what to do next.
3. **HE03:** The no automatic drop tuition warning is far from the action that triggers it.
4. **HE12:** Content and the Add button are clipped when zoomed.

**Issues that also showed up in user sessions:** [fill in after sessions]

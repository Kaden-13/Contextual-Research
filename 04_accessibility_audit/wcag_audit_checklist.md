# Baseline Accessibility Audit (WCAG 2.1 AA)

**Auditor:** Kaden Donaldson
**Date(s):** October 2026
**System:** eWeber portal, Register for Classes app (Fall 2026 term)
**Browser:** Desktop browser, full screen, plus 200% and 400% zoom
**Tools:** WAVE browser extension, browser DevTools (inspect, computed styles, accessibility pane), contrast calculations, keyboard only testing

## Pages Tested

Register for Classes is a single page with three panes (Find Classes, Schedule, Summary), so steps S4 to S8 are all tested on the same page.

| Page | Automated scan | Manual checks |
| --- | --- | --- |
| eWeber portal home (S1) | [run WAVE] | Not tested |
| Register for Classes page (S4 to S8) | [run WAVE] | Contrast, keyboard, focus, zoom, semantic structure |

## Part 1: Automated Scan

**To do:** Click the WAVE extension icon on the Register for Classes page (with search results showing), record the numbers below, and save a screenshot of the summary panel as `scan_exports/register_wave.png`.

| Page | WAVE errors | Contrast errors | Alerts | Most notable items |
| --- | --- | --- | --- | --- |
| Register for Classes | | | | |
| Portal home (optional) | | | | |

Automated tools catch only part of the accessibility problems on a page, which is why the manual checks below were also done.

## Part 2: Manual Checks

### A. Color Contrast (SC 1.4.3, Contrast Minimum)

**Requirement:** Normal text needs at least **4.5:1**. Large text (18pt, or 14pt bold) needs at least **3:1**. Colors were taken from DevTools computed styles.

| Element | Foreground | Background | Ratio | Result |
| --- | --- | --- | --- | --- |
| Active "Schedule" tab label | White | #F7F7F7 | 1.07:1 | **Fail** |
| Primary buttons (12 px bold), light top of gradient | White | #999999 | 2.85:1 | **Fail** |
| Primary buttons, middle of gradient | White | Mid gradient | 4.42:1 | **Fail** (just under 4.5:1) |
| Primary buttons, dark bottom of gradient | White | #575757 | 7.23:1 | Pass |
| Disabled Submit button | Light text | Light gray | 1.66:1 | Exempt (WCAG doesn't require contrast for disabled controls) |
| Body text | #333333 | White | 12.63:1 | Pass |

### B. Keyboard Access and Focus Visible (SC 2.1.1 Keyboard, SC 2.4.7 Focus Visible)

**Method:** Used Tab and Shift+Tab to move through the page without a mouse.

| Check | Result | Notes |
| --- | --- | --- |
| Can every control be reached with Tab? | **No** | Focus skips the listed classes and their **Add** buttons entirely. |
| Is the focus indicator visible on every control? | **No** | No indicator on the Add buttons (they never get focus). Where focus does appear, such as a link in the Summary, the indicator is faint. |
| Can the Add and Submit buttons be used by keyboard? | **No** | Add can't be reached. The disabled Submit button can't be focused and gives no explanation. |
| Could the full task be completed by keyboard only? | **No** | A keyboard only user cannot add a class. |

### C. Zoom and Reflow (SC 1.4.4 Resize Text, SC 1.4.10 Reflow)

| Test | Result | Notes |
| --- | --- | --- |
| 200% zoom | **Fail** | The table header row and many values are clipped. |
| 400% zoom | **Fail** | Seat counts become unreadable and the Add button is cut off. |
| Base text size | Concern | Results grid text is 10 to 12 px; the footer with credit limits is the smallest text on the page. |

### D. Semantic Structure and Screen Reader Support (SC 1.3.1, SC 2.4.6, SC 3.3.2, SC 4.1.2)

**Method:** Inspected the HTML in DevTools.

| Check | Result | Notes |
| --- | --- | --- |
| Page language set? | Pass | `<html lang="en">` |
| Landmarks used? | Partial | Has `<header>`, `<nav>` labeled "Breadcrumb navigation," and `<main>`. The bottom bar is a `<div class="footer">` instead of `<footer>`. |
| Headings or labels for each working area? | **Fail** | Inside `<main>`, the search, schedule, and summary panes are plain `<div>`s with no headings or labels, so screen reader users can't jump between them. |
| Real buttons used? | Partial | Submit is a real `<button>`. The "Resize panels" handles are `<div>` elements. |
| Form fields labeled with instructions? | Partial | The search form has visible labels, but no format hints. The only instructions are behind a small info icon. |
| Status changes announced? | Not confirmed | No live region was found for added classes or errors. |
| Error messages explain the problem? | **Fail** | The full class error didn't say the class was full or suggest a fix (from past experience). |

## Findings Log

| ID | WCAG SC | Level | Issue | Who it affects | Severity | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | 2.1.1 Keyboard | A | Tab skips the listed classes and Add buttons, so a class can't be added without a mouse. | Keyboard only users, screen reader users, people with motor disabilities | 4 | Make each Add a real, focusable `<button>` in a real table so Tab reaches it. |
| A02 | 2.4.7 Focus Visible | AA | No focus indicator on the Add buttons, and a faint one elsewhere. | Keyboard users, low vision users | 3 | Add a thick, high contrast focus outline on every control. |
| A03 | 1.4.3 Contrast | AA | Active "Schedule" tab label is 1.07:1, essentially invisible. | Low vision and color blind users, anyone in glare | 3 | Use dark text on the light tab, or a dark tab background. |
| A04 | 1.4.3 Contrast | AA | Primary button labels drop to 2.85:1 over the light part of the gradient. | Low vision users | 2 | Use a solid dark button color that gives at least 4.5:1. |
| A05 | 1.4.10 Reflow, 1.4.4 Resize Text | AA | At 200% and 400% zoom, table content is clipped and the Add button is cut off. | Low vision users who zoom, phone users | 3 | Use a responsive layout that stacks on narrow screens, and 16 px base text. |
| A06 | 1.3.1 Info and Relationships, 2.4.6 Headings and Labels | A / AA | The three main panes have no headings or labels. | Screen reader users | 2 | Wrap each pane in a labeled `<section>` with a heading. |
| A07 | 3.3.2 Labels or Instructions | A | Search fields have no format hints; help is hidden behind an info icon. | Users with cognitive disabilities, new students | 2 | Put hints under labels and link them with `aria-describedby`. |
| A08 | 3.3.3 Error Suggestion | AA | The full class error doesn't name the problem or suggest a fix. | Everyone, especially screen reader and cognitive disability users | 3 | Write errors that name the cause and next step, and announce them with an `aria-live` region. |

## Summary

**Overall result:** **Fail** against WCAG 2.1 AA for the tested flow. The most important task on the page, adding a class, cannot be done by keyboard.

**Most serious barriers:**
1. **A01:** A keyboard only user cannot reach the Add buttons, so they cannot register at all.
2. **A05:** Zooming in clips content and cuts off the Add button.
3. **A03 and A08:** A nearly invisible tab label, and an error message that doesn't explain what went wrong.

**Heuristic violation linked to a WCAG failure (for reflection question 2):** HE01 and A01/A02. The registration status is already hard to see (H1, visibility of system status), and for keyboard users the Add buttons don't receive focus or show a focus indicator at all, a direct SC 2.1.1 and 2.4.7 failure.

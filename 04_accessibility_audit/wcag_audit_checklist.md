# Baseline Accessibility Audit (WCAG 2.1 AA)

**Auditor:** Kaden Donaldson
**Date(s):** October 2026
**System:** eWeber portal, Register for Classes app (Fall 2026 term)
**Browser:** Desktop browser, full screen, plus 200% and 400% zoom
**Tools:** WAVE browser extension (WebAIM), browser DevTools (inspect, computed styles, accessibility pane), contrast calculations, keyboard only testing

## Pages Tested

| Step | Page | Automated scan | Manual checks |
| --- | --- | --- | --- |
| S1 | Registration home ("What would you like to do?") | WAVE | Not tested |
| S2 | Select the Semester and tuition agreement | WAVE | Not tested |
| S3 | Term selection ("How would you like to search?") | WAVE | Not tested |
| S4 to S8 | Register for Classes, before and after a search | WAVE | Contrast, keyboard, focus, zoom, semantic structure |

## Part 1: Automated Scan (WAVE)

Each page was scanned with the WAVE browser extension. AIM Score is WebAIM's overall rating out of 10.

| Step | Page | Errors | Contrast errors | Alerts | AIM Score |
| --- | --- | --- | --- | --- | --- |
| S1 | Registration home | 4 | 1 | 1 | 8.5 |
| S2 | Select the Semester and tuition agreement | 0 | 0 | 9 | 9.8 |
| S3 | Term selection | 3 | 1 | 5 | 8.4 |
| S4 | Register for Classes, before searching | 3 | 1 | 71 | 8.7 |
| S5 | Register for Classes, with search results | **23** | **89** | **282** | **2.5** |

**Key takeaway:** The pages leading up to registration score reasonably well, but the moment search results load, errors jump from 3 to 23, contrast errors from 1 to 89, and the AIM Score drops from 8.7 to 2.5. The page where students actually choose and add classes is the least accessible part of the whole flow.

### Error details

| Page | Errors | Notable alerts |
| --- | --- | --- |
| S1 Registration home | 1 empty link, 1 broken ARIA reference, 2 broken ARIA menus; contrast error on the "What would you like to do?" banner heading | 1 redundant link |
| S2 Tuition agreement | None | Semester dropdown missing a label, skipped heading level, JavaScript jump menu, very small text, 4 layout tables |
| S3 Term selection | 1 broken ARIA reference, 2 broken ARIA menus; contrast error on the "How would you like to search?" banner heading | "Terms Open for Registration" is an orphaned form label, 3 underlined text items that aren't links |
| S4 Register for Classes, before searching | 1 empty table header, 2 broken ARIA menus | 16 orphaned form labels, 29 very small text, 18 redundant title text, skipped heading level |
| S5 Register for Classes, with results | **19 broken ARIA references**, 2 empty table headers, 2 broken ARIA menus | 89 very low contrast items across the results table |

The 2 broken ARIA menus appear on every page except the tuition agreement, so they likely come from the shared site header.

### Saved scans (`scan_exports/`)

* `S1_wave_registration_home.png`
* `S2_wave_tuition_agreement.png`
* `S3_wave_term_selection.png`
* `S5_wave_search_results.png` (Schedule and Summary panes blurred to hide personal class information)

Automated tools catch only part of the accessibility problems on a page. The keyboard failure in A01, for example, was found by hand, which is why the manual checks below were also done.

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
| A09 | 4.1.2 Name, Role, Value; 1.3.1 Info and Relationships | A | WAVE found 19 broken ARIA references and 2 empty table headers on the search results. ARIA attributes point to elements that don't exist, so screen readers can't announce what controls in each result row are, and two table columns have no header. | Screen reader users | 3 | Fix each `aria-labelledby`/`aria-describedby` to point at a real element ID, and give every column header text. |
| A10 | 1.4.3 Contrast | AA | WAVE flagged 89 very low contrast items once search results load, compared with 1 before searching. | Low vision and color blind users, anyone in glare | 3 | Retest the results table colors and raise all text to at least 4.5:1. |
| A11 | 1.4.3 Contrast | AA | The gray banner headings "What would you like to do?" and "How would you like to search?" fail contrast on the first two registration screens. | Low vision users | 2 | Use darker banner backgrounds or dark text. |
| A12 | 1.3.1 Info and Relationships, 4.1.2 Name, Role, Value | A | Broken ARIA menus (2) appear on nearly every page, and form labels aren't connected to their fields (the semester dropdown has no label; "Terms Open for Registration" is orphaned; 16 orphaned labels on the registration page). | Screen reader users | 2 | Fix the shared header menu markup and link each label to its field with `for`/`id`. |

## Summary

**Overall result:** **Fail** against WCAG 2.1 AA for the tested flow. The most important task on the page, adding a class, cannot be done by keyboard, and WAVE rates the search results page 2.5 out of 10.

**Most serious barriers:**
1. **A01:** A keyboard only user cannot reach the Add buttons, so they cannot register at all.
2. **A05:** Zooming in clips content and cuts off the Add button.
3. **A09 and A10:** 19 broken ARIA references and 89 contrast errors on the search results, the exact screen where students pick classes.
4. **A03 and A08:** A nearly invisible tab label, and an error message that doesn't explain what went wrong.

**Heuristic violation linked to a WCAG failure (for reflection question 2):** HE01 and A01/A02. The registration status is already hard to see (H1, visibility of system status), and for keyboard users the Add buttons don't receive focus or show a focus indicator at all, a direct SC 2.1.1 and 2.4.7 failure.

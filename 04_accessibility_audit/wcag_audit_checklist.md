# Baseline Accessibility Audit (WCAG 2.1 AA)

**Auditor:** Kaden Donaldson
**Date(s):**
**System:** eWeber portal, Register for Classes app
**Browser and version:**
**Tools:** axe DevTools (browser extension), WAVE (browser extension), WebAIM Contrast Checker, keyboard only testing

## Pages Tested

Use the same flow steps as the heuristic evaluation.

| Step | Page | axe run | WAVE run | Manual checks done |
| --- | --- | --- | --- | --- |
| S1 | Portal home / app launcher | | | |
| S3 | Term selection | | | |
| S4 | Class search form | | | |
| S5 | Search results | | | |
| S6 | Section details | | | |
| S7 | Add option | | | |

## Part 1: Automated Scans

### axe DevTools
1. Open the page, press F12, open the **axe DevTools** tab, and click **Scan all of my page**.
2. Record the number of issues by impact (critical, serious, moderate, minor).
3. Export or screenshot the results into `scan_exports/` (for example `S5_axe.png`).

### WAVE
1. Click the WAVE extension icon on the page.
2. Record errors, contrast errors, and alerts.
3. Screenshot the summary panel into `scan_exports/` (for example `S5_wave.png`).

| Step | axe critical | axe serious | axe moderate | WAVE errors | WAVE contrast errors | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | | | | | | |
| S3 | | | | | | |
| S4 | | | | | | |
| S5 | | | | | | |
| S6 | | | | | | |
| S7 | | | | | | |

**Remember:** automated tools catch only part of the accessibility problems on a page. The manual checks below are required.

## Part 2: Manual Checks

### A. Color Contrast (SC 1.4.3, Contrast Minimum)

**Requirement:** Normal text needs at least **4.5:1** contrast against its background. Large text (18pt, or 14pt bold) needs at least **3:1**.

**How to test:** Use the eyedropper in the WebAIM Contrast Checker or the contrast info in Chrome DevTools (inspect an element, then click the color swatch). Prioritize placeholder text, disabled buttons, links, table headers, status labels like "Open" or "Full," and text on colored banners.

| Element | Step | Foreground | Background | Ratio | Pass / Fail |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |

### B. Keyboard Access and Focus Visible (SC 2.1.1 Keyboard, SC 2.4.7 Focus Visible)

**How to test:** Put the mouse away. Starting from the top of the page, use **Tab**, **Shift+Tab**, **Enter**, **Space**, and the **arrow keys** to complete Tasks 1 to 3.

| Check | Step | Result | Notes |
| --- | --- | --- | --- |
| Is there a "Skip to main content" link? | | | |
| Can every control be reached with Tab? | | | |
| Is the focus indicator visible on every control? | | | |
| Is the tab order logical (matches visual order)? | | | |
| Can dropdowns, date pickers, and filters be used without a mouse? | | | |
| Can the Add and Submit buttons be activated by keyboard? | | | |
| Do any dialogs trap focus, or lose focus when they close? | | | |
| Could the full task be completed by keyboard only? | | | |

### C. Semantic Structure and Screen Reader Support (SC 1.3.1, SC 2.4.6, SC 4.1.2)

**How to test:** Use the WAVE **Structure** tab, the axe results, and Chrome DevTools **Accessibility** pane. Optionally do a quick pass with a screen reader (NVDA on Windows, VoiceOver on Mac with Cmd+F5).

| Check | Step | Result | Notes |
| --- | --- | --- | --- |
| Does the page have one H1 and a logical heading order? | | | |
| Are landmarks used (header, nav, main)? | | | |
| Does every form field have a visible, programmatically linked label? | | | |
| Is the results table marked up as a real table with header cells? | | | |
| Do icon only buttons have accessible names (aria-label)? | | | |
| Are status changes (added, error) announced (aria-live)? | | | |
| Are ARIA roles and attributes valid and not misused? | | | |
| Do error messages identify the field in text (SC 3.3.1)? | | | |

## Findings Log

| ID | Step | WCAG SC | Level | Issue | Evidence | Who it affects | Severity (0 to 4) | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | | | | | | | | |
| A02 | | | | | | | | |
| A03 | | | | | | | | |
| A04 | | | | | | | | |
| A05 | | | | | | | | |

## Summary

**Overall result:** Pass / Partial / Fail against WCAG 2.1 AA for the tested flow

**Most serious barriers:**
1.
2.
3.

**Heuristic violation linked to a WCAG failure (for reflection question 2):**

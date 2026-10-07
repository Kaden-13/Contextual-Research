# Screenshots

* `raw/`: unedited captures taken by the researcher during the heuristic evaluation and accessibility audit (not during participant sessions)
* `annotated/`: marked up versions used in the report

## Shot List (8 screenshots)

Take these on your own eWeber account while doing the heuristic evaluation. Each one should show at least one logged finding.

| # | Step | What to capture | What to point out |
| --- | --- | --- | --- |
| 1 | S1 | eWeber portal home with the Register for Classes app | How easy or hard the app is to find among other tiles |
| 2 | S3 | Term selection screen | Whether it's clear which term you're in and what to pick |
| 3 | S4 | Class search form | Unclear labels, subject codes, hidden advanced search |
| 4 | S5 | Search results list | Abbreviations, codes, clutter, where times and open seats appear |
| 5 | S6 | Section details | Where prerequisites and restrictions are (or aren't) shown |
| 6 | S7 | Where you would add a class | Whether it's clear what Add does and what happens next |
| 7 | Any | axe DevTools or WAVE results on one page | Number of errors and the most serious ones |
| 8 | Any | One manual accessibility failure, such as a missing focus ring or a low contrast label | The exact element that fails |

If an error or warning message appears at any point, screenshot it too. Those make strong findings.

## Annotating

* Add numbered markers (1, 2, 3) on the issues, not just colored circles, so meaning doesn't depend on color alone
* Write a caption under each one in the report: finding ID, heuristic or WCAG criterion, and one sentence on the problem
* Add alt text to each image in the report

## Naming

`[step]_[finding ID]_[short description].png`

Examples:
* `S5_HE03_results_table_codes.png`
* `S6_A02_low_contrast_seats_label.png`
* `S4_A04_no_focus_ring.png`

## Before Committing

* Crop or blur names, student IDs, holds, grades, and anything else personal

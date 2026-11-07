# Keyboard Tab Order by Screen

Generated from the wireframe HTML in `../04_wireframes/src/` by reading every focusable element in DOM order, the same order the Tab key follows. No positive `tabindex` values are used anywhere, so visual order, DOM order, and tab order always match (WCAG 2.4.3 Focus Order).

Accessible names exclude content hidden with `aria-hidden="true"` and include visually hidden `.sr-only` text, matching what a screen reader announces.

## W1: Registration Home (20 tab stops)

| # | Accessible name | Element | Landmark | ARIA |
| --- | --- | --- | --- | --- |
| 1 | Skip to main content | `a` | before header (skip link) |  |
| 2 | Weber State Registration | `a` | header |  |
| 3 | Spring 2027 ▾ | `button` | header | `aria-haspopup="listbox" aria-expanded="false"` |
| 4 | Help and Glossary | `a` | nav (Utility) |  |
| 5 | Contact My Advisor | `a` | nav (Utility) |  |
| 6 | Sign Out | `a` | nav (Utility) |  |
| 7 | Registration Home | `a` | nav (Primary) | `aria-current="page"` |
| 8 | Find Classes | `a` | nav (Primary) |  |
| 9 | My Schedule (2 pending) | `a` | nav (Primary) |  |
| 10 | My Degree | `a` | nav (Primary) |  |
| 11 | Finances | `a` | nav (Primary) |  |
| 12 | What is a hold? | `a` | main |  |
| 13 | Review and register | `a` | main |  |
| 14 | Find classes | `a` | main |  |
| 15 | Check your degree progress | `a` | main |  |
| 16 | Review and register. | `a` | main |  |
| 17 | Tuition and drop deadlines | `a` | main |  |
| 18 | Accessibility | `a` | footer |  |
| 19 | Registration deadlines | `a` | footer |  |
| 20 | Contact the Registrar | `a` | footer |  |

## W2: Find Classes (31 tab stops)

| # | Accessible name | Element | Landmark | ARIA |
| --- | --- | --- | --- | --- |
| 1 | Skip to main content | `a` | before header (skip link) |  |
| 2 | Weber State Registration | `a` | header |  |
| 3 | Spring 2027 ▾ | `button` | header | `aria-haspopup="listbox" aria-expanded="false"` |
| 4 | Help and Glossary | `a` | nav (Utility) |  |
| 5 | Contact My Advisor | `a` | nav (Utility) |  |
| 6 | Sign Out | `a` | nav (Utility) |  |
| 7 | Registration Home | `a` | nav (Primary) |  |
| 8 | Find Classes | `a` | nav (Primary) | `aria-current="page"` |
| 9 | My Schedule (2 pending) | `a` | nav (Primary) |  |
| 10 | My Degree | `a` | nav (Primary) |  |
| 11 | Finances | `a` | nav (Primary) |  |
| 12 | Registration Home | `a` | nav (Breadcrumb) |  |
| 13 | Find Classes | `a` | nav (Breadcrumb) | `aria-current="page"` |
| 14 | Subject | `select[select-one]` | main |  |
| 15 | Course number | `input[text]` | main | `aria-describedby="num-hint"` |
| 16 | Morning | `input[checkbox]` | main |  |
| 17 | Afternoon | `input[checkbox]` | main |  |
| 18 | Evening | `input[checkbox]` | main |  |
| 19 | Only open sections | `input[checkbox]` | main |  |
| 20 | Search | `button` | main |  |
| 21 | More filters (days, campus, online) | `a` | main |  |
| 22 | Add to my schedule: CS 2420 Section 001 | `button` | main |  |
| 23 | Details for Section 001 | `button` | main | `aria-expanded="false" aria-controls="det-001"` |
| 24 | Add to my schedule: CS 2420 Section 002 | `button` | main | `aria-describedby="s2-conf"` |
| 25 | Details for Section 002 | `button` | main | `aria-expanded="false" aria-controls="det-002"` |
| 26 | Join waitlist: CS 2420 Section 601 | `button` | main |  |
| 27 | Details for Section 601 | `button` | main | `aria-expanded="false" aria-controls="det-601"` |
| 28 | Review and register (2) | `a` | aside |  |
| 29 | Accessibility | `a` | footer |  |
| 30 | Registration deadlines | `a` | footer |  |
| 31 | Contact the Registrar | `a` | footer |  |

## W3: Find Classes after Add, details expanded (33 tab stops)

| # | Accessible name | Element | Landmark | ARIA |
| --- | --- | --- | --- | --- |
| 1 | Skip to main content | `a` | before header (skip link) |  |
| 2 | Weber State Registration | `a` | header |  |
| 3 | Spring 2027 ▾ | `button` | header | `aria-haspopup="listbox" aria-expanded="false"` |
| 4 | Help and Glossary | `a` | nav (Utility) |  |
| 5 | Contact My Advisor | `a` | nav (Utility) |  |
| 6 | Sign Out | `a` | nav (Utility) |  |
| 7 | Registration Home | `a` | nav (Primary) |  |
| 8 | Find Classes | `a` | nav (Primary) | `aria-current="page"` |
| 9 | My Schedule (2 pending) | `a` | nav (Primary) |  |
| 10 | My Degree | `a` | nav (Primary) |  |
| 11 | Finances | `a` | nav (Primary) |  |
| 12 | Registration Home | `a` | nav (Breadcrumb) |  |
| 13 | Find Classes | `a` | nav (Breadcrumb) | `aria-current="page"` |
| 14 | Review and register | `a` | main |  |
| 15 | Subject | `select[select-one]` | main |  |
| 16 | Course number | `input[text]` | main | `aria-describedby="num-hint"` |
| 17 | Morning | `input[checkbox]` | main |  |
| 18 | Afternoon | `input[checkbox]` | main |  |
| 19 | Evening | `input[checkbox]` | main |  |
| 20 | Only open sections | `input[checkbox]` | main |  |
| 21 | Search | `button` | main |  |
| 22 | More filters (days, campus, online) | `a` | main |  |
| 23 | Added (pending): CS 2420 Section 001, not registered yet | `button` | main | `aria-disabled="true"` |
| 24 | Hide details for Section 001 | `button` | main | `aria-expanded="true" aria-controls="det-001"` |
| 25 | What is this? | `button` | main | `aria-describedby="crn-def"` |
| 26 | Add to my schedule: CS 2420 Section 002 | `button` | main | `aria-describedby="s2-conf"` |
| 27 | Details for Section 002 | `button` | main | `aria-expanded="false" aria-controls="det-002"` |
| 28 | Join waitlist: CS 2420 Section 601 | `button` | main |  |
| 29 | Details for Section 601 | `button` | main | `aria-expanded="false" aria-controls="det-601"` |
| 30 | Review and register (2) | `a` | aside |  |
| 31 | Accessibility | `a` | footer |  |
| 32 | Registration deadlines | `a` | footer |  |
| 33 | Contact the Registrar | `a` | footer |  |

## W4: My Schedule review (21 tab stops)

| # | Accessible name | Element | Landmark | ARIA |
| --- | --- | --- | --- | --- |
| 1 | Skip to main content | `a` | before header (skip link) |  |
| 2 | Weber State Registration | `a` | header |  |
| 3 | Spring 2027 ▾ | `button` | header | `aria-haspopup="listbox" aria-expanded="false"` |
| 4 | Help and Glossary | `a` | nav (Utility) |  |
| 5 | Contact My Advisor | `a` | nav (Utility) |  |
| 6 | Sign Out | `a` | nav (Utility) |  |
| 7 | Registration Home | `a` | nav (Primary) |  |
| 8 | Find Classes | `a` | nav (Primary) |  |
| 9 | My Schedule (2 pending) | `a` | nav (Primary) | `aria-current="page"` |
| 10 | My Degree | `a` | nav (Primary) |  |
| 11 | Finances | `a` | nav (Primary) |  |
| 12 | Registration Home | `a` | nav (Breadcrumb) |  |
| 13 | My Schedule | `a` | nav (Breadcrumb) | `aria-current="page"` |
| 14 | Remove CS 2420 from pending | `button` | main | `aria-label="Remove CS 2420 from pending"` |
| 15 | Remove MATH 1210 from pending | `button` | main | `aria-label="Remove MATH 1210 from pending"` |
| 16 | Register for 2 classes | `button` | main | `aria-describedby="drop-rule"` |
| 17 | Add another class | `a` | main |  |
| 18 | Drop ENGL 2010 | `button` | main | `aria-label="Drop ENGL 2010"` |
| 19 | Accessibility | `a` | footer |  |
| 20 | Registration deadlines | `a` | footer |  |
| 21 | Contact the Registrar | `a` | footer |  |

## W5: Registration results (20 tab stops)

| # | Accessible name | Element | Landmark | ARIA |
| --- | --- | --- | --- | --- |
| 1 | Skip to main content | `a` | before header (skip link) |  |
| 2 | Weber State Registration | `a` | header |  |
| 3 | Spring 2027 ▾ | `button` | header | `aria-haspopup="listbox" aria-expanded="false"` |
| 4 | Help and Glossary | `a` | nav (Utility) |  |
| 5 | Contact My Advisor | `a` | nav (Utility) |  |
| 6 | Sign Out | `a` | nav (Utility) |  |
| 7 | Registration Home | `a` | nav (Primary) |  |
| 8 | Find Classes | `a` | nav (Primary) |  |
| 9 | My Schedule (2 pending) | `a` | nav (Primary) | `aria-current="page"` |
| 10 | My Degree | `a` | nav (Primary) |  |
| 11 | Finances | `a` | nav (Primary) |  |
| 12 | Registration Home | `a` | nav (Breadcrumb) |  |
| 13 | My Schedule | `a` | nav (Breadcrumb) |  |
| 14 | Results | `a` | nav (Breadcrumb) | `aria-current="page"` |
| 15 | Join waitlist for MATH 1210 | `button` | main | `aria-describedby="full-msg"` |
| 16 | See other MATH 1210 sections | `a` | main |  |
| 17 | Back to My Schedule | `a` | main |  |
| 18 | Accessibility | `a` | footer |  |
| 19 | Registration deadlines | `a` | footer |  |
| 20 | Contact the Registrar | `a` | footer |  |

## W6: My Degree (18 tab stops)

| # | Accessible name | Element | Landmark | ARIA |
| --- | --- | --- | --- | --- |
| 1 | Skip to main content | `a` | before header (skip link) |  |
| 2 | Weber State Registration | `a` | header |  |
| 3 | Spring 2027 ▾ | `button` | header | `aria-haspopup="listbox" aria-expanded="false"` |
| 4 | Help and Glossary | `a` | nav (Utility) |  |
| 5 | Contact My Advisor | `a` | nav (Utility) |  |
| 6 | Sign Out | `a` | nav (Utility) |  |
| 7 | Registration Home | `a` | nav (Primary) |  |
| 8 | Find Classes | `a` | nav (Primary) |  |
| 9 | My Schedule (2 pending) | `a` | nav (Primary) |  |
| 10 | My Degree | `a` | nav (Primary) | `aria-current="page"` |
| 11 | Finances | `a` | nav (Primary) |  |
| 12 | Registration Home | `a` | nav (Breadcrumb) |  |
| 13 | My Degree | `a` | nav (Breadcrumb) | `aria-current="page"` |
| 14 | Find sections of CS 2420 | `a` | main |  |
| 15 | Contact my advisor | `a` | main |  |
| 16 | Accessibility | `a` | footer |  |
| 17 | Registration deadlines | `a` | footer |  |
| 18 | Contact the Registrar | `a` | footer |  |

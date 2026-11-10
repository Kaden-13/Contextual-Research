# Variable Mapping Tables

## 1. Independent Variables

| Variable | Role | Manipulation | Levels | Assignment |
|---|---|---|---|---|
| Interface_Condition | Primary IV | Prototype build loaded at session start | A = Baseline Control, B = Refactored Accessible Treatment | Within-subjects, order counterbalanced |
| Task_Type | Blocking factor | Task card | T1 = keyboard-only add and submit, T2 = full-section error recovery | Fixed order (T1 then T2) within each period |
| Task_Set | Counterbalanced nuisance factor | Fake course data loaded into the prototype | X, Y (isomorphic) | Crossed with interface in a 2×2 Latin square |

## 2. What Differs Between Conditions (manipulation check)

| Property | Interface A (Baseline) | Interface B (Treatment) | WCAG 2.1 SC |
|---|---|---|---|
| Add button element | `<div>` with click handler, not focusable | Native `<button>` | 2.1.1 Keyboard |
| Tab order through results | Skips results and Add buttons | Search, filters, each result row, Add, cart, Submit | 2.4.3 Focus Order |
| Focus indicator | Browser default, partly hidden by styles | 3px high-contrast outline | 2.4.7 Focus Visible |
| Full-section error | Generic message, no cause or next step | Names the section, seat count, and links to open sections | 3.3.1, 3.3.3 |
| Error announcement | Not announced | `aria-live="assertive"` region | 4.1.3 Status Messages |
| Everything else (color, type, layout, data) | Same | Same | n/a |

## 3. Dependent Variables

| Construct | Variable | Measurement instrument | When collected | Scale | Better is |
|---|---|---|---|---|---|
| Efficiency | Task_Completion_Time_sec | Prototype timer (`performance.now()`), recording backup | Every task | Ratio, seconds, cap 300 | Lower |
| Efficiency (secondary) | Keystroke_Count | Prototype key log | Every task | Count | Lower |
| Effectiveness | Task_Success_Binary | Correct end state check + moderator log | Every task | 0 / 1 | 1 |
| Effectiveness | Error_Count_Total | Video coding with E1 to E6 codebook | Every task | Count | Lower |
| Satisfaction | SEQ_Rating | Single Ease Question card | After every task | 1 to 7 | Higher |
| Satisfaction | SUS_Score | 10-item SUS | After each condition | 0 to 100 | Higher |

## 4. Hypothesis to Metric to Test

| Hypothesis | DV | Data used | Primary test | Effect size | Practical threshold |
|---|---|---|---|---|---|
| H1 Time | Task_Completion_Time_sec | T1, both conditions | Paired t-test (log time) | Cohen's d_z, ratio of geometric means | ≥ 20% faster or ≥ 30 s saved |
| H2 Errors | Error_Count_Total | T1 + T2 summed per condition | Wilcoxon signed-rank | Rank-biserial r | ≥ 1 fewer error per task |
| H3 Recovery | Task_Success_Binary | T2, both conditions | Exact McNemar | Difference in proportions with 95% CI | ≥ 25 percentage points |
| H4 Usability | SUS_Score | Per condition | Paired t-test | Cohen's d_z | ≥ 10 points |
| Exploratory | SEQ_Rating, Keystroke_Count | Per task | Wilcoxon signed-rank | Rank-biserial r | SEQ ≥ 1 point |

Alpha = .05, Holm-Bonferroni across H1 to H4.

## 5. Controlled and Measured Covariates

| Variable | Type | How controlled or measured |
|---|---|---|
| Registration_Experience | Measured covariate, stratification factor | Screening survey; balanced across sequences |
| Keyboard_Habit | Measured covariate | Screening survey (5 point frequency) |
| Hardware | Held constant | Same laptop, monitor, USB keyboard, mouse removed |
| Browser environment | Held constant | Same Chrome version, guest profile, 100% zoom, no extensions |
| Network | Held constant | Prototype runs offline on localhost |
| Room environment | Held constant | Same room, blinds closed, fixed lighting |
| Session length / fatigue | Limited and balanced | 45 min cap, 3 min break, counterbalanced order |
| Period (practice) | Counterbalanced and modeled | Latin square; Period term in mixed model |
| Sequence (carryover) | Counterbalanced and tested | Grizzle test; Period 1 fallback |

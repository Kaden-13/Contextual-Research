# Heuristic Evaluation: Nielsen's 10 Usability Heuristics

**Evaluator:** Kaden Donaldson
**Date(s):**
**System:** eWeber portal, Register for Classes app
**Browser / device:**
**Term used for testing:**

## Method

I walked through the registration flow one screen at a time, twice. The first pass was to learn the flow as a student would. The second pass checked each screen against all 10 heuristics. Every issue gets a screenshot in `screenshots/raw/`, an ID, and a severity rating.

### Flow Steps Evaluated

| Step | Screen |
| --- | --- |
| S1 | eWeber portal home, locating the Register for Classes app |
| S2 | Tuition agreement |
| S3 | Term selection |
| S4 | Class search form (subject, course number, campus, advanced search) |
| S5 | Search results list |
| S6 | Section details (meeting times, seats, prerequisites, restrictions) |
| S7 | Locating the Add option (adding is disabled outside the registration window; evaluate how clearly that is communicated) |
| S8 | Submitting registration and confirmation or errors (not testable outside the registration window; note as a limitation) |
| S9 | Error recovery (evaluate any messages that do appear, such as registration being closed) |

### Severity Scale

| Rating | Meaning |
| --- | --- |
| 0 | Not a usability problem |
| 1 | Cosmetic. Fix only if time allows |
| 2 | Minor. Low priority fix |
| 3 | Major. Important to fix, high priority |
| 4 | Usability catastrophe. Must fix before release |

Severity considers how often the problem happens, how hard it is to overcome, and whether it keeps happening once users know about it.

## What to Look For in Registration

Use these prompts while evaluating. They are starting points, not findings. Only log what you actually see.

| # | Heuristic | Questions to ask on each screen |
| --- | --- | --- |
| H1 | Visibility of system status | Is it clear which term I'm in? Do I know whether a class is in my cart versus actually registered? Is there feedback after clicking Add or Submit? |
| H2 | Match between system and real world | Are codes like CRN, schedule type, campus codes, block, or day abbreviations explained? Does it use student language or registrar language? |
| H3 | User control and freedom | Can I undo an add or drop? Can I go back without losing my search? Is there a way out of the tuition agreement screen? |
| H4 | Consistency and standards | Do buttons, labels, and date or time formats stay the same across screens and across the two registration apps? |
| H5 | Error prevention | Does it warn about time conflicts, missing prerequisites, or holds before I try to submit, or only after? |
| H6 | Recognition rather than recall | Do I have to remember a CRN, course number, or section time from another screen? Are prerequisites shown next to the section? |
| H7 | Flexibility and efficiency of use | Are there filters for time of day, online only, or open seats? Can experienced users register quickly? |
| H8 | Aesthetic and minimalist design | Is the results table cluttered? Is important info (seats, times) buried among less useful columns? |
| H9 | Help users recognize, diagnose, and recover from errors | Do error messages say what went wrong in plain language and how to fix it? |
| H10 | Help and documentation | Is help available inside the app, or only on separate weber.edu pages and tutorial videos? |

## Findings Log

Add one row per issue. If the same issue breaks more than one heuristic, list the main one first.

| ID | Step | Heuristic(s) | Issue description | Evidence (screenshot / participant) | Severity (0 to 4) | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| HE01 | | | | | | |
| HE02 | | | | | | |
| HE03 | | | | | | |
| HE04 | | | | | | |
| HE05 | | | | | | |
| HE06 | | | | | | |
| HE07 | | | | | | |
| HE08 | | | | | | |
| HE09 | | | | | | |
| HE10 | | | | | | |

## Summary

| Heuristic | Issues found | Highest severity |
| --- | --- | --- |
| H1 Visibility of system status | | |
| H2 Match between system and real world | | |
| H3 User control and freedom | | |
| H4 Consistency and standards | | |
| H5 Error prevention | | |
| H6 Recognition rather than recall | | |
| H7 Flexibility and efficiency of use | | |
| H8 Aesthetic and minimalist design | | |
| H9 Error recognition and recovery | | |
| H10 Help and documentation | | |

**Top 3 issues by severity:**
1.
2.
3.

**Issues that also showed up in user sessions:**

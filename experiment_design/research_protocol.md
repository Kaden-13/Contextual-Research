# Research Protocol: Register for Classes Keyboard and Error Recovery Study

Companion to `README.md`. This is the operational, step by step procedure the moderator follows in every session.

## 1. Materials Checklist (before each session)

- [ ] Lab laptop charged, connected to the 1920×1080 external monitor, display scaling 100%
- [ ] External full-size USB keyboard connected; **mouse unplugged and removed from the desk**
- [ ] Chrome (version recorded in the log) open in a fresh guest profile, no extensions, zoom 100%
- [ ] Prototype served locally (`localhost`), Wi-Fi off to remove network variability
- [ ] Prototype set to the participant's sequence (see `counterbalancing_matrix.csv`)
- [ ] Screen recorder (OBS) running, recording screen only, audio off unless participant opts in
- [ ] Blinds closed, overhead lights on, door closed, phones silenced
- [ ] Printed consent form (standard and large print), SEQ cards, SUS forms labeled Version 1 and Version 2
- [ ] Blank row block for this participant in `data_collection_sheet.csv`

## 2. Screening Survey (sent when scheduling)

1. Are you a currently enrolled Weber State student and 18 or older? (Yes / No; No = excluded)
2. How many terms have you registered for classes at Weber State? (0, 1, 2, 3, 4, 5 or more)
3. Have you ever done a usability interview, card sort, or prototype review with Kaden Donaldson? (Yes = excluded)
4. Do you work on eWeber or Banner development? (Yes = excluded)
5. How often do you navigate websites using only the keyboard? (Never, Rarely, Sometimes, Often, Always)
6. Do you use any assistive technology? (Optional, free text; used to plan accommodations, not as a variable)

Stratum: **Novice** = 0 to 2 terms, **Experienced** = 3 or more terms.

## 3. Task Cards

Both task sets are isomorphic: same number of search results (8), target row in the same position (5th), one full section, and two open alternatives.

### Task Set X
- **T1:** "You need to take **CS 2420 Introduction to Data Structures** next term. Using only the keyboard, find the class, add **section 001 (CRN 31842)** to your cart, and submit your registration."
- **T2:** "You also need **MATH 1210 Calculus I**. Try to add **section 003 (CRN 30517)**. If it can't be added, add another section of MATH 1210 that has open seats, and submit."

### Task Set Y
- **T1:** "You need to take **CS 2550 Database Design and SQL** next term. Using only the keyboard, find the class, add **section 001 (CRN 32206)** to your cart, and submit your registration."
- **T2:** "You also need **PHYS 2210 Physics for Scientists and Engineers I**. Try to add **section 002 (CRN 30944)**. If it can't be added, add another section of PHYS 2210 that has open seats, and submit."

(The full section in T2 is MATH 1210 sec 003 in Set X and PHYS 2210 sec 002 in Set Y. CRNs are fictional.)

## 4. Session Timeline (target 40 to 45 minutes)

| Minute | Step | Moderator action |
|---|---|---|
| 0 to 5 | Welcome, briefing, consent | Read the briefing script in `README.md` word for word. Collect consent. |
| 5 to 7 | Demographics | Confirm screening answers, record stratum. |
| 7 to 10 | Keyboard warm-up | Participant tabs through a neutral practice page (a fake library search form unrelated to registration). No data recorded. |
| 10 to 22 | **Period 1** | Run T1 then T2 for the first interface and task set. SEQ after each task, SUS after T2. |
| 22 to 25 | Break | Offer water. No discussion of the interfaces. |
| 25 to 37 | **Period 2** | Same as Period 1 with the second interface and task set. |
| 37 to 42 | Debrief | Read debrief script, answer questions, optional open comments. |

## 5. Running Each Task

1. Hand the participant the task card and read it aloud.
2. Say: *"When you're ready, press Enter on the Start Task button. Remember, keyboard only."*
3. The prototype starts its timer and keystroke log on Enter.
4. **Do not help.** If asked a question, say: *"What would you try if I weren't here?"*
5. If the participant is stuck for 60 seconds with no progress, or asks to stop, say: *"Would you like to move on?"* If yes, end the task. Record `Task_Success_Binary = 0` and `Moderator_Assist = 1`.
6. At 300 seconds the prototype ends the task automatically.
7. Show the SEQ card: *"Overall, how difficult or easy was this task to complete, from 1, very difficult, to 7, very easy?"*
8. Record observations in the `Notes` column (no judgments about the person, only behavior).

After T2 of each period, give the SUS form for that version.

## 6. Moderator Rules

- Refer to the interfaces only as **Version 1** and **Version 2** (in the order the participant sees them).
- Use the same neutral tone, no reactions to success or failure ("Okay, thanks" only).
- Never say "new," "old," "improved," or "redesign" before the debrief.
- If a participant becomes frustrated, remind them: *"That's useful for me. It shows where the design is falling short, not you."*

## 7. Data Handling

1. Export the prototype log (JSON) and copy time, success, and keystroke values into `data_collection_sheet.csv`.
2. Code errors from the recording using the E1 to E6 codebook in `README.md`.
3. Second coder independently codes 4 of 16 sessions (25%); compute Cohen's kappa; resolve disagreements by discussion.
4. Score SUS with the standard formula; compute SEQ medians.
5. Store recordings on an encrypted drive under participant ID only; delete at end of semester.

## 8. Pilot

Before real sessions, run 2 pilot participants (not counted in N = 16) to check that:
- Task sets X and Y take similar time (difference under 15%)
- Instructions are clear and the timer starts and stops correctly
- The 45 minute session length holds

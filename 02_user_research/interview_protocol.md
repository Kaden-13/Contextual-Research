# User Research Protocol

**Method:** Semi structured interview combined with a think aloud task observation (contextual inquiry)
**System:** Weber State University class search and registration (Register for Classes app in the eWeber portal)
**Participants:** 2 Weber State students
**Session length:** About 20 minutes
**Data collection:** Handwritten or typed observer notes only. Sessions are not audio or screen recorded.
**Setting:** The participant's own device and location when possible, so the context is realistic

## Participant Criteria

The two participants are chosen to sit at opposite ends of experience:

* **P1, novice:** a student who is new to Weber State registration and has registered once or never
* **P2, experienced:** a student who has registered for many semesters

Comparing the two shows both what blocks first time users and what experienced users have learned to work around.

Assign each participant an ID (P1, P2). Do not write full names in the repository.

## Materials

* Participant's own laptop or phone, logged into their own eWeber account
* This script and a printed or open copy of the participant's notes file (`raw_notes/P1_notes.md` or `P2_notes.md`)
* A timer (phone stopwatch works)
* Somewhere to take notes where you can see their screen over their shoulder

## Note Taking Tips

Since there is no recording, your notes are the only data. These habits make them usable later:

* **Sit beside them, slightly behind,** so you can see the screen without hovering.
* **Write quotes word for word inside quotation marks.** Anything not in quotes is your paraphrase. Keep the two separate.
* **Separate what you saw from what you think.** Write observations plainly ("clicked Back 3 times"). Put your own interpretations in brackets, like [seems confused by CRN].
* **Note the time** next to key moments (for example "2:15 stuck on term dropdown") so you can work out time on task later.
* **Use shorthand** to keep up: `?` = confused or hesitated, `X` = error or wrong turn, `!` = strong reaction, `A` = you had to assist, `W` = workaround.
* **Write down the exact screen** where something happened, so you can go back and screenshot it yourself during the heuristic evaluation.
* **It's okay to pause.** If they say something important, ask them to hold on a second while you write it down.
* **Clean up right after the session,** while it's fresh. Fill in anything you abbreviated, but add it as a dated note at the bottom instead of rewriting the original notes.

## 1. Introduction and Consent (2 minutes)

> Thanks for helping me out. I'm studying how students use Weber State's class registration system for my HCI class. I'm testing the system, not you, so there are no wrong answers. If something is confusing, that's exactly what I want to find.
>
> As you work, please think out loud: tell me what you're looking at, what you're trying to do, and what you expect to happen. I'll mostly stay quiet so I don't influence you, and I might ask a question now and then.
>
> I won't be recording anything. I'll just take notes on what you do and say. I won't write down your name or anything personal like grades, holds, or your student ID. You can stop at any time. Is that okay?

* [ ] Verbal consent given

## 2. Warm Up Questions (2 to 3 minutes)

1. What year are you, and what's your major?
2. What device do you usually register on?
3. (P1) Have you registered at Weber State before? What do you expect it to be like?
3. (P2) Walk me through how you usually build your schedule. Any shortcuts?

## 3. Task Observation (12 to 15 minutes)

Read each scenario aloud. Do not explain how to complete it. Start the timer when they begin and stop it when they finish or give up.

If they're stuck for about 2 minutes, ask "What would you do next if I weren't here?" If you have to step in and help, mark it with `A` in your notes.

**This is a mock run.** Participants search the **current semester**, and they won't actually add anything, so no real registration changes happen. Task 3 asks them to show and explain how they would add the class instead.

**Ground rules:** ask open questions, not leading ones. If they ask you how something works, turn it back: "What do you think it means?" Save most questions for right after each task so you don't break their flow.

### Task 1: Find a Course

> You need to take ENGL 2010. Find the list of sections being offered this semester.

*Substitute any common general education course offered that term.*

**Watch for:** finding the right app, the tuition agreement screen, term selection, subject codes, use of advanced search.

**Ask:**
* Was that where you expected to start?
* Was anything on the way there unclear or unnecessary?

### Task 2: Choose a Section That Fits Your Life

> You work every weekday until 1:00 PM. Find a section of that course that starts after 1:00 PM, or is fully online, and still has open seats.

**Watch for:** finding times, delivery method, and open seats; reading abbreviations; scrolling or switching screens; trying to filter by time.

**Ask:**
* How can you tell whether this one is online or in person, and whether it has room?
* How confident are you this section fits that schedule? (1 to 5)

### Task 3: Check Eligibility and Find How to Add

> Figure out whether you would be allowed to take this class. Then show me where you would go to add it to your schedule, and tell me what you expect to happen.

**Watch for:** whether prerequisites and restrictions are visible, and whether they can find where they would add a class.

**Ask:**
* What do you expect would happen if you added it?
* How would you know it worked?
* (P2) Have you ever gotten an error at this step? How did you fix it?

### Use Anytime

* You paused there. What were you thinking?
* What did you expect to happen when you clicked that?
* (When they move fast, mostly P2) How did you know to do that?

## 4. Post Task Questions (3 minutes)

1. Which task was the hardest, and why?
2. Was there anything on the screen you didn't understand or just ignored?
3. If you could change one thing about registration, what would it be?
4. On a scale of 1 (very difficult) to 5 (very easy), how easy was it today?

## 5. Wrap Up (1 minute)

> That's everything. Thanks so much, this really helps. Is there anything else about registration you want to mention?

## Observation Notes Template

Each participant's file in `raw_notes/` already has this template.

```
Participant: P_
Date:
Start time / end time:
Device / browser:
Location / setting:
Year / registration experience:

WARM UP
  Answers:

TASK 1: Find a Course
  Start time / end time:
  Completed: yes / with assist (A) / no
  Path taken (screens in order):
  Errors or wrong turns (X):
  Hesitations or confusion (?):
  Workarounds (W):
  Quotes (word for word, in quotes):
  Breakdown points:
  After task answers:

TASK 2: Choose a Section
  Start time / end time:
  Completed: yes / with assist (A) / no
  Path taken (screens in order):
  Errors or wrong turns (X):
  Hesitations or confusion (?):
  Workarounds (W):
  Quotes (word for word, in quotes):
  Breakdown points:
  Confidence rating (1 to 5):
  After task answers:

TASK 3: Check Eligibility and Find How to Add
  Start time / end time:
  Completed: yes / with assist (A) / no
  Path taken (screens in order):
  Errors or wrong turns (X):
  Hesitations or confusion (?):
  Workarounds (W):
  Quotes (word for word, in quotes):
  Breakdown points:
  After task answers:

Mental model mismatches (what they expected vs. what happened):

Post task answers:
  Hardest task:
  Didn't understand / ignored:
  One change:
  Ease rating (1 to 5):

Screens to screenshot myself later:

My interpretations [kept separate from observations]:

Cleanup notes (added after session, dated):
```

## After the Sessions

1. Clean up each participant's notes the same day and save them in `raw_notes/`
2. Pull every quote, error, and breakdown point onto an affinity board (sticky notes or a spreadsheet)
3. Group them into 3 to 5 themes, such as "jargon and codes," "information spread across screens," or "unhelpful error messages"
4. Write each theme with supporting quotes and the tasks where it showed up
5. Screenshot the screens you flagged, cropping out anything personal
6. Update the Evidence section of `problem_statement.md` with completion rates and times

# User Research Protocol

**Method:** Semi structured interview combined with a think aloud task observation (contextual inquiry).
**System:** Weber State University class search and registration (Register for Classes app in the eWeber portal)
**Participants:** 2 Weber State students
**Session length:** About 20 to 25 minutes
**Setting:** The participant's own device and location when possible, so the context is realistic

## Participant Criteria

The two participants are chosen to sit at opposite ends of experience:

* **P1, novice:** a student who is new to Weber State registration and has registered once or never
* **P2, experienced:** a student who has registered for many semesters

Comparing the two shows both what blocks first time users and what experienced users have learned to work around.

Assign each participant an ID (P1, P2). Do not record full names in the repository.

## Materials

* Participant's own laptop or phone, logged into their own eWeber account
* Screen recording (only with consent) or a second person taking notes
* Copy of this script and the observation notes template below
* A timer

## 1. Introduction and Consent (2 minutes)

> Thanks for helping me out. I'm studying how students use Weber State's class registration system for my HCI class. I'm testing the system, not you, so there are no wrong answers. If something is confusing, that's exactly what I want to find.
>
> As you work, please think out loud: tell me what you're looking at, what you're trying to do, and what you expect to happen. I may stay quiet while you work so I don't influence you.
>
> I'll take notes and, with your permission, record the screen. I won't use your name or show any personal information like grades or your student ID. You can stop at any time. Is that okay?

* [ ] Verbal consent given
* [ ] Recording consent given (yes / no)

## 2. Warm Up Questions (3 minutes)

1. What year are you, and what's your major?
2. How many times have you registered for classes at Weber State?
3. Walk me through how you usually build your schedule. Where do you start?
4. What device do you usually register on?
5. Have you ever needed help from an advisor, the registrar, or a friend to register? What happened?

## 3. Task Observation (12 to 15 minutes)

Read each scenario aloud. Do not explain how to complete it. Start the timer when the participant begins and stop it when they finish or give up.

If the participant is stuck for about 2 minutes, ask "What would you do next if I weren't here?" Note it as an assist if you have to step in.

**Note:** The participant should stop before final submission so no real registration changes are made, unless they actually want that class.

### Task 1: Find a Course

> You need to take ENGL 2010 next semester. Find the list of sections being offered.

*Substitute any common general education course offered that term.*

Watch for: how they find search, whether they understand subject codes and term selection, use of filters.

### Task 2: Choose a Section That Fits Your Life

> You work every weekday until 1:00 PM. Find a section of that course that starts after 1:00 PM, or is fully online, and still has open seats.

Watch for: whether they can tell meeting times, delivery method, and seat availability apart; abbreviations like days, campus, or delivery codes; how much they scroll or switch screens.

### Task 3: Check Eligibility and Add to Cart

> Before you add it, figure out whether you are allowed to take this class. Then get it ready to register, but stop before final submission.

Watch for: whether prerequisites and restrictions are visible, how errors or warnings are communicated, whether they know what happens next.

### Probing Questions (use during or after any task)

* What did you expect to happen when you clicked that?
* What does that label or code mean to you?
* How confident are you that this is the right section?
* You paused there. What were you thinking?

## 4. Post Task Questions (4 minutes)

1. Which of those tasks was the hardest? Why?
2. Was there anything on the screen you didn't understand or ignored?
3. Think of a time registration went wrong for you. What happened, and how did you fix it?
4. If you could change one thing about the registration system, what would it be?
5. On a scale of 1 (very difficult) to 5 (very easy), how easy was it to register today?

## 5. Wrap Up (1 minute)

> That's everything. Thanks so much, this really helps. Is there anything else about registration you want to mention?

## Observation Notes Template

Copy this section into a new file for each participant (for example `raw_notes/P1_notes.md`).

```
Participant: P_
Date:
Device / browser:
Year / registration experience:

TASK 1: Find a Course
  Completed: yes / with assist / no
  Time:
  Path taken:
  Errors or wrong turns:
  Quotes:
  Breakdown points:

TASK 2: Choose a Section
  Completed: yes / with assist / no
  Time:
  Path taken:
  Errors or wrong turns:
  Quotes:
  Breakdown points:

TASK 3: Check Eligibility and Add to Cart
  Completed: yes / with assist / no
  Time:
  Path taken:
  Errors or wrong turns:
  Quotes:
  Breakdown points:

Mental model mismatches (what they expected vs. what happened):

Post task answers:
  Hardest task:
  Didn't understand:
  Past registration problem:
  One change:
  Ease rating (1 to 5):

Observer notes / screenshots to capture:
```

## After the Sessions

1. Save each participant's notes in `raw_notes/`
2. Pull every quote, error, and breakdown point onto an affinity board (sticky notes or a spreadsheet)
3. Group them into 3 to 5 themes, such as "jargon and codes," "information spread across screens," or "unhelpful error messages"
4. Write each theme with supporting quotes and the tasks where it showed up
5. Update the Evidence section of `problem_statement.md` with completion rates and times

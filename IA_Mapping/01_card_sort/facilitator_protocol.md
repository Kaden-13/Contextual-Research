# Card Sort Facilitator Protocol

**Study:** Open card sort for the Weber State class registration system
**Researcher:** Kaden Donaldson
**Goal:** Learn how students naturally group registration tasks so the revised Information Architecture matches their mental model instead of the current split between Register for Classes, CatTracks, the tuition pages, and advisors.

## Study Design

| Item | Decision |
| --- | --- |
| Sort type | **Open sort.** Participants create and name their own groups. |
| Cards | 20 task cards (`card_deck.csv`), each traced to a Phase 1 finding |
| Participants | At least 3 Weber State students. Aim for a mix: at least one newer student and one who has registered several times. |
| Format | Physical index cards (print `card_deck_printable.pdf`) or a digital board (Miro, Mural, or Trello) |
| Length | About 15 to 20 minutes per session |
| Recording | Photo of the final layout plus notes on this sheet. No audio or screen recording. |

**Why open sort:** Phase 1 showed students do not think of CatTracks, Register for Classes, and tuition as separate tools. An open sort lets their own categories and labels show up instead of forcing them into the current menu structure.

**Card wording rules:** Cards use plain student language ("Add a class to my list"), not system names ("Summary panel," "CRN lookup," "Add/Drop"), and avoid repeating the same keyword across many cards so participants group by meaning instead of matching words.

## Before the Session

1. Shuffle the cards so every participant gets a different order.
2. Have blank cards and a pen ready for group labels.
3. Have the recording sheet below open.

## Script

> Thanks for helping. I'm redesigning how Weber State's class registration is organized, and I want to see how students would group these tasks. There are no right or wrong answers. I'm testing the system, not you.
>
> Here are 20 cards. Each one is something a student might do around registering for classes. Please sort them into groups that make sense to you. You can make as many or as few groups as you like, and groups can be any size.
>
> When you're done, give each group a name that describes it, the kind of name you'd expect to see on a menu or button.
>
> If a card doesn't fit anywhere, or you don't understand it, put it in a pile called "Unsure." Please think out loud while you work.

**During the sort:** Stay quiet. Don't explain cards unless asked, and if asked, read the card back instead of defining it. Write down any card the participant hesitates on, moves more than once, or asks about.

## Debrief Questions

1. Which cards were hardest to place? Why?
2. Were there any cards you thought could go in more than one group?
3. Which group would you go to first when it's time to register?
4. Is anything missing that you'd expect to find?

## Recording Sheet (one per participant)

**Participant ID:** P__   **Date:** ________   **Format:** Physical / Digital
**Year:** ________   **Times registered at Weber State:** ____   **Usual device:** ________

| Group label (participant's words) | Cards in group (IDs) |
| --- | --- |
| | |
| | |
| | |
| | |
| | |
| | |

**Unsure pile:** ____________________

**Cards moved more than once or hesitated on:** ____________________

**Quotes while sorting:**

**Debrief answers:**

1.
2.
3.
4.

## After the Session

1. Take a photo of the final layout and save it as `raw_data/P1_layout.jpg` (P2, P3, and so on).
2. Copy the groupings into `raw_data/card_sort_results.csv` using the template. One row per card per participant, with the participant's group label typed exactly as they wrote it.
3. Save the filled recording sheet as `raw_data/P1_session_notes.md`.
4. Run `python3 analyze_card_sort.py` to generate the similarity matrix, cluster diagram, and consensus tables.

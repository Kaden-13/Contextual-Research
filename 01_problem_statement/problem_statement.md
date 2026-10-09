# Problem Statement and Context of Use

## Target System

**Platform:** Weber State University class search and registration, accessed through the eWeber student portal. Students register with either the **Register for Classes (Add/Drop)** app or the **Registration Schedule Builder** app.

**Scope of this audit:** The flow a student follows in the Register for Classes app to find a course, evaluate its sections, confirm eligibility, and add it to their schedule. The Registration Schedule Builder is noted where participants choose to use it instead. So that no one's real schedule changes, sessions are a mock run: participants search current semester classes and show how they would add one, but do not actually add or submit anything.

## Target Users

**Primary users:** Undergraduate students at Weber State University.

* Ages roughly 18 to 30, plus a meaningful share of returning and nontraditional students
* Many work part time or full time and attend a mix of in person, online, and hybrid classes
* Range from first semester freshmen with no registration experience to seniors fitting in final requirements
* Access the system on both laptops and phones, often in short sessions between other obligations
* Includes students who use assistive technology such as screen readers, screen magnifiers, or keyboard only navigation

**Secondary users:** Academic advisors who help students build schedules.

## Core User Tasks

1. **Find a course:** Search for a class by subject, course number, or keyword.
2. **Evaluate sections:** Compare available sections by days, times, delivery method, instructor, and open seats.
3. **Confirm eligibility:** Check prerequisites, restrictions, and whether a section is full or waitlisted.
4. **Register:** Add the chosen section to the cart and complete registration.
5. **Recover from errors:** Understand and resolve registration errors such as time conflicts, holds, or missing prerequisites.

## The Problem

Registration is a high stakes, time sensitive task, yet the interface asks students to work like the system rather than the system working like them. Students must interpret institutional codes and abbreviations, hold section details in memory while moving between screens, and decode error messages that explain what went wrong in system terms but not how to fix it.

## Consequences

**Human consequences**

* Students spend far longer than necessary building a schedule and often give up and ask an advisor or a friend
* Unclear errors cause students to register for the wrong section, miss a prerequisite, or lose a seat in a popular class while troubleshooting
* Students who rely on keyboard navigation or screen readers may be unable to complete registration independently

**Institutional consequences**

* Increased load on advising and the registrar's office for questions the interface should answer
* Schedule mistakes that delay progress toward graduation, affecting retention and completion rates
* Potential legal exposure under the ADA and Section 504 if the system does not meet WCAG 2.1 AA

## Evidence to Collect

This statement will be validated or revised using the data gathered in this phase:

* Task completion: 5 of 6 tasks completed without help. The novice needed help finding class times and took 35 minutes on the first two tasks versus 15 for the experienced student. Ease ratings were 1 (novice) and 4 (experienced) out of 5.
* Quotes and breakdowns: "Where do i see the time for the class" and "Why do i have to click so many buttons" (novice); the experienced student avoids the portal entirely, using the Schedule Builder and her advisor.
* Heuristic violations with severity ratings: 14 issues logged, 6 rated severity 3 (major), led by the Add then Submit split and a full class error that never says the class is full
* WCAG 2.1 AA failures: 12 issues logged, and WAVE rates the search results page 2.5 out of 10 (23 errors, 89 contrast errors); the flow fails AA because a keyboard only user cannot reach the Add buttons (SC 2.1.1), plus contrast as low as 1.07:1 and clipped content at 200% and 400% zoom

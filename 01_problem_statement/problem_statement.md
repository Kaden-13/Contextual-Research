# Problem Statement and Context of Use

## Target System

**Platform:** Weber State University class search and registration, accessed through the eWeber student portal. Students register with either the **Register for Classes (Add/Drop)** app or the **Registration Schedule Builder** app.

**Scope of this audit:** The flow a student follows in the Register for Classes app to find a course, evaluate its sections, confirm eligibility, and add it to their schedule. The Registration Schedule Builder is noted where participants choose to use it instead. Because this audit takes place outside the registration window, sessions are a mock run: participants search current semester classes and show how they would add one, but adding is not available.

## Target Users

**Primary users:** Undergraduate students at Weber State University.

* Ages roughly 18 to 30, plus a meaningful share of returning and nontraditional students
* Many work part time or full time and attend a mix of in person, online, and hybrid classes
* Range from first semester freshmen with no registration experience to seniors fitting in final requirements
* Access the system on both laptops and phones, often in short sessions between other obligations
* Includes students who use assistive technology such as screen readers, screen magnifiers, or keyboard only navigation

**Secondary users:** Academic advisors who help students build schedules.

## Core User Tasks

1. **Find a course:** Search for a specific required course by subject and number.
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

* Task completion rate and time on task from 2 observed user sessions: [fill in after sessions]
* Direct user quotes and observed breakdown points: [fill in after sessions]
* Heuristic violations with severity ratings: [fill in after evaluation]
* WCAG 2.1 AA failures from axe DevTools, WAVE, and manual checks: [fill in after audit]

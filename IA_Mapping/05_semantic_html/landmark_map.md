# Semantic HTML and ARIA Landmark Map

The wireframes are built as real semantic HTML (`../04_wireframes/src/*.html`), so this map is the actual structure, not a separate plan. Open any page with `?annotate` at the end of the URL to see landmarks, tab order, and ARIA states drawn on top.

## Shared Page Skeleton

Every screen uses this structure. Only the contents of `<main>` and the optional `<aside>` change.

```html
<body>
  <a class="skip" href="#main">Skip to main content</a>          <!-- tab stop 1 -->

  <header class="site">                                          <!-- role=banner -->
    <a href="home.html">Weber State Registration</a>
    <button aria-haspopup="listbox" aria-expanded="false">Spring 2027</button>
    <nav aria-label="Utility">                                  <!-- role=navigation -->
      <ul> Help and Glossary | Contact My Advisor | Sign Out </ul>
    </nav>
  </header>

  <nav class="primary" aria-label="Primary">                    <!-- role=navigation -->
    <ul>
      <li><a href="home.html">Registration Home</a></li>
      <li><a href="find.html" aria-current="page">Find Classes</a></li>
      <li><a href="schedule.html">My Schedule
            <span aria-hidden="true">2</span><span class="sr-only">(2 pending)</span></a></li>
      <li><a href="degree.html">My Degree</a></li>
      <li><a href="money.html">Finances</a></li>
    </ul>
  </nav>

  <nav class="crumbs" aria-label="Breadcrumb">                  <!-- role=navigation -->
    <ol>
      <li><a href="home.html">Registration Home</a></li>
      <li><a href="find.html" aria-current="page">Find Classes</a></li>
    </ol>
  </nav>

  <main id="main" tabindex="-1">                                <!-- role=main, skip link target -->
    <h1>Find Classes</h1>
    <form role="search" aria-label="Class search"> ... </form>   <!-- role=search -->
    <section aria-labelledby="res-h">                            <!-- role=region -->
      <h2 id="res-h">CS 2420 Data Structures</h2>
      <p role="status" aria-live="polite">3 sections found</p>
      <article aria-labelledby="s1-title"> ... </article>        <!-- one per section -->
    </section>
  </main>

  <aside aria-labelledby="aside-h">                             <!-- role=complementary -->
    <h2 id="aside-h">My Schedule</h2> ...
  </aside>

  <footer class="site"> ... </footer>                            <!-- role=contentinfo -->
</body>
```

## Landmarks Per Screen

| Screen | header | nav (Utility, Primary, Breadcrumb) | main | aside | form role=search | Labelled sections | footer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| W1 Registration Home | Yes | Utility, Primary | Yes | No | No | Registration date, Holds, My classes, Next steps | Yes |
| W2 Find Classes | Yes | All 3 | Yes | My Schedule summary | Class search | Results | Yes |
| W3 Find Classes after Add | Yes | All 3 | Yes | My Schedule summary | Class search | Results | Yes |
| W4 My Schedule review | Yes | All 3 | Yes | No | No | Pending, Registered, Week view | Yes |
| W5 Registration results | Yes | All 3 | Yes | No | No | Registered, Not registered | Yes |
| W6 My Degree | Yes | All 3 | Yes | No | No | Computer Science core, Help | Yes |

Every page has exactly one `<h1>`, headings never skip a level, and each `<nav>` has a unique `aria-label` so a screen reader's landmark list reads "Utility navigation, Primary navigation, Breadcrumb navigation" instead of three identical "navigation" entries.

## ARIA States and Properties

| Attribute | Where | Why |
| --- | --- | --- |
| `aria-current="page"` | Active primary nav link and last breadcrumb | Announces "current page" so screen reader users know where they are (WCAG 2.4.8 Location, 1.3.1) |
| `aria-expanded="false/true"` + `aria-controls` | Semester switcher, every Details button | Announces whether the collapsible content is open and which region it controls (4.1.2 Name, Role, Value) |
| `aria-haspopup="listbox"` | Semester switcher | Warns that the button opens a list of semesters |
| `role="status"` + `aria-live="polite"` | Result count on W2, "Added. Not registered yet." message on W3, prerequisite notice on W6 | Announces changes without moving focus (4.1.3 Status Messages). Fixes Phase 1 HE01: the student hears that Add did not register them. |
| `role="alert"` | Registration summary on W5 | Interrupts to announce "1 of 2 classes registered" right away. Fixes Phase 1 HE02 (vague full class error). |
| `aria-describedby` | Course number hint, CRN definition, Register button (drop rule), Join waitlist (full section message), conflicting Add button (conflict flag) | Reads the hint, warning, or reason along with the control's name (3.3.2 Labels or Instructions) |
| `.sr-only` text inside buttons | "Add to my schedule: CS 2420 Section 001", "Details for Section 002" | Gives every repeated button a unique name so a screen reader's button list is usable (2.4.6 Headings and Labels, 2.5.3 Label in Name keeps the visible words first) |
| `aria-hidden="true"` | Pending count badge, logo placeholder, annotation layer | Hides decoration, replaced by `.sr-only` text where meaning matters |
| `aria-disabled="true"` | "Added (pending)" button on W3 | Announces the button as unavailable while keeping keyboard focus on it |
| `tabindex="-1"` | `<main>`, W5 `<h1>` | Lets the skip link and the post-Submit focus move land there without adding a tab stop |

## Focus Management After Actions

| Action | Where focus goes | What is announced |
| --- | --- | --- |
| Skip to main content | `<main id="main">` | Page `<h1>` |
| Add to my schedule | Stays on the button, which changes to "Added (pending)" with `aria-disabled="true"`. The real `disabled` attribute is avoided because it would drop focus to the top of the page. | Status message: "CS 2420 Section 001 added to My Schedule. Not registered yet." |
| Details / Hide details | Stays on the button | "expanded" or "collapsed" |
| Register for 2 classes | W5 `<h1>` "Registration results" | Alert: "1 of 2 classes registered. 1 class needs your attention." |
| Join waitlist | Stays on the button, which becomes "On waitlist, position 4" | Status message with waitlist position |

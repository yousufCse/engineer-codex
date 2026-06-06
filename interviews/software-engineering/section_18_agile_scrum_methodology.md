# Section 18 — Agile, Scrum & Methodology

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. This is a process topic — examples are real scenarios, not code.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a step-by-step explanation with real examples.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For Agile, interviewers want *real experience*, not textbook definitions. Tie each answer to "on my team we did X" — that's far more convincing than reciting the manifesto.

---

<a id="toc"></a>

## Table of Contents

**A. Agile foundations**
1. [The Agile Manifesto](#q1) · *Very common*
2. [Waterfall vs Agile](#q2) · *Very common*

**B. Scrum roles & artifacts**
3. [The Scrum framework (overview)](#q3) · *Very common*
4. [The 3 Scrum roles](#q4) · *Very common*
5. [Scrum artifacts](#q5) · *Common*

**C. Sprint & ceremonies**
6. [What is a Sprint?](#q6) · *Very common*
7. [Sprint Planning](#q7) · *Common*
8. [Daily Standup](#q8) · *Very common*
9. [Sprint Review vs Retrospective](#q9) · *Common*
10. [Backlog refinement](#q10) · *Common*

**D. Estimation & tracking**
11. [User stories (format, AC, DoD)](#q11) · *Very common*
12. [Story points & planning poker](#q12) · *Very common*
13. [Velocity](#q13) · *Common*
14. [Burndown chart](#q14) · *Common*

**E. Practice & tools**
15. [Kanban vs Scrum (WIP limits)](#q15) · *Common*
16. [Handling changing requirements mid-sprint](#q16) · *Common*
17. [Technical debt in a sprint team](#q17) · *Common*
18. [Jira (epics, stories, tasks)](#q18) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

**Stage 1 — The foundations (start here).**
→ [Q1 Agile Manifesto](#q1) · [Q2 Waterfall vs Agile](#q2) · [Q3 Scrum overview](#q3)

**Stage 2 — The Scrum machinery.**
→ [Q4 Roles](#q4) · [Q5 Artifacts](#q5) · [Q6 Sprint](#q6)

**Stage 3 — The ceremonies.**
→ [Q7 Planning](#q7) · [Q8 Standup](#q8) · [Q9 Review vs Retro](#q9) · [Q10 Refinement](#q10)

**Stage 4 — Estimation & tracking.**
→ [Q11 User stories](#q11) · [Q12 Story points](#q12) · [Q13 Velocity](#q13) · [Q14 Burndown](#q14)

**Stage 5 — Real-world practice.**
→ [Q15 Kanban](#q15) · [Q16 Changing requirements](#q16) · [Q17 Tech debt](#q17) · [Q18 Jira](#q18)

**Short on time?** Review [Q1](#q1) · [Q2](#q2) · [Q3](#q3) · [Q8](#q8) · [Q11](#q11) · [Q12](#q12), then the [Cheat Sheet](#cheatsheet).

---

# A. Agile foundations

---

<a id="q1"></a>
## 1. What is the Agile Manifesto?

> Very common · Easy

**Short answer (say this):**
"The Agile Manifesto (2001) is a set of values for building software in a flexible, customer-focused way. Its heart is four value statements — like 'individuals and interactions over processes and tools' and 'responding to change over following a plan'. It doesn't say the right side is worthless; it says the left side matters more."

**Let's understand it fully:**

**Step 1 — A real-life picture: cooking by taste.**
A rigid recipe (Waterfall) is followed exactly even if the dish tastes wrong. Agile means you taste as you cook and adjust — you respond to feedback instead of blindly following the plan.

**Step 2 — The 4 values (each is "X over Y").**

| We value... | over... |
|---|---|
| Individuals and interactions | processes and tools |
| Working software | comprehensive documentation |
| Customer collaboration | contract negotiation |
| Responding to change | following a plan |

The key phrase: "while there is value in the items on the right, we value the items on the left more."

**Step 3 — The 12 principles (the gist).**
They expand the values: deliver working software frequently, welcome changing requirements, work closely with the business, build around motivated people, reflect and improve regularly, and keep a sustainable pace.

**Step 4 — What Agile is NOT.**
Agile isn't "no planning" or "no documentation." It's *less upfront rigidity* and *more frequent feedback and adjustment*.

**Why interviewers ask:** It checks you understand Agile's *spirit* (feedback and flexibility), not just buzzwords.

**Common mistake:** Saying Agile means "no documentation" or "no plan." It means valuing working software and adaptability *more*, not throwing the others away.

**Follow-ups they may ask:**
- *"Agile vs Scrum?"* → Agile is the mindset (values); Scrum is one specific framework that implements it ([Q3](#q3)).

**Related:** [Q2 — Waterfall vs Agile](#q2) · [Q3 — Scrum](#q3)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What is the difference between Waterfall and Agile? When is each appropriate?

> Very common · Medium

**Short answer (say this):**
"Waterfall is sequential — you finish all requirements, then design, then build, then test, in fixed phases. Agile is iterative — you build and release in small cycles, getting feedback constantly. Waterfall suits projects with fixed, well-understood requirements (like regulated or hardware projects); Agile suits projects where requirements evolve, which is most software."

**Let's understand it fully:**

**Step 1 — Waterfall — one big sequence.**

```
Requirements → Design → Build → Test → Release
   (each phase finishes before the next starts; change is expensive)
```

**Step 2 — Agile — small repeating cycles.**

```
[plan → build → test → release → feedback] → repeat every 1–4 weeks
   (you adjust each cycle based on real feedback)
```

**Step 3 — The trade-offs.**

| | Waterfall | Agile |
|---|---|---|
| Requirements | fixed upfront | evolve over time |
| Feedback | late (after release) | continuous |
| Change | expensive, discouraged | expected, welcomed |
| Risk | found late | found early |

**Step 4 — When to use each.**
- **Waterfall** — requirements are fixed and clear, change is costly (medical devices, construction, fixed-scope contracts).
- **Agile** — requirements will change and you want early feedback (most apps and products).

**Why interviewers ask:** It tests that you can match the process to the project, not dogmatically push one.

**Common mistake:** Claiming Agile is always better. For truly fixed-scope, safety-critical projects, Waterfall's upfront rigor can be the right choice.

**Follow-ups they may ask:**
- *"Can you mix them?"* → Yes — "hybrid" approaches use upfront planning for fixed parts and Agile cycles for evolving parts.

**Related:** [Q1 — Agile Manifesto](#q1) · [Q19 (SDLC) — models](section_19_sdlc_interview_prep.md#q1)

[↑ Back to top](#toc)

---

# B. Scrum roles & artifacts

---

<a id="q3"></a>
## 3. Explain the Scrum framework (overview).

> Very common · Medium

**Short answer (say this):**
"Scrum is the most popular Agile framework. Work is done in fixed-length Sprints (usually 1–4 weeks). It has three roles (Product Owner, Scrum Master, Developers), three artifacts (Product Backlog, Sprint Backlog, Increment), and a set of events (Sprint Planning, Daily Standup, Sprint Review, Retrospective). The goal is to deliver a working increment every Sprint."

**Let's understand it fully:**

**Step 1 — The big picture.**

```
Product Backlog → [Sprint Planning] → Sprint Backlog
   → daily work + [Daily Standup] (1–4 weeks)
   → working Increment → [Sprint Review] + [Retrospective] → repeat
```

**Step 2 — The three parts.**
- **Roles** — Product Owner (the "what"), Scrum Master (the process coach), Developers (the "how"). See [Q4](#q4).
- **Artifacts** — Product Backlog, Sprint Backlog, Increment. See [Q5](#q5).
- **Events** — Planning, Daily Standup, Review, Retrospective (plus the Sprint itself). See [Q7](#q7)–[Q9](#q9).

**Step 3 — The rhythm.**
Each Sprint is a complete mini-cycle: plan it, build it, show it (Review), improve how you work (Retrospective), repeat. Every Sprint should end with something potentially shippable.

**Why interviewers ask:** It's the baseline Scrum question; they confirm you know the roles, artifacts, and events fit together.

**Common mistake:** Calling the Scrum Master a "boss" or "project manager." The Scrum Master is a facilitator/coach, not a manager ([Q4](#q4)).

**Follow-ups they may ask:**
- *"How long is a Sprint?"* → Usually 1–4 weeks, most commonly 2 ([Q6](#q6)).

**Related:** [Q4 — roles](#q4) · [Q5 — artifacts](#q5) · [Q6 — sprint](#q6)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. What are the three Scrum roles?

> Very common · Medium

**Short answer (say this):**
"There are three: the Product Owner owns the 'what' — the backlog and priorities, representing the customer. The Scrum Master owns the 'how we work' — coaching the team and removing obstacles, not bossing people. The Developers own the 'how' — they build the increment and decide how much they can commit to."

**Let's understand it fully:**

**Step 1 — Product Owner (PO) — the voice of the customer.**
- Owns and prioritizes the **Product Backlog**.
- Decides *what* gets built and in what order (maximizes value).
- Says yes/no to scope; the single decision-maker on priorities.

**Step 2 — Scrum Master (SM) — the coach.**
- Facilitates the events and protects the team's process.
- **Removes blockers** (impediments) so developers can work.
- Coaches the team on Scrum; serves the team, does **not** assign tasks or manage people.

**Step 3 — Developers — the builders.**
- Do the actual work (design, code, test).
- **Self-organizing**: they decide how to do the work and how much to commit to each Sprint.
- Cross-functional: together they have all skills needed to deliver.

**Step 4 — The clear line.**
PO = *what* and *why*. Developers = *how* and *how much*. SM = *helps the process work*. Mixing these (e.g. SM dictating tasks, or PO promising dates to clients without the team) breaks Scrum.

**Why interviewers ask:** Confusing the roles (especially SM as a manager) is the most common Scrum mistake; they check you understand the boundaries.

**Common mistake:** Treating the Scrum Master as a traditional project manager who assigns work. The SM facilitates and unblocks; the team self-organizes.

**Follow-ups they may ask:**
- *"Who decides the sprint scope?"* → The PO sets priority order; the **Developers** decide how much they can take on.

**Related:** [Q3 — Scrum overview](#q3) · [Q5 — artifacts](#q5)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What are the Scrum artifacts?

> Common · Easy–Medium

**Short answer (say this):**
"There are three: the Product Backlog is the full, prioritized list of everything the product might need. The Sprint Backlog is the subset the team commits to for the current Sprint, plus the plan to do it. The Increment is the working, potentially shippable result at the end of the Sprint."

**Let's understand it fully:**

**Step 1 — Product Backlog — the master to-do list.**
- Owned by the Product Owner.
- Everything that *might* be built, ordered by priority/value.
- Living — items are added, removed, and re-ordered continuously.

**Step 2 — Sprint Backlog — this Sprint's plan.**
- The items pulled from the Product Backlog for *this* Sprint, plus the Sprint Goal.
- Owned by the Developers; they decide what's realistic.
- Doesn't change much mid-Sprint (the goal is protected — see [Q16](#q16)).

**Step 3 — Increment — the working result.**
- The sum of all completed work this Sprint, meeting the **Definition of Done** ([Q11](#q11)).
- Must be *potentially shippable* — actually working, not half-done.

**Step 4 — The flow.**

```
Product Backlog (everything) → Sprint Backlog (this sprint) → Increment (done & working)
```

**Why interviewers ask:** It tests whether you understand what the team commits to and what "done" means each Sprint.

**Common mistake:** Confusing Product Backlog (everything, PO-owned) with Sprint Backlog (this Sprint, team-owned).

**Follow-ups they may ask:**
- *"Who owns each?"* → Product Backlog = PO; Sprint Backlog = Developers.

**Related:** [Q4 — roles](#q4) · [Q10 — refinement](#q10) · [Q11 — Definition of Done](#q11)

[↑ Back to top](#toc)

---

# C. Sprint & ceremonies

---

<a id="q6"></a>
## 6. What is a Sprint, how long is it, and what happens if the goal isn't met?

> Very common · Medium

**Short answer (say this):**
"A Sprint is a fixed time-box, usually 2 weeks, in which the team builds a working increment toward a Sprint Goal. The length is fixed and doesn't get extended. If the goal isn't met, you don't extend the Sprint — unfinished work goes back to the backlog and is re-planned, and the Retrospective looks at why."

**Let's understand it fully:**

**Step 1 — A fixed time-box.**
A Sprint has a set length (commonly 2 weeks; 1–4 is normal). The length stays consistent so the team builds a steady rhythm and predictable velocity.

**Step 2 — Key rules.**
- No changes that endanger the **Sprint Goal**.
- Scope can be clarified, but the goal is protected.
- It ends on the planned date — never extended.

**Step 3 — What if the goal isn't met?**
- The Sprint still **ends on time** — you don't extend it.
- Unfinished items go **back to the Product Backlog** to be re-estimated and re-prioritized.
- The **Retrospective** ([Q9](#q9)) examines *why* (over-commitment? blockers? unclear stories?) and the team adjusts.

**Step 4 — Why fixed length matters.**
A consistent Sprint length makes velocity meaningful ([Q13](#q13)) and creates a reliable delivery cadence. Extending Sprints hides problems instead of surfacing them.

**Why interviewers ask:** It tests the core Scrum discipline — fixed time-boxes and honest handling of unfinished work.

**Common mistake:** Saying "we extend the Sprint a few days to finish." That breaks the time-box; re-plan instead.

**Follow-ups they may ask:**
- *"Can you cancel a Sprint?"* → Only the PO can, and only if the Sprint Goal becomes obsolete — it's rare.

**Related:** [Q3 — Scrum overview](#q3) · [Q13 — velocity](#q13) · [Q16 — changing requirements](#q16)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. What happens in Sprint Planning?

> Common · Easy–Medium

**Short answer (say this):**
"Sprint Planning kicks off the Sprint. The whole team agrees on a Sprint Goal, the Product Owner presents the top-priority backlog items, and the Developers pull in as much as they can realistically finish — based on their velocity. The output is the Sprint Backlog and a shared plan."

**Let's understand it fully:**

**Step 1 — The two questions it answers.**
1. **What** can we deliver this Sprint? (the Sprint Goal + selected items)
2. **How** will we do it? (breaking items into tasks)

**Step 2 — Who does what.**
- **PO** — presents the highest-priority, refined items and clarifies them.
- **Developers** — estimate, decide how much they can commit to, and break items into tasks.
- **SM** — facilitates and keeps it time-boxed.

**Step 3 — Use velocity to stay realistic.**
The team uses its average velocity ([Q13](#q13)) to avoid over-committing. Pulling in 40 points when you average 25 sets the Sprint up to fail.

**Step 4 — The output.**
A clear **Sprint Goal** and a **Sprint Backlog** everyone agrees is achievable.

**Why interviewers ask:** It tests whether you plan realistically and understand who decides scope (the team, guided by the PO's priorities).

**Common mistake:** The PO or a manager *pushing* more work onto the team than its velocity supports. Commitment is the team's call.

**Follow-ups they may ask:**
- *"How long is planning?"* → Time-boxed, roughly 2 hours per week of Sprint (so ~4 hours for a 2-week Sprint).

**Related:** [Q6 — sprint](#q6) · [Q12 — story points](#q12) · [Q13 — velocity](#q13)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is the Daily Standup, and what do you say in it?

> Very common · Easy

**Short answer (say this):**
"The Daily Standup (Daily Scrum) is a short, 15-minute meeting where the team syncs on progress toward the Sprint Goal. Classically each person answers three things: what I did yesterday, what I'll do today, and any blockers. It's for coordination, not status reporting to a manager."

**Let's understand it fully:**

**Step 1 — The three questions.**
1. What did I do yesterday (toward the goal)?
2. What will I do today?
3. What's blocking me?

**Step 2 — Keep it short and focused.**
- Time-boxed to **15 minutes**.
- It's a sync between *developers*, not a report to the boss.
- Detailed discussions are taken "offline" after standup, with only the people involved.

**Step 3 — Common anti-patterns to avoid.**
- Turning it into a status report *to* the Scrum Master or manager.
- Long problem-solving in the meeting (take it offline).
- People only listening for their turn instead of the goal.

**Step 4 — The real purpose.**
It surfaces blockers early and keeps everyone aligned on the Sprint Goal. The format matters less than the outcome: a coordinated team with blockers visible.

**Why interviewers ask:** Standups are daily; they check you treat it as team coordination, not a micro-management status meeting.

**Common mistake:** Treating it as a status meeting *for the manager*, or letting it run long with deep technical debates.

**Follow-ups they may ask:**
- *"Remote standup tips?"* → Keep it on time, camera on, and post written updates async if time zones don't overlap.

**Related:** [Q3 — Scrum overview](#q3) · [Q14 — burndown](#q14)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What is the difference between a Sprint Review and a Sprint Retrospective?

> Common · Medium

**Short answer (say this):**
"The Sprint Review is about the *product* — the team demos the working increment to stakeholders and gets feedback on what to build next. The Retrospective is about the *process* — the team privately reflects on how they worked and picks improvements. Review = the what; Retrospective = the how."

**Let's understand it fully:**

**Step 1 — Sprint Review — show the work, get feedback.**
- Held at the end of the Sprint.
- The team **demos the increment** to the PO and stakeholders.
- Goal: get feedback and adjust the Product Backlog. It's about the *product*.

**Step 2 — Sprint Retrospective — improve how we work.**
- Held after the Review, **team-only** (a safe space).
- The team reflects: what went well, what didn't, what to improve.
- Goal: pick 1–2 concrete improvements for the next Sprint. It's about the *process*.

**Step 3 — The easy way to remember.**

| | Sprint Review | Retrospective |
|---|---|---|
| Focus | the product (what we built) | the process (how we worked) |
| Audience | team + stakeholders | team only |
| Output | feedback, backlog updates | process improvements |

**Step 4 — Why the Retro is private.**
Honest reflection needs psychological safety. With stakeholders present, people hide problems. Team-only keeps it candid.

**Why interviewers ask:** People often confuse the two; explaining the product/process split shows real Scrum understanding.

**Common mistake:** Mixing them — demoing in the Retro, or doing process improvement in front of stakeholders.

**Follow-ups they may ask:**
- *"A retro format you've used?"* → "Start / Stop / Continue", or "What went well / what didn't / actions."

**Related:** [Q8 — standup](#q8) · [Q17 — tech debt](#q17)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What is Backlog Refinement (grooming)?

> Common · Medium

**Short answer (say this):**
"Backlog refinement is the ongoing activity of getting backlog items ready for future Sprints — clarifying them, splitting big ones, adding acceptance criteria, and estimating. The PO and Developers do it together, usually a small slice of time each week, so Sprint Planning is fast and items are 'ready'."

**Let's understand it fully:**

**Step 1 — The goal: a 'ready' backlog.**
Refinement makes the top of the backlog clear, small enough, and estimated — so when Planning comes, the team can pick items without long discussion.

**Step 2 — What happens in it.**
- **Clarify** vague items (the PO answers questions).
- **Split** big items (epics/large stories) into smaller ones.
- **Add acceptance criteria** (what "done" means).
- **Estimate** with story points ([Q12](#q12)).

**Step 3 — Who and how often.**
- The **PO** and **Developers** together (SM facilitates).
- Ongoing — often ~1 short session per week, kept to about 10% of the team's time.

**Step 4 — Definition of Ready.**
A "ready" item is clear, small, estimated, and has acceptance criteria — so it can be safely pulled into a Sprint. Refinement produces ready items.

**Why interviewers ask:** It tests whether you keep the backlog healthy, which makes Sprints predictable.

**Common mistake:** Skipping refinement, so Sprint Planning turns into a long, chaotic meeting of half-understood items.

**Follow-ups they may ask:**
- *"Definition of Ready vs Done?"* → Ready = the item is good enough to start; Done = the work is complete and shippable ([Q11](#q11)).

**Related:** [Q5 — backlog](#q5) · [Q11 — acceptance criteria](#q11) · [Q12 — estimation](#q12)

[↑ Back to top](#toc)

---

# D. Estimation & tracking

---

<a id="q11"></a>
## 11. What is a user story? Explain the format, acceptance criteria, and Definition of Done.

> Very common · Medium

**Short answer (say this):**
"A user story describes a feature from the user's point of view, in the format 'As a [user], I want [goal], so that [benefit].' Acceptance criteria are the specific conditions that make it correct. The Definition of Done is the team-wide checklist (tested, reviewed, documented) that applies to *every* story before it counts as complete."

**Let's understand it fully:**

**Step 1 — The user story format.**

```
As a [type of user], I want [some goal], so that [some benefit].

Example:
As a shopper, I want to save items to a wishlist,
so that I can buy them later.
```

It focuses on the *who* and *why*, not the technical *how*.

**Step 2 — Acceptance Criteria (AC) — when is THIS story correct?**
Specific, testable conditions for this one story. A common format is Given/When/Then:

```
Given I am logged in,
When I tap the heart icon on a product,
Then the product appears in my wishlist.
```

**Step 3 — Definition of Done (DoD) — applies to EVERY story.**
A shared checklist the team agrees on, e.g.:
- Code written and peer-reviewed.
- Tests written and passing.
- Meets acceptance criteria.
- Merged and deployable.

**Step 4 — AC vs DoD (the key distinction).**
- **Acceptance Criteria** = specific to *one* story (what makes this feature right).
- **Definition of Done** = global, applies to *all* stories (the quality bar).

**Why interviewers ask:** Stories, AC, and DoD are the daily language of Agile teams; they check you write clear, testable work items.

**Common mistake:** Confusing AC (per-story) with DoD (team-wide). Or writing stories that describe technical tasks instead of user value.

**Follow-ups they may ask:**
- *"What makes a good story?"* → INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable.

**Related:** [Q10 — refinement](#q10) · [Q12 — story points](#q12) · [Q5 — increment & DoD](#q5)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. What are story points, why use them over hours, and what is planning poker?

> Very common · Medium

**Short answer (say this):**
"Story points estimate the *relative size* of work — its effort, complexity, and uncertainty — instead of exact hours. Teams prefer them because people are bad at estimating hours but decent at comparing sizes, and points don't pretend to be a precise promise. Planning poker is how the team estimates them together to surface different views."

**Let's understand it fully:**

**Step 1 — Points are relative size, not time.**
Like T-shirt sizes (S, M, L) or a Fibonacci scale (1, 2, 3, 5, 8, 13). A 2-point story is "about twice the size" of a 1-point story — not "2 hours."

**Step 2 — Why points over hours.**
- People estimate *relative* size better than absolute hours.
- Points cover effort + complexity + uncertainty, not just typing time.
- Hours feel like a precise promise (and create blame when wrong); points are honest about uncertainty.
- The team's velocity ([Q13](#q13)) turns points into predictable planning over time.

**Step 3 — Planning Poker.**
1. The PO reads a story.
2. Each developer privately picks a card (1, 2, 3, 5, 8...).
3. Everyone reveals at once.
4. If estimates differ a lot, the high and low explain their thinking, then re-vote.

The discussion is the real value — it surfaces hidden complexity and shared understanding.

**Step 4 — Why hide-then-reveal.**
Voting privately first stops the loudest or most senior person from anchoring everyone. Differences spark useful discussion.

**Why interviewers ask:** Estimation is a constant source of pain; they check you understand relative estimation and team-based estimating.

**Common mistake:** Converting points directly to hours ("a point = 4 hours"), which throws away the whole benefit and reintroduces false precision.

**Follow-ups they may ask:**
- *"Why Fibonacci numbers?"* → The growing gaps reflect that bigger items are far more uncertain — you can't meaningfully say "21 vs 22".

**Related:** [Q11 — user stories](#q11) · [Q13 — velocity](#q13) · [Q7 — planning](#q7)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. What is sprint velocity, and how is it used for planning?

> Common · Medium

**Short answer (say this):**
"Velocity is the average number of story points a team completes per Sprint. You use it to plan realistically — if a team averages 25 points, they shouldn't commit to 40. It's a planning tool for the team, not a productivity score to compare teams or pressure people."

**Let's understand it fully:**

**Step 1 — How it's measured.**
Add up the points of all *completed* stories each Sprint. Average the last few Sprints to get velocity.

```
Sprint 1: 22 done   Sprint 2: 26 done   Sprint 3: 24 done
Velocity ≈ 24 points per sprint
```

**Step 2 — How it's used.**
At Planning, the team pulls in roughly its velocity worth of work — not more. Over several Sprints, velocity also lets you forecast roughly when a backlog of N points will be finished.

**Step 3 — Important caveats.**
- Velocity is **team-specific** — never compare two teams' velocity (their points mean different things).
- It's a **planning aid**, not a target. Pushing for "higher velocity" makes teams inflate estimates, which destroys its value.
- It stabilizes only after a few Sprints with a steady team.

**Why interviewers ask:** It tests realistic planning and whether you'd misuse velocity as a performance metric (a classic anti-pattern).

**Common mistake:** Using velocity to compare teams or as a KPI to pressure the team — both corrupt the estimates and the metric.

**Follow-ups they may ask:**
- *"What lowers velocity unfairly?"* → Holidays, team changes, lots of unplanned bug work — context matters.

**Related:** [Q12 — story points](#q12) · [Q7 — planning](#q7) · [Q14 — burndown](#q14)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. What is a burndown chart?

> Common · Easy

**Short answer (say this):**
"A burndown chart shows how much work is left over time — the remaining work 'burns down' toward zero as the Sprint progresses. It gives a quick visual of whether the team is on track to finish the Sprint, and helps spot problems early."

**Let's understand it fully:**

**Step 1 — What it shows.**
- X-axis: days of the Sprint.
- Y-axis: remaining work (story points or tasks).
- A line that should slope down to zero by the last day.

```
points
 25 | \
 20 |  \___        actual line above the ideal = behind schedule
 15 |      \  .    (the dotted line is the "ideal" steady burn)
 10 |       \ .
  5 |        \.
  0 |_________\_____ days
    1  2  3  4  5
```

**Step 2 — How to read it.**
- **Above** the ideal line → behind schedule (work isn't finishing fast enough).
- **Below** → ahead.
- A **flat** line → work is stuck (a blocker, or nothing being completed).

**Step 3 — Why it helps.**
It surfaces trouble early — a flat or rising line tells the team to investigate now, not on the last day. It's a conversation starter at standup, not a judgment.

**Step 4 — Burndown vs burnup.**
A **burnup** chart shows work *completed* rising toward the total, and can also show scope changes (the total line moving) — useful when scope shifts.

**Why interviewers ask:** It tests whether you track progress and act on early warnings.

**Common mistake:** Treating a perfect burndown as the goal. The chart is a signal to start conversations, not a target to game.

**Follow-ups they may ask:**
- *"Burndown vs burnup?"* → Burndown shows work remaining; burnup shows work done plus total scope (reveals scope creep).

**Related:** [Q13 — velocity](#q13) · [Q8 — standup](#q8)

[↑ Back to top](#toc)

---

# E. Practice & tools

---

<a id="q15"></a>
## 15. What is Kanban, how does it differ from Scrum, and what are WIP limits?

> Common · Medium

**Short answer (say this):**
"Kanban is a flow-based Agile method: work items move across a board (To Do → In Progress → Done) continuously, with no fixed Sprints. WIP (Work In Progress) limits cap how many items can be in each column at once, which forces the team to finish work before starting new work. Kanban suits continuous, unpredictable work like support; Scrum suits planned feature delivery."

**Let's understand it fully:**

**Step 1 — Kanban = continuous flow.**
There are no Sprints. Items flow across the board as capacity frees up. You release whenever something's done, not on a Sprint boundary.

**Step 2 — WIP limits — the key idea.**
Each column has a maximum (e.g. "In Progress: max 3"). If it's full, you can't start new work — you must finish or unblock something first.

```
To Do        In Progress (max 3)     Done
[a][b][c]    [d][e][f]   ← full!     [g][h]
             (can't pull a new item until one moves to Done)
```

This stops everyone starting everything and finishing nothing, and exposes bottlenecks.

**Step 3 — Kanban vs Scrum.**

| | Scrum | Kanban |
|---|---|---|
| Cadence | fixed Sprints | continuous flow |
| Roles | PO, SM, Developers | no required roles |
| Change | not mid-Sprint | anytime |
| Best for | planned feature work | support, ops, steady streams |

**Step 4 — When to use Kanban.**
For interrupt-driven or continuous work (bug fixing, support, ops) where fixed Sprint commitments don't fit. Some teams blend them ("Scrumban").

**Why interviewers ask:** It tests whether you can pick the right Agile flavour for the work, and the powerful idea of limiting WIP.

**Common mistake:** Thinking Kanban means "no process." It has strong discipline — especially WIP limits and measuring flow.

**Follow-ups they may ask:**
- *"Why limit WIP?"* → Too much parallel work slows everything (context switching) and hides bottlenecks; limiting it speeds delivery.

**Related:** [Q3 — Scrum overview](#q3) · [Q6 — sprint](#q6)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. How do you handle changing requirements mid-sprint?

> Common · Medium

**Short answer (say this):**
"Agile welcomes change, but mid-Sprint the Sprint Goal is protected. For a small, urgent change I'd discuss with the PO and team — if something must come in, something of equal size usually comes out. Anything non-urgent goes to the backlog for the next Sprint. The point is to protect focus, not to refuse change."

**Let's understand it fully:**

**Step 1 — The principle vs the practice.**
Agile *welcomes* changing requirements — but Scrum *protects the Sprint Goal* so the team can focus. These aren't a contradiction: you welcome change at the backlog level, but don't thrash the current Sprint.

**Step 2 — The practical options.**
- **Non-urgent change** → add it to the Product Backlog; prioritize for a future Sprint.
- **Small urgent change** → the PO and team agree to swap it in, taking out work of similar size (a trade, not an addition).
- **Critical/emergency** (production down, security) → the PO may cancel or re-plan the Sprint; rare, but it happens.

**Step 3 — Who decides.**
The **Product Owner** decides priorities, but the **team** must agree the change is feasible without breaking the goal. It's a conversation, not a command.

**Step 4 — Why protect the Sprint.**
Constant mid-Sprint changes mean nothing ever finishes (everything is 80% done). The short Sprint length already limits how long any change has to wait — usually days.

**Why interviewers ask:** It tests the balance between flexibility and focus — a real tension every team faces.

**Common mistake:** Either rigidly refusing all change ("not in this Sprint, period") or accepting every interruption (so the team thrashes and finishes nothing).

**Follow-ups they may ask:**
- *"What if the change makes the Sprint Goal pointless?"* → The PO can cancel the Sprint and re-plan; it's the one clean way to fully change direction.

**Related:** [Q6 — sprint goal](#q6) · [Q4 — PO role](#q4) · [Q1 — welcoming change](#q1)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. What is technical debt, and how do you manage it in a sprint-based team?

> Common · Medium

**Short answer (say this):**
"Technical debt is the cost of shortcuts — code written quickly that will slow you down later, like borrowing time now and paying interest in future bugs and slow changes. You manage it by making it visible (tracking it), and budgeting a slice of each Sprint (say 10–20%) to pay it down steadily, while preventing new debt with reviews and a strong Definition of Done."

**Let's understand it fully:**

**Step 1 — A real-life picture: borrowing money.**
A shortcut delivers faster today (borrowing), but you pay interest later — every future change in that messy area takes longer and risks bugs. A little debt can be a smart trade; too much cripples the team.

**Step 2 — Common sources in Flutter projects.**
- Skipping tests to hit a deadline.
- Copy-pasted widgets/logic instead of reusable ones.
- Outdated packages, no architecture, business logic in widgets.

**Step 3 — How to manage it in Sprints.**
- **Make it visible** — track debt items in the backlog, don't keep them in your head.
- **Budget for it** — reserve ~10–20% of each Sprint for paying down debt, so it doesn't pile up.
- **Pay as you go** — the boy scout rule: improve the code near what you're already touching ([Q12 Clean Code](section_16_clean_code.md#q12)).
- **Prevent new debt** — code reviews and a strong Definition of Done.

**Step 4 — Frame it to the business.**
Don't say "we want to clean code." Say "this messy module causes most of our bugs and slows new features; fixing it will speed delivery." Tie debt to business cost.

**Why interviewers ask:** Senior engineers balance speed with sustainability; they want to see you manage debt deliberately, not ignore it or obsess over it.

**Common mistake:** Either ignoring debt until the codebase is unworkable, or demanding a big "stop everything and refactor" sprint (risky and usually rejected).

**Follow-ups they may ask:**
- *"How do you convince the PO to allocate time?"* → Show the cost in bug rates and slower delivery; propose a small, steady budget ([Q3 Refactoring](section_15_code_smells_refactoring.md#q3)).

**Related:** [Q3 (Refactoring) — convince a team](section_15_code_smells_refactoring.md#q3) · [Q12 (Clean Code) — boy scout rule](section_16_clean_code.md#q12)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. How do you use Jira? Explain epics, stories, tasks, and the board.

> Common · Easy–Medium

**Short answer (say this):**
"Jira is the most common tool for tracking Agile work. Work is organized in a hierarchy: an Epic is a large body of work, broken into Stories (user-facing features), which can be broken into Tasks/Subtasks. The board visualizes items moving across columns (To Do → In Progress → Done) so the whole team sees status."

**Let's understand it fully:**

**Step 1 — The hierarchy.**

```
Epic         "User authentication"          (large, spans many sprints)
 └─ Story    "As a user, I can log in"       (one feature, fits in a sprint)
     └─ Task        "Build the login form"   (a piece of work)
         └─ Subtask "Add email validation"   (a small step)
```

**Step 2 — Issue types.**
- **Epic** — a big theme, delivered over many Sprints.
- **Story** — a user-facing feature with acceptance criteria ([Q11](#q11)).
- **Task** — a technical piece of work (not always user-facing).
- **Bug** — something broken to fix.

**Step 3 — The board.**
A Scrum/Kanban board with columns (To Do, In Progress, In Review, Done). Each card is an issue; you drag it across as work progresses. The team reads status at a glance during standup.

**Step 4 — Keep it useful, not bureaucratic.**
The tool serves the team, not the other way around. Update tickets honestly, but don't drown in process — the goal is visibility, not paperwork.

**Why interviewers ask:** Most teams use Jira (or similar); they confirm you can work within a tracked Agile workflow.

**Common mistake:** Treating Jira as the goal — over-detailed tickets and status theatre — instead of as a simple visibility tool.

**Follow-ups they may ask:**
- *"Epic vs Story?"* → Epic = large, many Sprints; Story = one feature that fits in a Sprint.

**Related:** [Q11 — user stories](#q11) · [Q5 — backlog](#q5) · [Q15 — boards](#q15)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## Scrum at a glance

| Roles | Artifacts | Events |
|---|---|---|
| Product Owner (what) | Product Backlog | Sprint Planning |
| Scrum Master (process) | Sprint Backlog | Daily Standup |
| Developers (how) | Increment | Review + Retrospective |

## Easy-to-confuse pairs

| | A | B |
|---|---|---|
| Review vs Retro | product (demo) | process (improve) |
| Acceptance Criteria vs DoD | per-story | team-wide |
| Product vs Sprint Backlog | everything (PO) | this sprint (team) |
| Scrum vs Kanban | fixed sprints | continuous flow |
| Burndown vs Burnup | work remaining | work done + scope |

## One-line reminders

- **Agile** = working software + responding to change; not "no docs/plan". ([Q1](#q1))
- **Waterfall** = sequential, fixed scope; **Agile** = iterative, feedback-driven. ([Q2](#q2))
- **Scrum Master = coach/facilitator**, not a manager. ([Q4](#q4))
- **PO decides priority; the team decides how much** to commit. ([Q4](#q4), [Q7](#q7))
- **Sprint length is fixed** — don't extend; re-plan unfinished work. ([Q6](#q6))
- **Standup** = 15-min team sync (3 questions), not a status report to a boss. ([Q8](#q8))
- **Review = demo the product; Retro = improve the process** (team-only). ([Q9](#q9))
- **Story points = relative size, not hours**; estimate with planning poker. ([Q12](#q12))
- **Velocity** = avg points/sprint; a planning aid, never a cross-team KPI. ([Q13](#q13))
- **WIP limits** force finishing before starting — the heart of Kanban. ([Q15](#q15))
- **Protect the Sprint Goal** mid-sprint; swap, don't pile on. ([Q16](#q16))
- **Technical debt** = make it visible, budget ~10–20% per sprint. ([Q17](#q17))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Agile interviews probe real experience. Practice out loud:

1. *"Walk me through a Sprint you ran."* → planning → goal → daily standups → review/retro, with a real example.
2. *"A stakeholder demands a change on day 3 — what do you do?"* → protect the goal; swap with the PO if urgent, else backlog it.
3. *"Your velocity dropped — is the team slacking?"* → no; check holidays, blockers, scope; velocity isn't a performance score.
4. *"How do you stop tech debt piling up?"* → make it visible, budget a slice each sprint, strong DoD.
5. *"Scrum or Kanban for a support team?"* → Kanban — continuous flow with WIP limits fits interrupt-driven work.

Tying answers to "on my team we did X" — real, specific experience — beats textbook definitions every time, in both remote and BD interviews.

[↑ Back to top](#toc)

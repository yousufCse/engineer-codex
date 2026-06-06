# Section 22 — Senior Engineer Leadership & Behavioral

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. Behavioral answers use the **STAR** method with sample stories you can adapt.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply (or framing) to lead with.
- **Let's understand it fully** — your approach step by step, or a STAR breakdown with a sample story.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For leadership questions, show *judgment and empathy*, not just rules. For behavioral questions, use **STAR** (below) and **always end with a measurable result**. And use your *own real stories* — the samples here are templates to fill with your experience.

**The STAR method (for every behavioral question):**

| Letter | Meaning | Keep it... |
|---|---|---|
| **S — Situation** | the context/background | short (1–2 sentences) |
| **T — Task** | your specific goal/responsibility | clear |
| **A — Action** | what **you** did (use "I", not "we") | the longest part |
| **R — Result** | the outcome, with **numbers** | concrete and positive |

---

<a id="toc"></a>

## Table of Contents

**A. Technical leadership**
1. [Conducting a code review](#q1) · *Very common*
2. [Mentoring developers](#q2) · *Common*
3. [Handling a technical disagreement](#q3) · *Very common*
4. [Introducing a new technology](#q4) · *Common*
5. [Managing technical debt](#q5) · *Common*
6. [Balancing speed vs quality](#q6) · *Very common*
7. [Making & documenting architecture decisions](#q7) · *Common*
8. [Onboarding to a large codebase](#q8) · *Common*
9. [Reviewing a senior developer's PR](#q9) · *Common*

**B. Behavioral (STAR)**
10. [Tell me about yourself](#q10) · *Very common*
11. [Your biggest technical achievement](#q11) · *Very common*
12. [Led a project from scratch to production](#q12) · *Common*
13. [Fixed a critical production bug](#q13) · *Very common*
14. [Disagreed with your manager](#q14) · *Very common*
15. [Improved app performance](#q15) · *Common*
16. [A project that failed](#q16) · *Very common*
17. [Staying up to date](#q17) · *Common*
18. [Why this senior role?](#q18) · *Common*
19. [Where in 3–5 years?](#q19) · *Common*
20. [Your greatest weakness](#q20) · *Very common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

**Stage 1 — The leadership essentials (start here).**
→ [Q1 Code review](#q1) · [Q3 Disagreement](#q3) · [Q6 Speed vs quality](#q6)

**Stage 2 — Leading people & decisions.**
→ [Q2 Mentoring](#q2) · [Q4 New tech](#q4) · [Q5 Tech debt](#q5) · [Q7 Architecture decisions](#q7) · [Q8 Onboarding](#q8) · [Q9 Senior PR](#q9)

**Stage 3 — Your story (prepare 3–4 real ones).**
→ [Q10 About yourself](#q10) · [Q11 Achievement](#q11) · [Q12 Led a project](#q12) · [Q13 Production bug](#q13)

**Stage 4 — The tricky behavioral ones.**
→ [Q14 Disagree with manager](#q14) · [Q16 A failure](#q16) · [Q20 Weakness](#q20) · [Q15 Performance](#q15)

**Stage 5 — The closers.**
→ [Q17 Stay updated](#q17) · [Q18 Why this role](#q18) · [Q19 3–5 years](#q19)

**Short on time?** Prepare [Q10](#q10) · [Q11](#q11) · [Q13](#q13) · [Q14](#q14) · [Q16](#q16) · [Q20](#q20) as real stories, then the [Cheat Sheet](#cheatsheet).

---

# A. Technical leadership

---

<a id="q1"></a>
## 1. How do you conduct a code review? What do you look for?

> Very common · Medium

**Short answer (say this):**
"I review in layers — correctness and design first, readability next, and I let the linter handle pure style. I look for edge cases, clear naming, good structure, and tests. Just as important is *how* I give feedback: I ask questions instead of giving orders, stay kind and specific, and review promptly so I don't block the team."

**Let's understand it fully:**

**Step 1 — What I look for, in priority order.**
1. **Correctness** — does it work, including edge cases (null, empty, errors)?
2. **Design** — right place, well-structured, not over-engineered.
3. **Readability** — clear names, small functions, no surprises.
4. **Tests** — are the changes covered?
5. **Style** — leave to the formatter/linter, don't nitpick.

**Step 2 — How I give feedback (tone matters most).**
- Ask **questions**: "What happens here if the list is empty?" beats "This is wrong."
- Be **specific and kind** — about the code, never the person.
- **Explain the why** so it's a teaching moment.
- **Approve when good enough**, not perfect; flag minor things as optional.

```dart
// Instead of: "This is wrong."
// I write: "If getAll() throws, _loading stays true forever — wrap in try/finally?"
```

**Step 3 — As a senior, I also use reviews to teach.**
Reviews spread knowledge and standards. I point to *why* a pattern is better, not just *that* it is, so the author learns.

**Why interviewers ask:** Code review is a daily senior responsibility; they assess your judgment and how you treat people.

**Common mistake:** Nitpicking style a linter handles while missing real bugs, or harsh/vague feedback that demotivates.

**Follow-ups they may ask:**
- *"How do you handle a huge PR?"* → Ask to split it; big PRs get shallow reviews.

**Related:** [Q9 — reviewing a senior's PR](#q9) · [Q18 (Git) — PR best practices](../software-engineering/Section_17_Git_Version_Control.md#q18) · [Q5 (SDLC) — code review](../software-engineering/section_19_sdlc_interview_prep.md#q5)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. How do you mentor junior or mid-level developers?

> Common · Medium

**Short answer (say this):**
"I meet them where they are and grow their independence over time. I pair on problems, give context and the 'why' rather than just answers, set small stretch goals, and use code reviews as teaching moments. The goal is to make them self-sufficient, not dependent on me."

**Let's understand it fully:**

**Step 1 — Adjust to the person.**
A junior needs more guidance and confidence; a mid-level needs ownership and stretch. I tailor support to each.

**Step 2 — Teach the 'why', not just the answer.**
Giving the answer solves today's problem; explaining the reasoning builds a developer who solves the next one alone. I guide them to the answer with questions when I can.

**Step 3 — Concrete mentoring actions.**
- **Pair programming** on tricky problems.
- **Code reviews** as gentle, explained learning.
- **Small stretch goals** — slightly beyond their comfort zone, with a safety net.
- **Regular 1:1s** for growth and unblocking, not just tasks.

**Step 4 — Build independence and confidence.**
I let them make (safe) mistakes and learn, praise progress, and gradually hand over more ownership. Success is when they don't need me for that thing anymore.

**Why interviewers ask:** Senior engineers multiply the team; mentoring shows you grow others, not just yourself.

**Common mistake:** Doing the work *for* them (fast but they don't learn), or dumping answers without context.

**Follow-ups they may ask:**
- *"A mentee keeps making the same mistake?"* → Find the root cause (knowledge gap? rushing?), adjust the approach, and be patient.

**Related:** [Q1 — code review](#q1) · [Q8 — onboarding](#q8)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. How do you handle a technical disagreement with a teammate or architect?

> Very common · Medium

**Short answer (say this):**
"I focus on the problem, not winning. I make sure I understand their view, present mine with evidence and trade-offs, and look for the option that's best for the project. If we still disagree, I'll prototype or defer to data, and once the team decides, I commit fully — even if it wasn't my preference."

**Let's understand it fully:**

**Step 1 — Understand before persuading.**
First, restate their position so they know I get it. Often a disagreement is a misunderstanding, or they have context I lack.

**Step 2 — Argue with evidence, not ego.**
Present trade-offs, not opinions: "Option A is simpler but won't scale past X; option B is more work but handles growth." Make it about the project's needs.

**Step 3 — Resolve it constructively.**
- **Prototype/spike** to let data decide ([Q15 SDLC](../software-engineering/section_19_sdlc_interview_prep.md#q15)).
- **Bring in a third perspective** if stuck.
- **Disagree and commit** — once the team decides, I support the decision fully, even if it wasn't mine.

**Step 4 — Keep the relationship healthy.**
The goal is the best outcome *and* a good working relationship. I never make it personal; today's "opponent" is tomorrow's collaborator.

**Why interviewers ask:** Disagreements are constant; they want to see you handle them maturely and stay collaborative.

**Common mistake:** Making it a battle of egos, or refusing to commit after the team decides ("I told you so" energy).

**Follow-ups they may ask:**
- *"What if you're overruled and you think it's wrong?"* → Voice the risk clearly (maybe in writing), then commit and help make it work; revisit with data if problems appear.

**Related:** [Q14 — disagree with manager](#q14) · [Q7 — architecture decisions](#q7)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. How do you introduce a new library or technology to your team?

> Common · Medium

**Short answer (say this):**
"Carefully and with evidence. I start by confirming there's a real problem it solves, then evaluate options (maturity, maintenance, community, fit), run a small spike or proof-of-concept, and share the findings with the team. I get buy-in before adopting, and roll it out gradually rather than rewriting everything at once."

**Let's understand it fully:**

**Step 1 — Start with the problem, not the shiny tool.**
New tech must solve a real pain. "It's trendy" isn't a reason. I name the problem first.

**Step 2 — Evaluate properly.**
- **Maturity & maintenance** — is it actively maintained, widely used, stable?
- **Fit** — does it suit our app and team's skills?
- **Cost** — learning curve, migration effort, lock-in risk.
- **Alternatives** — including "do nothing" or using what we have.

**Step 3 — Prove it with a spike.**
A small proof-of-concept de-risks the decision ([Q15 SDLC](../software-engineering/section_19_sdlc_interview_prep.md#q15)) and gives real evidence instead of opinion.

**Step 4 — Get buy-in and roll out gradually.**
Share findings, discuss as a team, and adopt incrementally (one feature first), not a big-bang rewrite. Document the decision ([Q7](#q7)) and help the team learn it.

**Why interviewers ask:** It tests whether you make balanced, team-aware technology decisions instead of chasing hype.

**Common mistake:** Adopting trendy tech unilaterally without buy-in or a real need, then forcing a risky big-bang migration.

**Follow-ups they may ask:**
- *"A junior wants to add a flashy new state-management library — how do you respond?"* → Welcome the initiative, then evaluate it together against real needs and team consistency.

**Related:** [Q7 — architecture decisions](#q7) · [Q3 — disagreement](#q3)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. How do you manage and pay down technical debt?

> Common · Medium

**Short answer (say this):**
"I make it visible and pay it down steadily rather than ignoring it or demanding a big rewrite. I track debt items in the backlog, tie them to business impact (bugs, slow delivery), budget a slice of each sprint to address the worst, and prevent new debt with reviews and a strong Definition of Done."

**Let's understand it fully:**

**Step 1 — Make it visible.**
Debt kept in people's heads never gets fixed. I log debt items in the backlog with their impact, so they're real, prioritizable work.

**Step 2 — Prioritize by business impact.**
Not all debt is equal. I focus on the debt that causes the most bugs or slows the most-changed areas — and frame it in business terms: "this module causes 40% of our bugs."

**Step 3 — Pay it down steadily.**
- **Budget** ~10–20% of each sprint for debt.
- **Boy scout rule** — improve code near what you're already touching.
- **Avoid big-bang rewrites** — risky and usually rejected; prefer incremental (Strangler Fig for big cases).

**Step 4 — Prevent new debt.**
Code reviews, a strong Definition of Done, tests, and clear standards stop the pile from growing.

**Why interviewers ask:** Balancing debt is a core senior judgment — neither ignoring it nor obsessing over it.

**Common mistake:** Ignoring debt until the codebase is unworkable, or asking to "stop features for a month to refactor" (scares stakeholders, high risk).

**Follow-ups they may ask:**
- *"How do you convince a PO to allocate time?"* → Show the cost in bug rates and slower delivery; propose a small steady budget.

**Related:** [Q6 — speed vs quality](#q6) · [Q17 (Agile) — tech debt](../software-engineering/section_18_agile_scrum_methodology.md#q17) · [Q3 (Refactoring) — convince a team](../software-engineering/section_15_code_smells_refactoring.md#q3)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. How do you balance speed of delivery vs code quality?

> Very common · Medium

**Short answer (say this):**
"I treat it as a deliberate trade-off, not a fixed rule. For a quick experiment or a deadline, I'll take a *conscious* shortcut and log it as debt to fix later. For core, long-lived code, quality wins because it's cheaper over time. The key is to decide consciously and communicate it, never to let quality slip silently."

**Let's understand it fully:**

**Step 1 — It depends on context.**
- **Throwaway/experiment/urgent deadline** → speed can win; take a *tracked* shortcut.
- **Core, long-lived, high-risk code** → quality wins; rushing here costs far more later.

**Step 2 — Make shortcuts conscious and visible.**
If I cut a corner for speed, I say so and log it as tech debt ([Q5](#q5)) with a plan to fix it. The danger isn't shortcuts — it's *silent* ones nobody tracks.

**Step 3 — Quality often IS speed.**
Over any real timeframe, clean, tested code is *faster* — fewer bugs, easier changes. So "quality vs speed" is often a false choice; cutting quality usually slows you down within weeks.

**Step 4 — Communicate the trade-off.**
I make the cost clear to the PO/team: "We can ship Friday with a known limitation, or Monday done properly." Let the business choose with full information.

**Why interviewers ask:** This tension is constant; they want to see mature, conscious judgment, not dogma.

**Common mistake:** Always choosing one extreme — shipping fast garbage every time, or gold-plating everything and missing deadlines.

**Follow-ups they may ask:**
- *"A deadline forces a shortcut — what do you do?"* → Take it consciously, document the debt, and schedule the fix; never hide it.

**Related:** [Q5 — tech debt](#q5) · [Q13 (Clean Code) — clean vs over-engineered](../software-engineering/section_16_clean_code.md#q13)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. How do you make architectural decisions, and how do you document them?

> Common · Medium

**Short answer (say this):**
"I gather the requirements and constraints, list a few realistic options with their trade-offs, and choose based on the project's actual needs — not the trendiest option. I document significant decisions as short ADRs (Architecture Decision Records) capturing the context, the options, the choice, and *why*, so future developers understand the reasoning."

**Let's understand it fully:**

**Step 1 — Decide based on real needs.**
Start from requirements (scale, team size, lifespan, constraints). Match the architecture to *those*, not to a pattern you want to use ([Q14 Architecture](../software-engineering/section_13_software_architecture_patterns.md#q14)).

**Step 2 — Compare options and trade-offs.**
List 2–3 realistic options, each with pros/cons. There's rarely one "right" answer — there's the best fit for this context. Involve the team for buy-in.

**Step 3 — Document with an ADR.**
A short record per significant decision:

```
# ADR: State management choice
Context:  large app, 8 devs, need testability
Options:  Provider, Riverpod, BLoC
Decision: BLoC — team knows it, testable, event-traceable
Why:      consistency + testability outweigh extra boilerplate
```

**Step 4 — Why document the 'why'.**
Six months later, someone asks "why did we do this?" Without an ADR, that knowledge is lost and people second-guess or break decisions. ADRs preserve the reasoning cheaply.

**Why interviewers ask:** It tests structured decision-making and communication — key for senior/lead roles.

**Common mistake:** Deciding alone with no documented reasoning (so it's lost), or picking tech by hype rather than fit.

**Follow-ups they may ask:**
- *"What's an ADR?"* → A short, lightweight doc of a decision, the options, and the reasoning — kept with the code.

**Related:** [Q4 — new technology](#q4) · [Q14 (Architecture) — choosing](../software-engineering/section_13_software_architecture_patterns.md#q14) · [Q14 (SDLC) — documentation](../software-engineering/section_19_sdlc_interview_prep.md#q14)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. How do you onboard a new developer to a large Flutter codebase?

> Common · Medium

**Short answer (say this):**
"I make the first week about small wins and context, not the whole codebase at once. I ensure setup docs work, give them a small real task early, pair them with a buddy, walk them through the architecture and conventions, and point them to the parts that matter for their first feature. The goal is a confident first PR fast."

**Let's understand it fully:**

**Step 1 — Get them productive quickly.**
A clear, working **setup guide** (run the app in under an hour) and a **small starter task** in week one give an early win and confidence.

**Step 2 — Give context, not a firehose.**
Walk them through the **big picture**: the architecture, folder structure, key patterns, and how to run/test. They don't need every detail — they need a map and where to look.

**Step 3 — Pair them with a buddy.**
A go-to person for "dumb questions" removes fear and speeds learning far more than reading docs alone.

**Step 4 — Document the gaps.**
If onboarding revealed missing/confusing docs, fix them — that improves onboarding for the next person (and is a great starter task for the new hire).

**Why interviewers ask:** Good onboarding shows you scale the team and value others' ramp-up, not just your own output.

**Common mistake:** Dropping them into a huge complex feature with no guidance, or making them read everything before touching code (slow, demoralizing).

**Follow-ups they may ask:**
- *"First task for a new senior?"* → Something real but bounded that touches several areas, with a buddy — so they learn the system by doing.

**Related:** [Q2 — mentoring](#q2) · [Q14 (SDLC) — documentation](../software-engineering/section_19_sdlc_interview_prep.md#q14)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. How do you review a PR from a developer more senior than you?

> Common · Medium

**Short answer (say this):**
"The same standards apply to everyone — I review it carefully and honestly. I ask questions to understand their reasoning rather than assuming I'm wrong, raise concerns respectfully with evidence, and I'm also open to learning from their approach. Good seniors *want* real review, not a rubber stamp."

**Let's understand it fully:**

**Step 1 — Don't rubber-stamp out of intimidation.**
Seniors make mistakes too, and they value genuine review. Approving blindly because of their title helps no one and defeats the purpose.

**Step 2 — Ask, don't accuse.**
Frame concerns as questions: "I might be missing context — what happens here if the response is null?" This is respectful and often surfaces either a real issue or useful context for me.

**Step 3 — Bring evidence, stay humble.**
If I spot a problem, I back it with reasoning or a doc/standard. And I stay open — sometimes their approach is right and I learn something. It's a two-way conversation.

**Step 4 — It's about the code, not rank.**
A healthy team reviews everyone's code equally. Doing this well also shows confidence and earns respect.

**Why interviewers ask:** It tests confidence, humility, and that you uphold standards regardless of hierarchy.

**Common mistake:** Auto-approving a senior's PR without real review, or the opposite — being combative to prove a point.

**Follow-ups they may ask:**
- *"They dismiss your comment — what now?"* → Discuss the trade-off calmly; if it's important, bring data or a third opinion; if minor, let it go.

**Related:** [Q1 — code review](#q1) · [Q3 — disagreement](#q3)

[↑ Back to top](#toc)

---

# B. Behavioral (STAR)

> Use the **STAR** method (top of this section). Prepare 3–4 *real* stories from your experience that you can flex to fit many questions. The samples below are templates — replace them with your own projects and numbers.

---

<a id="q10"></a>
## 10. Tell me about yourself (senior-level framing).

> Very common · Easy–Medium

**Short answer (say this):**
"Keep it to ~90 seconds in three parts: a one-line summary of who you are, 2–3 highlights that match the role (with impact), and why you're excited about *this* job. It's a pitch, not your life story — lead with what's most relevant to a senior Flutter role."

**Let's understand it fully:**

**Step 1 — The 3-part structure.**
1. **Present** — "I'm a senior Flutter engineer with ~6 years building production mobile apps."
2. **Highlights** — 2–3 achievements that fit the role, with impact: "I led the rewrite of our e-commerce app to Clean Architecture + BLoC, cutting crash rate by 60% and onboarding time for new devs in half."
3. **Why this role** — "I'm drawn to this role because [specific reason about the company/product]."

**Step 2 — Tailor it to the job.**
Pick highlights that match the job description. Applying for a fintech role? Emphasize security and reliability. A startup? Emphasize ownership and shipping fast.

**Step 3 — Lead with impact, not tasks.**
Not "I wrote Flutter code." Instead "I improved app startup by 40% and mentored 3 juniors to independence." Senior = impact and leadership, not just coding.

**Step 4 — Keep it tight (~90 seconds).**
End with energy about the role, which naturally hands the conversation back.

**Why interviewers ask:** It sets the tone and shows whether you can communicate clearly and position yourself at a senior level.

**Common mistake:** Rambling through your whole history, listing tasks instead of impact, or a generic pitch not tailored to the role.

**Follow-ups they may ask:**
- *"Tell me more about that rewrite."* → Have a STAR story ready ([Q12](#q12)).

**Related:** [Q18 — why this role](#q18) · [Q11 — achievement](#q11)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What is your biggest technical achievement?

> Very common · Medium

**Short answer (say this):**
"Pick one achievement with real impact and tell it in STAR. Lead with the result, then explain the challenge and what *you* specifically did. Choose something that shows senior qualities — solving a hard problem, leading, or delivering measurable business value."

**Let's understand it fully (STAR sample — adapt to your own):**

- **Situation:** "Our Flutter app had a 3-second cold start and a 4% crash rate; users were complaining and reviews were dropping."
- **Task:** "As the senior on the team, I owned fixing performance and stability before a major marketing launch."
- **Action:** "I profiled with DevTools, moved heavy JSON parsing to isolates, added `const` widgets and `ListView.builder` for long lists, fixed several uncancelled stream subscriptions causing leaks, and set up Crashlytics with alerting. I also paired with two juniors so they could maintain it."
- **Result:** "Cold start dropped from 3s to 1.1s, crash-free users went from 96% to 99.6%, and the app rating rose from 3.8 to 4.5 over two months."

**Tips:**
- **Lead with the result** if you want impact up front, then fill in S-T-A.
- Use **"I"** for your actions (the interviewer is hiring *you*).
- Have **numbers** — they make it real and senior.

**Why interviewers ask:** It reveals what you consider impactful and whether you can deliver and communicate it.

**Common mistake:** A vague story with no measurable result, or saying "we" so much it's unclear what *you* did.

**Follow-ups they may ask:**
- *"What was the hardest part?"* → Have a specific technical challenge and how you solved it ready.

**Related:** [Q15 — improved performance](#q15) · [Q12 — led a project](#q12)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. Describe a time you led a project from scratch to production.

> Common · Medium

**Short answer (say this):**
"Use STAR and emphasize *leadership* and *delivery*: how you scoped it, made key decisions, coordinated people, handled problems, and shipped it with results. This is your chance to show ownership end-to-end, not just coding."

**Let's understand it fully (STAR sample — adapt):**

- **Situation:** "The company needed a new patient-booking feature in our telemedicine Flutter app, with no existing foundation."
- **Task:** "I led it end-to-end — architecture, a team of 3, and delivery in 10 weeks."
- **Action:** "I gathered requirements with the PO, chose Clean Architecture + BLoC and documented it in an ADR, broke the work into sprints, ran planning and reviews, paired on the hard parts, and handled a mid-project API change by isolating it behind a repository so the UI didn't churn."
- **Result:** "We shipped on time; booking completion rose 25%, and the modular structure let us reuse 60% of it for a later feature."

**Tips:**
- Show **decisions and trade-offs** you made (that's leadership).
- Mention how you **handled a problem** (scope change, a blocker) — projects never go perfectly.
- End with **business impact**, not just "it shipped."

**Why interviewers ask:** It tests end-to-end ownership and leadership under real constraints.

**Common mistake:** Describing only the coding and skipping the leadership (planning, decisions, coordinating, handling problems).

**Follow-ups they may ask:**
- *"What would you do differently?"* → Show reflection — one honest improvement.

**Related:** [Q11 — achievement](#q11) · [Q7 — architecture decisions](#q7)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. Tell me about a time you fixed a critical production bug.

> Very common · Medium

**Short answer (say this):**
"Use STAR and show a calm, methodical process under pressure: contain the impact first, find the root cause, fix it with a test so it can't return, deploy safely, and run a blameless post-mortem. Interviewers want composure and process, not heroics."

**Let's understand it fully (STAR sample — adapt):**

- **Situation:** "After a release, our app started crashing on login for ~30% of Android users — a P0 incident."
- **Task:** "I led the response and needed to restore service fast."
- **Action:** "First I contained it — we rolled back the release within 20 minutes so users could log in. Then I reproduced it from Crashlytics, found a null token from a changed API response that we weren't handling, wrote a fix plus a test that reproduced the crash, and deployed via a hotfix. Afterward I ran a blameless post-mortem and we added a contract test against the API."
- **Result:** "Downtime was limited to ~25 minutes, no data loss, and the contract test has caught two similar issues since."

**Tips:**
- Stress **'contain first, root-cause second'** ([Q9 SDLC](../software-engineering/section_19_sdlc_interview_prep.md#q9)).
- Mention the **test** that prevents recurrence.
- **Blameless** tone — focus on the system, not blaming a person.

**Why interviewers ask:** It tests how you act under pressure and whether you fix causes, not just symptoms.

**Common mistake:** Telling a chaotic "I panicked and hacked a fix" story, or fixing the symptom with no prevention.

**Follow-ups they may ask:**
- *"How did you prevent it recurring?"* → The test + a process/monitoring improvement.

**Related:** [Q9 (SDLC) — production bug](../software-engineering/section_19_sdlc_interview_prep.md#q9) · [Q19 (Git) — hotfix](../software-engineering/Section_17_Git_Version_Control.md#q19)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. Describe a time you disagreed with your manager.

> Very common · Medium

**Short answer (say this):**
"Use STAR and show respectful pushback plus commitment. I voiced my concern with evidence, listened to their view, and we found a path forward. The key signals: I raised it professionally, I backed it with facts, and once a decision was made I committed fully — no sulking."

**Let's understand it fully (STAR sample — adapt):**

- **Situation:** "My manager wanted to ship a feature without automated tests to hit a deadline."
- **Task:** "I felt the risk was too high for a core payments flow and needed to raise it constructively."
- **Action:** "I explained the specific risk — a bug in payments could cost real money and trust — and proposed a middle path: ship on time but with tests on the critical payment paths only, deferring lower-risk tests. I showed it would add just one day."
- **Result:** "We agreed on the middle path. The payment tests caught a rounding bug before release. My manager later thanked me for pushing back."

**Tips:**
- Pick a **professional** disagreement (about approach/quality), not a personal clash.
- Show you **listened** and offered a **constructive option**, not just "no".
- If you were overruled, show you **committed** anyway and it worked out (or you learned).

**Why interviewers ask:** It tests whether you can push back respectfully *and* be a team player — both matter.

**Common mistake:** A story where you were combative, or where you just gave in with no spine — they want balanced backbone.

**Follow-ups they may ask:**
- *"What if they'd said no?"* → I'd voice the risk clearly (in writing if serious), then commit and monitor for the problem.

**Related:** [Q3 — technical disagreement](#q3) · [Q6 — speed vs quality](#q6)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. Tell me about a time you improved the performance of an app.

> Common · Medium

**Short answer (say this):**
"Use STAR and show a *measured* approach: I identified the problem with profiling, found the real cause, applied targeted fixes, and measured the improvement. The signal is that I optimize with data, not guesses, and I know Flutter's performance tools."

**Let's understand it fully (STAR sample — adapt):**

- **Situation:** "A product list screen janked badly when scrolling — users noticed lag."
- **Task:** "I owned making it smooth (a steady 60fps)."
- **Action:** "I profiled with DevTools and the performance overlay, found the whole list rebuilt on every scroll and images weren't cached. I switched to `ListView.builder`, added `const` and `RepaintBoundary`, cached images with `cached_network_image`, and moved a heavy filter computation off the UI thread with an isolate. I measured before/after in *release* mode."
- **Result:** "Scrolling went from ~35fps with visible jank to a smooth 60fps, and the frame build time dropped from 28ms to under 8ms."

**Tips:**
- Stress **measure first** (profile), then fix, then **measure again** — in **release** mode.
- Name the specific Flutter tools/fixes ([Q5 Performance](../flutter/section5_performance_optimization.md#q1)).

**Why interviewers ask:** It tests a data-driven approach and real Flutter performance knowledge.

**Common mistake:** Optimizing by guessing without profiling, or quoting debug-mode numbers (always measure in release).

**Follow-ups they may ask:**
- *"How did you find the bottleneck?"* → DevTools timeline, the performance overlay, "Track Widget Rebuilds".

**Related:** [Q5 (Performance)](../flutter/section5_performance_optimization.md#q1) · [Q11 — achievement](#q11)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. Describe a time a project failed. What did you learn?

> Very common · Medium–Hard

**Short answer (say this):**
"Use STAR and pick a *real* failure where you take honest ownership and show clear learning. Don't blame others or pick a fake 'failure'. The signal they want: you can fail, own it, learn, and apply the lesson — that's how seniors grow."

**Let's understand it fully (STAR sample — adapt):**

- **Situation:** "We rushed a feature to launch without enough user validation."
- **Task:** "I was the lead and pushed to ship fast."
- **Action:** "We built it in three weeks and launched — but adoption was near zero. I dug in: we'd assumed what users wanted instead of validating. I ran user interviews, found the real need was different, and we reworked it."
- **Result:** "The reworked version got strong adoption. The lesson: I now insist on validating assumptions with users *before* building, which has saved us from two more wasted builds since."

**Tips:**
- Take **genuine ownership** ("I", not "the team failed me").
- Show a **concrete lesson** and that you **applied it** afterward.
- Pick a **real but recoverable** failure — not a catastrophe, not a fake one.

**Why interviewers ask:** It tests humility, self-awareness, and growth — they're wary of people who "never fail."

**Common mistake:** Blaming others, picking a non-failure ("I work too hard"), or showing no real learning.

**Follow-ups they may ask:**
- *"How did you apply the lesson?"* → A specific later example where you did it better.

**Related:** [Q20 — weakness](#q20) · [Q14 — disagree with manager](#q14)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. How do you stay up to date with Flutter and the Dart ecosystem?

> Common · Easy

**Short answer (say this):**
"A mix of sources and hands-on practice. I follow the official Flutter/Dart channels and release notes, read the community (newsletters, key blogs, conference talks), and most importantly I *try* new things in side projects. I also learn from my team and code reviews."

**Let's understand it fully:**

**Step 1 — Official sources.**
Flutter/Dart release notes and the official blog/YouTube — so I know about new language features (records, patterns), framework changes (Impeller), and deprecations.

**Step 2 — Community.**
A newsletter or two (e.g. Flutter Weekly), respected blogs, conference talks (Flutter Forward/Engage), and following maintainers. This surfaces patterns and pitfalls.

**Step 3 — Hands-on (the most important).**
Reading isn't enough — I try new features in small side projects or spikes so I actually understand them, not just recognize the names.

**Step 4 — Learn from the team.**
Code reviews, pairing, and team discussions spread knowledge both ways. Teaching something is also how I solidify it.

**Why interviewers ask:** Mobile moves fast; they want someone who keeps current without chasing every shiny thing.

**Common mistake:** A generic "I read blogs" with no specifics, or claiming you know the latest without having tried it.

**Follow-ups they may ask:**
- *"What's a recent Flutter/Dart change you like?"* → Have a specific, current example ready (e.g. Dart 3 records/patterns, Impeller).

**Related:** [Q4 — introducing new tech](#q4) · [Q19 — 3–5 years](#q19)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. Why do you want this Senior Flutter role?

> Common · Easy–Medium

**Short answer (say this):**
"Connect *their* specifics to *your* goals. Show you researched the company/product, name what genuinely excites you about it, and tie it to where you want to grow. Avoid generic answers that could apply to any company — be specific."

**Let's understand it fully:**

**Step 1 — Do your homework.**
Know their product, tech, and challenges. Reference something specific: "Your app serves [users] and I'm excited by [a real challenge/feature you saw]."

**Step 2 — Connect to your strengths and goals.**
Show mutual fit: what you bring (senior Flutter, leadership, the relevant domain) *and* what you want to grow into (more ownership, scale, mentoring).

**Step 3 — Show genuine interest.**
Maybe the product's mission, the tech challenges, the team's reputation, or remote culture. Authentic enthusiasm stands out.

**Step 4 — Keep it about them, not just you.**
Balance "what I get" with "what I'll contribute." Senior candidates show they'll add value, not just take a paycheck.

**Why interviewers ask:** It tests whether you're genuinely interested in *them* or just need any job — and whether you'll stay.

**Common mistake:** A generic answer ("good company, good tech") that fits anywhere, or focusing only on salary/perks.

**Follow-ups they may ask:**
- *"What do you know about our product?"* → Have specifics ready — it proves real interest.

**Related:** [Q10 — about yourself](#q10) · [Q19 — 3–5 years](#q19)

[↑ Back to top](#toc)

---

<a id="q19"></a>
## 19. Where do you see yourself in 3–5 years?

> Common · Easy

**Short answer (say this):**
"Show ambition that fits a realistic growth path and aligns with the role — deepening into senior/staff or tech lead, taking on bigger systems and more mentoring. Keep it honest and connected to growing *with* a company like theirs, not 'I'll start my own company in a year'."

**Let's understand it fully:**

**Step 1 — Show a realistic growth direction.**
Common honest paths: deeper technical mastery (staff/principal), or technical leadership (tech lead/architect). Pick the one that's true for you.

**Step 2 — Tie it to the role.**
"I want to grow into a tech-lead role, owning architecture and mentoring — which is why a senior role with scope like this appeals to me." Show you'd grow *with* them.

**Step 3 — Be honest but employer-friendly.**
Don't say "I'll be gone in a year" or "I want your interviewer's job." Show ambition that the company can support and benefit from.

**Step 4 — Emphasize impact and learning.**
Frame growth around bigger impact and skills, not just titles: "leading larger projects, mentoring more, and tackling harder system-design problems."

**Why interviewers ask:** It tests ambition, self-awareness, and whether your goals fit what they can offer (retention).

**Common mistake:** No direction ("I don't know"), unrealistic jumps, or signaling you'll leave soon.

**Follow-ups they may ask:**
- *"Management or technical track?"* → Be honest; both are fine, just show you've thought about it.

**Related:** [Q18 — why this role](#q18) · [Q17 — staying current](#q17)

[↑ Back to top](#toc)

---

<a id="q20"></a>
## 20. What is your greatest technical weakness?

> Very common · Medium

**Short answer (say this):**
"Name a *real* weakness, then show what you're actively doing about it. The trick isn't to disguise a strength ('I'm a perfectionist') — interviewers see through that. Pick something genuine but not central to the role, and show concrete improvement."

**Let's understand it fully:**

**Step 1 — Pick a real, honest weakness.**
Something true but not a deal-breaker for the role. Example: "Earlier in my career I under-invested in writing tests" or "I tended to dive into code before fully clarifying requirements."

**Step 2 — Show self-awareness and action.**
The real signal is *growth*: "I noticed it caused rework, so now I always write down acceptance criteria and confirm with the PO before coding — it's saved me from building the wrong thing twice."

**Step 3 — Don't fake it.**
"I'm a perfectionist / I work too hard" is a cliché that signals you're dodging the question. Genuine honesty (plus improvement) builds more trust.

**Step 4 — Keep it role-appropriate.**
Don't name a weakness that's core to the job (e.g. "I'm bad at Flutter" for a Flutter role). Pick something adjacent and improvable.

**Why interviewers ask:** It tests self-awareness and honesty — and whether you actively work on growth.

**Common mistake:** A fake "humblebrag" weakness, or a real weakness with no evidence you're improving it.

**Follow-ups they may ask:**
- *"How are you improving it?"* → Have a specific, concrete action and a result.

**Related:** [Q16 — a failure](#q16) · [Q2 — mentoring (growth mindset)](#q2)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. STAR template, tables, then reminders.

## The STAR template (fill in your own stories)

```
Situation:  (1–2 sentences of context)
Task:       (your specific goal)
Action:     (what I did — the longest part, use "I")
Result:     (the outcome WITH numbers)
```

## Stories to prepare (3–4 flexible ones)

| Story | Covers questions |
|---|---|
| A project you led | [Q11](#q11), [Q12](#q12) |
| A production bug you fixed | [Q13](#q13) |
| A disagreement handled well | [Q3](#q3), [Q14](#q14) |
| A failure + lesson | [Q16](#q16), [Q20](#q20) |
| A performance win | [Q11](#q11), [Q15](#q15) |

## Leadership in one line each

| Topic | Senior answer |
|---|---|
| Code review | correctness first; ask questions, be kind |
| Disagreement | evidence not ego; disagree and commit |
| New tech | real problem + spike + buy-in, not hype |
| Tech debt | make it visible, budget per sprint |
| Speed vs quality | conscious, tracked trade-off |
| Architecture | fit to needs; document with ADRs |

## One-line reminders

- **STAR** every behavioral answer; **end with numbers**. (top of section)
- Use **"I"**, not "we" — they're hiring *you*. ([Q11](#q11))
- **Disagree and commit** — push back with evidence, then support the decision. ([Q3](#q3), [Q14](#q14))
- **Production bug**: contain first, root-cause second, prevent with a test. ([Q13](#q13))
- **Failure**: own it honestly, show the lesson and that you applied it. ([Q16](#q16))
- **Weakness**: a real one + concrete improvement; never a fake humblebrag. ([Q20](#q20))
- **Why this role / 3–5 years**: be specific to *them*, show realistic growth. ([Q18](#q18), [Q19](#q19))
- **Mentoring/onboarding**: teach the *why*, build independence, small wins first. ([Q2](#q2), [Q8](#q8))
- **Speed vs quality**: decide consciously, log the debt, communicate. ([Q6](#q6))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Behavioral interviews drill for specifics. Practice out loud:

1. *"Tell me about a hard bug."* → STAR; contain first, root-cause, test to prevent, blameless post-mortem.
2. *"What was YOUR part?"* (after a 'we' answer) → switch to "I" and name your specific actions.
3. *"What was the result?"* → always have numbers (crash rate, fps, adoption, time saved).
4. *"What would you do differently?"* → show reflection — one honest improvement.
5. *"Why should we hire you over others?"* → tie your specific strengths to their specific needs.

Clear stories, honest ownership, and numbers — delivered calmly — are exactly the senior signal interviewers want, in both remote and BD interviews.

[↑ Back to top](#toc)

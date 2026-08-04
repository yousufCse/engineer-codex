# Section 19 — SDLC & Software Engineering Process

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

> **Interview tip:** For process questions, connect each phase to *quality and risk* — "we catch problems early because that's cheaper." That framing shows senior thinking.

---

<a id="toc"></a>

## Table of Contents

**A. Overview & requirements**
1. [What is SDLC? (the phases)](#q1) · *Very common*
2. [Requirement gathering (functional vs non-functional)](#q2) · *Very common*
3. [System design — HLD vs LLD](#q3) · *Common*

**B. Build & verify**
4. [Good development practices](#q4) · *Common*
5. [Code review](#q5) · *Very common*
6. [Testing phases (unit/integration/system/UAT)](#q6) · *Very common*

**C. Ship & maintain**
7. [Deployment (staging vs production, checklist)](#q7) · *Common*
8. [Maintenance (bug tracking, hotfixes, versioning)](#q8) · *Common*
9. [Handling a production bug (step by step)](#q9) · *Very common*

**D. Quality, risk & docs**
10. [Quality throughout the SDLC](#q10) · *Common*
11. [Shift-Left testing](#q11) · *Common*
12. [DevOps culture](#q12) · *Common*
13. [Risk management](#q13) · *Common*
14. [Documentation (what & what not)](#q14) · *Common*

**E. Concepts**
15. [What is a spike?](#q15) · *Deeper*
16. [Bug vs defect vs feature request](#q16) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

**Stage 1 — The lifecycle (start here).**
→ [Q1 SDLC phases](#q1) · [Q2 Requirements](#q2) · [Q3 HLD vs LLD](#q3)

**Stage 2 — Building well.**
→ [Q4 Dev practices](#q4) · [Q5 Code review](#q5) · [Q6 Testing phases](#q6)

**Stage 3 — Shipping & support.**
→ [Q7 Deployment](#q7) · [Q8 Maintenance](#q8) · [Q9 Production bug](#q9)

**Stage 4 — Quality & risk.**
→ [Q10 Quality throughout](#q10) · [Q11 Shift-left](#q11) · [Q12 DevOps](#q12) · [Q13 Risk](#q13)

**Stage 5 — The rest.**
→ [Q14 Documentation](#q14) · [Q15 Spike](#q15) · [Q16 Bug vs defect](#q16)

**Short on time?** Review [Q1](#q1) · [Q2](#q2) · [Q5](#q5) · [Q6](#q6) · [Q9](#q9), then the [Cheat Sheet](#cheatsheet).

---

# A. Overview & requirements

---

<a id="q1"></a>
## 1. What is SDLC, and what are its phases?

> Very common · Easy–Medium

**Short answer (say this):**
"SDLC, the Software Development Lifecycle, is the structured process for building software — from planning to retirement. The classic phases are: requirements, design, development, testing, deployment, and maintenance. It gives teams a repeatable way to deliver quality software predictably, and different models (Waterfall, Agile) arrange these phases differently."

**Let's understand it fully:**

**Step 1 — A real-life picture: building a house.**
You don't start laying bricks randomly. You gather requirements (what the owner wants), design a blueprint, build, inspect, move in, then maintain. Software follows the same logical flow.

**Step 2 — The phases.**

```
Requirements → Design → Development → Testing → Deployment → Maintenance
   (what)       (how)     (build)      (verify)   (release)    (support)
```

- **Requirements** — figure out what to build ([Q2](#q2)).
- **Design** — plan the architecture ([Q3](#q3)).
- **Development** — write the code ([Q4](#q4)).
- **Testing** — verify it works ([Q6](#q6)).
- **Deployment** — release it ([Q7](#q7)).
- **Maintenance** — fix and improve over time ([Q8](#q8)).

**Step 3 — Models arrange phases differently.**
- **Waterfall** — phases run once, in strict sequence.
- **Agile** — phases repeat in short cycles, with feedback each loop ([Q2 Agile](section_18_agile_scrum_methodology.md#q2)).
- Others: V-model, Spiral, Iterative.

**Step 4 — The point of having a process.**
A defined lifecycle catches problems early (cheaper), makes delivery predictable, and ensures quality isn't an afterthought.

**Why interviewers ask:** It's the foundation; they confirm you see software as a managed process, not just coding.

**Common mistake:** Listing phases mechanically without connecting them — e.g. not knowing that catching a requirements mistake early is far cheaper than after release.

**Follow-ups they may ask:**
- *"Which model do you prefer?"* → Usually Agile for products (feedback-driven); Waterfall for fixed-scope/regulated work.

**Related:** [Q2 — requirements](#q2) · [Q2 (Agile) — Waterfall vs Agile](section_18_agile_scrum_methodology.md#q2)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What is requirement gathering? Functional vs non-functional requirements?

> Very common · Medium

**Short answer (say this):**
"Requirement gathering is finding out what the software must do, before building it. Functional requirements describe *what* the system does — features and behaviour, like 'users can reset their password'. Non-functional requirements describe *how well* it does it — performance, security, scalability, usability. You gather them through interviews, user stories, and prototypes."

**Let's understand it fully:**

**Step 1 — Functional — what the system does.**
Features and behaviours: "users can log in," "the app sends a receipt email," "admins can delete posts."

**Step 2 — Non-functional — how well it does it.**
Quality attributes that cut across features:
- **Performance** — the screen loads in under 2 seconds.
- **Security** — passwords are encrypted; data is protected.
- **Scalability** — handles 10,000 concurrent users.
- **Usability, reliability, accessibility.**

```
Functional:     "the app shows the order history"   (a feature)
Non-functional: "...and loads within 1 second"       (how well)
```

**Step 3 — How you elicit them.**
- **Interviews/workshops** with stakeholders.
- **User stories** and acceptance criteria ([Q11 Agile](section_18_agile_scrum_methodology.md#q11)).
- **Prototypes/mockups** to make vague ideas concrete.
- **Observing real users** to find unspoken needs.

**Step 4 — Why this phase is critical.**
A mistake here is the most expensive kind — building the wrong thing wastes the whole project. Clarifying early (and confirming with stakeholders) prevents costly rework.

**Why interviewers ask:** Misunderstood requirements are a top project-failure cause; they check you take this seriously.

**Common mistake:** Ignoring non-functional requirements (performance, security) until the end, when they're hard and expensive to retrofit.

**Follow-ups they may ask:**
- *"How do you handle vague requirements?"* → Ask questions, build a prototype, and confirm with the stakeholder before building fully.

**Related:** [Q1 — SDLC](#q1) · [Q3 — system design](#q3) · [Q11 (Agile) — user stories](section_18_agile_scrum_methodology.md#q11)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. What is system design, and what is the difference between HLD and LLD?

> Common · Medium

**Short answer (say this):**
"System design is planning how the software will be built before coding. High-Level Design (HLD) is the big-picture architecture — the major components, how they connect, and the tech choices. Low-Level Design (LLD) is the detailed design of each component — the classes, methods, and data structures. HLD is the city map; LLD is the street-by-street plan."

**Let's understand it fully:**

**Step 1 — A real-life picture: two zoom levels of a map.**
HLD is the city map — you see districts and main roads. LLD is the street map of one district — exact streets and house numbers.

**Step 2 — High-Level Design (HLD).**
- The major pieces: app, backend, database, third-party services.
- How they communicate (REST, GraphQL, message queues).
- Big technology choices and trade-offs.
- The architecture pattern (layered, Clean Architecture).

**Step 3 — Low-Level Design (LLD).**
- The classes and their relationships inside a component.
- Method signatures, key algorithms, and data structures.
- Detailed enough that a developer can implement it.

```
HLD: "App ↔ API Gateway ↔ Auth Service + Order Service ↔ Database"
LLD: "OrderService has placeOrder(Order); Order has id, items, total..."
```

**Step 4 — Why both matter.**
HLD aligns the team and stakeholders on the shape and the big trade-offs. LLD ensures each piece is implementable and consistent before coding starts.

**Why interviewers ask:** It tests whether you plan before coding and can think at both the architecture and the detailed level.

**Common mistake:** Jumping straight to code with no HLD, leading to a tangled architecture that's hard to change later.

**Follow-ups they may ask:**
- *"How detailed should design be?"* → Enough to align and de-risk — not so much that it's a frozen, over-specified document (that's wasteful in Agile).

**Related:** [Q2 — requirements](#q2) · [Q21 — system design for mobile](section_21_system_design_for_mobile.md#q1) · [Q2 (Architecture) — Clean Architecture](section_13_software_architecture_patterns.md#q2)

[↑ Back to top](#toc)

---

# B. Build & verify

---

<a id="q4"></a>
## 4. What does good development practice look like?

> Common · Medium

**Short answer (say this):**
"Good development means writing clean, tested code in small, reviewed increments. In practice: work in small branches, follow coding standards and linters, write tests, commit with clear messages, get code reviewed, and integrate often via CI. The goal is code that's correct, readable, and safe to change."

**Let's understand it fully:**

**Step 1 — Small, frequent, reviewed increments.**
- Work in **short-lived branches** and merge via reviewed PRs ([Q5](#q5)).
- **Integrate often** (CI runs tests on every push) so problems surface early.
- Keep changes **small** — easier to review and less risky.

**Step 2 — Quality built in, not bolted on.**
- Follow **coding standards** and run **linters/formatters** automatically ([Q14 Clean Code](section_16_clean_code.md#q14)).
- **Write tests** alongside the code ([Q6](#q6)).
- A clear **Definition of Done** so "done" means done, not "works on my machine."

**Step 3 — Clear history and communication.**
- **Meaningful commits** (conventional commits) and PR descriptions ([Q16 Git](Section_17_Git_Version_Control.md#q16)).
- Update tickets/docs so the team has visibility.

**Step 4 — Why this matters.**
These habits catch bugs early (cheap), keep the codebase healthy, and let many people work together without chaos. Skipping them creates debt that slows the whole team later.

**Why interviewers ask:** It tests your day-to-day engineering discipline, not just whether you can code.

**Common mistake:** Big-bang merges (huge branches, rare integration) that cause painful conflicts and hide bugs until late.

**Follow-ups they may ask:**
- *"What is CI?"* → Continuous Integration: automatically build and test every change so integration problems appear immediately.

**Related:** [Q5 — code review](#q5) · [Q6 — testing](#q6) · [Q4 (Clean Code) — clean functions](section_16_clean_code.md#q3)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What is the purpose of code review? What do you look for?

> Very common · Medium

**Short answer (say this):**
"Code review is a second pair of eyes before code merges. Its purpose is to catch bugs, improve design and readability, share knowledge across the team, and keep a consistent standard. I look for correctness, edge cases, clear naming, good design, and tests — and I let the linter handle pure style."

**Let's understand it fully:**

**Step 1 — Why review at all.**
- **Catch bugs** before they reach users.
- **Improve design** — a reviewer spots better approaches.
- **Share knowledge** — more people understand the code.
- **Consistency** — the codebase stays uniform.

**Step 2 — What to look for (in priority order).**
1. **Correctness** — does it work, including edge cases (empty, null, errors)?
2. **Design** — is it in the right place, well-structured, not over-engineered?
3. **Readability** — clear names, small functions, no surprises.
4. **Tests** — are the changes covered?
5. **Style** — leave to the formatter/linter, don't nitpick.

**Step 3 — How to give good feedback.**
- Ask **questions**, don't issue commands: "What happens if the list is empty?"
- Be **kind and specific**; focus on the code, not the person.
- Be **timely** — a blocked teammate is costly.
- **Approve when good enough**, not perfect.

**Step 4 — As the author.**
Keep PRs small, write a clear description, self-review first, and make tests pass before requesting review ([Q18 Git](Section_17_Git_Version_Control.md#q18)).

**Why interviewers ask:** Reviews are a daily senior responsibility; they assess your judgment and collaboration.

**Common mistake:** Nitpicking formatting (a tool's job) while missing real correctness/design issues, or giving harsh, vague feedback ("this is wrong").

**Follow-ups they may ask:**
- *"How do you handle disagreement in review?"* → Discuss the trade-offs, defer to data/standards, and escalate to the team if needed — keep it about the code.

**Related:** [Q18 (Git) — PR best practices](Section_17_Git_Version_Control.md#q18) · [Q4 — dev practices](#q4) · [Q22 (Leadership) — code review](../leadership/Section_22_Senior_Leadership_Behavioral.md#q1)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What are the testing phases? Explain unit, integration, system, and UAT.

> Very common · Medium

**Short answer (say this):**
"Testing happens at levels, from small to big. Unit tests check one piece in isolation. Integration tests check that pieces work together. System testing checks the whole app end-to-end. UAT (User Acceptance Testing) is real users or the client confirming it meets their needs. Each level catches different kinds of bugs."

**Let's understand it fully:**

**Step 1 — A real-life picture: building a house.**
- **Unit** — test one brick.
- **Integration** — test a wall (bricks together).
- **System** — walk through the whole house.
- **UAT** — the owner inspects and signs off.

**Step 2 — The four levels.**

| Level | Tests | Example |
|---|---|---|
| Unit | one function/class alone | a `calculateTotal()` function |
| Integration | pieces working together | the repository + API layer |
| System | the whole app end-to-end | full checkout flow on a device |
| UAT | client/user acceptance | the customer confirms it fits their needs |

**Step 3 — Where most tests should be (the pyramid).**
Most tests should be fast **unit** tests, fewer **integration**, and even fewer slow **end-to-end** tests. This "test pyramid" keeps the suite fast and reliable ([Q6 Flutter Testing](../flutter/section6_testing_in_flutter.md#q1)).

**Step 4 — Who does what.**
Developers write unit/integration tests; QA often drives system testing; the **client or end users** do UAT. UAT is about *fit for purpose*, not just "no bugs."

**Why interviewers ask:** It tests whether you understand testing as layered, not just "we test at the end."

**Common mistake:** Relying only on manual end-to-end testing (slow, flaky) with few unit tests — the inverted pyramid.

**Follow-ups they may ask:**
- *"Regression testing?"* → Re-running tests after a change to confirm you didn't break existing behaviour — automated tests make this cheap.

**Related:** [Q6 (Flutter) — testing in Flutter](../flutter/section6_testing_in_flutter.md#q1) · [Q11 — shift-left](#q11)

[↑ Back to top](#toc)

---

# C. Ship & maintain

---

<a id="q7"></a>
## 7. What is the deployment process? Staging vs production, and what's on a deployment checklist?

> Common · Medium

**Short answer (say this):**
"Deployment is releasing the software to an environment. Staging is a near-identical copy of production used for a final test (a dress rehearsal); production is the live environment real users hit. A deployment checklist ensures a safe release: tests pass, a backup/rollback plan exists, config and secrets are correct, and monitoring is ready."

**Let's understand it fully:**

**Step 1 — The environments.**

```
Local (your machine) → Dev → Staging (like production) → Production (real users)
```

- **Staging** — mirrors production as closely as possible; final testing happens here.
- **Production** — the real, live system. Mistakes here affect users.

**Step 2 — Why a staging environment.**
It catches problems that only appear in a production-like setup (real config, data volumes, integrations) — a dress rehearsal before opening night.

**Step 3 — A deployment checklist.**
- All tests and CI checks pass.
- Database migrations prepared (and reversible).
- Config and secrets correct for the target environment.
- A **rollback plan** if something breaks.
- Monitoring/alerts ready to catch issues.
- Stakeholders informed; deploy during low-traffic if risky.

**Step 4 — Safer release strategies.**
- **Blue-green** — run two production environments, switch traffic instantly (easy rollback).
- **Canary** — release to a small percentage first, watch, then roll out fully.
- **Feature flags** — ship code dark, turn it on gradually.

**Why interviewers ask:** It tests whether you release safely, with rollback and monitoring — not "push to prod and hope."

**Common mistake:** Deploying with no rollback plan or monitoring, so a bad release becomes a long outage.

**Follow-ups they may ask:**
- *"How do you roll back quickly?"* → Blue-green switch, redeploy the previous build, or toggle a feature flag off.

**Related:** [Q10 (CI/CD) — release](../flutter/Section_10_CICD_Flavors_App_Release.md#q1) · [Q9 — production bug](#q9)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What does maintenance look like? How do you handle bug tracking, hotfixes, and versioning?

> Common · Medium

**Short answer (say this):**
"Maintenance is everything after release — fixing bugs, improving performance, and adding small changes. Bugs are tracked in a tool (Jira/GitHub Issues) with priority. Hotfixes are urgent fixes branched off production and shipped fast. Versioning (semantic versioning: major.minor.patch) communicates the size of each release."

**Let's understand it fully:**

**Step 1 — Maintenance is most of a product's life.**
A product spends far longer being maintained than being first built. Good maintenance means tracking issues, fixing them by priority, and keeping the app healthy.

**Step 2 — Bug tracking.**
- Log every bug with steps to reproduce, severity, and priority.
- Triage regularly — fix critical bugs fast, schedule the rest.

**Step 3 — Hotfixes.**
For urgent production problems, branch directly off production, fix narrowly, test, deploy, then merge back to main ([Q19 Git](Section_17_Git_Version_Control.md#q19)).

**Step 4 — Semantic versioning (semver).**

```
MAJOR.MINOR.PATCH   e.g. 2.4.1

PATCH (2.4.1 → 2.4.2)  bug fix, backward compatible
MINOR (2.4.1 → 2.5.0)  new feature, backward compatible
MAJOR (2.4.1 → 3.0.0)  breaking change
```

This tells users at a glance how risky an upgrade is.

**Why interviewers ask:** It tests that you think beyond launch — most engineering effort is maintenance.

**Common mistake:** Treating versioning casually (random numbers), so users can't tell a breaking change from a patch.

**Follow-ups they may ask:**
- *"What is regression?"* → A bug that reappears or a new change breaking old behaviour — automated tests catch these.

**Related:** [Q9 — production bug](#q9) · [Q19 (Git) — hotfix](Section_17_Git_Version_Control.md#q19) · [Q16 (Git) — conventional commits/versioning](Section_17_Git_Version_Control.md#q16)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. How do you handle a production bug? Walk through the process.

> Very common · Medium

**Short answer (say this):**
"I follow a clear order: first contain the damage (mitigate so users aren't hurt), then reproduce and diagnose, then fix and test, then deploy the fix safely, and finally do a blameless post-mortem to prevent it recurring. The instinct is 'stop the bleeding first, find the root cause second'."

**Let's understand it fully:**

**Step 1 — Contain first (stop the bleeding).**
Reduce user impact immediately: roll back the bad release, toggle a feature flag off, or disable the broken feature. Don't spend an hour debugging while users suffer — mitigate first.

**Step 2 — Reproduce and diagnose.**
- Reproduce the bug reliably (from reports, logs, crash reports like Crashlytics/Sentry).
- Find the **root cause**, not just the symptom.

**Step 3 — Fix, test, and deploy safely.**
- Write a focused fix and a **test** that would have caught it (so it never returns).
- Deploy via a hotfix process with a rollback plan ([Q19 Git](Section_17_Git_Version_Control.md#q19)).

**Step 4 — Post-mortem (blameless).**
After it's resolved, the team reviews: what happened, why, and how to prevent it (better tests, monitoring, alerts). **Blameless** means focusing on the system and process, not punishing a person — that keeps people honest.

**Step 5 — Communicate throughout.**
Keep stakeholders/users informed during a serious incident — silence is worse than bad news.

**Why interviewers ask:** Incident handling is a key senior skill; they want to see "contain first, root-cause second, prevent always."

**Common mistake:** Jumping straight to debugging while users are impacted (should mitigate first), or fixing the symptom without a test to prevent recurrence.

**Follow-ups they may ask:**
- *"Why blameless post-mortems?"* → Fear hides information; blameless reviews surface the real causes so the system improves.

**Related:** [Q7 — deployment & rollback](#q7) · [Q19 (Git) — hotfix](Section_17_Git_Version_Control.md#q19)

[↑ Back to top](#toc)

---

# D. Quality, risk & docs

---

<a id="q10"></a>
## 10. How do you ensure quality throughout the SDLC, not just at testing?

> Common · Medium

**Short answer (say this):**
"Quality can't be tested in at the end — it has to be built in at every phase. That means clear requirements, good design reviews, coding standards and linters, tests written with the code, code reviews, CI checks, and monitoring in production. Each phase has its own quality gate, so problems are caught where they're cheapest to fix."

**Let's understand it fully:**

**Step 1 — The key idea: quality is everyone's job, all the time.**
Bugs are cheapest to fix early. A requirements mistake caught in design costs little; the same mistake found after release costs a fortune.

**Step 2 — Quality gates at each phase.**

| Phase | Quality gate |
|---|---|
| Requirements | clear, confirmed, testable acceptance criteria |
| Design | design review, consider edge cases & non-functional needs |
| Development | linters, standards, tests, code review |
| Testing | the test pyramid + automated regression |
| Deployment | CI checks, staging verification, rollback plan |
| Production | monitoring, alerts, crash reporting |

**Step 3 — Automate the gates.**
CI runs format, lint, and tests on every change and blocks merging if any fail. Automation makes quality consistent and removes human forgetfulness.

**Step 4 — The cost curve.**
The cost of fixing a bug grows roughly 10× each phase it slips. Building quality in early (shift-left, [Q11](#q11)) is the cheapest strategy.

**Why interviewers ask:** It tests whether you see quality as continuous, not a final QA step.

**Common mistake:** "We'll test at the end" — by then, design and requirements bugs are baked in and expensive.

**Follow-ups they may ask:**
- *"How do you measure quality?"* → Bug escape rate, test coverage (with judgment), crash-free users, lead time to fix.

**Related:** [Q11 — shift-left](#q11) · [Q6 — testing phases](#q6) · [Q14 (Clean Code) — enforcing](section_16_clean_code.md#q14)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What is Shift-Left testing, and why is it important?

> Common · Medium

**Short answer (say this):**
"Shift-left means moving testing and quality checks earlier (to the 'left') in the timeline, instead of leaving them to the end. You test as you build, automate checks in CI, and even involve QA during design. It's important because bugs caught early are far cheaper and faster to fix than bugs found in production."

**Let's understand it fully:**

**Step 1 — The picture.**

```
Traditional:  build everything ............... then TEST at the end (right)
Shift-left:   TEST from the start → → → and all along the way (left)
```

**Step 2 — What it looks like in practice.**
- Developers write **unit tests as they code** (or TDD).
- **CI runs tests automatically** on every commit.
- QA gets involved during **requirements/design**, not just at the end.
- **Static analysis/linters** catch issues before code even runs.

**Step 3 — Why it's cheaper.**
A bug found while coding might take minutes to fix. The same bug found in production can mean an incident, a hotfix, and lost trust — orders of magnitude more expensive. Shift-left moves the catch to the cheap end.

**Step 4 — The result.**
Faster feedback, fewer production bugs, and developers who own quality (rather than "throwing it over the wall" to QA at the end).

**Why interviewers ask:** It tests modern quality thinking and overlaps with CI/CD and DevOps.

**Common mistake:** Thinking shift-left means "developers do all the testing and QA isn't needed." It means *everyone* tests *earlier*, QA included.

**Follow-ups they may ask:**
- *"How does CI enable shift-left?"* → It runs the checks automatically and early, on every change, giving instant feedback.

**Related:** [Q10 — quality throughout](#q10) · [Q12 — DevOps](#q12) · [Q6 — testing](#q6)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. What is DevOps culture, and how does it relate to the SDLC?

> Common · Medium

**Short answer (say this):**
"DevOps is a culture where development and operations work as one team, sharing responsibility for building, releasing, and running software. It uses automation — CI/CD, infrastructure as code, monitoring — to ship faster and more reliably. In SDLC terms, it tightens the loop between development, deployment, and maintenance so feedback is fast."

**Let's understand it fully:**

**Step 1 — The problem DevOps solves.**
Traditionally, developers built code and "threw it over the wall" to operations to run — and blamed each other when things broke. DevOps removes that wall: one team owns the whole lifecycle.

**Step 2 — The key practices.**
- **CI/CD** — automatically build, test, and deploy ([Q10 CI/CD](../flutter/Section_10_CICD_Flavors_App_Release.md#q1)).
- **Infrastructure as Code** — servers/config defined in version-controlled files.
- **Monitoring & observability** — see how the system behaves in production.
- **Automation everywhere** — less manual, error-prone work.

**Step 3 — The cultural part (the most important).**
- Shared ownership ("you build it, you run it").
- Fast feedback and continuous improvement.
- Blameless culture for incidents ([Q9](#q9)).

**Step 4 — How it relates to SDLC.**
DevOps makes the SDLC a fast, continuous loop instead of a one-way line — code flows to production quickly and safely, and production feedback flows straight back to development.

**Why interviewers ask:** DevOps is standard in modern teams; they check you understand it's a culture plus automation, not just "a tools team."

**Common mistake:** Thinking DevOps is just a job title or a set of tools. It's primarily a culture of shared ownership, enabled by automation.

**Follow-ups they may ask:**
- *"CI vs CD?"* → CI = integrate + test every change automatically; CD = automatically deliver/deploy that tested change.

**Related:** [Q11 — shift-left](#q11) · [Q10 (CI/CD)](../flutter/Section_10_CICD_Flavors_App_Release.md#q1) · [Q7 — deployment](#q7)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. What is risk management in a software project?

> Common · Medium

**Short answer (say this):**
"Risk management is spotting things that could go wrong before they do, and planning for them. You identify risks (technical, schedule, people, external), judge each by how likely it is and how bad the impact would be, then mitigate the important ones — and keep watching. It's checking the weather before a trip."

**Let's understand it fully:**

**Step 1 — Identify risks.**
Common types: a new technology that might not work, a tight deadline, a key person leaving, a third-party API that could change, unclear requirements.

**Step 2 — Assess by likelihood × impact.**

```
            Impact: Low        High
Likelihood
   High        monitor       ACT NOW (top priority)
   Low         ignore        have a plan ready
```

Focus your energy on high-likelihood, high-impact risks.

**Step 3 — Mitigate.**
- **Reduce likelihood** — e.g. do a spike ([Q15](#q15)) to de-risk new tech.
- **Reduce impact** — e.g. a backup plan, extra buffer in the schedule.
- **Avoid** — change the approach to sidestep the risk.
- **Accept** — for small risks, just acknowledge them.

**Step 4 — Keep watching.**
Risks change over the project. Review them regularly (a risk register) and update plans. New risks appear; old ones fade.

**Why interviewers ask:** Senior engineers anticipate problems; they want to see proactive thinking, not just reacting to fires.

**Common mistake:** Ignoring risks until they become crises, or treating all risks equally instead of prioritizing by likelihood × impact.

**Follow-ups they may ask:**
- *"How do you de-risk new technology?"* → A time-boxed spike to prove it works before committing ([Q15](#q15)).

**Related:** [Q15 — spike](#q15) · [Q2 — requirements (unclear = risk)](#q2)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. What should you document, and what should you NOT over-document?

> Common · Medium

**Short answer (say this):**
"Document the things people need that the code can't tell them: architecture decisions and *why*, setup/onboarding steps, API contracts, and runbooks for operations. Don't over-document things that change constantly or that the code already says — like line-by-line comments or detailed specs that go stale. Good docs are useful and maintained; bad docs mislead."

**Let's understand it fully:**

**Step 1 — Worth documenting (the 'why' and the 'how to operate').**
- **Architecture decisions** and *why* (ADRs — Architecture Decision Records).
- **Onboarding/setup** — how to run the project.
- **API contracts** — endpoints, request/response shapes.
- **Runbooks** — how to deploy, roll back, handle incidents.
- **Non-obvious business rules.**

**Step 2 — NOT worth over-documenting.**
- Comments that restate the code (`i++; // increment`).
- Huge specs that freeze fast-changing details and go stale.
- Anything the code already makes clear with good names ([Q6 Clean Code](section_16_clean_code.md#q6)).

**Step 3 — The guiding rule.**
Document **why**, not **what**. The code shows *what* it does; docs should capture *why* a decision was made and knowledge that isn't in the code.

**Step 4 — Keep docs alive.**
Stale docs are worse than none — they mislead. Keep docs close to the code, lightweight, and updated when things change. If a doc can't be maintained, don't write it.

**Why interviewers ask:** It tests judgment — enough documentation to help, not so much it becomes a burden that rots.

**Common mistake:** Either no documentation (new people are lost) or massive, detailed docs that nobody updates and that quickly mislead.

**Follow-ups they may ask:**
- *"What's an ADR?"* → A short record of a significant decision and the reasoning, so future devs know *why*.

**Related:** [Q6 (Clean Code) — comments](section_16_clean_code.md#q6) · [Q3 — design](#q3)

[↑ Back to top](#toc)

---

# E. Concepts

---

<a id="q15"></a>
## 15. What is a spike, and when do you use it?

> Deeper · Easy–Medium

**Short answer (say this):**
"A spike is a short, time-boxed piece of research to answer a question or reduce uncertainty before committing to real work. You use it when you don't know enough to estimate or design — like trying a new library or proving an approach is feasible. The output is knowledge, not shippable code."

**Let's understand it fully:**

**Step 1 — A real-life picture: a scouting trip.**
Before leading everyone down a path, you send a scout to check it's passable. A spike is that scouting trip for a technical unknown.

**Step 2 — When to use one.**
- A new technology/library you're unsure about.
- A story you can't estimate because it's too uncertain.
- Proving a tricky approach works before building on it.

**Step 3 — Keep it time-boxed.**
A spike has a fixed limit (e.g. "2 days to find out if this works"). The goal is to *learn enough to decide/estimate*, then stop. Without a time-box, research can drag on forever.

**Step 4 — The output is a decision, not a feature.**
A spike usually ends in a recommendation and a better estimate — and the throwaway code is often discarded. The real deliverable is reduced uncertainty.

**Why interviewers ask:** It tests whether you de-risk the unknown before committing — a sign of mature planning.

**Common mistake:** Letting a spike run unbounded (it becomes a rabbit hole), or trying to ship the throwaway spike code as the real solution.

**Follow-ups they may ask:**
- *"Spike vs a normal story?"* → A story delivers a feature; a spike delivers knowledge to make the next story estimable.

**Related:** [Q13 — risk management](#q13) · [Q12 (Agile) — story points](section_18_agile_scrum_methodology.md#q12)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. What is the difference between a bug, a defect, and a feature request?

> Common · Easy

**Short answer (say this):**
"A defect is a flaw in the software found at any stage; a bug is the common word for a defect found while running the software — it behaves differently from the requirement. A feature request is a *new* capability someone wants that was never part of the requirements. The key difference: bugs/defects are 'it's broken'; a feature request is 'I want something new'."

**Let's understand it fully:**

**Step 1 — The distinctions.**
- **Defect** — a flaw versus the intended behaviour. Often used for issues found in testing/review.
- **Bug** — the everyday term for a defect, usually one found when the software runs.
- **Feature request** — a request for new functionality that wasn't specified.

(In many teams "bug" and "defect" are used interchangeably; the important line is *broken* vs *new*.)

**Step 2 — Why the difference matters.**
- A **bug/defect** means the software doesn't meet its existing requirement → fix it (often no extra charge in a contract).
- A **feature request** is new scope → it gets estimated, prioritized, and may cost extra/time.

```
Requirement: "users can reset their password"
Bug:         the reset email never arrives          → it's broken, fix it
Feature:     "also allow reset via SMS"              → new scope, plan it
```

**Step 3 — Why teams care.**
Mislabeling a feature as a "bug" lets scope creep in for free; mislabeling a bug as a "feature" lets real defects get deprioritized. Clear classification keeps planning and contracts honest.

**Why interviewers ask:** It tests precise communication about issues — important for planning and client relationships.

**Common mistake:** Calling every new request a "bug" to get it done faster, or dismissing a real defect as "just a feature request."

**Follow-ups they may ask:**
- *"What about an 'enhancement'?"* → A smaller improvement to existing functionality — still new scope, not a defect.

**Related:** [Q8 — bug tracking](#q8) · [Q11 (Agile) — user stories](section_18_agile_scrum_methodology.md#q11)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## SDLC phases

```
Requirements → Design → Development → Testing → Deployment → Maintenance
   (what)       (how)     (build)      (verify)   (release)    (support)
```

## Testing levels (small → big)

| Level | Checks |
|---|---|
| Unit | one piece alone |
| Integration | pieces together |
| System | the whole app end-to-end |
| UAT | client/user sign-off |

## Easy-to-confuse pairs

| | A | B |
|---|---|---|
| Functional vs non-functional | what it does | how well it does it |
| HLD vs LLD | architecture (city map) | detail (street map) |
| Staging vs production | rehearsal | live |
| Bug vs feature request | it's broken | new scope |

## One-line reminders

- **SDLC** = requirements → design → build → test → deploy → maintain. ([Q1](#q1))
- **Functional** = what; **non-functional** = how well (perf, security). ([Q2](#q2))
- **HLD** = big-picture architecture; **LLD** = detailed classes/methods. ([Q3](#q3))
- **Code review** — correctness & design first; let the linter do style. ([Q5](#q5))
- **Test pyramid** — many unit, fewer integration, few end-to-end. ([Q6](#q6))
- **Staging** mirrors production; always have a **rollback plan**. ([Q7](#q7))
- **Semver**: PATCH=fix, MINOR=feature, MAJOR=breaking. ([Q8](#q8))
- **Production bug**: contain first → diagnose → fix+test → blameless post-mortem. ([Q9](#q9))
- **Quality is built in at every phase**, not tested in at the end. ([Q10](#q10))
- **Shift-left** = test early; early bugs are far cheaper. ([Q11](#q11))
- **DevOps** = dev + ops as one team, automated (CI/CD), shared ownership. ([Q12](#q12))
- **Risk** = likelihood × impact; mitigate the big ones, keep watching. ([Q13](#q13))
- **Document the *why***, not the *what*; keep docs alive. ([Q14](#q14))
- **Spike** = time-boxed research to reduce uncertainty. ([Q15](#q15))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Process interviews probe judgment under pressure. Practice out loud:

1. *"Walk me through your SDLC."* → phases, but stress catching problems early (cheaper).
2. *"Production is down — what's your first move?"* → contain (rollback/flag), then diagnose, then fix with a test.
3. *"How do you ensure quality?"* → built in at every phase, automated in CI, shift-left.
4. *"You're unsure a library will work — what do you do?"* → a time-boxed spike to de-risk before committing.
5. *"Is this a bug or a feature?"* → broken vs new scope; it changes who pays and how it's planned.

Connecting each phase to *cost, quality, and risk* — not just naming it — is the senior signal, in both remote and BD interviews.

[↑ Back to top](#toc)

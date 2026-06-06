# Section 15 — Code Smells & Refactoring

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. Each fix shows before/after Dart.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a step-by-step explanation with before/after code.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** Name the smell, say *why* it hurts, then name the refactoring that fixes it. Refactoring means improving the structure **without changing behaviour** — always say "behaviour stays the same."

---

<a id="toc"></a>

## Table of Contents

**A. Foundations**
1. [Code smell vs bug](#q1) · *Very common*
2. [How to refactor safely](#q2) · *Very common*
3. [How to convince a team to refactor](#q3) · *Common*

**B. Bloater smells**
4. [Long Method](#q4) · *Very common*
5. [Large Class (God Object)](#q5) · *Very common*
6. [Long Parameter List](#q6) · *Common*
7. [Data Clumps](#q7) · *Common*
8. [Primitive Obsession](#q8) · *Common*

**C. Duplication & dead weight**
9. [Duplicate Code](#q9) · *Very common*
10. [Magic Numbers & Strings](#q10) · *Very common*
11. [Dead Code](#q11) · *Common*
12. [Comments as a smell](#q12) · *Common*

**D. Coupling smells**
13. [Feature Envy](#q13) · *Common*
14. [Shotgun Surgery vs Divergent Change](#q14) · *Common*

**E. Refactoring techniques**
15. [Extract Method](#q15) · *Very common*
16. [Extract Class](#q16) · *Common*
17. [Inline Method](#q17) · *Common*
18. [Move Method](#q18) · *Common*
19. [Rename safely](#q19) · *Common*
20. [Introduce Parameter Object](#q20) · *Common*
21. [Replace Temp with Query](#q21) · *Deeper*

**F. Conditional refactorings**
22. [Replace Magic Number with Named Constant](#q22) · *Common*
23. [Replace Conditional with Polymorphism](#q23) · *Very common*
24. [Decompose Conditional](#q24) · *Common*
25. [Consolidate Conditional Expression](#q25) · *Deeper*

**G. Legacy code**
26. [Strangler Fig Pattern](#q26) · *Deeper*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

**Stage 1 — The foundations (start here).**
→ [Q1 Smell vs bug](#q1) · [Q2 Refactor safely](#q2) · [Q15 Extract Method](#q15)

**Stage 2 — The most-named smells.**
→ [Q4 Long Method](#q4) · [Q5 Large Class](#q5) · [Q9 Duplicate Code](#q9) · [Q10 Magic Numbers](#q10)

**Stage 3 — The deeper smells.**
→ [Q6 Long Param List](#q6) · [Q7 Data Clumps](#q7) · [Q8 Primitive Obsession](#q8) · [Q13 Feature Envy](#q13) · [Q14 Shotgun Surgery](#q14)

**Stage 4 — The refactorings.**
→ [Q16 Extract Class](#q16) · [Q18 Move Method](#q18) · [Q20 Parameter Object](#q20) · [Q23 Replace Conditional with Polymorphism](#q23)

**Stage 5 — Advanced & legacy.**
→ [Q21 Replace Temp with Query](#q21) · [Q24 Decompose](#q24) · [Q25 Consolidate](#q25) · [Q26 Strangler Fig](#q26) · [Q3 Convince a team](#q3)

**Short on time?** Review [Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q9](#q9) · [Q10](#q10) · [Q23](#q23), then the [Cheat Sheet](#cheatsheet).

---

# A. Foundations

---

<a id="q1"></a>
## 1. What is a code smell, and how is it different from a bug?

> Very common · Easy

**Short answer (say this):**
"A code smell is a sign that something in the code is poorly structured and may cause trouble later — but it still works correctly. A bug means the code is actually broken. So a smell is a warning about *design*, while a bug is a failure in *behaviour*."

**Let's understand it fully:**

**Step 1 — A real-life picture: a bad smell in the kitchen.**
A bad smell doesn't mean you're sick yet, but it warns that something is rotting. A code smell warns that the code will become hard to change or buggy if ignored.

**Step 2 — The difference.**
- **Bug** → the program gives the wrong result or crashes. Must fix now.
- **Smell** → the program works, but the code is messy (a 300-line method, copy-pasted logic). Fix it to prevent future pain.

```dart
// A smell (works, but a 'God' method doing too much):
void handleOrder() { /* validate, charge, email, log... 200 lines */ }

// A bug (wrong behaviour):
double total(double price, int qty) => price - qty; // should be price * qty
```

**Step 3 — Why smells matter.**
Smells slow the team down: messy code is hard to read, test, and change, and it breeds real bugs over time. Spotting and naming smells is a senior skill.

**Why interviewers ask:** It checks you can judge code *quality*, not just correctness.

**Common mistake:** Treating smells as bugs (urgent crashes) or ignoring them entirely. They're early warnings to address steadily.

**Follow-ups they may ask:**
- *"Give examples of smells."* → Long Method, Duplicate Code, Large Class, Magic Numbers (this section).

**Related:** [Q2 — refactor safely](#q2) · [Q4 — Long Method](#q4)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. How do you refactor safely?

> Very common · Medium

**Short answer (say this):**
"Refactoring means improving the structure of code without changing what it does. To do it safely: make sure tests exist first, change in small steps, and run the tests after each step. If a step breaks a test, you undo just that small step — not a day's work."

**Let's understand it fully:**

**Step 1 — The golden rule: behaviour must not change.**
Refactoring only changes the *shape* of the code. The inputs and outputs stay identical. If behaviour changes, that's a feature change or a bug, not a refactor.

**Step 2 — The safe process.**
1. **Have tests** — they're your safety net that behaviour didn't change.
2. **Small steps** — rename, then extract, then move — one tiny change at a time.
3. **Run tests after each step** — catch a mistake immediately, while it's easy to undo.
4. **Commit often** — small commits make it easy to roll back.

**Step 3 — Why small steps matter.**
If you refactor a whole file at once and tests fail, you don't know which change broke it. Small steps mean the broken step is obvious.

**Step 4 — If there are no tests.**
Add a few "characterization tests" first — tests that lock in the *current* behaviour (even if it's odd). Then refactor with that safety net.

**Why interviewers ask:** It tests discipline. Reckless refactoring breaks production; safe refactoring is a senior habit.

**Common mistake:** Refactoring and adding a feature in the same commit — now you can't tell which change caused a bug. Keep them separate.

**Follow-ups they may ask:**
- *"What if there are no tests?"* → Write characterization tests first to capture current behaviour.

**Related:** [Q3 — convince a team](#q3) · [Q15 — Extract Method](#q15)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. How do you convince a team to refactor old code?

> Common · Medium

**Short answer (say this):**
"I tie refactoring to business value, not 'clean code for its own sake'. I show how the messy area slows delivery or causes bugs, and I refactor in small, safe steps alongside feature work — the 'boy scout rule', leave the code a little cleaner than you found it — rather than asking for a big risky rewrite."

**Let's understand it fully:**

**Step 1 — Speak the team's language: value, not vanity.**
Managers care about delivery speed, bugs, and risk — not "elegance." Frame refactoring as: "this module causes most of our bugs and takes days to change; cleaning it will speed up the next features."

**Step 2 — Use evidence.**
Point to real signals: bug counts in that file, how long recent changes took, repeated hotfixes. Data convinces more than opinion.

**Step 3 — Refactor incrementally, not a big-bang rewrite.**
Big rewrites are risky and often fail. Instead, improve a little with each feature you touch (the **boy scout rule**: "leave the code cleaner than you found it"). This spreads the cost and lowers risk.

**Step 4 — Make it safe and visible.**
Do it behind tests, in small PRs, and show the before/after improvement. Small wins build trust for bigger cleanups later.

**Why interviewers ask:** Senior engineers influence teams. This tests communication and pragmatism, not just coding.

**Common mistake:** Asking to "stop features for two weeks to rewrite everything." That scares stakeholders and usually gets rejected.

**Follow-ups they may ask:**
- *"What's the boy scout rule?"* → Always leave the code a little cleaner than you found it — continuous small improvement.

**Related:** [Q2 — refactor safely](#q2) · [Q26 — Strangler Fig](#q26)

[↑ Back to top](#toc)

---

# B. Bloater smells

---

<a id="q4"></a>
## 4. What is a Long Method, and how do you fix it?

> Very common · Easy–Medium

**Short answer (say this):**
"A Long Method tries to do too much in one place, so it's hard to read and test. The fix is Extract Method — pull each distinct task into its own small, well-named method. A good method does one thing and reads like a short paragraph."

**Let's understand it fully:**

**Step 1 — The smell.**
A method that scrolls for screens, with comments like `// now validate`, `// now save` marking sections — each comment is a hint that a method is hiding inside.

**Step 2 — Before: one long method.**

```dart
void checkout(Cart cart) {
  // validate
  if (cart.items.isEmpty) throw Exception('empty');
  // calculate total
  var total = 0.0;
  for (final i in cart.items) total += i.price * i.qty;
  // apply discount
  if (total > 100) total *= 0.9;
  // ... charge, email, log ...
}
```

**Step 3 — After: extract each task.**

```dart
void checkout(Cart cart) {
  _validate(cart);
  final total = _applyDiscount(_calculateTotal(cart));
  _charge(total);
}

void _validate(Cart cart) { if (cart.items.isEmpty) throw Exception('empty'); }
double _calculateTotal(Cart cart) =>
    cart.items.fold(0.0, (s, i) => s + i.price * i.qty);
double _applyDiscount(double total) => total > 100 ? total * 0.9 : total;
```

Now `checkout` reads like a summary, and each piece is testable on its own.

**Why interviewers ask:** Long methods are the most common smell. They check you split work into small, named pieces.

**Common mistake:** Extracting blindly so the small methods are tightly tangled. Each extracted method should make sense on its own.

**Follow-ups they may ask:**
- *"How long is too long?"* → Less about line count, more about doing one thing. If it needs section comments, it's too long.

**Related:** [Q15 — Extract Method (the how)](#q15) · [Q5 — Large Class](#q5)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What is a Large Class (God Object), and how do you fix it?

> Very common · Medium

**Short answer (say this):**
"A Large Class, or God Object, knows and does too much — it holds many unrelated fields and methods. It breaks the Single Responsibility Principle. The fix is Extract Class: split it into smaller classes, each with one clear job."

**Let's understand it fully:**

**Step 1 — The smell.**
A `User` class that holds profile data *and* sends emails *and* talks to the database *and* formats dates. It has a reason to change for every one of those concerns.

**Step 2 — Before: one God class.**

```dart
class User {
  String name = '';
  void saveToDb() {/* db code */}
  void sendEmail() {/* email code */}
  String formatJoinDate() {/* date code */}
}
```

**Step 3 — After: split responsibilities.**

```dart
class User { String name = ''; }
class UserRepository { void save(User u) {/* db */} }
class EmailService { void sendWelcome(User u) {/* email */} }
```

Each class now has one reason to change (high cohesion, [SRP](section_12_oop_design_principles.md#q10)).

**Why interviewers ask:** God objects are a top cause of unmaintainable code. They check you can apply SRP.

**Common mistake:** Over-splitting into dozens of tiny classes for a small app. Split by *responsibility*, not by line count.

**Follow-ups they may ask:**
- *"How do you spot which methods to extract?"* → Group fields and methods that change together; each group becomes a class.

**Related:** [Q16 — Extract Class (the how)](#q16) · [Q4 — Long Method](#q4)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What is a Long Parameter List, and how do you fix it?

> Common · Easy–Medium

**Short answer (say this):**
"A Long Parameter List means a method takes too many arguments, which is hard to read and easy to pass in the wrong order. The fix is Introduce Parameter Object — group related parameters into one small object. In Dart, named parameters also help a lot."

**Let's understand it fully:**

**Step 1 — The smell.**

```dart
void createUser(String first, String last, String street, String city, String zip, String country) {}
// six positional args — easy to mix up; what's the order again?
```

**Step 2 — The fix: group related ones into an object.**

```dart
class Address {
  final String street, city, zip, country;
  Address(this.street, this.city, this.zip, this.country);
}

void createUser(String first, String last, Address address) {} // clear groups
```

**Step 3 — Dart's extra help: named parameters.**
Even without a parameter object, named parameters remove the ordering risk:

```dart
void createUser({required String first, required String last, required Address address}) {}
```

**Why interviewers ask:** It tests readable API design and recognizing when data belongs together.

**Common mistake:** Bundling unrelated parameters into one object just to shorten the list — group only things that truly belong together (see [Data Clumps](#q7)).

**Follow-ups they may ask:**
- *"When is it worth a parameter object?"* → When the same group of parameters travels together in several methods.

**Related:** [Q20 — Introduce Parameter Object (the how)](#q20) · [Q7 — Data Clumps](#q7)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. What are Data Clumps, and how do you fix them?

> Common · Medium

**Short answer (say this):**
"Data Clumps are the same group of variables that keep appearing together — like `startDate` and `endDate`, or `x` and `y` everywhere. It's a sign they should be one object. The fix is to wrap the clump in a small class, which also gives a home for related behaviour."

**Let's understand it fully:**

**Step 1 — The smell: the same trio travels everywhere.**

```dart
void book(DateTime start, DateTime end) {}
bool overlaps(DateTime start, DateTime end, DateTime start2, DateTime end2) {}
// start + end keep appearing as a pair
```

**Step 2 — The fix: make the clump a class.**

```dart
class DateRange {
  final DateTime start, end;
  DateRange(this.start, this.end);
  bool overlaps(DateRange other) => start.isBefore(other.end) && other.start.isBefore(end);
}

void book(DateRange range) {}
```

Now the pair is one concept, and behaviour like `overlaps` lives where it belongs.

**Step 3 — Why it helps.**
It removes repetition, makes signatures shorter, and gives a place for related logic — turning scattered data into a meaningful object.

**Why interviewers ask:** It tests whether you notice hidden concepts (a `DateRange`, a `Money`) buried in loose variables.

**Common mistake:** Leaving the clump scattered, so the same validation/logic is duplicated wherever the pair appears.

**Follow-ups they may ask:**
- *"Data Clumps vs Primitive Obsession?"* → Clumps = a *group* that belongs together; Primitive Obsession = a *single* primitive that should be a typed value object ([Q8](#q8)).

**Related:** [Q6 — Long Parameter List](#q6) · [Q8 — Primitive Obsession](#q8)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is Primitive Obsession, and how do you fix it with value objects?

> Common · Medium

**Short answer (say this):**
"Primitive Obsession is using raw primitives (String, int) for concepts that deserve their own type — like a `String` for an email or an `int` for money. The fix is a value object: a small class that wraps the primitive and enforces its rules, so invalid values can't exist."

**Let's understand it fully:**

**Step 1 — The smell.**

```dart
void sendEmail(String email) {} // any string passes — even "not-an-email"
double price = 999;             // is that dollars? cents? taka?
```

The type doesn't carry the meaning or the rules.

**Step 2 — The fix: a value object that validates.**

```dart
class Email {
  final String value;
  Email(this.value) {
    if (!value.contains('@')) throw ArgumentError('invalid email');
  }
}

void sendEmail(Email email) {} // now only a valid Email can be passed
```

**Step 3 — Why it helps.**
- Invalid states become impossible (validation lives in one place).
- The type documents the meaning (`Money`, `Email`, `PhoneNumber`).
- Related behaviour has a home (`Money.add`, `Email.domain`).

**Why interviewers ask:** It tests whether you let the type system protect you, instead of validating the same primitive everywhere.

**Common mistake:** Wrapping every primitive in a value object, even trivial ones — adds noise. Use it for concepts with real rules or behaviour.

**Follow-ups they may ask:**
- *"Where have you used this?"* → `Money`, `Email`, `UserId` — anything with validation or units.

**Related:** [Q7 — Data Clumps](#q7) · [Q10 — Magic Numbers](#q10)

[↑ Back to top](#toc)

---

# C. Duplication & dead weight

---

<a id="q9"></a>
## 9. What is Duplicate Code, and how do you fix it?

> Very common · Easy

**Short answer (say this):**
"Duplicate Code is the same logic copy-pasted in several places. It's dangerous because a change means fixing every copy, and you'll miss one. The fix is to pull the shared logic into one function or class — the DRY principle. But be careful only to merge code that represents the same *knowledge*."

**Let's understand it fully:**

**Step 1 — The smell.**

```dart
double priceA(double p) => p - (p * 0.1);
double priceB(double p) => p - (p * 0.1); // same logic, two places
```

**Step 2 — The fix: one source of truth.**

```dart
double applyDiscount(double price, double rate) => price - (price * rate);
```

Change the rule once; everywhere updates.

**Step 3 — The caution.**
Don't merge code just because it *looks* the same today. If two pieces represent different rules that happen to match, forcing them together creates bad coupling. DRY is about removing duplicate *knowledge*, not duplicate-looking lines.

**Why interviewers ask:** Duplication is the most common, most damaging smell. They check you fix it the right way.

**Common mistake:** Over-DRYing — merging unrelated code into one tangled function with many flags.

**Follow-ups they may ask:**
- *"DRY downside?"* → Premature merging couples things that should evolve separately; a little duplication is sometimes healthier.

**Related:** [Q15 — Extract Method](#q15) · [Q12 (OOP) — DRY](section_12_oop_design_principles.md#q15)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What are Magic Numbers and Magic Strings, and how do you fix them?

> Very common · Easy

**Short answer (say this):**
"Magic numbers and strings are unexplained literal values sprinkled in the code, like `if (status == 3)` or `'admin'`. Nobody knows what they mean, and changing one means hunting through the codebase. The fix is to replace them with named constants or enums."

**Let's understand it fully:**

**Step 1 — The smell.**

```dart
if (user.role == 1) {}          // what is 1?
if (status == 'A') {}           // what is 'A'?
final price = total * 0.15;     // 0.15 is... tax? discount?
```

**Step 2 — The fix: name them.**

```dart
const taxRate = 0.15;
final price = total * taxRate;  // now it's obvious

enum Role { user, admin, owner } // even better than constants for a fixed set
if (user.role == Role.admin) {}
```

**Step 3 — Why it helps.**
- The name explains the meaning.
- Change the value in one place.
- A typo becomes a compile error (with enums) instead of a silent bug.

**Why interviewers ask:** It's a basic readability habit they expect every engineer to have.

**Common mistake:** Naming truly self-evident values (`* 2` to double) — that adds noise. Name values that carry *meaning*.

**Follow-ups they may ask:**
- *"Constant vs enum?"* → Enum for a fixed set of related options (roles, statuses); constant for a single named value.

**Related:** [Q22 — Replace Magic Number with Named Constant](#q22) · [Q8 — Primitive Obsession](#q8)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What is Dead Code, and why is it dangerous?

> Common · Easy

**Short answer (say this):**
"Dead code is code that's never used — unused functions, variables, commented-out blocks, or unreachable branches. It's dangerous because it confuses readers, hides real logic, and rots over time. The fix is simple: delete it. Version control remembers it if you ever need it back."

**Let's understand it fully:**

**Step 1 — The smell.**

```dart
// final oldDiscount = 0.2; // we don't use this anymore
void unusedHelper() {}      // never called
if (false) { doThing(); }   // unreachable
```

**Step 2 — Why it's dangerous.**
- Readers waste time figuring out if it matters.
- It can hide bugs (you "fix" dead code thinking it runs).
- It drifts out of date and misleads.

**Step 3 — The fix: delete it.**
Don't comment it out "just in case" — that's the worst of both worlds. Git keeps history; you can recover anything.

```dart
// Just delete the unused parts. The codebase gets lighter and clearer.
```

**Why interviewers ask:** It tests whether you keep the codebase clean and trust version control.

**Common mistake:** Keeping big blocks of commented-out code "for reference." It rots and clutters.

**Follow-ups they may ask:**
- *"How do you find dead code?"* → IDE warnings, linters (`dart analyze`), and coverage reports.

**Related:** [Q2 — refactor safely](#q2) · [Q12 — comments as a smell](#q12)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. When do comments become a code smell?

> Common · Easy–Medium

**Short answer (say this):**
"Comments become a smell when they explain *what* badly-written code does, instead of the code explaining itself. A comment that restates the code, or apologizes for messy logic, usually means the code should be refactored. Good comments explain *why*, not *what*."

**Let's understand it fully:**

**Step 1 — The bad comment: explaining unclear code.**

```dart
// check if user is an adult
if (u.a >= 18) {} // the comment exists because the code is cryptic
```

**Step 2 — The fix: make the code self-explaining.**

```dart
if (user.isAdult) {} // no comment needed — the name says it
```

Extract a well-named method or variable, and the comment disappears.

**Step 3 — When comments are GOOD.**
- Explaining **why** (a non-obvious decision, a workaround, a business rule).
- Warnings ("this must run before X").
- Public API docs.

```dart
// Stripe rounds half-up, so we match that to avoid off-by-one refunds.
final cents = (amount * 100).round();
```

**Why interviewers ask:** It tests whether you write self-documenting code instead of leaning on comments.

**Common mistake:** Writing comments that restate the code (`i++; // increment i`), which just adds noise and goes stale.

**Follow-ups they may ask:**
- *"What's a good comment?"* → One that explains *why*, captures intent, or warns — things the code can't say itself.

**Related:** [Q16 (Clean Code) — comments](section_16_clean_code.md#q1) · [Q15 — Extract Method](#q15)

[↑ Back to top](#toc)

---

# D. Coupling smells

---

<a id="q13"></a>
## 13. What is Feature Envy, and how do you fix it?

> Common · Medium

**Short answer (say this):**
"Feature Envy is when a method is more interested in another class's data than its own — it keeps reaching into another object's fields to do its work. The fix is Move Method: move that logic to the class that owns the data, so behaviour lives with the data it uses."

**Let's understand it fully:**

**Step 1 — The smell.**

```dart
class Order {
  double total(Customer c) {
    // this method keeps poking into Customer's fields
    return c.cartSubtotal * (1 - c.loyaltyDiscount) + c.shippingFee;
  }
}
```

`Order.total` uses mostly `Customer` data — it envies `Customer`'s features.

**Step 2 — The fix: move the logic to where the data lives.**

```dart
class Customer {
  double cartSubtotal = 0, loyaltyDiscount = 0, shippingFee = 0;
  double total() => cartSubtotal * (1 - loyaltyDiscount) + shippingFee; // now here
}
```

**Step 3 — The guiding idea.**
"Put behaviour next to the data it operates on." This reduces coupling — classes stop reaching into each other's internals.

**Why interviewers ask:** It tests whether you place logic where it belongs, a sign of good object design.

**Common mistake:** Leaving the method where it is and exposing more getters from the other class — that increases coupling instead of fixing it.

**Follow-ups they may ask:**
- *"When is reaching into another class okay?"* → Sometimes (e.g. a coordinator/service), but if a method uses mostly another class's data, move it.

**Related:** [Q18 — Move Method (the how)](#q18) · [Q14 — Shotgun Surgery](#q14)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. What is Shotgun Surgery, and how is it different from Divergent Change?

> Common · Medium

**Short answer (say this):**
"Shotgun Surgery is when one small change forces edits in many different classes — the logic is scattered. Divergent Change is the opposite: one class has to be changed for many different reasons. Shotgun Surgery means 'too spread out'; Divergent Change means 'too much in one place'."

**Let's understand it fully:**

**Step 1 — Shotgun Surgery — one change, many files.**
Example: changing how a tax is calculated means editing 8 different classes that each do their own tax math. The fix is to **gather** the scattered logic into one place (a `TaxCalculator`).

**Step 2 — Divergent Change — one class, many reasons.**
Example: a `UserManager` must change when the UI changes, when the database changes, and when email rules change. The fix is to **split** it by responsibility (Extract Class, [SRP](section_12_oop_design_principles.md#q10)).

**Step 3 — The easy way to remember.**

| Smell | Problem | Fix |
|---|---|---|
| Shotgun Surgery | one change → many classes (too scattered) | gather logic into one class |
| Divergent Change | one class → many reasons (too crowded) | split the class |

They're mirror images: one is too spread out, the other too concentrated.

**Why interviewers ask:** They're commonly confused; explaining the difference shows real understanding of cohesion and coupling.

**Common mistake:** Mixing the two up. Remember: shotgun = scattered (gather it); divergent = crowded (split it).

**Follow-ups they may ask:**
- *"Which principle do both relate to?"* → Both are about cohesion — keeping related things together and unrelated things apart.

**Related:** [Q5 — Large Class](#q5) · [Q13 — Feature Envy](#q13) · [Q9 (coupling/cohesion)](section_12_oop_design_principles.md#q9)

[↑ Back to top](#toc)

---

# E. Refactoring techniques

---

<a id="q15"></a>
## 15. Extract Method — how and when?

> Very common · Easy

**Short answer (say this):**
"Extract Method takes a chunk of code and turns it into its own well-named method. You do it when a piece of code does one identifiable task, or when you'd otherwise write a comment to explain a block. The method name then replaces the comment."

**Let's understand it fully:**

**Step 1 — When to use it.**
- A method is too long ([Q4](#q4)).
- A block needs a `// explanation` comment.
- The same few lines appear in two places.

**Step 2 — How (before/after).**

```dart
// Before
void printReport(List<Order> orders) {
  // calculate total
  var total = 0.0;
  for (final o in orders) total += o.amount;
  print('Total: $total');
}

// After — the comment becomes a method name
void printReport(List<Order> orders) {
  print('Total: ${_calculateTotal(orders)}');
}
double _calculateTotal(List<Order> orders) =>
    orders.fold(0.0, (s, o) => s + o.amount);
```

**Step 3 — Do it safely.**
Extract, run tests, repeat. Modern IDEs do "Extract Method" automatically and safely — use that.

**Why interviewers ask:** It's the single most-used refactoring and the cure for long methods.

**Common mistake:** Giving the extracted method a vague name (`_doStuff`). The name should say exactly what it does.

**Follow-ups they may ask:**
- *"Opposite of Extract Method?"* → Inline Method ([Q17](#q17)) — remove a method that's pointless indirection.

**Related:** [Q4 — Long Method](#q4) · [Q17 — Inline Method](#q17)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. Extract Class — how and when?

> Common · Medium

**Short answer (say this):**
"Extract Class splits a class that's doing two jobs into two classes. You do it when a class has grown too large, or when a group of its fields and methods clearly belong together as their own concept. It's the main fix for a God Object."

**Let's understand it fully:**

**Step 1 — When to use it.**
A class has two clusters of fields/methods that change for different reasons — a sign of a hidden second class.

**Step 2 — How (before/after).**

```dart
// Before — Person also handles phone details
class Person {
  String name = '';
  String areaCode = '';
  String number = '';
  String phoneNumber() => '($areaCode) $number';
}

// After — phone becomes its own class
class Person {
  String name = '';
  Phone phone = Phone('', '');
}
class Phone {
  final String areaCode, number;
  Phone(this.areaCode, this.number);
  String formatted() => '($areaCode) $number';
}
```

**Step 3 — Do it gradually.**
Create the new class, move one field/method at a time, run tests, repeat — small safe steps.

**Why interviewers ask:** It's the practical tool for applying SRP to bloated classes.

**Common mistake:** Splitting into classes that still depend heavily on each other — find a clean seam where the new class is fairly independent.

**Follow-ups they may ask:**
- *"How do you find the seam?"* → Look for fields and methods that are used together and not by the rest.

**Related:** [Q5 — Large Class](#q5) · [Q18 — Move Method](#q18)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. Inline Method — when is a method unnecessary indirection?

> Common · Easy

**Short answer (say this):**
"Inline Method is the opposite of Extract Method: when a method's body is just as clear as its name and adds no value, you replace calls to it with the body and delete it. You do it to remove pointless indirection that makes the code harder to follow."

**Let's understand it fully:**

**Step 1 — The smell: a method that adds nothing.**

```dart
// Before — the method just wraps one trivial expression
int getRating(Driver d) => moreThanFiveLateDeliveries(d) ? 2 : 1;
bool moreThanFiveLateDeliveries(Driver d) => d.lateDeliveries > 5;
```

**Step 2 — After: inline it.**

```dart
int getRating(Driver d) => d.lateDeliveries > 5 ? 2 : 1;
```

The extra method didn't make things clearer, so removing it simplifies the code.

**Step 3 — When NOT to inline.**
If the method name adds meaning, is used in many places, or could be overridden, keep it. Inline only when the indirection is genuinely pointless.

**Why interviewers ask:** It shows you balance "extract for clarity" with "don't over-fragment." Both directions matter.

**Common mistake:** Inlining a method that's used in many places or that documents intent — that hurts readability.

**Follow-ups they may ask:**
- *"When extract vs inline?"* → Extract when a block needs a name; inline when a method adds no meaning.

**Related:** [Q15 — Extract Method](#q15)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. Move Method — how and when?

> Common · Medium

**Short answer (say this):**
"Move Method moves a method to the class whose data it mostly uses. You do it to fix Feature Envy and to put behaviour next to the data it works on, which lowers coupling between classes."

**Let's understand it fully:**

**Step 1 — When to use it.**
A method uses another class's fields more than its own ([Feature Envy](#q13)), or it would clearly fit better elsewhere.

**Step 2 — How (before/after).**

```dart
// Before — discount logic lives on Order but uses Account
class Order {
  double discount(Account account) => account.isPremium ? 0.2 : 0.0;
}

// After — moved to Account, where the data lives
class Account {
  bool isPremium = false;
  double discount() => isPremium ? 0.2 : 0.0;
}
```

**Step 3 — Do it safely.**
Copy the method to the target class, adjust references, update callers, run tests, then remove the old one.

**Why interviewers ask:** It's the concrete fix for Feature Envy and tests good placement of behaviour.

**Common mistake:** Moving a method but leaving callers reaching across classes, which doesn't actually reduce coupling.

**Follow-ups they may ask:**
- *"How do you decide the right home?"* → The class whose data the method uses most.

**Related:** [Q13 — Feature Envy](#q13) · [Q16 — Extract Class](#q16)

[↑ Back to top](#toc)

---

<a id="q19"></a>
## 19. How do you Rename (a method, variable, or class) safely?

> Common · Easy

**Short answer (say this):**
"Renaming is the simplest, highest-value refactoring — a clear name removes the need for comments. To do it safely, use the IDE's Rename refactoring so every reference updates at once, and run the tests. Never rename with find-and-replace text, which can hit unrelated matches."

**Let's understand it fully:**

**Step 1 — Why renaming matters.**
A vague name (`data`, `temp`, `flag`, `process()`) forces readers to dig. A clear name (`unpaidInvoices`, `isExpired`, `sendReceipt()`) explains itself. Good names are the cheapest documentation.

**Step 2 — The safe way: IDE rename.**
The IDE's "Rename" understands the code, so it updates every real reference (and only those) and leaves unrelated text alone.

```dart
// Before
var d = users.where((u) => u.active).toList();
// After (renamed for clarity)
var activeUsers = users.where((u) => u.active).toList();
```

**Step 3 — Avoid text find-and-replace.**
Plain text replace can change a comment, a string, or a different variable with the same name. Use the language-aware rename and run tests after.

**Why interviewers ask:** It tests whether you value clear names and use safe tooling.

**Common mistake:** Renaming with a raw find-and-replace and accidentally changing unrelated code or strings.

**Follow-ups they may ask:**
- *"What makes a good name?"* → It reveals intent: what it is or does, no abbreviations, no need for a comment.

**Related:** [Q12 — comments as a smell](#q12) · [Q1 (Clean Code) — naming](section_16_clean_code.md#q1)

[↑ Back to top](#toc)

---

<a id="q20"></a>
## 20. Introduce Parameter Object — when and how?

> Common · Medium

**Short answer (say this):**
"Introduce Parameter Object groups several parameters that travel together into a single object. You use it to shorten long parameter lists and to give the group a name and a home for related behaviour. It's the fix for Long Parameter List and Data Clumps."

**Let's understand it fully:**

**Step 1 — When to use it.**
The same set of parameters appears in multiple method signatures, or a method takes too many arguments.

**Step 2 — How (before/after).**

```dart
// Before
double amountInvoiced(DateTime start, DateTime end) => 0;
double amountReceived(DateTime start, DateTime end) => 0;

// After — group the pair into a DateRange
class DateRange {
  final DateTime start, end;
  DateRange(this.start, this.end);
  int get days => end.difference(start).inDays; // behaviour now has a home
}
double amountInvoiced(DateRange range) => 0;
double amountReceived(DateRange range) => 0;
```

**Step 3 — The bonus.**
Once the parameters are an object, you can move related logic onto it (like `days` above), which often reveals more refactorings.

**Why interviewers ask:** It tests recognizing hidden objects and cleaning up method signatures.

**Common mistake:** Bundling unrelated parameters just to shorten the list. Group only parameters that genuinely belong together.

**Follow-ups they may ask:**
- *"What's the relationship to Data Clumps?"* → A parameter object is the fix for a data clump that shows up in parameters.

**Related:** [Q6 — Long Parameter List](#q6) · [Q7 — Data Clumps](#q7)

[↑ Back to top](#toc)

---

<a id="q21"></a>
## 21. Replace Temp with Query — what is it?

> Deeper · Medium

**Short answer (say this):**
"Replace Temp with Query turns a temporary variable that holds a calculation into a small method (a 'query') that computes it. This removes duplicated temp variables, makes the calculation reusable, and often enables extracting larger methods."

**Let's understand it fully:**

**Step 1 — The smell: a temp that just holds a calculation.**

```dart
double price() {
  final basePrice = quantity * itemPrice; // a temp
  if (basePrice > 1000) return basePrice * 0.95;
  return basePrice * 0.98;
}
```

**Step 2 — The fix: make it a query method.**

```dart
double get _basePrice => quantity * itemPrice; // now a reusable query
double price() {
  if (_basePrice > 1000) return _basePrice * 0.95;
  return _basePrice * 0.98;
}
```

**Step 3 — Why it helps.**
- The calculation is reusable anywhere in the class, not trapped in one method.
- It makes the surrounding method easier to break apart (Extract Method) because there's no shared temp to drag along.

**Step 4 — The trade-off.**
A query recomputes each time it's called. For cheap calculations that's fine; for expensive ones, keep the temp or cache.

**Why interviewers ask:** It's a deeper Fowler refactoring that tests whether you can clean up local-variable clutter.

**Common mistake:** Replacing an expensive calculation with a query that's called many times — that can hurt performance.

**Follow-ups they may ask:**
- *"Why does this enable Extract Method?"* → Methods sharing the same temp are hard to split; a query removes that shared dependency.

**Related:** [Q15 — Extract Method](#q15) · [Q4 — Long Method](#q4)

[↑ Back to top](#toc)

---

# F. Conditional refactorings

---

<a id="q22"></a>
## 22. Replace Magic Number with Named Constant — how to do it correctly in Dart?

> Common · Easy

**Short answer (say this):**
"You give an unexplained literal a named constant, so the meaning is clear and the value lives in one place. In Dart, use `const` for compile-time values and `static const` for class-level constants. For a fixed set of related values, an enum is even better."

**Let's understand it fully:**

**Step 1 — Before: a magic number.**

```dart
double area(double r) => 3.14159 * r * r; // what is 3.14159?
if (attempts > 3) lockAccount();           // why 3?
```

**Step 2 — After: named constants.**

```dart
const double pi = 3.14159;
const int maxLoginAttempts = 3;

double area(double r) => pi * r * r;
if (attempts > maxLoginAttempts) lockAccount();
```

**Step 3 — Dart specifics.**
- `const` — compile-time constant; prefer it for fixed values.
- `static const` inside a class — for grouped constants (`AppColors.primary`).
- Enum — for a fixed set of options instead of magic ints/strings.

**Why interviewers ask:** It's a basic, expected readability habit, and they check you know Dart's `const`/`static const`/enum choices.

**Common mistake:** Using a non-const variable for a value that never changes, or naming truly obvious literals (adding noise).

**Follow-ups they may ask:**
- *"const vs final for constants?"* → `const` is compile-time and canonicalized; use it for fixed constants. `final` is set-once at runtime.

**Related:** [Q10 — Magic Numbers (the smell)](#q10) · [Q23 — Replace Conditional with Polymorphism](#q23)

[↑ Back to top](#toc)

---

<a id="q23"></a>
## 23. Replace Conditional with Polymorphism — when and how?

> Very common · Medium–Hard

**Short answer (say this):**
"When you have a big switch or if/else that behaves differently based on a type, you can replace it with polymorphism: make each case its own class that implements a shared method. Then adding a new case means adding a class, not editing the conditional — that's the Open/Closed Principle."

**Let's understand it fully:**

**Step 1 — The smell: a type-based conditional.**

```dart
double pay(Employee e) {
  switch (e.type) {
    case 'engineer': return e.base;
    case 'manager': return e.base + e.bonus;
    case 'sales': return e.base + e.commission;
  }
  return 0;
}
```

Every new employee type forces editing this method.

**Step 2 — The fix: a class per case.**

```dart
abstract class Employee { double pay(); }
class Engineer extends Employee {
  final double base; Engineer(this.base);
  @override double pay() => base;
}
class Manager extends Employee {
  final double base, bonus; Manager(this.base, this.bonus);
  @override double pay() => base + bonus;
}
// Add Sales by adding a class — no existing code changes.

double pay(Employee e) => e.pay(); // the conditional is gone
```

**Step 3 — When NOT to do this.**
If there are only two cases that rarely change, a simple `if` is clearer. Polymorphism shines when cases grow or change often. (Dart's sealed classes + switch are a good middle ground for a fixed set.)

**Why interviewers ask:** It's the classic OOP move that connects refactoring to the Open/Closed Principle ([Q11 OCP](section_12_oop_design_principles.md#q11)).

**Common mistake:** Applying it to a tiny, stable conditional — that's over-engineering. Use judgment.

**Follow-ups they may ask:**
- *"Isn't a sealed class + switch also fine?"* → Yes — it gives compile-time exhaustiveness; pick it when the set is fixed and you want the compiler to catch missing cases.

**Related:** [Q11 (OCP)](section_12_oop_design_principles.md#q11) · [Q24 — Decompose Conditional](#q24)

[↑ Back to top](#toc)

---

<a id="q24"></a>
## 24. What is the Decompose Conditional refactoring?

> Common · Easy–Medium

**Short answer (say this):**
"Decompose Conditional breaks a complex if/else into well-named methods — one for the condition, and one for each branch. The logic becomes readable: instead of a tangled boolean, you read a sentence."

**Let's understand it fully:**

**Step 1 — Before: a hard-to-read condition.**

```dart
if (date.isBefore(summerStart) || date.isAfter(summerEnd)) {
  charge = quantity * winterRate + winterServiceCharge;
} else {
  charge = quantity * summerRate;
}
```

**Step 2 — After: name the parts.**

```dart
if (_isWinter(date)) {
  charge = _winterCharge(quantity);
} else {
  charge = _summerCharge(quantity);
}

bool _isWinter(DateTime d) => d.isBefore(summerStart) || d.isAfter(summerEnd);
double _winterCharge(int qty) => qty * winterRate + winterServiceCharge;
double _summerCharge(int qty) => qty * summerRate;
```

Now the `if` reads almost like English.

**Step 3 — Why it helps.**
The *intent* (winter vs summer pricing) becomes obvious, and each piece is testable. It's Extract Method applied to a conditional.

**Why interviewers ask:** It tests making complex logic readable — a core daily skill.

**Common mistake:** Leaving a giant boolean expression inline that readers must decode every time.

**Follow-ups they may ask:**
- *"How is this different from Consolidate Conditional?"* → Decompose *names* the parts of one condition; Consolidate *merges* several conditions with the same result ([Q25](#q25)).

**Related:** [Q15 — Extract Method](#q15) · [Q25 — Consolidate Conditional](#q25)

[↑ Back to top](#toc)

---

<a id="q25"></a>
## 25. What is Consolidate Conditional Expression?

> Deeper · Easy–Medium

**Short answer (say this):**
"Consolidate Conditional Expression combines several separate checks that all lead to the *same* result into one condition, then names it. It removes repetition and makes the shared outcome clear."

**Let's understand it fully:**

**Step 1 — Before: several checks, same result.**

```dart
double disabilityAmount(Employee e) {
  if (e.seniority < 2) return 0;
  if (e.monthsDisabled > 12) return 0;
  if (e.isPartTime) return 0;
  // ... real calculation
  return e.base * 0.5;
}
```

Three separate `if`s all return 0 — repetition.

**Step 2 — After: combine and name.**

```dart
double disabilityAmount(Employee e) {
  if (_isNotEligible(e)) return 0;
  return e.base * 0.5;
}
bool _isNotEligible(Employee e) =>
    e.seniority < 2 || e.monthsDisabled > 12 || e.isPartTime;
```

**Step 3 — Why it helps.**
The shared outcome ("not eligible → 0") is now one clear idea with a name, instead of three scattered checks.

**Step 4 — When NOT to do it.**
If the checks are truly independent (different results, side effects), keep them separate. Only consolidate checks that share the *same* result.

**Why interviewers ask:** A deeper refactoring that tests spotting repeated outcomes in conditionals.

**Common mistake:** Merging conditions that don't actually share a result, hiding important distinct logic.

**Follow-ups they may ask:**
- *"Decompose vs Consolidate?"* → Decompose splits one complex condition into named parts; Consolidate merges many simple conditions with one result.

**Related:** [Q24 — Decompose Conditional](#q24)

[↑ Back to top](#toc)

---

# G. Legacy code

---

<a id="q26"></a>
## 26. What is the Strangler Fig Pattern, and when do you use it?

> Deeper · Medium

**Short answer (say this):**
"The Strangler Fig pattern replaces an old system gradually, piece by piece, instead of in one risky big-bang rewrite. You build the new code around the old, route a little traffic to it at a time, and slowly 'strangle' the old system until it can be removed. You use it for large legacy migrations."

**Let's understand it fully:**

**Step 1 — A real-life picture: the strangler fig tree.**
A strangler fig grows around a host tree, slowly taking over, until the original tree is gone but the structure remains. The pattern replaces a legacy system the same way — gradually.

**Step 2 — How it works.**
1. Put a layer (a facade or router) in front of the old system.
2. Build the new version of one feature.
3. Route that one feature's traffic to the new code; everything else still uses the old.
4. Repeat feature by feature.
5. When nothing uses the old system, delete it.

```
Requests → [Router] → mostly OLD system
                    → a few features → NEW system
   (over time, more and more routes move to NEW, until OLD is gone)
```

**Step 3 — Why it beats a big rewrite.**
- **Lower risk** — small pieces, each reversible.
- **Continuous delivery** — the app keeps working throughout.
- **Early feedback** — you learn from each migrated piece.

Big-bang rewrites are famous for failing (they take longer than planned and the old system keeps changing). Strangler Fig avoids that.

**Why interviewers ask:** It's the senior answer to "how do you modernize a large legacy app safely?"

**Common mistake:** Proposing a full rewrite from scratch — high risk, often never finishes, and the business stalls.

**Follow-ups they may ask:**
- *"Mobile example?"* → Migrating screen by screen from an old architecture to a new one (e.g. old state management to BLoC), behind a routing/feature-flag layer.

**Related:** [Q3 — convince a team](#q3) · [Q2 — refactor safely](#q2)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## Smell → the refactoring that fixes it

| Smell | Fix |
|---|---|
| Long Method | Extract Method ([Q15](#q15)) |
| Large Class / God Object | Extract Class ([Q16](#q16)) |
| Long Parameter List / Data Clumps | Introduce Parameter Object ([Q20](#q20)) |
| Primitive Obsession | value object ([Q8](#q8)) |
| Duplicate Code | Extract + DRY ([Q9](#q9)) |
| Magic Numbers | Named Constant / enum ([Q22](#q22)) |
| Feature Envy | Move Method ([Q18](#q18)) |
| Type-based switch | Replace Conditional with Polymorphism ([Q23](#q23)) |
| Complex conditional | Decompose Conditional ([Q24](#q24)) |

## Confusing pairs

- **Shotgun Surgery vs Divergent Change** → scattered (gather it) vs crowded (split it). ([Q14](#q14))
- **Data Clumps vs Primitive Obsession** → a *group* belongs together vs a *single* primitive needs a type. ([Q7](#q7), [Q8](#q8))
- **Extract vs Inline Method** → name a block vs remove pointless indirection. ([Q15](#q15), [Q17](#q17))
- **Decompose vs Consolidate Conditional** → split one condition vs merge many with one result. ([Q24](#q24), [Q25](#q25))

## One-line reminders

- **Code smell** = a design warning; the code still works (vs a bug). ([Q1](#q1))
- **Refactoring** = improve structure, **behaviour stays the same**; tests first, small steps. ([Q2](#q2))
- **Long Method** → Extract Method; **Large Class** → Extract Class. ([Q4](#q4), [Q5](#q5))
- **Duplicate Code** → one source of truth (DRY) — but only merge same *knowledge*. ([Q9](#q9))
- **Magic Numbers** → named constants / enums. ([Q10](#q10), [Q22](#q22))
- **Feature Envy** → put behaviour next to its data (Move Method). ([Q13](#q13), [Q18](#q18))
- **Big type-switch** → polymorphism (Open/Closed). ([Q23](#q23))
- **Comments smell** when they explain bad code; good comments explain *why*. ([Q12](#q12))
- **Convince a team** → tie to business value, do it incrementally (boy scout rule). ([Q3](#q3))
- **Strangler Fig** → migrate legacy gradually, never a big-bang rewrite. ([Q26](#q26))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers show you messy code and ask you to improve it. Practice out loud:

1. *"This method is 150 lines — what do you do?"* → name the smell (Long Method), Extract Method for each task.
2. *"How do you make sure you didn't break anything?"* → tests first, small steps, run tests after each.
3. *"There's a big switch on `type` — improve it."* → Replace Conditional with Polymorphism (open/closed).
4. *"The whole app uses an old architecture — how do you modernize?"* → Strangler Fig, screen by screen, not a rewrite.
5. *"The team says there's no time to refactor."* → tie it to bug rates and delivery speed; do it incrementally with features.

Naming the smell, naming the fix, and stressing "behaviour stays the same" is exactly the senior signal — in both remote and BD interviews.

[↑ Back to top](#toc)

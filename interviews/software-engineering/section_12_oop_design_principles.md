# Section 12 — OOP & Design Principles

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a detailed, step-by-step explanation with real-life examples and code.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For OOP and SOLID, give the definition in one line, then a tiny real-life example, then the code. The example is what makes the interviewer nod.

---

<a id="toc"></a>

## Table of Contents

**A. The four pillars of OOP**
1. [The four pillars — overview](#q1) · *Very common*
2. [Encapsulation](#q2) · *Very common*
3. [Inheritance — `extends`, `super`, `@override`](#q3) · *Very common*
4. [Polymorphism](#q4) · *Very common*
5. [Abstraction — abstract class vs interface](#q5) · *Very common*

**B. Class relationships & design**
6. [Composition over Inheritance](#q6) · *Very common*
7. [Mixins vs Abstract Classes vs Interfaces](#q7) · *Common*
8. [Class vs Object vs Instance](#q8) · *Common*
9. [Coupling & Cohesion](#q9) · *Very common*

**C. SOLID principles**
10. [S — Single Responsibility](#q10) · *Very common*
11. [O — Open/Closed](#q11) · *Very common*
12. [L — Liskov Substitution](#q12) · *Common*
13. [I — Interface Segregation](#q13) · *Common*
14. [D — Dependency Inversion](#q14) · *Very common*

**D. Other key principles**
15. [DRY — Don't Repeat Yourself](#q15) · *Common*
16. [KISS — Keep It Simple](#q16) · *Common*
17. [YAGNI — You Aren't Gonna Need It](#q17) · *Common*

**E. Dart OOP details**
18. [Constructor types](#q18) · *Common*
19. [`static` members](#q19) · *Common*
20. [Covariance & contravariance](#q20) · *Deeper*
21. [Method overriding vs method hiding](#q21) · *Deeper*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

Follow these stages in order. Tick a stage off only when you can give the **short answer** with a real-life example, without looking.

**Stage 1 — The four pillars (start here).** The base of all OOP questions.
→ [Q1 Overview](#q1) · [Q2 Encapsulation](#q2) · [Q3 Inheritance](#q3) · [Q4 Polymorphism](#q4) · [Q5 Abstraction](#q5)

**Stage 2 — How classes relate.**
→ [Q6 Composition over inheritance](#q6) · [Q9 Coupling & cohesion](#q9) · [Q7 Mixins vs abstract vs interface](#q7) · [Q8 Class vs object](#q8)

**Stage 3 — SOLID (the senior favourite).**
→ [Q10 SRP](#q10) · [Q11 OCP](#q11) · [Q14 DIP](#q14) · [Q12 LSP](#q12) · [Q13 ISP](#q13)

**Stage 4 — The short principles.**
→ [Q15 DRY](#q15) · [Q16 KISS](#q16) · [Q17 YAGNI](#q17)

**Stage 5 — Dart-specific details.**
→ [Q18 Constructors](#q18) · [Q19 static](#q19) · [Q20 Covariance](#q20) · [Q21 Overriding vs hiding](#q21)

**Short on time (1 hour before the interview)?** Review these eight:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q6](#q6) · [Q9](#q9) · [Q10](#q10) · [Q11](#q11) · [Q14](#q14), then read the [Cheat Sheet](#cheatsheet).

---

# A. The four pillars of OOP

---

<a id="q1"></a>
## 1. What are the four pillars of Object-Oriented Programming?

> Very common · Easy–Medium

**Short answer (say this):**
"The four pillars are Encapsulation, Abstraction, Inheritance, and Polymorphism. Encapsulation hides the inside details, abstraction shows only what matters and hides complexity, inheritance lets one class reuse another's code, and polymorphism lets one action behave differently for different types. Together they help model real things in clean, reusable code."

**Let's understand it fully:**

**Step 1 — A one-line picture of each.**

| Pillar | One line | Real-life example |
|---|---|---|
| **Encapsulation** | hide the internal state, expose a safe API | a TV remote hides the wiring; you press buttons |
| **Abstraction** | show only what matters, hide complexity | driving a car without knowing the engine |
| **Inheritance** | a child class reuses a parent's code | a child inherits traits from a parent |
| **Polymorphism** | one action, many forms | "draw()" works for circle, square, triangle |

**Step 2 — A tiny code example tying them together.**

```dart
// Abstraction: the shape only promises an area, hides the math
abstract class Shape {
  double area(); // what, not how
}

// Inheritance + Polymorphism: each shape implements area() its own way
class Circle extends Shape {
  final double r;
  Circle(this.r);
  @override
  double area() => 3.14 * r * r;
}

class Square extends Shape {
  final double side;
  Square(this.side);
  @override
  double area() => side * side;
}

// Polymorphism in action: same call, different behaviour
void printArea(Shape s) => print(s.area());
```

**Step 3 — Encapsulation in the same idea.**
If `Circle` kept `r` private and exposed only a getter, that is encapsulation — the field is protected from outside changes.

**Why interviewers ask:** It's the foundation of OOP. They want crisp definitions plus a real example for each — not just memorized words.

**Common mistake:** Listing the four words with no example, or confusing abstraction (hide complexity) with encapsulation (hide data). They overlap but are different angles.

**Follow-ups they may ask:**
- *"Abstraction vs encapsulation?"* → Abstraction is about *design* (show only what matters). Encapsulation is about *implementation* (protect the data). See [Q2](#q2) and [Q5](#q5).

**Related:** [Q2 — encapsulation](#q2) · [Q3 — inheritance](#q3) · [Q4 — polymorphism](#q4) · [Q5 — abstraction](#q5)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What is Encapsulation, how do you implement it in Dart, and why does it matter?

> Very common · Easy–Medium

**Short answer (say this):**
"Encapsulation means hiding an object's internal data and only letting the outside touch it through safe methods. In Dart, you make a field private with a leading underscore, then expose getters or methods to control access. It matters because it protects the object from being put into an invalid state."

**Let's understand it fully:**

**Step 1 — A real-life picture: a medicine capsule.**
A capsule wraps the medicine inside a safe shell. You don't touch the powder directly; you take the whole capsule. Encapsulation wraps data in a safe shell.

**Step 2 — In Dart, `_` makes things private (to the file/library).**

```dart
class BankAccount {
  double _balance = 0; // private — cannot be touched from outside the file

  double get balance => _balance; // read-only view

  void deposit(double amount) {
    if (amount <= 0) throw ArgumentError('must be positive'); // a safe gate
    _balance += amount;
  }
}
```

Outside code can `deposit` but cannot set `_balance = -999` directly. The class controls its own state.

**Step 3 — Why it matters: protect invariants.**
Without encapsulation, anyone could set the balance to a wrong value. With it, every change goes through a method that can validate. This prevents bugs and keeps the object always valid.

**Step 4 — Note on Dart's privacy.**
In Dart, `_` is private to the *library* (the file), not the class. Within the same file, other classes can see it. Across files, it's hidden.

**Why interviewers ask:** It's the most practical pillar. They want to see you protect state instead of exposing public fields everywhere.

**Common mistake:** Making all fields public and mutable, then "encapsulating" with getters/setters that do nothing. Real encapsulation adds validation or hides the field entirely.

**Follow-ups they may ask:**
- *"Getters and setters?"* → `get` exposes a read view; `set` lets you validate on write. Use them to control access, not just to wrap every field.
- *"Is `_` truly private?"* → It's private to the library (file), so same-file code can access it.

**Related:** [Q1 — four pillars](#q1) · [Q9 — low coupling](#q9)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. How does Inheritance work in Dart? Explain `extends`, `super`, and `@override`.

> Very common · Medium

**Short answer (say this):**
"Inheritance lets a class reuse another class's code with `extends`. The child gets the parent's fields and methods, can call the parent's version with `super`, and can replace a method with its own using `@override`. Dart allows only one parent (single inheritance)."

**Let's understand it fully:**

**Step 1 — A real-life picture: a child and a parent.**
A child inherits traits from a parent but can also have their own. The parent is the base; the child adds or changes things.

**Step 2 — `extends` reuses the parent's code.**

```dart
class Animal {
  void breathe() => print('breathing');
  void describe() => print('I am an animal');
}

class Dog extends Animal {
  void bark() => print('woof');     // new behaviour
}

Dog().breathe(); // inherited for free
```

**Step 3 — `@override` replaces a parent method.**

```dart
class Dog extends Animal {
  @override
  void describe() => print('I am a dog'); // replaces the parent version
}
```

`@override` is optional but strongly recommended — it tells the compiler "I mean to replace this," so a typo in the method name becomes an error instead of a silent new method.

**Step 4 — `super` calls the parent's version.**

```dart
class Dog extends Animal {
  @override
  void describe() {
    super.describe();          // run the parent's version first
    print('...specifically a dog');
  }
}
```

`super` is also used in constructors to pass values up to the parent.

**Step 5 — Dart allows only ONE parent.**
You can `extends` exactly one class. To reuse code from several sources, use mixins (`with`) or composition (see [Q6](#q6), [Q7](#q7)).

**Why interviewers ask:** Inheritance is everywhere in Flutter (every widget extends another). They check you know `super`, `@override`, and the single-parent rule.

**Common mistake:** Overusing inheritance to share code between unrelated classes. If it's not a true "is-a" relationship, prefer composition ([Q6](#q6)).

**Follow-ups they may ask:**
- *"Inheritance vs composition?"* → Inheritance = "is-a"; composition = "has-a". Prefer composition for flexibility ([Q6](#q6)).
- *"Why use `@override`?"* → It catches typos and makes intent clear.

**Related:** [Q6 — composition over inheritance](#q6) · [Q7 — mixins](#q7) · [Q4 — polymorphism](#q4)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. What is Polymorphism? Explain compile-time vs runtime, and how Dart handles overloading.

> Very common · Medium

**Short answer (say this):**
"Polymorphism means one action takes many forms — the same method call behaves differently depending on the object's real type. Runtime polymorphism is method overriding, decided when the program runs. Important Dart detail: Dart does NOT support method overloading (same name, different parameters), so we use optional or named parameters instead."

**Let's understand it fully:**

**Step 1 — A real-life picture: the word "run".**
"Run" means different things for a person, an app, and a river. One word, many behaviours — that is polymorphism.

**Step 2 — Runtime polymorphism = method overriding.**
You hold a parent type, but the real object decides which method runs.

```dart
abstract class Shape { double area(); }
class Circle extends Shape { final double r; Circle(this.r); double area() => 3.14 * r * r; }
class Square extends Shape { final double s; Square(this.s); double area() => s * s; }

void show(Shape shape) => print(shape.area()); // same call...
show(Circle(2)); // 12.56  ...different behaviour
show(Square(3)); // 9
```

The variable's type is `Shape`, but the actual object (Circle or Square) decides which `area()` runs. That decision happens at runtime.

**Step 3 — Dart has NO method overloading.**
In Java you can have two methods with the same name but different parameters. Dart does not allow this. Instead, use optional or named parameters:

```dart
// Not allowed in Dart:
// void greet() {}
// void greet(String name) {}

// Do this instead:
void greet([String? name]) {
  print(name == null ? 'Hi' : 'Hi $name');
}
```

**Step 4 — Compile-time polymorphism.**
In languages with overloading, picking which overloaded method to call is decided at compile time ("compile-time polymorphism"). Since Dart has no overloading, the main polymorphism you use is the runtime (overriding) kind. Dart's generics also give a form of compile-time polymorphism.

**Why interviewers ask:** Polymorphism is what makes code extensible. The "Dart has no overloading" point is a favourite gotcha.

**Common mistake:** Saying Dart supports overloading. It does not — use optional/named parameters.

**Follow-ups they may ask:**
- *"Real Flutter example?"* → `Widget build()` is overridden by every widget — same call, different UI.
- *"How to fake overloading?"* → Named/optional parameters, or factory constructors with different names.

**Related:** [Q3 — inheritance (overriding)](#q3) · [Q1 — four pillars](#q1) · [Q21 — overriding vs hiding](#q21)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What is Abstraction? What's the difference between an `abstract class` and an interface (`implements`) in Dart?

> Very common · Medium

**Short answer (say this):**
"Abstraction means showing only what something does and hiding how it does it. In Dart, an `abstract class` can have both unfinished methods and shared code, and you `extends` it. Any class can also be used as an interface with `implements`, where you take only the method signatures and must write all the code yourself. Dart has no separate `interface` keyword — every class is an interface."

**Let's understand it fully:**

**Step 1 — A real-life picture: driving a car.**
You use the steering wheel and pedals (the interface). You don't need to know how the engine burns fuel (the implementation). Abstraction hides the engine.

**Step 2 — `abstract class` = a partial blueprint (can have shared code).**

```dart
abstract class Payment {
  void pay(double amount);     // abstract: no body, must be filled in
  void logReceipt() => print('receipt saved'); // shared code, inherited
}

class CardPayment extends Payment {
  @override
  void pay(double amount) => print('paid \$amount by card');
}
```

You cannot create `Payment()` directly — it's abstract. You `extends` it and fill in the missing methods.

**Step 3 — `implements` = take only the contract, write everything yourself.**

```dart
class WalletPayment implements Payment {
  // implements gives NO code — you must write every method, even logReceipt()
  @override
  void pay(double amount) => print('paid by wallet');
  @override
  void logReceipt() => print('wallet receipt');
}
```

**Step 4 — The difference in one line.**
- `extends` (abstract class) → inherit code + contract. One parent only.
- `implements` (interface) → contract only, no code. Many at once.

**Step 5 — Dart has no `interface` keyword.**
Every class automatically defines an interface, so you can `implements` any class. Use an abstract class when you want to share some code; use a pure interface (`implements`) when you only want to force a contract — great for testing with fakes.

**Why interviewers ask:** It tests whether you can design to contracts, which is the heart of flexible, testable code.

**Common mistake:** Thinking Dart has a separate `interface` keyword (it doesn't), or that `implements` inherits code (it doesn't — you rewrite everything).

**Follow-ups they may ask:**
- *"When abstract class vs interface?"* → Abstract class when sharing code; interface (`implements`) when you only need the contract and want easy mocking.

**Related:** [Q7 — mixins vs abstract vs interface](#q7) · [Q1 — abstraction pillar](#q1) · [Q14 — DIP](#q14)

[↑ Back to top](#toc)

---

# B. Class relationships & design

---

<a id="q6"></a>
## 6. What is "Composition over Inheritance"? When and why should you prefer it?

> Very common · Medium

**Short answer (say this):**
"Composition means a class is built from other objects it *has*, instead of inheriting from a parent it *is*. The advice 'prefer composition over inheritance' means: rather than building deep class trees, give a class the pieces it needs as fields. It's more flexible — you can mix and change behaviours without a rigid hierarchy."

**Let's understand it fully:**

**Step 1 — "is-a" vs "has-a".**
- Inheritance = "is-a": a Dog **is an** Animal.
- Composition = "has-a": a Car **has an** Engine.

**Step 2 — The problem with deep inheritance.**
Imagine `Animal → Bird → FlyingBird`. Now you need a penguin (a bird that can't fly) and a bat (a mammal that flies). The tree breaks — "can fly" doesn't fit neatly into a single parent chain.

**Step 3 — Composition fixes it: give the class the behaviour as a piece.**

```dart
// Behaviours as small, swappable pieces
class FlyAbility { void fly() => print('flying'); }
class SwimAbility { void swim() => print('swimming'); }

// A Duck HAS the abilities it needs
class Duck {
  final _fly = FlyAbility();
  final _swim = SwimAbility();
  void move() { _fly.fly(); _swim.swim(); }
}
```

Now any class can pick exactly the abilities it needs — no rigid tree.

**Step 4 — Why it's more flexible.**
- You can change a behaviour at runtime (swap the piece).
- You avoid the "fragile base class" problem, where changing a parent breaks many children.
- It keeps classes small and focused.

**Step 5 — When inheritance is still right.**
Use inheritance for a true, stable "is-a" relationship (every Flutter widget extends `Widget`). Use composition when you're just reusing behaviour.

**Why interviewers ask:** It's a senior design instinct. Reaching for composition shows you avoid rigid, hard-to-change hierarchies.

**Common mistake:** Building tall inheritance trees to share code. If it's not a real "is-a," that's a red flag — compose instead.

**Follow-ups they may ask:**
- *"How does Flutter use composition?"* → Widgets are composed: you nest small widgets (Padding wraps Center wraps Text) instead of subclassing.
- *"Mixins?"* → Dart mixins are a middle ground — reusable behaviour without a parent ([Q7](#q7)).

**Related:** [Q3 — inheritance](#q3) · [Q7 — mixins](#q7) · [Q9 — coupling](#q9)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. What is the difference between Mixins, Abstract Classes, and Interfaces in Dart? When do you use each?

> Common · Medium

**Short answer (say this):**
"An abstract class is a partial blueprint you `extends` — it can share code, but you get only one parent. A mixin is reusable behaviour you add with `with` — you can add many, and it gives you working code without inheritance. An interface (any class used with `implements`) is a contract only — no code, but you can implement many."

**Let's understand it fully:**

**Step 1 — The three tools, side by side.**

| Tool | Keyword | Gives you code? | How many? |
|---|---|---|---|
| Abstract class | `extends` | yes (shared) | one parent |
| Mixin | `with` | yes (behaviour) | many |
| Interface | `implements` | no (contract only) | many |

**Step 2 — Abstract class — share code + force a contract.**

```dart
abstract class Repository {
  Future<void> save(String data);   // contract
  void log(String m) => print(m);   // shared code
}
```

**Step 3 — Mixin — add behaviour to many unrelated classes.**

```dart
mixin Logger {
  void log(String m) => print('[LOG] $m');
}

class ApiService with Logger {}   // now has log() for free
class CacheService with Logger {} // also has log()
```

A mixin can't have a constructor, because it's merged into the host class.

**Step 4 — Interface — only a contract (great for testing).**

```dart
class FakeRepository implements Repository {
  @override
  Future<void> save(String data) async {} // a fake for tests
  @override
  void log(String m) {}
}
```

**Step 5 — How to choose.**
- Need shared code + a true "is-a"? → abstract class.
- Need to reuse behaviour across unrelated classes? → mixin.
- Need only a contract (for swapping/mocking)? → interface (`implements`).

**Why interviewers ask:** It tests deep Dart OOP knowledge and good design judgment.

**Common mistake:** Using a mixin when an interface (contract) was meant, or thinking `implements` gives you code (it doesn't).

**Follow-ups they may ask:**
- *"Can a mixin require a base type?"* → Yes, with `on`: `mixin X on Animal` can only be used on Animals.

**Related:** [Q5 — abstract vs interface](#q5) · [Q6 — composition](#q6) · [Q3 — inheritance](#q3)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is the difference between a Class, an Object, and an Instance?

> Common · Easy

**Short answer (say this):**
"A class is the blueprint. An object is a real thing built from that blueprint. 'Instance' is just another word for an object — we say an object is 'an instance of' a class. So `class User` is the plan, and `User('Sara')` creates an instance."

**Let's understand it fully:**

**Step 1 — A real-life picture: blueprint and houses.**
- The **class** is the architect's blueprint for a house.
- An **object** is an actual house built from it.
- "Instance" means the same as object — each built house is "an instance of" the blueprint.

**Step 2 — In code.**

```dart
class User {              // the class (blueprint)
  final String name;
  User(this.name);
}

final a = User('Sara');   // an object / instance
final b = User('Rahim');  // another instance — same class, different data
```

One class, many instances. Each instance has its own data but shares the same structure and methods.

**Step 3 — "Instance of".**
`a is User` is true — `a` is an instance of `User`. The word "instance" just emphasizes "a specific one made from the class."

**Why interviewers ask:** A quick check that you have the basic vocabulary right — common in early/screening rounds.

**Common mistake:** Using "class" and "object" interchangeably. The class is the plan; the object is the built thing.

**Follow-ups they may ask:**
- *"What does `new` do?"* → It creates an instance. In modern Dart, `new` is optional and usually omitted.

**Related:** [Q1 — OOP basics](#q1) · [Q18 — constructors](#q18)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What are Coupling and Cohesion? Why do we want low coupling and high cohesion?

> Very common · Medium

**Short answer (say this):**
"Coupling is how much one part depends on another; cohesion is how focused a single part is on one job. We want low coupling (parts can change independently) and high cohesion (each class does one clear thing). Together they make code easy to change, test, and reuse."

**Let's understand it fully:**

**Step 1 — A real-life picture.**
- **Low coupling** = appliances plugged into wall sockets. You can swap the toaster without rewiring the house.
- **High cohesion** = a toolbox where everything inside belongs together (all tools), not a junk drawer.

**Step 2 — Coupling: how tangled are the parts?**
High (bad) coupling: a class reaches deep into another's internals, so changing one breaks the other.

```dart
// High coupling — OrderService builds its own database, hard to change/test
class OrderService {
  final db = MySqlDatabase(); // tightly tied to a specific database
}

// Low coupling — depend on an abstraction, pass it in
class OrderService {
  final Database db;
  OrderService(this.db); // any Database works; easy to swap or fake in tests
}
```

**Step 3 — Cohesion: does the class do ONE thing?**
Low (bad) cohesion: a `User` class that also sends emails, saves files, and formats dates. High cohesion: `User` holds user data; separate classes handle email, storage, and formatting.

**Step 4 — Why both matter.**
- Low coupling → you can change or replace a part without breaking others (and you can test it with a fake).
- High cohesion → each class is small, clear, and reusable.

These two ideas are the "why" behind most of SOLID (especially [SRP](#q10) and [DIP](#q14)).

**Why interviewers ask:** They're the core measures of good design. Senior engineers talk in these terms.

**Common mistake:** Building "god classes" that do everything (low cohesion) and hard-wiring dependencies with `new` inside (high coupling).

**Follow-ups they may ask:**
- *"How do you lower coupling?"* → Depend on abstractions and inject dependencies ([Q14](#q14)).
- *"Link to SOLID?"* → SRP raises cohesion; DIP lowers coupling.

**Related:** [Q10 — SRP](#q10) · [Q14 — DIP](#q14) · [Q6 — composition](#q6)

[↑ Back to top](#toc)

---

# C. SOLID principles

> SOLID is five rules for classes that are easy to change and test. Expect at least one — often all five.

---

<a id="q10"></a>
## 10. SOLID — S: Single Responsibility Principle (SRP)

> Very common · Medium

**Short answer (say this):**
"A class should have one reason to change — one job. If a class handles two different concerns, a change to one can break the other. So I split mixed responsibilities into focused classes."

**Let's understand it fully:**

**Step 1 — A real-life picture: one job per person.**
A restaurant has a chef, a waiter, and a cashier. You don't want one person doing all three — if the cashier rules change, you don't want the cooking to break.

**Step 2 — A violation: one class doing too much.**

```dart
// Bad: User does data AND saving AND email — three reasons to change
class User {
  String name;
  User(this.name);
  void saveToDatabase() {/* ... */}
  void sendWelcomeEmail() {/* ... */}
}
```

**Step 3 — The fix: split by responsibility.**

```dart
class User {
  final String name;
  User(this.name); // only holds user data
}

class UserRepository {
  void save(User user) {/* saving logic */}
}

class EmailService {
  void sendWelcome(User user) {/* email logic */}
}
```

Now each class has one reason to change.

**Step 4 — "One reason to change" is the real test.**
Don't read SRP as "one method." Read it as "one responsibility / one reason to change." A class can have many methods if they all serve the same job.

**Why interviewers ask:** SRP is the most-used SOLID rule and the basis of clean architecture layers.

**Common mistake:** Building a "god class" that holds data, talks to the network, and builds UI. Or over-splitting into dozens of tiny classes.

**Follow-ups they may ask:**
- *"How does SRP relate to cohesion?"* → SRP gives high cohesion — each class focuses on one thing ([Q9](#q9)).

**Related:** [Q9 — cohesion](#q9) · [Q11 — OCP](#q11)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. SOLID — O: Open/Closed Principle (OCP)

> Very common · Medium

**Short answer (say this):**
"Classes should be open for extension but closed for modification. That means you add new behaviour by adding new code, not by editing existing, tested code. The usual way is to depend on an abstraction and add new implementations."

**Let's understand it fully:**

**Step 1 — A real-life picture: a power strip.**
To add a new device, you plug it into a new socket — you don't rewire the wall. New behaviour is added, old wiring is untouched.

**Step 2 — A violation: editing a class for every new case.**

```dart
// Bad: every new shape forces editing this method
double area(Object shape) {
  if (shape is Circle) return 3.14 * shape.r * shape.r;
  if (shape is Square) return shape.s * shape.s;
  // add Triangle? must EDIT this function again
  return 0;
}
```

**Step 3 — The fix: extend via an abstraction.**

```dart
abstract class Shape { double area(); }
class Circle extends Shape { final double r; Circle(this.r); double area() => 3.14 * r * r; }
class Square extends Shape { final double s; Square(this.s); double area() => s * s; }

// To add a Triangle, ADD a new class — no existing code changes.
class Triangle extends Shape { final double b, h; Triangle(this.b, this.h); double area() => 0.5 * b * h; }

double totalArea(List<Shape> shapes) =>
    shapes.fold(0, (sum, s) => sum + s.area()); // never needs editing
```

**Step 4 — Why it matters.**
Editing tested code risks breaking it. Adding new code (a new class) leaves the old, working code alone — safer and easier to extend.

**Why interviewers ask:** It shows you design for change, the most valuable trait in long-lived code.

**Common mistake:** Big `if/else` or `switch` chains on a type that grow every time a new case appears — a classic OCP violation.

**Follow-ups they may ask:**
- *"Isn't a sealed class + switch a violation?"* → It's a balanced trade-off: sealed classes give compile-time safety (you can't forget a case), at the cost of editing the switch. Both styles are valid; pick by how often the set changes.

**Related:** [Q10 — SRP](#q10) · [Q14 — DIP](#q14) · [Q5 — abstraction](#q5)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. SOLID — L: Liskov Substitution Principle (LSP)

> Common · Medium–Hard

**Short answer (say this):**
"Any subclass should work wherever its parent is expected, without breaking things. If you replace a parent with a child and the program misbehaves, you've broken LSP. It usually means the inheritance was wrong."

**Let's understand it fully:**

**Step 1 — A real-life picture: a stand-in actor.**
A stand-in must be able to play the role wherever the main actor would. If the stand-in can't do the basic role, the substitution breaks the show.

**Step 2 — The classic violation: Square extends Rectangle.**
A square "is a" rectangle in math, but in code it breaks expectations:

```dart
class Rectangle {
  int width, height;
  Rectangle(this.width, this.height);
  int area() => width * height;
}

class Square extends Rectangle {
  Square(int size) : super(size, size);
  // If someone sets width and height separately (valid for a Rectangle),
  // a Square breaks that expectation — width and height must stay equal.
}

void resizeAndCheck(Rectangle r) {
  r.width = 4;
  r.height = 5;
  assert(r.area() == 20); // FAILS if r is actually a Square
}
```

The code that works for `Rectangle` breaks when given a `Square` — that violates LSP.

**Step 3 — The fix: don't force a bad "is-a".**
Don't make `Square extends Rectangle`. Use a common abstraction (`Shape`) instead, or use composition. The lesson: inheritance must preserve the parent's promises.

**Step 4 — Another common sign.**
A subclass that throws "not supported" for a parent method (e.g. a read-only list that throws on `add`) is also breaking LSP — it can't truly stand in for the parent.

**Why interviewers ask:** It tests whether you understand that inheritance is a *promise*, not just code reuse.

**Common mistake:** Inheriting just to reuse fields, then overriding methods to do nothing or throw. That breaks substitution.

**Follow-ups they may ask:**
- *"How to fix the Square/Rectangle case?"* → Use a `Shape` interface with `area()`, and make Square and Rectangle separate implementations.

**Related:** [Q3 — inheritance](#q3) · [Q11 — OCP](#q11) · [Q6 — composition](#q6)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. SOLID — I: Interface Segregation Principle (ISP)

> Common · Medium

**Short answer (say this):**
"Don't force a class to implement methods it doesn't need. Prefer several small, focused interfaces over one big fat interface. That way a class only depends on the methods it actually uses."

**Let's understand it fully:**

**Step 1 — A real-life picture: a simple menu.**
A small café menu is easier than a 200-item menu where most things aren't available. Small, focused interfaces are like small menus — you only take what you need.

**Step 2 — A violation: one fat interface.**

```dart
// Bad: every worker must implement ALL of these, even if irrelevant
abstract class Worker {
  void work();
  void eat();
  void sleep();
}

class Robot implements Worker {
  @override void work() {}
  @override void eat() {}   // a robot doesn't eat — forced to fake it
  @override void sleep() {} // a robot doesn't sleep — forced to fake it
}
```

**Step 3 — The fix: split into small interfaces.**

```dart
abstract class Workable { void work(); }
abstract class Eatable  { void eat(); }

class Robot implements Workable {           // only what it needs
  @override void work() {}
}
class Human implements Workable, Eatable {  // takes both
  @override void work() {}
  @override void eat() {}
}
```

**Step 4 — Why it matters.**
Fat interfaces force empty or fake methods, and they couple classes to things they don't use — so a change to an unused method can still ripple out. Small interfaces keep dependencies tight.

**Why interviewers ask:** It shows you design lean contracts, which keeps code decoupled and easy to mock.

**Common mistake:** One giant "service" interface with 20 methods that everything implements partially.

**Follow-ups they may ask:**
- *"How is this related to SRP?"* → ISP is SRP applied to interfaces — each interface has one focused purpose.

**Related:** [Q10 — SRP](#q10) · [Q5 — interfaces](#q5)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. SOLID — D: Dependency Inversion Principle (DIP)

> Very common · Medium–Hard

**Short answer (say this):**
"High-level code should depend on abstractions, not on concrete details. Instead of a class creating its own database or API client inside, it should receive an interface from outside. This makes code flexible and testable — you can swap real for fake without changing the class."

**Let's understand it fully:**

**Step 1 — A real-life picture: a wall socket.**
Your lamp doesn't wire directly into the power station. It plugs into a standard socket (an interface). You can move the lamp to any socket. DIP is "depend on the socket, not the power station."

**Step 2 — A violation: depend on a concrete detail.**

```dart
// Bad: high-level OrderService is glued to a specific API class
class OrderService {
  final api = HttpApiClient(); // hard-wired — can't swap or fake
  void placeOrder() => api.post('/order');
}
```

**Step 3 — The fix: depend on an abstraction, inject it.**

```dart
abstract class ApiClient {       // the abstraction (the "socket")
  void post(String path);
}

class OrderService {
  final ApiClient api;           // depends on the interface, not a class
  OrderService(this.api);        // injected from outside
  void placeOrder() => api.post('/order');
}

// Real app:
OrderService(HttpApiClient());
// Test:
OrderService(FakeApiClient());   // easy to test, no real network
```

**Step 4 — Why "inversion"?**
Normally high-level code would directly create low-level details. DIP *inverts* that: both depend on an abstraction in the middle. This is exactly what dependency injection tools like `get_it` and `injectable` do in Flutter.

**Why interviewers ask:** DIP is the backbone of testable, layered architecture — a strong senior signal.

**Common mistake:** Creating dependencies with `new`/constructors inside a class (hard-wired). Inject them instead.

**Follow-ups they may ask:**
- *"DIP vs dependency injection?"* → DIP is the principle (depend on abstractions). DI is the technique (passing them in, often via `get_it`).
- *"How does this help testing?"* → You inject a fake implementation, so tests run without a real network or database.

**Related:** [Q9 — low coupling](#q9) · [Q11 — OCP](#q11) · [Q5 — abstraction](#q5)

[↑ Back to top](#toc)

---

# D. Other key principles

---

<a id="q15"></a>
## 15. What is the DRY principle?

> Common · Easy

**Short answer (say this):**
"DRY means Don't Repeat Yourself — every piece of knowledge should live in one place. If you copy-paste the same logic in several spots, a change means fixing it everywhere and forgetting one. So I pull repeated logic into one function or class."

**Let's understand it fully:**

**Step 1 — A violation: copy-pasted logic.**

```dart
// Bad: the same discount math repeated
double priceA(double p) => p - (p * 0.1);
double priceB(double p) => p - (p * 0.1); // change the rate? fix it twice
```

**Step 2 — The fix: one source of truth.**

```dart
double applyDiscount(double price, double rate) => price - (price * rate);
// Change the rule once, everywhere updates.
```

**Step 3 — The caution: DRY is about knowledge, not just text.**
Don't merge two pieces of code just because they *look* the same right now. If they represent different rules that happen to match today, forcing them together creates a worse coupling. DRY is about removing duplicate *knowledge*, not duplicate-looking lines.

**Why interviewers ask:** It's a basic quality habit. They want to see you remove repetition the right way.

**Common mistake:** Over-applying DRY — merging unrelated code that just looks similar, creating a tangled shared function.

**Follow-ups they may ask:**
- *"DRY vs WET?"* → WET = "Write Everything Twice" (the opposite). A little duplication is sometimes fine; premature merging can hurt.

**Related:** [Q16 — KISS](#q16) · [Q10 — SRP](#q10)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. What is the KISS principle?

> Common · Easy

**Short answer (say this):**
"KISS means Keep It Simple, Stupid — prefer the simplest solution that works. Clever, complex code is harder to read, test, and change. I reach for the plain, clear version unless there's a real reason to add complexity."

**Let's understand it fully:**

**Step 1 — A violation: clever but unreadable.**

```dart
// Bad: too clever to read at a glance
bool isEven(int n) => (n & 1) == 0 ? true : false;
```

**Step 2 — The fix: plain and clear.**

```dart
bool isEven(int n) => n % 2 == 0;
```

Both work, but the second is instantly readable. Simple code is a feature.

**Step 3 — Where KISS matters most.**
- Don't add layers, patterns, or abstractions you don't need yet.
- Prefer a clear `if` over a clever one-liner nobody can read.
- A junior should be able to understand your code.

**Why interviewers ask:** Senior engineers value clarity over cleverness. KISS shows maturity.

**Common mistake:** Over-engineering — adding design patterns and indirection "just in case," making simple things complicated.

**Follow-ups they may ask:**
- *"KISS vs YAGNI?"* → KISS = keep the solution simple. YAGNI = don't build things you don't need yet ([Q17](#q17)). They work together.

**Related:** [Q17 — YAGNI](#q17) · [Q15 — DRY](#q15)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. What is the YAGNI principle?

> Common · Easy

**Short answer (say this):**
"YAGNI means You Aren't Gonna Need It — don't build features or flexibility until you actually need them. Code written for an imagined future need is often wrong, unused, and just extra weight to maintain. Build for today's real requirement."

**Let's understand it fully:**

**Step 1 — A real-life picture.**
Don't buy a 10-seater van because you *might* have a big family one day. Buy what you need now; upgrade when the need is real.

**Step 2 — A Flutter example.**

```dart
// Bad (YAGNI violation): building support for 5 payment providers
// when the app only needs one today, "just in case".

// Good: build the one you need now, behind a simple interface
abstract class PaymentGateway { Future<void> pay(double amount); }
class BkashGateway implements PaymentGateway {
  @override
  Future<void> pay(double amount) async {/* only what we need today */}
}
// Add more gateways later, when there's a real requirement.
```

**Step 3 — Why it matters.**
Speculative features cost time to build, test, and maintain — and they're usually wrong because you guessed the future. YAGNI keeps the codebase lean and focused.

**Step 4 — The balance.**
YAGNI doesn't mean "write careless code." It means don't add *unneeded* flexibility. You still design clean, simple code (KISS) that's easy to extend *when* the need appears (OCP).

**Why interviewers ask:** It shows you focus on real requirements and avoid over-engineering — valuable in fast-moving teams.

**Common mistake:** Building elaborate "configurable" systems for needs that never come, slowing delivery.

**Follow-ups they may ask:**
- *"YAGNI vs designing for change?"* → Keep code clean and extensible (OCP), but don't pre-build specific features no one asked for yet.

**Related:** [Q16 — KISS](#q16) · [Q11 — OCP](#q11)

[↑ Back to top](#toc)

---

# E. Dart OOP details

---

<a id="q18"></a>
## 18. What are the different constructor types in Dart?

> Common · Medium

**Short answer (say this):**
"Dart has default (generative) constructors that always make a new object, named constructors for a clearly-labeled second way to build, factory constructors that can return a cached object or a subtype, and const constructors that build the object at compile time. The part after the colon, the initializer list, sets final fields before the body runs."

**Let's understand it fully:**

**Step 1 — Default and named constructors.**

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name);                 // default (generative)
  User.guest() : id = '0', name = 'Guest';  // named
}
```

**Step 2 — Factory constructor — doesn't have to make a new object.**
It can return a cached instance, a subtype, or the result of parsing.

```dart
class User {
  final String id, name;
  User(this.id, this.name);
  factory User.fromJson(Map<String, dynamic> j) => User(j['id'], j['name']);
}
```

**Step 3 — const constructor — built at compile time.**
All fields must be `final`; equal const objects are shared in memory (good for Flutter widget performance).

```dart
class Point {
  final int x, y;
  const Point(this.x, this.y);
}
const a = Point(1, 2); // can be a compile-time constant
```

**Step 4 — The initializer list.**
The code after `:` runs before the body and is the only place to set `final` fields and call `super`.

```dart
class Circle {
  final double radius;
  Circle(double d) : radius = d / 2; // initializer list
}
```

**Why interviewers ask:** Constructors are used constantly (every `fromJson`). They check you know factory's special powers and const's performance benefit.

**Common mistake:** Thinking a factory always makes a new object — it doesn't have to.

**Follow-ups they may ask:**
- *"Why is `fromJson` a factory?"* → Because it can fail, return a cached object, or return a subtype — a normal constructor can't.

**Related:** [Q8 — class vs object](#q8) · [Q2 — encapsulation](#q2)

[↑ Back to top](#toc)

---

<a id="q19"></a>
## 19. When and why should you use `static` members in Dart?

> Common · Easy–Medium

**Short answer (say this):**
"A `static` member belongs to the class itself, not to any one object. You use it for shared constants, utility/helper functions that don't need instance data, and factory-style helpers. You call it on the class name, not an instance."

**Let's understand it fully:**

**Step 1 — Static = shared by the whole class.**
A normal field belongs to each object. A `static` field belongs to the class — there's only one copy, shared by everyone.

```dart
class AppConfig {
  static const String baseUrl = 'https://api.example.com'; // one shared value
  static int requestCount = 0;                              // one shared counter
}

print(AppConfig.baseUrl);   // called on the class, not an instance
AppConfig.requestCount++;    // shared across the whole app
```

**Step 2 — Static methods — utilities that need no object.**

```dart
class MathUtils {
  static int square(int n) => n * n; // doesn't need any instance data
}
print(MathUtils.square(5)); // 25
```

**Step 3 — When to use it.**
- App-wide **constants** (`static const`).
- **Helper/utility** functions that don't touch instance fields.
- **Counters or caches** shared across all instances.

**Step 4 — When NOT to use it.**
Static makes code harder to test and mock (you can't easily swap a static call for a fake). For real dependencies (database, API), prefer instances injected via DIP ([Q14](#q14)), not statics.

**Why interviewers ask:** They check you know the difference between class-level and instance-level, and that you don't overuse static (which hurts testability).

**Common mistake:** Putting business logic and dependencies in static methods, making the code impossible to mock in tests.

**Follow-ups they may ask:**
- *"static vs singleton?"* → A static class is shared but can't implement interfaces or be injected. A singleton is one object that can. Prefer a singleton for services you might mock.

**Related:** [Q14 — DIP (avoid hard statics)](#q14) · [Q18 — constructors](#q18)

[↑ Back to top](#toc)

---

<a id="q20"></a>
## 20. What is covariance and contravariance in Dart?

> Deeper · Hard

**Short answer (say this):**
"Covariance means a more specific type can be used where a general one is expected — for example, a `List<Cat>` can be treated as a `List<Animal>`. Dart's generics are covariant by default, which is convenient but slightly unsafe, so Dart adds runtime checks. The `covariant` keyword lets you intentionally narrow a parameter type in an override."

**Let's understand it fully:**

**Step 1 — A real-life picture.**
If a recipe asks for "fruit," giving "apples" (more specific) is fine — that's covariance (specific stands in for general). The reverse (giving "food" where "apples" is required) is contravariance and is usually not safe.

**Step 2 — Dart generics are covariant.**

```dart
class Animal {}
class Cat extends Animal {}

List<Cat> cats = [Cat()];
List<Animal> animals = cats; // allowed — covariant
```

This is handy, but technically unsafe (you could try to add a `Dog` to `animals`, which is really a list of `Cat`). Dart inserts a runtime check to catch that, so it stays safe at the cost of a possible runtime error.

**Step 3 — The `covariant` keyword (narrowing a parameter).**
Normally an override must accept the same or a wider parameter type. `covariant` lets you accept a narrower one, accepting a runtime check.

```dart
class Animal {}
class Cat extends Animal {}

class Vet {
  void treat(Animal a) {}
}
class CatVet extends Vet {
  @override
  void treat(covariant Cat a) {} // narrowed to Cat — Dart adds a runtime check
}
```

**Step 4 — When you actually meet this.**
Most developers rarely write `covariant` by hand. It shows up in advanced generic APIs and some framework code. Knowing the concept (specific-for-general) is enough for most interviews.

**Why interviewers ask:** It's a "do you know the deep corners of the type system?" question, used to separate strong seniors.

**Common mistake:** Confusing the direction — covariance is specific-for-general (Cat where Animal is wanted); contravariance is the reverse.

**Follow-ups they may ask:**
- *"Is Dart's covariance safe?"* → Mostly; Dart adds runtime checks to catch the unsafe cases that slip past compile time.

**Related:** [Q4 — polymorphism](#q4) · [Q3 — inheritance](#q3)

[↑ Back to top](#toc)

---

<a id="q21"></a>
## 21. What is the difference between method overriding and method hiding in Dart?

> Deeper · Medium–Hard

**Short answer (say this):**
"Overriding replaces an instance method in a subclass, and the object's real type decides which version runs at runtime — that's true polymorphism. Method 'hiding' happens with static methods: they belong to the class, not the object, so a subclass's static method just shadows the parent's by name — there's no runtime dispatch."

**Let's understand it fully:**

**Step 1 — Overriding (instance methods) — runtime decides.**

```dart
class Animal {
  void speak() => print('some sound');
}
class Dog extends Animal {
  @override
  void speak() => print('woof'); // overrides
}

Animal a = Dog();
a.speak(); // 'woof' — the REAL type (Dog) decides at runtime
```

This is polymorphism: even though the variable is typed `Animal`, the `Dog` version runs.

**Step 2 — Hiding (static methods) — type decides, no polymorphism.**
Static methods belong to the class. If both parent and child define a static method with the same name, the one used depends on which class name you write — there's no runtime dispatch.

```dart
class Parent {
  static void hello() => print('parent');
}
class Child extends Parent {
  static void hello() => print('child'); // hides, doesn't override
}

Parent.hello(); // 'parent'
Child.hello();  // 'child' — chosen by the class name, not an object
```

**Step 3 — The key difference.**
- **Override** → instance methods, decided by the object's real type at runtime (polymorphism).
- **Hide** → static methods (and field shadowing), decided by the declared class/type, not the object.

**Step 4 — Field shadowing is similar.**
If a subclass declares a field with the same name as the parent's, it shadows it — accessed by the declared type, not polymorphic like methods.

**Why interviewers ask:** It tests whether you truly understand that polymorphism applies to instance methods, not statics.

**Common mistake:** Expecting static methods to be polymorphic (overridable). They are not — they're resolved by the class name.

**Follow-ups they may ask:**
- *"Can you override a static method?"* → No. Static methods are hidden/shadowed, not overridden.

**Related:** [Q4 — polymorphism](#q4) · [Q19 — static members](#q19) · [Q3 — overriding](#q3)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## The four pillars

| Pillar | Meaning | Remember |
|---|---|---|
| Encapsulation | hide data, expose safe API | medicine capsule |
| Abstraction | show what, hide how | driving without the engine |
| Inheritance | reuse parent's code | child and parent |
| Polymorphism | one action, many forms | "draw()" for any shape |

## SOLID in one line each

| Letter | Principle | One line |
|---|---|---|
| S | Single Responsibility | one class, one reason to change |
| O | Open/Closed | add new code, don't edit old code |
| L | Liskov Substitution | a child must work wherever the parent does |
| I | Interface Segregation | many small interfaces, not one fat one |
| D | Dependency Inversion | depend on abstractions, inject them |

## Composition vs inheritance

| | Inheritance | Composition |
|---|---|---|
| Relationship | "is-a" | "has-a" |
| Flexibility | rigid tree | swappable pieces |
| Prefer when | true, stable is-a | reusing behaviour |

## One-line reminders

- **Encapsulation** = private fields (`_`) + safe methods that validate. ([Q2](#q2))
- **Inheritance** = `extends` (one parent), `@override` to replace, `super` to call up. ([Q3](#q3))
- **Polymorphism** = same call, different behaviour; Dart has NO method overloading. ([Q4](#q4))
- **Abstraction**: `abstract class` (shares code, `extends`) vs interface (`implements`, contract only). ([Q5](#q5))
- **Prefer composition over inheritance** — "has-a" is more flexible than deep "is-a" trees. ([Q6](#q6))
- **Low coupling + high cohesion** = easy to change, test, reuse. ([Q9](#q9))
- **SRP** = one reason to change; **OCP** = open to extend, closed to modify. ([Q10](#q10), [Q11](#q11))
- **LSP** = subclass must stand in for the parent; **ISP** = small interfaces. ([Q12](#q12), [Q13](#q13))
- **DIP** = depend on abstractions, inject them (the base of testable code). ([Q14](#q14))
- **DRY** (one source of truth), **KISS** (keep it simple), **YAGNI** (don't build what you don't need yet). ([Q15](#q15), [Q16](#q16), [Q17](#q17))
- **Factory** constructor can return a cached object/subtype; **static** belongs to the class. ([Q18](#q18), [Q19](#q19))
- **Override** = instance method, runtime dispatch; **hiding** = static, by class name. ([Q21](#q21))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers chain OOP questions from concept to design. Practice out loud:

1. *"What is SRP?"* → one class, one reason to change.
2. *"Show a violation."* → a `User` class that also saves to DB and sends email.
3. *"Fix it."* → split into `User`, `UserRepository`, `EmailService`.
4. *"Now the repository uses a real database — how do you test it?"* → depend on a `Database` abstraction and inject a fake (that's DIP).
5. *"Why is that better?"* → low coupling: you can swap or mock the database without touching `UserRepository`.

Moving smoothly from a principle → a violation → a fix → testing is exactly the senior signal interviewers look for, in both remote and BD interviews.

[↑ Back to top](#toc)

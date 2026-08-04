# Section 1 — Dart Language

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

> **Interview tip:** Always give the **short answer first** (2–3 sentences), then stop. Let the interviewer ask "can you go deeper?" Speaking simply and clearly is itself a senior skill — and it works the same for both remote and BD companies.

---

<a id="toc"></a>

## Table of Contents

**A. Variables, null safety & types**
1. [Null safety — `?`, `!`, `late`, `required`](#q1) · *Very common*
2. [`var`, `dynamic`, `Object`, `final`, `const`](#q2) · *Very common*
3. [`const` constructor & Flutter performance](#q3) · *Common*
4. [Equality — `==`, `hashCode`, `identical`](#q4) · *Very common*
5. [Generics & bounded generics](#q5) · *Common*
6. [Exception vs Error](#q6) · *Common*

**B. Functions & closures**
7. [Named / positional / optional parameters](#q7) · *Very common*
8. [Closures](#q8) · *Common*
9. [Cascade `..` vs method chaining](#q9) · *Common*
10. [`typedef`, spread `...`, collection if/for](#q10) · *Common*

**C. Classes & object-oriented Dart**
11. [Constructors — normal / named / factory / const / redirecting](#q11) · *Very common*
12. [`extends` vs `implements` vs `with` vs `on`](#q12) · *Very common*
13. [Mixins in depth](#q13) · *Common*
14. [Extension methods](#q14) · *Common*
15. [Enhanced enums](#q15) · *Common*

**D. Dart 3 new features**
16. [Records](#q16) · *Very common*
17. [Patterns & switch expressions](#q17) · *Very common*
18. [Sealed classes & class modifiers](#q18) · *Common*

**E. Async & concurrency**
19. [Future & async/await](#q19) · *Very common*
20. [Event loop — microtask vs event queue](#q20) · *Deeper*
21. [Streams — single vs broadcast](#q21) · *Very common*
22. [Generators — `sync*` / `async*`](#q22) · *Common*
23. [Isolates & `compute()`](#q23) · *Very common*

**F. How Dart runs (compile & memory)**
24. [JIT vs AOT](#q24) · *Common*
25. [Dart VM](#q25) · *Deeper*
26. [Garbage collection](#q26) · *Deeper*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 26 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — Core fundamentals (start here).** These come up in almost every interview.
→ [Q1 Null safety](#q1) · [Q2 var/final/const](#q2) · [Q7 Parameters](#q7) · [Q19 Future & async](#q19) · [Q21 Streams](#q21)

**Stage 2 — Object-oriented Dart.** How you design classes.
→ [Q11 Constructors](#q11) · [Q12 extends/implements/with/on](#q12) · [Q4 Equality](#q4) · [Q13 Mixins](#q13) · [Q14 Extensions](#q14)

**Stage 3 — Modern Dart 3 (shows you are up to date).**
→ [Q16 Records](#q16) · [Q17 Patterns](#q17) · [Q18 Sealed classes](#q18) · [Q15 Enhanced enums](#q15)

**Stage 4 — Depth & senior signal.**
→ [Q3 const & performance](#q3) · [Q5 Generics](#q5) · [Q6 Exceptions](#q6) · [Q9 Cascade](#q9) · [Q10 typedef/spread](#q10) · [Q22 Generators](#q22) · [Q23 Isolates](#q23)

**Stage 5 — Deep-dive tie-breakers (do last).** These separate strong seniors from the rest.
→ [Q20 Event loop](#q20) · [Q24 JIT vs AOT](#q24) · [Q25 Dart VM](#q25) · [Q26 Garbage collection](#q26)

**Short on time (1 hour before the interview)?** Just review these eight:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q12](#q12) · [Q19](#q19) · [Q20](#q20) · [Q21](#q21) · [Q23](#q23), then read the [Cheat Sheet](#cheatsheet).

---

# A. Variables, null safety & types

---

<a id="q1"></a>
## 1. What is null safety in Dart? Explain `?`, `!`, `late`, and `required`.

> Very common · Easy–Medium

**Short answer (say this):**
"Null safety means a variable cannot hold `null` unless I clearly allow it. Before null safety, any object could secretly be null, and using a null object crashed the app. Now Dart catches this mistake while I am writing code, before the app ever runs — so a whole category of crashes disappears."

**Let's understand it fully:**

**Step 1 — The problem null safety solves.**
Before null safety, this code looked fine but crashed for real users:

```dart
String name = null;   // old Dart allowed this
print(name.length);   // crash at runtime: "name is null"
```

The bug was found only after the app shipped — the worst time. Null safety moves the error to coding time, where it is cheap to fix:

```dart
String name = null;   // red error in your editor right away
```

This is the whole point: catch null mistakes early, not in front of users.

**Step 2 — `?` means "this is allowed to be null."**
A normal type can never be null. Add `?` to opt in:

```dart
String  city = 'Dhaka';   // can NEVER be null
String? nickname;          // CAN be null (starts as null)

print(nickname?.length);   // ?. means: only call .length if not null, else give null
```

The `?.` operator is the safe way to use a maybe-null value. If `nickname` is null, the whole thing becomes null instead of crashing.

**Step 3 — `!` means "I promise this is NOT null right now."**
It is a promise to the compiler. If your promise is wrong, the app crashes on that exact line:

```dart
String? email = getEmail();
print(email!.length);   // if email is null, it crashes right here
```

So `!` is risky. It turns off Dart's protection. Use it only when you are 100% sure.

**Step 4 — `late` means "I'll set this soon, before anyone reads it."**
Use it when you can't set the value immediately, but it's never truly null:

```dart
class ProfilePage {
  late String userId;            // not set yet, but not null either

  void init(String id) {
    userId = id;                 // set it later
  }
}
// Reading userId before init() runs gives a LateInitializationError
```

`late` is also great for lazy loading — the value is created only when first used:

```dart
late final result = doExpensiveWork(); // runs only when 'result' is first read
```

**Step 5 — `required` means "you must pass this value."**
This is used a lot in Flutter widgets:

```dart
class LoginRequest {
  final String username;
  LoginRequest({required this.username}); // you cannot forget username
}

LoginRequest();                  // error: username is required
LoginRequest(username: 'srana'); // correct
```

**Step 6 — The smart part: Dart "promotes" after a check.**
Once you check a value is not null, Dart is smart enough to treat it as not-null below that line — so you don't need `!`:

```dart
String greet(String? name) {
  if (name == null) return 'Hi guest';
  return 'Hi $name';   // Dart already knows name is NOT null here
}
```

**Bonus — the helper operators you should know:**

```dart
final shown = nickname ?? 'Guest';   // ?? = use 'Guest' if nickname is null
nickname ??= 'Guest';                // ??= = set it to 'Guest' only if it's null now
```

**Why interviewers ask:** They want to see you treat null safety as a guarantee from the compiler, not just as red errors to silence. Using `if`-checks and `??` instead of `!` shows maturity.

**Common mistake:** Putting `!` everywhere to make red errors go away. That only moves the crash from your screen (safe) to the user's phone (bad). Every `!` is a place where you turned off Dart's help.

**Follow-ups they may ask:**
- *"`late` vs `final`?"* → `late` = set later. `final` = set only once. `late final` = set later and only once.
- *"What is `??`?"* → "use this default if null." Example: `final name = nickname ?? 'Guest';`
- *"What does 'sound' null safety mean?"* → "Sound" means the guarantee is 100% reliable — if a type is not nullable, Dart truly makes sure it is never null.

**Related:** [Q2 — var/dynamic/final/const](#q2)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What is the difference between `var`, `dynamic`, `Object`, `final`, and `const`?

> Very common · Medium

**Short answer (say this):**
"These solve three different problems. `var` lets Dart guess the type. `dynamic` turns off type checking (risky). `Object` is the safe parent of all types. `final` means a value can be set only once. `const` means the value is fixed and known before the app even runs."

**Let's understand it fully:**

These five words feel similar but answer three different questions:
1. *What type is it?* → `var`, `dynamic`, `Object`
2. *Can it change?* → `final`, `const`

**Step 1 — `var`: let Dart guess the type.**
You don't write the type; Dart figures it out from the value. After that, the type is fixed.

```dart
var count = 10;     // Dart sees 10, so count is an int, forever
// count = 'hello'; // error: count is locked as int
```

**Step 2 — `dynamic`: turn off type checking (be careful).**
`dynamic` says "I don't care about the type." You can call any method. If that method doesn't exist, it crashes while running, not while coding.

```dart
dynamic value = 'hello';
value = 42;                 // allowed
value.somethingFake();      // compiles fine, but crashes when run
```

Use `dynamic` almost never. The main real reason is reading messy JSON where the type is truly unknown.

**Step 3 — `Object`: the safe parent of everything.**
Every type is an `Object`. But unlike `dynamic`, it is safe — you can only call methods that all objects have (like `toString()`), until you check the real type.

```dart
Object thing = 'hello';
// print(thing.length);     // error: Object has no 'length'
if (thing is String) {
  print(thing.length);      // now Dart knows it's a String
}
```

Quick comparison: `dynamic` = "trust me, don't check" (dangerous). `Object` = "check before you use" (safe).

**Step 4 — `final`: set only once.**
A `final` variable is assigned one time. The value can be decided while the app runs (like the current time). Important: `final` locks the variable, but you can still change inside a final list.

```dart
final now = DateTime.now();  // value decided at runtime, fine
// now = DateTime.now();      // error: already set once

final items = [1, 2, 3];
items.add(4);                // OK! final locks the box, not the contents
```

**Step 5 — `const`: fixed and known before running.**
A `const` value must be known at compile time (before the app runs). It is fully frozen, and Dart reuses the same one in memory.

```dart
const pi = 3.14;             // a fixed number, fine
const list = [1, 2, 3];
// list.add(4);              // error: const is fully frozen

// const bad = DateTime.now(); // error: now() is only known while running
```

Easy way to remember:
- **`final`** = *lock the box* (you can set it once, even at runtime).
- **`const`** = *freeze everything from the factory* (must be known before running).

**Why interviewers ask:** Many people wrongly say "final means constant." They want to hear the real difference: `final` = set once; `const` = known before running.

**Common mistake:** Thinking a `final List` is fully unchangeable. It is not — you can still add or remove items. Only `const` makes the contents frozen.

**Follow-ups they may ask:**
- *"When would you use `dynamic`?"* → Almost never. Maybe only for unknown JSON. Prefer `Object` or a real type.
- *"Can `final` and `const` be combined?"* → Yes — `static const` for class-level constants. A single variable is either `final` or `const`, not both.

**Related:** [Q1 — null safety](#q1) · [Q3 — const constructor](#q3)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. What is a `const` constructor, and why does it help Flutter performance?

> Common · Medium

**Short answer (say this):**
"A `const` constructor lets Dart build the whole object before the app runs. Dart then reuses the same object in memory instead of making new copies. In Flutter, `const` widgets are built once and skipped during rebuilds, so the screen updates faster."

**Let's understand it fully:**

**Step 1 — What a const constructor is.**
A normal constructor builds a new object every time you call it. A `const` constructor lets Dart build the object at compile time (before running) — but only if all its fields are `final`.

```dart
class Point {
  final int x;
  final int y;
  const Point(this.x, this.y);  // const constructor (x and y are final)
}
```

**Step 2 — The magic: Dart reuses the same object.**
When two `const` objects have the same values, Dart creates only one and shares it everywhere. This is called *canonicalization* — a big word that simply means "reuse the same one."

```dart
const a = Point(1, 2);
const b = Point(1, 2);
print(identical(a, b)); // true, SAME object in memory (reused)

final c = Point(1, 2);
print(identical(a, c)); // false, final builds a NEW object
```

**Step 3 — Why this matters in Flutter (the real benefit).**
Flutter rebuilds widgets very often. When you write `const Text('Hello')`, Flutter sees it is the same object as last time, so it skips rebuilding it. Less work means a smoother app, especially in long lists.

```dart
// Good: this Text is built once and reused on every rebuild
const Text('Welcome');

// Without const: a new Text object is made on every rebuild
Text('Welcome');
```

So the advice "use `const` everywhere you can" is not random — it directly reduces rebuild work.

**Why interviewers ask:** They want to know if "use const everywhere" is something you just memorized, or something you understand. The real reason is: const objects are reused, so Flutter can skip rebuilding them.

**Common mistake:** Saying const "makes it faster" with no reason. The reason is: const objects are shared in memory, and Flutter skips rebuilding the same object.

**Follow-ups they may ask:**
- *"Why must all fields be `final`?"* → Because a const object is frozen. If a field could change, it wouldn't be a fixed compile-time value.
- *"What if one value comes from the network?"* → Then it can't be `const`. Keep the changing part separate and make the rest `const`.

**Related:** [Q2 — final vs const](#q2) · [Q26 — garbage collection](#q26)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. How do you check if two objects are equal? Explain `==`, `hashCode`, and `identical`.

> Very common · Medium

**Short answer (say this):**
"By default, Dart says two objects are equal only if they are the exact same object. To compare by values, I override `==` and `hashCode` together — they must always agree. In real projects I use `Equatable` or `freezed` so I don't make mistakes by hand."

**Let's understand it fully:**

**Step 1 — The default is "same object" equality.**
By default, two objects are equal only if they are literally the same one in memory:

```dart
class User { final String name; User(this.name); }

final a = User('Sara');
final b = User('Sara');
print(a == b); // false! Same name, but they are two different objects
```

This surprises people. Same data, but `==` is false, because Dart compared identity, not values.

**Step 2 — Three things, explained with people.**
Imagine two people:
- **`identical(a, b)`** asks: *"Are these the same single person?"* (same object in memory)
- **`==`** (value equality) asks: *"Are these two people twins with the exact same details?"*
- **`hashCode`** is like a person's ID number used for fast searching.

**Step 3 — How to compare by value (override `==` and `hashCode`).**
You must override both together. The rule: if `a == b`, then `a.hashCode` must equal `b.hashCode`.

```dart
class Money {
  final int amount;
  final String currency;
  const Money(this.amount, this.currency);

  @override
  bool operator ==(Object other) =>
      other is Money &&
      other.amount == amount &&
      other.currency == currency;

  @override
  int get hashCode => Object.hash(amount, currency); // easy and correct
}

print(Money(100, 'BDT') == Money(100, 'BDT')); // true now
```

Use `Object.hash(...)` to combine fields — don't invent your own math.

**Step 4 — Why `hashCode` matters (the hidden bug).**
`Set` and `Map` use `hashCode` first to find items quickly, then use `==` to confirm. If you override `==` but forget `hashCode`, your objects can "disappear" from a `Set` or `Map`:

```dart
final seen = <Money>{};
seen.add(Money(100, 'BDT'));
print(seen.contains(Money(100, 'BDT'))); // false if hashCode is missing!
```

**Step 5 — Why this matters in state management.**
In BLoC or Riverpod, if a new state object is `==` the old one, the UI correctly does not rebuild. If your equality is wrong, you either rebuild too much, or never rebuild. That is why `Equatable` and `freezed` (which auto-generate `==` and `hashCode`) are so popular.

**Why interviewers ask:** Wrong equality causes two classic bugs: items lost in a Set or Map, and screens rebuilding wrongly in state management. They want to know you understand the `==` plus `hashCode` contract.

**Common mistake:** Overriding `==` but forgetting `hashCode` (or the opposite). Always do both. Also, never use changing (mutable) fields in `hashCode`.

**Follow-ups they may ask:**
- *"Why use only unchanging fields in `hashCode`?"* → If a field changes after the object is inside a Set, its "ID" changes and the Set can't find it anymore.
- *"How do you avoid writing this by hand?"* → Use `Equatable` or `freezed`; they generate correct `==` and `hashCode` for you.

**Related:** [Q16 — records (built-in value equality)](#q16) · [Q3 — const & identical](#q3)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. Why do we use generics? Explain `<T>` and bounded generics.

> Common · Medium

**Short answer (say this):**
"Generics let me write code once and reuse it safely with any type. `List<int>` means only ints go in and come out, and Dart checks this while I code. A bound like `<T extends Comparable>` adds a rule, so I can safely use certain methods on T."

**Let's understand it fully:**

**Step 1 — The problem without generics.**
Without generics, you'd use `dynamic`, which removes safety:

```dart
List things = [1, 2, 'oops']; // mixed types, no safety
int total = 0;
for (var t in things) total += t; // crash at 'oops' while running
```

**Step 2 — Generics = a labeled container.**
Think of a generic like a labeled box. A "box of `int`" only holds ints. The label keeps wrong items out — and Dart checks it while you code:

```dart
List<int> numbers = [1, 2, 3];
// numbers.add('oops'); // caught immediately, not at runtime
```

**Step 3 — Writing your own generic class.**
The `<T>` is a placeholder for "any one type the caller chooses."

```dart
class Box<T> {
  final T value;
  const Box(this.value);
  T get content => value;
}

final intBox = Box<int>(5);        // T is int
final textBox = Box<String>('hi'); // T is String
```

**Step 4 — Bounded generics = a rule on the label.**
Sometimes you need T to have certain abilities. A bound says "T must be this kind of type." For example, to compare values, T must be `Comparable`:

```dart
// T must be comparable (like numbers or text), so compareTo() is allowed
T bigger<T extends Comparable<T>>(T a, T b) =>
    a.compareTo(b) >= 0 ? a : b;

print(bigger<int>(5, 9));         // 9
print(bigger<String>('a', 'z'));  // 'z'
```

Without the bound `extends Comparable`, Dart wouldn't know T can be compared, so `compareTo` would be an error.

**Why interviewers ask:** To see you write type-safe, reusable code instead of using `dynamic` and hoping nothing breaks.

**Common mistake:** Using `List<dynamic>` or a bare `List` when `List<int>` works. This throws away Dart's safety.

**Follow-ups they may ask:**
- *"Why add a bound?"* → Without it, Dart treats T as a plain `Object`, so you can only use basic methods. The bound unlocks more methods.
- *"Real Flutter example?"* → `Future<User>`, `List<Widget>`, `StreamBuilder<int>` — generics are everywhere.

**Related:** [Q2 — types](#q2)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What is the difference between an `Exception` and an `Error` in Dart?

> Common · Easy–Medium

**Short answer (say this):**
"An `Exception` is a problem you can expect and handle — like a failed network call. An `Error` usually means a bug in my code — like a wrong list index. So I catch and handle exceptions, but I fix errors instead of hiding them."

**Let's understand it fully:**

**Step 1 — The simple difference.**
- **Exception** = something that can go wrong even in correct code (no internet, bad server response). → Catch and handle it.
- **Error** = a programmer mistake (wrong index, calling something wrongly). → Fix the code, don't catch it.

```dart
// Exception, expected, handle it:
throw const FormatException('Bad date format');

// Error, a bug, fix it:
final list = [1, 2];
print(list[5]); // RangeError, your code is wrong, fix it
```

**Step 2 — How to catch exceptions properly.**

```dart
Future<User> loadUser() async {
  try {
    return await api.fetchUser();
  } on TimeoutException {
    rethrow;                         // pass it up to be retried
  } catch (e, stackTrace) {
    log('Failed to load user', e, stackTrace);
    throw UserLoadException();       // turn it into a clear app error
  } finally {
    print('done trying');            // 'finally' always runs
  }
}
```

**Step 3 — Three keywords to know.**
- **`on Type`** → catch only a specific exception type.
- **`catch (e, stackTrace)`** → get the error and where it came from.
- **`rethrow`** → throw the same error again without losing the original stack trace. (Using `throw e;` instead loses that information — a common mistake.)
- **`finally`** → runs no matter what (good for closing files, hiding a loading spinner).

**Step 4 — Make your own exception.**

```dart
class UserLoadException implements Exception {
  final String message;
  UserLoadException([this.message = 'Could not load user']);
  @override
  String toString() => 'UserLoadException: $message';
}
```

**Why interviewers ask:** To check you don't wrap everything in an empty `catch (e) {}` that hides real bugs.

**Common mistake:** Catching every error just to stop crashes. This hides bugs and makes them very hard to find later. Catch what you can handle; let real bugs surface in development.

**Follow-ups they may ask:**
- *"`rethrow` vs `throw e`?"* → `rethrow` keeps the original stack trace (where it really started). `throw e` resets it, so you lose the trail.
- *"Should you catch `Error` types?"* → Usually no. They mean your code is wrong — fix the code instead.

**Related:** [Q19 — error handling with async](#q19)

[↑ Back to top](#toc)

---

# B. Functions & closures

---

<a id="q7"></a>
## 7. What are named, positional, and optional parameters? When do you use each?

> Very common · Easy

**Short answer (say this):**
"Positional parameters depend on order and are good for one or two obvious values. Named parameters use a label, so the code reads clearly — that's why Flutter widgets use them everywhere. `required` makes a named one mandatory, and `[ ]` makes a positional one optional with a default."

**Let's understand it fully:**

**Step 1 — Positional parameters (order matters).**

```dart
int add(int a, int b) => a + b;
add(2, 3); // 5, you must pass them in order
```

**Step 2 — Optional positional with a default (use `[ ]`).**

```dart
int increase(int x, [int by = 1]) => x + by;
increase(5);     // 6  (by defaults to 1)
increase(5, 10); // 15
```

**Step 3 — Named parameters (use a label, very readable).**

```dart
void createUser({required String name, bool isAdmin = false}) {}

createUser(name: 'Sara');                 // isAdmin defaults to false
createUser(name: 'Sara', isAdmin: true);  // clear and readable
```

**Step 4 — Why named parameters are better for many values.**
Compare these two calls:

```dart
createUser('Sara', true, false);                       // what do true/false mean?
createUser(name: 'Sara', isAdmin: true, sendEmail: false); // explains itself
```

Simple rule: if you have many values, or any `true/false` value, use named parameters. They explain themselves and survive code changes (order doesn't matter).

**Why interviewers ask:** Good parameter design is a sign of a senior who writes readable, maintainable APIs.

**Common mistake:** Passing a bare `true` as a positional value. Six months later, nobody remembers what that `true` means.

**Follow-ups they may ask:**
- *"Can a parameter be required AND named?"* → Yes: `{required String name}`. This is the most common Flutter style.
- *"Default value for a named parameter?"* → `{bool isAdmin = false}`.

**Related:** [Q11 — constructors use named params](#q11)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is a closure? Explain it simply with an example.

> Common · Medium

**Short answer (say this):**
"A closure is a function that remembers the variables around it, even after that outer code has finished running. It is how callbacks keep access to their data. The key point: a closure remembers the variable itself, not a frozen copy of its value."

**Let's understand it fully:**

**Step 1 — The backpack idea.**
Think of a closure like a backpack. When you create a function, it puts the nearby variables into its backpack and carries them everywhere — even after the outer function has ended.

```dart
Function makeCounter() {
  var count = 0;            // this goes into the function's "backpack"
  return () => ++count;     // the returned function remembers count
}

final next = makeCounter();
print(next()); // 1
print(next()); // 2  (count is remembered between calls!)
print(next()); // 3
```

The outer function `makeCounter` already finished, but `count` is still alive inside the returned function. That is a closure.

**Step 2 — It remembers the variable, not a copy.**
This is important. If the variable changes, the closure sees the new value:

```dart
int value = 10;
final show = () => print(value); // remembers the variable 'value'
value = 99;
show(); // prints 99, not 10 — it read the latest value
```

**Step 3 — Closures are everywhere in Flutter.**
Every button callback is a closure that remembers data from around it:

```dart
ElevatedButton(
  onPressed: () => context.read<AuthBloc>().add(LoginPressed(user)),
  // this closure "remembers" context and user
  child: const Text('Login'),
);
```

**Why interviewers ask:** Closures power all callbacks, `.then()`, and event handlers. They want to see you understand how the data stays available.

**Common mistake:** Thinking a closure copies the value. It remembers the live variable, so the value can change.

**Follow-ups they may ask:**
- *"Any danger with closures?"* → Yes. Accidentally keeping a big object or `context` alive can cause a memory leak. Be careful with closures inside long-living objects.

**Related:** [Q19 — async callbacks](#q19) · [Q21 — stream listeners](#q21)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What is cascade notation (`..`)? How is it different from method chaining?

> Common · Easy–Medium

**Short answer (say this):**
"Cascade (`..`) lets me run many actions on the same object without writing its name again. Each `..` ignores what the action returns and gives back the original object. Method chaining is different — it works only because each method returns something to call the next one on."

**Let's understand it fully:**

**Step 1 — The "and also..." idea.**
`..` is like saying "...and also...and also..." about the same object.

```dart
// Without cascade, repeat the name every time:
final paint = Paint();
paint.color = Colors.red;
paint.strokeWidth = 4;
paint.style = PaintingStyle.stroke;

// With cascade, cleaner, same object:
final paint2 = Paint()
  ..color = Colors.red
  ..strokeWidth = 4
  ..style = PaintingStyle.stroke;
```

Both do the same thing, but the cascade version is shorter and clearer.

**Step 2 — Cascade vs method chaining (the real difference).**
- **Cascade (`..`)** → ignores the return value, always gives back the original object. Good for setting many properties.
- **Method chaining (`a.b().c()`)** → works only because each method returns an object to keep going.

```dart
// Method chaining: each step returns a String to continue
final result = 'hello world'.toUpperCase().trim().substring(0, 5);

// Cascade: setting properties returns nothing useful, so .. is perfect
final list = <int>[]..add(1)..add(2)..add(3);
```

**Step 3 — Null-safe cascade (`?..`).**

```dart
paint?..color = Colors.blue; // does nothing if paint is null
```

**Why interviewers ask:** It's small, but it shows whether you read return types and write clean Dart.

**Follow-ups they may ask:**
- *"What is `?..`?"* → Same as `..`, but it does nothing if the object is null.

**Related:** [Q10 — more syntax sugar](#q10)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What is `typedef`, the spread operator (`...`), and collection `if`/`for`?

> Common · Easy

**Short answer (say this):**
"`typedef` gives a nickname to a type — usually a function type — so the code reads better. The spread operator and collection `if`/`for` let me build lists in a clean, readable way, which is very useful for Flutter widget lists."

**Let's understand it fully:**

**Step 1 — `typedef`: a nickname for a type.**
If a function type is long and used many times, give it one clear name:

```dart
// Without typedef, long and repeated:
void setValidator(String? Function(String value) check) {}

// With typedef, clean:
typedef Validator = String? Function(String value);
void setValidator(Validator check) {}
```

`typedef` can also name non-function types: `typedef Json = Map<String, dynamic>;`

**Step 2 — Spread (`...`): pour one list into another.**

```dart
final first = [1, 2];
final second = [3, 4];
final all = [...first, ...second]; // [1, 2, 3, 4]
```

`...?` is the null-safe version (pours in only if not null):

```dart
final all = [...first, ...?maybeNullList];
```

**Step 3 — Collection `if` and `for`: build lists with logic inside.**
This is extremely useful in Flutter widget lists:

```dart
final widgets = [
  const Header(),
  if (isLoggedIn) const ProfileButton(),   // add only if logged in
  for (final item in items) ItemTile(item), // add one per item
  ...?footerWidgets,                         // add list if not null
];
```

Without this, you'd build the list with many `if` blocks and `.add()` calls before the `return` — messy and hard to read.

**Why interviewers ask:** To see if you write clean, modern, declarative Dart instead of old imperative list-building.

**Follow-ups they may ask:**
- *"Is there a collection `if-else`?"* → Yes: `if (cond) WidgetA() else WidgetB()` inside a list.

**Related:** [Q9 — cascade](#q9)

[↑ Back to top](#toc)

---

# C. Classes & object-oriented Dart

---

<a id="q11"></a>
## 11. Explain Dart's constructors: normal, named, factory, const, and redirecting.

> Very common · Medium

**Short answer (say this):**
"A normal constructor always makes a new object. A named constructor gives a clear second way to build it. A factory constructor does not have to make a new object — it can return a cached one or even a subtype. Redirecting means one constructor calls another to avoid repeating code."

**Let's understand it fully:**

**Step 1 — Normal (generative) constructor.**
Builds a fresh object every time. The `this.x` shortcut assigns the field directly.

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name); // normal constructor
}
```

**Step 2 — Named constructor (a clearly-labeled second way).**

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name);
  User.guest() : id = '0', name = 'Guest'; // named constructor
}

final u = User.guest(); // clear what this does
```

**Step 3 — The initializer list (the part after `:`).**
The code after `:` runs before the constructor body. It is the only place to set `final` fields, call `super(...)`, and use `assert`.

```dart
User(String id, String name)
    : id = id,
      assert(id.isNotEmpty, 'id cannot be empty') {
  // body runs after the initializer list
}
```

**Step 4 — Redirecting constructor (call another constructor).**
Avoids repeating logic by forwarding to another constructor:

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name);
  User.anonymous() : this('0', 'Anonymous'); // redirects to User(...)
}
```

**Step 5 — Factory constructor (the special one).**
A factory does not have to create a new object. It can:
- return a cached object,
- return a subtype,
- or fail (throw) while building.

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name);

  factory User.fromJson(Map<String, dynamic> json) {
    return User(json['id'] as String, json['name'] as String);
  }
}
```

`fromJson` is a factory exactly because it might fail, return a cached object, or return a subtype — a normal constructor can't do that.

**Step 6 — const constructor.**
Builds the object before running (all fields must be `final`). See [Q3](#q3).

**Why interviewers ask:** Many people only know `fromJson` but can't explain why it's a factory. They want the real reason: factories can break the "one call = one new object" rule.

**Common mistake:** Thinking a factory always makes a new object. It doesn't have to. Also, trying to use `this` inside a factory — the object doesn't exist yet.

**Follow-ups they may ask:**
- *"Can a factory return null?"* → No (with null safety, the return type must be non-null unless declared nullable). It must return a valid object.
- *"When use named vs factory?"* → Named = a simple alternate way to build. Factory = when you need control (caching, subtypes, validation).

**Related:** [Q3 — const constructor](#q3) · [Q12 — OOP keywords](#q12) · [Q7 — named parameters](#q7)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. Dart has no `interface` keyword. How do you get interfaces? And what is the difference between `extends`, `implements`, `with`, and `on`?

> Very common · Medium — the most common Dart OOP question.

**Short answer (say this):**
"In Dart, every class can be used as an interface automatically. `extends` is for inheriting code — only one parent. `implements` takes only the rules (the contract) and forces me to write everything myself. `with` adds reusable behavior (a mixin). `on` limits which classes a mixin can be used with."

**Let's understand it fully:**

**Step 1 — Dart has no `interface` keyword, because every class IS an interface.**
In Java you write `interface`. In Dart, every class automatically defines an interface (its list of methods). So you can `implements` any class.

**Step 2 — `extends`: inherit the parent's code (only ONE parent).**
You get the parent's working code for free and can reuse or override it.

```dart
class Animal {
  void breathe() => print('breathing');
}

class Dog extends Animal {
  void bark() => print('woof');
}

Dog().breathe(); // inherited from Animal for free
```

**Step 3 — `implements`: take only the rules, write all the code yourself.**
You get none of the code — only the requirement to provide every method.

```dart
class Animal {
  void breathe() => print('breathing');
}

class Robot implements Animal {
  // must write breathe() myself; nothing is inherited
  @override
  void breathe() => print('robot pretends to breathe');
}
```

You can `implements` many classes at once (many contracts).

**Step 4 — `with`: add reusable behavior (mixin).**

```dart
mixin Swimmer {
  void swim() => print('swimming');
}

class Duck extends Animal with Swimmer {} // gets breathe() AND swim()
```

**Step 5 — `on`: limit where a mixin can be used.**

```dart
mixin Validating on Form {
  // can only be added to classes that are a Form
}
```

**Step 6 — A clear comparison table.**

| Keyword | What you get | How many | When to use |
|---|---|---|---|
| `extends` | the parent's **code** | only **one** | "is-a" + reuse code |
| `implements` | only the **rules** (write all code) | many | follow a contract |
| `with` | reusable **behavior** | many | share behavior across classes |
| `on` | a **rule** for a mixin | — | restrict a mixin to a type |

Easy way to remember:
- **`extends`** = "I get my parent's code for free."
- **`implements`** = "I promise to follow these rules, but I write the code myself."

**Why interviewers ask:** This is the clearest test of whether you truly understand Dart OOP.

**Common mistake:** Saying "Dart has no interfaces." Wrong — every class is also an interface. Also mixing up `extends` (inherit code) with `implements` (rewrite everything).

**Follow-ups they may ask:**
- *"Why use `implements` in testing?"* → You can make a fake version of a class to test without pulling in the real code. Great for mocking.
- *"Can a class extend one and implement many?"* → Yes: `class A extends B implements C, D {}`.

**Related:** [Q13 — mixins in depth](#q13) · [Q11 — constructors](#q11)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. What are mixins? Explain `with`, `on`, and what happens when two mixins have the same method.

> Common · Medium–Hard

**Short answer (say this):**
"A mixin is reusable behavior you add to a class with `with`, without using inheritance. You can add many mixins. If two mixins have the same method, the last one wins. The `on` keyword limits a mixin so it can only be used on a certain type."

**Let's understand it fully:**

**Step 1 — Mixins are "extra skills" for a class.**
Think of mixins as abilities you attach to a class. A `Duck` can get the "Swimmer" skill and the "Walker" skill — without inheriting from them.

```dart
mixin Swimmer {
  void swim() => print('swimming');
}
mixin Walker {
  void walk() => print('walking');
}

class Duck with Swimmer, Walker {}

Duck()..swim()..walk(); // has both skills
```

**Step 2 — What if two mixins have the SAME method?**
Dart lines them up from left to right, and the last one wins:

```dart
mixin A { void greet() => print('Hello from A'); }
mixin B { void greet() => print('Hello from B'); }

class C with A, B {}   // B is last
C().greet();           // "Hello from B"  (last mixin wins)
```

This ordering is called *linearization* — Dart flattens the mixins into a clear single line, so there is no confusion.

**Step 3 — `on`: restrict a mixin to a certain type.**
`on` says "this mixin can only be added to classes of this type." This lets the mixin safely use that type's methods:

```dart
class Animal {
  void breathe() => print('breathing');
}

mixin Pet on Animal {
  void play() {
    breathe();        // safe — we know the host is an Animal
    print('playing');
  }
}

class Cat extends Animal with Pet {} // Cat is an Animal, so Pet is allowed
```

**Step 4 — Why mixins can't have a constructor.**
A mixin gets merged into the main class, which already handles object creation. So a mixin has no separate object to construct — that's why it can't have a constructor.

**Why interviewers ask:** To check you understand mixin order (last wins) and the purpose of `on`.

**Common mistake:** Calling mixins "multiple inheritance." It's not a confusing diamond — Dart lines them up in order and the last one wins. Clean and predictable.

**Follow-ups they may ask:**
- *"Mixin vs interface (`implements`)?"* → A mixin gives you working code. `implements` gives you only rules and you write the code.
- *"`with` vs `extends`?"* → `extends` = one parent's code. `with` = add many reusable behaviors.

**Related:** [Q12 — extends/implements/with/on](#q12)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. What are extension methods? What can they NOT do?

> Common · Medium

**Short answer (say this):**
"Extensions let me add methods to a type I don't own — like `String` or `int` — without changing it or wrapping it. The main limits: they are chosen based on the variable's written type (not its real type), and they cannot add new fields (no state)."

**Let's understand it fully:**

**Step 1 — Add a "button" to an existing tool.**
An extension is like adding a new helper method to a type you can't edit:

```dart
extension StringHelpers on String {
  bool get isValidEmail => contains('@') && contains('.');
  String capitalize() =>
      isEmpty ? this : '${this[0].toUpperCase()}${substring(1)}';
}

'a@b.com'.isValidEmail; // true
'hello'.capitalize();   // 'Hello'
```

Now `String` feels like it always had these methods. Very clean.

**Step 2 — Real Flutter example (very common).**

```dart
extension ContextX on BuildContext {
  double get width => MediaQuery.of(this).size.width;
  ThemeData get theme => Theme.of(this);
}

// usage inside a widget:
final w = context.width;     // instead of MediaQuery.of(context).size.width
final t = context.theme;     // instead of Theme.of(context)
```

**Step 3 — Limit 1: no new fields (no stored data).**
Extensions can add methods and getters, but not instance variables. They add behavior, not state.

**Step 4 — Limit 2: chosen by the WRITTEN type, not the real type.**
This is the tricky part. Extensions are picked at compile time based on the declared type:

```dart
String text = 'hi';
text.capitalize();   // works — declared type is String

Object thing = 'hi';
// thing.capitalize(); // error — declared type is Object, not String
```

So extensions are not like overridden methods (which use the real runtime type).

**Why interviewers ask:** To see if you know extensions are resolved by the written type, and that they can't hold state.

**Common mistake:** Expecting an extension to behave polymorphically (by real type). It is chosen by the declared type.

**Follow-ups they may ask:**
- *"Can two extensions define the same method?"* → Yes, but then it's ambiguous; you must call one explicitly: `StringHelpers('hi').capitalize()`.

**Related:** [Q12 — OOP keywords](#q12)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. What are enhanced enums? Can an enum have fields and methods?

> Common · Medium

**Short answer (say this):**
"Yes. Since Dart 2.17, enums can have fields, a const constructor, and methods. So instead of an enum plus a separate helper, I keep the data and behavior together on the enum itself."

**Let's understand it fully:**

**Step 1 — A basic enum is a fixed list of choices.**

```dart
enum Status { active, paused, cancelled }
```

**Step 2 — The old, painful way (before 2.17).**
People used a `switch` helper to attach data to each value — messy and easy to forget cases:

```dart
int priceOf(Plan p) {
  switch (p) {
    case Plan.free: return 0;
    case Plan.pro: return 12;
    // forget a case, and you get a bug
  }
}
```

**Step 3 — The modern way: put data and methods on the enum.**

```dart
enum Plan {
  free(price: 0, maxProjects: 1),
  pro(price: 12, maxProjects: 50),
  team(price: 40, maxProjects: 1000);

  // const constructor + final fields
  const Plan({required this.price, required this.maxProjects});
  final int price;
  final int maxProjects;

  // methods and getters on the enum
  bool get isPaid => price > 0;
}

Plan.pro.price;     // 12
Plan.pro.isPaid;    // true
```

**Step 4 — Useful built-in enum features.**

```dart
Plan.values;                 // [Plan.free, Plan.pro, Plan.team]
Plan.pro.index;              // 1
Plan.pro.name;               // 'pro'
Plan.values.byName('free');  // Plan.free  (find by text)
```

**Why interviewers ask:** To see if you write modern Dart instead of old enum + switch helpers.

**Follow-ups they may ask:**
- *"enum vs sealed class?"* → enum = a fixed list of single values that all share the same shape. sealed class = a fixed list of types that can each hold different data (see [Q18](#q18)).

**Related:** [Q18 — sealed classes](#q18)

[↑ Back to top](#toc)

---

# D. Dart 3 new features (records, patterns, sealed classes)

> These three features show you write Dart **today**, not Dart from years ago. Expect at least one of them.

---

<a id="q16"></a>
## 16. What are records in Dart 3?

> Very common (Dart 3) · Medium

**Short answer (say this):**
"A record is a quick way to group a few values together without creating a class. It is immutable (cannot change), and two records with the same values are equal. The most common use is returning more than one value from a function."

**Let's understand it fully:**

**Step 1 — The problem before records.**
To return two values, you either made a whole class (too much work) or returned a `List`/`Map` (no safety):

```dart
// Old, unsafe way:
List getResponse() => [200, 'OK'];
final r = getResponse();
final code = r[0]; // which index is what? easy to mix up
```

**Step 2 — Records = a small bag of values.**
Think of a record like a small bag carrying a few items together. No class needed.

```dart
// Return two values cleanly:
(int, String) getResponse() => (200, 'OK');

final result = getResponse();
print(result.$1); // 200  (access by position: $1, $2, ...)
print(result.$2); // OK
```

**Step 3 — Unpack (destructure) in one line.**

```dart
final (code, body) = getResponse();
print('$code $body'); // 200 OK
```

**Step 4 — Named fields (clearer than $1, $2).**

```dart
({double lat, double lng}) getLocation() => (lat: 23.8, lng: 90.4);

final loc = getLocation();
print(loc.lat); // 23.8
print(loc.lng); // 90.4
```

**Step 5 — Records compare by value (built-in equality).**

```dart
print((1, 'a') == (1, 'a')); // true, same values means equal
```

When to use: use a record for quick, temporary groups of values. Use a real class once the data has a clear name and needs methods.

**Why interviewers ask:** To see if you use records instead of old tricks like the `Tuple2` package or returning a `Map`.

**Common mistake:** Using records everywhere as your main data model. Once data has a real meaning (like `User`), make a proper class.

**Follow-ups they may ask:**
- *"Can you change a record's value?"* → No, records are immutable.
- *"Records vs a class?"* → Records = quick, no name, no methods. Class = named, can have methods, better for real models.

**Related:** [Q4 — value equality](#q4) · [Q17 — destructuring patterns](#q17)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. What is pattern matching, destructuring, and switch expressions?

> Very common (Dart 3) · Medium–Hard

**Short answer (say this):**
"Patterns let me check the shape of data and pull values out at the same time. A switch *expression* returns a value, which is much cleaner than a long switch that assigns variables. And `if-case` lets me check a shape and unpack it in one line — great for reading JSON safely."

**Let's understand it fully:**

**Step 1 — Destructuring: unpack values in one step.**

```dart
final (a, b) = (1, 2);            // a = 1, b = 2
final [first, second] = [10, 20]; // first = 10, second = 20
final {'name': name} = {'name': 'Sara'}; // name = 'Sara'
```

**Step 2 — switch expression: a switch that RETURNS a value.**
Old switch *statement* (sets a variable):

```dart
String label;
switch (status) {
  case Status.active: label = 'Active'; break;
  case Status.paused: label = 'Paused'; break;
  default: label = 'Unknown';
}
```

New switch *expression* (returns the value directly, cleaner):

```dart
final label = switch (status) {
  Status.active => 'Active',
  Status.paused => 'Paused',
  _ => 'Unknown',          // _ means "anything else"
};
```

**Step 3 — Patterns inside a switch (match shape + unpack).**

```dart
String describe(Object o) => switch (o) {
  (int x, int y) => 'point $x, $y',          // matches a record
  [final first, ...] => 'list starts with $first', // matches a list
  int n when n > 0 => 'positive number',     // 'when' adds a condition
  String s => 'text: $s',                     // matches a String + binds it
  _ => 'something else',
};
```

**Step 4 — `if-case`: check a shape and unpack in one line.**
This is excellent for safely reading JSON:

```dart
final json = {'token': 'abc123'};

if (json case {'token': final String token}) {
  saveToken(token); // token is ready to use AND guaranteed to be a String
}
```

If the shape doesn't match (no `token`, or it's not a String), the `if` is simply skipped — no crash.

**Why interviewers ask:** To replace old, long `if (x is Type) { final t = x as Type; ... }` code with clean pattern matching.

**Common mistake:** Not knowing the difference between a switch *statement* (does an action) and a switch *expression* (returns a value).

**Follow-ups they may ask:**
- *"What does `User(:final id)` mean?"* → It matches a `User` object and pulls out its `id` field into a variable named `id`.
- *"What is `when`?"* → An extra condition added to a pattern, like `int n when n > 0`.

**Related:** [Q16 — records](#q16) · [Q18 — sealed + exhaustive switch](#q18)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. What are sealed classes? And the new class modifiers (`sealed`, `final`, `base`, `interface`)?

> Common (Dart 3) · Hard

**Short answer (say this):**
"A `sealed` class has a fixed, known set of subclasses, all in the same file. The big benefit: when I `switch` over it, Dart checks that I handled every case. If I add a new subclass later and forget to handle it, the code won't even compile. The other modifiers — `final`, `base`, `interface` — control how a class can be reused in other files."

**Let's understand it fully:**

**Step 1 — `sealed` is like a fixed menu.**
A sealed class says "these are the only options that exist." This is perfect for app states like *loading / success / error*:

```dart
sealed class Result {}

class Loading extends Result {}
class Success extends Result {
  final String data;
  Success(this.data);
}
class Failure extends Result {
  final String error;
  Failure(this.error);
}
```

**Step 2 — The big benefit: Dart forces you to handle every case.**

```dart
String show(Result r) => switch (r) {
  Loading() => 'Loading...',
  Success(:final data) => 'Got: $data',
  Failure(:final error) => 'Error: $error',
  // No "default" needed — Dart knows these are ALL the options.
};
```

If you later add `class Empty extends Result {}` and forget to handle it, the code won't compile. Dart points right at the missing case. This stops a whole class of bugs.

**Step 3 — Why this beats old approaches.**
Old way: one class with three nullable fields and a `type` flag — easy to create invalid states (data AND error at once?). Sealed classes make invalid states impossible and ensure every state is handled.

**Step 4 — The other class modifiers (control reuse in other files).**

| Modifier | Can `extend`? | Can `implement`? | Meaning |
|---|:---:|:---:|---|
| (none) | yes | yes | normal class |
| `final` | no | no | fully locked, no extending or implementing |
| `base` | yes | no | can extend, but cannot re-implement |
| `interface` | no | yes | only a contract, implement it, don't extend it |
| `sealed` | no | no | fixed subclasses, safe and complete `switch` |

(Note: `final` here is the *class modifier*, which is different from the `final` keyword for variables.)

**Why interviewers ask:** To see if you use the type system to prevent bugs — like making sure every app state is handled.

**Common mistake:** Not knowing that the "handle every case" benefit specifically needs `sealed`. A normal class doesn't give that check.

**Follow-ups they may ask:**
- *"sealed class vs freezed union?"* → Both model fixed states. `sealed` is built into the language and gives compile-time "handle all cases" for free, without code generation.
- *"Why the `interface` modifier?"* → It clearly says "implement me, don't extend me," and Dart enforces it across files.

**Related:** [Q15 — enum vs sealed](#q15) · [Q17 — switch patterns](#q17)

[↑ Back to top](#toc)

---

# E. Async & concurrency (Future, Stream, Isolate)

---

<a id="q19"></a>
## 19. What is a `Future`? How does `async`/`await` work? Does `await` freeze the app?

> Very common · Medium

**Short answer (say this):**
"A `Future` is a value that will be ready later — like a receipt for food you ordered. `async`/`await` lets me write this in a simple top-to-bottom style. Very important: `await` does not freeze the app. It only pauses that one function and lets the rest of the app keep working."

**Let's understand it fully:**

**Step 1 — The restaurant example.**
Imagine ordering food at a restaurant:
- You order and get a receipt now → that's the `Future`.
- The food arrives later → that's the value.
- While you wait, the kitchen keeps serving other customers → that's the app staying responsive.

`await` waits for your order only — it does not stop the whole restaurant.

**Step 2 — Without and with async/await.**

```dart
// A Future is a "value coming later"
Future<String> fetchName() async {
  await Future.delayed(const Duration(seconds: 2)); // pretend network
  return 'Sara';
}

void main() async {
  print('start');
  final name = await fetchName(); // pause THIS function for 2s
  print('Hello $name');           // runs after the value arrives
  print('end');
}
// Output: start, then after 2s, Hello Sara, then end
```

During those 2 seconds, the app is not frozen — buttons still work, animations still play. Only this function is paused.

**Step 3 — The most important point: `await` is not blocking.**
`await` means "pause here and let the app do other things until the value is ready." It does not stop the screen. (If it did, every app would freeze on every network call.)

**Step 4 — Running things in parallel (a senior detail).**
If two tasks don't depend on each other, don't `await` them one by one — that's slow. Run them together with `Future.wait`:

```dart
// Slow: 2s + 2s = 4s total
final a = await fetchA();
final b = await fetchB();

// Fast: both run together = about 2s total
final results = await Future.wait([fetchA(), fetchB()]);
```

But if B needs A's result, then sequential `await` is correct.

**Why interviewers ask:** The number one async mistake is thinking `await` freezes the whole app. They want to hear: it only pauses that function; the app keeps running.

**Common mistake:** Awaiting independent calls one by one (slow). Use `Future.wait` to run them together.

**Follow-ups they may ask:**
- *"`Future.wait` vs `Future.any`?"* → `wait` finishes when all are done. `any` finishes when the first one is done.
- *"How do you handle errors with await?"* → Wrap the `await` in `try/catch` to catch errors from the Future.

**Related:** [Q20 — event loop](#q20) · [Q21 — Streams](#q21) · [Q6 — error handling](#q6)

[↑ Back to top](#toc)

---

<a id="q20"></a>
## 20. Explain the event loop: microtask queue vs event queue.

> Deeper question · Hard — a senior tie-breaker.

**Short answer (say this):**
"Dart runs on a single event loop with two lines: a microtask line (high priority) and an event line (normal). Dart finishes all microtasks before taking the next event. Futures and code after `await` use the microtask line, while timers, taps, and network results use the event line."

**Let's understand it fully:**

**Step 1 — The bank with two lines.**
Imagine a bank with two queues:
- **Microtask line = VIP line.** Always served completely first.
- **Event line = normal line.** Served only after the VIP line is empty.

Dart works the same way: it empties the whole microtask (VIP) line before taking even one item from the event (normal) line.

**Step 2 — Who goes in which line?**
- **Microtask (VIP):** `Future.microtask(...)`, `scheduleMicrotask(...)`, and the code that runs after an `await` completes.
- **Event (normal):** `Future(...)`, `Timer`, user taps, network responses, file reads.

**Step 3 — Predict the output (this exact question is common).**

```dart
void main() {
  print('1');                          // runs now (synchronous)
  Future(() => print('2'));            // normal line (event)
  Future.microtask(() => print('3'));  // VIP line (microtask)
  print('4');                          // runs now (synchronous)
}
```

Output order:
1. `1` and `4` — normal synchronous code runs first, top to bottom.
2. `3` — the VIP (microtask) line is emptied next.
3. `2` — finally the normal (event) line.

So the output is: **`1, 4, 3, 2`.**

**Step 4 — Why this matters in real apps.**
If you keep adding microtasks in a loop, the VIP line never empties, and the normal line (which includes rendering and taps) never gets served — the app freezes. So don't flood the microtask queue.

**Why interviewers ask:** If you can correctly predict `1, 4, 3, 2`, you truly understand Dart's async model. It's a strong senior signal.

**Common mistake:** Thinking timers or Futures run before microtasks. Microtasks (VIP) always go first.

**Follow-ups they may ask:**
- *"Where does code after `await` continue?"* → On the microtask (VIP) line, so it runs before the next normal event.
- *"What can freeze the UI?"* → Long synchronous work, or flooding the microtask queue. Both block rendering.

**Related:** [Q19 — async/await](#q19) · [Q23 — single-threaded & isolates](#q23)

[↑ Back to top](#toc)

---

<a id="q21"></a>
## 21. What is a `Stream`? Explain single-subscription vs broadcast, `StreamController`, and `StreamBuilder`.

> Very common · Medium

**Short answer (say this):**
"A `Future` gives one value; a `Stream` gives many values over time. A single-subscription stream allows only one listener (the default). A broadcast stream allows many listeners. `StreamController` creates and feeds a stream, and `StreamBuilder` rebuilds a widget every time a new value arrives."

**Let's understand it fully:**

**Step 1 — Future vs Stream.**
- **Future = one delivery.** (One pizza arrives, once.)
- **Stream = a subscription.** (A YouTube channel keeps posting new videos over time.)

```dart
Future<int> oneValue() async => 42;        // one value
Stream<int> manyValues() async* {          // many values
  yield 1;
  yield 2;
  yield 3;
}
```

**Step 2 — Single-subscription vs broadcast.**
- **Single-subscription (default):** only one listener allowed. If you try to listen twice, it throws an error. Good for a one-time data flow (like reading a file).
- **Broadcast:** many listeners allowed. But new listeners do not see old values — only values added after they join.

```dart
// Single-subscription:
final controller = StreamController<int>();
controller.stream.listen((v) => print('A: $v')); // one listener
// controller.stream.listen(...);                  // second listen throws error

// Broadcast:
final bus = StreamController<int>.broadcast();
bus.stream.listen((v) => print('A: $v'));
bus.stream.listen((v) => print('B: $v')); // many listeners allowed
```

**Step 3 — StreamController = the "feed" side of a stream.**
It gives you a `stream` to listen to, and you push values with `add(...)`. Always `close()` it when done.

```dart
final controller = StreamController<int>();
controller.stream.listen((v) => print(v));
controller.add(1);  // listener prints 1
controller.add(2);  // listener prints 2
controller.close(); // always close to free resources
```

**Step 4 — StreamBuilder = auto-rebuild a widget on each value.**

```dart
StreamBuilder<int>(
  stream: counterStream,
  builder: (context, snapshot) {
    if (snapshot.hasError) return Text('Error: ${snapshot.error}');
    if (!snapshot.hasData) return const CircularProgressIndicator();
    return Text('Count: ${snapshot.data}');
  },
);
```

**Step 5 — The number one stream bug: not cleaning up.**
Every subscription must be cancelled, and every controller closed, usually in `dispose()`. Forgetting this is a very common memory leak:

```dart
late final StreamSubscription _sub;

@override
void initState() {
  super.initState();
  _sub = myStream.listen(_onData);
}

@override
void dispose() {
  _sub.cancel();    // stop listening
  super.dispose();
}
```

**Why interviewers ask:** To check you know single vs broadcast, and that you clean up properly.

**Common mistake:** Forgetting to cancel subscriptions or close controllers, causing a memory leak. Also, exposing the `StreamController` itself instead of just its `stream` (which lets others mess with it).

**Follow-ups they may ask:**
- *"Does broadcast replay old values to new listeners?"* → No. They only get values added after they start listening. (Use RxDart's `BehaviorSubject` if you need the last value replayed.)
- *"FutureBuilder vs StreamBuilder?"* → FutureBuilder = one value. StreamBuilder = many values over time.

**Related:** [Q19 — Future vs Stream](#q19) · [Q22 — generators make streams](#q22)

[↑ Back to top](#toc)

---

<a id="q22"></a>
## 22. What are generators — `sync*`/`yield` and `async*`/`yield*`?

> Common · Medium–Hard

**Short answer (say this):**
"Generators produce a sequence of values lazily, one at a time. `sync*` makes an `Iterable` and gives values only when asked. `async*` makes a `Stream` and can `await` between values. `yield` gives one value; `yield*` gives all values from another sequence."

**Let's understand it fully:**

**Step 1 — `sync*` makes a lazy `Iterable`.**
"Lazy" means nothing runs until you actually ask for each value. This saves memory:

```dart
Iterable<int> firstNumbers(int n) sync* {
  for (var i = 0; i < n; i++) {
    print('making $i');
    yield i;            // give one value, then pause until asked again
  }
}

final nums = firstNumbers(3); // nothing printed yet!
print('created');             // "created" prints first
for (final n in nums) {       // NOW it runs, one at a time
  print('got $n');
}
```

**Step 2 — `async*` makes a `Stream` (values over time).**
It can `await` between values — perfect for things like a timer or live updates:

```dart
Stream<int> ticks(int n) async* {
  for (var i = 0; i < n; i++) {
    await Future.delayed(const Duration(seconds: 1));
    yield i;            // emit one value every second
  }
}
```

**Step 3 — `yield` vs `yield*`.**
- `yield value` → give one value.
- `yield* anotherSequence` → give all values from another iterable or stream (flatten it in):

```dart
Iterable<int> combined() sync* {
  yield 0;
  yield* firstNumbers(3); // gives 0, 1, 2 from the other generator
  yield 99;
}
// produces: 0, 0, 1, 2, 99
```

**Why interviewers ask:** To check you understand laziness (`sync*` does nothing until used) and the difference between `Iterable` and `Stream`.

**Common mistake:** Mixing them up. Remember: `sync*` → `Iterable` (pull when asked). `async*` → `Stream` (pushed over time).

**Follow-ups they may ask:**
- *"Why is `sync*` useful?"* → For big or even infinite sequences — you only compute what you actually use, saving memory.

**Related:** [Q21 — async* makes streams](#q21)

[↑ Back to top](#toc)

---

<a id="q23"></a>
## 23. Why is Dart single-threaded? What are isolates, and what is `compute()` / `Isolate.run`?

> Very common · Medium–Hard

**Short answer (say this):**
"Dart runs your code on a single thread, so there are no locks and no race conditions — it's simple and safe. The downside: heavy work freezes the screen. An isolate is a separate worker with its own memory. Isolates don't share memory; they pass messages. `compute()` and `Isolate.run` are easy shortcuts to run heavy work on another isolate."

**Let's understand it fully:**

**Step 1 — Single-threaded = one worker at one desk.**
Dart does one thing at a time on a single thread. The good news: no two pieces of code touch the same data at once, so there are no race conditions and no need for locks. Simple and safe.

**Step 2 — The problem: heavy work freezes the screen.**
Because there's only one worker, a slow CPU task blocks everything — including drawing the screen. The app freezes (janks):

```dart
// This heavy loop freezes the UI while it runs
int slowSum() {
  var total = 0;
  for (var i = 0; i < 1000000000; i++) total += i;
  return total;
}
```

(Note: a network call does NOT freeze the app — that's I/O, which is already non-blocking. Only heavy CPU work freezes it.)

**Step 3 — Isolates = hire a second worker at a separate desk.**
An isolate is a separate worker with its own memory. They cannot share papers (memory) — they pass notes (messages) to each other. This is why there are no locks: nothing is shared.

**Step 4 — The easy ways to use an isolate.**

```dart
// Easiest, modern way (Dart 2.19+):
final result = await Isolate.run(() => slowSum()); // runs on another worker

// Flutter's older shortcut (needs a top-level or static function):
final parsed = await compute(parseBigJson, rawText);
```

While the isolate does the heavy work, the UI thread stays free, so the screen stays smooth.

**Step 5 — The cost: data is copied.**
Because memory isn't shared, the input and result are copied between isolates. This copy has a cost. So use isolates only for big work, not small tasks.

Rule of thumb: use an isolate for CPU-heavy work that takes more than about 16ms — big JSON parsing, image processing, encryption. Don't use it for network calls (already non-blocking) or tiny tasks (copy cost isn't worth it).

**Why interviewers ask:** To see if you understand the "no shared memory" model and know when an isolate is actually worth it.

**Common mistake:** Saying "use an isolate to speed up a network call." Network I/O is already non-blocking — an isolate won't help and just adds copy cost.

**Follow-ups they may ask:**
- *"How do isolates talk to each other?"* → Through `SendPort` and `ReceivePort` (sending messages). `compute`/`Isolate.run` hide this for the simple case.
- *"Why no locks in Dart?"* → Because nothing is shared between isolates — each has its own memory.

**Related:** [Q20 — event loop / single-threaded](#q20) · [Q19 — async/await](#q19)

[↑ Back to top](#toc)

---

# F. How Dart runs (compile & memory)

---

<a id="q24"></a>
## 24. What is JIT vs AOT? Why does it matter for Flutter?

> Common · Medium

**Short answer (say this):**
"During development, Dart uses JIT (compiles while running), which is what makes hot reload so fast. In a release build, Dart uses AOT (compiled to native code before running), so the app starts fast and runs smoothly. That's why we never judge performance from a debug build."

**Let's understand it fully:**

**Step 1 — What the two words mean.**
- **JIT = Just-In-Time:** code is compiled while the app runs. Flexible and fast to change, which enables hot reload.
- **AOT = Ahead-Of-Time:** code is compiled to native machine code before the app runs. No compiling at runtime, which gives fast startup and smooth performance.

**Step 2 — When each is used in Flutter.**

| | JIT (debug mode) | AOT (release mode) |
|---|---|---|
| When | development | production (real users) |
| Best for | hot reload, fast coding | fast startup, real performance |
| Speed | slower (extra checks) | fast (native code) |

**Step 3 — Why this matters in practice.**
In debug mode, the app is slower because of JIT and extra debug checks. So if your app feels laggy in debug, don't panic — test it in release mode (`flutter run --release`) before judging performance. Many "performance bugs" disappear in release.

**Why interviewers ask:** To check you know you must never measure performance in debug mode.

**Common mistake:** Complaining about lag in a debug build and trying to "optimize" it. Always test speed in release mode first.

**Follow-ups they may ask:**
- *"What about Flutter web?"* → For web, Dart compiles to JavaScript (or newer WebAssembly), not native ARM code.
- *"What is profile mode?"* → A middle mode: release-like performance, but with some profiling tools on, for measuring real performance.

**Related:** [Q25 — Dart VM](#q25)

[↑ Back to top](#toc)

---

<a id="q25"></a>
## 25. What is the Dart VM?

> Deeper question · Hard

**Short answer (say this):**
"The Dart VM is the system that runs Dart. In development it compiles and runs your code (JIT). In a release build, your code is already compiled to native (AOT), but a small part of the VM is still included to handle things like garbage collection, isolates, and the event loop. So 'VM' does not mean 'slow' or 'interpreted'."

**Let's understand it fully:**

**Step 1 — Two jobs of the VM: compiler + runtime helpers.**
The Dart VM has two parts:
1. A compiler (used in development for JIT).
2. Runtime helpers — garbage collection (memory cleanup), isolate management, the event loop.

**Step 2 — What happens in release (AOT).**
In a release build, the compiler part is no longer needed (code is already native). But the runtime helpers are still bundled into your app, because the app still needs memory cleanup, isolates, and the event loop.

So: AOT removes the compiler, but keeps the runtime helpers.

**Step 3 — The common misunderstanding.**
"VM" makes people think "slow or interpreted like old Java." That's wrong for release Flutter — your code runs as native machine code. The VM runtime just provides support services in the background.

**Common mistake:** Thinking AOT means "no VM at all." The compiler is gone in release, but the runtime support stays.

**Follow-ups they may ask:**
- *"What is a snapshot?"* → A saved, ready-to-load form of your program, used to make the app start faster.

**Related:** [Q24 — JIT vs AOT](#q24) · [Q26 — garbage collection](#q26)

[↑ Back to top](#toc)

---

<a id="q26"></a>
## 26. How does Dart manage memory (garbage collection)?

> Deeper question · Hard

**Short answer (say this):**
"Dart automatically frees memory you no longer use — that's garbage collection (GC). It uses a 'generational' design based on a simple idea: most objects die young. New objects go to a small area that is cleaned quickly. Objects that survive move to an older area that is cleaned less often."

**Let's understand it fully:**

**Step 1 — What garbage collection is.**
You don't free memory by hand in Dart. The GC automatically finds objects you no longer use and frees them. This prevents most memory bugs.

**Step 2 — The key idea: "most objects die young."**
In real apps, most objects are created and thrown away very fast (especially Flutter widgets, which are rebuilt constantly). Dart's GC is designed around this:
- **Young area (new space):** new objects go here. It is cleaned quickly and often (cheap).
- **Old area (old space):** objects that survive a while get moved here. It is cleaned less often.

This is called generational GC — separating "young" (short-lived) from "old" (long-lived) objects.

**Step 3 — Why this matters for Flutter.**
Flutter creates a huge number of short-lived widget objects every frame. Because cleaning the young area is cheap, this is okay by design — it's a big reason rebuilding widgets is acceptable.

**Step 4 — The practical rule.**
GC still takes a tiny bit of time. If you create lots of objects inside `build()` or inside scroll/animation callbacks (which run 60–120 times per second), the cleanup adds up and can cause small freezes (jank). So avoid heavy object creation in these "hot paths."

```dart
// Wrong: creating a new heavy object on every build/frame
Widget build(BuildContext context) {
  final formatter = DateFormat('yyyy-MM-dd'); // made every rebuild
  return Text(formatter.format(date));
}

// Better: create it once and reuse it
static final _formatter = DateFormat('yyyy-MM-dd');
```

**Why interviewers ask:** To connect memory behavior to a real Flutter rule — don't allocate heavily in hot paths.

**Follow-ups they may ask:**
- *"What triggers a GC?"* → Mostly when the young area fills up. You can't control GC directly, but you control how many objects you create.
- *"Can Dart still leak memory?"* → Yes — if you hold references you don't need (uncancelled stream subscriptions, listeners, big objects in closures). GC can't free what is still referenced.

**Related:** [Q25 — Dart VM](#q25) · [Q3 — const reduces allocations](#q3)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**`final` vs `const`**

| | `final` | `const` |
|---|---|---|
| Set when | once, runtime is fine | compile time (before running) |
| Contents | can change inside (e.g. a list) | fully frozen |
| Memory | a new object each time | the same object is reused |

**`extends` vs `implements` vs `with`**

| | What you get | How many |
|---|---|---|
| `extends` | the parent's code | one |
| `implements` | only the rules (rewrite all) | many |
| `with` (mixin) | reusable behavior | many |

**`Future` vs `Stream`**

| `Future` | `Stream` |
|---|---|
| one value, once | many values over time |
| `await` / `.then()` | `listen()` / `await for` |
| `FutureBuilder` | `StreamBuilder` |

**`sync*` vs `async*`**

| `sync*` | `async*` |
|---|---|
| returns an `Iterable` | returns a `Stream` |
| lazy — pulled when asked | pushed over time |

**JIT vs AOT**

| JIT (debug) | AOT (release) |
|---|---|
| compile while running | compile before running |
| enables hot reload | fast startup, smooth |
| development | production |

## One-line reminders

- **Null safety** = a variable can't be null unless you allow it with `?`. Every `!` is a risky promise. ([Q1](#q1))
- **`final`** locks the box (set once); **`const`** freezes everything and reuses the same object. ([Q2](#q2), [Q3](#q3))
- **`==` and `hashCode`** must always be overridden together, using fields that don't change. ([Q4](#q4))
- **`extends`** = inherit code (one). **`implements`** = follow rules, write all code (many). **`with`** = add behavior. ([Q12](#q12))
- **Factory** constructor can return a cached object or a subtype; a normal one always makes a new object. ([Q11](#q11))
- **Records** = quick value bags. **Patterns** = match shape + unpack. **Sealed** classes = "handle every case" safety. ([Q16](#q16), [Q17](#q17), [Q18](#q18))
- **`await` does NOT freeze the app** — it pauses one function and lets other work continue. ([Q19](#q19))
- **Microtasks (VIP) run before events (normal)** → output `1, 4, 3, 2`. ([Q20](#q20))
- **Single-subscription** stream = one listener; **broadcast** = many. Always cancel and close. ([Q21](#q21))
- **`sync*`** → lazy `Iterable`; **`async*`** → `Stream`. `yield` = one value; `yield*` = all from another. ([Q22](#q22))
- **Isolates** = separate worker, separate memory, pass messages. Use for heavy CPU work, not network. ([Q23](#q23))
- **JIT** (debug) = hot reload; **AOT** (release) = fast native. Never test speed in debug. ([Q24](#q24))
- **Generational GC**: most objects die young, so cleanup is cheap. Don't allocate inside `build()`. ([Q26](#q26))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers rarely stop at one question. They keep digging to test your depth. Practice answering this chain out loud — calmly, step by step:

1. *"What is the difference between `final` and `const`?"* → set once (runtime ok) vs known before running (frozen).
2. *"Then why does `const` help Flutter?"* → const objects are reused in memory, so Flutter skips rebuilding them.
3. *"How does Flutter know it can skip?"* → it's the same object as before, so the widget doesn't need to update.
4. *"What if one value is decided at runtime?"* → then it can't be `const`; keep the changing part separate and make the rest `const`.
5. *"How would you prove the rebuild was skipped?"* → use Flutter DevTools, "Track Widget Rebuilds".

Being able to calmly go step by step like this — without guessing — is exactly what makes you sound **senior**, in both remote and BD interviews.

[↑ Back to top](#toc)

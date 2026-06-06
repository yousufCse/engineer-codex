# Section 13 — Software Architecture Patterns

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a detailed, step-by-step explanation with real-life examples, diagrams, and code.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For architecture, draw the layers (even with words) and explain the **direction of dependencies**. Senior interviews are won by explaining *why* a structure exists, not just naming it.

---

<a id="toc"></a>

## Table of Contents

**A. Layers & separation**
1. [Layered Architecture](#q1) · *Very common*
2. [Clean Architecture — 3 layers & the dependency rule](#q2) · *Very common*
3. [Separation of Concerns](#q3) · *Very common*

**B. UI architecture patterns (MVx)**
4. [MVC — Model-View-Controller](#q4) · *Common*
5. [MVVM — and how BLoC/Cubit map to it](#q5) · *Very common*
6. [MVP — and how it differs from MVVM](#q6) · *Common*

**C. Core building blocks**
7. [Repository Pattern](#q7) · *Very common*
8. [Use Case / Interactor](#q8) · *Common*
9. [Dependency Injection (`get_it`)](#q9) · *Very common*
10. [Service Locator vs Dependency Injection](#q10) · *Common*
11. [Event-driven architecture & BLoC](#q11) · *Common*

**D. Scaling & choosing**
12. [Monorepo vs Multi-repo](#q12) · *Common*
13. [Modular architecture (feature packages)](#q13) · *Common*
14. [How to choose an architecture](#q14) · *Very common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

Follow these stages in order. Tick a stage off only when you can give the **short answer** and draw the layers, without looking.

**Stage 1 — The foundation (start here).**
→ [Q1 Layered](#q1) · [Q2 Clean Architecture](#q2) · [Q3 Separation of concerns](#q3)

**Stage 2 — UI patterns interviewers love.**
→ [Q5 MVVM](#q5) · [Q4 MVC](#q4) · [Q6 MVP](#q6)

**Stage 3 — The building blocks.**
→ [Q7 Repository](#q7) · [Q9 Dependency injection](#q9) · [Q8 Use case](#q8) · [Q11 Event-driven](#q11)

**Stage 4 — Trade-offs & scale.**
→ [Q10 Service locator vs DI](#q10) · [Q12 Monorepo](#q12) · [Q13 Modular](#q13) · [Q14 Choosing](#q14)

**Short on time (1 hour before the interview)?** Review these six:
[Q1](#q1) · [Q2](#q2) · [Q5](#q5) · [Q7](#q7) · [Q9](#q9) · [Q14](#q14), then read the [Cheat Sheet](#cheatsheet).

---

# A. Layers & separation

---

<a id="q1"></a>
## 1. What is Layered Architecture, and what are the typical layers in a mobile app?

> Very common · Medium

**Short answer (say this):**
"Layered architecture splits the app into horizontal layers, each with one job, where a layer only talks to the layer directly below it. In a mobile app the layers are usually Presentation (UI), Domain/Application (business logic), and Data (APIs, database). It keeps concerns separate so each layer can change and be tested independently."

**Let's understand it fully:**

**Step 1 — A real-life picture: floors of a building.**
A building has floors. Each floor does its own thing and only connects to the floor right below it through fixed stairs — not by drilling random holes. Layers work the same way.

**Step 2 — The typical layers.**

```
+----------------------------------+
|       Presentation Layer         |  UI: widgets, screens, state management
+----------------------------------+
|     Domain / Application Layer   |  business rules, use cases
+----------------------------------+
|           Data Layer             |  APIs, database, cache
+----------------------------------+
```

The rule: upper layers depend on lower ones, never the reverse. The UI calls business logic, which calls data — not the other way around.

**Step 3 — Why split into layers.**
- **Separation** — UI code doesn't mix with database code.
- **Testability** — you can test business logic without the UI.
- **Replaceability** — swap the data source (REST → GraphQL) without touching the UI.

**Step 4 — A small example of the flow.**
A button tap (Presentation) → calls a use case (Domain) → which asks a repository (Data) → returns up through the layers to update the UI.

**Why interviewers ask:** It's the base idea behind Clean Architecture and most app structures. They want to see you keep UI, logic, and data apart.

**Common mistake:** Letting the UI talk directly to the database or API (skipping layers), which tangles everything together.

**Follow-ups they may ask:**
- *"How is this different from Clean Architecture?"* → Clean Architecture is a stricter layered design with a specific dependency rule ([Q2](#q2)).

**Related:** [Q2 — Clean Architecture](#q2) · [Q3 — separation of concerns](#q3)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. Explain Clean Architecture in Flutter — the 3 layers and the dependency rule.

> Very common · Medium–Hard

**Short answer (say this):**
"Clean Architecture splits the app into Presentation, Domain, and Data layers, with one strict rule: dependencies point inward, toward the Domain. The Domain is the center — pure business logic with no Flutter or package imports. Presentation and Data both depend on Domain, but Domain depends on nothing. This makes the core logic stable and easy to test."

**Let's understand it fully:**

**Step 1 — A real-life picture: an onion with the rules in the center.**
The most important, most stable thing (your business rules) sits in the center. Outer layers (UI, database) can change often, but they can't force the center to change. Everything points inward.

**Step 2 — The three layers.**

```
        +-------------------------+
        |   Presentation (UI)     |  widgets, BLoC/Cubit  ─┐
        +-------------------------+                         │ depend on
        |        Domain           |  entities, use cases,   │ (inward)
        |     (the center)        |  repository interfaces ←┘
        +-------------------------+                         │
        |         Data            |  repository impls,      │ depend on
        |                         |  API, database         ─┘ (inward)
        +-------------------------+
```

- **Domain** — entities, use cases, and repository *interfaces*. Pure Dart, no Flutter, no packages.
- **Data** — concrete repository *implementations*, API clients, database, models (`fromJson`).
- **Presentation** — widgets and state management (BLoC, Riverpod).

**Step 3 — The dependency rule: point inward.**
The key trick is that the Domain defines a repository *interface*, and the Data layer *implements* it. So the Domain never imports the Data layer — it only knows the interface.

```dart
// DOMAIN layer — pure, no Flutter, no API code
abstract class UserRepository {        // interface lives in Domain
  Future<User> getUser(String id);
}

class GetUser {                        // a use case
  final UserRepository repo;
  GetUser(this.repo);
  Future<User> call(String id) => repo.getUser(id);
}

// DATA layer — implements the Domain's interface (points inward)
class UserRepositoryImpl implements UserRepository {
  final ApiClient api;
  UserRepositoryImpl(this.api);
  @override
  Future<User> getUser(String id) async => /* call api, map to User */ User(id);
}
```

**Step 4 — Why the Domain must not depend on Data or Presentation.**
The Domain is your business rules — the most valuable, longest-living code. If it depended on Flutter or a specific database, every UI or database change could break it. By keeping it pure, you can test it with plain Dart and reuse it anywhere.

**Step 5 — The trade-off.**
Clean Architecture adds boilerplate (interfaces, use cases, models vs entities). It shines on large, long-lived apps; for a tiny app it can be overkill ([Q14](#q14)).

**Why interviewers ask:** It's the standard "serious" Flutter architecture. They want to hear the *dependency rule* (inward) and *why* the Domain is pure.

**Common mistake:** Importing Flutter or API/database code in the Domain layer — that breaks the whole point. Also, applying it to a trivial app where it's just overhead.

**Follow-ups they may ask:**
- *"Entity vs Model?"* → Entity = pure Domain object. Model = Data-layer object with `fromJson`/`toJson` that maps to/from the entity.
- *"Where do use cases go?"* → In the Domain layer ([Q8](#q8)).

**Related:** [Q1 — layered](#q1) · [Q7 — repository](#q7) · [Q8 — use case](#q8) · [Q14 — choosing](#q14)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. What is "Separation of Concerns"? Give a Flutter example of a violation and the fix.

> Very common · Medium

**Short answer (say this):**
"Separation of concerns means each part of the code handles one concern — UI, business logic, or data — and they don't mix. A common violation is calling the network and parsing JSON directly inside a widget's `build` method. The fix is to move that work into a repository and keep the widget focused on showing UI."

**Let's understand it fully:**

**Step 1 — The idea.**
A "concern" is one responsibility: drawing UI, deciding business rules, or fetching data. Mixing them makes code hard to read, test, and change.

**Step 2 — A violation: everything in the widget.**

```dart
// Bad: the widget fetches, parses, AND displays — three concerns mixed
class UserScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: http.get(Uri.parse('https://api/user')), // networking in UI
      builder: (context, snapshot) {
        final json = jsonDecode(snapshot.data!.body);   // parsing in UI
        return Text(json['name']);                       // display
      },
    );
  }
}
```

This is impossible to test without a real network, and the UI is tangled with data logic.

**Step 3 — The fix: each concern in its own place.**

```dart
// Data concern — a repository
class UserRepository {
  final ApiClient api;
  UserRepository(this.api);
  Future<User> getUser() async => User.fromJson(await api.get('/user'));
}

// Logic/state concern — a Cubit
class UserCubit extends Cubit<UserState> {
  final UserRepository repo;
  UserCubit(this.repo) : super(UserLoading());
  Future<void> load() async => emit(UserLoaded(await repo.getUser()));
}

// UI concern — only displays
class UserScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) =>
      BlocBuilder<UserCubit, UserState>(builder: (c, s) => /* show s */ Text('...'));
}
```

**Step 4 — Why it matters.**
Now the data layer is testable on its own, the logic is testable on its own, and the UI just renders. A change in one concern doesn't ripple into the others.

**Why interviewers ask:** It's the practical heart of every architecture pattern. They want to see you keep UI free of networking/parsing.

**Common mistake:** Putting business logic and network calls inside widgets, making them untestable and bloated.

**Follow-ups they may ask:**
- *"How does this relate to SRP?"* → Separation of concerns is SRP applied across the whole app, not just one class.

**Related:** [Q1 — layered](#q1) · [Q2 — Clean Architecture](#q2) · [Q7 — repository](#q7)

[↑ Back to top](#toc)

---

# B. UI architecture patterns (MVx)

---

<a id="q4"></a>
## 4. What is MVC (Model-View-Controller)?

> Common · Medium

**Short answer (say this):**
"MVC splits an app into three parts: the Model holds data and rules, the View shows the UI, and the Controller handles input and updates the Model and View. The goal is to keep the UI separate from the data. In Flutter, pure MVC is less common because Flutter's reactive widgets blur the View/Controller line."

**Let's understand it fully:**

**Step 1 — A real-life picture: a restaurant.**
- **Model** = the kitchen (food and recipes — the data and rules).
- **View** = the dining area (what the customer sees).
- **Controller** = the waiter (takes your order, tells the kitchen, brings the food).

**Step 2 — The three parts and how they talk.**

```
   input        updates
View  ───────►  Controller  ───────►  Model
  ▲                                     │
  └──────────── reads data ─────────────┘
```

The Controller takes user input, updates the Model, and the View shows the Model's data.

**Step 3 — Why MVC is less natural in Flutter.**
Flutter widgets are reactive — they rebuild from state. So the "View" and "Controller" roles often merge, and most Flutter teams use MVVM or BLoC instead ([Q5](#q5)). MVC is still very common on the web and in older mobile frameworks, so interviewers may ask it.

**Why interviewers ask:** It's the classic UI pattern; they check you know the three roles and can compare it to MVVM.

**Common mistake:** Putting business logic in the View (UI). In MVC, logic belongs in the Model/Controller.

**Follow-ups they may ask:**
- *"MVC vs MVVM?"* → MVVM adds a ViewModel that exposes ready-to-show state and removes the View's need to know the Model directly ([Q5](#q5)).

**Related:** [Q5 — MVVM](#q5) · [Q6 — MVP](#q6)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What is MVVM, and how do Cubit/BLoC map to it?

> Very common · Medium

**Short answer (say this):**
"MVVM is Model-View-ViewModel. The ViewModel sits between the UI and the data: it holds the screen's state and exposes it in a ready-to-display form, and the View just binds to it. In Flutter, a Cubit or BLoC acts as the ViewModel — it holds state, the widget rebuilds when the state changes."

**Let's understand it fully:**

**Step 1 — A real-life picture: a personal translator.**
The ViewModel is a translator between the raw data (Model) and the screen (View). The View doesn't talk to the messy data directly; it asks the translator for the clean, ready answer.

**Step 2 — The three parts.**

```
View (widget)  ◄── binds to ──  ViewModel (Cubit/BLoC)  ──► Model (repository)
   rebuilds on state change       holds & exposes state      data & rules
```

- **Model** — data and business rules (repositories, entities).
- **View** — the widget; it only displays state and sends user actions.
- **ViewModel** — holds the screen's state, talks to the Model, exposes clean state to the View.

**Step 3 — Cubit as a ViewModel (Flutter example).**

```dart
// Model
class CounterRepository { int load() => 0; }

// ViewModel
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);
  void increment() => emit(state + 1); // updates state; UI rebuilds
}

// View — just binds to the ViewModel
BlocBuilder<CounterCubit, int>(
  builder: (context, count) => Text('$count'),
);
```

The widget never holds the logic; it only shows `state` and calls `increment()`. That's MVVM.

**Step 4 — Why MVVM fits Flutter so well.**
Flutter is reactive: the UI rebuilds from state. A ViewModel (Cubit/BLoC/Riverpod notifier) holding that state is a perfect match. This is why MVVM-style architectures dominate Flutter.

**Why interviewers ask:** MVVM is the most common Flutter architecture pattern. They want to hear that BLoC/Cubit/Riverpod play the ViewModel role.

**Common mistake:** Putting business logic in the widget instead of the ViewModel, or letting the View read the Model directly.

**Follow-ups they may ask:**
- *"MVVM vs MVP?"* → In MVVM the View binds to state (reactive); in MVP the Presenter pushes updates to the View through an interface ([Q6](#q6)).

**Related:** [Q4 — MVC](#q4) · [Q6 — MVP](#q6) · [Q11 — event-driven BLoC](#q11)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What is MVP (Model-View-Presenter), and how is it different from MVVM?

> Common · Medium

**Short answer (say this):**
"MVP has a Presenter that does all the logic and tells a 'dumb' View exactly what to show, usually through a View interface. The main difference from MVVM: in MVP the Presenter pushes updates to the View directly; in MVVM the View binds to observable state and updates itself. MVVM is more reactive, which fits Flutter better."

**Let's understand it fully:**

**Step 1 — The three parts.**
- **Model** — data and rules.
- **View** — passive; just shows what it's told (often via an interface like `showLoading()`, `showUser()`).
- **Presenter** — holds all the logic; it talks to the Model and commands the View.

**Step 2 — How MVP works.**

```
View interface  ◄── commands (showUser) ──  Presenter  ──► Model
   (passive)                                  (logic)
```

The Presenter holds a reference to a View interface and calls methods on it.

```dart
abstract class UserView {
  void showLoading();
  void showUser(User user);
}

class UserPresenter {
  final UserView view;
  final UserRepository repo;
  UserPresenter(this.view, this.repo);

  Future<void> load() async {
    view.showLoading();
    view.showUser(await repo.getUser()); // Presenter pushes to the View
  }
}
```

**Step 3 — The key difference from MVVM.**
- **MVP** — the Presenter *pushes* updates to the View by calling its methods. The View is passive.
- **MVVM** — the View *pulls/binds* to observable state; when state changes, the framework rebuilds the View. No direct calls.

**Step 4 — Why Flutter prefers MVVM.**
Flutter's whole model is "rebuild from state," which is MVVM's binding style. MVP's manual `view.showX()` calls feel unnatural in a reactive framework, so MVP is more common in older Android (Java) apps.

**Why interviewers ask:** To check you understand the difference between *pushing* to the View (MVP) and *binding* to state (MVVM).

**Common mistake:** Saying MVP and MVVM are the same. The update direction (push vs bind) is the real difference.

**Follow-ups they may ask:**
- *"Which would you use in Flutter?"* → MVVM (BLoC/Cubit/Riverpod), because it matches Flutter's reactive rebuild model.

**Related:** [Q5 — MVVM](#q5) · [Q4 — MVC](#q4)

[↑ Back to top](#toc)

---

# C. Core building blocks

---

<a id="q7"></a>
## 7. What is the Repository Pattern, what problem does it solve, and how does it fit Clean Architecture?

> Very common · Medium

**Short answer (say this):**
"A repository is a class that hides where data comes from. The rest of the app asks the repository for data and doesn't care if it came from the network, a database, or a cache. It solves the problem of UI and logic being tied to a specific data source. In Clean Architecture, the Domain defines the repository interface and the Data layer implements it."

**Let's understand it fully:**

**Step 1 — A real-life picture: a librarian.**
You ask the librarian for a book. You don't know or care whether they got it from the shelf, the back room, or another branch. The repository is that librarian for your data.

**Step 2 — The problem it solves.**
Without a repository, your Cubit/BLoC would call the API directly and parse JSON — so it's glued to that API. If you add caching or switch APIs, you'd rewrite the logic. A repository hides all that behind one clean method.

**Step 3 — The structure (interface + implementation).**

```dart
// Domain layer: the interface (what, not how)
abstract class UserRepository {
  Future<User> getUser(String id);
}

// Data layer: the implementation (decides the source)
class UserRepositoryImpl implements UserRepository {
  final ApiClient api;
  final LocalCache cache;
  UserRepositoryImpl(this.api, this.cache);

  @override
  Future<User> getUser(String id) async {
    final cached = cache.get(id);
    if (cached != null) return cached;        // from cache
    final user = await api.fetchUser(id);     // or from network
    cache.save(id, user);
    return user;
  }
}
```

The caller just does `repo.getUser(id)` — the cache-then-network decision is hidden.

**Step 4 — Why it fits Clean Architecture.**
The Domain owns the *interface* (so the Domain stays pure), and the Data layer provides the *implementation*. The Presentation layer depends only on the interface, so you can swap the implementation or inject a fake for tests.

**Why interviewers ask:** The repository is the most-used pattern in real Flutter apps. They want to see you separate "what data" from "where it comes from."

**Common mistake:** Putting API calls and JSON parsing directly in the Cubit/BLoC, skipping the repository — that couples your logic to one data source.

**Follow-ups they may ask:**
- *"How does it help testing?"* → You inject a fake repository, so you test logic without a real network.
- *"Single source of truth?"* → A repository can combine network + local DB and present one consistent view (offline-first).

**Related:** [Q2 — Clean Architecture](#q2) · [Q9 — DI](#q9) · [Q8 — use case](#q8)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is the Use Case (Interactor) pattern? When is it useful, and when is it overkill?

> Common · Medium

**Short answer (say this):**
"A use case is a class that does exactly one business action — like 'get user profile' or 'place order'. It sits in the Domain layer between the state management and the repository. It's useful for complex apps with real business rules, but on a simple CRUD app it can be just an extra layer that forwards a call, which is overkill."

**Let's understand it fully:**

**Step 1 — A real-life picture: one recipe.**
A use case is one specific recipe: "make a cappuccino." It knows the exact steps for that one action. Each business action gets its own use case.

**Step 2 — What it looks like.**
Often a class with a single `call` method, so it can be used like a function.

```dart
class GetUserProfile {
  final UserRepository repo;
  GetUserProfile(this.repo);

  Future<User> call(String id) {
    // could add business rules here: validation, combining sources, etc.
    return repo.getUser(id);
  }
}

// Used in the Cubit:
final user = await getUserProfile('123');
```

**Step 3 — When it's useful.**
- The action has real **business rules** (validation, combining several repositories, calculations).
- You want the logic **reusable** across screens.
- You want each action **testable** on its own.

**Step 4 — When it's overkill.**
If the use case just calls `repo.getUser(id)` and nothing else, it's an empty middle layer. For a simple app, the Cubit can call the repository directly. Don't add use cases just to follow a diagram (that's a YAGNI issue).

**Why interviewers ask:** It tests judgment — do you add structure for a reason, or blindly follow a template?

**Common mistake:** Adding a use case for every single repository call even when it does nothing, doubling the boilerplate for no benefit.

**Follow-ups they may ask:**
- *"Where does it live?"* → In the Domain layer, depending only on the repository interface.
- *"Why the `call` method?"* → It lets you invoke the object like a function: `getUser('123')`.

**Related:** [Q2 — Clean Architecture](#q2) · [Q7 — repository](#q7) · [Q14 — choosing](#q14)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What is Dependency Injection, why do we use it, and how does `get_it` implement it?

> Very common · Medium

**Short answer (say this):**
"Dependency Injection (DI) means a class receives the things it needs from outside, instead of creating them itself. We use it for low coupling and testability — you can swap a real dependency for a fake. `get_it` is a service locator that registers dependencies once at startup and hands them out wherever you need them."

**Let's understand it fully:**

**Step 1 — A real-life picture: plugging into a socket.**
A lamp doesn't build its own power plant; it plugs into a socket and receives power. A class shouldn't build its own database; it should receive one.

**Step 2 — Without DI vs with DI.**

```dart
// Without DI — the class builds its own dependency (hard-wired, hard to test)
class OrderService {
  final api = HttpApiClient();
}

// With DI — the dependency is passed in (swappable, testable)
class OrderService {
  final ApiClient api;
  OrderService(this.api); // injected
}
```

**Step 3 — How `get_it` works.**
`get_it` is a shared "toolbox": you register each dependency once at startup, then ask for it anywhere — no need to pass it through many constructors.

```dart
final sl = GetIt.instance;

void setup() {
  sl.registerLazySingleton<ApiClient>(() => HttpApiClient());
  sl.registerLazySingleton<UserRepository>(() => UserRepositoryImpl(sl()));
  sl.registerFactory(() => UserCubit(sl())); // new instance each time
}

// Use it anywhere:
final cubit = sl<UserCubit>();
```

- `registerLazySingleton` → one shared instance, created on first use.
- `registerFactory` → a new instance every time you ask.

**Step 4 — Why DI matters.**
- **Testability** — inject a fake `ApiClient` in tests; no real network.
- **Low coupling** — classes depend on interfaces, not concrete classes ([DIP](#q10)).
- **One place to wire** — change a dependency in the setup, not in 50 files.

**Why interviewers ask:** DI is essential for testable, layered apps. They want to see you don't hard-wire dependencies with `new` inside classes.

**Common mistake:** Calling `sl<X>()` deep inside business logic everywhere (hidden dependencies). Prefer injecting through constructors; use the locator at the edges.

**Follow-ups they may ask:**
- *"get_it vs Provider/Riverpod for DI?"* → `get_it` is a plain service locator (no `BuildContext`). Provider/Riverpod tie DI to the widget tree.
- *"Singleton vs factory registration?"* → Singleton = one shared instance; factory = fresh each call.

**Related:** [Q10 — service locator vs DI](#q10) · [Q7 — repository](#q7) · [Q2 — Clean Architecture](#q2)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What is the difference between a Service Locator and Dependency Injection? What are the trade-offs?

> Common · Medium–Hard

**Short answer (say this):**
"Both provide dependencies, but in opposite directions. With Dependency Injection, dependencies are *pushed in* through the constructor, so they're visible in the class's signature. With a Service Locator, the class *pulls* dependencies by asking a global registry. DI is more explicit and testable; a service locator is convenient but hides dependencies."

**Let's understand it fully:**

**Step 1 — The two styles.**

```dart
// Dependency Injection — dependency is visible in the constructor
class OrderService {
  final ApiClient api;
  OrderService(this.api); // you can SEE what it needs
}

// Service Locator — dependency is fetched from a global registry
class OrderService {
  final api = sl<ApiClient>(); // hidden need; you must read the body to know
}
```

**Step 2 — The trade-offs.**

| | Dependency Injection | Service Locator |
|---|---|---|
| Dependencies are | visible in the constructor | hidden inside the class |
| Testability | easy (pass a fake in) | harder (must set up the global registry) |
| Convenience | more wiring | very convenient |
| Coupling | low, explicit | couples to the locator |

**Step 3 — `get_it` is technically a service locator.**
Even though we call it "DI", `get_it` is a service locator — you pull from `sl<X>()`. Many teams get the best of both: register in `get_it`, but **inject** the resolved objects through constructors (so the classes themselves use DI, and only the setup uses the locator).

**Step 4 — The practical advice.**
Prefer constructor injection inside your classes (visible, testable). Use the service locator only at the "edges" (app setup, where you build the object graph). That keeps business classes clean while staying convenient.

**Why interviewers ask:** It's a senior judgment question — do you understand *why* explicit dependencies are better, even while using a locator?

**Common mistake:** Calling `sl<X>()` everywhere inside business logic, hiding what each class depends on and making tests painful.

**Follow-ups they may ask:**
- *"Is a service locator an anti-pattern?"* → Not inherently. It becomes one when used deep inside logic, hiding dependencies. At the composition root it's fine.

**Related:** [Q9 — DI / get_it](#q9) · [Q3 — separation of concerns](#q3)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What is event-driven architecture, and how does BLoC use this concept?

> Common · Medium

**Short answer (say this):**
"Event-driven means parts of the system communicate by sending and reacting to events, instead of calling each other directly. BLoC uses this: the UI sends events in, the BLoC processes them and emits states out. This one-way flow makes the logic predictable and easy to test."

**Let's understand it fully:**

**Step 1 — A real-life picture: a notice board.**
Instead of person A directly ordering person B, A pins a note (event) on a board. Whoever cares reacts to it. Parts stay loosely connected through events.

**Step 2 — BLoC's flow: events in, states out.**

```
UI  ──(add Event)──►  BLoC  ──(emit State)──►  UI rebuilds
```

The UI never changes state directly; it sends an event. The BLoC decides what new state to emit. The UI just rebuilds from the new state.

```dart
// Events (things that happen)
sealed class CounterEvent {}
class Increment extends CounterEvent {}

// BLoC: events in -> states out
class CounterBloc extends Bloc<CounterEvent, int> {
  CounterBloc() : super(0) {
    on<Increment>((event, emit) => emit(state + 1));
  }
}

// UI sends an event:
context.read<CounterBloc>().add(Increment());
```

**Step 3 — Why one-way flow helps.**
- **Predictable** — every state change starts from a clear event.
- **Testable** — give events, check the emitted states (no UI needed).
- **Traceable** — you can log every event and state for debugging.
- **Decoupled** — the UI doesn't know *how* state is produced.

**Step 4 — Cubit is the simpler cousin.**
Cubit drops the explicit events and exposes methods directly (`increment()`). Use Cubit for simple flows, full BLoC when you want the traceable event log.

**Why interviewers ask:** Event-driven, one-way data flow is the core idea behind BLoC, Redux, and Riverpod. They want to see you understand "events in, states out."

**Common mistake:** Mutating state directly from the UI instead of sending an event/calling a method, breaking the one-way flow.

**Follow-ups they may ask:**
- *"BLoC vs Cubit?"* → BLoC uses explicit events (more traceable); Cubit uses direct methods (simpler).

**Related:** [Q5 — MVVM](#q5) · [Q3 — separation of concerns](#q3)

[↑ Back to top](#toc)

---

# D. Scaling & choosing

---

<a id="q12"></a>
## 12. What are the trade-offs between Monorepo and Multi-repo for mobile teams?

> Common · Medium

**Short answer (say this):**
"A monorepo keeps all code in one repository; a multi-repo splits it across many. A monorepo makes sharing code and making cross-cutting changes easy, with one source of truth — but it can get big and needs good tooling. Multi-repo gives strong separation and independent releases, but sharing code and coordinating changes is harder."

**Let's understand it fully:**

**Step 1 — A real-life picture.**
- **Monorepo** = one big house where every room (project) shares the same address. Easy to move things between rooms.
- **Multi-repo** = separate houses. Strong boundaries, but moving things between them takes effort.

**Step 2 — The trade-offs.**

| | Monorepo | Multi-repo |
|---|---|---|
| Code sharing | easy (one place) | harder (publish packages) |
| Cross-cutting change | one commit/PR | many coordinated PRs |
| Boundaries | softer | strong, enforced |
| Independent release | harder | easy per repo |
| Tooling needed | more (e.g. `melos`) | simpler per repo |

**Step 3 — Monorepo in Flutter (`melos`).**
Flutter teams often use a monorepo with `melos` to manage multiple packages (a core package, feature packages, the app) in one repo — linking local packages and running scripts across all of them.

**Step 4 — How to choose.**
- **Monorepo** — one team or tightly related projects that share a lot of code.
- **Multi-repo** — separate teams that release independently and want hard boundaries.

**Why interviewers ask:** It's a scaling/team-structure question for senior roles. They want to hear the trade-offs, not a blanket "X is better."

**Common mistake:** Claiming one is always better. It depends on team size, release cadence, and how much code is shared.

**Follow-ups they may ask:**
- *"What is `melos`?"* → A tool to manage a Flutter monorepo: links local packages and runs commands across all of them.

**Related:** [Q13 — modular architecture](#q13) · [Q14 — choosing](#q14)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. What is modular architecture (feature packages) in Flutter, and why do large teams adopt it?

> Common · Medium

**Short answer (say this):**
"Modular architecture splits the app into separate packages — usually one per feature, plus shared core packages — instead of one big lib folder. Large teams adopt it because it gives clear boundaries, lets teams work in parallel without stepping on each other, enforces dependency rules, and speeds up builds and tests for a single feature."

**Let's understand it fully:**

**Step 1 — A real-life picture: Lego blocks.**
Instead of one giant glued statue, you build with separate blocks (features). Each block is self-contained and snaps into the app. You can change one block without touching the others.

**Step 2 — A typical structure.**

```
app/                  (the shell that wires features together)
packages/
  core/               (shared: networking, theming, utilities)
  domain/             (shared entities, repository interfaces)
  feature_auth/       (login feature — its own UI + logic)
  feature_profile/    (profile feature)
  feature_orders/     (orders feature)
```

A rule is usually enforced: feature packages may depend on `core`/`domain`, but **not on each other** — keeping features independent.

**Step 3 — Why large teams adopt it.**
- **Parallel work** — team A owns `feature_auth`, team B owns `feature_orders`, no conflicts.
- **Enforced boundaries** — the package system blocks a feature from importing another feature's internals.
- **Faster builds/tests** — test or build one feature without the whole app.
- **Reusability** — a feature package can be reused in another app.

**Step 4 — The cost.**
More setup and tooling (often a monorepo with `melos`). For a small app it's overhead; for a large multi-team app it's a big win.

**Why interviewers ask:** It's a senior/lead scaling topic. They want to hear about boundaries and parallel team work.

**Common mistake:** Letting feature packages depend on each other, which recreates the tangle you were trying to avoid.

**Follow-ups they may ask:**
- *"How do features communicate?"* → Through shared abstractions in `core`/`domain`, or a navigation/event layer in the app shell — not by importing each other directly.

**Related:** [Q12 — monorepo](#q12) · [Q2 — Clean Architecture](#q2) · [Q14 — choosing](#q14)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. How do you decide which architecture to use for a new Flutter project?

> Very common · Medium

**Short answer (say this):**
"I match the architecture to the project's size and lifespan. A tiny app gets a simple structure — Cubit plus a repository. A medium app gets layered MVVM with repositories and DI. A large, long-lived, multi-team app gets full Clean Architecture with modular feature packages. The rule is: enough structure to stay maintainable, but not so much that it slows you down."

**Let's understand it fully:**

**Step 1 — There is no single 'best' architecture.**
The right choice depends on size, team, and how long the app will live. Over-architecting a small app wastes time; under-architecting a big app creates chaos.

**Step 2 — A simple decision guide.**

| Project | Suggested approach |
|---|---|
| Prototype / tiny app | `setState` or a simple Cubit + a repository |
| Medium app | Layered MVVM: UI → Cubit/BLoC → repository, with DI ([Q9](#q9)) |
| Large / long-lived | Clean Architecture ([Q2](#q2)) + use cases + DI |
| Large multi-team | Clean Architecture + modular feature packages ([Q13](#q13)) |

**Step 3 — Questions I ask before choosing.**
- How big and long-lived is the app?
- How many people/teams will work on it?
- How complex are the business rules?
- How important is testability and offline support?

**Step 4 — Start simple, evolve.**
You can begin with a simple structure and add layers (use cases, modular packages) as the app grows. Adding structure later is fine; ripping out over-engineering is painful. This is YAGNI applied to architecture.

**Why interviewers ask:** It tests real-world judgment — the senior skill of fitting the solution to the problem rather than cargo-culting a pattern.

**Common mistake:** Applying full Clean Architecture to a 3-screen app (boilerplate overload), or having no structure on a large app (spaghetti).

**Follow-ups they may ask:**
- *"When is Clean Architecture overkill?"* → Small, short-lived apps with simple logic — the extra interfaces and use cases add cost with little benefit.
- *"Can you change architecture mid-project?"* → Yes, incrementally — introduce repositories first, then DI, then use cases as complexity grows.

**Related:** [Q2 — Clean Architecture](#q2) · [Q13 — modular](#q13) · [Q8 — use case (overkill?)](#q8)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## Clean Architecture layers

| Layer | Holds | Depends on |
|---|---|---|
| Presentation | widgets, BLoC/Cubit | Domain |
| Domain (center) | entities, use cases, repo interfaces | nothing (pure Dart) |
| Data | repo impls, API, DB, models | Domain |

Rule: **dependencies point inward, toward the Domain.**

## UI patterns compared

| Pattern | Update style | Flutter fit |
|---|---|---|
| MVC | Controller updates Model & View | weak (roles blur) |
| MVP | Presenter pushes to a passive View | older Android |
| MVVM | View binds to observable state | strong (BLoC/Cubit/Riverpod) |

## Service Locator vs DI

| | DI (constructor) | Service Locator |
|---|---|---|
| Dependencies | visible | hidden |
| Testability | easy | harder |
| Best used | inside classes | at app setup only |

## One-line reminders

- **Layered**: UI → Domain → Data; a layer only talks to the one below. ([Q1](#q1))
- **Clean Architecture**: Domain is pure and central; dependencies point inward. ([Q2](#q2))
- **Separation of concerns**: no networking/parsing inside widgets. ([Q3](#q3))
- **MVVM** = ViewModel (Cubit/BLoC) holds state; the View binds to it. ([Q5](#q5))
- **MVP pushes** to the View; **MVVM binds** to state. ([Q6](#q6))
- **Repository** hides where data comes from (network/cache/db). ([Q7](#q7))
- **Use case** = one business action; skip it when it just forwards a call. ([Q8](#q8))
- **DI** = pass dependencies in (testable); **get_it** is a service locator. ([Q9](#q9), [Q10](#q10))
- **BLoC** = events in, states out (one-way, testable flow). ([Q11](#q11))
- **Monorepo** = easy sharing, needs tooling; **multi-repo** = strong boundaries, independent release. ([Q12](#q12))
- **Modular packages** = clear boundaries + parallel team work for large apps. ([Q13](#q13))
- **Choose by size**: simple app → Cubit+repo; large app → Clean + modular. Don't over-engineer. ([Q14](#q14))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers push from "name a pattern" to "design a real app." Practice out loud:

1. *"How would you structure a medium Flutter app?"* → layered MVVM: UI → Cubit → repository, with DI.
2. *"Where does the API call go?"* → in the repository (Data layer), never the widget.
3. *"How do you test the logic?"* → inject a fake repository into the Cubit; no real network.
4. *"The app grows to 5 teams — now what?"* → split into feature packages (modular), enforce boundaries, use a monorepo with melos.
5. *"Isn't Clean Architecture overkill for a small app?"* → yes; match the structure to size — start simple, add layers as it grows.

Explaining the *direction of dependencies* and *why* each layer exists is what separates a senior answer from a memorized one — in both remote and BD interviews.

[↑ Back to top](#toc)

# Section 3 — State Management

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

**A. The basics every interview starts with**
1. [What is "state"? Ephemeral vs app state](#q1) · *Very common*
2. [How `setState` works (and when NOT to use it)](#q2) · *Very common*
3. [`StatefulWidget` lifecycle (where state lives)](#q3) · *Common*
4. [Lifting state up & passing callbacks down](#q4) · *Common*

**B. The foundation: InheritedWidget & Provider**
5. [`InheritedWidget` & `updateShouldNotify`](#q5) · *Common*
6. [Provider — ChangeNotifier, Consumer, Selector, ProxyProvider](#q6) · *Very common*
7. [`context.watch` vs `read` vs `select`](#q7) · *Very common*

**C. The BLoC family**
8. [The BLoC pattern — events, states, streams](#q8) · *Very common*
9. [Cubit vs BLoC — when to use each](#q9) · *Very common*
10. [`BlocBuilder` vs `BlocListener` vs `BlocConsumer`](#q10) · *Very common*
11. [`buildWhen` & `listenWhen` (performance)](#q11) · *Common*
12. [`emit()` vs `setState()` & "emit after close"](#q12) · *Common*

**D. Riverpod & GetX**
13. [Riverpod — why it beats Provider, provider types, ref methods](#q13) · *Very common*
14. [GetX — controllers, `Obx`, `GetBuilder`, trade-offs](#q14) · *Common*

**E. Architecture & senior decisions**
15. [Modelling state with a sealed union (loading / success / error)](#q15) · *Very common*
16. [Sharing state between two unrelated screens](#q16) · *Common*
17. [How to choose a state management solution](#q17) · *Very common*
18. [Testing BLoC / Cubit logic](#q18) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 18 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — Core fundamentals (start here).** Almost every interview begins here.
→ [Q1 What is state](#q1) · [Q2 setState](#q2) · [Q3 Lifecycle](#q3) · [Q4 Lifting state up](#q4)

**Stage 2 — The foundation (how everything works underneath).**
→ [Q5 InheritedWidget](#q5) · [Q6 Provider](#q6) · [Q7 watch/read/select](#q7)

**Stage 3 — The BLoC family (the most common production pattern in BD jobs).**
→ [Q8 BLoC pattern](#q8) · [Q9 Cubit vs BLoC](#q9) · [Q10 Builder/Listener/Consumer](#q10) · [Q12 emit vs setState](#q12)

**Stage 4 — Modern tools & clean state.**
→ [Q13 Riverpod](#q13) · [Q15 Sealed union states](#q15) · [Q11 buildWhen/listenWhen](#q11) · [Q14 GetX](#q14)

**Stage 5 — Senior signal (architecture & testing, do last).**
→ [Q16 Sharing state across screens](#q16) · [Q17 Choosing a solution](#q17) · [Q18 Testing BLoC/Cubit](#q18)

**Short on time (1 hour before the interview)?** Just review these eight:
[Q1](#q1) · [Q2](#q2) · [Q6](#q6) · [Q7](#q7) · [Q8](#q8) · [Q9](#q9) · [Q15](#q15) · [Q17](#q17), then read the [Cheat Sheet](#cheatsheet).

---

# A. The basics every interview starts with

---

<a id="q1"></a>
## 1. What is "state" in Flutter? What is the difference between ephemeral and app state?

> Very common · Easy

**Short answer (say this):**
"State is any data that can change and that the screen shows. Flutter splits it into two kinds: ephemeral state, which only one widget cares about — like which tab is open — and app state, which many screens share — like the logged-in user or a shopping cart. The simple test is: 'Who else needs this data?' If only this widget, it's ephemeral; if other screens too, it's app state."

**Let's understand it fully:**

**Step 1 — State just means "data that can change."**
A widget draws itself from some data. When that data changes, the widget redraws. That changing data is the state. A text label, a checkbox value, a list of products — all of these are state.

**Step 2 — Ephemeral state = belongs to one widget only.**
"Ephemeral" means short-lived and private. Think of it like notes you scribble on your own desk — nobody else needs them. Examples: the open tab in a `BottomNavigationBar`, the current page in a `PageView`, whether a dropdown is open.

```dart
// Only this widget cares whether the FAQ is expanded.
class _FaqTileState extends State<FaqTile> {
  bool _isExpanded = false; // ephemeral state, kept right here

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => setState(() => _isExpanded = !_isExpanded),
      child: Column(children: [
        const Text('Question'),
        if (_isExpanded) const Text('Answer details...'),
      ]),
    );
  }
}
```

**Step 3 — App state = shared across the app.**
This is data that many screens read, or that must survive when you move between screens. Think of it like a noticeboard in a shared office — everyone reads from the same board. Examples: the logged-in user, a shopping cart, theme preference, unread-message count.

```dart
// Many screens need the cart, so it must live ABOVE all of them
// (managed with Provider, Riverpod, or BLoC) — not inside one widget.
```

**Step 4 — The boundary is not always sharp.**
The same piece of data can change category. A "selected tab" starts ephemeral, but if a deep link must restore that tab when the app reopens, it becomes app state. So don't memorize a fixed list — always ask the one question that matters.

**Step 5 — The one question to always ask.**
"Who else needs this data?" If the answer is "only this widget," keep it ephemeral with `setState`. If the answer is "other screens, or it must survive navigation," lift it into app state with a proper state manager.

**Why interviewers ask:** If you can't classify state, you will either over-engineer a simple toggle with BLoC, or under-engineer shared login state with `setState`. They want to see you pick the right size of tool.

**Common mistake:** Saying "just use Provider for everything" or "`setState` is bad." Both are wrong. `setState` is exactly right for ephemeral state; the mistake is only using it for data that must be shared.

**Follow-ups they may ask:**
- *"Give an example that could be either."* → A selected tab: ephemeral normally, but app state if a deep link must restore it.
- *"Where does app state physically live?"* → Above all the screens that need it, or outside the widget tree (Riverpod), so every screen reads the same copy.

**Related:** [Q2 — how setState works](#q2) · [Q16 — sharing state across screens](#q16) · [Q17 — choosing a solution](#q17)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. How does `setState` work internally? When should you NOT use it?

> Very common · Medium

**Short answer (say this):**
"`setState` does two things: it runs my little function to change the data, then it marks this widget as 'dirty' so Flutter rebuilds it on the next frame. It's the right tool for state that lives in one widget. I avoid it when state must be shared across screens, when it would rebuild a huge subtree for one tiny change, or when I'm setting state after an `await` and the widget might already be gone."

**Let's understand it fully:**

**Step 1 — The "raise your hand" idea.**
Think of `setState` like a student raising their hand to say "I need to be redrawn." The teacher (Flutter) doesn't redraw instantly — it notes the hand, finishes the current moment, then on the next frame redraws everyone who raised a hand. So `setState` schedules a rebuild; it doesn't redraw on the spot.

**Step 2 — The exact internal sequence.**
When you call `setState(fn)`:

1. Your function `fn` runs **right away** (synchronously) — this is where you change your variables.
2. Flutter marks this widget's element as **dirty** by calling `markNeedsBuild()`.
3. The framework schedules a new frame (if one isn't already scheduled).
4. On the next frame, `build()` runs again for this widget and its subtree.
5. Flutter compares the new widget tree with the old one and updates only the parts that actually changed on screen.

```
setState(fn)
   |
   v
run fn() now            <- your data changes happen here
   |
   v
markNeedsBuild()        <- this element is flagged "dirty"
   |
   v
a new frame is scheduled
   |
   v
next frame: build() runs again
   |
   v
old tree vs new tree compared -> only real changes hit the screen
```

**Step 3 — A concrete counter.**

```dart
class _CounterPageState extends State<CounterPage> {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++; // step 1: runs now; _count is already updated
    });
    // steps 2–5 happen automatically on the next frame
  }

  @override
  Widget build(BuildContext context) {
    // this WHOLE method re-runs on every setState call
    return Column(children: [
      Text('$_count'),
      ElevatedButton(onPressed: _increment, child: const Text('+')),
      // if 200 heavy widgets sat here, all of them would rebuild too
    ]);
  }
}
```

**Step 4 — When NOT to use `setState`.**
- **Shared state:** if a sibling, a far-away ancestor, or another screen needs the same data, `setState` forces you to lift state up awkwardly and pass callbacks down many layers.
- **Big subtree, tiny change:** if `setState` sits high in a deep tree but only a leaf changed, you rebuild hundreds of widgets for nothing. Push the state down, or use a scoped tool.
- **Async after the widget is gone:** if you `await` something, then `setState` after the user left the screen, you get `setState() called after dispose()`. Guard it with a `mounted` check.
- **Business logic in the UI:** `setState` tempts you to put login or API logic right in the widget, which is hard to test. Keep logic out of the UI.

```dart
Future<void> _load() async {
  final data = await api.fetch();
  if (!mounted) return;        // guard: the widget may be disposed now
  setState(() => _data = data);
}
```

**Why interviewers ask:** Knowing that `setState` marks the element dirty and triggers a full `build()` on the subtree shows you understand the rebuild pipeline — and whether you write performant code.

**Common mistake:** Changing the variable outside the closure (`_count++; setState(() {});`). It works, but it hides the intent — put the change inside the closure. Also: calling `setState` inside `build()` (infinite loop) or inside `initState` (error).

**Follow-ups they may ask:**
- *"Does `setState` rebuild instantly?"* → No. It marks the widget dirty and rebuilds on the next frame.
- *"What is `mounted`?"* → A flag on `State` that is `false` after dispose. Check it before `setState` following an `await`.

**Related:** [Q1 — what is state](#q1) · [Q3 — lifecycle](#q3) · [Q12 — emit vs setState](#q12)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. Walk me through the `StatefulWidget` lifecycle. Where does state actually live?

> Common · Medium

**Short answer (say this):**
"A `StatefulWidget` itself is throwaway and rebuilt often, so the real state lives in its separate `State` object, which Flutter keeps alive across rebuilds. The key lifecycle steps are `initState` (set things up once), `didChangeDependencies`, `build` (runs many times), `didUpdateWidget` (parent gave new inputs), and `dispose` (clean up). I create controllers and subscriptions in `initState` and free them in `dispose`."

**Let's understand it fully:**

**Step 1 — Why state lives in a separate object.**
A widget is just a lightweight description and is rebuilt constantly. If your data lived inside the widget, it would be wiped on every rebuild. So Flutter splits it: the `StatefulWidget` is the throwaway recipe, and the `State` object is the long-lived kitchen that actually holds the data. Flutter keeps the same `State` object alive even as the widget is rebuilt.

**Step 2 — The lifecycle in order.**

```dart
class _ProfilePageState extends State<ProfilePage> {
  late final TextEditingController _controller;

  @override
  void initState() {
    super.initState();
    // runs ONCE when the State is created — set up controllers, subscriptions
    _controller = TextEditingController();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // runs after initState, and again if an InheritedWidget we depend on changed
  }

  @override
  void didUpdateWidget(ProfilePage oldWidget) {
    super.didUpdateWidget(oldWidget);
    // parent rebuilt and gave us NEW inputs — react to changed widget fields
    if (oldWidget.userId != widget.userId) {
      // reload for the new user
    }
  }

  @override
  Widget build(BuildContext context) {
    // runs MANY times — keep it cheap, no setup or network calls here
    return TextField(controller: _controller);
  }

  @override
  void dispose() {
    _controller.dispose();   // clean up to avoid leaks
    super.dispose();         // call super LAST
  }
}
```

**Step 3 — The golden rule: set up in `initState`, clean up in `dispose`.**
Anything that holds a resource — a `TextEditingController`, an `AnimationController`, a `StreamSubscription`, a timer — must be created in `initState` and freed in `dispose`. Forgetting `dispose` is one of the most common memory leaks in Flutter.

**Step 4 — `build` vs `didUpdateWidget`.**
People mix these up. `build` runs on every rebuild and should be cheap. `didUpdateWidget` runs only when the parent passes **new input values** to this widget — use it to react to a changed input, like reloading when `userId` changes.

**Step 5 — Why the `widget` field matters.**
Inside `State`, you read the widget's inputs through `widget.something` (for example `widget.userId`). Because the `State` outlives many widget instances, `widget` always points at the latest one — that's how the long-lived State sees fresh inputs.

**Why interviewers ask:** It proves you understand the widget/element/state split, and whether you clean up resources properly — a frequent source of production bugs.

**Common mistake:** Putting setup code or network calls in `build` (runs too often), or forgetting to `dispose` controllers and subscriptions. Also calling `super.dispose()` first instead of last.

**Follow-ups they may ask:**
- *"Where do you start a network call?"* → `initState` for a one-time load, never in `build`.
- *"What is `mounted`?"* → It tells you whether the `State` is still attached. Check it before `setState` after an `await`. (See [Q2](#q2).)

**Related:** [Q2 — setState](#q2) · [Q5 — InheritedWidget & didChangeDependencies](#q5)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. What does "lifting state up" mean, and why does it stop scaling?

> Common · Easy–Medium

**Short answer (say this):**
"Lifting state up means moving shared state to the nearest common parent of the widgets that need it, then passing the data down and passing callbacks up. It's the simplest way to share state between a few close widgets. It stops scaling because, as the tree grows, you end up threading data and callbacks through many widgets that don't even use them — that pain is exactly why Provider, Riverpod, and BLoC exist."

**Let's understand it fully:**

**Step 1 — The idea: move state to a shared parent.**
If two sibling widgets need the same value, neither can own it, because siblings can't see each other. So you move the value up to their common parent. The parent owns the state, hands the value **down** to children, and the children send changes **up** through callbacks.

```dart
class _ParentState extends State<Parent> {
  int _count = 0; // the shared state lives in the common parent

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      CountLabel(count: _count),                       // data goes DOWN
      IncrementButton(
        onPressed: () => setState(() => _count++),     // change comes UP
      ),
    ]);
  }
}
```

**Step 2 — Why this is good for small cases.**
There is no extra package, no magic, and the data flow is obvious: down through constructors, up through callbacks. For two or three close widgets, this is the right, simplest answer.

**Step 3 — Why it stops scaling (prop drilling).**
Now imagine the value is needed five layers deep. Every widget in between must accept it and pass it on, even though it never uses it. This is called "prop drilling," and it's painful:

```dart
// Screen -> Section -> Card -> Row -> finally the widget that needs 'user'
Section(user: user)        // Section doesn't use user, just forwards it
  -> Card(user: user)      // Card doesn't use it either
    -> ProfileRow(user: user) // ...only this leaf actually needs it
```

Every new piece of shared data means editing every layer again. It is fragile and noisy.

**Step 4 — The fix: provide state higher, read it directly.**
State managers solve prop drilling by letting any descendant read shared state directly, without the middle widgets carrying it. `Provider`/`Riverpod`/`BLoC` all give you this "read it where you need it" power. That is the whole reason they exist — they replace manual lifting once the tree gets deep.

**Why interviewers ask:** It shows you understand the natural progression: start simple with lifting state up, and reach for a state manager only when prop drilling becomes the pain.

**Common mistake:** Either never lifting state (using globals instead) or lifting everything to the very top, causing huge rebuilds. Lift only to the **nearest** common parent.

**Follow-ups they may ask:**
- *"When do you stop lifting and add a state manager?"* → When you'd have to pass data through widgets that don't use it (prop drilling), or when unrelated screens need it.
- *"What's the cost of lifting too high?"* → A change high up rebuilds a large subtree. Keep state as low as possible.

**Related:** [Q5 — InheritedWidget](#q5) · [Q16 — sharing across screens](#q16) · [Q1 — what is state](#q1)

[↑ Back to top](#toc)

---

# B. The foundation: InheritedWidget & Provider

---

<a id="q5"></a>
## 5. How does `InheritedWidget` pass data down, and what does `updateShouldNotify` do?

> Common · Medium–Hard

**Short answer (say this):**
"`InheritedWidget` is Flutter's built-in way to push data down the tree so any descendant can read it directly, without passing it through every constructor. A descendant reads it with `dependOnInheritedWidgetOfExactType`, which also subscribes that widget to changes. When the data updates, Flutter calls `updateShouldNotify`; if it returns true, only the widgets that depend on it rebuild. It's the engine under `Theme.of(context)` and Provider."

**Let's understand it fully:**

**Step 1 — The "shared noticeboard" idea.**
Think of an `InheritedWidget` as a noticeboard placed high in the tree. Any widget below can walk up, read the board, and (if it wants) subscribe to be told when the board changes. It does not need anyone to carry the data down by hand — that solves the prop-drilling pain from [Q4](#q4).

**Step 2 — How a descendant reads and subscribes.**
A descendant calls `context.dependOnInheritedWidgetOfExactType<MyInherited>()`. This does two things: it returns the data, and it registers this widget as a **dependent**. Being a dependent means "rebuild me when this data changes."

**Step 3 — The update flow.**

1. The `InheritedWidget` is rebuilt with new data.
2. Flutter calls `updateShouldNotify(oldWidget)` on it.
3. If it returns `true`, Flutter calls `didChangeDependencies()` on every dependent and marks them to rebuild.
4. If it returns `false`, dependents are **not** rebuilt — even though the inherited widget itself rebuilt.

```
        MyApp
          |
   ThemeInherited (holds the theme)
        /        \
   ScreenA      ScreenB
      |             |
  LabelX        LabelY
 (depends)     (depends)

theme changes:
  1. ThemeInherited rebuilds
  2. updateShouldNotify(old) -> color changed? -> true
  3. LabelX & LabelY rebuild; ScreenA/ScreenB do NOT (they didn't depend)
```

**Step 4 — `updateShouldNotify` is the performance switch.**
It answers one question: "did the data really change enough to bother rebuilding the listeners?" Compare old and new values and return `true` only when needed.

```dart
class ThemeInherited extends InheritedWidget {
  final AppTheme theme;
  const ThemeInherited({required this.theme, required super.child});

  static AppTheme of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<ThemeInherited>()!.theme;

  @override
  bool updateShouldNotify(ThemeInherited oldWidget) =>
      theme.primaryColor != oldWidget.theme.primaryColor ||
      theme.fontSize != oldWidget.theme.fontSize; // rebuild only if these changed
}

// any descendant:
final theme = ThemeInherited.of(context);
```

**Step 5 — Read without subscribing.**
There are two lookups. `dependOnInheritedWidgetOfExactType` subscribes (rebuild on change). `getInheritedWidgetOfExactType` only reads, with no subscription (no rebuild on change). Picking the wrong one causes either missed updates or wasted rebuilds.

**Why interviewers ask:** `InheritedWidget` is the foundation under `Theme.of`, `MediaQuery.of`, and Provider itself. If you understand it, you understand how all higher-level state management works underneath.

**Common mistake:** Returning `true` from `updateShouldNotify` unconditionally — that rebuilds every dependent on every change and throws away the optimization. Also confusing the subscribing lookup with the non-subscribing one.

**Follow-ups they may ask:**
- *"What calls `didChangeDependencies`?"* → A dependency changing (when `updateShouldNotify` returns true). It runs once after `initState` too.
- *"Why is Provider built on this?"* → Provider wraps `InheritedWidget` to remove boilerplate and add listening to `ChangeNotifier`. (See [Q6](#q6).)

**Related:** [Q4 — prop drilling](#q4) · [Q6 — Provider](#q6) · [Q3 — didChangeDependencies](#q3)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. Explain Provider — `ChangeNotifier`, `Consumer`, `Selector`, and `ProxyProvider`.

> Very common · Medium

**Short answer (say this):**
"Provider is a thin, friendly wrapper around `InheritedWidget` that removes boilerplate. My model extends `ChangeNotifier` and calls `notifyListeners()` when data changes. `Consumer` rebuilds just one subtree when the model changes, `Selector` rebuilds only when one chosen field changes, and `ProxyProvider` builds one provided value from another. It's the officially recommended starting point for most apps."

**Let's understand it fully:**

**Step 1 — `ChangeNotifier` = "tell my listeners when I change."**
Think of `ChangeNotifier` like a town crier. Your model holds data, and when the data changes, it shouts `notifyListeners()`. Anyone listening updates.

```dart
class CartModel extends ChangeNotifier {
  final List<Item> _items = [];
  List<Item> get items => List.unmodifiable(_items);
  int get totalCount => _items.length;
  double get totalPrice => _items.fold(0, (sum, i) => sum + i.price);

  void add(Item item) {
    _items.add(item);
    notifyListeners(); // shout: "I changed!" -> listeners rebuild
  }
}
```

**Step 2 — Provide the model above the widgets that need it.**

```dart
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => CartModel(),
      child: const MyApp(),
    ),
  );
}
```

**Step 3 — `Consumer` = rebuild only this subtree.**
Wrap just the part that should rebuild, so the rest of the screen stays still.

```dart
Consumer<CartModel>(
  builder: (context, cart, child) => Text('Items: ${cart.totalCount}'),
)
```

The `child` parameter is a bonus: pass a widget that does **not** depend on the model, and Provider reuses it instead of rebuilding it.

**Step 4 — `Selector` = rebuild only when ONE field changes.**
`Consumer` rebuilds on any `notifyListeners()`. `Selector` is finer: you pick one value, and it rebuilds only when that value changes (compared with `==`).

```dart
// rebuilds only when totalPrice changes, ignores everything else in the model
final price = context.select<CartModel, double>((cart) => cart.totalPrice);
Text('Total: \$${price.toStringAsFixed(2)}');
```

**Step 5 — `ProxyProvider` = build one value from another.**
Use it when one object needs another injected into it — for example, an `AuthService` that needs an `ApiClient`.

```dart
MultiProvider(
  providers: [
    Provider<ApiClient>(create: (_) => ApiClient()),
    ProxyProvider<ApiClient, AuthService>(
      update: (_, api, __) => AuthService(api), // rebuilt if ApiClient changes
    ),
  ],
  child: const MyApp(),
)
```

**Step 6 — Always release resources.**
`ChangeNotifierProvider` calls `dispose()` on your `ChangeNotifier` automatically when it leaves the tree, so timers and subscriptions inside the model get cleaned up. If you build the notifier yourself and pass it with `.value`, you own disposing it.

**Why interviewers ask:** Provider is the officially recommended beginner-to-intermediate tool. They test whether you can scope rebuilds with `Consumer`/`Selector` instead of rebuilding the whole screen on every change.

**Common mistake:** Wrapping a huge subtree in a single `Consumer` so everything rebuilds. Scope `Consumer` tightly, or use `Selector` to react to just one field. Another: mutating the model's list directly from outside instead of through a method that calls `notifyListeners()`.

**Follow-ups they may ask:**
- *"`Consumer` vs `Selector`?"* → `Consumer` rebuilds on any change; `Selector` rebuilds only when the chosen value changes.
- *"What's the `child` argument for?"* → A widget that doesn't depend on the model; Provider keeps it and skips rebuilding it.

**Related:** [Q5 — InheritedWidget](#q5) · [Q7 — watch/read/select](#q7) · [Q13 — Riverpod](#q13)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. What is the difference between `context.watch`, `context.read`, and `context.select`?

> Very common · Easy–Medium

**Short answer (say this):**
"All three read a provided value, but they listen differently. `watch` subscribes and rebuilds the widget on every change — use it in `build`. `read` reads once with no subscription — use it inside callbacks like `onPressed`. `select` is the precise one: it watches a derived value and rebuilds only when that exact value changes. The classic rule is: `watch`/`select` in `build`, `read` in callbacks."

**Let's understand it fully:**

**Step 1 — The "subscription" idea.**
Think of these as three ways to follow a news source. `watch` is "notify me on every update." `select` is "notify me only when this one headline changes." `read` is "just tell me today's news once, don't follow me."

**Step 2 — `context.watch<T>()` — rebuild on any change.**
Use it inside `build`. The widget rebuilds whenever `T` calls `notifyListeners()`.

```dart
@override
Widget build(BuildContext context) {
  final cart = context.watch<CartModel>(); // rebuilds on any cart change
  return Text('Items: ${cart.totalCount}');
}
```

**Step 3 — `context.read<T>()` — read once, no rebuild.**
Use it inside callbacks (`onPressed`, `onTap`). You just want to act, not subscribe.

```dart
FloatingActionButton(
  onPressed: () => context.read<CartModel>().add(Item('Shoes', 59.99)),
  child: const Icon(Icons.add),
)
```

**Step 4 — `context.select<T, R>(...)` — watch one derived value.**
The finest-grained option. It rebuilds only when the selected value `R` changes, even if other parts of `T` change.

```dart
// rebuilds only when totalPrice changes, not when item names change
final price = context.select<CartModel, double>((c) => c.totalPrice);
```

**Step 5 — The decision table.**

```
context.watch<T>()      -> rebuild on ANY change to T        (use in build)
context.select<T,R>()   -> rebuild only when R (part of T) changes (use in build)
context.read<T>()       -> read once, NO subscription        (use in callbacks)
```

**Step 6 — Why `watch` in a callback throws.**
`watch` subscribes to changes, and subscribing is only valid during the build phase. A button callback runs outside build, so calling `watch` there throws an error. Use `read` in callbacks.

**Why interviewers ask:** This is the most common Provider performance question. Picking the wrong one means either missed updates (`read` in `build`) or a runtime error (`watch` in a callback).

**Common mistake:** Using `context.watch` inside `onPressed` (runtime error), or `context.read` inside `build` (the widget won't rebuild when data changes).

**Follow-ups they may ask:**
- *"Why is `read` correct in `onPressed`?"* → Callbacks run outside build; you only want a one-time read, not a subscription.
- *"What does `select` save?"* → It avoids rebuilds when fields you don't care about change.

**Related:** [Q6 — Provider](#q6) · [Q13 — Riverpod's ref.watch/read/listen](#q13)

[↑ Back to top](#toc)

---

# C. The BLoC family

---

<a id="q8"></a>
## 8. Explain the BLoC pattern — events, states, and streams.

> Very common · Medium–Hard

**Short answer (say this):**
"BLoC stands for Business Logic Component. The UI sends in events — like 'login pressed' — and the BLoC sends back a stream of states — like loading, then success or failure. The UI just rebuilds from whatever state it receives. This keeps business logic out of the widgets, which makes it predictable and easy to test. In modern bloc v8+, I register handlers with `on<Event>()` and emit new states with an `Emitter`."

**Let's understand it fully:**

**Step 1 — The "order counter" idea.**
Think of a BLoC like a fast-food counter. You (the UI) hand in an order slip — that's an **event**. The kitchen (the BLoC) works on it and hands back plates one by one — those are **states** (first "cooking", then "ready" or "sorry, out of stock"). You don't cook anything yourself; you just react to the plates you get.

```
   UI  --event-->  BLoC  --stream of states-->  UI (rebuilds)

   event in  ->  BLoC processes  ->  new state emitted  ->  UI updates
```

**Step 2 — Events and states are plain classes.**
Events are inputs (button tapped, page loaded). States are outputs (initial, loading, success, failure). Making them classes — often `sealed` — means the type system can check you handled them all (see [Q15](#q15)).

```dart
// Events (inputs)
sealed class AuthEvent {}
class LoginRequested extends AuthEvent {
  final String email;
  final String password;
  LoginRequested(this.email, this.password);
}
class LogoutRequested extends AuthEvent {}

// States (outputs)
sealed class AuthState {}
class AuthInitial extends AuthState {}
class AuthLoading extends AuthState {}
class AuthSuccess extends AuthState {
  final User user;
  AuthSuccess(this.user);
}
class AuthFailure extends AuthState {
  final String message;
  AuthFailure(this.message);
}
```

**Step 3 — The BLoC maps events to states (modern v8+ style).**
You register one handler per event in the constructor with `on<Event>()`. Each handler gets the event and an `Emitter` to push out new states.

```dart
class AuthBloc extends Bloc<AuthEvent, AuthState> {
  final AuthRepository _repo;

  AuthBloc(this._repo) : super(AuthInitial()) {
    on<LoginRequested>(_onLogin);
    on<LogoutRequested>(_onLogout);
  }

  Future<void> _onLogin(LoginRequested event, Emitter<AuthState> emit) async {
    emit(AuthLoading());
    try {
      final user = await _repo.login(event.email, event.password);
      emit(AuthSuccess(user));
    } catch (e) {
      emit(AuthFailure(e.toString()));
    }
  }

  Future<void> _onLogout(LogoutRequested event, Emitter<AuthState> emit) async {
    await _repo.logout();
    emit(AuthInitial());
  }
}
```

**Step 4 — The old `mapEventToState` (good to recognize).**
Before bloc v8, you overrode one big `mapEventToState` method that used `async*` and `yield`. Interviewers may show this — recognize it as the legacy style replaced by `on<Event>()`.

```dart
// Legacy (pre-v8) — replaced by on<Event>():
// Stream<AuthState> mapEventToState(AuthEvent event) async* {
//   if (event is LoginRequested) {
//     yield AuthLoading();
//     try {
//       final user = await _repo.login(event.email, event.password);
//       yield AuthSuccess(user);
//     } catch (e) {
//       yield AuthFailure(e.toString());
//     }
//   }
// }
```

**Step 5 — Why this design is loved.**
Because everything flows one way (event in → state out), the logic is predictable and easy to test: give an event, assert the states. And because each event is an object, you can log every event that happened — great for debugging.

**Why interviewers ask:** BLoC is one of the most widely used production patterns in Flutter, especially in BD and agency teams. They want to hear that you understand the one-way, stream-based flow and why separating events from states makes code testable.

**Common mistake:** Mixing the old `mapEventToState` with the new `on<Event>` API. Also calling `emit()` after an `await` when the bloc may be closed (see [Q12](#q12)), and building one giant bloc instead of splitting by feature.

**Follow-ups they may ask:**
- *"Why are events separate from states?"* → It gives one-way flow and a log of inputs, which makes behavior predictable and testable.
- *"What is an `EventTransformer`?"* → A way to control how events are processed — for example debounce or throttle search-as-you-type.

**Related:** [Q9 — Cubit vs BLoC](#q9) · [Q10 — Builder/Listener/Consumer](#q10) · [Q15 — sealed states](#q15)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What is a Cubit? How does it differ from BLoC, and when should you prefer each?

> Very common · Medium

**Short answer (say this):**
"A Cubit is a simpler BLoC with the event layer removed. Instead of sending events, I just call methods on the Cubit, and those methods call `emit(newState)`. Both share the same base class, so both work with `BlocBuilder` and friends. I use Cubit for simple logic like counters and toggles, and full BLoC when I need a log of events or stream transformations like debounce."

**Let's understand it fully:**

**Step 1 — Cubit = "just call a method."**
With a BLoC you add an event object; with a Cubit you call a normal method. Think of BLoC as ordering through a ticket system, and Cubit as just telling the cook directly. Less ceremony.

```
BLoC:   UI -> Event -> on<Event> -> emit(State) -> UI
Cubit:  UI -> cubit.method()      -> emit(State) -> UI
```

**Step 2 — Same family, same widgets.**
Both `Cubit` and `Bloc` extend the same base (`BlocBase`). That base gives the state stream, `emit`, the current `state`, and `isClosed`. So a Cubit works with `BlocBuilder`, `BlocListener`, and `BlocConsumer` exactly like a Bloc.

```dart
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);
  void increment() => emit(state + 1);
  void decrement() => emit(state - 1);
  void reset() => emit(0);
}

final cubit = CounterCubit();
cubit.increment(); // state is now 1
cubit.increment(); // state is now 2
```

**Step 3 — The same logic in a Bloc needs more ceremony.**

```dart
sealed class CounterEvent {}
class Increment extends CounterEvent {}
class Decrement extends CounterEvent {}

class CounterBloc extends Bloc<CounterEvent, int> {
  CounterBloc() : super(0) {
    on<Increment>((event, emit) => emit(state + 1));
    on<Decrement>((event, emit) => emit(state - 1));
  }
}

final bloc = CounterBloc();
bloc.add(Increment()); // must create an event object first
```

**Step 4 — The trade-off table.**

| Aspect | Cubit | Bloc |
|---|---|---|
| Input | direct method calls | event objects |
| Boilerplate | less — no event classes | more — event classes required |
| Traceability | harder to log | every event is a logged object (`onTransition`) |
| Transformations | none | `EventTransformer` for debounce, throttle, merge |
| Testing | call methods directly | add events, verify the state stream |

**Step 5 — When to pick each.**
- **Prefer Cubit** for straightforward logic: counters, toggles, simple form state, settings. Less code, easy to read.
- **Prefer Bloc** when you need a log of what happened (event sourcing), or when you must debounce/throttle events (search-as-you-type), or when a feature is complex enough that the extra structure pays off.

**Why interviewers ask:** They want pragmatism. Choosing Cubit for simple cases shows you value simplicity; choosing Bloc for complex event flows shows you understand traceability. The weakest answer is "always use Bloc."

**Common mistake:** Claiming a Cubit can't be used with `BlocBuilder`/`BlocListener` — it can, because both extend `BlocBase`. Also forgetting that Cubit loses event-level traceability, which can hurt when debugging complex flows.

**Follow-ups they may ask:**
- *"Can a Cubit do debounce?"* → Not built in. Event transformers are a Bloc feature. With a Cubit you'd debounce manually before calling the method.
- *"Do both auto-close?"* → `BlocProvider` closes the bloc/cubit when it leaves the tree, just like Provider disposes a `ChangeNotifier`.

**Related:** [Q8 — BLoC pattern](#q8) · [Q12 — emit after close](#q12) · [Q18 — testing](#q18)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. When do you use `BlocBuilder` vs `BlocListener` vs `BlocConsumer`?

> Very common · Medium

**Short answer (say this):**
"`BlocBuilder` rebuilds UI when the state changes — use it to show data or a spinner. `BlocListener` runs a one-time side-effect on a state change without rebuilding — use it for navigation, a SnackBar, or a dialog. `BlocConsumer` is both together, for when one state change should both rebuild the UI and fire a side-effect. The key idea: rebuild with the builder, do one-shot actions with the listener."

**Let's understand it fully:**

**Step 1 — The "screen vs action" idea.**
Some state changes should change what's drawn (show the welcome text). Others should trigger a one-time action (push a new screen, pop a SnackBar). Builder is for drawing; listener is for one-time actions.

```
state change
   |
   +--> BlocBuilder   -> rebuild widget (visual)
   |
   +--> BlocListener  -> fire a side-effect ONCE (navigate, snackbar)
   |
   +--> BlocConsumer  -> both: rebuild + side-effect
```

**Step 2 — `BlocBuilder` rebuilds UI.**

```dart
BlocBuilder<AuthBloc, AuthState>(
  builder: (context, state) {
    if (state is AuthLoading) return const CircularProgressIndicator();
    if (state is AuthSuccess) return Text('Welcome, ${state.user.name}');
    if (state is AuthFailure) return Text('Error: ${state.message}');
    return const LoginForm();
  },
)
```

**Step 3 — `BlocListener` fires a one-time side-effect.**
Its `child` is **not** rebuilt. The listener runs once per state change — perfect for things that must not repeat.

```dart
BlocListener<AuthBloc, AuthState>(
  listener: (context, state) {
    if (state is AuthSuccess) {
      Navigator.pushReplacementNamed(context, '/home');
    }
    if (state is AuthFailure) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(state.message)),
      );
    }
  },
  child: const LoginForm(), // NOT rebuilt by the listener
)
```

**Step 4 — `BlocConsumer` does both.**
Use it when the same state change should rebuild the UI **and** run a side-effect.

```dart
BlocConsumer<AuthBloc, AuthState>(
  listener: (context, state) {
    if (state is AuthSuccess) Navigator.pushReplacementNamed(context, '/home');
  },
  builder: (context, state) {
    if (state is AuthLoading) {
      return const ElevatedButton(onPressed: null, child: CircularProgressIndicator());
    }
    return ElevatedButton(
      onPressed: () => context.read<AuthBloc>().add(LoginRequested(email, password)),
      child: const Text('Login'),
    );
  },
)
```

**Step 5 — The rule of thumb.**
If it changes pixels → `BlocBuilder`. If it's a one-shot action (navigate, snackbar, dialog) → `BlocListener`. If both at once → `BlocConsumer`.

**Why interviewers ask:** This directly tests whether you know when to rebuild vs when to do a one-time action. Getting it wrong causes dialogs that open repeatedly, or navigation that never fires.

**Common mistake:** Showing a SnackBar inside a `BlocBuilder` — the builder re-runs on every rebuild, so the SnackBar pops over and over. SnackBars are side-effects, so they belong in `BlocListener`. Conversely, using `BlocListener` to display state on screen does nothing, because it has no builder.

**Follow-ups they may ask:**
- *"Why not navigate in a builder?"* → A builder can run many times; navigation would fire repeatedly. Listener runs once per change.
- *"How do you skip irrelevant rebuilds?"* → Use `buildWhen`/`listenWhen` (see [Q11](#q11)).

**Related:** [Q8 — BLoC pattern](#q8) · [Q11 — buildWhen/listenWhen](#q11) · [Q15 — sealed states](#q15)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What do `buildWhen` and `listenWhen` do, and why do they matter for performance?

> Common · Medium

**Short answer (say this):**
"They are filters. `buildWhen` sits on `BlocBuilder` and gets the previous and current state; if it returns false, the builder skips that rebuild even though the state changed. `listenWhen` does the same for `BlocListener`. They matter because a single bloc may emit many states a second, and without filtering, every connected widget rebuilds every time — that's the difference between a smooth app and a janky one."

**Let's understand it fully:**

**Step 1 — The "do I care about this change?" idea.**
A bloc might emit states for many reasons. A widget that only shows the name shouldn't rebuild when the email changes. `buildWhen` lets that widget say "only rebuild me when the part I care about changed."

**Step 2 — `buildWhen` filters rebuilds.**
It gets `previous` and `current` and returns a `bool`. Return `false` to skip the rebuild.

```dart
BlocBuilder<FormBloc, FormState>(
  buildWhen: (previous, current) => previous.name != current.name, // only on name change
  builder: (context, state) => Text('Name: ${state.name}'),
)
```

**Step 3 — `listenWhen` filters side-effects.**
Same idea for `BlocListener`. Useful to fire a SnackBar only on a real transition.

```dart
BlocListener<FormBloc, FormState>(
  listenWhen: (prev, curr) => prev.isSubmitting && !curr.isSubmitting, // only when submit finishes
  listener: (context, state) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Form submitted!')),
    );
  },
  child: const FormBody(),
)
```

**Step 4 — Both together in `BlocConsumer`.**

```dart
BlocConsumer<AuthBloc, AuthState>(
  buildWhen: (prev, curr) => prev.runtimeType != curr.runtimeType, // rebuild only on type change
  listenWhen: (prev, curr) => curr is AuthFailure,                 // listen only on failure
  listener: (context, state) {
    if (state is AuthFailure) {
      showDialog(context: context, builder: (_) => AlertDialog(content: Text(state.message)));
    }
  },
  builder: (context, state) => switch (state) {
    AuthLoading() => const CircularProgressIndicator(),
    AuthSuccess() => const HomePage(),
    _             => const LoginForm(),
  },
)
```

**Step 5 — The real-world payoff.**
Imagine search-as-you-type: the bloc emits a new state on every keystroke. Without `buildWhen`, every keystroke rebuilds every connected widget — janky. With it, only the widgets whose data actually changed rebuild.

**Why interviewers ask:** It shows you know `BlocBuilder` is **not** smart by default — it rebuilds on every state — and that you can opt into filtering for performance.

**Common mistake:** Assuming `buildWhen` defaults to skipping; it defaults to `(prev, curr) => true`, meaning "always rebuild." Another: putting slow logic inside `buildWhen` — it must be a cheap comparison.

**Follow-ups they may ask:**
- *"What's the default?"* → Always rebuild / always listen. You must opt into filtering.
- *"Provider equivalent?"* → `Selector` / `context.select` play a similar role (see [Q7](#q7)).

**Related:** [Q10 — Builder/Listener/Consumer](#q10) · [Q7 — select](#q7) · [Q8 — BLoC pattern](#q8)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. What is the difference between `emit()` and `setState()`? What happens if you call `emit()` after a Cubit is closed?

> Common · Medium

**Short answer (say this):**
"Both push a new state and update the UI, but they live in different systems. `setState` belongs to a widget's `State` and rebuilds that widget's own subtree. `emit` belongs to a Cubit/Bloc and pushes a new state onto its stream, so any `BlocBuilder` listening rebuilds. If I call `emit` after the Cubit is closed — usually after an `await` once the user has left the screen — it throws a `StateError`. I guard it with an `isClosed` check."

**Let's understand it fully:**

**Step 1 — Two tools, two systems.**
`setState` is part of the widget layer; it marks the widget dirty and rebuilds it. `emit` is part of the bloc layer; it adds a new value to the bloc's state stream, which any number of listening widgets receive.

```
setState() -> marks THIS widget dirty -> rebuilds its own subtree
emit()     -> pushes state onto the stream -> every BlocBuilder rebuilds
```

**Step 2 — The comparison table.**

| Aspect | `setState()` | `emit()` |
|---|---|---|
| Lives in | `State` (StatefulWidget) | `Cubit` / `Bloc` (BlocBase) |
| What it does | mark element dirty, schedule rebuild | push a new state onto the stream |
| Who rebuilds | this widget's own `build()` | any `BlocBuilder`/`BlocListener` listening |
| State scope | local to one widget | shared with any widget that reads the bloc |
| Lifecycle guard | throws if called after `dispose()` | throws `StateError` if called after `close()` |

**Step 3 — The "emit after close" crash.**
A common bug: you start an async call, the user navigates away (the bloc is closed and disposed), then the async call finishes and tries to `emit`. Because the bloc is closed, this throws "Cannot emit new states after calling close."

```dart
class SearchCubit extends Cubit<SearchState> {
  SearchCubit(this._repo) : super(SearchInitial());
  final SearchRepository _repo;

  Future<void> search(String query) async {
    emit(SearchLoading());
    final results = await _repo.search(query); // takes a few seconds
    emit(SearchSuccess(results)); // if user left -> StateError!
  }
}
```

**Step 4 — The fix: guard with `isClosed`.**

```dart
Future<void> search(String query) async {
  emit(SearchLoading());
  try {
    final results = await _repo.search(query);
    if (!isClosed) emit(SearchSuccess(results)); // guard before emitting
  } catch (e) {
    if (!isClosed) emit(SearchFailure(e.toString()));
  }
}
```

This mirrors the widget-side `if (!mounted) return;` guard from [Q2](#q2) — same problem (async outlives the object), different system.

**Step 5 — A note on Bloc handlers.**
Inside a Bloc's `on<Event>` handler, the framework helps: emits after close are ignored rather than crashing (bloc v8.1+). But explicit guards are still good practice, especially in Cubits and in code that emits outside a handler.

**Why interviewers ask:** It tests your grasp of both the widget lifecycle and the bloc lifecycle. In production, "emit after close" is one of the most common crash sources in bloc apps.

**Common mistake:** Not guarding `emit()` after an async gap and assuming "the framework handles it." For Cubits it does not — it throws. Also confusing `setState`'s "after dispose" error with `emit`'s "after close" error; they're analogous but from different systems.

**Follow-ups they may ask:**
- *"`mounted` vs `isClosed`?"* → `mounted` guards `setState` in a widget; `isClosed` guards `emit` in a bloc/cubit.
- *"How do you avoid leaks here?"* → Cancel subscriptions in `close()`/`dispose()`, and don't emit after the object is gone.

**Related:** [Q2 — setState & mounted](#q2) · [Q9 — Cubit](#q9) · [Q8 — BLoC pattern](#q8)

[↑ Back to top](#toc)

---

# D. Riverpod & GetX

---

<a id="q13"></a>
## 13. Explain Riverpod — how it differs from Provider, its provider types, and `ref.watch` vs `ref.read` vs `ref.listen`.

> Very common · Medium–Hard

**Short answer (say this):**
"Riverpod is by the same author as Provider and fixes its main limits: providers are global and don't depend on the widget tree, so there are no 'provider not found' runtime errors. It has typed providers — `StateProvider`, `FutureProvider`, `StreamProvider`, and `NotifierProvider` for complex logic. Inside a widget I use `ref.watch` to rebuild on change, `ref.read` for one-time access in callbacks, and `ref.listen` for side-effects like navigation."

**Let's understand it fully:**

**Step 1 — Why Riverpod exists (the Provider pain points).**

| Problem with Provider | How Riverpod fixes it |
|---|---|
| Needs the widget tree (`BuildContext`) | providers are global, tree-independent |
| "Provider not found" crashes at runtime | caught at compile time |
| Can't have two providers of the same type | each provider is its own unique variable |
| Hard to combine providers | built-in dependencies via `ref` |
| No built-in auto-dispose | `autoDispose` modifier |

**Step 2 — Providers are declared globally.**
Because a provider is just a top-level variable, any widget can read it from anywhere — no need to find it in the tree.

```dart
final counterProvider = StateProvider<int>((ref) => 0);

final todosProvider = FutureProvider<List<Todo>>((ref) async {
  final repo = ref.watch(todoRepositoryProvider); // providers can depend on each other
  return repo.fetchAll();
});

final chatProvider = StreamProvider<List<Message>>(
  (ref) => ref.watch(chatRepositoryProvider).messageStream(),
);
```

**Step 3 — The provider types (pick by need).**
- **`Provider<T>`** — a read-only or computed value.
- **`StateProvider<T>`** — a single simple mutable value (int, bool, enum). Don't use it for complex state.
- **`FutureProvider<T>`** — exposes an `AsyncValue<T>` from a `Future`. Great for one-shot async loads.
- **`StreamProvider<T>`** — same, but from a `Stream`. For live data (sockets, Firestore).
- **`NotifierProvider<N, T>`** (Riverpod 2.0+) — the modern home for complex logic, using a `Notifier` class. It replaced `StateNotifierProvider`.

```dart
class TodosNotifier extends Notifier<List<Todo>> {
  @override
  List<Todo> build() => [];                 // initial state

  void add(Todo todo) => state = [...state, todo];
  void toggle(String id) => state = [
        for (final t in state)
          if (t.id == id) t.copyWith(done: !t.done) else t,
      ];
}

final todosProvider = NotifierProvider<TodosNotifier, List<Todo>>(TodosNotifier.new);
```

**Step 4 — `ref.watch` vs `ref.read` vs `ref.listen`.**
These mirror Provider's `watch`/`read` plus a listener.

```dart
class TodoPage extends ConsumerWidget {
  const TodoPage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final todos = ref.watch(todosProvider); // rebuild when todos change

    ref.listen<List<Todo>>(todosProvider, (prev, next) { // side-effect, no rebuild
      if (next.length > (prev?.length ?? 0)) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Todo added!')),
        );
      }
    });

    return ListView(
      children: todos
          .map((t) => ListTile(
                title: Text(t.title),
                onTap: () => ref.read(todosProvider.notifier).toggle(t.id), // one-time in a callback
              ))
          .toList(),
    );
  }
}
```

- `ref.watch` → subscribe and rebuild (use in `build`).
- `ref.read` → read once, no subscription (use in callbacks).
- `ref.listen` → run a side-effect on change, like `BlocListener`.

**Step 5 — `AsyncValue` makes loading/error easy.**
`FutureProvider` and `StreamProvider` hand back an `AsyncValue`, which you unwrap with `.when` — no manual loading flags.

```dart
final userAsync = ref.watch(userProvider);
return userAsync.when(
  loading: () => const CircularProgressIndicator(),
  error: (err, st) => Text('Error: $err'),
  data: (user) => Text('Hello, ${user.name}'),
);
```

**Step 6 — `autoDispose` frees resources.**
Add `.autoDispose` so a provider is destroyed when nobody is listening — important for providers holding streams or controllers, to avoid leaks.

**Why interviewers ask:** Riverpod is increasingly the default for new Flutter projects. They want to see you understand why it beats Provider and can use the right provider type and ref method.

**Common mistake:** Using `ref.read` in `build` (the widget won't rebuild on change) or `ref.watch` in a callback (creates a needless subscription). Also forgetting `.autoDispose` and leaking providers that hold resources.

**Follow-ups they may ask:**
- *"Why no 'provider not found' error?"* → Providers are global variables resolved at compile time, not looked up by type in the tree.
- *"`StateNotifier` vs `Notifier`?"* → `Notifier` (Riverpod 2.0+) is the modern replacement; older code uses `StateNotifierProvider`.

**Related:** [Q6 — Provider](#q6) · [Q7 — watch/read/select](#q7) · [Q15 — sealed states](#q15)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. Explain GetX — controllers, `Obx`, `GetBuilder` — and its trade-offs.

> Common · Medium

**Short answer (say this):**
"GetX is an all-in-one package bundling state management, dependency injection, and routing, with very little boilerplate. State lives in a `GetxController`. You make a variable reactive with `.obs`, and any `Obx(() => ...)` reading it rebuilds automatically; or you use `GetBuilder` and call `update()` manually. The trade-off: it's fast to build but uses a lot of hidden magic and global singletons, which makes data flow harder to trace and testing harder — and it's not endorsed by the Flutter team."

**Let's understand it fully:**

**Step 1 — Controllers hold the logic.**
A `GetxController` is where your state and methods live, similar to a Cubit but with GetX's reactive helpers.

```dart
class CartController extends GetxController {
  var items = <Item>[].obs;       // reactive list
  var total = 0.0.obs;            // reactive double

  void addItem(Item item) {
    items.add(item);
    total.value = items.fold(0, (sum, i) => sum + i.price);
  }
}
```

**Step 2 — `.obs` + `Obx` = automatic rebuilds.**
Adding `.obs` turns a value into an observable. Any `Obx` widget that reads it rebuilds when it changes — no `notifyListeners`, no events.

```dart
Get.put(CartController()); // register it (dependency injection)

Obx(() {
  final ctrl = Get.find<CartController>();
  return Text('Items: ${ctrl.items.length}, Total: ${ctrl.total}');
})
```

**Step 3 — `GetBuilder` = manual rebuilds.**
The non-reactive option. You call `update()` to tell `GetBuilder` widgets to rebuild — like a controller-scoped `setState`. It uses less memory because there's no observable stream.

```dart
class CounterController extends GetxController {
  int count = 0;
  void increment() {
    count++;
    update(); // manually trigger rebuild
  }
}

GetBuilder<CounterController>(
  init: CounterController(),
  builder: (ctrl) => Text('${ctrl.count}'),
)
```

```
Reactive:  var count = 0.obs;  ->  Obx(() => Text('${ctrl.count}'))   (auto rebuild)
Manual:    int count = 0;      ->  GetBuilder(builder: ...)           (call update())
```

**Step 4 — The trade-offs.**

| Pros | Cons |
|---|---|
| Very low boilerplate | implicit "magic" — hard to trace data flow |
| Fast prototyping | global singletons make testing harder |
| Built-in routing + DI | not endorsed by the Flutter team |
| Large community, many examples | tight coupling to the GetX ecosystem |
| | `.obs` can hide performance issues in big lists |

**Step 5 — Where it fits.**
GetX shines for solo developers, prototypes, and small apps where speed of building matters more than strict architecture. For large teams and complex apps, its implicit dependencies (`Get.find`) and global state make code reviews and testing harder.

**Why interviewers ask:** Even teams that don't use GetX want to see you can evaluate a tool critically — naming concrete strengths and concrete drawbacks shows maturity.

**Common mistake:** Saying "GetX is bad" or "GetX is best" with no nuance. The strong answer praises its speed for small apps while naming specific costs for large teams (global state, implicit `Get.find`, harder mocking).

**Follow-ups they may ask:**
- *"`Obx` vs `GetBuilder`?"* → `Obx` is automatic and reactive; `GetBuilder` is manual via `update()` and lighter.
- *"Why is testing harder?"* → Global singletons via `Get.find` are harder to replace with mocks than constructor-injected dependencies.

**Related:** [Q6 — Provider](#q6) · [Q13 — Riverpod](#q13) · [Q17 — choosing a solution](#q17)

[↑ Back to top](#toc)

---

# E. Architecture & senior decisions

---

<a id="q15"></a>
## 15. How do you model loading, success, and error states cleanly using a sealed union?

> Very common · Medium

**Short answer (say this):**
"Instead of juggling separate booleans like `isLoading`, `hasError`, and a nullable `data`, I model the state as a sealed class with one subtype per case: `Loading`, `Success`, `Failure`. Because it's sealed, the compiler forces my `switch` to handle every case, so I can't forget one and there's no `default` needed. This makes impossible states — like loading and error at the same time — literally unrepresentable."

**Let's understand it fully:**

**Step 1 — The problem with boolean flags.**
A common but fragile approach uses several flags:

```dart
// Fragile: allows impossible combos like isLoading=true AND error!=null AND data!=null
class BadState {
  bool isLoading = false;
  String? error;
  UserProfile? data;
}
```

Now every widget must guess which flag wins, and you can accidentally create nonsense states.

**Step 2 — The sealed union: one type per case.**
A `sealed` class lists all the possible states in one file. Each state carries exactly the data it needs — and nothing else.

```dart
sealed class ResultState<T> {
  const ResultState();
}
class Loading<T> extends ResultState<T> {
  const Loading();
}
class Success<T> extends ResultState<T> {
  final T data;
  const Success(this.data);
}
class Failure<T> extends ResultState<T> {
  final String message;
  final Object? error;
  const Failure(this.message, {this.error});
}
```

`Loading` has no data. `Success` always has data. `Failure` always has a message. You cannot build a "loading with an error" — that state simply does not exist.

**Step 3 — Use it in a Cubit.**

```dart
class UserProfileCubit extends Cubit<ResultState<UserProfile>> {
  UserProfileCubit(this._repo) : super(const Loading());
  final UserRepository _repo;

  Future<void> load() async {
    emit(const Loading());
    try {
      final profile = await _repo.getProfile();
      if (!isClosed) emit(Success(profile)); // guard from Q12
    } catch (e) {
      if (!isClosed) emit(Failure('Failed to load profile', error: e));
    }
  }
}
```

**Step 4 — The big payoff: exhaustive `switch`.**
Because the class is sealed, a `switch` expression must cover every subtype, or the code won't compile. No `default` needed.

```dart
BlocBuilder<UserProfileCubit, ResultState<UserProfile>>(
  builder: (context, state) => switch (state) {
    Loading() => const Center(child: CircularProgressIndicator()),
    Success(:final data) => Column(children: [Text(data.name), Text(data.email)]),
    Failure(:final message) => Column(children: [
        Text(message),
        ElevatedButton(
          onPressed: () => context.read<UserProfileCubit>().load(),
          child: const Text('Retry'),
        ),
      ]),
  },
)
```

If you later add `class Empty extends ResultState<T> {}` and forget to handle it, the `switch` stops compiling and points right at the gap. The bug is caught before the app runs.

**Step 5 — Make it reusable.**
You can write one generic widget that renders any `ResultState`, so every screen handles async the same way.

```dart
class AsyncStateWidget<T> extends StatelessWidget {
  final ResultState<T> state;
  final Widget Function(T data) onSuccess;
  final VoidCallback? onRetry;
  const AsyncStateWidget({super.key, required this.state, required this.onSuccess, this.onRetry});

  @override
  Widget build(BuildContext context) => switch (state) {
        Loading() => const Center(child: CircularProgressIndicator()),
        Success(:final data) => onSuccess(data),
        Failure(:final message) => Center(
            child: Column(mainAxisSize: MainAxisSize.min, children: [
              Text(message),
              if (onRetry != null)
                ElevatedButton(onPressed: onRetry, child: const Text('Retry')),
            ]),
          ),
      };
}
```

**Why interviewers ask:** It shows you model states explicitly instead of with fragile boolean combinations, and that you use the type system to make illegal states unrepresentable — a strong senior signal.

**Common mistake:** Adding a `default` case to the `switch`, which silently swallows missing states and throws away the exhaustiveness check. Also keeping the boolean flags around "just in case."

**Follow-ups they may ask:**
- *"sealed class vs `freezed` union?"* → Both model fixed states. `sealed` is built into Dart 3 and gives the exhaustive check for free, with no code generation.
- *"How does Riverpod do this?"* → `AsyncValue` is a built-in version with `.when(loading, error, data)` (see [Q13](#q13)).

**Related:** [Q8 — BLoC states](#q8) · [Q12 — emit guards](#q12) · [Q13 — AsyncValue](#q13)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. How do you share state between two completely unrelated screens?

> Common · Medium

**Short answer (say this):**
"'Unrelated' means neither screen is an ancestor of the other, so I must put the state above both of them, or outside the tree entirely. The cleanest options are a Provider/BLoC at a common ancestor like `MaterialApp`, or a Riverpod provider, which is global and tree-independent so both screens read the same instance. I avoid global mutable variables, because the data changes but the UI never updates."

**Let's understand it fully:**

**Step 1 — Why this needs lifting above both.**
Two screens in different tabs can't see each other. So the shared state must live somewhere both can reach: either a common ancestor in the tree, or a global provider that doesn't care about the tree at all.

```
        MaterialApp
            |
   ChangeNotifierProvider<CartModel>   <- lives above BOTH
        /              \
   /orders route    /catalog route
      |                 |
  OrdersScreen      CatalogScreen
  (reads cart)      (writes cart)
```

**Step 2 — The options, simplest to most decoupled.**
1. **Provider / Riverpod / BLoC at a common ancestor** — place it at `MaterialApp` level; both screens read it. The standard answer.
2. **Global Riverpod provider** — tree-independent, so both screens `ref.watch` the same provider regardless of position.
3. **Service locator (`get_it`)** — register a singleton service both screens fetch. Simple, but you still need a reactive layer (a stream or notifier) for the UI to update.
4. **Event bus / shared `StreamController`** — both screens listen to one stream. Very decoupled, but harder to trace.
5. **Navigator result / callbacks** — only for simple "Screen B returns a value to Screen A" cases.

**Step 3 — The clean Riverpod version (no tree dependency).**

```dart
final sharedCartProvider = NotifierProvider<CartNotifier, CartState>(CartNotifier.new);

// Screen A — deep in tab 1
class OrdersScreen extends ConsumerWidget {
  const OrdersScreen({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final cart = ref.watch(sharedCartProvider);
    return Text('You have ${cart.items.length} items in cart');
  }
}

// Screen B — deep in tab 2, completely unrelated
class CatalogScreen extends ConsumerWidget {
  const CatalogScreen({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return ElevatedButton(
      onPressed: () => ref.read(sharedCartProvider.notifier).addItem(someItem),
      child: const Text('Add to cart'),
    );
  }
}
```

Both screens touch the **same** provider instance, so adding in B instantly updates A.

**Step 4 — The trap to avoid.**
A plain global variable shares the value but has no way to tell the UI it changed — so the screen won't update. You need something reactive (a `ChangeNotifier`, bloc, or Riverpod provider), not a bare static field.

**Why interviewers ask:** It's a practical architecture question. They want to see you think in terms of scoping and dependency injection, not passing callbacks through fifteen widgets.

**Common mistake:** Reaching for global mutable variables or static singletons with no reactivity — the data changes but the UI doesn't. Another: accidentally creating a separate controller instance in each screen, so each has its own isolated state.

**Follow-ups they may ask:**
- *"Where exactly do you place the provider?"* → At the lowest common ancestor of both screens (often `MaterialApp`), or globally with Riverpod.
- *"Why not a plain singleton?"* → It can hold the data but can't notify the UI; you need a reactive wrapper.

**Related:** [Q4 — lifting state up](#q4) · [Q6 — Provider](#q6) · [Q13 — Riverpod](#q13)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. How do you choose a state management solution for a project?

> Very common · Medium

**Short answer (say this):**
"There's no single right answer — it depends on the state and the team. I use `setState` for state local to one widget, Provider or Riverpod for most app-wide state, and BLoC when I need strict architecture or complex event handling like debounce. And it's fine to mix them in one app. The senior point is weighing trade-offs — team familiarity, testability, complexity — instead of defending one tool."

**Let's understand it fully:**

**Step 1 — A simple decision flow.**

```
Is the state local to one widget?
   -> YES: setState()

Small/medium app or prototype?
   -> YES: Provider or Riverpod

Need strict architecture the whole team follows?
   -> YES: BLoC (clear event/state separation)

Need fine-grained reactivity with little boilerplate?
   -> YES: Riverpod

Rapid prototyping, solo / small team?
   -> YES: GetX (knowing the long-term cost)

Complex async events (debounce, throttle, merge)?
   -> YES: BLoC with EventTransformers
```

**Step 2 — The factors that actually decide it.**
- **Team familiarity:** a team fluent in BLoC ships faster with BLoC than learning a new tool mid-project.
- **Testability:** BLoC and Riverpod are highly testable; GetX is harder to mock.
- **App complexity:** a counter doesn't need BLoC; an enterprise banking app benefits from its structure.
- **Onboarding & reviews:** BLoC's explicitness reads clearly for newcomers; GetX's implicit magic can confuse.

**Step 3 — Mixing is not only allowed, it's smart.**
Use the right tool per layer in the **same** app.

```dart
// Ephemeral UI state -> setState
class _DropdownState extends State<Dropdown> {
  bool _isOpen = false;
}

// Complex auth flow -> BLoC
BlocProvider(create: (_) => AuthBloc(repo));

// Simple theme value -> Riverpod StateProvider
final themeProvider = StateProvider<ThemeMode>((ref) => ThemeMode.system);

// Medium-complexity cart -> Riverpod NotifierProvider
final cartProvider = NotifierProvider<CartNotifier, CartState>(CartNotifier.new);
```

**Step 4 — Match the tool to the size of the problem.**
Don't bring BLoC to a toggle, and don't manage app-wide auth with `setState`. Over-engineering and under-engineering are both red flags; the right size shows judgement.

**Why interviewers ask:** This is a senior-level question. They don't want a partisan answer — they want evidence you can weigh trade-offs, consider team dynamics, and decide pragmatically.

**Common mistake:** Dogmatically defending one tool — "BLoC is the only professional choice" or "Riverpod is always better" are red flags. Another: picking a heavy tool for a tiny app (or the reverse) without explaining why.

**Follow-ups they may ask:**
- *"Can you mix BLoC and Riverpod?"* → Yes — use each where it fits; nothing forces one tool for the whole app.
- *"What would you pick for a brand-new app today?"* → Often Riverpod for app state plus `setState` for local UI; BLoC if the team prefers it or the domain is event-heavy. Justify with the factors above.

**Related:** [Q1 — what is state](#q1) · [Q9 — Cubit vs BLoC](#q9) · [Q13 — Riverpod](#q13) · [Q14 — GetX](#q14)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. How do you test BLoC / Cubit state logic?

> Common · Medium

**Short answer (say this):**
"I use the `bloc_test` package and its `blocTest` helper. The pattern is: `build` creates the bloc with mocked dependencies, `act` triggers an action — add an event for a Bloc, call a method for a Cubit — and `expect` asserts the exact sequence of emitted states. For Blocs with dependencies, I mock the repository and verify it was called. The key gotcha is that `blocTest` skips the initial state, so I only list the states emitted after the action."

**Let's understand it fully:**

**Step 1 — Why testability is the whole point.**
Teams choose BLoC/Cubit largely because the logic is isolated from the UI and easy to test. If you can't show how to test it, the benefit is only theoretical. So expect this question whenever you mention BLoC.

**Step 2 — The `blocTest` shape.**

```
build:  () => CounterCubit()         <- create the instance
act:    (cubit) => cubit.increment() <- trigger an action
expect: () => [1]                    <- assert the emitted states
```

**Step 3 — Testing a simple Cubit.**

```dart
import 'package:bloc_test/bloc_test.dart';
import 'package:test/test.dart';

void main() {
  group('CounterCubit', () {
    blocTest<CounterCubit, int>(
      'emits [1] when increment is called',
      build: () => CounterCubit(),
      act: (cubit) => cubit.increment(),
      expect: () => [1],
    );

    blocTest<CounterCubit, int>(
      'emits [1, 2, 3] when increment is called three times',
      build: () => CounterCubit(),
      act: (cubit) {
        cubit.increment();
        cubit.increment();
        cubit.increment();
      },
      expect: () => [1, 2, 3],
    );
  });
}
```

**Step 4 — Testing a Bloc with a mocked dependency.**
Mock the repository, drive an event, assert both the state sequence and that the repo was called.

```dart
group('AuthBloc', () {
  late MockAuthRepository mockRepo;
  setUp(() => mockRepo = MockAuthRepository());

  blocTest<AuthBloc, AuthState>(
    'emits [AuthLoading, AuthSuccess] on successful login',
    setUp: () {
      when(() => mockRepo.login(any(), any()))
          .thenAnswer((_) async => User(name: 'Alice'));
    },
    build: () => AuthBloc(mockRepo),
    act: (bloc) => bloc.add(LoginRequested('a@b.com', 'pass')),
    expect: () => [
      isA<AuthLoading>(),
      isA<AuthSuccess>().having((s) => s.user.name, 'name', 'Alice'),
    ],
    verify: (_) {
      verify(() => mockRepo.login('a@b.com', 'pass')).called(1);
    },
  );

  blocTest<AuthBloc, AuthState>(
    'emits [AuthLoading, AuthFailure] on failed login',
    setUp: () {
      when(() => mockRepo.login(any(), any()))
          .thenThrow(Exception('Invalid credentials'));
    },
    build: () => AuthBloc(mockRepo),
    act: (bloc) => bloc.add(LoginRequested('a@b.com', 'wrong')),
    expect: () => [isA<AuthLoading>(), isA<AuthFailure>()],
  );
});
```

**Step 5 — Test the unhappy paths too.**
Don't only test success. Test failures, edge cases (like calling a method after `close()`), and use `setUp`/`tearDown` to share mock setup. Strong candidates show error-state tests, not just the happy path.

**Why interviewers ask:** Testability is a primary reason teams pick BLoC/Cubit. They expect you to know `blocTest`, mocking, and how to assert state sequences.

**Common mistake:** Including the initial state in `expect`. `blocTest` automatically skips it, so for a counter starting at 0, writing `expect: () => [0, 1]` fails — it should be `[1]`. Another: testing only the happy path and ignoring error states.

**Follow-ups they may ask:**
- *"Why isn't the initial state in `expect`?"* → `blocTest` records only states emitted **after** the action; the initial state is already set by `super(...)`.
- *"How do you mock the repository?"* → With `mocktail` or `mockito`: stub methods with `when(...)` and assert calls with `verify(...)`.

**Related:** [Q8 — BLoC pattern](#q8) · [Q9 — Cubit](#q9) · [Q15 — sealed states](#q15)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**setState vs Provider vs Riverpod vs BLoC**

| | `setState` | Provider | Riverpod | BLoC / Cubit |
|---|---|---|---|---|
| Best for | one widget's state | small/medium apps | new apps, all sizes | strict architecture, complex events |
| Boilerplate | none | low | low–medium | medium (BLoC), low (Cubit) |
| Tree-dependent? | yes | yes (`BuildContext`) | no (global) | yes (`BlocProvider`) |
| Testability | weak | good | strong | strong |
| Read in build | the widget rebuilds | `context.watch` | `ref.watch` | `BlocBuilder` |
| One-time read | direct field | `context.read` | `ref.read` | `context.read<Bloc>()` |

**`context.watch` vs `read` vs `select`**

| | rebuilds? | where to use |
|---|---|---|
| `watch` | on any change | in `build` |
| `select` | only when chosen value changes | in `build` |
| `read` | never (one-time) | in callbacks |

**Cubit vs BLoC**

| Cubit | BLoC |
|---|---|
| call methods | add event objects |
| less boilerplate | more structure |
| no event log | every event traceable |
| no transformers | debounce/throttle via transformers |

**BlocBuilder vs BlocListener vs BlocConsumer**

| Widget | What it does |
|---|---|
| `BlocBuilder` | rebuilds UI on state change |
| `BlocListener` | one-time side-effect (navigate, snackbar), no rebuild |
| `BlocConsumer` | both rebuild and side-effect |

**`emit()` vs `setState()`**

| `setState()` | `emit()` |
|---|---|
| in a widget's `State` | in a Cubit/Bloc |
| rebuilds this widget | pushes onto the state stream |
| guard with `mounted` | guard with `isClosed` |

## One-line reminders

- **State** = data that changes and shows on screen. Ephemeral = one widget; app state = shared. Ask "who else needs it?" ([Q1](#q1))
- **`setState`** runs your function, marks the widget dirty, rebuilds next frame. Guard async with `mounted`. ([Q2](#q2))
- **State lives in the `State` object**, not the widget. Set up in `initState`, clean up in `dispose`. ([Q3](#q3))
- **Lifting state up** = move it to the nearest common parent; prop drilling is the pain that motivates state managers. ([Q4](#q4))
- **`InheritedWidget`** pushes data down; `updateShouldNotify` decides if dependents rebuild. It's under Provider and `Theme.of`. ([Q5](#q5))
- **Provider**: `ChangeNotifier` + `notifyListeners`. `Consumer` scopes a rebuild; `Selector` rebuilds on one field. ([Q6](#q6))
- **`watch`** in build (rebuilds), **`read`** in callbacks (once), **`select`** for one value. `watch` in a callback throws. ([Q7](#q7))
- **BLoC** = event in → stream of states out. Modern API: `on<Event>()` + `Emitter`. Logic stays out of the UI. ([Q8](#q8))
- **Cubit** = BLoC without events; call methods, `emit` state. Pick Cubit for simple, Bloc for complex/traceable. ([Q9](#q9))
- **Builder** rebuilds, **Listener** does one-shot actions, **Consumer** does both. SnackBars go in a Listener. ([Q10](#q10))
- **`buildWhen`/`listenWhen`** filter rebuilds/effects; default is always rebuild. Keep the check cheap. ([Q11](#q11))
- **`emit` after `close()` throws** — guard with `if (!isClosed)`, like `mounted` for widgets. ([Q12](#q12))
- **Riverpod** providers are global (no tree, no "not found" crash). `ref.watch/read/listen`; `AsyncValue.when`; `autoDispose`. ([Q13](#q13))
- **GetX**: `.obs` + `Obx` auto-rebuild, `GetBuilder` + `update()` manual. Low boilerplate, but global magic hurts testing. ([Q14](#q14))
- **Sealed union states** make impossible states unrepresentable and force an exhaustive `switch` — no `default`. ([Q15](#q15))
- **Share across unrelated screens** by lifting above both (common ancestor or global Riverpod). Never a plain global variable. ([Q16](#q16))
- **Choosing a tool** = weigh team, testability, complexity. Mixing tools is fine. Never be dogmatic. ([Q17](#q17))
- **Test with `blocTest`**: `build` → `act` → `expect`. It skips the initial state, so don't list it. ([Q18](#q18))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers rarely stop at one question. They keep digging to test your depth. Practice answering this chain out loud — calmly, step by step:

1. *"How do you manage a simple toggle?"* → `setState`; it's ephemeral state in one widget.
2. *"Now the login state must be shared across screens — what changes?"* → lift it out: a BLoC/Cubit or a Riverpod provider above both screens.
3. *"Why a BLoC over `setState` here?"* → shared, testable, logic out of the UI; states flow one way (event in → state out).
4. *"You `await` a login, the user leaves — what bug appears?"* → emit after close throws `StateError`; guard with `if (!isClosed)`.
5. *"How do you model the loading/success/error states?"* → a sealed union, so the `switch` is exhaustive and impossible states can't exist.
6. *"How would you prove the UI rebuilds only when needed?"* → scope with `buildWhen`/`Selector` and check "Track Widget Rebuilds" in Flutter DevTools.

Being able to calmly go step by step like this — without guessing — is exactly what makes you sound **senior**, in both remote and BD interviews.

[↑ Back to top](#toc)

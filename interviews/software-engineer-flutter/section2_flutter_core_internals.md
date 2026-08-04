# Section 2 — Flutter Core Internals

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

**A. The three trees & widget identity**
1. [The three trees — Widget, Element, RenderObject](#q1) · *Very common*
2. [Why are widgets immutable?](#q2) · *Common*
3. [Keys — Value, Object, Unique, Global, Local](#q3) · *Very common*
4. [How Flutter reuses widgets (reconciliation)](#q4) · *Common*

**B. Widgets & state**
5. [StatelessWidget vs StatefulWidget](#q5) · *Very common*
6. [The full StatefulWidget lifecycle](#q6) · *Very common*
7. [What does `setState` really do?](#q7) · *Very common*
8. [What is BuildContext?](#q8) · *Very common*
9. [InheritedWidget & how Provider is built on it](#q9) · *Very common*

**C. Performance — const, repaints, threads**
10. [How `const` prevents rebuilds](#q10) · *Common*
11. [RepaintBoundary — isolating repaints](#q11) · *Common*
12. [How Flutter hits 60/120fps — UI thread vs raster thread](#q12) · *Very common*

**D. Layout & constraints**
13. [The layout rule — constraints down, sizes up, parent sets position](#q13) · *Very common*
14. [BoxConstraints — tight, loose, unbounded](#q14) · *Common*
15. ["RenderFlex overflowed" — why and how to fix](#q15) · *Very common*
16. [MediaQuery vs LayoutBuilder](#q16) · *Common*

**E. The rendering pipeline & graphics**
17. [The rendering pipeline — from tap to pixels](#q17) · *Common*
18. [Impeller vs Skia — why Flutter switched](#q18) · *Common*

**F. Tooling & the dev loop**
19. [Hot Reload vs Hot Restart vs Full Restart](#q19) · *Very common*
20. [pub.dev, pubspec.yaml & version constraints](#q20) · *Common*
21. [Flutter SDK channels — stable, beta, master](#q21) · *Common*

**G. How Flutter & Dart fit together (deep architecture)**
22. [The three layers — Embedder, Engine, Framework](#q22) · *Deeper*
23. [How Dart runs inside the engine (JIT vs AOT)](#q23) · *Deeper*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 23 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — The mental model (start here).** Nothing else makes sense without this.
→ [Q1 Three trees](#q1) · [Q5 Stateless vs Stateful](#q5) · [Q7 setState](#q7) · [Q8 BuildContext](#q8)

**Stage 2 — State & lifecycle (the daily work).**
→ [Q6 Lifecycle](#q6) · [Q9 InheritedWidget & Provider](#q9) · [Q3 Keys](#q3) · [Q2 Why widgets are immutable](#q2)

**Stage 3 — Layout (where bugs happen).**
→ [Q13 Constraints down, sizes up](#q13) · [Q15 RenderFlex overflow](#q15) · [Q14 BoxConstraints](#q14) · [Q16 MediaQuery vs LayoutBuilder](#q16)

**Stage 4 — Performance (the senior signal).**
→ [Q10 const & rebuilds](#q10) · [Q12 60/120fps & threads](#q12) · [Q11 RepaintBoundary](#q11) · [Q4 Reconciliation](#q4)

**Stage 5 — Deep internals (tie-breakers, do last).**
→ [Q17 Rendering pipeline](#q17) · [Q18 Impeller vs Skia](#q18) · [Q22 Three layers](#q22) · [Q23 JIT vs AOT inside the engine](#q23) · [Q19 Hot reload](#q19) · [Q20 pubspec](#q20) · [Q21 Channels](#q21)

**Short on time (1 hour before the interview)?** Just review these eight:
[Q1](#q1) · [Q3](#q3) · [Q5](#q5) · [Q7](#q7) · [Q8](#q8) · [Q12](#q12) · [Q13](#q13) · [Q15](#q15), then read the [Cheat Sheet](#cheatsheet).

---

# A. The three trees & widget identity

---

<a id="q1"></a>
## 1. Explain the three trees in Flutter — Widget, Element, and RenderObject. Why does Flutter need all three?

> Very common · Medium

**Short answer (say this):**
"Flutter keeps three trees that work together. The Widget tree is the cheap blueprint I write in code. The Element tree is the living bridge that remembers each widget's place and state. The RenderObject tree does the real layout and painting. Flutter needs all three so it can throw away and rebuild cheap widgets constantly, while reusing the expensive render objects underneath."

**Let's understand it fully:**

**Step 1 — A real-life picture: blueprint, site manager, building.**
Think of building a house:
- The **Widget** is the *blueprint* — a piece of paper that says "blue door here." Paper is cheap; you can redraw it many times.
- The **Element** is the *site manager* — a real person who stands on the spot, remembers what was built there, and decides what actually needs changing.
- The **RenderObject** is the *real building* — bricks and walls. Expensive to build, so you don't tear it down for a small change.

**Step 2 — The Widget tree (cheap blueprint, immutable).**
Widgets are the objects you write. They only *describe* the UI. They are immutable and cheap, so Flutter happily throws them away and makes new ones on every rebuild.

```dart
Container(
  color: Colors.blue,
  child: const Text('Hello'),
)
```

**Step 3 — The Element tree (the living bridge).**
When a widget is first shown, Flutter "inflates" it into an **Element**. The element holds the widget's position in the tree, keeps the `State` object (for stateful widgets), and points to the render object. Elements are long-lived — they survive across rebuilds, which is exactly why your state survives.

**Step 4 — The RenderObject tree (real layout and paint).**
Render objects know their size and position, and how to paint. They are expensive to create, so Flutter avoids making new ones.

```dart
// What you write:    Container → Text
// Element tree:      ContainerElement → TextElement   (long-lived)
// RenderObject tree: RenderDecoratedBox → RenderParagraph (expensive, reused)
```

**Step 5 — Why three? The whole point is speed.**
On every `setState`, Flutter makes a fresh Widget tree (cheap). The Element looks at the old widget and the new widget. If the type and key match, it keeps the same element and the same render object, and only updates the changed properties — like the color.

```dart
// setState runs → a new Container widget is created
// Element checks: same type? same key? → yes
// → REUSE the existing RenderDecoratedBox, just change its color
// → no new render object, no full rebuild of the subtree
```

So: cheap rebuilds at the widget level, expensive objects reused at the render level. That is how Flutter can rebuild 60+ times a second without dying.

**Why interviewers ask:** This is the single most fundamental Flutter architecture question. They want to see you understand the performance model — not just how to use widgets, but why rebuilding them constantly is cheap.

**Common mistake:** Saying "widgets are the things on screen." Widgets are **not** on screen — RenderObjects are. Widgets are just configuration. Another mistake is not knowing the Element tree exists at all.

**Follow-ups they may ask:**
- *"What lives where?"* → The widget holds config. The element holds the `State` and tree position. The render object holds size, position, and paint.
- *"Why is state on the Element, not the Widget?"* → Because widgets are thrown away on every rebuild. State must live on something long-lived — the element.

**Related:** [Q2 — why widgets are immutable](#q2) · [Q4 — reconciliation](#q4) · [Q8 — BuildContext is the element](#q8)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. Why are Flutter widgets immutable? Doesn't creating new widgets every frame waste memory?

> Common · Medium

**Short answer (say this):**
"Widgets are immutable because they are just a description of the UI, and a description should not change under you. Making new widgets is cheap — they are tiny config objects, and Dart's garbage collector is tuned for exactly this 'create and throw away' pattern. The expensive things, the render objects, are not recreated; they are reused through the element tree."

**Let's understand it fully:**

**Step 1 — Immutable means "cannot change after it's built."**
A widget's fields are all `final`. Once you create `Text('Hi')`, that object never changes. To show new text, you create a brand-new `Text` widget.

```dart
class Greeting extends StatelessWidget {
  final String name;            // final — cannot change
  const Greeting({required this.name});
  // ...
}
```

**Step 2 — Why immutable is a good thing.**
A widget is a *snapshot* of what the UI should look like right now. If a widget could change itself secretly, Flutter could never trust it to compare old vs new during a rebuild. Immutability makes the "did anything change?" check simple and safe.

**Step 3 — But isn't making new objects every frame wasteful?**
This is the key worry, and the answer is no, for two reasons:
1. Widgets are **tiny** — just a few fields. Creating one is almost free.
2. Dart's garbage collector uses a "most objects die young" design. Short-lived objects (like widgets) are cleaned up extremely cheaply.

**Step 4 — The expensive stuff is NOT recreated.**
You rebuild the cheap Widget tree, but the expensive RenderObject tree is reused via the Element tree (see [Q1](#q1)). So "new widgets every frame" does **not** mean "new layout objects every frame."

```dart
// Rebuild: new Text('1') widget made (cheap)
// Element reuses the SAME RenderParagraph (expensive) and updates its text
```

**Step 5 — The practical rule that follows.**
Because rebuilds are cheap, you should not fight them. Instead, keep rebuilds small and use `const` so unchanged parts are skipped entirely (see [Q10](#q10)).

**Why interviewers ask:** To see you understand that "rebuild" is cheap by design, and that you won't write hacky code to avoid rebuilds out of fear.

**Common mistake:** Trying hard to "avoid rebuilds" everywhere because you think they are expensive. The rebuild itself is cheap; what matters is keeping `build()` light and using `const`.

**Follow-ups they may ask:**
- *"If widgets are immutable, how does the UI change?"* → You build a new widget tree; the element diffs it and updates only what changed.
- *"Where does the changing data live then?"* → In the `State` object (on the element), not in the widget.

**Related:** [Q1 — three trees](#q1) · [Q10 — const skips rebuilds](#q10) · [Q7 — setState](#q7)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. What are Keys in Flutter? When do you use ValueKey, ObjectKey, UniqueKey, GlobalKey, and LocalKey?

> Very common · Medium

**Short answer (say this):**
"Keys solve the widget identity problem. When Flutter rebuilds, it matches old and new widgets by type and key. Without a key, it matches same-type widgets by position, so reordering a list attaches the wrong state to the wrong item. I use a `ValueKey` with a stable id for list items, and a `GlobalKey` only when I truly need to reach a widget's state from outside."

**Let's understand it fully:**

**Step 1 — The problem: same type, wrong identity.**
When Flutter updates a list of same-type widgets, and there is no key, it matches them by their position. So if two items swap places, the state (typed text, scroll position, animation) stays at the old position — attached to the wrong item.

```dart
// WITHOUT keys — swapping these two breaks their state,
// because Flutter matches by index, not by item.
Column(children: [
  TextField(),  // typed text stays at index 0
  TextField(),  // even if the items swap
])
```

**Step 2 — A key is like a name tag.**
A key tells Flutter "this is the *same* widget as before, even if it moved." Now Flutter follows the widget, not the slot.

**Step 3 — `LocalKey` and its three kinds (unique among siblings).**
`LocalKey` is the base for keys that only need to be unique among siblings (same parent).
- **`ValueKey<T>`** — identity from a value using `==`. Best when you have a natural id like a database id or email.
- **`ObjectKey`** — identity from an object's reference (`identical`). Use when two objects might be `==` equal but you must tell them apart by reference.
- **`UniqueKey`** — every instance is different. Use to *force* a fresh element/state ("treat this as brand new").

```dart
// ValueKey with a stable id — state follows the item
Column(
  children: items.map((item) => Dismissible(
    key: ValueKey(item.id),
    child: ListTile(title: Text(item.name)),
  )).toList(),
)
```

**Step 4 — `GlobalKey` (unique across the whole app).**
A `GlobalKey` is unique app-wide and lets you reach a widget's `State` or render object from outside. The classic use is form validation.

```dart
final formKey = GlobalKey<FormState>();

Form(
  key: formKey,
  child: ElevatedButton(
    onPressed: () {
      if (formKey.currentState!.validate()) {
        formKey.currentState!.save();
      }
    },
    child: const Text('Submit'),
  ),
)
```

**Step 5 — Force a fresh widget on purpose.**
Changing a key makes Flutter throw away the old element and build a new one. This is how `AnimatedSwitcher` knows to animate:

```dart
AnimatedSwitcher(
  duration: const Duration(milliseconds: 300),
  child: Text('$_counter', key: ValueKey<int>(_counter)),
  // new value → new key → new element → animation plays
)
```

**Why interviewers ask:** This separates developers who just patch layout bugs from those who understand the reconciliation algorithm. Key misuse causes subtle, hard-to-reproduce bugs in lists and animations.

**Common mistake:** Using `GlobalKey` everywhere "to be safe." It is expensive (global registry lookup) and blocks some optimizations. Another classic: using the list *index* as a key for a reorderable list — the index changes on reorder, so it defeats the purpose.

**Follow-ups they may ask:**
- *"Index as a key — why bad?"* → On reorder the index moves, so Flutter still matches by position. Use a stable id (`ValueKey(item.id)`).
- *"When is `UniqueKey` right?"* → When you *want* a rebuild from scratch, e.g. to replay an animation or reset state.

**Related:** [Q4 — reconciliation](#q4) · [Q1 — three trees](#q1) · [Q6 — state lives on the element](#q6)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. How does Flutter decide whether to reuse a widget or rebuild it? (Reconciliation)

> Common · Medium

**Short answer (say this):**
"On each rebuild, Flutter walks the new widget tree next to the old element tree and asks one question per spot: does the new widget have the same type and key as the old one? If yes, it reuses the element and render object and just updates properties. If no, it throws the old one away and inflates a new one."

**Let's understand it fully:**

**Step 1 — Reconciliation is the "what changed?" step.**
After `build()` produces a new widget tree, Flutter must turn those cheap blueprints into real updates without rebuilding everything. That matching process is called reconciliation (or diffing).

**Step 2 — The rule: same `runtimeType` AND same `key` → reuse.**
At each position, Flutter compares the old widget with the new widget:
- Same type and same key → **reuse** the element and render object, just update the changed fields.
- Different type or different key → **discard** the old element (and its state) and build a fresh one.

```dart
// Old: Container(color: blue)   New: Container(color: red)
// Same type, same key → reuse the RenderDecoratedBox, change color only.

// Old: Container(...)           New: SizedBox(...)
// Different type → discard the old element + state, build SizedBox fresh.
```

**Step 3 — This is per-position, top to bottom.**
Flutter does not search the whole tree for a match. It compares position by position. That is why reordering a list without keys confuses it — the widget at slot 1 is compared to whatever used to be at slot 1.

**Step 4 — Keys override position matching.**
A key lets Flutter match by identity instead of slot, so it can move an element to a new position and keep its state (see [Q3](#q3)).

**Step 5 — Why this matters for performance.**
Because reuse keeps the expensive render objects, a rebuild is usually just "update a few properties." This is the mechanism that makes the three-tree design (see [Q1](#q1)) fast in practice.

**Why interviewers ask:** It proves you understand *why* keys exist and *why* changing a widget's type resets its state. It connects the three trees to real behavior.

**Common mistake:** Thinking Flutter does a deep "smart diff" that can find a moved widget anywhere. It only checks type and key, position by position — that is why keys are needed.

**Follow-ups they may ask:**
- *"What happens to State when the type changes?"* → The old element and its `State` are thrown away; a brand-new `State` is created.
- *"Why does wrapping a widget in a new parent reset its state?"* → Its position/type in the tree changed, so it no longer matches the old element.

**Related:** [Q3 — keys](#q3) · [Q1 — three trees](#q1) · [Q10 — const short-circuits this](#q10)

[↑ Back to top](#toc)

---

# B. Widgets & state

---

<a id="q5"></a>
## 5. What is the difference between StatelessWidget and StatefulWidget? What is different internally?

> Very common · Easy–Medium

**Short answer (say this):**
"A StatelessWidget has no changing data — it only rebuilds when its parent gives it new inputs. A StatefulWidget owns changing data in a separate `State` object and can rebuild itself by calling `setState`. The key internal point: the `State` lives on the Element, not on the widget, which is why state survives rebuilds."

**Let's understand it fully:**

**Step 1 — StatelessWidget: output depends only on input.**
It cannot change on its own. Give it the same inputs and it always builds the same thing. It rebuilds only when the parent passes new constructor values.

```dart
class Greeting extends StatelessWidget {
  final String name;
  const Greeting({required this.name});

  @override
  Widget build(BuildContext context) => Text('Hello, $name');
}
```

**Step 2 — StatefulWidget: owns changing data.**
It pairs an immutable widget with a long-lived `State` object. The `State` can change its own fields and call `setState` to rebuild.

```dart
class Counter extends StatefulWidget {
  const Counter({super.key});
  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _count = 0;
  @override
  Widget build(BuildContext context) => TextButton(
        onPressed: () => setState(() => _count++),
        child: Text('Count: $_count'),
      );
}
```

**Step 3 — The internal difference (this is the senior point).**
- `StatelessWidget` → creates a `StatelessElement` → the element calls `widget.build(context)`.
- `StatefulWidget` → creates a `StatefulElement` → the element calls `createState()` once, then calls `state.build(context)`.

The `State` object is attached to the **Element**, which is long-lived. The widget itself is thrown away on every rebuild. That is exactly why `_count` survives: it lives on the element's `State`, not on the widget.

**Step 4 — When to use each.**
- `StatelessWidget` when everything comes from the constructor or inherited data (a styled label, a layout wrapper).
- `StatefulWidget` when the widget owns data that changes over its life (a form field, an `AnimationController`, a toggle).

**Why interviewers ask:** They want the state-ownership model, not just the syntax. Saying "the `State` lives on the element" shows real understanding.

**Common mistake:** Saying "a StatelessWidget can't change." It can absolutely rebuild with new data from its parent — it just can't trigger its own rebuild. Another: reaching for `StatefulWidget` when `StatelessWidget` plus a state manager (Provider, Riverpod, BLoC) would be cleaner.

**Follow-ups they may ask:**
- *"Why is the widget and State split into two classes?"* → So the widget can be immutable and disposable while the `State` stays alive on the element.
- *"Does a StatelessWidget ever rebuild?"* → Yes, whenever its parent rebuilds it with new configuration, or an `InheritedWidget` it depends on changes.

**Related:** [Q6 — lifecycle](#q6) · [Q7 — setState](#q7) · [Q2 — immutability](#q2)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. Walk through the full StatefulWidget lifecycle. When is each method called, and what do you do in it?

> Very common · Medium

**Short answer (say this):**
"The order is: `createState`, then `initState` for one-time setup, then `didChangeDependencies` where it's safe to read inherited widgets, then `build`. While alive, `didUpdateWidget` runs when the parent passes new config, and `build` runs on every rebuild. At the end, `deactivate` then `dispose`, where I clean up controllers and subscriptions."

**Let's understand it fully:**

**Step 1 — `createState()`.**
Called once when the framework inflates the widget. It creates the `State` object. You never call it yourself.

**Step 2 — `initState()`.**
Called once, right after the `State` is created and put in the tree. Do one-time setup here: create `AnimationController`s, subscribe to streams, set initial values. You **cannot** do inherited-widget lookups here yet (the element isn't fully mounted).

**Step 3 — `didChangeDependencies()`.**
Called right after `initState`, and again whenever an `InheritedWidget` you depend on changes. This is the first **safe** place to use `context` for inherited lookups like `Theme.of` or `MediaQuery.of`.

**Step 4 — `build()`.**
Called whenever the widget must render: after `setState`, after `didChangeDependencies`, or when the parent rebuilds. It must be **pure and fast** — no side effects, no heavy work.

**Step 5 — `didUpdateWidget(oldWidget)`.**
Called when the parent rebuilds and gives a new widget of the same type. Compare old vs new config and react — e.g. update a controller if a duration changed.

**Step 6 — `deactivate()` then `dispose()`.**
`deactivate` runs when the element is removed (it might be reinserted via a `GlobalKey`). `dispose` runs when the `State` is gone for good. Clean up everything in `dispose`: cancel timers, dispose controllers, close streams, remove listeners.

```dart
class _MyWidgetState extends State<MyWidget>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final StreamSubscription _sub;

  @override
  void initState() {
    super.initState();                         // call super FIRST
    _controller = AnimationController(
      vsync: this,
      duration: widget.duration,
    );
    _sub = myStream.listen(_onData);
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final locale = Localizations.localeOf(context); // safe here
  }

  @override
  void didUpdateWidget(MyWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.duration != oldWidget.duration) {
      _controller.duration = widget.duration;
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    _sub.cancel();
    super.dispose();                           // call super LAST
  }

  @override
  Widget build(BuildContext context) => const SizedBox();
}
```

**Why interviewers ask:** It directly tests whether you write leak-free code. A missed `dispose()` is one of the most common causes of memory leaks and "setState called after dispose" crashes.

**Common mistake:** Forgetting `super.initState()` first and `super.dispose()` last. Doing inherited lookups (`MediaQuery.of`) in `initState`. Not cancelling listeners in `dispose`.

**Follow-ups they may ask:**
- *"Why not read MediaQuery in initState?"* → The element isn't mounted yet, so the inherited ancestors aren't reachable. Use `didChangeDependencies`.
- *"What's the difference between `didChangeDependencies` and `didUpdateWidget`?"* → `didChangeDependencies` reacts to inherited-widget changes; `didUpdateWidget` reacts to the parent passing new config.

**Related:** [Q8 — BuildContext](#q8) · [Q7 — setState](#q7) · [Q9 — InheritedWidget](#q9)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. What does `setState` actually do? Why is it not just "refresh the screen"?

> Very common · Medium

**Short answer (say this):**
"`setState` does two things: it runs the function I give it so I can change my state fields, then it marks this element as dirty so Flutter schedules a rebuild on the next frame. It does not paint immediately, and it does not rebuild the whole app — only this element's subtree is rebuilt."

**Let's understand it fully:**

**Step 1 — `setState` is "change data, then mark dirty."**
The function you pass is where you mutate your fields. After it runs, `setState` calls `markNeedsBuild()` on the element, which adds the element to a list of dirty elements.

```dart
setState(() {
  _count++;          // change the data here
});
// Flutter now knows: this element is dirty, rebuild it next frame
```

**Step 2 — It does NOT rebuild right now.**
`setState` does not paint on the spot. Flutter waits for the next vsync (frame), then rebuilds all dirty elements together. So calling `setState` five times in a row still results in one rebuild.

**Step 3 — Only this subtree rebuilds, not the app.**
Flutter rebuilds from the dirty element down. Parents and siblings are untouched (unless they were also marked dirty). This is why `const` children are skipped — they didn't change (see [Q10](#q10)).

**Step 4 — Why the function form (not just a flag)?**
Putting the change *inside* `setState(() { ... })` makes it obvious which state changed, and guarantees the mutation happens before the rebuild is scheduled. Changing the field outside and then calling `setState(() {})` works but is considered poor style.

**Step 5 — The number one bug: `setState` after dispose.**
If an async task finishes after the widget is gone, calling `setState` crashes. Guard with `mounted`:

```dart
Future<void> load() async {
  final data = await api.fetch();
  if (!mounted) return;      // widget gone? stop here
  setState(() => _data = data);
}
```

**Why interviewers ask:** Many people think `setState` instantly redraws everything. They want to hear: it marks dirty and schedules one rebuild of this subtree on the next frame.

**Common mistake:** Doing heavy work *inside* the `setState` callback. The callback should only assign fields. Compute first, then `setState` to assign the result. Also forgetting the `mounted` check in async code.

**Follow-ups they may ask:**
- *"Does `setState` rebuild parents?"* → No. It marks this element dirty; the rebuild starts here and goes down.
- *"What if I call setState 3 times quickly?"* → You still get one rebuild on the next frame; dirty elements are batched.

**Related:** [Q5 — Stateful state lives on element](#q5) · [Q10 — const skips rebuilds](#q10) · [Q12 — frames](#q12)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is BuildContext? Why can't you use it before `initState` finishes?

> Very common · Medium

**Short answer (say this):**
"BuildContext *is* the Element — `Element` implements `BuildContext`. It represents this widget's exact spot in the element tree, and it's how you walk up to find inherited widgets, theme, or media data. You can't use it for inherited lookups in `initState` because the element isn't fully mounted in the tree yet."

**Let's understand it fully:**

**Step 1 — The big reveal: context is the element.**
People imagine `context` as some magic handle. In the Flutter source, `abstract class Element implements BuildContext`. So when you use `context`, you are talking to the element node that represents your widget's position.

**Step 2 — What it represents: your place in the tree.**
Because it is your element, it knows your ancestors. That is how `Theme.of(context)`, `MediaQuery.of(context)`, and `Navigator.of(context)` work — they walk up from your element to find the nearest matching ancestor.

**Step 3 — Why `initState` can't do inherited lookups.**
During `initState`, the element exists but is not yet fully *active* in the tree, so the inherited-widget ancestor chain isn't reachable for it. `dependOnInheritedWidgetOfExactType` needs the element to be active. So lookups crash or return null there.

```dart
@override
void initState() {
  super.initState();
  // WRONG — element not fully mounted yet:
  // final size = MediaQuery.of(context).size;

  // OK — reading widget config needs no tree walk:
  print(widget.title);
}

@override
void didChangeDependencies() {
  super.didChangeDependencies();
  // CORRECT — first safe place to walk the tree:
  final size = MediaQuery.of(context).size;
}
```

**Step 4 — The async trap: a "stale" context.**
After an `await`, the widget may already be disposed, so its context is dead. Using it then throws "looking up a deactivated widget's ancestor." Always check `mounted` first.

```dart
Future<void> go() async {
  await Future.delayed(const Duration(seconds: 2));
  if (!mounted) return;
  Navigator.of(context).pop();   // safe now
}
```

**Why interviewers ask:** It tests whether you understand tree mounting and the difference between compile-time widget config and runtime tree relationships.

**Common mistake:** Saying "context is a reference to the widget." It is not — it **is** the element. Also using a context in async callbacks after the widget might be gone.

**Follow-ups they may ask:**
- *"Why does `context.read` work but `context.watch` not in initState?"* → Both ultimately need the active element; do reads in `initState` only via `context.read` carefully, and prefer `didChangeDependencies` for anything that depends on inherited data.
- *"What is `mounted`?"* → A flag on `State` that is true while the element is in the tree. Check it before using `context` after an `await`.

**Related:** [Q1 — context is the element](#q1) · [Q6 — lifecycle](#q6) · [Q9 — InheritedWidget lookups](#q9)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What is InheritedWidget? How does it pass data down, and how is Provider built on top of it?

> Very common · Medium–Hard

**Short answer (say this):**
"InheritedWidget pushes data down the tree so any descendant can read it in O(1) with `dependOnInheritedWidgetOfExactType`. When it updates, only the widgets that *registered* a dependency on it rebuild — not the whole subtree. Provider is a friendly wrapper around it that adds lifecycle, lazy creation, and a cleaner API like `context.watch` and `Consumer`."

**Let's understand it fully:**

**Step 1 — The problem: passing data through many layers.**
Without it, you would pass data down through every constructor ("prop drilling"). InheritedWidget lets a deep child grab the data directly.

**Step 2 — How a child reads it (and why it's fast).**
The framework keeps a map of inherited widgets by type at each element, so looking up the nearest one is O(1) — not a slow walk. The call also *registers* your element as a dependent.

```dart
class AppTheme extends InheritedWidget {
  final Color primaryColor;
  const AppTheme({required this.primaryColor, required super.child});

  static AppTheme of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<AppTheme>()!;

  @override
  bool updateShouldNotify(AppTheme oldWidget) =>
      primaryColor != oldWidget.primaryColor;
}

// any descendant:
final theme = AppTheme.of(context);   // O(1) lookup + registers dependency
```

**Step 3 — Only dependents rebuild (the key efficiency).**
When the InheritedWidget is replaced and `updateShouldNotify` returns true, the framework calls `didChangeDependencies` and marks **only the registered dependents** for rebuild — not the entire subtree.

**Step 4 — `dependOn...` vs `getInheritedWidget...`.**
- `dependOnInheritedWidgetOfExactType` → reads **and** registers a dependency (you rebuild on change).
- `getInheritedWidgetOfExactType` → just reads, no dependency, no rebuild.

**Step 5 — How Provider sits on top.**
Provider creates an InheritedWidget under the hood and gives you a nicer API: `context.watch<T>()` (read + rebuild), `context.read<T>()` (read once, no rebuild), and `Consumer<T>`. It also handles lazy creation, disposing resources, and change notification via `ChangeNotifier`.

```dart
ChangeNotifierProvider<CartModel>(
  create: (_) => CartModel(),
  child: Consumer<CartModel>(
    builder: (ctx, cart, _) => Text('${cart.itemCount}'),
  ),
)
```

**Why interviewers ask:** InheritedWidget is the backbone of almost every state solution — Provider, Riverpod's `ProviderScope`, Theme, MediaQuery, Navigator. Understanding it means understanding how data flows in Flutter.

**Common mistake:** Thinking it rebuilds the whole subtree. Only registered dependents rebuild. Also confusing `dependOn...` (registers + rebuilds) with `get...` (just reads).

**Follow-ups they may ask:**
- *"What is `updateShouldNotify`?"* → It decides whether dependents should rebuild when the inherited data changes. Return true only if the value actually changed.
- *"Why is the lookup O(1)?"* → Each element caches its inherited widgets by type in a map, so finding the nearest one is a direct lookup, not a tree walk.

**Related:** [Q6 — didChangeDependencies](#q6) · [Q8 — BuildContext](#q8) · [Q16 — MediaQuery uses this](#q16)

[↑ Back to top](#toc)

---

# C. Performance — const, repaints, threads

---

<a id="q10"></a>
## 10. How does a `const` constructor prevent widget rebuilds? What does `const` mean at the tree level?

> Common · Medium

**Short answer (say this):**
"A `const` widget is built at compile time and canonicalized — every `const Text('Hello')` in the app is the exact same object in memory. During reconciliation, when the parent rebuilds, Flutter sees the new child is the *identical* object as the old one, so it skips rebuilding that whole subtree instantly. No `build` call, no diffing."

**Let's understand it fully:**

**Step 1 — `const` builds the object before the app runs.**
With a const constructor and a const call, Dart creates the widget at compile time and reuses one shared instance everywhere (canonicalization).

**Step 2 — The reconciliation short-circuit.**
When the parent rebuilds, Flutter compares old child vs new child. If they are the **identical** object (which `const` guarantees), Flutter stops right there — "nothing changed" — and skips the subtree.

```dart
class _ParentState extends State<Parent> {
  int _counter = 0;

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      const Text('I never rebuild'),     // identical object → skipped
      const ExpensiveWidget(),           // its build() won't run again
      Text('Counter: $_counter'),        // NOT const → rebuilds each time
      ElevatedButton(
        onPressed: () => setState(() => _counter++),
        child: const Text('Increment'),  // even this child is const
      ),
    ]);
  }
}
```

**Step 3 — Same data is NOT the same as `const`.**
Two `Text('Hello')` without `const` are two *different* objects, so Flutter still calls `build` and compares properties. With `const`, the `identical()` check is true immediately, so it bails out faster.

**Step 4 — The three requirements for a widget to be const.**
1. It has a `const` constructor.
2. All its fields are `final`.
3. All the arguments you pass are compile-time constants.

**Step 5 — The limit: const only stops *parent-triggered* rebuilds.**
If a const widget depends on an `InheritedWidget` that changes (like Theme), it still rebuilds — because that is a dependency change, not a parent rebuild.

**Why interviewers ask:** It tests whether "use const everywhere" is something you memorized or understood. The real reason is identical-object reuse plus the reconciliation short-circuit.

**Common mistake:** Thinking `const` prevents *all* rebuilds. It only stops rebuilds caused by the parent reconstructing. Also thinking `final` alone is enough — `final` stops reassignment, but `const` makes the whole object a compile-time constant.

**Follow-ups they may ask:**
- *"What if one value comes from the network?"* → It can't be `const`. Keep the changing part separate and make the rest `const`.
- *"Does const help if the widget watches an InheritedWidget?"* → Not against that dependency — it will still rebuild when the inherited data changes.

**Related:** [Q4 — reconciliation](#q4) · [Q2 — immutability](#q2) · [Q12 — fewer rebuilds = smoother frames](#q12)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What is RepaintBoundary? How does it reduce repaints, and when should you add it?

> Common · Medium

**Short answer (say this):**
"A RepaintBoundary puts its subtree on its own paint layer. Without it, when something needs repainting, Flutter repaints everything up to the nearest boundary, which can be a large region. With it, a frequently-changing area repaints alone, without forcing its expensive neighbors to repaint."

**Let's understand it fully:**

**Step 1 — A real-life picture: separate sheets of glass.**
Imagine painting on layers of glass stacked on top of each other. If everything is on one sheet, changing one thing means repainting the whole sheet. A RepaintBoundary gives the changing thing its **own** sheet, so you only repaint that one.

**Step 2 — How repaint regions work by default.**
When a render object needs repainting, Flutter walks up to the nearest repaint boundary and repaints everything inside it. If that boundary is far up, a big region repaints unnecessarily.

**Step 3 — Inserting a boundary isolates the change.**
You are telling Flutter: "the inside changes on its own; don't repaint the outside when the inside changes."

```dart
// WITHOUT — the spinner forces the whole column to repaint
Column(children: [
  ExpensiveHeader(),
  CircularProgressIndicator(),   // animates ~60fps
  ExpensiveFooter(),
])

// WITH — only the spinner's layer repaints
Column(children: [
  const ExpensiveHeader(),
  RepaintBoundary(child: CircularProgressIndicator()),
  const ExpensiveFooter(),
])
```

**Step 4 — When to add it (and when not to).**
Add it around something that repaints often while its neighbors don't: an animation, a video, custom canvas drawing. Do **not** add it everywhere — each boundary makes a new compositing layer that uses GPU memory, so overuse can make things worse.

**Step 5 — Flutter already adds some for you.**
`ListView` items and `Navigator` routes already get RepaintBoundaries, so you don't need to add your own there.

**Why interviewers ask:** It tests advanced rendering knowledge — knowing *when* repaints happen and how to isolate them is what lets you ship 60fps on low-end devices.

**Common mistake:** Wrapping everything in RepaintBoundary. Each one costs GPU memory; too many can exhaust texture memory and hurt performance. Also thinking it helps layout — it does not; layout still flows through it normally.

**Follow-ups they may ask:**
- *"How do you check if it helps?"* → DevTools → "Highlight Repaints". Regions that flash together should be split with a boundary.
- *"Does it help with layout cost?"* → No, only paint. Layout still propagates normally.

**Related:** [Q12 — raster thread cost](#q12) · [Q17 — paint phase](#q17)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. How does Flutter hit 60/120fps? What are the UI thread and the raster thread?

> Very common · Medium–Hard

**Short answer (say this):**
"Flutter has a frame budget of about 16ms at 60fps, or 8ms at 120fps. It uses multiple threads: the UI thread runs my Dart code — build, layout, and building the layer tree — and the raster thread turns those layers into pixels on the GPU. Because they run in parallel, the raster thread can paint frame N while the UI thread builds frame N+1."

**Let's understand it fully:**

**Step 1 — The frame budget.**
At 60fps each frame must finish in ~16ms; at 120fps in ~8ms. Miss the budget and you drop a frame — that is jank.

**Step 2 — The UI thread (your Dart code).**
This runs `build()`, layout, hit-testing, gestures, and animation ticks. Its output is a **LayerTree** — a set of paint instructions, *not* pixels yet.

**Step 3 — The raster thread (the GPU work).**
It takes the LayerTree and rasterizes it into actual pixels on the GPU. It runs on a *separate* thread, so even slow rasterization doesn't block the UI thread.

**Step 4 — Two more threads.**
- **Platform thread** — platform messages, plugin calls, system events.
- **I/O thread** — heavy I/O like image decoding, so it doesn't block the UI thread.

**Step 5 — The diagnosis that changes the fix.**
This is the senior point. Open DevTools and look at the two bars:
- **UI bar is red (>16ms)** → your *Dart* is the problem: heavy `build()`, big synchronous work. Fix with `const`, fewer widgets, or move CPU work to an isolate.
- **Raster bar is red** → the *GPU* is the problem: too much overdraw, expensive shadows/clips. Fix with `RepaintBoundary`, simpler effects.

```dart
// Jank: heavy work on the UI thread blocks frames
void onTap() {
  setState(() {
    _data = expensiveComputation();   // 50ms → misses ~3 frames
  });
}

// Fix: move CPU-heavy work off the UI thread with an isolate
void onTap() async {
  final result = await compute(expensiveComputation, input);
  if (!mounted) return;
  setState(() => _data = result);
}
```

**Why interviewers ask:** This is the ultimate performance question. It tests whether you can tell *where* the jank is — UI thread (your code) vs raster thread (GPU) — because the fix is completely different.

**Common mistake:** Saying "Flutter is single-threaded." It has at least four threads. Also blaming all jank on the GPU — if the UI bar is red, the problem is your Dart code. And remember `async`/`await` does **not** create a new thread; only isolates give true parallel CPU work.

**Follow-ups they may ask:**
- *"Why does shader jank stall the raster thread?"* → Old Skia compiled shaders at runtime, stalling the raster thread on first use (see [Q18](#q18)).
- *"Why does my 60fps app jank on a 120Hz phone?"* → The budget drops from 16ms to 8ms, so marginal work now misses frames.

**Related:** [Q11 — RepaintBoundary](#q11) · [Q17 — rendering pipeline](#q17) · [Q18 — Impeller](#q18)

[↑ Back to top](#toc)

---

# D. Layout & constraints

---

<a id="q13"></a>
## 13. Explain Flutter's layout rule: "constraints go down, sizes go up, parent sets position." Walk through an example.

> Very common · Medium

**Short answer (say this):**
"Layout is a single pass with three rules. A parent passes constraints (min/max width and height) down to each child. Each child picks its own size within those constraints and reports it back up. Then the parent places the child — the child never knows its own position. Because it's one walk down and up, layout is O(n)."

**Let's understand it fully:**

**Step 1 — A real-life picture: a tailor and a customer.**
The parent is the tailor who says "your shirt must be between size S and L" (constraints down). The child customer picks a size in that range and says "I'll take M" (size up). Then the tailor decides where the customer stands in the photo (parent sets position).

**Step 2 — Rule 1: constraints go down.**
A parent gives each child a `BoxConstraints`: `minWidth, maxWidth, minHeight, maxHeight`. The child *must* end up within these.

**Step 3 — Rule 2: sizes go up.**
The child chooses its own size inside the constraints and reports it back. It cannot pick a size outside the allowed range.

**Step 4 — Rule 3: parent sets position.**
The child does not know where it will be placed; only the parent knows (stored in the parent data as an offset). A child's `size` says nothing about its position.

```dart
// Screen is 400 x 800
SizedBox(            // gets 0≤w≤400, 0≤h≤800
  width: 300,
  height: 200,       // passes tight 0≤w≤300, 0≤h≤200 down
  child: Center(     // receives 0≤w≤300, 0≤h≤200
                     // passes LOOSE 0≤w≤300, 0≤h≤200 down
    child: Container( // receives those loose constraints
      width: 100,
      height: 50,     // picks 100x50, reports size UP
      color: Colors.blue,
    ),
    // Center is 300x200, child is 100x50
    // → Center POSITIONS the child at offset (100, 75) to center it
  ),
)
```

**Step 5 — Why it's a single pass (O(n)).**
Constraints flow down once and sizes flow up once, in one depth-first walk. It is **not** multi-pass like CSS. That is a big reason Flutter layout is fast.

**Why interviewers ask:** This is the foundation of every layout bug. "RenderFlex overflowed," "unbounded constraints," and sizing surprises all come from misunderstanding this flow. They want proof you can debug layout without trial and error.

**Common mistake:** Saying "a child knows its position." It does not. Also thinking layout is multi-pass like CSS. And assuming a widget "has" a fixed size — a `Container()` with no explicit size behaves completely differently depending on the constraints flowing in.

**Follow-ups they may ask:**
- *"Where is a child's position stored?"* → In the parent data (an offset), set by the parent — not on the child itself.
- *"Why is layout O(n)?"* → Each render object is visited once on the way down (constraints) and once on the way up (size).

**Related:** [Q14 — BoxConstraints](#q14) · [Q15 — overflow](#q15) · [Q16 — LayoutBuilder gives constraints](#q16)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. What are BoxConstraints? Explain tight vs loose, and what "unbounded" means.

> Common · Medium

**Short answer (say this):**
"BoxConstraints are four numbers: min and max width, min and max height. Tight means min equals max, so the child has no choice. Loose means min is 0, so the child can be any size up to the max. Unbounded means a max is infinity, which happens inside scrollables — and a widget that tries to fill all space will then try to be infinitely big and error."

**Let's understand it fully:**

**Step 1 — The four numbers.**
Every `RenderBox` receives `minWidth, maxWidth, minHeight, maxHeight` from its parent and must choose a size within them.

**Step 2 — Tight constraints (no choice).**
`minWidth == maxWidth` (and/or the height pair are equal). The child must be exactly that size. The screen passes tight constraints to your root, forcing it to fill the screen.

```dart
BoxConstraints.tight(const Size(200, 200));
// min=max=200 in both axes → child MUST be 200x200
```

**Step 3 — Loose constraints (freedom up to a max).**
`minWidth = 0`, so the child can be anywhere from 0 to max. `Center` loosens constraints — "be as small as you want, up to my size."

```dart
BoxConstraints.loose(const Size(200, 200));
// min=0, max=200 → child can be 0..200
```

**Step 4 — Unbounded constraints (max is infinity).**
Scrollables like `ListView` pass `maxHeight = double.infinity` in the scroll direction, because children can be any height. The trouble: a widget that wants to be as big as possible (a bare `Container()`, or `Expanded`) tries to become infinitely large and errors.

```dart
// CRASHES — Column has infinite height inside ListView
ListView(children: [
  Column(children: [
    Expanded(child: Text('Boom')),
    // remaining space = infinity → "unbounded height" error
  ]),
])

// FIX — give the inner Column a bounded height
ListView(children: [
  SizedBox(
    height: 300,
    child: Column(children: [
      Expanded(child: Text('Works')),   // now 300 - siblings
    ]),
  ),
])
```

**Step 5 — Reading the error.**
"BoxConstraints forces an infinite ... " or "RenderFlex children have non-zero flex but incoming height constraints are unbounded" both mean: a flex/fill widget met infinity. Give it a bounded size.

**Why interviewers ask:** Almost every "RenderBox was not laid out" or "Infinity" trace comes back to a constraints mismatch. They want to see you can diagnose from the message, not randomly wrap things in `Expanded`.

**Common mistake:** Thinking `double.infinity` is itself a bug. It is intentional — scrollables use it. The bug is a child that doesn't know how to handle unbounded constraints.

**Follow-ups they may ask:**
- *"Why does `Container()` with no size sometimes fill and sometimes not?"* → It expands to fill *bounded* constraints, but errors under *unbounded* ones.
- *"How do I give a height inside a scrollable?"* → Wrap in `SizedBox`, or use `shrinkWrap: true` on the inner list.

**Related:** [Q13 — constraints flow](#q13) · [Q15 — overflow fixes](#q15) · [Q16 — LayoutBuilder](#q16)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. Why does "RenderFlex overflowed" happen, and how do you fix it?

> Very common · Easy–Medium

**Short answer (say this):**
"RenderFlex is the render object behind Row and Column. The overflow means the children's total size along the main axis is bigger than the space available. The fix depends on intent: let children share space with Flexible or Expanded, ellipsis long text, or wrap in a scroll view if the content is genuinely larger than the screen."

**Let's understand it fully:**

**Step 1 — What the error means.**
A `Row` of three 200px children in a 400px screen needs 600px but has 400px. The extra 200px overflows, and you see the yellow-and-black stripes.

**Step 2 — Root cause 1: fixed children exceed the parent.**
Fix with `Expanded` (children share space, each forced to fill its share) or `Flexible` (children share space but may be smaller).

```dart
// OVERFLOW — three fixed 200px items in a 400px row
Row(children: [
  Container(width: 200, height: 50, color: Colors.red),
  Container(width: 200, height: 50, color: Colors.green),
  Container(width: 200, height: 50, color: Colors.blue),
])

// FIX — Expanded shares the space
Row(children: [
  Expanded(child: Container(height: 50, color: Colors.red)),
  Expanded(flex: 2, child: Container(height: 50, color: Colors.green)),
  Expanded(child: Container(height: 50, color: Colors.blue)),
])
```

**Step 3 — Root cause 2: long text.**
Wrap the `Text` in `Expanded` and add `overflow: TextOverflow.ellipsis`.

```dart
Row(children: [
  const Icon(Icons.info),
  Expanded(
    child: Text(
      'A very long line that would overflow without Expanded',
      overflow: TextOverflow.ellipsis,
    ),
  ),
])
```

**Step 4 — Root cause 3: content should scroll.**
If the content is legitimately bigger than the screen, wrap the Row/Column in a `SingleChildScrollView`.

```dart
SingleChildScrollView(
  scrollDirection: Axis.horizontal,
  child: Row(children: tiles),
)
```

**Step 5 — Root cause 4: unbounded cascade.**
A `Column` inside a `ListView` (both vertical) gives the Column infinite height. Wrap the inner Column in a `SizedBox`, or set `shrinkWrap: true` on the inner list (see [Q14](#q14)).

**Why interviewers ask:** It is the single most common Flutter layout error. They want to see you pick the *right* fix based on intent, not randomly try wrappers.

**Common mistake:** Using `Expanded` outside a Row/Column/Flex — it only works inside flex containers. Wrapping everything in `SingleChildScrollView` as a blanket fix. Confusing `Flexible` (`FlexFit.loose`, may be smaller) with `Expanded` (`FlexFit.tight`, must fill its share).

**Follow-ups they may ask:**
- *"Flexible vs Expanded?"* → `Expanded` is `Flexible(fit: FlexFit.tight)` — it must fill its share. `Flexible` lets the child be smaller.
- *"Why does `Expanded` crash inside a ListView?"* → The main-axis constraint is unbounded (infinity), so "fill remaining space" is undefined.

**Related:** [Q13 — constraints](#q13) · [Q14 — unbounded](#q14)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. What is the difference between MediaQuery and LayoutBuilder? When do you use each?

> Common · Medium

**Short answer (say this):**
"MediaQuery gives global screen info — full screen size, padding, text scale, orientation. LayoutBuilder gives the actual constraints my widget got at its specific spot in the tree. So if my widget sits inside a 300px box, MediaQuery still reports the full screen width, but LayoutBuilder reports 300. For reusable, responsive widgets, LayoutBuilder is usually more correct."

**Let's understand it fully:**

**Step 1 — MediaQuery = info about the whole window.**
It reports screen size, device pixel ratio, text scale factor, safe-area padding (notch, status bar), orientation, and brightness. It comes from the nearest `MediaQuery` ancestor (usually set by `MaterialApp`) and is the **same** everywhere in the tree.

```dart
final screenWidth = MediaQuery.of(context).size.width;
if (screenWidth > 600) return TabletLayout();
return PhoneLayout();
```

**Step 2 — LayoutBuilder = the space YOU actually got.**
It gives you the `BoxConstraints` the parent passed to *this* spot. That is how much room your widget really has — not the whole screen.

```dart
SizedBox(
  width: 300,
  child: LayoutBuilder(
    builder: (context, constraints) {
      // constraints.maxWidth == 300, NOT the screen width
      return constraints.maxWidth > 200 ? WideVersion() : NarrowVersion();
    },
  ),
)
```

**Step 3 — The critical difference, side by side.**
Inside a `SizedBox(width: 300)` on a 400px screen:
- `MediaQuery.of(context).size.width` → **400** (whole screen).
- `LayoutBuilder` → `maxWidth: 300` (your actual space).

**Step 4 — A real responsive example.**
A grid that adapts to the space it is given, so it works in split-screen or inside a panel:

```dart
LayoutBuilder(
  builder: (context, constraints) {
    final columns = (constraints.maxWidth / 150).floor().clamp(1, 6);
    return GridView.count(crossAxisCount: columns, children: cards);
  },
)
```

**Step 5 — A rebuild gotcha with MediaQuery.**
`MediaQuery.of(context)` depends on *all* media properties, so your widget rebuilds when *any* of them change — including the keyboard appearing. To depend only on size, use `MediaQuery.sizeOf(context)`.

**Why interviewers ask:** It tests practical responsive-design knowledge. Many apps break in split-screen or when embedded in a smaller container because the dev used MediaQuery where LayoutBuilder was correct.

**Common mistake:** Using MediaQuery for layout inside nested, reusable widgets. If a widget might ever sit in a constrained parent (it usually will), LayoutBuilder is more correct. Also not knowing `MediaQuery.of` causes rebuilds on keyboard show/hide — prefer `sizeOf`.

**Follow-ups they may ask:**
- *"Why does `MediaQuery.of` rebuild on keyboard open?"* → It depends on the whole MediaQueryData, including view insets. Use `MediaQuery.sizeOf` to avoid that.
- *"Which for tablet vs phone?"* → MediaQuery for whole-screen breakpoints; LayoutBuilder for adapting to local space.

**Related:** [Q9 — MediaQuery is an InheritedWidget](#q9) · [Q13 — LayoutBuilder exposes constraints](#q13)

[↑ Back to top](#toc)

---

# E. The rendering pipeline & graphics

---

<a id="q17"></a>
## 17. Describe Flutter's rendering pipeline. How does a frame go from a tap to pixels on screen?

> Common · Medium–Hard

**Short answer (say this):**
"Each frame, triggered by a vsync signal, runs through phases: a state change marks an element dirty, then build produces new widgets, then layout sizes and positions render objects, then paint records draw commands into layers, then compositing flattens the layers, then the raster thread turns them into pixels, and finally the GPU shows the frame."

**Let's understand it fully:**

**Step 1 — Trigger: a state change marks dirty.**
A tap, scroll, or animation tick calls `setState` (or similar), which marks the element dirty and asks the engine to schedule a frame.

**Step 2 — Vsync: the frame begins.**
The platform sends a vsync callback (~every 16ms at 60fps). Flutter starts the frame work.

**Step 3 — Build phase.**
Flutter rebuilds the dirty elements by calling `build()`, then reconciles new widgets against old ones (see [Q4](#q4)), updating render-object properties where needed.

**Step 4 — Layout phase.**
Starting at the root, constraints flow down and sizes flow up in one depth-first pass; parents position children (see [Q13](#q13)).

**Step 5 — Paint phase.**
Each render object paints itself into `Layer` objects as *recorded draw commands* — not pixels yet. `RepaintBoundary` nodes create separate layers (see [Q11](#q11)).

**Step 6 — Composite, rasterize, display.**
The layer tree is flattened and handed to the engine. The **raster thread** turns it into GPU commands and actual pixels, then the GPU presents the frame.

```dart
// Tracing a tap:
ElevatedButton(
  onPressed: () => setState(() => _count++), // 1. marks dirty
  child: Text('$_count'),
)
// 2. next vsync arrives
// 3. BUILD: build() runs, Text('0') vs Text('1') → update RenderParagraph
// 4. LAYOUT: RenderParagraph re-measures text
// 5. PAINT: records new draw commands into its Layer
// 6. COMPOSITE → RASTERIZE (raster thread) → DISPLAY
// user sees '1'
```

**Why interviewers ask:** Understanding the pipeline is essential for debugging janky frames. If you know layout and paint are separate, you know a `RepaintBoundary` helps paint, not layout. If you know rasterization is on a separate thread, you understand why shader compilation causes jank.

**Common mistake:** Saying "Flutter repaints the whole screen every frame." It tracks dirty regions and repaint boundaries. Also conflating build and paint — `build()` produces widgets, not pixels. And forgetting rasterization runs on a separate thread.

**Follow-ups they may ask:**
- *"Where does build end and paint begin?"* → Build makes widgets/elements; layout sizes them; paint records draw commands; raster makes pixels.
- *"Why does a RepaintBoundary not help layout?"* → It isolates the paint layer only; layout constraints still flow through it.

**Related:** [Q12 — UI vs raster thread](#q12) · [Q13 — layout phase](#q13) · [Q18 — rasterization & shaders](#q18)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. What is Impeller, and how does it differ from Skia? Why did Flutter move to it?

> Common · Medium

**Short answer (say this):**
"Skia is the older 2D engine Flutter used; it compiled GPU shaders the first time it met a new drawing operation, which caused 'shader jank' — a stutter the first time you saw an animation. Impeller is Flutter's newer engine that compiles all shaders ahead of time, at build time, so there is no runtime shader compilation and no first-frame jank."

**Let's understand it fully:**

**Step 1 — Skia and the shader-jank problem.**
Skia is a general-purpose 2D graphics library. It compiled shaders **lazily at runtime** — the first time a particular effect appeared, the raster thread stalled (often 50–200ms) compiling the shader. You could pre-warm shaders with `--cache-sksl`, but it was fragile and manual.

**Step 2 — Impeller's core idea: compile shaders ahead of time.**
Impeller is built specifically for Flutter. All its shaders are **precompiled at engine build time**, so at runtime there is zero shader compilation. The GPU pipeline state is known in advance.

```dart
// With Skia:
// First time a complex animation appears
//   → Skia compiles its shader now → raster thread STALLS → visible stutter
//   → later frames are smooth (shader cached)

// With Impeller:
// Same animation → shaders already compiled at build time
//   → raster thread proceeds immediately → smooth from frame one
```

**Step 3 — Other differences.**
- Skia: shared, general-purpose codebase. Impeller: purpose-built for Flutter's patterns.
- Impeller uses **Metal** on iOS and **Vulkan** (OpenGL fallback) on Android.
- Impeller's win is *predictability* — even if average FPS is similar, the worst-case frames are far better.

**Step 4 — You don't change app code.**
Impeller is enabled at the engine level. As of recent Flutter releases it is the default on iOS (since 3.16) and on Android (since 3.27 generally; began 3.22).

```bash
flutter run --enable-impeller     # force Impeller
flutter run --no-enable-impeller  # force Skia
```

**Why interviewers ask:** It shows you keep up with Flutter's evolution and understand the rendering stack below the widgets. Teams shipping to low-end Android especially care, because shader jank was their top user complaint.

**Common mistake:** Saying Impeller is "faster" in every case. Its advantage is *consistency* (no jank spikes), not raw throughput. Some Skia-optimized paths may even be slightly slower on Impeller today.

**Follow-ups they may ask:**
- *"What exactly is shader jank?"* → A stall on the raster thread the first time Skia must compile a shader for a new drawing operation.
- *"Why is predictable frame time better than higher average FPS?"* → Users notice the *worst* frames (stutters), not the average.

**Related:** [Q12 — raster thread](#q12) · [Q17 — rasterization](#q17)

[↑ Back to top](#toc)

---

# F. Tooling & the dev loop

---

<a id="q19"></a>
## 19. What is the difference between Hot Reload, Hot Restart, and Full Restart? What does each reset?

> Very common · Easy–Medium

**Short answer (say this):**
"Hot Reload injects new code into the running VM and keeps all state — it just re-runs `build`, in about a second. Hot Restart restarts the Dart VM and wipes all state, re-running `main` and `initState`. Full Restart rebuilds everything including native code and reinstalls the app — needed when you touch native code, plugins, or pubspec."

**Let's understand it fully:**

**Step 1 — Hot Reload (keeps state).**
It pushes updated Dart code into the running VM **without** restarting. All `State` objects, globals, statics, and the navigation stack are preserved. It re-runs `build()` with the new code but does **not** re-run `main()` or `initState()`. About 1 second.

**Step 2 — Hot Restart (wipes Dart state).**
It restarts the Dart VM. Globals, statics, and `State` objects are recreated; `main()` and `initState()` run again. A few seconds. It does **not** recompile native Kotlin/Swift code.

**Step 3 — Full Restart / cold start (rebuilds native too).**
It stops the app, recompiles everything including native platform code, and reinstalls the APK/IPA. Needed when you change native code, add a plugin, edit `pubspec.yaml` dependencies, or change platform config. 30+ seconds.

```dart
int globalCounter = 0;

class _MyState extends State<MyWidget> {
  int localCounter = 10;

  @override
  void initState() {
    super.initState();
    globalCounter++;            // runs again only on Hot Restart
  }

  @override
  Widget build(BuildContext context) =>
      Text('L:$localCounter G:$globalCounter',
          style: const TextStyle(fontSize: 24)); // change to 32...
}

// Hot Reload after changing fontSize to 32:
//   fontSize → 32, localCounter stays 10, initState NOT called
// Hot Restart:
//   localCounter → 10 fresh, globalCounter → 0 then 1, initState called
// Full Restart needed when:
//   adding firebase_core, editing AndroidManifest.xml, new method channel
```

**Step 4 — When Hot Reload can't help.**
Hot Reload cannot apply changes to `main()`, global initializers, `initState` logic that already ran, enum definitions, or some generic type changes. When it "doesn't work," reach for Hot Restart.

**Why interviewers ask:** It is a practical productivity question. Knowing which change needs which restart level makes debugging far faster.

**Common mistake:** Expecting Hot Reload to pick up `initState` changes, enum changes, or native code changes. Also not knowing Hot Reload can't handle changes to `main()` or global initializers.

**Follow-ups they may ask:**
- *"Why doesn't Hot Reload re-run initState?"* → It preserves existing `State` objects, so their `initState` already ran; only `build` re-runs.
- *"When is Full Restart mandatory?"* → Any native change: new plugin, edited manifest/Info.plist, new platform channel.

**Related:** [Q6 — initState runs on restart](#q6) · [Q23 — JIT enables hot reload](#q23)

[↑ Back to top](#toc)

---

<a id="q20"></a>
## 20. What is pub.dev? How does pubspec.yaml manage dependencies, and how do `^`, `>=`, and `==` work?

> Common · Medium

**Short answer (say this):**
"pub.dev is the official package registry for Dart and Flutter, like npm for JavaScript. pubspec.yaml declares your project's dependencies and version rules; `flutter pub get` resolves and locks exact versions into pubspec.lock. `dependencies` ship in the app; `dev_dependencies` are only for development. The caret `^1.5.0` means `>=1.5.0 <2.0.0` and is the recommended default."

**Let's understand it fully:**

**Step 1 — pub.dev and pubspec.yaml.**
pub.dev hosts open-source packages with a score for popularity, health, and maintenance. `pubspec.yaml` at the project root declares the name, version, SDK constraints, and dependencies. `flutter pub get` resolves compatible versions and writes the exact resolved versions to `pubspec.lock` for reproducible builds.

**Step 2 — `dependencies` vs `dev_dependencies`.**
- `dependencies` — needed to **run** the app; they ship in the binary (e.g. `http`, `provider`, `flutter_bloc`).
- `dev_dependencies` — needed only for **development/testing**; they are **not** in the release build (e.g. `flutter_test`, `flutter_lints`, `mockito`, `build_runner`).

Putting a test tool in `dependencies` bloats your release binary for no reason.

**Step 3 — Semantic versioning: MAJOR.MINOR.PATCH.**
- MAJOR (`2.x.x`) — breaking changes.
- MINOR (`x.4.x`) — new features, backward-compatible.
- PATCH (`x.x.1`) — bug fixes, backward-compatible.

**Step 4 — The constraint syntax.**
- `^1.5.0` (caret) → `>=1.5.0 <2.0.0`. Allows minor/patch upgrades, not the next major. The recommended default.
- `>=1.5.0 <3.0.0` → explicit range, when you know your code works across majors.
- `==1.5.0` → exact pin. Discourages updates and causes conflicts; rarely right.
- `>=1.5.0` → open-ended, dangerous (a future major could break you).
- `any` → accepts anything; only for throwaway prototypes.

```yaml
name: my_flutter_app
version: 1.0.0+1            # appVersion+buildNumber

environment:
  sdk: '>=3.0.0 <4.0.0'
  flutter: '>=3.10.0'

dependencies:
  flutter:
    sdk: flutter
  provider: ^6.1.0         # >=6.1.0 <7.0.0
  http: ^1.2.0             # >=1.2.0 <2.0.0
  shared_models:
    path: ../shared_models # local package / monorepo

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^5.0.0    # dev only
  build_runner: ^2.4.0     # dev only
```

**Step 5 — Resolving conflicts.**
If two packages need incompatible versions of a third, the solver fails with "incompatible version constraints." Fix by loosening/upgrading constraints. As a last resort, `dependency_overrides` forces a version globally — use it only temporarily, since mismatched APIs can crash at runtime.

```bash
flutter pub deps        # dependency tree
flutter pub outdated    # available upgrades
flutter pub upgrade     # upgrade within constraints
```

**Why interviewers ask:** Every project starts with pubspec.yaml. They gauge whether you can manage real projects — resolving conflicts, structuring monorepos with path dependencies, and keeping builds small by separating dev deps.

**Common mistake:** Using `==` for everything, which makes resolution nearly impossible. Putting `build_runner`/`mockito`/`flutter_test` in `dependencies`. Also: commit `pubspec.lock` for **apps** (reproducible builds) but not for **packages** (consumers need flexible resolution).

**Follow-ups they may ask:**
- *"What does the caret `^` mean?"* → "Up to the next major" — `^1.5.0` is `>=1.5.0 <2.0.0`.
- *"Should you commit pubspec.lock?"* → Yes for apps, no for reusable packages.

**Related:** [Q21 — SDK channels & versions](#q21) · [Q23 — SDK constraints](#q23)

[↑ Back to top](#toc)

---

<a id="q21"></a>
## 21. What are Flutter's SDK channels — stable, beta, and master? Which should production use?

> Common · Easy–Medium

**Short answer (say this):**
"Stable is the production-ready track, released about quarterly and heavily tested, including by Google's own apps — it's the only channel for production. Beta is a monthly preview of nearly-final features. Master is the bleeding edge, updated many times a day, and can break anytime — only for Flutter contributors or experiments."

**Let's understand it fully:**

**Step 1 — Stable (use this in production).**
Production-ready releases, roughly quarterly (e.g. 3.22, 3.24). Extensively tested, including in Google Pay and Google Ads. APIs are frozen across patch releases (3.22.0 → 3.22.1), so no breaking changes within a stable line.

**Step 2 — Beta (preview / pre-test).**
Updated about monthly. Features are complete but still in broader testing; APIs may still change before they reach stable. Use it to try an upcoming feature or to pre-test your app against the next stable — but don't ship it to users.

**Step 3 — Master (bleeding edge).**
The `main` branch of the Flutter repo, updated with every merge, many times a day. Experimental and can break anytime. Only for contributing to Flutter or grabbing a fix that hasn't reached beta.

```bash
flutter channel              # shows current channel
flutter channel stable       # for production
flutter upgrade              # always upgrade after switching

flutter --version
# Flutter 3.24.0 • channel stable • ...
```

**Step 4 — Pin versions in CI.**
Don't rely on "latest stable" in CI. Pin a specific version so every machine builds the same thing, avoiding "works on my machine" drift.

```bash
flutter version 3.22.2       # pin a specific version in CI
```

**Step 5 — Channel vs version.**
A channel is a *release track*; a version is a *specific build*. You can be on the stable channel at version 3.22.2 — the channel says which track you follow, not which exact version.

**Why interviewers ask:** It tests professional maturity. Juniors chase shiny features on master; seniors understand release management, reproducible builds, and the cost of debugging framework bugs instead of shipping features.

**Common mistake:** Using beta/master in production because "stable lacks a feature." There is almost always a safer workaround on stable. Also not pinning the SDK version in CI. And confusing channels with versions.

**Follow-ups they may ask:**
- *"How do you test against the next release safely?"* → Run CI on beta periodically to catch breaking changes early, without shipping beta.
- *"Channel vs version — what's the difference?"* → Channel = track (stable/beta/master); version = exact build (e.g. 3.22.2).

**Related:** [Q20 — version constraints](#q20) · [Q19 — dev loop](#q19)

[↑ Back to top](#toc)

---

# G. How Flutter & Dart fit together (deep architecture)

---

<a id="q22"></a>
## 22. Explain Flutter's three architecture layers — Embedder, Engine, and Framework. How do they communicate?

> Deeper question · Hard

**Short answer (say this):**
"Flutter is three layers. The Embedder is the thin, platform-specific host that gives Flutter a window, input events, and vsync. The Engine is the C++ core that holds the Dart runtime, the rendering engine, and text layout. The Framework is the Dart layer I actually use — render objects, widgets, and Material/Cupertino. The framework sends layer trees down to the engine, and the engine sends events and vsync up."

**Let's understand it fully:**

**Step 1 — A real-life picture: stage, crew, and script.**
The Embedder is the *stage* the platform provides. The Engine is the *backstage crew* (lights, sound, the heavy machinery). The Framework is the *script and actors* you write. You work on the script; the crew turns it into a real show on the stage.

**Step 2 — Embedder layer (platform-native, thin).**
Different for each platform (Kotlin/Java on Android, Swift/Obj-C on iOS, C++ on Windows, JS on web). It hosts the engine inside the native app: creates the window/surface, forwards touch/keyboard/lifecycle events, delivers the display's vsync, provides the render surface, routes platform channels, and bridges accessibility (TalkBack/VoiceOver).

**Step 3 — Engine layer (C/C++, ships precompiled).**
The core runtime, shipped as a precompiled binary with every app. It contains:
- The **Dart runtime** (the VM in debug/profile; AOT runtime support in release) — memory, GC, isolates.
- The **rendering engine** — Impeller (or Skia) turns the layer tree into pixels.
- **Text layout** — HarfBuzz, ICU, libtxt; this is why text looks identical across platforms.
- **Platform-channel codec** and low-level I/O.

**Step 4 — Framework layer (Dart, what you write).**
From bottom to top:
- **`dart:ui`** — the thin binding exposing engine features (Canvas, SceneBuilder).
- **Rendering** — the RenderObject tree, layout, paint, hit-testing.
- **Widgets** — Element tree, reconciliation, Stateless/Stateful/Inherited widgets.
- **Material / Cupertino** — the high-level design widgets.

**Step 5 — How they talk.**
- Framework → Engine: builds a `LayerTree` and submits it via `dart:ui` (`SceneBuilder`, `window.render(scene)`).
- Engine → Framework: delivers vsync, input, and lifecycle up via `dart:ui` hooks (`onBeginFrame`, `onPointerDataPacket`).
- Engine ↔ Embedder: the embedder calls the engine's C API (surface, input, vsync); the engine calls back for platform tasks (clipboard, haptics).
- Framework ↔ Native code: platform channels carry binary messages through the engine to the embedder, which routes to plugin code.

```dart
// Trace a tap, hardware → your Dart:
// 1. EMBEDDER: Android gets a MotionEvent → sends pointer data to engine
// 2. ENGINE: builds a PointerDataPacket → calls window.onPointerDataPacket
// 3. FRAMEWORK: GestureBinding hit-tests → your onTap runs:
GestureDetector(
  onTap: () => setState(() => _tapped = true),
  // setState → build → new LayerTree → DOWN to engine → rasterized → shown
  child: const Text('Tap me'),
)

// Platform channel: Dart → Engine → Embedder → native code
const platform = MethodChannel('com.example/battery');
final level = await platform.invokeMethod('getBatteryLevel');
```

**Why interviewers ask:** It shows whether you see Flutter as a whole system or just a widget toolkit. It matters for writing plugins, debugging platform-specific issues, and optimizing rendering — exactly what senior roles expect.

**Common mistake:** Saying Flutter uses the platform's native widgets like React Native. It does **not** — Flutter owns every pixel via its own engine; the embedder only gives a canvas and events. Also thinking `dart:ui` *is* the engine — it's just a thin Dart binding to it.

**Follow-ups they may ask:**
- *"Why does Flutter text look the same on iOS and Android?"* → Text layout lives in the engine (HarfBuzz/ICU), not in the OS.
- *"What does the embedder NOT do?"* → It doesn't render widgets; it only hosts the engine and forwards events/surface/vsync.

**Related:** [Q23 — Dart runtime in the engine](#q23) · [Q12 — threads](#q12) · [Q17 — pipeline](#q17)

[↑ Back to top](#toc)

---

<a id="q23"></a>
## 23. How do Flutter and Dart work together? How is the Dart VM embedded, and how does Dart reach native code (JIT vs AOT)?

> Deeper question · Hard

**Short answer (say this):**
"The Dart runtime is compiled right into the Flutter engine — Dart doesn't run as a separate process. In debug it's JIT-compiled, which is what makes hot reload possible. In release it's AOT-compiled to native machine code, so there's no interpreter and startup is fast. Dart talks to the engine through `dart:ui` bindings that map to C++ engine calls."

**Let's understand it fully:**

**Step 1 — The Dart runtime lives inside the engine.**
When a Flutter app launches, the embedder boots the engine, which boots the Dart runtime. Dart is a *component inside the engine process* — not a separate program like Node running V8.

**Step 2 — Debug mode (JIT — Just-In-Time).**
The full Dart VM is included with its JIT compiler. Source is compiled to **Kernel bytecode** (`.dill`); at runtime the VM runs it and JIT-compiles hot paths. This is what enables **hot reload**: the VM can inject updated Kernel into the running isolate and re-run `build()`. It's slower than release because of JIT overhead and enabled assertions.

```text
debug:   .dart → Kernel .dill → VM interprets + JIT-compiles at runtime
         → hot reload works, assertions on, slower
```

**Step 3 — Release mode (AOT — Ahead-Of-Time).**
`gen_snapshot` compiles the Kernel to native ARM/x86 at **build time**. The output is a shared library (`.so` on Android, inside `App.framework` on iOS). At runtime a slimmed-down Dart runtime (no JIT, no interpreter) only manages memory, GC, and isolates — all code is already native.

```text
release: .dart → Kernel .dill → gen_snapshot (AOT) → native .so / .framework
         → no VM compile, fast startup, no hot reload, no reflection
profile: AOT like release, but with DevTools/profiling support
```

**Step 4 — How Dart calls the engine (going down).**
Dart calls `dart:ui` classes (`Canvas.drawRect`, `SceneBuilder.pushTransform`). These are bindings that map to C++ engine methods. When a frame is ready, the framework calls `window.render(scene)` to hand the composited scene to the engine for rasterization.

```dart
import 'dart:ui' as ui;
// Framework → Engine (down):
final recorder = ui.PictureRecorder();
final canvas = ui.Canvas(recorder);
canvas.drawRect(const Rect.fromLTWH(0, 0, 100, 100),
    ui.Paint()..color = const ui.Color(0xFF0000FF)); // native call into C++
final scene = (ui.SceneBuilder()..addPicture(ui.Offset.zero, recorder.endRecording())).build();
ui.PlatformDispatcher.instance.views.first.render(scene); // hand to engine
```

**Step 5 — How the engine calls Dart (going up).**
The engine holds references to Dart callbacks registered via `dart:ui`. At each vsync it calls `onBeginFrame` then `onDrawFrame`; on touch it calls `onPointerDataPacket`. These callbacks drive the framework's frame loop (you never write them — `WidgetsBinding` sets them up).

**Why interviewers ask:** It separates devs who understand the full compile/runtime model from those who only write widgets. It explains why hot reload is debug-only, why release is faster, and why reflection (`dart:mirrors`) is unavailable.

**Common mistake:** Saying "Dart is interpreted." In release it's fully AOT-compiled native code. Also thinking the Dart VM runs separately like Node — it's statically linked into the engine, one process. And blaming JIT alone for debug slowness — assertions and instrumentation also matter.

**Follow-ups they may ask:**
- *"Why no hot reload in release?"* → AOT code is fixed native machine code; there's no VM to inject new Kernel into.
- *"Why is reflection unavailable in release?"* → AOT tree-shakes unused code, so `dart:mirrors` can't inspect types at runtime.

**Related:** [Q22 — engine layer](#q22) · [Q19 — JIT enables hot reload](#q19)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**The three trees**

| Tree | What it is | Lifespan | Cost |
|---|---|---|---|
| Widget | the blueprint you write | thrown away each rebuild | cheap |
| Element | the living bridge + holds `State` | long-lived | medium |
| RenderObject | does layout & paint | reused, rarely recreated | expensive |

**Stateless vs Stateful**

| | StatelessWidget | StatefulWidget |
|---|---|---|
| Changing data | none | yes, in a `State` object |
| Rebuilds itself | no (only parent rebuilds it) | yes, via `setState` |
| State lives on | — | the Element |

**Keys**

| Key | Identity by | Use for |
|---|---|---|
| `ValueKey` | a value (`==`) | list items with a stable id |
| `ObjectKey` | reference (`identical`) | objects equal by value, differ by reference |
| `UniqueKey` | always unique | force a fresh element/state |
| `GlobalKey` | app-wide | reach state from outside (e.g. Form) |

**MediaQuery vs LayoutBuilder**

| MediaQuery | LayoutBuilder |
|---|---|
| whole-screen info | your actual constraints |
| same everywhere | depends on your spot |
| phone vs tablet breakpoints | adapt to local space |

**Constraints**

| Term | Meaning |
|---|---|
| tight | min == max (no choice) |
| loose | min = 0 (free up to max) |
| unbounded | max = infinity (inside scrollables) |

**Hot Reload vs Hot Restart vs Full Restart**

| | Hot Reload | Hot Restart | Full Restart |
|---|---|---|---|
| State | kept | wiped | wiped |
| Runs `main`/`initState` | no | yes | yes |
| Native code | no | no | rebuilt |
| Speed | ~1s | a few s | 30s+ |

**JIT vs AOT**

| JIT (debug) | AOT (release) |
|---|---|
| compile while running | compile before running |
| enables hot reload | fast startup, native |
| slower (assertions on) | no reflection, no hot reload |

## One-line reminders

- **Three trees**: Widget = cheap blueprint, Element = living bridge + state, RenderObject = expensive layout/paint. ([Q1](#q1))
- **Widgets are immutable** and cheap; the expensive render objects are reused via the element. ([Q2](#q2))
- **Keys** match widgets by identity, not position — use `ValueKey(id)` for lists, `GlobalKey` sparingly. ([Q3](#q3))
- **Reconciliation**: same type + same key → reuse; else discard and rebuild. ([Q4](#q4))
- **State lives on the Element**, which is why it survives rebuilds. ([Q5](#q5))
- **Lifecycle**: initState (setup) → didChangeDependencies (safe context) → build; dispose to clean up. ([Q6](#q6))
- **`setState`** changes data + marks dirty → one rebuild next frame of this subtree only. Check `mounted` after `await`. ([Q7](#q7))
- **BuildContext IS the Element** — no inherited lookups in `initState`; use `didChangeDependencies`. ([Q8](#q8))
- **InheritedWidget** rebuilds only registered dependents; Provider wraps it with a nicer API. ([Q9](#q9))
- **`const`** widgets are identical objects → reconciliation skips them instantly. ([Q10](#q10))
- **RepaintBoundary** isolates frequent repaints onto their own layer — don't overuse it. ([Q11](#q11))
- **UI thread = your Dart**, **raster thread = GPU**. Red UI bar → fix your code; red raster bar → fix GPU work. ([Q12](#q12))
- **Layout**: constraints down, sizes up, parent sets position — single pass, O(n). ([Q13](#q13))
- **Unbounded** (infinity) constraints inside scrollables break fill/flex widgets — give a bounded size. ([Q14](#q14))
- **RenderFlex overflow** → `Expanded`/`Flexible`, ellipsis text, or a scroll view. ([Q15](#q15))
- **MediaQuery** = whole screen; **LayoutBuilder** = your actual space. Prefer LayoutBuilder for reusable widgets. ([Q16](#q16))
- **Pipeline**: build → layout → paint (layers) → composite → rasterize (raster thread) → display. ([Q17](#q17))
- **Impeller** precompiles shaders (no jank); **Skia** compiled them at runtime (first-frame jank). ([Q18](#q18))
- **Hot Reload** keeps state; **Hot Restart** wipes Dart state; **Full Restart** rebuilds native. ([Q19](#q19))
- **`^1.5.0`** = `>=1.5.0 <2.0.0`; keep test tools in `dev_dependencies`; commit `pubspec.lock` for apps. ([Q20](#q20))
- **Stable** for production; **beta** to pre-test; **master** only for contributors. Pin versions in CI. ([Q21](#q21))
- **Three layers**: Embedder (host) → Engine (C++ core, Dart runtime, rendering) → Framework (your Dart). ([Q22](#q22))
- **Dart is JIT in debug** (hot reload), **AOT native in release** (fast, no reflection); the runtime is inside the engine. ([Q23](#q23))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers rarely stop at one question. They keep digging to test your depth. Practice answering this chain out loud — calmly, step by step:

1. *"What are the three trees?"* → Widget (blueprint), Element (living bridge + state), RenderObject (layout/paint).
2. *"Then why can Flutter rebuild widgets 60 times a second?"* → Widgets are cheap; the element reuses the expensive render objects.
3. *"How does the element decide to reuse?"* → Same type and key → reuse and update properties; else discard and rebuild.
4. *"So why do keys matter in a list?"* → Without keys, matching is by position, so reordering attaches state to the wrong item.
5. *"How would you make a frequently-changing item cheaper?"* → `const` for the static parts, `RepaintBoundary` to isolate its repaints, and keep `build()` light.

Being able to calmly go step by step like this — without guessing — is exactly what makes you sound **senior**, in both remote and BD interviews.

[↑ Back to top](#toc)

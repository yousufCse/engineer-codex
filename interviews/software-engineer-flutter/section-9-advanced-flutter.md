# Section 9 — Advanced Flutter

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

**A. Animations — the engine and the pieces**
1. [`AnimationController` — vsync & dispose](#q1) · *Very common*
2. [`Tween` — remap the 0→1 range](#q2) · *Very common*
3. [`CurvedAnimation` & `Curves` (easing)](#q3) · *Common*
4. [`AnimatedWidget` vs `AnimatedBuilder`](#q4) · *Very common*
5. [Implicit vs explicit animations](#q5) · *Very common*
6. [Staggered animations with `Interval`](#q6) · *Common*

**B. Animations — between screens and with tools**
7. [`Hero` animation & the `tag` rule](#q7) · *Very common*
8. [Rive vs Lottie](#q8) · *Common*

**C. Gestures & pointer events**
9. [`GestureDetector` vs `Listener` & the gesture arena](#q9) · *Very common*

**D. Slivers & scrolling**
10. [What are Slivers and why they exist](#q10) · *Common*
11. [`SliverList` vs `SliverGrid` vs `SliverFixedExtentList`](#q11) · *Common*
12. [`SliverAppBar` — pinned / floating / snap](#q12) · *Very common*
13. [`CustomScrollView` — combining slivers](#q13) · *Common*

**E. Custom painting**
14. [`CustomPainter`, `Canvas`, `Paint`, `Path`](#q14) · *Very common*
15. [`CustomPainter` vs widget composition](#q15) · *Common*
16. [`shouldRepaint` & `RepaintBoundary`](#q16) · *Common*

**F. Accessibility**
17. [`Semantics` & screen readers](#q17) · *Common*
18. [`ExcludeSemantics` vs `MergeSemantics`](#q18) · *Common*
19. [Testing accessibility](#q19) · *Common*

**G. Localization**
20. [Multi-language (l10n) with ARB, `flutter_localizations`, `intl`](#q20) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 20 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — Core animation pieces (start here).** Almost every Flutter interview touches these.
→ [Q1 AnimationController](#q1) · [Q2 Tween](#q2) · [Q5 Implicit vs explicit](#q5) · [Q4 AnimatedBuilder vs AnimatedWidget](#q4)

**Stage 2 — Polished, real-app animation.** What makes motion feel good and reusable.
→ [Q3 Curves](#q3) · [Q7 Hero](#q7) · [Q6 Staggered](#q6) · [Q8 Rive vs Lottie](#q8)

**Stage 3 — Touch and scrolling.** How the app reacts to fingers and big lists.
→ [Q9 Gestures](#q9) · [Q10 Slivers](#q10) · [Q12 SliverAppBar](#q12) · [Q13 CustomScrollView](#q13)

**Stage 4 — Drawing your own pixels.** When no widget can do it.
→ [Q14 CustomPainter](#q14) · [Q15 Painter vs widgets](#q15) · [Q16 shouldRepaint & RepaintBoundary](#q16) · [Q11 Sliver types](#q11)

**Stage 5 — Senior signal: reach everyone, everywhere.** These separate strong seniors from the rest.
→ [Q17 Semantics](#q17) · [Q18 Exclude/Merge](#q18) · [Q19 Accessibility testing](#q19) · [Q20 Localization](#q20)

**Short on time (1 hour before the interview)?** Just review these seven:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q5](#q5) · [Q7](#q7) · [Q9](#q9) · [Q14](#q14), then read the [Cheat Sheet](#cheatsheet).

---

# A. Animations — the engine and the pieces

> Flutter animation is a small pipeline: a **controller** drives progress, a **Tween** maps that progress to real values, a **curve** shapes the speed, and a **widget** shows the result. Get these four in your head and the rest is easy.

---

<a id="q1"></a>
## 1. What is `AnimationController`? Explain `vsync` and why you must dispose it.

> Very common · Medium

**Short answer (say this):**
"`AnimationController` is the engine behind explicit animations. It produces a number — by default from 0.0 to 1.0 — once per frame over a duration. `vsync` ties it to the screen's frame clock so it only ticks while the widget is visible, saving battery. I must call `dispose()` on it, or its ticker keeps firing after the widget is gone and leaks memory."

**Let's understand it fully:**

**Step 1 — Think of the controller as a clock that drives the motion.**
The controller does not draw anything by itself. It just produces a steady stream of numbers over time — like a clock hand sweeping from 0.0 to 1.0. You then wire those numbers to a widget (size, opacity, rotation) to create motion.

```dart
_controller = AnimationController(
  duration: const Duration(milliseconds: 800),
  vsync: this,           // explained in Step 3
);
_controller.forward();   // start: value goes 0.0 -> 1.0 over 800ms
```

**Step 2 — The values it can produce.**
By default the value runs `0.0 → 1.0`, but you control the direction and looping:

```dart
_controller.forward();   // 0.0 -> 1.0
_controller.reverse();   // 1.0 -> 0.0
_controller.repeat();    // loop forever
_controller.value;       // read the current number any time
```

**Step 3 — `vsync` = "only tick when on screen."**
`vsync` means "vertical sync." You pass `vsync: this`, which gives the controller a `TickerProvider`. A ticker is the thing that fires a callback on every frame (about 60 or 120 times a second). The point of `vsync` is this: if the widget is off-screen or the app is in the background, the ticker stops, so you don't waste CPU, GPU, and battery animating something nobody can see.

To provide `vsync`, add a mixin to your `State`:

```dart
class _MyWidgetState extends State<MyWidget>
    with SingleTickerProviderStateMixin {   // gives 'this' a ticker
  late final AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    )..forward();
  }

  @override
  void dispose() {
    _controller.dispose();   // REQUIRED — see Step 4
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(opacity: _controller, child: const Text('Hello'));
  }
}
```

Use `SingleTickerProviderStateMixin` for one controller, and `TickerProviderStateMixin` only if you truly have several controllers.

**Step 4 — Why `dispose()` is not optional.**
The controller holds a ticker. If you forget to dispose it, the ticker keeps firing forever after the widget is removed. That is a memory leak, and Flutter will throw a clear error: *"A TickerProvider was disposed but a Ticker was not."* So the rule is simple: every controller you create in `initState` you dispose in `dispose`.

**Why interviewers ask:** They want to see you understand the frame-by-frame pipeline, why `vsync` exists (performance, not "smoothness"), and that you know the dispose contract. Forgetting dispose is a real production bug.

**Common mistake:** Saying `vsync` "makes the animation smooth." No — it ties the animation to the frame clock and stops it when the widget is not visible. Another mistake: using `TickerProviderStateMixin` (many tickers) when you only have one controller; use `SingleTickerProviderStateMixin`.

**Follow-ups they may ask:**
- *"What if you have two controllers?"* → Use `TickerProviderStateMixin` instead of the single one, and dispose both.
- *"Does the controller draw anything?"* → No. It only produces numbers; a `Tween` and a widget turn them into visuals.

**Related:** [Q2 — Tween](#q2) · [Q4 — AnimatedBuilder](#q4) · [Q5 — implicit vs explicit](#q5)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What is a `Tween`, and how does it chain with `AnimationController`?

> Very common · Medium

**Short answer (say this):**
"A `Tween` defines a start and an end. The controller only gives 0.0→1.0, but I rarely want exactly that. The Tween remaps that 0→1 progress to a useful range — a size, a color, an offset. I connect them with `tween.animate(controller)`, which gives me an `Animation<T>` to use."

**Let's understand it fully:**

**Step 1 — Think of a Tween as the start/end range, and the controller as the dial.**
The controller is a dial that moves from 0 to 1. The Tween says "0 means *this* value, 1 means *that* value." The Tween does the in-between math for you (the word "tween" comes from "be**tween**").

```dart
// Controller: 0.0 -> 1.0
// Tween: 0.0 means 50, 1.0 means 200
final size = Tween<double>(begin: 50, end: 200);
```

**Step 2 — Chain it to the controller with `.animate(...)`.**
`.animate(controller)` returns an `Animation<T>` — an object whose `.value` follows the controller, but in the Tween's range:

```dart
late final AnimationController _controller;
late final Animation<double> _sizeAnimation;
late final Animation<Color?> _colorAnimation;

@override
void initState() {
  super.initState();
  _controller = AnimationController(
    duration: const Duration(seconds: 1),
    vsync: this,
  );

  // Same controller can drive several tweens at once:
  _sizeAnimation = Tween<double>(begin: 50, end: 200).animate(_controller);
  _colorAnimation =
      ColorTween(begin: Colors.red, end: Colors.blue).animate(_controller);

  _controller.forward();
}
```

**Step 3 — Read the values in the UI.**
You read `.value` from the animation, usually inside an `AnimatedBuilder` (see [Q4](#q4)):

```dart
@override
Widget build(BuildContext context) {
  return AnimatedBuilder(
    animation: _controller,
    builder: (context, child) => Container(
      width: _sizeAnimation.value,
      height: _sizeAnimation.value,
      color: _colorAnimation.value,
    ),
  );
}
```

**Step 4 — A Tween alone does nothing.**
This is the key point. A Tween is just a description of a range. It has no concept of time. It only animates once a controller drives it. There are also ready-made tweens: `ColorTween`, `SizeTween`, `RectTween`, and `IntTween`.

**Why interviewers ask:** They want to see you understand the composition: the controller makes raw 0→1 progress, the Tween maps that progress to a meaningful value, and the widget shows it. This separation is the whole mental model of explicit animation.

**Common mistake:** Trying to use a Tween without a controller (nothing happens — it has no clock). Another mistake: building a new Tween inside `build()` on every frame; create it once in `initState`.

**Follow-ups they may ask:**
- *"How do you map to a non-number, like a color?"* → Use a typed tween such as `ColorTween` or `Tween<Offset>`.
- *"Can one controller drive several tweens?"* → Yes — call `.animate(controller)` on each. They all share the same 0→1 progress.

**Related:** [Q1 — AnimationController](#q1) · [Q3 — CurvedAnimation](#q3) · [Q4 — AnimatedBuilder](#q4)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. What is `CurvedAnimation`? What are `Curves`, and how do you apply easing?

> Common · Medium

**Short answer (say this):**
"By default the controller moves at a constant speed, which looks robotic. A `CurvedAnimation` wraps the controller and bends that linear 0→1 into a natural speed — slow start, fast middle, gentle stop. A `Curve` is just a function that reshapes the progress, and Flutter ships many ready-made ones in the `Curves` class."

**Let's understand it fully:**

**Step 1 — The car example.**
A real car does not jump instantly to full speed and stop dead. It speeds up, cruises, then slows down. A curve adds that real-world feel to motion. Without a curve, animation moves at one flat speed, which the eye reads as "cheap."

**Step 2 — A `Curve` reshapes the timeline.**
A curve takes the linear input `t` (0.0 → 1.0) and returns a reshaped value. `Curves.easeOut`, for example, moves fast at first and eases to a soft stop:

```dart
final t = 0.5;                    // halfway in time
Curves.linear.transform(t);       // 0.5  (no change)
Curves.easeOut.transform(t);      // ~0.7 (already most of the way there)
```

**Step 3 — Wrap the controller with `CurvedAnimation`, then chain a Tween.**
The order is: controller → curve → Tween.

```dart
late final AnimationController _controller;
late final Animation<double> _animation;

@override
void initState() {
  super.initState();
  _controller = AnimationController(
    duration: const Duration(milliseconds: 600),
    vsync: this,
  );

  // 1. Bend the controller's progress with a curve:
  final curved = CurvedAnimation(
    parent: _controller,
    curve: Curves.easeOutBack,      // overshoots slightly, then settles
    reverseCurve: Curves.easeIn,    // a different shape when reversing
  );

  // 2. Map the curved progress to a real range:
  _animation = Tween<double>(begin: 0, end: 300).animate(curved);

  _controller.forward();
}
```

**Step 4 — Common curves and when to use them.**

| Curve | Feel | Use for |
|---|---|---|
| `Curves.easeInOut` | smooth both ends | general UI transitions |
| `Curves.easeOut` | fast start, soft stop | something appearing |
| `Curves.easeIn` | soft start, fast end | something disappearing |
| `Curves.bounceOut` | bounces at the end | playful, game-like UI |
| `Curves.elasticOut` | springs past, settles | attention-grabbing |
| `Curves.decelerate` | natural slow-down | a flick coming to rest |

The `In`/`Out` naming tells you which end gets the effect: `bounceIn` bounces at the start, `bounceOut` bounces at the end.

**Why interviewers ask:** Knowing curves is the difference between an animation that "works" and one that "feels good." It shows polish, which seniors are expected to bring.

**Common mistake:** Using `bounceIn` when you meant `bounceOut` (wrong end gets the effect). Another mistake: worrying about disposing the `CurvedAnimation` — it is cleaned up automatically when its parent controller is disposed.

**Follow-ups they may ask:**
- *"Can you write a custom curve?"* → Yes — extend `Curve` and override `transformInternal(double t)`.
- *"Where does the curve go in the chain?"* → Between the controller and the Tween: `Tween.animate(CurvedAnimation(parent: controller, curve: ...))`.

**Related:** [Q1 — AnimationController](#q1) · [Q2 — Tween](#q2) · [Q6 — staggered animations](#q6)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. What is the difference between `AnimatedWidget` and `AnimatedBuilder`, and when do you use each?

> Very common · Medium

**Short answer (say this):**
"Both let an animation rebuild the UI without me calling `setState` by hand. `AnimatedWidget` is a subclass you create — good for a reusable, self-contained animated widget. `AnimatedBuilder` is an inline builder — good for adding motion to an existing widget. The big trick with `AnimatedBuilder` is the `child` argument, which is built once and not rebuilt each frame."

**Let's understand it fully:**

**Step 1 — The problem both solve.**
An animation changes its value about 60 times a second. You do not want to call `setState` 60 times a second by hand. Both `AnimatedWidget` and `AnimatedBuilder` listen to the animation and rebuild only the small part that moves.

**Step 2 — `AnimatedWidget`: make a reusable animated widget (subclass).**
You extend `AnimatedWidget` and pass the animation as the `listenable`. The widget rebuilds itself whenever the animation ticks. This is best when you want a clean, reusable component.

```dart
class PulsatingCircle extends AnimatedWidget {
  const PulsatingCircle({super.key, required Animation<double> animation})
      : super(listenable: animation);

  @override
  Widget build(BuildContext context) {
    final animation = listenable as Animation<double>;
    return Container(
      width: animation.value,
      height: animation.value,
      decoration: const BoxDecoration(
        shape: BoxShape.circle,
        color: Colors.blue,
      ),
    );
  }
}

// Usage:
PulsatingCircle(animation: _sizeAnimation);
```

**Step 3 — `AnimatedBuilder`: animate an existing widget inline.**
You pass a `builder` callback. No new class needed. Best for one-off animations.

```dart
AnimatedBuilder(
  animation: _controller,
  child: const FlutterLogo(size: 100),   // built ONCE — see Step 4
  builder: (context, child) {
    return Transform.rotate(
      angle: _controller.value * 2 * pi,
      child: child,                       // reused, not rebuilt
    );
  },
);
```

**Step 4 — The `child` trick (the performance point they want).**
The `child` you pass to `AnimatedBuilder` is built one time and handed back to your `builder` on every frame. So only the wrapper (here `Transform.rotate`) is recreated each frame — the expensive child is not. This is the optimization interviewers are listening for.

**Step 5 — Which one to pick.**

| | `AnimatedWidget` | `AnimatedBuilder` |
|---|---|---|
| Form | a subclass you write | an inline builder |
| Best for | reusable animated component | one-off, adding motion to an existing tree |
| Skip rebuilding a child? | wrap a static child inside | pass it as `child` |

**Why interviewers ask:** They are checking whether you know how to avoid rebuilding expensive widgets during animation, and whether you understand composition (`AnimatedBuilder`) versus inheritance (`AnimatedWidget`).

**Common mistake:** Building an expensive widget tree inside `AnimatedBuilder`'s `builder` instead of passing it as `child`. Then it rebuilds 60 times a second. Pass the static part as `child` and reference it.

**Follow-ups they may ask:**
- *"Why is `child` faster?"* → It is created once and reused; only the wrapping widget rebuilds each frame.
- *"Are the transition widgets related?"* → Yes — `FadeTransition`, `ScaleTransition`, etc. are built on the same listenable idea and are even simpler when they fit.

**Related:** [Q2 — Tween](#q2) · [Q5 — implicit vs explicit](#q5) · [Q16 — RepaintBoundary](#q16)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What is the difference between implicit and explicit animations, and when do you use each?

> Very common · Medium

**Short answer (say this):**
"Implicit animations are the easy mode: I just change a value and a widget like `AnimatedContainer` animates the change for me — no controller. Explicit animations give full control — start, stop, loop, reverse, sequence — but I manage the `AnimationController` myself. I reach for implicit by default and only go explicit when I need looping, sequencing, or programmatic control."

**Let's understand it fully:**

**Step 1 — Implicit = "set the new value, Flutter does the rest."**
You give a duration and a curve, then just change the target. Flutter animates from the old value to the new one automatically. No controller, no tween, no dispose.

```dart
// Tapping toggles _isExpanded; the box animates by itself:
AnimatedContainer(
  duration: const Duration(milliseconds: 300),
  curve: Curves.easeInOut,
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  color: _isExpanded ? Colors.blue : Colors.red,
  child: const Text('Tap me'),
);
```

Common implicit widgets: `AnimatedContainer`, `AnimatedOpacity`, `AnimatedPadding`, `AnimatedPositioned`, `AnimatedAlign`, `AnimatedDefaultTextStyle`, `AnimatedCrossFade`, and `TweenAnimationBuilder` (for custom one-off values).

**Step 2 — Explicit = "I hold the controller and decide everything."**
You create an `AnimationController` and drive it. This is the only way to loop, play in reverse on demand, coordinate several animations, or stop at an exact moment.

```dart
class _SpinnerState extends State<Spinner>
    with SingleTickerProviderStateMixin {
  late final AnimationController _ctrl;

  @override
  void initState() {
    super.initState();
    _ctrl = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    )..repeat();   // loops forever — impossible with implicit
  }

  @override
  Widget build(BuildContext context) {
    return RotationTransition(
      turns: _ctrl,
      child: const Icon(Icons.refresh, size: 48),
    );
  }

  @override
  void dispose() {
    _ctrl.dispose();
    super.dispose();
  }
}
```

**Step 3 — A simple decision rule.**
Ask one question: *does the motion need to loop, sequence, or be controlled by code?*

- **No** → implicit (less code, fewer bugs): toggles, layout changes, hover effects, a one-time fade-in.
- **Yes** → explicit: spinners, repeating pulses, staggered intros, swipe-to-dismiss progress, anything you start and stop from code.

**Step 4 — Why this choice matters.**
Using an explicit controller for a simple color change is over-engineering — more code and a dispose to remember. Using implicit for a complex orchestrated sequence is simply impossible. Picking correctly is a senior signal.

**Why interviewers ask:** They want to see you choose the right tool. The wrong choice in either direction is a red flag.

**Common mistake:** Reaching for `AnimationController` for everything. Most everyday UI motion (state toggles, layout shifts) should be implicit.

**Follow-ups they may ask:**
- *"What about a custom value that has no `AnimatedX` widget?"* → Use `TweenAnimationBuilder` — it is implicit but for any value you define.
- *"Can you mix them?"* → Yes, but keep it clear; usually one screen leans one way.

**Related:** [Q1 — AnimationController](#q1) · [Q4 — AnimatedBuilder](#q4) · [Q6 — staggered animations](#q6)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. How do you build a staggered animation (several parts moving at different times)?

> Common · Medium–Hard

**Short answer (say this):**
"A staggered animation runs several pieces from a single controller, but each piece is active during a different slice of the timeline. I use one `AnimationController` and give each piece a `CurvedAnimation` with an `Interval`, which says 'only animate between, say, 0.0 and 0.5 of the total.' One clock, many parts with different start and end times."

**Let's understand it fully:**

**Step 1 — The relay-race idea.**
Think of one stopwatch timing a relay race. Runner 1 runs in the first part of the time, runner 2 in the middle, runner 3 at the end. There is still only one stopwatch (one controller); each runner just has their own slice of it.

**Step 2 — Use one controller for the whole sequence.**
You do **not** create three controllers. You create one, and its 0→1 covers the full sequence:

```dart
_controller = AnimationController(
  duration: const Duration(milliseconds: 1200), // total length
  vsync: this,
);
```

**Step 3 — Give each part an `Interval`.**
An `Interval` is a curve that stays still outside its window and animates inside it. `Interval(0.0, 0.5)` means "do your motion in the first half of the timeline."

```dart
// Fade in during the first 40% of the timeline:
final fade = CurvedAnimation(
  parent: _controller,
  curve: const Interval(0.0, 0.4, curve: Curves.easeOut),
);

// Slide up during the middle (30% -> 70%):
final slide = Tween<Offset>(
  begin: const Offset(0, 0.3),
  end: Offset.zero,
).animate(CurvedAnimation(
  parent: _controller,
  curve: const Interval(0.3, 0.7, curve: Curves.easeOut),
));

// Scale at the end (60% -> 100%):
final scale = CurvedAnimation(
  parent: _controller,
  curve: const Interval(0.6, 1.0, curve: Curves.easeOutBack),
);
```

**Step 4 — Wire them up and play once.**

```dart
@override
Widget build(BuildContext context) {
  return AnimatedBuilder(
    animation: _controller,
    builder: (context, child) => FadeTransition(
      opacity: fade,
      child: SlideTransition(
        position: slide,
        child: ScaleTransition(scale: scale, child: child),
      ),
    ),
    child: const Card(child: Padding(padding: EdgeInsets.all(24), child: Text('Hi'))),
  );
}

// somewhere: _controller.forward();
```

Now the card fades, then slides, then pops — all from one `forward()` call.

**Why interviewers ask:** Staggered intros are everywhere in polished apps (onboarding, list reveals). They want to see you know the trick is *one controller plus intervals*, not many controllers fighting each other.

**Common mistake:** Creating a separate controller per element and trying to start them with delays. That is hard to keep in sync. One controller with intervals stays perfectly aligned.

**Follow-ups they may ask:**
- *"How would you stagger a whole list?"* → Give item *i* an interval that shifts with its index, or use a package like `flutter_staggered_animations`.
- *"What does `Interval` return outside its window?"* → The clamped end value (0 before it starts, 1 after it ends), so the part simply holds still.

**Related:** [Q3 — Curves](#q3) · [Q1 — AnimationController](#q1) · [Q4 — AnimatedBuilder](#q4)

[↑ Back to top](#toc)

---

# B. Animations — between screens and with tools

---

<a id="q7"></a>
## 7. How does a `Hero` animation work between routes? What is the `tag` requirement?

> Very common · Medium

**Short answer (say this):**
"A `Hero` makes a widget appear to fly from one screen to the next during navigation — like a list thumbnail growing into a full detail image. The same widget on both screens must share the same `tag`. Flutter uses the tag to match the two, then animates the widget's size and position over the route transition."

**Let's understand it fully:**

**Step 1 — Think of the Hero as one shared object flying between screens.**
On screen A there is a small avatar. You tap, go to screen B, and the same avatar grows and moves into its new spot. It feels like one object moved, not two separate images. That continuity is the Hero effect.

**Step 2 — How it works under the hood.**
During the route transition, Flutter:
1. Finds the `Hero` on the source route and measures its size and position.
2. Finds the `Hero` with the **same tag** on the destination route and measures its target size and position.
3. Lifts a copy onto an overlay above both screens and animates it from the source rect to the destination rect.
4. Drops it into place when the transition finishes.

**Step 3 — The `tag` rule.**
Both heroes must use the **same `tag`**, and each tag must be **unique within a single screen**. The tag is how Flutter knows which hero matches which.

```dart
// Screen A — source (in a list)
GestureDetector(
  onTap: () => Navigator.push(
    context,
    MaterialPageRoute(builder: (_) => const DetailScreen()),
  ),
  child: Hero(
    tag: 'avatar-123',        // must match destination
    child: CircleAvatar(radius: 30, backgroundImage: NetworkImage(imageUrl)),
  ),
);

// Screen B — destination
Scaffold(
  body: Center(
    child: Hero(
      tag: 'avatar-123',      // same tag as the source
      child: CircleAvatar(radius: 100, backgroundImage: NetworkImage(imageUrl)),
    ),
  ),
);
```

**Step 4 — Lists need unique tags.**
In a `ListView`, never give every item the same tag like `'image'` — that crashes at runtime because the tags clash. Use the item's id:

```dart
Hero(tag: 'image-${product.id}', child: ...);
```

**Step 5 — Customizing the in-flight look.**
If the widget looks different on the two screens (say, a different corner radius), the flight can look jumpy. Use `flightShuttleBuilder` to control exactly what is drawn while flying.

**Why interviewers ask:** Hero transitions are one of the highest-impact UX patterns (photo galleries, product details, profiles). They want to see you understand tag matching and the overlay flight path, not just that the widget is called `Hero`.

**Common mistake:** Reusing the same tag for many items in one list (runtime error). Another mistake: wrapping the two heroes in very different layouts so the child changes shape mid-flight; fix it with `flightShuttleBuilder`.

**Follow-ups they may ask:**
- *"What if the tags don't match?"* → No flight happens; it's a normal page push with no shared element.
- *"Can the child be a whole card?"* → Yes, but keep the begin/end shapes similar, or the flight looks odd.

**Related:** [Q5 — explicit vs implicit](#q5) · [Q8 — Rive vs Lottie](#q8)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is the difference between Rive and Lottie, and when would you use each?

> Common · Medium

**Short answer (say this):**
"Both play pre-designed animations, but they differ in power. Lottie plays a fixed animation exported from After Effects as JSON — pure playback. Rive uses its own editor and a compact binary file, and it supports state machines, so the animation can react to taps and app state at runtime. For decorative motion, Lottie is fine; for interactive motion, choose Rive."

**Let's understand it fully:**

**Step 1 — Lottie = playback of a designer's animation.**
The pipeline: a designer builds the animation in Adobe After Effects, exports it with the Bodymovin plugin to a `.json` file, and Flutter plays that file. What you see is exactly what the designer made. You can play, pause, loop, and scrub — but you cannot branch its logic at runtime.

```dart
import 'package:lottie/lottie.dart';

Lottie.asset(
  'assets/animations/loading.json',
  width: 200,
  height: 200,
  repeat: true,
);
```

**Step 2 — Rive = interactive animation with state machines.**
Rive has its own web-based editor and exports a compact `.riv` binary. Its key feature is the **state machine**: inputs (a tap, a boolean, a number) drive transitions between animation states at runtime. So a single Rive file can be an animated button that reacts to presses.

```dart
import 'package:rive/rive.dart';

class _AnimatedButtonState extends State<AnimatedButton> {
  SMITrigger? _press;

  void _onInit(Artboard artboard) {
    final controller =
        StateMachineController.fromArtboard(artboard, 'State Machine 1')!;
    artboard.addController(controller);
    _press = controller.findSMI('pressed') as SMITrigger;
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => _press?.fire(),   // tells the state machine to react
      child: RiveAnimation.asset('assets/button.riv', onInit: _onInit),
    );
  }
}
```

**Step 3 — A side-by-side comparison.**

| | Lottie | Rive |
|---|---|---|
| Source tool | After Effects + Bodymovin | Rive editor |
| File | `.json` (text) | `.riv` (binary, smaller) |
| Runtime logic | playback only | state machines, inputs, conditions |
| Reacts to input | no | yes |
| Best for | decorative motion | interactive motion |

**Step 4 — When to pick each.**
- **Lottie:** your team already lives in After Effects; the animation is decorative (loading spinners, success checkmarks, onboarding art); no runtime interaction needed.
- **Rive:** you need interactivity (animated toggles, character reactions), runtime state changes, or smaller files and better performance on complex scenes.

**Why interviewers ask:** They want to see you can advise the team on tooling trade-offs, and that you understand the design-to-code pipeline, not just the Dart side.

**Common mistake:** Saying "they're the same, just different file formats." They differ fundamentally: Rive has interactive state machines; Lottie does not. Another mistake: ignoring file size — complex Lottie JSON can get large, while `.riv` stays compact.

**Follow-ups they may ask:**
- *"Can Lottie react to a tap?"* → Only in coarse ways (play a segment, change speed). It has no real state logic; that's Rive's job.
- *"Why is Rive often more performant?"* → A compact binary format and a runtime built for real-time graphics, versus parsing larger JSON.

**Related:** [Q7 — Hero](#q7) · [Q5 — implicit vs explicit](#q5)

[↑ Back to top](#toc)

---

# C. Gestures & pointer events

> Touch in Flutter has two layers: raw pointer events (`Listener`) and recognized gestures like tap, drag, and scale (`GestureDetector`). Seniors are expected to know the difference and how Flutter decides who "wins" a touch.

---

<a id="q9"></a>
## 9. What is the difference between `GestureDetector` and `Listener`? And what is the gesture arena?

> Very common · Medium–Hard

**Short answer (say this):**
"`Listener` gives me raw pointer events — down, move, up — with no interpretation. `GestureDetector` sits on top and recognizes meaningful gestures like tap, double-tap, long-press, drag, and scale. When several widgets could claim the same touch, Flutter runs a 'gesture arena' to decide which one wins, so two gestures don't both fire."

**Let's understand it fully:**

**Step 1 — `Listener` = raw finger data.**
`Listener` reports the low-level pointer events exactly as they happen. It does not know what a "tap" or a "swipe" is — it just tells you a finger went down, moved, and lifted.

```dart
Listener(
  onPointerDown: (e) => print('finger down at ${e.position}'),
  onPointerMove: (e) => print('moved by ${e.delta}'),
  onPointerUp: (e) => print('finger up'),
  child: const ColoredBox(color: Colors.amber, child: SizedBox(width: 100, height: 100)),
);
```

You rarely need this directly — it is for custom interactions where the built-in gestures don't fit.

**Step 2 — `GestureDetector` = recognized gestures.**
`GestureDetector` interprets those raw events into the gestures you actually care about. This is what you use 95% of the time.

```dart
GestureDetector(
  onTap: () => print('tap'),
  onDoubleTap: () => print('double tap'),
  onLongPress: () => print('long press'),
  onPanUpdate: (d) => print('dragged by ${d.delta}'),  // pan = drag
  onScaleUpdate: (d) => print('pinch scale ${d.scale}'),
  child: const FlutterLogo(size: 100),
);
```

**Step 3 — The problem: who owns the touch?**
Imagine a small tappable card inside a scrollable list. When you press, is it a tap on the card or the start of a scroll? Both want the same finger. If both fired, you'd get a tap *and* a scroll — wrong.

**Step 4 — The gesture arena decides the winner.**
Flutter solves this with the **gesture arena**. Think of it like an auction for the touch:
1. When a finger goes down, every interested recognizer (tap, drag, scroll) enters the arena.
2. As the finger moves, recognizers either **claim victory** (e.g. the finger moved far enough to be a drag) or **give up** (a tap recognizer bows out the moment the finger moves too much).
3. Exactly one recognizer wins; the rest are cancelled. So you get *either* a tap *or* a scroll, never both.

This is why a tap inside a `ListView` still works, but turns into a scroll if you move your finger — the arena hands the touch to the scroll recognizer once it's clearly a drag.

**Step 5 — `behavior`: catching taps on empty space.**
By default a `GestureDetector` only receives touches that land on its child's painted pixels. To catch taps on transparent or empty areas, set the hit-test behavior:

```dart
GestureDetector(
  behavior: HitTestBehavior.opaque,  // whole area is tappable, even empty space
  onTap: _dismissKeyboard,
  child: const SizedBox.expand(),
);
```

**Why interviewers ask:** They want to see you know the two layers (raw vs recognized) and that you can explain how Flutter avoids conflicting gestures. The arena is the senior-level part of the answer.

**Common mistake:** Reaching for `Listener` for simple taps — use `GestureDetector`. Another mistake: expecting two gestures to both fire from one touch; the arena guarantees a single winner. Also forgetting `HitTestBehavior.opaque` when you need to tap empty space (e.g. dismissing a keyboard).

**Follow-ups they may ask:**
- *"Why doesn't my tap fire inside a `Stack`?"* → A sibling on top may be absorbing the hit test; check `behavior` and z-order.
- *"`onPanUpdate` vs `onScaleUpdate`?"* → You can't use both on one detector — scale is the superset (it also reports drag), so use scale callbacks when you need both pan and pinch.
- *"What is `RawGestureDetector`?"* → A lower-level version where you register your own custom recognizers in the arena.

**Related:** [Q7 — Hero (tap to navigate)](#q7) · [Q17 — Semantics for tappable widgets](#q17)

[↑ Back to top](#toc)

---

# D. Slivers & scrolling

> A sliver is a scrollable section that paints content on demand based on scroll position. Even `ListView` is a sliver underneath. Slivers let you mix headers, grids, and lists in one smooth scroll.

---

<a id="q10"></a>
## 10. What are Slivers, and why do they exist?

> Common · Medium–Hard

**Short answer (say this):**
"A sliver is a low-level scrollable section that produces visual content on demand as you scroll. They exist so you can combine different scroll behaviors — a collapsing app bar, then a grid, then a list — in one single scroll view. `ListView` and `GridView` are just friendly wrappers around slivers."

**Let's understand it fully:**

**Step 1 — Why a plain `ListView` is not enough.**
A `ListView` assumes one uniform scrolling behavior. But real screens often need several behaviors in one scroll: a header image that shrinks, then a horizontal carousel, then a grid, then a list. Nesting scrollables to do this is awkward and buggy. Slivers solve it.

**Step 2 — The conveyor-belt idea.**
Think of the scroll view as one conveyor belt. Each sliver is a section on that belt. As the belt moves, Flutter asks each sliver, "given how far we've scrolled and how much room is left, how much do you paint right now?" Each sliver answers with its **geometry**. This back-and-forth is the **sliver layout protocol**.

```text
Plain ListView (problematic):          CustomScrollView with slivers (correct):

  ListView(                              CustomScrollView(
    children: [                            slivers: [
      Header(),         // ok                SliverAppBar(...)   // collapses
      GridView(...)     // nested scroll!    SliverGrid(...)     // grid section
      AnotherList(...)  // nested scroll!    SliverList(...)     // list section
    ],                                       SliverToBoxAdapter(...) // one widget
  )                                        ],
                                         )
```

**Step 3 — A sliver is laid out differently from a normal widget.**
A normal (box) widget thinks in width and height. A sliver thinks in *scroll extent* — how much it occupies along the scroll direction and how much has scrolled away. Because they speak different layout languages, you cannot freely mix them (see Step 4).

**Step 4 — The two-world rule.**
- You **cannot** put a sliver inside a `Column` or `Row`.
- You **cannot** put a normal widget directly into a `slivers:` list — wrap it in `SliverToBoxAdapter` first.

```dart
CustomScrollView(
  slivers: [
    const SliverAppBar(expandedHeight: 200, pinned: true),
    SliverToBoxAdapter(child: Text('A normal widget, wrapped')),  // bridge
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, i) => ListTile(title: Text('Row $i')),
        childCount: 50,
      ),
    ),
  ],
);
```

**Why interviewers ask:** Slivers are the real scrolling architecture of Flutter. Knowing them shows you understand more than the convenience APIs and can build complex screens that stay smooth.

**Common mistake:** Calling a sliver "just another widget." It uses a different layout protocol. Putting a regular widget straight into `slivers:` (without `SliverToBoxAdapter`) is a classic error.

**Follow-ups they may ask:**
- *"Is `ListView` a sliver?"* → Internally it wraps a `SliverList` inside a `Viewport`. The convenience widgets are sliver-powered.
- *"Why on demand?"* → A sliver only builds the children currently visible (plus a small cache), so a 10,000-item list stays cheap.

**Related:** [Q11 — sliver list types](#q11) · [Q12 — SliverAppBar](#q12) · [Q13 — CustomScrollView](#q13)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What are the differences between `SliverList`, `SliverGrid`, and `SliverFixedExtentList`?

> Common · Medium

**Short answer (say this):**
"`SliverList` lays children in a line where each can have a different height. `SliverGrid` lays them in a 2D grid. `SliverFixedExtentList` is like `SliverList` but every child has the same fixed height — and because the height is known in advance, Flutter can jump straight to the visible items with simple math, which is much faster for very long lists."

**Let's understand it fully:**

**Step 1 — `SliverList`: a line of variable-height items.**
Each child can be a different height. Flutter builds only the visible children (plus a small cache), so it's efficient even for long lists — but it must lay children out one after another to know where each sits.

```dart
SliverList(
  delegate: SliverChildBuilderDelegate(
    (context, index) => ListTile(
      title: Text('Item $index'),
      subtitle: index.isEven ? const Text('Has subtitle') : null, // varies height
    ),
    childCount: 100,
  ),
);
```

**Step 2 — `SliverGrid`: a 2D grid.**
You control the layout with a grid delegate — a fixed number of columns, or a maximum tile width.

```dart
SliverGrid(
  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
    crossAxisCount: 3,
    mainAxisSpacing: 8,
    crossAxisSpacing: 8,
  ),
  delegate: SliverChildBuilderDelegate(
    (context, index) => Container(color: Colors.teal[100 * (index % 9)]),
    childCount: 30,
  ),
);
```

**Step 3 — `SliverFixedExtentList`: same height = fast.**
Every child is forced to the same main-axis size (`itemExtent`). Because Flutter knows each item's height up front, it can compute *exactly* which items are on screen with a quick calculation — no need to measure items one by one. For a 10,000-row list, this is a real performance win.

```dart
SliverFixedExtentList(
  itemExtent: 56.0,  // every row is exactly 56px tall
  delegate: SliverChildBuilderDelegate(
    (context, index) => ListTile(title: Text('Row $index')),
    childCount: 10000,
  ),
);
```

**Step 4 — A quick comparison.**

| Sliver | Layout | Item heights | Speed on huge lists |
|---|---|---|---|
| `SliverList` | one line | each can differ | good |
| `SliverGrid` | 2D grid | by grid delegate | good |
| `SliverFixedExtentList` | one line | all the same | fastest (direct jump to visible) |

**Why interviewers ask:** They are checking your sense of scrolling performance. Choosing the fixed-extent list for a uniform 10,000-item contacts screen is a meaningful, senior-level decision.

**Common mistake:** Using `SliverList` for items that are all the same height. If they're uniform, prefer `SliverFixedExtentList`. Also worth knowing: `SliverPrototypeExtentList` measures the extent from a sample widget instead of a hard-coded number — handy when row height depends on the text scale or theme.

**Follow-ups they may ask:**
- *"Why is fixed-extent faster?"* → Flutter computes the visible range by division instead of laying out each child to find its position.
- *"What if height depends on font size?"* → Use `SliverPrototypeExtentList` and give it a prototype item.

**Related:** [Q10 — what are slivers](#q10) · [Q13 — CustomScrollView](#q13)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. What does `SliverAppBar` do? What is the difference between `pinned`, `floating`, and `snap`?

> Very common · Medium

**Short answer (say this):**
"`SliverAppBar` is an app bar that lives inside a `CustomScrollView` and reacts to scroll. `pinned` keeps the collapsed toolbar stuck at the top. `floating` makes the bar reappear the moment you scroll up, even mid-list. `snap` (which needs `floating`) makes it animate fully in or out — no half-open state."

**Let's understand it fully:**

**Step 1 — What it is.**
A `SliverAppBar` can expand to show a big image or title, then collapse to a normal toolbar as you scroll. Three booleans control how it behaves.

**Step 2 — `pinned: true` — the toolbar stays.**
When you scroll down, the bar collapses to toolbar height and **stays** at the top. It never fully disappears. This is the classic collapsing header (think Gmail).

**Step 3 — `floating: true` — it comes back early.**
With floating, the moment you scroll **up** even a little, the bar reappears — you don't have to scroll all the way back to the top. Common in feeds and news apps.

**Step 4 — `snap: true` — all or nothing (needs floating).**
Snap removes the half-visible state. Scroll up a tiny bit and the bar snaps fully open with an animation; scroll down and it snaps fully away. It must be combined with `floating: true`.

```text
PINNED                 FLOATING                SNAP (+ floating)
Scroll down:           Scroll down:            Scroll down:
  [Toolbar stays]        [Fully gone]            [Fully gone]
Scroll up:             Scroll up a little:     Scroll up a little:
  [Toolbar stays]        [Immediately shows]     [Snaps fully open]
```

**Step 5 — Example and common combinations.**

```dart
CustomScrollView(
  slivers: [
    SliverAppBar(
      expandedHeight: 250,    // height when fully open
      pinned: true,           // collapsed toolbar sticks at top
      floating: false,
      snap: false,
      flexibleSpace: FlexibleSpaceBar(
        title: const Text('My App'),
        background: Image.network('https://example.com/header.jpg', fit: BoxFit.cover),
      ),
    ),
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, i) => ListTile(title: Text('Item $i')),
        childCount: 50,
      ),
    ),
  ],
);

// pinned: true,  floating: false → collapsing toolbar (Gmail)
// pinned: false, floating: true  → reappears on scroll up (news feed)
// floating: true, snap: true     → snappy, no half-open state
```

**Why interviewers ask:** This exact behavior is requested constantly by designers. They want to know you can configure the precise UX without trial and error.

**Common mistake:** Setting `snap: true` without `floating: true` — that throws an assertion error. Another mistake: confusing `expandedHeight` (open height) with `toolbarHeight` (collapsed height). Also: the flexible-space background only shows while expanded; once collapsed (with `pinned`), only the toolbar and title remain.

**Follow-ups they may ask:**
- *"How do you fade the title in as it collapses?"* → Use `FlexibleSpaceBar` with `collapseMode`, or listen to scroll and adjust opacity.
- *"Can you stack two SliverAppBars?"* → Yes — for example a pinned search bar below a collapsing header.

**Related:** [Q10 — what are slivers](#q10) · [Q13 — CustomScrollView](#q13)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. How do you use `CustomScrollView` to combine multiple sliver widgets?

> Common · Medium

**Short answer (say this):**
"`CustomScrollView` is the container that hosts slivers. Its `slivers:` list is laid out one after another along the scroll axis, and they all share one scroll position. Everything in that list must be a sliver — wrap any normal widget in `SliverToBoxAdapter`, and use `SliverFillRemaining` to fill leftover space."

**Let's understand it fully:**

**Step 1 — One scroll view, many sections.**
`CustomScrollView` takes a `slivers:` list. Each entry is a scrollable section. Because they share a single scroll position, the whole thing scrolls as one smooth surface.

**Step 2 — The golden rule: everything must be a sliver.**
- A normal widget? Wrap it in `SliverToBoxAdapter`.
- Need to fill the remaining space (a footer, an empty state)? Use `SliverFillRemaining`.

**Step 3 — A realistic shop screen.**

```dart
CustomScrollView(
  physics: const BouncingScrollPhysics(),
  slivers: [
    // 1. Collapsing header
    const SliverAppBar(
      expandedHeight: 200,
      pinned: true,
      flexibleSpace: FlexibleSpaceBar(title: Text('Shop')),
    ),

    // 2. Search bar — a normal widget, so wrap it
    SliverToBoxAdapter(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: TextField(decoration: const InputDecoration(hintText: 'Search...')),
      ),
    ),

    // 3. Horizontal category chips — also a normal widget
    SliverToBoxAdapter(
      child: SizedBox(
        height: 50,
        child: ListView.builder(
          scrollDirection: Axis.horizontal,
          itemCount: 10,
          itemBuilder: (ctx, i) => Chip(label: Text('Cat $i')),
        ),
      ),
    ),

    // 4. Product grid
    SliverGrid(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        childAspectRatio: 0.8,
      ),
      delegate: SliverChildBuilderDelegate(
        (context, index) => ProductCard(index: index),
        childCount: 20,
      ),
    ),

    // 5. Footer that fills whatever space is left
    const SliverFillRemaining(
      hasScrollBody: false,
      child: Center(child: Text('End of products')),
    ),
  ],
);
```

**Step 4 — Why this is the most practical sliver question.**
Real screens almost always mix sections — a header, a search field, a grid, a list. `CustomScrollView` is how you assemble them into one production-quality scroll.

**Why interviewers ask:** It is the proof that you can actually build a complex scrollable screen, not just recite that slivers exist.

**Common mistake:** Dropping a normal widget straight into `slivers:` without `SliverToBoxAdapter` — a compile-time type error or a render crash. Another mistake: nesting a `CustomScrollView` inside another without `shrinkWrap` and `NeverScrollableScrollPhysics` on the inner one — usually a sign you should flatten it into a single `CustomScrollView` with more slivers.

**Follow-ups they may ask:**
- *"What about pull-to-refresh?"* → Wrap the `CustomScrollView` in a `RefreshIndicator`, or add a `CupertinoSliverRefreshControl` as the first sliver.
- *"`SliverToBoxAdapter` vs `SliverFillRemaining`?"* → Adapter wraps one normal widget at its natural size; fill-remaining stretches to use the leftover viewport space.

**Related:** [Q10 — what are slivers](#q10) · [Q11 — sliver list types](#q11) · [Q12 — SliverAppBar](#q12)

[↑ Back to top](#toc)

---

# E. Custom painting

> When no widget can draw what you need — a chart, a gauge, a signature pad — `CustomPainter` gives you a raw canvas. With that power comes a duty: control repaints so you don't redraw every frame for no reason.

---

<a id="q14"></a>
## 14. What is `CustomPainter`? How do `Canvas`, `Paint`, and `Path` work?

> Very common · Medium–Hard

**Short answer (say this):**
"`CustomPainter` gives me a raw 2D drawing surface, the `Canvas`, where I can draw shapes, lines, arcs, text, and paths. The `Canvas` is *where* I draw, `Paint` describes *how* (color, stroke vs fill, width), and `Path` describes a custom *shape* built from lines and curves. I use it when no existing widget can produce the visual."

**Let's understand it fully:**

**Step 1 — The three tools, in plain words.**
- **Canvas** = the paper. It has methods like `drawCircle`, `drawLine`, `drawRect`, `drawArc`, `drawPath`. Its origin `(0,0)` is the top-left.
- **Paint** = the brush settings: color, stroke width, fill vs outline, anti-aliasing, shaders.
- **Path** = a custom shape you build step by step (move here, line to there, curve, close).

```text
Canvas coordinate system:
(0,0) ----------> x
  |
  |   your drawing area (size.width x size.height)
  v
  y
```

**Step 2 — Set up a painter and choose fill vs stroke.**

```dart
class ChartPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    // Fill paint — solid shape
    final fill = Paint()
      ..color = Colors.blue.withValues(alpha: 0.3)
      ..style = PaintingStyle.fill;

    // Stroke paint — outline only
    final stroke = Paint()
      ..color = Colors.blue
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round;

    // A filled circle in the middle:
    canvas.drawCircle(Offset(size.width / 2, size.height / 2), 50, fill);

    // ... see Step 3 for a path and Step 4 for text
  }

  @override
  bool shouldRepaint(covariant ChartPainter oldDelegate) => false;
}
```

**Step 3 — Build a custom shape with `Path`.**
A `Path` connects points into any shape. Here is a triangle:

```dart
final path = Path()
  ..moveTo(size.width / 2, 20)                 // top vertex
  ..lineTo(size.width - 20, size.height - 20)  // bottom-right
  ..lineTo(20, size.height - 20)               // bottom-left
  ..close();                                   // connect back to start

canvas.drawPath(path, stroke);
```

**Step 4 — Drawing text uses `TextPainter`.**
You can't just call a `drawText`; you lay out a `TextPainter` first, then paint it:

```dart
final tp = TextPainter(
  text: const TextSpan(
    text: 'Score: 95',
    style: TextStyle(color: Colors.black, fontSize: 16),
  ),
  textDirection: TextDirection.ltr,
)..layout();
tp.paint(canvas, const Offset(10, 10));
```

**Step 5 — Show it with `CustomPaint`.**

```dart
CustomPaint(
  size: const Size(300, 300),
  painter: ChartPainter(),
);
```

**Why interviewers ask:** Charts, signature pads, gauges, game rendering, and unusual progress indicators all need this. They want to confirm you can drop to the drawing layer when widgets run out.

**Common mistake:** Forgetting that `Paint` defaults to `PaintingStyle.fill` — if you expected an outline but got a solid blob, set `PaintingStyle.stroke`. Another mistake: trying to draw text without `TextPainter`.

**Follow-ups they may ask:**
- *"How do you draw a gradient?"* → Set a `shader` on the `Paint`, e.g. `LinearGradient(...).createShader(rect)`.
- *"How do you clip to a shape?"* → `canvas.clipPath(path)` before drawing, or use a `CustomClipper`.

**Related:** [Q15 — painter vs widgets](#q15) · [Q16 — shouldRepaint](#q16)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. When should you use `CustomPainter` versus a widget composition approach?

> Common · Medium

**Short answer (say this):**
"Default to composing widgets. Reach for `CustomPainter` only when widgets can't make the shape, or when drawing it as widgets would be too expensive. Widgets give you hit testing, accessibility, and gestures for free; a custom painter gives raw control but you give those niceties up."

**Let's understand it fully:**

**Step 1 — Prefer widgets when you can.**
If a `Container`, `ClipRRect`, `Stack`, `DecoratedBox`, or `Transform` can do it, use them. You get accessibility, gesture handling, and easy maintenance with no extra effort.

```dart
// Rounded gradient card — NO CustomPainter needed:
Container(
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(16),
    gradient: const LinearGradient(colors: [Colors.purple, Colors.blue]),
    boxShadow: const [BoxShadow(color: Colors.black26, blurRadius: 10, offset: Offset(0, 4))],
  ),
  child: const Padding(padding: EdgeInsets.all(24), child: Text('Beautiful Card')),
);
```

**Step 2 — Use `CustomPainter` for shapes widgets can't make.**
Line charts, waveforms, radial gauges, signatures — these have no widget equivalent and must be drawn.

```dart
class LineChartPainter extends CustomPainter {
  final List<double> dataPoints;
  const LineChartPainter(this.dataPoints);

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.blue
      ..strokeWidth = 2
      ..style = PaintingStyle.stroke;

    final path = Path();
    for (var i = 0; i < dataPoints.length; i++) {
      final x = (i / (dataPoints.length - 1)) * size.width;
      final y = size.height - (dataPoints[i] / 100) * size.height;
      i == 0 ? path.moveTo(x, y) : path.lineTo(x, y);
    }
    canvas.drawPath(path, paint);
  }

  @override
  bool shouldRepaint(LineChartPainter old) => old.dataPoints != dataPoints;
}
```

**Step 3 — Also use it for performance with many primitives.**
If you'd need hundreds of tiny widgets (a scatter plot with 10,000 points, a particle effect), drawing them on one canvas is far cheaper than building thousands of widgets.

**Step 4 — A quick decision guide.**

| Situation | Choose |
|---|---|
| Standard shapes (rounded box, gradient, shadow) | widgets |
| Need gestures/accessibility on sub-parts | widgets |
| Shape no widget can make (chart, gauge, waveform) | `CustomPainter` |
| Hundreds/thousands of tiny visual elements | `CustomPainter` (performance) |

**Why interviewers ask:** They are testing architectural judgment. Jumping to `CustomPainter` for everything is over-engineering (harder to maintain, no built-in accessibility). Never using it means you can't handle custom visuals. Seniors pick the right one.

**Common mistake:** Hand-painting a rounded rectangle with a gradient (trivial with `Container` + `BoxDecoration`). The reverse: stacking `Container`s to fake a waveform instead of drawing it.

**Follow-ups they may ask:**
- *"What about accessibility on a custom-painted chart?"* → Wrap it in a `Semantics` widget and provide a label/value, since the painter has none (see [Q17](#q17)).
- *"Where do interactive charts fit?"* → Often a painter for the visuals plus a `GestureDetector` on top for taps.

**Related:** [Q14 — CustomPainter basics](#q14) · [Q16 — shouldRepaint & RepaintBoundary](#q16) · [Q17 — Semantics](#q17)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. What does `shouldRepaint` do, and how does `RepaintBoundary` help?

> Common · Medium

**Short answer (say this):**
"`shouldRepaint` tells Flutter whether the painter actually needs to redraw. I compare the new data with the old painter's data and return `false` when nothing changed, so I skip expensive redraws. `RepaintBoundary` is the partner trick: it isolates a part of the screen into its own layer, so repainting one area doesn't force everything around it to repaint too."

**Let's understand it fully:**

**Step 1 — `shouldRepaint` is a "do I need to redraw?" check.**
Flutter calls it with the previous painter instance. Return `true` to repaint, `false` to keep the old painting. Since `paint()` can be costly (complex paths, text layout), skipping it when nothing changed is a real win.

**Step 2 — How to write it correctly.**
Store the data your painter depends on as fields, then compare them:

```dart
class ProgressPainter extends CustomPainter {
  final double progress;   // 0.0 .. 1.0
  final Color color;
  const ProgressPainter({required this.progress, required this.color});

  @override
  void paint(Canvas canvas, Size size) {
    final rect = Rect.fromLTWH(0, 0, size.width, size.height);

    final bg = Paint()
      ..color = Colors.grey.shade300
      ..style = PaintingStyle.stroke
      ..strokeWidth = 10;
    canvas.drawArc(rect, -pi / 2, 2 * pi, false, bg);

    final fg = Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 10
      ..strokeCap = StrokeCap.round;
    canvas.drawArc(rect, -pi / 2, 2 * pi * progress, false, fg);
  }

  @override
  bool shouldRepaint(ProgressPainter old) =>
      old.progress != progress || old.color != color;  // only when data changed
}
```

**Step 3 — The two wrong answers.**
- Always returning `true` → repaints every frame, wasting GPU. (A common "to be safe" mistake.)
- Always returning `false` → the drawing never updates when data changes; you get a frozen, stale visual.

**Step 4 — `RepaintBoundary`: contain the repaint.**
Think of `RepaintBoundary` as a wall around a busy area. Without it, when one widget repaints (say a spinning animation), Flutter may repaint its neighbors too because they share a layer. Wrap the busy part in a `RepaintBoundary` and it gets its own layer — repaints stay inside the wall.

```dart
// The animated chart repaints constantly; isolate it so the rest of the
// screen is not repainted along with it:
RepaintBoundary(
  child: CustomPaint(painter: AnimatedChartPainter(...)),
);
```

This pairs naturally with custom painting and animations: `shouldRepaint` decides *whether* to repaint, and `RepaintBoundary` limits *how far* a repaint spreads.

**Why interviewers ask:** They want to know you understand Flutter's repaint optimization. On a screen with several `CustomPaint` widgets, returning `true` everywhere is wasted GPU work every frame.

**Common mistake:** Returning `true` "to be safe" (defeats the optimization) or `false` always (stale visuals). Also: comparing mutable lists with `==` (reference check) — use `listEquals` from `package:flutter/foundation.dart`, or keep the data immutable.

**Follow-ups they may ask:**
- *"Can `RepaintBoundary` be overused?"* → Yes — each one adds a layer and a little memory. Use it around genuinely busy areas, not everywhere.
- *"How do you confirm it helps?"* → Use DevTools' "Highlight Repaints" to see which areas repaint each frame.

**Related:** [Q14 — CustomPainter](#q14) · [Q15 — painter vs widgets](#q15) · [Q4 — AnimatedBuilder child](#q4)

[↑ Back to top](#toc)

---

# F. Accessibility

> Flutter builds two trees: the render tree you see, and a semantics tree that screen readers "see." Built-in widgets fill the semantics tree automatically; your custom widgets, icons, and gesture detectors often need help.

---

<a id="q17"></a>
## 17. What is the `Semantics` widget, and how do screen readers use it?

> Common · Medium

**Short answer (say this):**
"The `Semantics` widget attaches meaning to the UI for assistive tech like TalkBack on Android and VoiceOver on iOS. Flutter keeps a separate semantics tree describing what each element is. Many built-in widgets fill it automatically, but custom widgets, icons, images, and raw gesture detectors usually have no semantics — I add them with `Semantics`."

**Let's understand it fully:**

**Step 1 — Two trees in parallel.**
Flutter maintains the **render tree** (what you see) and the **semantics tree** (what a screen reader announces). `Text` contributes its content, `ElevatedButton` announces "button," `Checkbox` announces checked or not — all automatically.

```text
Widget tree              Semantics tree (what a screen reader says)
  Column                   "Shopping Cart screen"
   ├─ IconButton            ├─ "Back, button, double tap to activate"
   ├─ Image                 ├─ "Product photo: blue running shoes"
   ├─ GestureDetector       ├─ "Add to cart, button, double tap to activate"
   └─ Text                  └─ "Price: 99 dollars"
```

**Step 2 — The gap: custom and raw widgets have no semantics.**
A bare `GestureDetector`, a `CustomPaint`, and a decorative `Image` carry **no** meaning by default. To a screen reader they are invisible or silent. You fix this by wrapping them in `Semantics`.

**Step 3 — Add a label and a role.**

```dart
// An image has no inherent description:
Semantics(
  label: 'Company logo',
  image: true,
  child: Image.asset('assets/logo.png'),
);

// A custom tappable icon — announce it as a button and give the action:
Semantics(
  label: 'Delete item',
  button: true,
  onTap: _deleteItem,            // screen reader: "Delete item, button"
  child: GestureDetector(
    onTap: _deleteItem,
    child: const Icon(Icons.delete, color: Colors.red),
  ),
);
```

**Step 4 — Provide values and adjustable actions.**
For sliders and steppers, give the current value and how to change it:

```dart
Semantics(
  label: 'Volume',
  value: '${(_volume * 100).round()}%',
  increasedValue: '${((_volume + 0.1) * 100).round()}%',
  decreasedValue: '${((_volume - 0.1) * 100).round()}%',
  onIncrease: () => setState(() => _volume += 0.1),
  onDecrease: () => setState(() => _volume -= 0.1),
  child: CustomSlider(value: _volume),
);
```

**Why interviewers ask:** Accessibility is a legal requirement in many markets (ADA, EU rules) and the right thing to do. They want engineers who build apps everyone can use, not only sighted users with full motor control.

**Common mistake:** Assuming every widget is automatically accessible. Raw gesture detectors, custom-painted widgets, and decorative images have zero semantics by default. Another mistake: overly long labels like "This is a button you can tap to delete the item" — keep them short and action-first: "Delete item."

**Follow-ups they may ask:**
- *"What does `button: true` do?"* → It tells the screen reader to announce the element as a button, so the user knows it's tappable.
- *"How do you hide something from the reader?"* → Use `ExcludeSemantics` (see [Q18](#q18)).

**Related:** [Q18 — Exclude vs Merge](#q18) · [Q19 — testing accessibility](#q19) · [Q9 — gestures need semantics](#q9)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. What is the difference between `ExcludeSemantics` and `MergeSemantics`?

> Common · Medium

**Short answer (say this):**
"`ExcludeSemantics` removes its subtree from the semantics tree entirely — good for purely decorative elements. `MergeSemantics` combines everything under it into one announcement — good when several widgets form a single logical unit, like a star icon plus a rating plus a review count read as one item."

**Let's understand it fully:**

**Step 1 — `ExcludeSemantics` = make the screen reader ignore it.**
Use it for decoration that adds no meaning — a background wave, a spacer image. The reader skips it instead of announcing noise.

```dart
ExcludeSemantics(
  child: Image.asset('assets/decorative_wave.png'), // purely visual
);
```

**Step 2 — `MergeSemantics` = read several widgets as one.**
By default a row of icon + number + text is announced as three separate items, forcing the user to swipe three times. `MergeSemantics` folds them into one node, read in a single swipe.

```text
WITHOUT MergeSemantics            WITH MergeSemantics
reader says:                      reader says:
  "Star icon"                       "Rating: 4.5 stars, 128 reviews"
  "4.5"                             (one announcement, one swipe)
  "128 reviews"
  (three swipes)
```

```dart
MergeSemantics(
  child: Row(
    children: [
      const Icon(Icons.star, color: Colors.amber),
      const Text(' 4.5'),
      const Text(' (128 reviews)', style: TextStyle(color: Colors.grey)),
    ],
  ),
);
```

**Step 3 — Use them together.**
A common pattern: merge the parts into one unit *and* give it a clean label, excluding the now-redundant children.

```dart
Semantics(
  label: 'Call us',
  button: true,
  child: Row(
    children: const [
      ExcludeSemantics(child: Icon(Icons.phone)),   // decorative now
      ExcludeSemantics(child: Text('Call us')),      // label already says it
    ],
  ),
);
```

**Step 4 — The mental model.**
- Too many separate announcements? → `MergeSemantics`.
- Meaningless decoration cluttering the reader? → `ExcludeSemantics`.

**Why interviewers ask:** They want to know you think about the screen-reader *experience*, not just whether semantics exist. A card that fires 50 separate announcements is as unusable as one with none.

**Common mistake:** Using `ExcludeSemantics` on a real control the user must reach (like a close button). Only exclude truly decorative content. Another mistake: not merging custom list items, forcing users to swipe through every child of what should be one item.

**Follow-ups they may ask:**
- *"What if a merged group has two actions?"* → Don't merge then; the reader needs each action separately. Merge only single logical units.
- *"Is `MergeSemantics` the same as a `Semantics` label?"* → No. Merge folds existing children together; a `Semantics` label replaces/adds a description.

**Related:** [Q17 — Semantics](#q17) · [Q19 — testing accessibility](#q19)

[↑ Back to top](#toc)

---

<a id="q19"></a>
## 19. How do you test accessibility in Flutter?

> Common · Medium

**Short answer (say this):**
"I use several layers: the Semantics Debugger overlay to see the tree, widget tests that assert semantic labels and actions, the built-in guideline matchers for tap-target size and contrast, and — most importantly — manual testing with real TalkBack and VoiceOver. Automated checks catch labels and sizes; only manual testing confirms the experience makes sense."

**Let's understand it fully:**

**Step 1 — See the tree: the Semantics Debugger.**
Turn on a visual overlay that shows what screen readers would see:

```dart
MaterialApp(
  showSemanticsDebugger: true,  // visual overlay of the semantics tree
  home: const MyHomePage(),
);
```

**Step 2 — Assert semantics in widget tests.**
Verify labels and actions exist:

```dart
testWidgets('delete button is accessible', (tester) async {
  await tester.pumpWidget(const MyApp());

  expect(find.bySemanticsLabel('Delete item'), findsOneWidget);

  final node = tester.getSemantics(find.bySemanticsLabel('Delete item'));
  expect(node.hasAction(SemanticsAction.tap), isTrue);
});
```

**Step 3 — Use the built-in guideline matchers.**
Flutter ships matchers that check minimum tap-target size, text contrast, and label presence:

```dart
testWidgets('meets accessibility guidelines', (tester) async {
  await tester.pumpWidget(const MyApp());

  await expectLater(tester, meetsGuideline(androidTapTargetGuideline)); // 48x48
  await expectLater(tester, meetsGuideline(iOSTapTargetGuideline));     // 44x44
  await expectLater(tester, meetsGuideline(textContrastGuideline));     // contrast
  await expectLater(tester, meetsGuideline(labeledTapTargetGuideline)); // has labels
});
```

**Step 4 — Manual testing on real devices (the irreplaceable layer).**
Enable TalkBack (Android) and VoiceOver (iOS) and actually use the app:

- Swipe through every screen and confirm each interactive element is announced.
- Check the reading order is logical (top to bottom, left to right).
- Test with a large font scale and with screen magnification.
- Confirm dialogs, snackbars, and route changes announce correctly.

**Step 5 — DevTools inspector.**
The Flutter Inspector in DevTools shows the semantics tree beside the widget tree, useful for spotting missing or wrong nodes.

**Why interviewers ask:** They want a real methodology, not theory. Saying "we add `Semantics` widgets" without knowing how to verify them shows incomplete practice.

**Common mistake:** Relying only on automated tests. They check sizes and labels, but they cannot tell you whether the reading order is sensible, announcements are helpful, or the flow is usable. Manual testing with actual screen readers is essential and cannot be skipped.

**Follow-ups they may ask:**
- *"What's a good minimum tap target?"* → ~48x48 dp on Android, ~44x44 pt on iOS; the guideline matchers enforce this.
- *"How do you test announcements over time?"* → Manually with the screen reader, plus widget tests that pump and check semantics after state changes.

**Related:** [Q17 — Semantics](#q17) · [Q18 — Exclude vs Merge](#q18)

[↑ Back to top](#toc)

---

# G. Localization

---

<a id="q20"></a>
## 20. How do you implement multi-language support (l10n) using ARB files, `flutter_localizations`, and `intl`?

> Common · Medium

**Short answer (say this):**
"Three pieces work together. `flutter_localizations` translates built-in material widgets (date pickers, dialogs). ARB files hold my own strings, one file per language. The `gen-l10n` tool reads those ARB files and generates a typed `AppLocalizations` class, so a missing key is a compile error, not a runtime crash. I wire it into `MaterialApp` and read strings with `AppLocalizations.of(context)`."

**Let's understand it fully:**

**Step 1 — The three pieces.**
- **`flutter_localizations`** — built-in translations for material/cupertino widgets in many languages. Without it, even date pickers stay English.
- **ARB files** (Application Resource Bundle) — JSON-like files holding your strings: `app_en.arb`, `app_es.arb`, `app_bn.arb` (Bengali, useful for BD apps).
- **`intl` + `gen-l10n`** — code generation that turns the ARB files into a typed Dart class with a getter per string.

```text
Localization pipeline:

  app_en.arb ─┐
  app_es.arb ─┼─> flutter gen-l10n ─> AppLocalizations class
  app_bn.arb ─┘                            │
                                           v
                          AppLocalizations.of(context).welcomeMessage
                                           │
                                           v
                          "Welcome" / "Bienvenido" / "স্বাগতম"
                          (based on the device locale)
```

**Step 2 — Add dependencies and turn on generation (`pubspec.yaml`).**

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  intl: any

flutter:
  generate: true   # enables gen-l10n code generation
```

**Step 3 — Configure `l10n.yaml` in the project root.**

```yaml
arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
```

**Step 4 — Write the ARB files in `lib/l10n/`.**

`app_en.arb` (the template — describes placeholders and plurals):

```json
{
  "@@locale": "en",
  "welcomeMessage": "Welcome to our app!",
  "@welcomeMessage": { "description": "Greeting on the home screen" },

  "greeting": "Hello, {name}!",
  "@greeting": {
    "placeholders": { "name": { "type": "String" } }
  },

  "itemCount": "{count, plural, =0{No items} =1{1 item} other{{count} items}}",
  "@itemCount": {
    "description": "Number of items",
    "placeholders": { "count": { "type": "int" } }
  }
}
```

`app_bn.arb` (translations only — no need to repeat the metadata):

```json
{
  "@@locale": "bn",
  "welcomeMessage": "আমাদের অ্যাপে স্বাগতম!",
  "greeting": "হ্যালো, {name}!",
  "itemCount": "{count, plural, =0{কোনো আইটেম নেই} =1{১টি আইটেম} other{{count}টি আইটেম}}"
}
```

**Step 5 — Generate the code.**

```bash
flutter gen-l10n
```

**Step 6 — Wire it into `MaterialApp`.**

```dart
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

MaterialApp(
  supportedLocales: AppLocalizations.supportedLocales,
  localizationsDelegates: AppLocalizations.localizationsDelegates,
  home: const HomePage(),
);
```

**Step 7 — Use the strings in widgets.**

```dart
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    return Column(
      children: [
        Text(l10n.welcomeMessage),    // "Welcome to our app!"
        Text(l10n.greeting('Ahmed')), // "Hello, Ahmed!"
        Text(l10n.itemCount(0)),      // "No items"
        Text(l10n.itemCount(1)),      // "1 item"
        Text(l10n.itemCount(5)),      // "5 items"
      ],
    );
  }
}
```

**Why interviewers ask:** Localization is not optional for a global or BD-facing app. They want the full pipeline — ARB format, code generation, placeholders, plural rules, delegates — not just "use some JSON files."

**Common mistake:** Hardcoding `Text('Welcome')` everywhere and trying to retrofit l10n later — extremely painful. Start localized from day one. Another mistake: ignoring plural rules (some languages have several plural forms); the ICU `plural` syntax in ARB handles them, but you define the cases. Also: forgetting `generate: true` in `pubspec.yaml`, so `gen-l10n` produces files that never reach the build.

**Follow-ups they may ask:**
- *"How do you let the user switch language in-app?"* → Hold the chosen `Locale` in state and pass it to `MaterialApp`'s `locale:`; the typed class updates the strings.
- *"How are dates and numbers formatted per locale?"* → Use `intl`'s `DateFormat` and `NumberFormat`, which respect the active locale.

**Related:** [Q17 — Semantics (labels also need translating)](#q17)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**Implicit vs explicit animations**

| | Implicit | Explicit |
|---|---|---|
| You manage | nothing (just change a value) | the `AnimationController` |
| Examples | `AnimatedContainer`, `AnimatedOpacity` | `AnimationController` + `Tween` |
| Can loop / sequence? | no | yes |
| Best for | toggles, layout changes | spinners, staggered intros, control |

**`AnimatedBuilder` vs `AnimatedWidget`**

| | `AnimatedBuilder` | `AnimatedWidget` |
|---|---|---|
| Form | inline builder | a subclass you write |
| Best for | one-off, existing widget | reusable animated component |
| Skip rebuilding a child | pass it as `child` | wrap a static child inside |

**`GestureDetector` vs `Listener`**

| `Listener` | `GestureDetector` |
|---|---|
| raw pointer events (down/move/up) | recognized gestures (tap, drag, scale) |
| no interpretation | uses the gesture arena to pick one winner |
| custom, rare | the everyday choice |

**Sliver list types**

| `SliverList` | `SliverGrid` | `SliverFixedExtentList` |
|---|---|---|
| variable heights | 2D grid | one fixed height |
| good | good | fastest on huge lists |

**`SliverAppBar` flags**

| `pinned` | `floating` | `snap` (needs floating) |
|---|---|---|
| toolbar stays at top | reappears on scroll up | snaps fully in/out |

**`CustomPainter` vs widgets**

| Widgets | `CustomPainter` |
|---|---|
| standard shapes, free a11y/gestures | shapes no widget can make |
| easy to maintain | many primitives = perf win |

## One-line reminders

- **`AnimationController`** drives 0→1 each frame; `vsync` stops it off-screen; always `dispose()`. ([Q1](#q1))
- **`Tween`** maps 0→1 to a real range and does nothing without a controller (`tween.animate(controller)`). ([Q2](#q2))
- **Curves** bend linear progress into natural motion; `In`/`Out` = which end gets the effect. ([Q3](#q3))
- **`AnimatedBuilder`** rebuilds on each tick — pass the static part as `child` so it isn't rebuilt. ([Q4](#q4))
- **Implicit** = change a value (easy); **explicit** = hold a controller (loop, sequence, control). ([Q5](#q5))
- **Staggered** = one controller + an `Interval` per part, not many controllers. ([Q6](#q6))
- **`Hero`** flies a widget between screens; both sides need the **same, unique `tag`**. ([Q7](#q7))
- **Lottie** = After Effects JSON, playback only; **Rive** = `.riv` binary with interactive state machines. ([Q8](#q8))
- **`Listener`** = raw pointers; **`GestureDetector`** = recognized gestures; the **arena** picks one winner. ([Q9](#q9))
- **Slivers** paint on demand; wrap normal widgets in `SliverToBoxAdapter`, can't put slivers in a `Column`. ([Q10](#q10))
- **`SliverFixedExtentList`** beats `SliverList` for uniform-height huge lists (direct jump to visible). ([Q11](#q11))
- **`SliverAppBar`**: `pinned` stays, `floating` returns on scroll up, `snap` needs `floating`. ([Q12](#q12))
- **`CustomScrollView`** hosts slivers in one shared scroll; everything must be a sliver. ([Q13](#q13))
- **`CustomPainter`**: `Canvas` = where, `Paint` = how (default is fill!), `Path` = custom shape. ([Q14](#q14))
- **Default to widgets**; use `CustomPainter` for shapes widgets can't make or many primitives. ([Q15](#q15))
- **`shouldRepaint`** returns `false` when data is unchanged; **`RepaintBoundary`** walls off a busy area. ([Q16](#q16))
- **`Semantics`** fills the screen-reader tree; raw gesture/paint widgets have none by default. ([Q17](#q17))
- **`ExcludeSemantics`** hides decoration; **`MergeSemantics`** reads several widgets as one item. ([Q18](#q18))
- **Test a11y** with the debugger, guideline matchers, and (essential) real TalkBack/VoiceOver. ([Q19](#q19))
- **l10n**: ARB files + `gen-l10n` → typed `AppLocalizations`; missing keys fail at compile time. ([Q20](#q20))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers rarely stop at one question. They keep digging to test your depth. Practice answering this chain out loud — calmly, step by step:

1. *"How do you animate a box growing?"* → implicit `AnimatedContainer`, just change the size.
2. *"Now make it pulse forever."* → that needs looping, so go explicit: `AnimationController()..repeat()`.
3. *"How do you avoid rebuilding the whole widget each frame?"* → `AnimatedBuilder` with the static part passed as `child`.
4. *"The pulse animation makes the rest of the screen repaint — fix it."* → wrap the animated part in a `RepaintBoundary` to isolate its layer.
5. *"How would you prove the repaint is contained?"* → DevTools "Highlight Repaints" shows only that area flashing.

Being able to calmly go step by step like this — without guessing — is exactly what makes you sound **senior**, in both remote and BD interviews.

[↑ Back to top](#toc)

# Section 9 — Advanced Flutter

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-09-advanced-flutter.md](../software-engineer-flutter/section-09-advanced-flutter.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code দিয়ে ধাপে ধাপে পুরো ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর সেটা কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তরটা** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন — "আরও গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলাটাই একটা senior skill — remote আর BD দুই ধরনের কোম্পানিতেই এটা একইভাবে কাজ করে।

---


## <a id="toc"></a>সূচিপত্র

**A. Animations — engine আর তার অংশগুলো**
1. [`AnimationController` — vsync আর dispose](#q1) · *Very common*
2. [`Tween` — 0→1 range নতুন করে map করা](#q2) · *Very common*
3. [`CurvedAnimation` আর `Curves` (easing)](#q3) · *Common*
4. [`AnimatedWidget` বনাম `AnimatedBuilder`](#q4) · *Very common*
5. [Implicit বনাম explicit animation](#q5) · *Very common*
6. [`Interval` দিয়ে staggered animation](#q6) · *Common*

**B. Animations — screen-এর মাঝে আর tool দিয়ে**
7. [`Hero` animation আর `tag`-এর নিয়ম](#q7) · *Very common*
8. [Rive বনাম Lottie](#q8) · *Common*

**C. Gestures আর pointer event**
9. [`GestureDetector` বনাম `Listener` আর gesture arena](#q9) · *Very common*

**D. Slivers আর scrolling**
10. [Sliver কী আর কেন এগুলো আছে](#q10) · *Common*
11. [`SliverList` বনাম `SliverGrid` বনাম `SliverFixedExtentList`](#q11) · *Common*
12. [`SliverAppBar` — pinned / floating / snap](#q12) · *Very common*
13. [`CustomScrollView` — sliver একসাথে জোড়া](#q13) · *Common*

**E. Custom painting**
14. [`CustomPainter`, `Canvas`, `Paint`, `Path`](#q14) · *Very common*
15. [`CustomPainter` বনাম widget composition](#q15) · *Common*
16. [`shouldRepaint` আর `RepaintBoundary`](#q16) · *Common*

**F. Accessibility**
17. [`Semantics` আর screen reader](#q17) · *Common*
18. [`ExcludeSemantics` বনাম `MergeSemantics`](#q18) · *Common*
19. [Accessibility test করা](#q19) · *Common*

**G. Localization**
20. [ARB, `flutter_localizations`, `intl` দিয়ে multi-language (l10n)](#q20) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিউ)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

একসাথে ২০টা প্রশ্নই পড়ার দরকার নেই। এই পর্যায়গুলো একটার পর একটা শেষ করুন — প্রতিটা পর্যায় আগেরটার উপর দাঁড়ানো। কোনো পর্যায় শেষ ধরবেন তখনই, যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন।

**পর্যায় ১ — মূল animation অংশগুলো (এখান থেকে শুরু করুন)।** প্রায় প্রতিটা Flutter interview-এ এগুলো আসে।
→ [Q1 AnimationController](#q1) · [Q2 Tween](#q2) · [Q5 Implicit বনাম explicit](#q5) · [Q4 AnimatedBuilder বনাম AnimatedWidget](#q4)

**পর্যায় ২ — পরিপাটি, বাস্তব app-এর animation।** কোন জিনিস motion-কে ভালো অনুভব করায় আর আবার ব্যবহার করা যায় এমন করে।
→ [Q3 Curves](#q3) · [Q7 Hero](#q7) · [Q6 Staggered](#q6) · [Q8 Rive বনাম Lottie](#q8)

**পর্যায় ৩ — Touch আর scrolling।** আঙুল আর বড় list-এ app কীভাবে সাড়া দেয়।
→ [Q9 Gestures](#q9) · [Q10 Slivers](#q10) · [Q12 SliverAppBar](#q12) · [Q13 CustomScrollView](#q13)

**পর্যায় ৪ — নিজের pixel নিজে আঁকা।** যখন কোনো widget কাজটা করতে পারে না।
→ [Q14 CustomPainter](#q14) · [Q15 Painter বনাম widgets](#q15) · [Q16 shouldRepaint আর RepaintBoundary](#q16) · [Q11 Sliver-এর ধরন](#q11)

**পর্যায় ৫ — Senior signal: সবার কাছে, সব জায়গায় পৌঁছান।** এগুলোই শক্তিশালী senior-দের বাকিদের থেকে আলাদা করে।
→ [Q17 Semantics](#q17) · [Q18 Exclude/Merge](#q18) · [Q19 Accessibility testing](#q19) · [Q20 Localization](#q20)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই সাতটা রিভিউ করুন:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q5](#q5) · [Q7](#q7) · [Q9](#q9) · [Q14](#q14), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Animations — engine আর তার অংশগুলো

> Flutter animation একটা ছোট pipeline: একটা **controller** progress চালায়, একটা **Tween** সেই progress-কে আসল value-তে map করে, একটা **curve** গতির আকার ঠিক করে, আর একটা **widget** ফলাফল দেখায়। এই চারটা মাথায় ঢুকে গেলে বাকিটা সহজ।

---

## <a id="q1"></a>1. `AnimationController` কী? `vsync` ব্যাখ্যা করুন, আর কেন এটা dispose করতেই হবে বলুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`AnimationController` হলো explicit animation-এর পেছনের engine। এটা একটা সংখ্যা তৈরি করে — default-এ 0.0 থেকে 1.0 পর্যন্ত — একটা duration ধরে প্রতি frame-এ একবার। `vsync` এটাকে screen-এর frame clock-এর সাথে বেঁধে দেয়। ফলে widget দেখা যাওয়ার সময়েই শুধু tick হয়, battery বাঁচে। আমাকে এটার উপর `dispose()` call করতেই হবে। না হলে widget চলে যাওয়ার পরেও এর ticker চলতেই থাকে আর memory leak করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Controller-কে একটা ঘড়ি ভাবুন, যেটা motion চালায়।**
Controller নিজে কিছুই আঁকে না। এটা শুধু সময়ের সাথে সাথে সংখ্যার একটা নিয়মিত ধারা তৈরি করে — ঘড়ির কাঁটা 0.0 থেকে 1.0 পর্যন্ত ঘোরার মতো। তারপর আপনি সেই সংখ্যাগুলো একটা widget-এর সাথে জুড়ে দেন (size, opacity, rotation) — এভাবেই motion তৈরি হয়।

```dart
_controller = AnimationController(
  duration: const Duration(milliseconds: 800),
  vsync: this,           // ধাপ ৩-এ ব্যাখ্যা করা আছে
);
_controller.forward();   // শুরু: value 800ms-এ 0.0 -> 1.0 হয়
```

**ধাপ ২ — এটা যে যে value তৈরি করতে পারে।**
Default-এ value চলে `0.0 → 1.0`, কিন্তু দিক আর looping আপনি control করেন:

```dart
_controller.forward();   // 0.0 -> 1.0
_controller.reverse();   // 1.0 -> 0.0
_controller.repeat();    // চিরকাল loop চলবে
_controller.value;       // যেকোনো সময় বর্তমান সংখ্যাটা পড়ুন
```

**ধাপ ৩ — `vsync` = "screen-এ থাকলে তবেই tick করবে।"**
`vsync` মানে "vertical sync"। আপনি `vsync: this` পাঠান, এতে controller একটা `TickerProvider` পায়। Ticker হলো সেই জিনিস, যেটা প্রতি frame-এ একটা callback চালায় (সেকেন্ডে প্রায় 60 বা 120 বার)। `vsync`-এর মূল কথা এটাই: widget screen-এর বাইরে গেলে বা app background-এ গেলে ticker থেমে যায়। ফলে কেউ দেখছে না এমন জিনিস animate করে CPU, GPU আর battery নষ্ট হয় না।

`vsync` দিতে হলে আপনার `State`-এ একটা mixin যোগ করুন:

```dart
class _MyWidgetState extends State<MyWidget>
    with SingleTickerProviderStateMixin {   // 'this'-কে একটা ticker দেয়
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
    _controller.dispose();   // আবশ্যক — ধাপ ৪ দেখুন
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(opacity: _controller, child: const Text('Hello'));
  }
}
```

একটা controller-এর জন্য `SingleTickerProviderStateMixin` ব্যবহার করুন। সত্যিই একের বেশি controller থাকলে তবেই `TickerProviderStateMixin` ব্যবহার করুন।

**ধাপ ৪ — `dispose()` কেন optional নয়।**
Controller একটা ticker ধরে রাখে। Dispose করতে ভুলে গেলে widget সরে যাওয়ার পরেও ticker চিরকাল চলতে থাকে। এটা একটা memory leak। আর Flutter একটা পরিষ্কার error দেবে: *"A TickerProvider was disposed but a Ticker was not."* তাই নিয়মটা সহজ: `initState`-এ যে controller তৈরি করবেন, `dispose`-এ সেটা dispose করবেন।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি frame-by-frame pipeline বোঝেন কি না। `vsync` কেন আছে সেটাও (performance-এর জন্য, "মসৃণতার" জন্য নয়)। আর dispose-এর চুক্তিটা আপনি জানেন কি না। Dispose ভুলে যাওয়া বাস্তব production bug।

**সাধারণ ভুল:** বলা যে `vsync` "animation মসৃণ করে"। না — এটা animation-কে frame clock-এর সাথে বাঁধে। আর widget দেখা না গেলে সেটা থামিয়ে দেয়। আরেকটা ভুল: একটা মাত্র controller থাকলেও `TickerProviderStateMixin` (অনেক ticker) ব্যবহার করা; তখন `SingleTickerProviderStateMixin` ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"দুটো controller থাকলে কী করবেন?"* → single-টার বদলে `TickerProviderStateMixin` ব্যবহার করুন, আর দুটোই dispose করুন।
- *"Controller কি কিছু আঁকে?"* → না। এটা শুধু সংখ্যা তৈরি করে; `Tween` আর widget সেগুলোকে দৃশ্যে রূপ দেয়।

**সম্পর্কিত:** [Q2 — Tween](#q2) · [Q4 — AnimatedBuilder](#q4) · [Q5 — implicit বনাম explicit](#q5)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. `Tween` কী, আর এটা `AnimationController`-এর সাথে কীভাবে জোড়া লাগে?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা `Tween` শুরু আর শেষ ঠিক করে দেয়। Controller শুধু 0.0→1.0 দেয়, কিন্তু আমার ঠিক ওটাই খুব কম দরকার হয়। Tween সেই 0→1 progress-কে কাজের একটা range-এ map করে — একটা size, একটা color, একটা offset। আমি দুটোকে জোড়া লাগাই `tween.animate(controller)` দিয়ে, যেটা আমাকে ব্যবহার করার জন্য একটা `Animation<T>` দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Tween-কে ভাবুন শুরু/শেষের range, আর controller-কে ভাবুন dial।**
Controller হলো একটা dial, যেটা 0 থেকে 1-এ যায়। Tween বলে — "0 মানে *এই* value, 1 মানে *ওই* value।" মাঝখানের হিসাবটা Tween আপনার হয়ে করে দেয় ("tween" শব্দটা এসেছে "be**tween**" থেকে)।

```dart
// Controller: 0.0 -> 1.0
// Tween: 0.0 মানে 50, 1.0 মানে 200
final size = Tween<double>(begin: 50, end: 200);
```

**ধাপ ২ — `.animate(...)` দিয়ে এটাকে controller-এর সাথে জোড়ুন।**
`.animate(controller)` একটা `Animation<T>` ফেরত দেয় — এমন একটা object, যার `.value` controller-কে অনুসরণ করে, কিন্তু Tween-এর range-এ:

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

  // একই controller একসাথে অনেকগুলো tween চালাতে পারে:
  _sizeAnimation = Tween<double>(begin: 50, end: 200).animate(_controller);
  _colorAnimation =
      ColorTween(begin: Colors.red, end: Colors.blue).animate(_controller);

  _controller.forward();
}
```

**ধাপ ৩ — UI-তে value-গুলো পড়ুন।**
আপনি animation থেকে `.value` পড়েন, সাধারণত একটা `AnimatedBuilder`-এর ভেতরে ([Q4](#q4) দেখুন):

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

**ধাপ ৪ — শুধু Tween একা কিছুই করে না।**
এটাই মূল কথা। Tween হলো শুধু একটা range-এর বর্ণনা। সময় নিয়ে এর কোনো ধারণা নেই। Controller চালালে তবেই এটা animate করে। কিছু তৈরি করা tween-ও আছে: `ColorTween`, `SizeTween`, `RectTween`, আর `IntTween`।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি composition-টা বোঝেন কি না: controller কাঁচা 0→1 progress বানায়, Tween সেই progress-কে অর্থপূর্ণ value-তে map করে, আর widget সেটা দেখায়। এই আলাদা করাটাই explicit animation-এর পুরো mental model।

**সাধারণ ভুল:** Controller ছাড়া Tween ব্যবহার করার চেষ্টা করা (কিছুই হয় না — এর কোনো ঘড়ি নেই)। আরেকটা ভুল: প্রতি frame-এ `build()`-এর ভেতরে নতুন Tween বানানো; এটা একবার `initState`-এ তৈরি করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"সংখ্যা নয় এমন কিছুতে, যেমন color-এ, কীভাবে map করবেন?"* → `ColorTween` বা `Tween<Offset>`-এর মতো typed tween ব্যবহার করুন।
- *"একটা controller কি অনেকগুলো tween চালাতে পারে?"* → হ্যাঁ — প্রত্যেকটার উপর `.animate(controller)` call করুন। সবাই একই 0→1 progress ভাগ করে নেয়।

**সম্পর্কিত:** [Q1 — AnimationController](#q1) · [Q3 — CurvedAnimation](#q3) · [Q4 — AnimatedBuilder](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. `CurvedAnimation` কী? `Curves` কী, আর easing কীভাবে কাজে লাগাবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"সাধারণভাবে controller একই গতিতে চলে, যেটা দেখতে যান্ত্রিক লাগে। `CurvedAnimation` controller-কে মুড়ে নেয়। এটা সোজা 0→1 চলাকে বাঁকিয়ে স্বাভাবিক গতি দেয় — ধীরে শুরু, মাঝে দ্রুত, নরমভাবে থামা। একটা `Curve` আসলে একটা function, যেটা progress-কে নতুন আকার দেয়। Flutter-এ `Curves` class-এ অনেক তৈরি curve দেওয়া আছে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — গাড়ির উদাহরণ।**
আসল গাড়ি এক লাফে পুরো গতিতে যায় না, আর হঠাৎ থেমেও যায় না। এটা গতি বাড়ায়, সমান গতিতে চলে, তারপর ধীরে থামে। Curve motion-এ এই বাস্তব অনুভূতিটা যোগ করে। Curve ছাড়া animation একই সমান গতিতে চলে, আর চোখে সেটা "সস্তা" লাগে।

**ধাপ ২ — একটা `Curve` timeline-এর আকার বদলে দেয়।**
Curve সোজা input `t` (0.0 → 1.0) নেয় আর নতুন আকারের একটা মান ফেরত দেয়। যেমন `Curves.easeOut` শুরুতে দ্রুত চলে, তারপর নরমভাবে থামে:

```dart
final t = 0.5;                    // সময়ের ঠিক মাঝামাঝি
Curves.linear.transform(t);       // 0.5  (কোনো পরিবর্তন নেই)
Curves.easeOut.transform(t);      // ~0.7 (অনেকটা পথ আগেই পার হয়ে গেছে)
```

**ধাপ ৩ — `CurvedAnimation` দিয়ে controller-কে মুড়ুন, তারপর Tween যোগ করুন।**
ক্রমটা হলো: controller → curve → Tween।

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

  // ১. curve দিয়ে controller-এর progress বাঁকান:
  final curved = CurvedAnimation(
    parent: _controller,
    curve: Curves.easeOutBack,      // একটু বেশি এগিয়ে যায়, তারপর থিতু হয়
    reverseCurve: Curves.easeIn,    // উল্টো দিকে চলার সময় অন্য আকার
  );

  // ২. বাঁকানো progress-কে আসল range-এ map করুন:
  _animation = Tween<double>(begin: 0, end: 300).animate(curved);

  _controller.forward();
}
```

**ধাপ ৪ — সাধারণ curve আর কখন কোনটা ব্যবহার করবেন।**

| Curve | অনুভূতি | কীসের জন্য |
|---|---|---|
| `Curves.easeInOut` | দুই মাথাতেই মসৃণ | সাধারণ UI transition |
| `Curves.easeOut` | দ্রুত শুরু, নরম থামা | কিছু আসছে এমন |
| `Curves.easeIn` | নরম শুরু, দ্রুত শেষ | কিছু মিলিয়ে যাচ্ছে এমন |
| `Curves.bounceOut` | শেষে লাফায় | মজাদার, game-এর মতো UI |
| `Curves.elasticOut` | ছাড়িয়ে গিয়ে থিতু হয় | নজর কাড়ার জন্য |
| `Curves.decelerate` | স্বাভাবিকভাবে ধীর হওয়া | flick করার পরে থেমে যাওয়া |

`In`/`Out` নামটা বলে দেয় কোন মাথায় effect পড়বে: `bounceIn` শুরুতে লাফায়, `bounceOut` শেষে লাফায়।

**Interviewer কেন জিজ্ঞেস করে:** Curve জানা থাকলে animation শুধু "কাজ করে" না, "ভালো লাগে"ও। এটা পরিপাটি কাজের লক্ষণ, আর senior-দের কাছ থেকে এটাই আশা করা হয়।

**সাধারণ ভুল:** `bounceOut` বোঝাতে চেয়ে `bounceIn` ব্যবহার করা (ভুল মাথায় effect পড়ে)। আরেকটা ভুল: `CurvedAnimation` dispose করা নিয়ে চিন্তা করা — parent controller dispose হলে এটা নিজেই পরিষ্কার হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"নিজের custom curve লিখতে পারবেন?"* → হ্যাঁ — `Curve` extend করুন আর `transformInternal(double t)` override করুন।
- *"Chain-এ curve কোথায় বসে?"* → controller আর Tween-এর মাঝখানে: `Tween.animate(CurvedAnimation(parent: controller, curve: ...))`।

**সম্পর্কিত:** [Q1 — AnimationController](#q1) · [Q2 — Tween](#q2) · [Q6 — staggered animation](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. `AnimatedWidget` আর `AnimatedBuilder`-এর পার্থক্য কী, আর কখন কোনটা ব্যবহার করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"দুটোই animation দিয়ে UI rebuild করায়, আমাকে হাতে `setState` call করতে হয় না। `AnimatedWidget` হলো একটা subclass যেটা আমি বানাই — আবার ব্যবহার করা যায় এমন, নিজে নিজেই চলে এমন animated widget-এর জন্য ভালো। `AnimatedBuilder` হলো inline builder — চালু থাকা কোনো widget-এ motion যোগ করার জন্য ভালো। `AnimatedBuilder`-এর বড় কৌশল হলো `child` argument, যেটা একবার build হয় আর প্রতি frame-এ rebuild হয় না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুটোই কোন সমস্যা সমাধান করে।**
একটা animation সেকেন্ডে প্রায় 60 বার তার মান বদলায়। আপনি নিশ্চয়ই সেকেন্ডে 60 বার হাতে `setState` call করতে চান না। `AnimatedWidget` আর `AnimatedBuilder` দুটোই animation শোনে। যে ছোট অংশটা নড়ে, শুধু সেটাই rebuild করে।

**ধাপ ২ — `AnimatedWidget`: আবার ব্যবহার করা যায় এমন animated widget বানান (subclass)।**
আপনি `AnimatedWidget` extend করেন আর animation-টা `listenable` হিসেবে পাঠান। Animation tick করলেই widget নিজেকে rebuild করে। পরিষ্কার, আবার ব্যবহার করা যায় এমন component চাইলে এটাই সেরা।

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

// ব্যবহার:
PulsatingCircle(animation: _sizeAnimation);
```

**ধাপ ৩ — `AnimatedBuilder`: চালু থাকা widget-এ inline animation।**
আপনি একটা `builder` callback পাঠান। নতুন কোনো class লাগে না। একবার-ব্যবহারের animation-এর জন্য সেরা।

```dart
AnimatedBuilder(
  animation: _controller,
  child: const FlutterLogo(size: 100),   // একবারই build হয় — ধাপ ৪ দেখুন
  builder: (context, child) {
    return Transform.rotate(
      angle: _controller.value * 2 * pi,
      child: child,                       // আবার ব্যবহার হয়, rebuild হয় না
    );
  },
);
```

**ধাপ ৪ — `child` কৌশল (যে performance পয়েন্টটা তাঁরা শুনতে চান)।**
`AnimatedBuilder`-এ আপনি যে `child` পাঠান, সেটা একবার build হয়। তারপর প্রতি frame-এ আপনার `builder`-কে সেটাই ফেরত দেওয়া হয়। তাই প্রতি frame-এ শুধু মোড়কটা (এখানে `Transform.rotate`) নতুন করে তৈরি হয় — ভারী child নয়। Interviewer এই optimization-টাই শুনতে চান।

**ধাপ ৫ — কোনটা বেছে নেবেন।**

| | `AnimatedWidget` | `AnimatedBuilder` |
|---|---|---|
| গঠন | আপনার লেখা একটা subclass | একটা inline builder |
| কীসের জন্য সেরা | আবার ব্যবহার করা যায় এমন animated component | একবারের কাজ, চালু tree-তে motion যোগ করা |
| Child-এর rebuild এড়ানো? | ভেতরে static child মুড়ে দিন | `child` হিসেবে পাঠান |

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান animation-এর সময় ভারী widget rebuild করা আপনি এড়াতে জানেন কি না। আরও দেখতে চান আপনি composition (`AnimatedBuilder`) আর inheritance (`AnimatedWidget`)-এর পার্থক্য বোঝেন কি না।

**সাধারণ ভুল:** ভারী widget tree `AnimatedBuilder`-এর `builder`-এর ভেতরে বানানো, `child` হিসেবে না পাঠিয়ে। তখন সেটা সেকেন্ডে 60 বার rebuild হয়। Static অংশটা `child` হিসেবে পাঠান আর সেটাকেই ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`child` কেন দ্রুত?"* → এটা একবার তৈরি হয় আর বারবার ব্যবহার হয়; প্রতি frame-এ শুধু মোড়ক widget-টা rebuild হয়।
- *"Transition widget-গুলো কি এর সাথে সম্পর্কিত?"* → হ্যাঁ — `FadeTransition`, `ScaleTransition` ইত্যাদি একই listenable ধারণার উপরে বানানো। কাজে লাগলে এগুলো আরও সহজ।

**সম্পর্কিত:** [Q2 — Tween](#q2) · [Q5 — implicit বনাম explicit](#q5) · [Q16 — RepaintBoundary](#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Implicit আর explicit animation-এর পার্থক্য কী, আর কখন কোনটা ব্যবহার করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Implicit animation হলো সহজ mode: আমি শুধু একটা মান বদলাই, আর `AnimatedContainer`-এর মতো widget সেই পরিবর্তনটা animate করে দেয় — কোনো controller লাগে না। Explicit animation পুরো control দেয় — start, stop, loop, reverse, sequence — কিন্তু `AnimationController` আমাকে নিজেই সামলাতে হয়। আমি সাধারণভাবে implicit বেছে নিই। Looping, sequencing বা code থেকে control লাগলে তবেই explicit-এ যাই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Implicit = "নতুন মান বসান, বাকিটা Flutter করবে।"**
আপনি একটা duration আর একটা curve দেন, তারপর শুধু target বদলান। Flutter নিজেই পুরোনো মান থেকে নতুন মানে animate করে। কোনো controller নেই, tween নেই, dispose নেই।

```dart
// Tap করলে _isExpanded বদলায়; box নিজেই animate হয়:
AnimatedContainer(
  duration: const Duration(milliseconds: 300),
  curve: Curves.easeInOut,
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  color: _isExpanded ? Colors.blue : Colors.red,
  child: const Text('Tap me'),
);
```

সাধারণ implicit widget: `AnimatedContainer`, `AnimatedOpacity`, `AnimatedPadding`, `AnimatedPositioned`, `AnimatedAlign`, `AnimatedDefaultTextStyle`, `AnimatedCrossFade`, আর `TweenAnimationBuilder` (নিজের বানানো একবারের মানের জন্য)।

**ধাপ ২ — Explicit = "controller আমার হাতে, সব সিদ্ধান্ত আমার।"**
আপনি একটা `AnimationController` বানান আর সেটা চালান। Loop করা, চাহিদামতো উল্টো দিকে চালানো, কয়েকটা animation মিলিয়ে চালানো, বা ঠিক নির্দিষ্ট মুহূর্তে থামানো — এগুলোর একমাত্র উপায় এটাই।

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
    )..repeat();   // চিরকাল loop করে — implicit দিয়ে অসম্ভব
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

**ধাপ ৩ — সিদ্ধান্ত নেওয়ার সহজ নিয়ম।**
একটাই প্রশ্ন করুন: *motion-টার কি loop, sequence, বা code দিয়ে control দরকার?*

- **না** → implicit (কম code, কম bug): toggle, layout পরিবর্তন, hover effect, একবারের fade-in।
- **হ্যাঁ** → explicit: spinner, বারবার চলা pulse, staggered intro, swipe-to-dismiss progress, আর যা কিছু code থেকে শুরু ও বন্ধ করেন।

**ধাপ ৪ — এই পছন্দটা কেন গুরুত্বপূর্ণ।**
সাধারণ একটা রঙ বদলানোর জন্য explicit controller ব্যবহার করা মানে over-engineering — বেশি code, আর dispose মনে রাখার ঝামেলা। আর জটিল সাজানো sequence-এর জন্য implicit ব্যবহার করা সোজা কথায় অসম্ভব। সঠিকটা বেছে নেওয়া একটা senior signal।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি সঠিক tool বেছে নেন কি না। যেকোনো দিকেই ভুল পছন্দ একটা red flag।

**সাধারণ ভুল:** সব কিছুর জন্য `AnimationController` ধরা। দৈনন্দিন বেশিরভাগ UI motion (state toggle, layout সরে যাওয়া) implicit হওয়া উচিত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"যে মানের জন্য কোনো `AnimatedX` widget নেই, তার কী হবে?"* → `TweenAnimationBuilder` ব্যবহার করুন — এটা implicit, কিন্তু আপনার সংজ্ঞা দেওয়া যেকোনো মানের জন্য চলে।
- *"দুটো কি মেশানো যায়?"* → হ্যাঁ, তবে পরিষ্কার রাখুন; সাধারণত একটা screen একদিকেই ঝোঁকে।

**সম্পর্কিত:** [Q1 — AnimationController](#q1) · [Q4 — AnimatedBuilder](#q4) · [Q6 — staggered animation](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. Staggered animation (কয়েকটা অংশ আলাদা আলাদা সময়ে নড়ে) কীভাবে বানাবেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Staggered animation একটাই controller থেকে কয়েকটা অংশ চালায়। কিন্তু প্রতিটা অংশ timeline-এর আলাদা আলাদা ভাগে active থাকে। আমি একটা `AnimationController` ব্যবহার করি। আর প্রতিটা অংশকে `Interval` সহ একটা `CurvedAnimation` দিই। সেটা বলে — 'শুধু মোট সময়ের 0.0 থেকে 0.5 এর মধ্যে animate করো।' একটাই ঘড়ি, অনেক অংশ, আলাদা শুরু আর শেষ সময়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — রিলে রেসের ধারণা।**
ভাবুন একটা stopwatch দিয়ে একটা রিলে রেসের সময় মাপা হচ্ছে। প্রথম দৌড়বিদ সময়ের প্রথম ভাগে দৌড়ায়, দ্বিতীয়জন মাঝখানে, তৃতীয়জন শেষে। stopwatch কিন্তু একটাই (একটা controller)। প্রতিটা দৌড়বিদ শুধু তার নিজের ভাগটা পায়।

**ধাপ ২ — পুরো sequence-এর জন্য একটাই controller ব্যবহার করুন।**
আপনি তিনটা controller বানাবেন **না**। একটাই বানাবেন। তার 0→1 পুরো sequence-টা ঢেকে রাখে:

```dart
_controller = AnimationController(
  duration: const Duration(milliseconds: 1200), // মোট সময়
  vsync: this,
);
```

**ধাপ ৩ — প্রতিটা অংশকে একটা `Interval` দিন।**
`Interval` হলো এমন একটা curve, যেটা নিজের window-এর বাইরে স্থির থাকে আর ভেতরে animate করে। `Interval(0.0, 0.5)` মানে "তোমার নড়াচড়াটা timeline-এর প্রথম অর্ধেকে করো।"

```dart
// Timeline-এর প্রথম 40%-এ fade in:
final fade = CurvedAnimation(
  parent: _controller,
  curve: const Interval(0.0, 0.4, curve: Curves.easeOut),
);

// মাঝখানে উপরের দিকে slide (30% -> 70%):
final slide = Tween<Offset>(
  begin: const Offset(0, 0.3),
  end: Offset.zero,
).animate(CurvedAnimation(
  parent: _controller,
  curve: const Interval(0.3, 0.7, curve: Curves.easeOut),
));

// শেষে scale (60% -> 100%):
final scale = CurvedAnimation(
  parent: _controller,
  curve: const Interval(0.6, 1.0, curve: Curves.easeOutBack),
);
```

**ধাপ ৪ — সব যুক্ত করুন আর একবার চালান।**

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

// কোথাও একটা জায়গায়: _controller.forward();
```

এখন card প্রথমে fade হবে, তারপর slide করবে, তারপর pop করবে — সবই একটা `forward()` call থেকে।

**Interviewer কেন জিজ্ঞেস করে:** পালিশ করা app-এ staggered intro সব জায়গায় থাকে (onboarding, list reveal)। তাঁরা দেখতে চান আপনি জানেন কি না যে কৌশলটা হলো *একটা controller আর কয়েকটা interval*। অনেকগুলো controller একে অপরের সাথে লড়াই করা নয়।

**সাধারণ ভুল:** প্রতিটা element-এর জন্য আলাদা controller বানানো, আর delay দিয়ে সেগুলো শুরু করার চেষ্টা করা। এটা sync-এ রাখা কঠিন। Interval সহ একটা controller একদম নিখুঁতভাবে সারিবদ্ধ থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"পুরো একটা list কীভাবে stagger করবেন?"* → *i* নম্বর item-কে এমন একটা interval দিন যেটা তার index-এর সাথে সরে যায়। অথবা `flutter_staggered_animations`-এর মতো package ব্যবহার করুন।
- *"`Interval` তার window-এর বাইরে কী return করে?"* → clamp করা শেষ মান (শুরুর আগে 0, শেষের পরে 1)। তাই অংশটা শুধু স্থির হয়ে থাকে।

**সম্পর্কিত:** [Q3 — Curves](#q3) · [Q1 — AnimationController](#q1) · [Q4 — AnimatedBuilder](#q4)

[↑ উপরে ফিরুন](#toc)

---

# B. Animations — screen-এর মাঝে এবং tool দিয়ে

---

## <a id="q7"></a>7. Route-এর মাঝে `Hero` animation কীভাবে কাজ করে? `tag`-এর শর্তটা কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`Hero` একটা widget-কে navigation-এর সময় এক screen থেকে আরেক screen-এ উড়ে যাওয়ার মতো দেখায় — যেমন list-এর ছোট thumbnail বড় হয়ে পুরো detail image হয়ে যায়। দুই screen-এ একই widget-কে একই `tag` ব্যবহার করতে হবে। Flutter এই tag দিয়ে দুটোকে মেলায়। তারপর route transition-এর সময় widget-এর size আর position animate করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Hero-কে ভাবুন এক screen থেকে আরেক screen-এ উড়ে যাওয়া একটাই জিনিস হিসেবে।**
Screen A-তে একটা ছোট avatar আছে। আপনি tap করলেন, screen B-তে গেলেন। ওই একই avatar বড় হয়ে নতুন জায়গায় সরে গেল। মনে হয় একটাই জিনিস সরল, দুটো আলাদা image নয়। এই টানা মিলটাই Hero effect।

**ধাপ ২ — ভেতরে এটা কীভাবে কাজ করে।**
Route transition-এর সময় Flutter:
1. source route-এর `Hero` খুঁজে বের করে আর তার size ও position মাপে।
2. গন্তব্য route-এ **একই tag** সহ `Hero` খুঁজে বের করে আর তার লক্ষ্য size ও position মাপে।
3. দুই screen-এর উপরে একটা overlay-তে একটা copy তুলে নেয়। তারপর source rect থেকে গন্তব্য rect পর্যন্ত সেটা animate করে।
4. Transition শেষ হলে সেটাকে জায়গামতো বসিয়ে দেয়।

**ধাপ ৩ — `tag`-এর নিয়ম।**
দুটো hero-কেই **একই `tag`** ব্যবহার করতে হবে। আর প্রতিটা tag **একটা screen-এর ভেতরে unique** হতে হবে। এই tag দিয়েই Flutter বোঝে কোন hero-র সাথে কোনটা মেলে।

```dart
// Screen A — source (একটা list-এর ভেতরে)
GestureDetector(
  onTap: () => Navigator.push(
    context,
    MaterialPageRoute(builder: (_) => const DetailScreen()),
  ),
  child: Hero(
    tag: 'avatar-123',        // গন্তব্যের সাথে মিলতে হবে
    child: CircleAvatar(radius: 30, backgroundImage: NetworkImage(imageUrl)),
  ),
);

// Screen B — গন্তব্য
Scaffold(
  body: Center(
    child: Hero(
      tag: 'avatar-123',      // উৎসের মতোই একই tag
      child: CircleAvatar(radius: 100, backgroundImage: NetworkImage(imageUrl)),
    ),
  ),
);
```

**ধাপ ৪ — List-এ unique tag লাগে।**
একটা `ListView`-এ প্রতিটা item-কে কখনোই `'image'`-এর মতো একই tag দেবেন না — tag সংঘর্ষ করায় runtime-এ crash হবে। Item-এর id ব্যবহার করুন:

```dart
Hero(tag: 'image-${product.id}', child: ...);
```

**ধাপ ৫ — ওড়ার সময়ের চেহারা নিজের মতো করা।**
দুই screen-এ widget-টা দেখতে আলাদা হলে (যেমন আলাদা corner radius), ওড়াটা লাফিয়ে লাফিয়ে দেখাতে পারে। ওড়ার সময় ঠিক কী আঁকা হবে তা control করতে `flightShuttleBuilder` ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** Hero transition সবচেয়ে বেশি প্রভাব ফেলা UX pattern-গুলোর একটা (photo gallery, product detail, profile)। তাঁরা দেখতে চান আপনি tag matching আর overlay flight path বোঝেন কি না। শুধু widget-টার নাম `Hero` — এটুকু নয়।

**সাধারণ ভুল:** একটা list-এর অনেক item-এ একই tag আবার ব্যবহার করা (runtime error)। আরেকটা ভুল: দুটো hero-কে খুব আলাদা layout-এ মুড়ে দেওয়া, ফলে child ওড়ার মাঝপথে আকার বদলায়; এটা `flightShuttleBuilder` দিয়ে ঠিক করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"tag না মিললে কী হয়?"* → কোনো flight হয় না; এটা shared element ছাড়া সাধারণ একটা page push হয়।
- *"child কি পুরো একটা card হতে পারে?"* → হ্যাঁ, তবে শুরু আর শেষের আকার কাছাকাছি রাখুন। নাহলে ওড়াটা অদ্ভুত দেখায়।

**সম্পর্কিত:** [Q5 — explicit বনাম implicit](#q5) · [Q8 — Rive বনাম Lottie](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. Rive আর Lottie-র মধ্যে পার্থক্য কী, আর কখন কোনটা ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"দুটোই আগে থেকে design করা animation চালায়, কিন্তু ক্ষমতায় আলাদা। Lottie চালায় After Effects থেকে JSON হিসেবে export করা একটা নির্দিষ্ট animation — শুধুই playback। Rive-এর নিজের editor আছে আর একটা ছোট binary file আছে। এটা state machine support করে, তাই animation runtime-এ tap আর app state-এর সাথে সাড়া দিতে পারে। সাজসজ্জার নড়াচড়ার জন্য Lottie ঠিক আছে; interactive নড়াচড়ার জন্য Rive বেছে নিন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Lottie = designer-এর বানানো animation চালানো।**
Pipeline-টা এমন: একজন designer Adobe After Effects-এ animation বানান, Bodymovin plugin দিয়ে একটা `.json` file-এ export করেন, আর Flutter সেই file চালায়। আপনি যা দেখেন, designer ঠিক সেটাই বানিয়েছেন। আপনি play, pause, loop আর scrub করতে পারবেন — কিন্তু runtime-এ এর logic-কে আলাদা পথে চালাতে পারবেন না।

```dart
import 'package:lottie/lottie.dart';

Lottie.asset(
  'assets/animations/loading.json',
  width: 200,
  height: 200,
  repeat: true,
);
```

**ধাপ ২ — Rive = state machine সহ interactive animation।**
Rive-এর নিজের web-based editor আছে আর এটা ছোট `.riv` binary export করে। এর প্রধান গুণ হলো **state machine**: input (একটা tap, একটা boolean, একটা number) runtime-এ animation state-গুলোর মধ্যে transition চালায়। তাই একটা Rive file-ই এমন একটা animated button হতে পারে যা press-এ সাড়া দেয়।

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
      onTap: () => _press?.fire(),   // state machine-কে সাড়া দিতে বলে
      child: RiveAnimation.asset('assets/button.riv', onInit: _onInit),
    );
  }
}
```

**ধাপ ৩ — পাশাপাশি একটা তুলনা।**

| | Lottie | Rive |
|---|---|---|
| source tool | After Effects + Bodymovin | Rive editor |
| File | `.json` (text) | `.riv` (binary, ছোট) |
| Runtime logic | শুধু playback | state machine, input, condition |
| Input-এ সাড়া দেয় | না | হ্যাঁ |
| কীসের জন্য ভালো | সাজসজ্জার নড়াচড়া | interactive নড়াচড়া |

**ধাপ ৪ — কখন কোনটা বেছে নেবেন।**
- **Lottie:** আপনার team আগে থেকেই After Effects-এ কাজ করে; animation-টা সাজসজ্জার (loading spinner, success checkmark, onboarding art); runtime-এ কোনো interaction লাগবে না।
- **Rive:** আপনার interactivity লাগবে (animated toggle, character-এর প্রতিক্রিয়া), runtime-এ state বদল লাগবে, অথবা জটিল দৃশ্যে ছোট file আর ভালো performance লাগবে।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি tooling-এর trade-off নিয়ে team-কে পরামর্শ দিতে পারেন কি না। আর আপনি design থেকে code পর্যন্ত pipeline বোঝেন কি না, শুধু Dart-এর দিকটা নয়।

**সাধারণ ভুল:** বলা যে "দুটো একই জিনিস, শুধু file format আলাদা।" এগুলো মূল জায়গাতেই আলাদা: Rive-এ interactive state machine আছে; Lottie-তে নেই। আরেকটা ভুল: file size বাদ দেওয়া — জটিল Lottie JSON বেশ বড় হয়ে যেতে পারে, যেখানে `.riv` ছোট থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Lottie কি একটা tap-এ সাড়া দিতে পারে?"* → শুধু মোটা দাগে (একটা segment চালানো, speed বদলানো)। এর সত্যিকারের কোনো state logic নেই; ওটা Rive-এর কাজ।
- *"Rive প্রায়ই বেশি performant কেন?"* → একটা ছোট binary format, আর real-time graphics-এর জন্য বানানো একটা runtime। এর বিপরীতে বড় JSON parse করা লাগে।

**সম্পর্কিত:** [Q7 — Hero](#q7) · [Q5 — implicit বনাম explicit](#q5)

[↑ উপরে ফিরুন](#toc)

---

# C. Gestures ও pointer events

> Flutter-এ touch-এর দুটো layer আছে: raw pointer event (`Listener`) আর চেনা gesture যেমন tap, drag, scale (`GestureDetector`)। Senior-দের কাছ থেকে আশা করা হয় তাঁরা এই পার্থক্য জানবেন। আর জানবেন Flutter কীভাবে ঠিক করে একটা touch কে "জিতবে"।

---

## <a id="q9"></a>9. `GestureDetector` আর `Listener`-এর মধ্যে পার্থক্য কী? আর gesture arena কী?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`Listener` আমাকে raw pointer event দেয় — down, move, up — কোনো ব্যাখ্যা ছাড়া। `GestureDetector` তার উপরে বসে অর্থপূর্ণ gesture চেনে, যেমন tap, double-tap, long-press, drag আর scale। যখন একের বেশি widget একই touch দাবি করতে পারে, তখন Flutter একটা 'gesture arena' চালায় ঠিক করতে কে জিতবে। ফলে দুটো gesture একসাথে fire করে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `Listener` = আঙুলের raw data।**
`Listener` low-level pointer event ঠিক যেভাবে ঘটে সেভাবেই জানায়। "tap" বা "swipe" কী, সেটা এটা জানে না। এটা শুধু বলে আঙুল নামল, সরল, আর উঠে গেল।

```dart
Listener(
  onPointerDown: (e) => print('finger down at ${e.position}'),
  onPointerMove: (e) => print('moved by ${e.delta}'),
  onPointerUp: (e) => print('finger up'),
  child: const ColoredBox(color: Colors.amber, child: SizedBox(width: 100, height: 100)),
);
```

এটা সরাসরি খুব কমই লাগে। এটা custom interaction-এর জন্য, যেখানে built-in gesture মানানসই হয় না।

**ধাপ ২ — `GestureDetector` = চেনা gesture।**
`GestureDetector` ওই raw event-গুলোকে সেই gesture-এ রূপ দেয়, যেগুলো আপনার আসলে দরকার। 95% সময় এটাই ব্যবহার করবেন।

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

**ধাপ ৩ — সমস্যা: touch-এর মালিক কে?**
ধরুন একটা scrollable list-এর ভেতরে ছোট একটা tappable card আছে। আপনি চাপ দিলে সেটা কি card-এর উপর tap, নাকি scroll-এর শুরু? দুজনেই একই আঙুল চায়। দুটোই fire করলে আপনি পেতেন একটা tap *এবং* একটা scroll — ভুল।

**ধাপ ৪ — Gesture arena বিজয়ী ঠিক করে।**
Flutter এটা সমাধান করে **gesture arena** দিয়ে। এটাকে touch-এর জন্য একটা নিলাম ভাবুন:
1. আঙুল নামলে আগ্রহী প্রতিটা recognizer (tap, drag, scroll) arena-তে ঢোকে।
2. আঙুল সরার সাথে সাথে recognizer-রা হয় **জয় দাবি করে** (যেমন আঙুল drag হওয়ার মতো যথেষ্ট দূরে সরেছে), নয়তো **হাল ছেড়ে দেয়** (আঙুল বেশি সরলেই tap recognizer সরে যায়)।
3. ঠিক একটা recognizer জেতে; বাকিগুলো cancel হয়। তাই আপনি পান *হয়* একটা tap *নয়* একটা scroll, কখনোই দুটো একসাথে নয়।

এই কারণেই `ListView`-এর ভেতরে tap এখনও কাজ করে। কিন্তু আঙুল সরালে সেটা scroll হয়ে যায় — স্পষ্টভাবে drag হয়ে গেলেই arena touch-টা scroll recognizer-কে দিয়ে দেয়।

**ধাপ ৫ — `behavior`: ফাঁকা জায়গায় tap ধরা।**
Default অবস্থায় একটা `GestureDetector` শুধু সেই touch পায় যেটা তার child-এর আঁকা pixel-এ পড়ে। স্বচ্ছ বা ফাঁকা জায়গার tap ধরতে hit-test behavior সেট করুন:

```dart
GestureDetector(
  behavior: HitTestBehavior.opaque,  // পুরো এলাকা tappable, ফাঁকা জায়গাও
  onTap: _dismissKeyboard,
  child: const SizedBox.expand(),
);
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি দুটো layer জানেন কি না (raw বনাম চেনা gesture)। আর আপনি ব্যাখ্যা করতে পারেন কি না Flutter কীভাবে gesture-এর সংঘর্ষ এড়ায়। Arena-ই উত্তরের senior-level অংশ।

**সাধারণ ভুল:** সাধারণ tap-এর জন্য `Listener` ধরা — `GestureDetector` ব্যবহার করুন। আরেকটা ভুল: একটা touch থেকে দুটো gesture fire করবে আশা করা; arena একটাই বিজয়ী নিশ্চিত করে। ফাঁকা জায়গায় tap দরকার হলে `HitTestBehavior.opaque` ভুলে যাওয়াও একটা ভুল (যেমন keyboard বন্ধ করা)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আমার tap `Stack`-এর ভেতরে fire করে না কেন?"* → উপরের কোনো sibling hit test শুষে নিচ্ছে হয়তো; `behavior` আর z-order দেখুন।
- *"`onPanUpdate` বনাম `onScaleUpdate`?"* → একটা detector-এ দুটোই ব্যবহার করা যায় না — scale হলো superset (এটা drag-ও জানায়)। তাই pan আর pinch দুটোই লাগলে scale callback ব্যবহার করুন।
- *"`RawGestureDetector` কী?"* → আরও নিচু স্তরের version, যেখানে আপনি নিজের custom recognizer arena-তে register করেন।

**সম্পর্কিত:** [Q7 — Hero (tap করে navigate)](#q7) · [Q17 — Tappable widget-এর জন্য Semantics](#q17)

[↑ উপরে ফিরুন](#toc)

---

# D. Slivers ও scrolling

> Sliver হলো একটা scrollable section, যেটা scroll position অনুযায়ী চাহিদামতো content আঁকে। `ListView`-ও ভেতরে একটা sliver। Sliver দিয়ে header, grid আর list এক মসৃণ scroll-এ মেশানো যায়।

---

## <a id="q10"></a>10. Sliver কী, আর এগুলো কেন আছে?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Sliver হলো একটা low-level scrollable section, যেটা scroll করার সাথে সাথে চাহিদামতো দেখা যায় এমন content বানায়। এগুলো আছে যাতে আপনি আলাদা আলাদা scroll behavior এক scroll view-তে মেশাতে পারেন — একটা collapsing app bar, তারপর একটা grid, তারপর একটা list। `ListView` আর `GridView` আসলে sliver-এর উপরে বন্ধুত্বপূর্ণ মোড়ক।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সাধারণ `ListView` কেন যথেষ্ট নয়।**
`ListView` ধরে নেয় পুরোটায় একটাই একরকম scroll behavior। কিন্তু বাস্তব screen-এ প্রায়ই এক scroll-এ কয়েকটা behavior লাগে: একটা header image যেটা ছোট হয়, তারপর একটা horizontal carousel, তারপর একটা grid, তারপর একটা list। এর জন্য scrollable-এর ভেতরে scrollable বসানো অস্বস্তিকর আর bug-ভরা। Sliver এটা সমাধান করে।

**ধাপ ২ — Conveyor belt-এর ধারণা।**
Scroll view-টাকে একটা conveyor belt ভাবুন। প্রতিটা sliver সেই belt-এর একটা অংশ। Belt চলার সাথে সাথে Flutter প্রতিটা sliver-কে জিজ্ঞেস করে, "আমরা কতটা scroll করেছি আর কতটা জায়গা বাকি আছে — এখন তুমি কতটুকু আঁকবে?" প্রতিটা sliver তার **geometry** দিয়ে উত্তর দেয়। এই আদান-প্রদানই **sliver layout protocol**।

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

**ধাপ ৩ — Sliver-এর layout সাধারণ widget-এর থেকে আলাদা।**
একটা সাধারণ (box) widget ভাবে width আর height নিয়ে। একটা sliver ভাবে *scroll extent* নিয়ে — scroll direction বরাবর সে কতটা জায়গা নেয় আর কতটা scroll হয়ে সরে গেছে। দুজনে আলাদা layout ভাষায় কথা বলে, তাই এদের ইচ্ছেমতো মেশানো যায় না (ধাপ ৪ দেখুন)।

**ধাপ ৪ — দুই জগতের নিয়ম।**
- একটা sliver-কে `Column` বা `Row`-এর ভেতরে রাখা **যাবে না**।
- একটা সাধারণ widget সরাসরি `slivers:` তালিকায় দেওয়া **যাবে না** — আগে `SliverToBoxAdapter` দিয়ে মুড়ে নিন।

```dart
CustomScrollView(
  slivers: [
    const SliverAppBar(expandedHeight: 200, pinned: true),
    SliverToBoxAdapter(child: Text('A normal widget, wrapped')),  // সেতু
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, i) => ListTile(title: Text('Row $i')),
        childCount: 50,
      ),
    ),
  ],
);
```

**Interviewer কেন জিজ্ঞেস করে:** Sliver-ই Flutter-এর আসল scrolling architecture। এগুলো জানা দেখায় আপনি সুবিধাজনক API-র চেয়ে বেশি বোঝেন। আর মসৃণ থাকে এমন জটিল screen বানাতে পারেন।

**সাধারণ ভুল:** Sliver-কে "আরেকটা widget" বলা। এটা আলাদা layout protocol ব্যবহার করে। `SliverToBoxAdapter` ছাড়া সরাসরি `slivers:`-এ সাধারণ widget বসানো একটা চেনা ভুল।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`ListView` কি একটা sliver?"* → ভেতরে এটা একটা `Viewport`-এর মধ্যে `SliverList` মুড়ে রাখে। সুবিধাজনক widget-গুলো sliver-চালিত।
- *"চাহিদামতো কেন?"* → একটা sliver শুধু এখন দেখা যায় এমন child-গুলো বানায় (সাথে ছোট একটা cache)। তাই 10,000 item-এর list-ও সস্তা থাকে।

**সম্পর্কিত:** [Q11 — sliver list-এর ধরন](#q11) · [Q12 — SliverAppBar](#q12) · [Q13 — CustomScrollView](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. `SliverList`, `SliverGrid` আর `SliverFixedExtentList`-এর মধ্যে পার্থক্য কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`SliverList` child-গুলোকে এক লাইনে সাজায়, যেখানে প্রতিটার height আলাদা হতে পারে। `SliverGrid` এগুলোকে 2D grid-এ সাজায়। `SliverFixedExtentList` হলো `SliverList`-এর মতোই, কিন্তু প্রতিটা child-এর height একই আর নির্দিষ্ট — আর height আগে থেকেই জানা বলে Flutter সহজ হিসাব করে সরাসরি দেখা যায় এমন item-এ চলে যেতে পারে, যেটা খুব লম্বা list-এর জন্য অনেক দ্রুত।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `SliverList`: আলাদা আলাদা height-এর item-এর এক লাইন।**
প্রতিটা child-এর height আলাদা হতে পারে। Flutter শুধু দেখা যায় এমন child-গুলো বানায় (সাথে ছোট একটা cache)। তাই লম্বা list-এও এটা কার্যকর — কিন্তু প্রতিটা কোথায় বসবে জানতে child-গুলো একের পর এক layout করতেই হয়।

```dart
SliverList(
  delegate: SliverChildBuilderDelegate(
    (context, index) => ListTile(
      title: Text('Item $index'),
      subtitle: index.isEven ? const Text('Has subtitle') : null, // height বদলায়
    ),
    childCount: 100,
  ),
);
```

**ধাপ ২ — `SliverGrid`: একটা 2D grid।**
Layout আপনি control করেন একটা grid delegate দিয়ে — নির্দিষ্ট সংখ্যক column, অথবা সবচেয়ে বেশি tile width।

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

**ধাপ ৩ — `SliverFixedExtentList`: একই height = দ্রুত।**
প্রতিটা child-কে একই main-axis size (`itemExtent`) মানতে বাধ্য করা হয়। Flutter প্রতিটা item-এর height আগে থেকেই জানে, তাই দ্রুত হিসাবে *ঠিক* কোন item-গুলো screen-এ আছে বের করে ফেলে — একটা একটা করে মাপার দরকার হয় না। 10,000 row-এর list-এ এটা সত্যিকারের performance লাভ।

```dart
SliverFixedExtentList(
  itemExtent: 56.0,  // প্রতিটা row ঠিক 56px উঁচু
  delegate: SliverChildBuilderDelegate(
    (context, index) => ListTile(title: Text('Row $index')),
    childCount: 10000,
  ),
);
```

**ধাপ ৪ — দ্রুত একটা তুলনা।**

| Sliver | Layout | Item-এর height | বিশাল list-এ গতি |
|---|---|---|---|
| `SliverList` | এক লাইন | প্রতিটা আলাদা হতে পারে | ভালো |
| `SliverGrid` | 2D grid | grid delegate অনুযায়ী | ভালো |
| `SliverFixedExtentList` | এক লাইন | সবগুলো একই | সবচেয়ে দ্রুত (সরাসরি দেখা যায় এমন অংশে লাফ) |

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা scrolling performance নিয়ে আপনার বোধ যাচাই করছেন। একরকম উচ্চতার 10,000 item-এর contacts screen-এ fixed-extent list বেছে নেওয়া একটা অর্থপূর্ণ, senior-level সিদ্ধান্ত।

**সাধারণ ভুল:** সব item একই height হলেও `SliverList` ব্যবহার করা। একরকম হলে `SliverFixedExtentList` বেছে নিন। আরেকটা জিনিস জানা ভালো: `SliverPrototypeExtentList` একটা নমুনা widget থেকে extent মেপে নেয়, hard-coded সংখ্যার বদলে — row height যখন text scale বা theme-এর উপর নির্ভর করে তখন কাজে লাগে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Fixed-extent কেন দ্রুত?"* → Flutter প্রতিটা child layout করে অবস্থান বের করার বদলে ভাগ করে দেখা যায় এমন পরিসর হিসাব করে।
- *"Height যদি font size-এর উপর নির্ভর করে?"* → `SliverPrototypeExtentList` ব্যবহার করুন আর তাকে একটা prototype item দিন।

**সম্পর্কিত:** [Q10 — sliver কী](#q10) · [Q13 — CustomScrollView](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. `SliverAppBar` কী কাজ করে? `pinned`, `floating`, আর `snap`-এর পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`SliverAppBar` হলো এমন একটা app bar যেটা `CustomScrollView`-এর ভেতরে থাকে আর scroll-এর সাথে সাড়া দেয়। `pinned` collapsed toolbar-টাকে উপরে আটকে রাখে। `floating` দিলে scroll up করার সাথে সাথেই bar ফিরে আসে, list-এর মাঝখানে থাকলেও। `snap` (এটার জন্য `floating` লাগে) bar-কে পুরো ভেতরে বা পুরো বাইরে animate করে — অর্ধেক খোলা অবস্থা থাকে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কী।**
একটা `SliverAppBar` expand হয়ে বড় image বা title দেখাতে পারে। তারপর scroll করলে সাধারণ toolbar-এ collapse হয়ে যায়। তিনটি boolean এর আচরণ ঠিক করে।

**ধাপ ২ — `pinned: true` — toolbar থেকে যায়।**
Scroll down করলে bar toolbar-এর height-এ collapse হয় আর উপরে **থেকে যায়**। এটা কখনোই পুরোপুরি হারায় না। এটাই ক্লাসিক collapsing header (Gmail-এর কথা ভাবুন)।

**ধাপ ৩ — `floating: true` — এটা আগেভাগেই ফিরে আসে।**
Floating দিলে আপনি একটু **উপরে** scroll করলেই bar ফিরে আসে — একেবারে উপরে ফিরে যাওয়া লাগে না। Feed আর news app-এ এটা খুব সাধারণ।

**ধাপ ৪ — `snap: true` — হয় পুরো, নয় কিছুই না (floating লাগে)।**
Snap অর্ধেক-দেখানো অবস্থাটা সরিয়ে দেয়। একটু উপরে scroll করলেই bar animation দিয়ে পুরো খুলে যায়; নিচে scroll করলে পুরো সরে যায়। এটা অবশ্যই `floating: true`-এর সাথে দিতে হবে।

```text
PINNED                 FLOATING                SNAP (+ floating)
Scroll down:           Scroll down:            Scroll down:
  [Toolbar stays]        [Fully gone]            [Fully gone]
Scroll up:             Scroll up a little:     Scroll up a little:
  [Toolbar stays]        [Immediately shows]     [Snaps fully open]
```

**ধাপ ৫ — উদাহরণ আর সাধারণ combination।**

```dart
CustomScrollView(
  slivers: [
    SliverAppBar(
      expandedHeight: 250,    // পুরো খোলা অবস্থায় height
      pinned: true,           // collapsed toolbar উপরে আটকে থাকে
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
// pinned: false, floating: true  → scroll up করলেই ফিরে আসে (news feed)
// floating: true, snap: true     → snappy, অর্ধেক-খোলা অবস্থা নেই
```

**Interviewer কেন জিজ্ঞেস করে:** ঠিক এই আচরণটাই designer-রা বারবার চান। তাঁরা দেখতে চান আপনি trial and error ছাড়াই সঠিক UX configure করতে পারেন কি না।

**সাধারণ ভুল:** `floating: true` ছাড়া `snap: true` দেওয়া — এতে assertion error হয়। আরেকটা ভুল: `expandedHeight` (খোলা অবস্থার height) আর `toolbarHeight` (collapsed height) গুলিয়ে ফেলা। আরও একটা: flexible-space background শুধু expanded অবস্থায় দেখা যায়; collapse হয়ে গেলে (`pinned` দিয়ে) শুধু toolbar আর title থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Collapse হওয়ার সময় title fade in করবেন কীভাবে?"* → `collapseMode` সহ `FlexibleSpaceBar` ব্যবহার করুন, অথবা scroll শুনে opacity বদলান।
- *"দুটো SliverAppBar একসাথে বসানো যায়?"* → হ্যাঁ — যেমন collapsing header-এর নিচে একটা pinned search bar।

**সম্পর্কিত:** [Q10 — sliver কী](#q10) · [Q13 — CustomScrollView](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. একের বেশি sliver widget একসাথে করতে `CustomScrollView` কীভাবে ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`CustomScrollView` হলো সেই container যেটা sliver-দের রাখে। এর `slivers:` তালিকা scroll axis বরাবর একটার পর একটা সাজানো হয়, আর সবাই একটাই scroll position ভাগ করে নেয়। ওই তালিকার সবকিছুকে sliver হতে হবে — যেকোনো সাধারণ widget-কে `SliverToBoxAdapter`-এ wrap করুন, আর বাকি জায়গা ভরতে `SliverFillRemaining` ব্যবহার করুন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটাই scroll view, অনেক section।**
`CustomScrollView` একটা `slivers:` তালিকা নেয়। প্রতিটা entry একটা scrollable section। সবাই একটাই scroll position ভাগ করে নেয় বলে পুরোটা একটা মসৃণ surface-এর মতো scroll করে।

**ধাপ ২ — মূল নিয়ম: সবকিছুকে sliver হতে হবে।**
- সাধারণ widget? `SliverToBoxAdapter`-এ wrap করুন।
- বাকি জায়গা ভরতে হবে (footer, empty state)? `SliverFillRemaining` ব্যবহার করুন।

**ধাপ ৩ — বাস্তব একটা shop screen।**

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

    // 2. Search bar — সাধারণ widget, তাই wrap করা হলো
    SliverToBoxAdapter(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: TextField(decoration: const InputDecoration(hintText: 'Search...')),
      ),
    ),

    // 3. Horizontal category chips — এটাও সাধারণ widget
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

    // 5. Footer — বাকি যতটুকু জায়গা আছে ভরে দেয়
    const SliverFillRemaining(
      hasScrollBody: false,
      child: Center(child: Text('End of products')),
    ),
  ],
);
```

**ধাপ ৪ — এটাই কেন সবচেয়ে কাজের sliver প্রশ্ন।**
বাস্তব screen-এ প্রায় সবসময় অনেক section মেশানো থাকে — header, search field, grid, list। এগুলোকে একটা production-quality scroll-এ জোড়া লাগানোর উপায়ই হলো `CustomScrollView`।

**Interviewer কেন জিজ্ঞেস করে:** এটাই প্রমাণ যে আপনি সত্যিই একটা জটিল scrollable screen বানাতে পারেন। শুধু "sliver আছে" মুখস্থ বলা নয়।

**সাধারণ ভুল:** `SliverToBoxAdapter` ছাড়া সরাসরি `slivers:`-এ সাধারণ widget বসিয়ে দেওয়া — এতে compile-time type error বা render crash হয়। আরেকটা ভুল: একটা `CustomScrollView`-এর ভেতরে আরেকটা রাখা, ভেতরেরটাতে `shrinkWrap` আর `NeverScrollableScrollPhysics` না দিয়ে — সাধারণত এটা ইশারা দেয় যে আপনার উচিত সবটা একটাই `CustomScrollView`-এ আরও sliver দিয়ে সমতল করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Pull-to-refresh কীভাবে করবেন?"* → `CustomScrollView`-কে `RefreshIndicator`-এ wrap করুন, অথবা প্রথম sliver হিসেবে `CupertinoSliverRefreshControl` দিন।
- *"`SliverToBoxAdapter` আর `SliverFillRemaining`-এর পার্থক্য?"* → Adapter একটা সাধারণ widget-কে তার স্বাভাবিক size-এ wrap করে; fill-remaining বাকি থাকা viewport-এর জায়গা ভরতে টেনে বড় হয়।

**সম্পর্কিত:** [Q10 — sliver কী](#q10) · [Q11 — sliver list-এর ধরন](#q11) · [Q12 — SliverAppBar](#q12)

[↑ উপরে ফিরুন](#toc)

---

# E. Custom painting

> যখন কোনো widget-ই আপনার দরকারি জিনিস আঁকতে পারে না — একটা chart, একটা gauge, একটা signature pad — তখন `CustomPainter` আপনাকে একটা raw canvas দেয়। এই ক্ষমতার সাথে একটা দায়িত্বও আসে: repaint control করুন, যাতে অকারণে প্রতি frame-এ আবার আঁকা না হয়।

---

## <a id="q14"></a>14. `CustomPainter` কী? `Canvas`, `Paint`, আর `Path` কীভাবে কাজ করে?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`CustomPainter` আমাকে একটা raw 2D drawing surface দেয় — `Canvas`। সেখানে আমি shape, line, arc, text আর path আঁকতে পারি। `Canvas` হলো *কোথায়* আঁকব, `Paint` বলে *কীভাবে* (color, stroke নাকি fill, width), আর `Path` line আর curve দিয়ে বানানো একটা custom *shape* বোঝায়। যখন কোনো widget-ই ওই visual বানাতে পারে না, তখন আমি এটা ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটি tool, সহজ কথায়।**
- **Canvas** = কাগজ। এতে `drawCircle`, `drawLine`, `drawRect`, `drawArc`, `drawPath`-এর মতো method আছে। এর origin `(0,0)` উপরে-বামে।
- **Paint** = তুলির setting: color, stroke width, fill নাকি outline, anti-aliasing, shader।
- **Path** = একটা custom shape, যেটা আপনি ধাপে ধাপে বানান (এখানে যান, ওখানে line টানুন, curve, close)।

```text
Canvas coordinate system:
(0,0) ----------> x
  |
  |   your drawing area (size.width x size.height)
  v
  y
```

**ধাপ ২ — একটা painter সাজান আর fill নাকি stroke বেছে নিন।**

```dart
class ChartPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    // Fill paint — ভরাট shape
    final fill = Paint()
      ..color = Colors.blue.withValues(alpha: 0.3)
      ..style = PaintingStyle.fill;

    // Stroke paint — শুধু outline
    final stroke = Paint()
      ..color = Colors.blue
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round;

    // মাঝখানে একটা filled circle:
    canvas.drawCircle(Offset(size.width / 2, size.height / 2), 50, fill);

    // ... path-এর জন্য Step 3, text-এর জন্য Step 4 দেখুন
  }

  @override
  bool shouldRepaint(covariant ChartPainter oldDelegate) => false;
}
```

**ধাপ ৩ — `Path` দিয়ে custom shape বানান।**
একটা `Path` কয়েকটা point জুড়ে যেকোনো shape বানায়। এই যে একটা triangle:

```dart
final path = Path()
  ..moveTo(size.width / 2, 20)                 // উপরের vertex
  ..lineTo(size.width - 20, size.height - 20)  // নিচে-ডানে
  ..lineTo(20, size.height - 20)               // নিচে-বামে
  ..close();                                   // শুরুর বিন্দুতে ফিরে যাও

canvas.drawPath(path, stroke);
```

**ধাপ ৪ — Text আঁকতে `TextPainter` লাগে।**
আপনি সরাসরি কোনো `drawText` call করতে পারবেন না; আগে একটা `TextPainter` layout করতে হয়, তারপর সেটা paint করতে হয়:

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

**ধাপ ৫ — `CustomPaint` দিয়ে দেখান।**

```dart
CustomPaint(
  size: const Size(300, 300),
  painter: ChartPainter(),
);
```

**Interviewer কেন জিজ্ঞেস করে:** Chart, signature pad, gauge, game rendering আর অস্বাভাবিক progress indicator — সবগুলোতেই এটা লাগে। তাঁরা নিশ্চিত হতে চান, widget শেষ হয়ে গেলে আপনি drawing layer-এ নামতে পারেন কি না।

**সাধারণ ভুল:** ভুলে যাওয়া যে `Paint`-এর default হলো `PaintingStyle.fill` — আপনি outline আশা করেছিলেন কিন্তু ভরাট দলা পেলেন, তাহলে `PaintingStyle.stroke` সেট করুন। আরেকটা ভুল: `TextPainter` ছাড়া text আঁকার চেষ্টা করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Gradient কীভাবে আঁকবেন?"* → `Paint`-এ একটা `shader` সেট করুন, যেমন `LinearGradient(...).createShader(rect)`।
- *"একটা shape-এ clip করবেন কীভাবে?"* → আঁকার আগে `canvas.clipPath(path)` দিন, অথবা `CustomClipper` ব্যবহার করুন।

**সম্পর্কিত:** [Q15 — painter বনাম widget](#q15) · [Q16 — shouldRepaint](#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. কখন `CustomPainter` ব্যবহার করবেন, আর কখন widget composition?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Default হিসেবে আমি widget compose করি। `CustomPainter`-এ যাই শুধু তখন, যখন widget দিয়ে shape-টা বানানো যায় না, বা widget দিয়ে আঁকলে খরচ অনেক বেশি হয়। Widget আপনাকে বিনা খরচে hit testing, accessibility আর gesture দেয়। Custom painter কাঁচা control দেয়, কিন্তু ওই সুবিধাগুলো ছেড়ে দিতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — যেখানে পারেন, widget-ই বেছে নিন।**
`Container`, `ClipRRect`, `Stack`, `DecoratedBox`, বা `Transform` দিয়ে কাজ হলে ওগুলোই ব্যবহার করুন। বাড়তি কোনো পরিশ্রম ছাড়াই accessibility, gesture handling আর সহজ maintenance পেয়ে যাবেন।

```dart
// Rounded gradient card — CustomPainter লাগে না:
Container(
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(16),
    gradient: const LinearGradient(colors: [Colors.purple, Colors.blue]),
    boxShadow: const [BoxShadow(color: Colors.black26, blurRadius: 10, offset: Offset(0, 4))],
  ),
  child: const Padding(padding: EdgeInsets.all(24), child: Text('Beautiful Card')),
);
```

**ধাপ ২ — যে shape widget বানাতে পারে না, তার জন্য `CustomPainter`।**
Line chart, waveform, radial gauge, signature — এগুলোর কোনো widget বিকল্প নেই। এগুলো এঁকেই বানাতে হয়।

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

**ধাপ ৩ — অনেক ছোট ছোট primitive থাকলে performance-এর জন্যও এটা ব্যবহার করুন।**
যদি শত শত ছোট widget লাগে (10,000 point-এর scatter plot, বা particle effect), তাহলে একটা canvas-এ সেগুলো এঁকে ফেলা হাজারটা widget বানানোর চেয়ে অনেক সস্তা।

**ধাপ ৪ — দ্রুত সিদ্ধান্তের গাইড।**

| পরিস্থিতি | যা বেছে নেবেন |
|---|---|
| সাধারণ shape (rounded box, gradient, shadow) | widget |
| ছোট ছোট অংশে gesture/accessibility লাগবে | widget |
| যে shape কোনো widget বানাতে পারে না (chart, gauge, waveform) | `CustomPainter` |
| শত বা হাজারখানেক ছোট visual element | `CustomPainter` (performance) |

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা আপনার architectural বুদ্ধি যাচাই করছেন। সব কিছুর জন্য `CustomPainter`-এ ঝাঁপিয়ে পড়া over-engineering (maintain করা কঠিন, built-in accessibility নেই)। আবার কখনোই ব্যবহার না করা মানে আপনি custom visual সামলাতে পারেন না। Senior-রা সঠিকটা বেছে নেন।

**সাধারণ ভুল:** gradient সহ একটা rounded rectangle হাতে এঁকে ফেলা (যেটা `Container` + `BoxDecoration` দিয়ে খুবই সহজ)। উল্টো ভুলটাও হয়: waveform না এঁকে `Container` স্তূপ করে নকল waveform বানানো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Custom-painted chart-এ accessibility কীভাবে দেবেন?"* → এটাকে একটা `Semantics` widget-এ মুড়ে দিন এবং label/value দিন, কারণ painter-এর নিজের কিছু নেই ([Q17](#q17) দেখুন)।
- *"Interactive chart কোথায় বসে?"* → সাধারণত visual-এর জন্য painter, আর tap ধরার জন্য উপরে একটা `GestureDetector`।

**সম্পর্কিত:** [Q14 — CustomPainter-এর basics](#q14) · [Q16 — shouldRepaint ও RepaintBoundary](#q16) · [Q17 — Semantics](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. `shouldRepaint` কী কাজ করে, আর `RepaintBoundary` কীভাবে সাহায্য করে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`shouldRepaint` Flutter-কে জানায় painter-টার সত্যিই আবার আঁকা দরকার কি না। আমি নতুন data-র সাথে পুরোনো painter-এর data মিলিয়ে দেখি। কিছু না বদলালে `false` ফেরত দিই, ফলে ভারী redraw বাদ যায়। `RepaintBoundary` হলো এর সঙ্গী কৌশল: এটা screen-এর একটা অংশকে আলাদা layer-এ আলাদা করে। ফলে এক জায়গার repaint চারপাশের সবকিছুকে repaint করতে বাধ্য করে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `shouldRepaint` হলো "আবার আঁকা কি দরকার?" check।**
Flutter এটাকে আগের painter instance দিয়ে call করে। Repaint করাতে চাইলে `true`, পুরোনো আঁকা রাখতে চাইলে `false` ফেরত দিন। `paint()` ভারী হতে পারে (জটিল path, text layout)। তাই কিছু না বদলালে এটা বাদ দেওয়া সত্যিকারের লাভ।

**ধাপ ২ — সঠিকভাবে কীভাবে লিখবেন।**
Painter যে data-র উপর নির্ভর করে সেটা field হিসেবে রাখুন, তারপর তুলনা করুন:

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
      old.progress != progress || old.color != color;  // শুধু data বদলালেই
}
```

**ধাপ ৩ — দুটো ভুল উত্তর।**
- সবসময় `true` ফেরত দেওয়া → প্রতি frame-এ repaint হয়, GPU নষ্ট হয়। ("নিরাপদে থাকি" ভেবে করা একটা সাধারণ ভুল।)
- সবসময় `false` ফেরত দেওয়া → data বদলালেও আঁকা কখনো update হয় না; জমে যাওয়া, বাসি visual পাবেন।

**ধাপ ৪ — `RepaintBoundary`: repaint-কে আটকে রাখুন।**
`RepaintBoundary`-কে ভাবুন একটা ব্যস্ত এলাকার চারপাশের দেয়াল হিসেবে। এটা না থাকলে, একটা widget repaint হলে (ধরুন একটা ঘুরন্ত animation) Flutter তার প্রতিবেশীদেরও repaint করতে পারে, কারণ তারা একই layer শেয়ার করে। ব্যস্ত অংশটাকে `RepaintBoundary`-তে মুড়ে দিন, তখন সেটা নিজের layer পায় — repaint দেয়ালের ভেতরেই থাকে।

```dart
// Animated chart অনবরত repaint হয়; একে আলাদা করুন যাতে screen-এর
// বাকি অংশ এর সাথে repaint না হয়:
RepaintBoundary(
  child: CustomPaint(painter: AnimatedChartPainter(...)),
);
```

এটা custom painting আর animation-এর সাথে স্বাভাবিকভাবেই জোড়া লাগে: `shouldRepaint` ঠিক করে repaint *করা হবে কি না*, আর `RepaintBoundary` সীমা বেঁধে দেয় repaint *কতদূর ছড়াবে*।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান আপনি Flutter-এর repaint optimization বোঝেন কি না। কয়েকটা `CustomPaint` widget আছে এমন screen-এ সব জায়গায় `true` ফেরত দেওয়া মানে প্রতি frame-এ GPU-র কাজ নষ্ট করা।

**সাধারণ ভুল:** "নিরাপদে থাকতে" সবসময় `true` ফেরত দেওয়া (optimization-টাই নষ্ট হয়), বা সবসময় `false` (বাসি visual)। আরেকটা: mutable list-কে `==` দিয়ে তুলনা করা (এটা reference check) — `package:flutter/foundation.dart`-এর `listEquals` ব্যবহার করুন, অথবা data-টা immutable রাখুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`RepaintBoundary` কি বেশি ব্যবহার করা যায়?"* → হ্যাঁ — প্রতিটা একটা করে layer আর একটু memory যোগ করে। সত্যিই ব্যস্ত এলাকার চারপাশে ব্যবহার করুন, সব জায়গায় নয়।
- *"এটা কাজে লাগছে তা কীভাবে নিশ্চিত হবেন?"* → DevTools-এর "Highlight Repaints" ব্যবহার করুন, দেখবেন প্রতি frame-এ কোন এলাকা repaint হচ্ছে।

**সম্পর্কিত:** [Q14 — CustomPainter](#q14) · [Q15 — painter বনাম widget](#q15) · [Q4 — AnimatedBuilder child](#q4)

[↑ উপরে ফিরুন](#toc)

---

# F. Accessibility

> Flutter দুটো tree বানায়: আপনি যেটা দেখেন সেই render tree, আর screen reader যেটা "দেখে" সেই semantics tree। Built-in widget-গুলো semantics tree নিজে থেকেই ভরে দেয়; কিন্তু আপনার custom widget, icon, আর gesture detector-এর প্রায়ই সাহায্য লাগে।

---

## <a id="q17"></a>17. `Semantics` widget কী, আর screen reader এটা কীভাবে ব্যবহার করে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`Semantics` widget UI-তে অর্থ যোগ করে, assistive tech-এর জন্য — যেমন Android-এর TalkBack আর iOS-এর VoiceOver। Flutter আলাদা একটা semantics tree রাখে, যেটা বলে প্রতিটা element আসলে কী। অনেক built-in widget এটা নিজে থেকেই ভরে দেয়। কিন্তু custom widget, icon, image, আর কাঁচা gesture detector-এর সাধারণত কোনো semantics থাকে না — আমি `Semantics` দিয়ে সেগুলো যোগ করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — পাশাপাশি দুটো tree।**
Flutter দুটো জিনিস রাখে: **render tree** (আপনি যা দেখেন) আর **semantics tree** (screen reader যা বলে)। `Text` তার content দেয়, `ElevatedButton` বলে "button," `Checkbox` বলে checked কি না — সবই নিজে থেকে।

```text
Widget tree              Semantics tree (what a screen reader says)
  Column                   "Shopping Cart screen"
   ├─ IconButton            ├─ "Back, button, double tap to activate"
   ├─ Image                 ├─ "Product photo: blue running shoes"
   ├─ GestureDetector       ├─ "Add to cart, button, double tap to activate"
   └─ Text                  └─ "Price: 99 dollars"
```

**ধাপ ২ — ফাঁকটা: custom আর কাঁচা widget-এর কোনো semantics নেই।**
খালি একটা `GestureDetector`, একটা `CustomPaint`, আর একটা সাজসজ্জার `Image` — এদের default অবস্থায় **কোনো** অর্থ থাকে না। Screen reader-এর কাছে এরা দেখা যায় না এমন বা নীরব। এদেরকে `Semantics`-এ মুড়ে দিয়ে এটা ঠিক করবেন।

**ধাপ ৩ — একটা label আর একটা role দিন।**

```dart
// Image-এর নিজের কোনো description থাকে না:
Semantics(
  label: 'Company logo',
  image: true,
  child: Image.asset('assets/logo.png'),
);

// Custom tappable icon — একে button হিসেবে জানান আর action দিন:
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

**ধাপ ৪ — value আর adjustable action দিন।**
Slider আর stepper-এর জন্য বর্তমান value দিন, আর কীভাবে বদলাতে হয় সেটাও দিন:

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

**Interviewer কেন জিজ্ঞেস করে:** অনেক বাজারে accessibility আইনি বাধ্যবাধকতা (ADA, EU-র নিয়ম), আর এটা করাই ঠিক কাজ। তাঁরা এমন engineer চান যাঁরা এমন app বানান যা সবাই ব্যবহার করতে পারে, শুধু পূর্ণ দৃষ্টি আর হাতের control থাকা user নয়।

**সাধারণ ভুল:** ধরে নেওয়া যে প্রতিটা widget নিজে থেকেই accessible। কাঁচা gesture detector, custom-painted widget, আর সাজসজ্জার image-এ default অবস্থায় শূন্য semantics থাকে। আরেকটা ভুল: বাড়তি লম্বা label, যেমন "This is a button you can tap to delete the item" — label ছোট রাখুন আর action আগে বলুন: "Delete item."

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`button: true` কী করে?"* → এটা screen reader-কে বলে element-টাকে button হিসেবে ঘোষণা করতে, যাতে user বোঝেন এটা tap করা যায়।
- *"Reader থেকে কোনো কিছু কীভাবে লুকাবেন?"* → `ExcludeSemantics` ব্যবহার করুন ([Q18](#q18) দেখুন)।

**সম্পর্কিত:** [Q18 — Exclude বনাম Merge](#q18) · [Q19 — accessibility testing](#q19) · [Q9 — gesture-এ semantics লাগে](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. `ExcludeSemantics` আর `MergeSemantics`-এর মধ্যে পার্থক্য কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`ExcludeSemantics` তার পুরো subtree-কে semantics tree থেকে একদম সরিয়ে দেয় — শুধু সাজসজ্জার element-এর জন্য ভালো। `MergeSemantics` তার নিচের সবকিছুকে এক announcement-এ জোড়া লাগায় — যখন কয়েকটা widget মিলে একটাই logical unit বানায় তখন ভালো, যেমন একটা star icon, একটা rating আর একটা review count একসাথে একটা item হিসেবে পড়া হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `ExcludeSemantics` = screen reader-কে এটা বাদ দিতে বলা।**
যে সাজসজ্জা কোনো অর্থ যোগ করে না, তার জন্য এটা ব্যবহার করুন — background wave, spacer image। Reader শব্দদূষণ না করে ওটা বাদ দিয়ে যায়।

```dart
ExcludeSemantics(
  child: Image.asset('assets/decorative_wave.png'), // শুধুই দেখার জিনিস
);
```

**ধাপ ২ — `MergeSemantics` = কয়েকটা widget-কে একটা হিসেবে পড়া।**
Default অবস্থায় icon + number + text-এর একটা row তিনটা আলাদা item হিসেবে announce হয়। ফলে user-কে তিনবার swipe করতে হয়। `MergeSemantics` এগুলোকে একটা node-এ ভাঁজ করে, এক swipe-এ পড়া হয়।

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

**ধাপ ৩ — দুটো একসাথে ব্যবহার করুন।**
একটা সাধারণ pattern: অংশগুলোকে এক unit-এ merge করা *এবং* তাকে একটা পরিষ্কার label দেওয়া, আর এখন দরকার নেই এমন হয়ে যাওয়া children-কে বাদ দেওয়া।

```dart
Semantics(
  label: 'Call us',
  button: true,
  child: Row(
    children: const [
      ExcludeSemantics(child: Icon(Icons.phone)),   // এখন এটা সাজসজ্জা
      ExcludeSemantics(child: Text('Call us')),      // label-ই তো বলে দিচ্ছে
    ],
  ),
);
```

**ধাপ ৪ — মনে রাখার সহজ মডেল।**
- অনেক বেশি আলাদা announcement হচ্ছে? → `MergeSemantics`।
- মানে নেই এমন সাজসজ্জা reader-কে ভরিয়ে ফেলছে? → `ExcludeSemantics`।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান আপনি screen-reader-এর *অভিজ্ঞতা* নিয়ে ভাবেন কি না, শুধু semantics আছে কি না তা নয়। যে card ৫০টা আলাদা announcement ছোড়ে, সেটা একদম semantics-হীন card-এর মতোই অব্যবহারযোগ্য।

**সাধারণ ভুল:** যে control-এ user-কে সত্যিই পৌঁছাতে হবে (যেমন close button) তার উপর `ExcludeSemantics` বসানো। শুধু সত্যিকারের সাজসজ্জা বাদ দিন। আরেকটা ভুল: custom list item merge না করা, ফলে user-কে একটা item-এর প্রতিটা child ধরে swipe করতে হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা merged group-এ যদি দুটো action থাকে?"* → তখন merge করবেন না; reader-এর প্রতিটা action আলাদা করে দরকার। শুধু একক logical unit merge করুন।
- *"`MergeSemantics` কি `Semantics` label-এর মতোই?"* → না। Merge আগে থেকে থাকা children-কে একসাথে ভাঁজ করে; `Semantics` label একটা description বসায় বা যোগ করে।

**সম্পর্কিত:** [Q17 — Semantics](#q17) · [Q19 — accessibility testing](#q19)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q19"></a>19. Flutter-এ accessibility কীভাবে test করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি কয়েকটা layer ব্যবহার করি: tree দেখার জন্য Semantics Debugger overlay, semantic label আর action assert করার widget test, tap-target size আর contrast-এর জন্য built-in guideline matcher, আর — সবচেয়ে গুরুত্বপূর্ণ — আসল TalkBack ও VoiceOver দিয়ে manual testing। Automated check label আর size ধরে; কিন্তু অভিজ্ঞতাটা অর্থবহ কি না, সেটা শুধু manual testing-ই নিশ্চিত করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Tree দেখুন: Semantics Debugger।**
একটা visual overlay চালু করুন যেটা দেখায় screen reader কী দেখত:

```dart
MaterialApp(
  showSemanticsDebugger: true,  // semantics tree-র visual overlay
  home: const MyHomePage(),
);
```

**ধাপ ২ — Widget test-এ semantics assert করুন।**
Label আর action আছে কি না verify করুন:

```dart
testWidgets('delete button is accessible', (tester) async {
  await tester.pumpWidget(const MyApp());

  expect(find.bySemanticsLabel('Delete item'), findsOneWidget);

  final node = tester.getSemantics(find.bySemanticsLabel('Delete item'));
  expect(node.hasAction(SemanticsAction.tap), isTrue);
});
```

**ধাপ ৩ — Built-in guideline matcher ব্যবহার করুন।**
Flutter-এর সাথেই matcher আসে, যেগুলো সবচেয়ে কম tap-target size, text contrast আর label আছে কি না check করে:

```dart
testWidgets('meets accessibility guidelines', (tester) async {
  await tester.pumpWidget(const MyApp());

  await expectLater(tester, meetsGuideline(androidTapTargetGuideline)); // 48x48
  await expectLater(tester, meetsGuideline(iOSTapTargetGuideline));     // 44x44
  await expectLater(tester, meetsGuideline(textContrastGuideline));     // contrast
  await expectLater(tester, meetsGuideline(labeledTapTargetGuideline)); // label আছে
});
```

**ধাপ ৪ — আসল device-এ manual testing (যে layer-টা বদলানো যায় না)।**
TalkBack (Android) আর VoiceOver (iOS) চালু করুন, তারপর সত্যিই app-টা ব্যবহার করুন:

- প্রতিটা screen ধরে swipe করুন আর নিশ্চিত করুন প্রতিটা interactive element announce হচ্ছে।
- Reading order যুক্তিসঙ্গত কি না check করুন (উপর থেকে নিচে, বাঁ থেকে ডানে)।
- বড় font scale দিয়ে আর screen magnification দিয়ে test করুন।
- Dialog, snackbar আর route change ঠিকমতো announce হচ্ছে কি না নিশ্চিত করুন।

**ধাপ ৫ — DevTools inspector।**
DevTools-এর Flutter Inspector widget tree-র পাশে semantics tree দেখায়। অনুপস্থিত বা ভুল node খুঁজে বের করতে এটা কাজে লাগে।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা একটা বাস্তব উপায় চান, তত্ত্ব নয়। "আমরা `Semantics` widget যোগ করি" বলা, অথচ সেগুলো কীভাবে verify করতে হয় না জানা — এটা অসম্পূর্ণ চর্চা দেখায়।

**সাধারণ ভুল:** শুধু automated test-এর উপর নির্ভর করা। ওগুলো size আর label check করে। কিন্তু reading order যুক্তিসঙ্গত কি না, announcement সহায়ক কি না, বা flow ব্যবহার করা যায় এমন কি না — ওগুলো বলতে পারে না। আসল screen reader দিয়ে manual testing অবশ্যই লাগে এমন, এটা বাদ দেওয়া যায় না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ভালো সবচেয়ে কম tap target কত?"* → Android-এ ~48x48 dp, iOS-এ ~44x44 pt; guideline matcher এগুলো জোর করে মানায়।
- *"সময়ের সাথে হওয়া announcement কীভাবে test করবেন?"* → Screen reader দিয়ে হাতে-কলমে, সাথে widget test যেখানে pump করে state change-এর পরে semantics check করা হয়।

**সম্পর্কিত:** [Q17 — Semantics](#q17) · [Q18 — Exclude বনাম Merge](#q18)

[↑ উপরে ফিরুন](#toc)

---

# G. Localization

---

## <a id="q20"></a>20. ARB file, `flutter_localizations` আর `intl` দিয়ে multi-language support (l10n) কীভাবে implement করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-09-advanced-flutter.md#q20)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"তিনটা অংশ একসাথে কাজ করে। `flutter_localizations` built-in material widget (date picker, dialog) অনুবাদ করে। ARB file-এ আমার নিজের string থাকে, প্রতি ভাষার জন্য একটা file। `gen-l10n` tool ওই ARB file পড়ে একটা typed `AppLocalizations` class generate করে। ফলে key না থাকলে সেটা compile error হয়, runtime crash নয়। আমি এটা `MaterialApp`-এ যুক্ত করি আর `AppLocalizations.of(context)` দিয়ে string পড়ি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটা অংশ।**
- **`flutter_localizations`** — material/cupertino widget-এর জন্য অনেক ভাষায় built-in অনুবাদ। এটা ছাড়া date picker-ও ইংরেজিতেই থেকে যায়।
- **ARB file** (Application Resource Bundle) — JSON-এর মতো file, যেখানে আপনার string থাকে: `app_en.arb`, `app_es.arb`, `app_bn.arb` (বাংলা, BD app-এর জন্য কাজের)।
- **`intl` + `gen-l10n`** — code generation, যা ARB file-গুলোকে একটা typed Dart class-এ বদলে দেয়, প্রতিটা string-এর জন্য একটা getter সহ।

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

**ধাপ ২ — Dependency যোগ করুন আর generation চালু করুন (`pubspec.yaml`)।**

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  intl: any

flutter:
  generate: true   # gen-l10n code generation চালু করে
```

**ধাপ ৩ — Project root-এ `l10n.yaml` configure করুন।**

```yaml
arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
```

**ধাপ ৪ — `lib/l10n/`-এ ARB file লিখুন।**

`app_en.arb` (template — placeholder আর plural বর্ণনা করে):

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

`app_bn.arb` (শুধু অনুবাদ — metadata আবার লেখার দরকার নেই):

```json
{
  "@@locale": "bn",
  "welcomeMessage": "আমাদের অ্যাপে স্বাগতম!",
  "greeting": "হ্যালো, {name}!",
  "itemCount": "{count, plural, =0{কোনো আইটেম নেই} =1{১টি আইটেম} other{{count}টি আইটেম}}"
}
```

**ধাপ ৫ — Code generate করুন।**

```bash
flutter gen-l10n
```

**ধাপ ৬ — `MaterialApp`-এ যুক্ত করুন।**

```dart
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

MaterialApp(
  supportedLocales: AppLocalizations.supportedLocales,
  localizationsDelegates: AppLocalizations.localizationsDelegates,
  home: const HomePage(),
);
```

**ধাপ ৭ — Widget-এ string ব্যবহার করুন।**

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

**Interviewer কেন জিজ্ঞেস করে:** Global বা BD-মুখী app-এর জন্য localization optional নয়। তাঁরা পুরো pipeline জানতে চান — ARB format, code generation, placeholder, plural rule, delegate — শুধু "কিছু JSON file ব্যবহার করি" নয়।

**সাধারণ ভুল:** সব জায়গায় `Text('Welcome')` hardcode করা, আর পরে l10n জুড়ে দেওয়ার চেষ্টা করা — ভীষণ কষ্টকর। প্রথম দিন থেকেই localized শুরু করুন। আরেকটা ভুল: plural rule বাদ দেওয়া (কিছু ভাষায় একের বেশি plural form থাকে); ARB-এর ICU `plural` syntax এগুলো সামলায়, কিন্তু case-গুলো আপনাকেই লিখতে হয়। আরও একটা: `pubspec.yaml`-এ `generate: true` দিতে ভুলে যাওয়া, ফলে `gen-l10n` যে file বানায় সেগুলো কখনো build-এ পৌঁছায় না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"User-কে app-এর ভেতরেই ভাষা বদলাতে দেবেন কীভাবে?"* → বেছে নেওয়া `Locale`-টা state-এ রাখুন আর `MaterialApp`-এর `locale:`-এ পাঠান; typed class string-গুলো update করে দেয়।
- *"প্রতিটা locale অনুযায়ী date আর number কীভাবে format হয়?"* → `intl`-এর `DateFormat` আর `NumberFormat` ব্যবহার করুন, এগুলো active locale মেনে চলে।

**সম্পর্কিত:** [Q17 — Semantics (label-ও অনুবাদ করতে হয়)](#q17)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিউ)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার তালিকাগুলো, তারপর এক-লাইনের মনে করিয়ে দেওয়া পয়েন্ট।

## দ্রুত তুলনার তালিকা

**Implicit বনাম explicit animation**

| | Implicit | Explicit |
|---|---|---|
| আপনি সামলান | কিছুই না (শুধু একটা value বদলান) | `AnimationController` |
| উদাহরণ | `AnimatedContainer`, `AnimatedOpacity` | `AnimationController` + `Tween` |
| Loop / sequence করা যায়? | না | হ্যাঁ |
| কোথায় সবচেয়ে ভালো | toggle, layout বদল | spinner, staggered intro, control |

**`AnimatedBuilder` বনাম `AnimatedWidget`**

| | `AnimatedBuilder` | `AnimatedWidget` |
|---|---|---|
| ধরন | inline builder | আপনার লেখা একটা subclass |
| কোথায় সবচেয়ে ভালো | এককালীন কাজ, আগে থেকেই থাকা widget | আবার ব্যবহার করা যায় এমন animated component |
| Child-এর rebuild এড়ানো | সেটা `child` হিসেবে pass করুন | ভেতরে একটা static child মুড়ে দিন |

**`GestureDetector` বনাম `Listener`**

| `Listener` | `GestureDetector` |
|---|---|
| raw pointer event (down/move/up) | চেনা gesture (tap, drag, scale) |
| কোনো ব্যাখ্যা করে না | gesture arena দিয়ে একজন winner বেছে নেয় |
| custom, খুব কম লাগে | প্রতিদিনের পছন্দ |

**Sliver list-এর ধরন**

| `SliverList` | `SliverGrid` | `SliverFixedExtentList` |
|---|---|---|
| আলাদা আলাদা উচ্চতা | 2D grid | একটাই fixed উচ্চতা |
| ভালো | ভালো | বিশাল list-এ সবচেয়ে দ্রুত |

**`SliverAppBar`-এর flag**

| `pinned` | `floating` | `snap` (`floating` লাগে) |
|---|---|---|
| toolbar উপরে থেকে যায় | উপরে scroll করলে ফিরে আসে | পুরোপুরি ভেতরে/বাইরে snap করে |

**`CustomPainter` বনাম widget**

| Widget | `CustomPainter` |
|---|---|
| চেনা shape, a11y/gesture ফ্রি পাওয়া যায় | যে shape কোনো widget বানাতে পারে না |
| maintain করা সহজ | অনেক primitive = perf-এ লাভ |

## এক লাইনের মনে করিয়ে দেওয়া

- **`AnimationController`** প্রতি frame-এ 0→1 চালায়; `vsync` screen-এর বাইরে গেলে থামায়; সবসময় `dispose()` করুন। ([Q1](#q1))
- **`Tween`** 0→1-কে একটা বাস্তব range-এ বদলায়, আর controller ছাড়া কিছুই করে না (`tween.animate(controller)`)। ([Q2](#q2))
- **Curve** সোজা progress-কে বাঁকিয়ে স্বাভাবিক গতি দেয়; `In`/`Out` = কোন মাথায় effect পড়বে। ([Q3](#q3))
- **`AnimatedBuilder`** প্রতি tick-এ rebuild করে — static অংশটা `child` হিসেবে pass করুন, তাহলে সেটা rebuild হবে না। ([Q4](#q4))
- **Implicit** = একটা value বদলানো (সহজ); **explicit** = একটা controller ধরে রাখা (loop, sequence, control)। ([Q5](#q5))
- **Staggered** = একটা controller + প্রতি অংশের জন্য একটা `Interval`, অনেকগুলো controller নয়। ([Q6](#q6))
- **`Hero`** একটা widget-কে screen থেকে screen-এ উড়িয়ে নেয়; দুই পাশে **একই, unique `tag`** লাগে। ([Q7](#q7))
- **Lottie** = After Effects JSON, শুধু playback; **Rive** = `.riv` binary, ভেতরে interactive state machine। ([Q8](#q8))
- **`Listener`** = raw pointer; **`GestureDetector`** = চেনা gesture; **arena** একজন winner বেছে নেয়। ([Q9](#q9))
- **Sliver** দরকার মতো paint করে; সাধারণ widget-কে `SliverToBoxAdapter`-এ মুড়ুন, sliver-কে `Column`-এ রাখা যায় না। ([Q10](#q10))
- **`SliverFixedExtentList`** সমান উচ্চতার বিশাল list-এ `SliverList`-এর চেয়ে ভালো (সরাসরি visible অংশে লাফ দেয়)। ([Q11](#q11))
- **`SliverAppBar`**: `pinned` থেকে যায়, `floating` উপরে scroll করলে ফেরে, `snap`-এর জন্য `floating` লাগে। ([Q12](#q12))
- **`CustomScrollView`** একটাই shared scroll-এ sliver রাখে; সবকিছুকে sliver হতে হবে। ([Q13](#q13))
- **`CustomPainter`**: `Canvas` = কোথায়, `Paint` = কীভাবে (default হলো fill!), `Path` = custom shape। ([Q14](#q14))
- **Default হিসেবে widget নিন**; যে shape widget বানাতে পারে না বা অনেক primitive লাগে, সেখানে `CustomPainter`। ([Q15](#q15))
- **`shouldRepaint`** data না বদলালে `false` ফেরত দেয়; **`RepaintBoundary`** ব্যস্ত একটা এলাকা আলাদা করে দেয়। ([Q16](#q16))
- **`Semantics`** screen-reader tree ভরে দেয়; raw gesture/paint widget-এ default-এ কিছুই থাকে না। ([Q17](#q17))
- **`ExcludeSemantics`** সাজসজ্জা লুকায়; **`MergeSemantics`** কয়েকটা widget-কে একটা item হিসেবে পড়ায়। ([Q18](#q18))
- **a11y test করুন** debugger, guideline matcher, আর (সবচেয়ে জরুরি) আসল TalkBack/VoiceOver দিয়ে। ([Q19](#q19))
- **l10n**: ARB file + `gen-l10n` → typed `AppLocalizations`; key না থাকলে compile time-এ fail করে। ([Q20](#q20))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: interviewer কীভাবে আরও গভীরে যায়

Interviewer সাধারণত একটা প্রশ্নে থামেন না। আপনার গভীরতা মাপতে তাঁরা খুঁড়তে থাকেন। এই চেইনটা মুখে বলে অনুশীলন করুন — শান্তভাবে, ধাপে ধাপে:

1. *"একটা box বড় হওয়ার animation কীভাবে করবেন?"* → implicit `AnimatedContainer`, শুধু size বদলান।
2. *"এবার এটাকে সারাক্ষণ pulse করান।"* → এতে loop লাগবে, তাই explicit-এ যান: `AnimationController()..repeat()`।
3. *"প্রতি frame-এ পুরো widget rebuild হওয়া কীভাবে এড়াবেন?"* → `AnimatedBuilder`, আর static অংশটা `child` হিসেবে pass করুন।
4. *"Pulse animation-এ বাকি screen repaint হচ্ছে — ঠিক করুন।"* → animated অংশটা `RepaintBoundary`-তে মুড়ে তার layer আলাদা করুন।
5. *"Repaint সত্যিই আটকে আছে, সেটা কীভাবে প্রমাণ করবেন?"* → DevTools-এর "Highlight Repaints"-এ শুধু ওই এলাকাটাই ঝলকাবে।

এভাবে শান্তভাবে ধাপে ধাপে এগোতে পারা — আন্দাজ না করে — এটাই আপনাকে **senior** শোনায়, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

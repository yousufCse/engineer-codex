# Section 3 — State Management

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-03-state-management.md](../software-engineer-flutter/section-03-state-management.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code দিয়ে ধাপে ধাপে পুরো ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর তার কঠিনতা (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তরটা** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন — "আরও গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলাটাই একটা senior skill — remote আর BD দুই ধরনের কোম্পানিতেই এটা একইভাবে কাজ করে।

---


## <a id="toc"></a>সূচিপত্র

**A. যে basic দিয়ে প্রতিটা interview শুরু হয়**
1. ["State" কী? Ephemeral vs app state](#q1) · *Very common*
2. [`setState` কীভাবে কাজ করে (আর কখন ব্যবহার করবেন না)](#q2) · *Very common*
3. [`StatefulWidget` lifecycle (state কোথায় থাকে)](#q3) · *Common*
4. [State উপরে তোলা আর callback নিচে পাঠানো](#q4) · *Common*

**B. ভিত্তি: InheritedWidget আর Provider**
5. [`InheritedWidget` আর `updateShouldNotify`](#q5) · *Common*
6. [Provider — ChangeNotifier, Consumer, Selector, ProxyProvider](#q6) · *Very common*
7. [`context.watch` vs `read` vs `select`](#q7) · *Very common*

**C. BLoC পরিবার**
8. [BLoC pattern — event, state, stream](#q8) · *Very common*
9. [Cubit vs BLoC — কোনটা কখন ব্যবহার করবেন](#q9) · *Very common*
10. [`BlocBuilder` vs `BlocListener` vs `BlocConsumer`](#q10) · *Very common*
11. [`buildWhen` আর `listenWhen` (performance)](#q11) · *Common*
12. [`emit()` vs `setState()` আর "emit after close"](#q12) · *Common*

**D. Riverpod আর GetX**
13. [Riverpod — কেন এটা Provider-এর চেয়ে ভালো, provider-এর ধরন, ref method](#q13) · *Very common*
14. [GetX — controller, `Obx`, `GetBuilder`, trade-off](#q14) · *Common*

**E. Architecture আর senior সিদ্ধান্ত**
15. [Sealed union দিয়ে state model করা (loading / success / error)](#q15) · *Very common*
16. [সম্পর্ক নেই এমন দুটো screen-এর মধ্যে state শেয়ার করা](#q16) · *Common*
17. [State management solution কীভাবে বাছবেন](#q17) · *Very common*
18. [BLoC / Cubit logic-এর testing](#q18) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিউ)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

১৮টা প্রশ্ন একসাথে পড়ার দরকার নেই। এই পর্যায়গুলো একটার পর একটা শেষ করুন — প্রতিটা আগেরটার উপর দাঁড়ানো। একটা পর্যায় তখনই শেষ ধরবেন যখন না দেখে **সংক্ষিপ্ত উত্তরটা** দিতে পারবেন।

**পর্যায় ১ — মূল ভিত্তি (এখান থেকে শুরু করুন)।** প্রায় প্রতিটা interview এখান থেকেই শুরু হয়।
→ [Q1 State কী](#q1) · [Q2 setState](#q2) · [Q3 Lifecycle](#q3) · [Q4 State উপরে তোলা](#q4)

**পর্যায় ২ — ভিত্তি (ভেতরে সবকিছু কীভাবে কাজ করে)।**
→ [Q5 InheritedWidget](#q5) · [Q6 Provider](#q6) · [Q7 watch/read/select](#q7)

**পর্যায় ৩ — BLoC পরিবার (BD চাকরিতে সবচেয়ে বেশি ব্যবহার করা production pattern)।**
→ [Q8 BLoC pattern](#q8) · [Q9 Cubit vs BLoC](#q9) · [Q10 Builder/Listener/Consumer](#q10) · [Q12 emit vs setState](#q12)

**পর্যায় ৪ — আধুনিক tool আর পরিষ্কার state।**
→ [Q13 Riverpod](#q13) · [Q15 Sealed union state](#q15) · [Q11 buildWhen/listenWhen](#q11) · [Q14 GetX](#q14)

**পর্যায় ৫ — Senior signal (architecture আর testing, সবার শেষে)।**
→ [Q16 Screen-এর মধ্যে state শেয়ার](#q16) · [Q17 Solution বাছাই](#q17) · [Q18 BLoC/Cubit testing](#q18)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই আটটা রিভিউ করুন:
[Q1](#q1) · [Q2](#q2) · [Q6](#q6) · [Q7](#q7) · [Q8](#q8) · [Q9](#q9) · [Q15](#q15) · [Q17](#q17), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. যে basic দিয়ে প্রতিটা interview শুরু হয়

---

## <a id="q1"></a>1. Flutter-এ "state" কী? Ephemeral আর app state-এর পার্থক্য কী?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"State হলো এমন যেকোনো data যা বদলাতে পারে আর screen যেটা দেখায়। Flutter এটাকে দুই ভাগে ভাগ করে: ephemeral state, যেটা নিয়ে শুধু একটা widget-এর মাথাব্যথা — যেমন কোন tab খোলা আছে — আর app state, যেটা অনেক screen শেয়ার করে — যেমন logged-in user বা shopping cart। সহজ পরীক্ষা হলো: 'এই data আর কার দরকার?' যদি শুধু এই widget-এর হয়, তাহলে ephemeral; যদি অন্য screen-এরও দরকার হয়, তাহলে app state।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — State মানে শুধু "যে data বদলাতে পারে।"**
একটা widget কিছু data থেকে নিজেকে আঁকে। সেই data বদলালে widget আবার আঁকা হয়। ওই বদলে যাওয়া data-ই হলো state। একটা text label, একটা checkbox-এর মান, product-এর একটা তালিকা — এগুলো সবই state।

**ধাপ ২ — Ephemeral state = শুধু একটা widget-এর নিজের।**
"Ephemeral" মানে স্বল্পস্থায়ী আর ব্যক্তিগত। এটাকে ভাবুন নিজের টেবিলে লেখা নোটের মতো — আর কারও ওগুলো লাগে না। যেমন: `BottomNavigationBar`-এ খোলা tab, `PageView`-এর বর্তমান page, একটা dropdown খোলা আছে কি না।

```dart
// FAQ খোলা আছে কি না, সেটা নিয়ে শুধু এই widget-এর মাথাব্যথা।
class _FaqTileState extends State<FaqTile> {
  bool _isExpanded = false; // ephemeral state, এখানেই রাখা

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

**ধাপ ৩ — App state = পুরো app জুড়ে শেয়ার করা।**
এটা এমন data যা অনেক screen পড়ে, বা screen বদলালেও যেটা টিকে থাকতে হয়। এটাকে ভাবুন শেয়ার করা office-এর noticeboard-এর মতো — সবাই একই board থেকে পড়ে। যেমন: logged-in user, shopping cart, theme preference, না পড়া message-এর সংখ্যা।

```dart
// অনেক screen-এর cart দরকার, তাই এটা ওদের সবার উপরে থাকতে হবে
// (Provider, Riverpod, বা BLoC দিয়ে manage করা) — একটা widget-এর ভেতরে নয়।
```

**ধাপ ৪ — সীমানাটা সবসময় স্পষ্ট নয়।**
একই data-র শ্রেণি বদলে যেতে পারে। একটা "selected tab" শুরুতে ephemeral, কিন্তু app আবার খুললে deep link-কে যদি ওই tab ফিরিয়ে আনতে হয়, তাহলে এটা app state হয়ে যায়। তাই একটা নির্দিষ্ট তালিকা মুখস্থ করবেন না — সবসময় আসল প্রশ্নটা জিজ্ঞেস করুন।

**ধাপ ৫ — যে প্রশ্নটা সবসময় করতে হবে।**
"এই data আর কার দরকার?" উত্তর যদি হয় "শুধু এই widget-এর," তাহলে `setState` দিয়ে ephemeral রাখুন। উত্তর যদি হয় "অন্য screen-এরও, বা navigation-এর পরেও টিকতে হবে," তাহলে একটা ঠিকঠাক state manager দিয়ে এটাকে app state-এ তুলে দিন।

**Interviewer কেন জিজ্ঞেস করে:** State শ্রেণিভাগ করতে না পারলে আপনি হয় একটা সহজ toggle-এর জন্য BLoC দিয়ে over-engineer করবেন, নয়তো শেয়ার করা login state-এর জন্য `setState` দিয়ে under-engineer করবেন। তাঁরা দেখতে চান আপনি সঠিক মাপের tool বাছেন কি না।

**সাধারণ ভুল:** "সব কিছুর জন্য Provider ব্যবহার করুন" বা "`setState` খারাপ" — এমন বলা। দুটোই ভুল। Ephemeral state-এর জন্য `setState` একদম সঠিক; ভুলটা শুধু তখনই, যখন শেয়ার করতে হবে এমন data-র জন্য এটা ব্যবহার করা হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এমন একটা উদাহরণ দিন যেটা দুটোই হতে পারে।"* → একটা selected tab: সাধারণভাবে ephemeral, কিন্তু deep link-কে সেটা ফিরিয়ে আনতে হলে app state।
- *"App state আসলে কোথায় থাকে?"* → যেসব screen-এর দরকার, তাদের সবার উপরে, বা widget tree-র বাইরে (Riverpod) — যাতে প্রতিটা screen একই copy পড়ে।

**সম্পর্কিত:** [Q2 — setState কীভাবে কাজ করে](#q2) · [Q16 — screen-এর মধ্যে state শেয়ার](#q16) · [Q17 — solution বাছাই](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. `setState` ভেতরে কীভাবে কাজ করে? কখন এটা ব্যবহার করবেন না?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`setState` দুটো কাজ করে: প্রথমে আমার ছোট function-টা চালিয়ে data বদলায়, তারপর এই widget-কে 'dirty' চিহ্ন দেয় যাতে Flutter পরের frame-এ এটাকে rebuild করে। যে state একটা widget-এর ভেতরেই থাকে, তার জন্য এটাই সঠিক tool। আমি এটা এড়িয়ে চলি যখন state অনেক screen-এ শেয়ার করতে হয়, যখন ছোট একটা পরিবর্তনের জন্য বিশাল subtree rebuild হবে, বা যখন `await`-এর পরে state set করছি আর widget হয়তো ইতিমধ্যে চলে গেছে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "হাত তোলার" ধারণা।**
`setState`-কে ভাবুন এক ছাত্রের হাত তোলার মতো, যে বলছে "আমাকে আবার আঁকতে হবে।" শিক্ষক (Flutter) সাথে সাথে আঁকেন না — তিনি হাতটা খেয়াল করেন, চলতি মুহূর্তটা শেষ করেন, তারপর পরের frame-এ যারা যারা হাত তুলেছিল সবাইকে আবার আঁকেন। তাই `setState` একটা rebuild-এর সময় ঠিক করে দেয়; সাথে সাথে আঁকে না।

**ধাপ ২ — ভেতরে ঠিক কোনটার পর কোনটা হয়।**
আপনি যখন `setState(fn)` call করেন:

1. আপনার function `fn` **সাথে সাথে** চলে (synchronously) — এখানেই আপনি variable বদলান।
2. Flutter `markNeedsBuild()` call করে এই widget-এর element-কে **dirty** চিহ্ন দেয়।
3. Framework একটা নতুন frame-এর সময় ঠিক করে (যদি আগে থেকে ঠিক করা না থাকে)।
4. পরের frame-এ এই widget আর তার subtree-র জন্য `build()` আবার চলে।
5. Flutter নতুন widget tree-র সাথে পুরোনোটার তুলনা করে, আর screen-এ শুধু যেটুকু সত্যিই বদলেছে সেটুকু update করে।

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

**ধাপ ৩ — একটা বাস্তব counter।**

```dart
class _CounterPageState extends State<CounterPage> {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++; // ধাপ ১: এখনই চলে; _count ইতিমধ্যে update হয়ে গেছে
    });
    // ধাপ ২–৫ পরের frame-এ নিজে থেকেই ঘটে
  }

  @override
  Widget build(BuildContext context) {
    // প্রতিটা setState call-এ এই পুরো method আবার চলে
    return Column(children: [
      Text('$_count'),
      ElevatedButton(onPressed: _increment, child: const Text('+')),
      // এখানে 200টা ভারী widget থাকলে সেগুলোও সব rebuild হতো
    ]);
  }
}
```

**ধাপ ৪ — কখন `setState` ব্যবহার করবেন না।**
- **শেয়ার করা state:** একই data যদি কোনো sibling-এর, দূরের কোনো ancestor-এর, বা অন্য কোনো screen-এর দরকার হয়, তাহলে `setState` আপনাকে অস্বস্তিকরভাবে state উপরে তুলতে আর অনেক স্তর নিচে callback পাঠাতে বাধ্য করে।
- **বড় subtree, ছোট পরিবর্তন:** `setState` যদি গভীর tree-র উপরে বসে থাকে কিন্তু বদলেছে শুধু একটা leaf, তাহলে অকারণে শত শত widget rebuild হয়। State-কে নিচে নামান, বা একটা scoped tool ব্যবহার করুন।
- **Widget চলে যাওয়ার পরে async:** আপনি যদি কিছু `await` করেন, তারপর user screen ছেড়ে যাওয়ার পরে `setState` করেন, তাহলে `setState() called after dispose()` পাবেন। একটা `mounted` check দিয়ে এটা সামলান।
- **UI-তে business logic:** `setState` আপনাকে লোভ দেখায় login বা API logic সরাসরি widget-এ রাখতে, যেটা test করা কঠিন। Logic-কে UI-এর বাইরে রাখুন।

```dart
Future<void> _load() async {
  final data = await api.fetch();
  if (!mounted) return;        // পাহারা: widget এখন dispose হয়ে থাকতে পারে
  setState(() => _data = data);
}
```

**Interviewer কেন জিজ্ঞেস করে:** `setState` যে element-কে dirty চিহ্ন দেয় আর subtree-তে পুরো `build()` চালায় — এটা জানা মানে আপনি rebuild pipeline বোঝেন। এতে বোঝা যায় আপনি performant code লেখেন কি না।

**সাধারণ ভুল:** Closure-এর বাইরে variable বদলানো (`_count++; setState(() {});`)। এটা কাজ করে, কিন্তু উদ্দেশ্যটা লুকিয়ে ফেলে — পরিবর্তনটা closure-এর ভেতরে রাখুন। আরেকটা: `build()`-এর ভেতরে `setState` call করা (অসীম loop) বা `initState`-এর ভেতরে করা (error)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`setState` কি সাথে সাথে rebuild করে?"* → না। এটা widget-কে dirty চিহ্ন দেয় আর পরের frame-এ rebuild করে।
- *"`mounted` কী?"* → `State`-এর উপর একটা flag, যেটা dispose-এর পরে `false` হয়। `await`-এর পরে `setState` করার আগে এটা check করুন।

**সম্পর্কিত:** [Q1 — state কী](#q1) · [Q3 — lifecycle](#q3) · [Q12 — emit vs setState](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. `StatefulWidget`-এর lifecycle ধাপে ধাপে বলুন। State আসলে কোথায় থাকে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`StatefulWidget` নিজে ফেলে দেওয়ার জিনিস, এটা বারবার rebuild হয়। তাই আসল state থাকে এর আলাদা `State` object-এ। Flutter সেই `State` object-কে rebuild-এর পরেও বাঁচিয়ে রাখে। মূল lifecycle ধাপগুলো হলো `initState` (একবার সব সেট করা), `didChangeDependencies`, `build` (অনেকবার চলে), `didUpdateWidget` (parent নতুন input দিয়েছে), আর `dispose` (পরিষ্কার করা)। আমি controller আর subscription তৈরি করি `initState`-এ, আর ছেড়ে দিই `dispose`-এ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — State কেন আলাদা object-এ থাকে।**
Widget শুধু একটা হালকা বর্ণনা, আর এটা অনবরত rebuild হয়। আপনার data যদি widget-এর ভেতরে থাকত, প্রতিটা rebuild-এ তা মুছে যেত। তাই Flutter জিনিসটা ভাগ করে দেয়: `StatefulWidget` হলো ফেলে দেওয়ার recipe, আর `State` object হলো অনেকক্ষণ টিকে থাকা রান্নাঘর যেটা সত্যিকারের data ধরে রাখে। Widget rebuild হলেও Flutter একই `State` object বাঁচিয়ে রাখে।

**ধাপ ২ — Lifecycle ক্রম অনুযায়ী।**

```dart
class _ProfilePageState extends State<ProfilePage> {
  late final TextEditingController _controller;

  @override
  void initState() {
    super.initState();
    // State তৈরি হলে একবারই চলে — controller, subscription সেট করুন
    _controller = TextEditingController();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // initState-এর পরে চলে, আর নির্ভর করে এমন InheritedWidget বদলালে আবার চলে
  }

  @override
  void didUpdateWidget(ProfilePage oldWidget) {
    super.didUpdateWidget(oldWidget);
    // parent rebuild হয়ে NEW input দিয়েছে — বদলানো widget field-এ সাড়া দিন
    if (oldWidget.userId != widget.userId) {
      // নতুন user-এর জন্য আবার load করুন
    }
  }

  @override
  Widget build(BuildContext context) {
    // অনেকবার চলে — সস্তা রাখুন, এখানে setup বা network call নয়
    return TextField(controller: _controller);
  }

  @override
  void dispose() {
    _controller.dispose();   // leak এড়াতে পরিষ্কার করুন
    super.dispose();         // super সবার শেষে call করুন
  }
}
```

**ধাপ ৩ — সোনার নিয়ম: `initState`-এ সেট করুন, `dispose`-এ পরিষ্কার করুন।**
যা কিছু resource ধরে রাখে — একটা `TextEditingController`, একটা `AnimationController`, একটা `StreamSubscription`, একটা timer — সবই `initState`-এ তৈরি করতে হবে আর `dispose`-এ ছাড়তে হবে। `dispose` ভুলে যাওয়া Flutter-এর সবচেয়ে সাধারণ memory leak-গুলোর একটা।

**ধাপ ৪ — `build` বনাম `didUpdateWidget`।**
লোকে এই দুটো গুলিয়ে ফেলে। `build` প্রতিটা rebuild-এ চলে, তাই এটা সস্তা হওয়া দরকার। `didUpdateWidget` শুধু তখনই চলে যখন parent এই widget-কে **নতুন input value** দেয় — বদলানো input-এ সাড়া দিতে এটা ব্যবহার করুন, যেমন `userId` বদলালে আবার load করা।

**ধাপ ৫ — `widget` field কেন গুরুত্বপূর্ণ।**
`State`-এর ভেতরে আপনি widget-এর input পড়েন `widget.something` দিয়ে (যেমন `widget.userId`)। `State` অনেক widget instance-এর চেয়ে বেশি দিন বাঁচে। তাই `widget` সবসময় সবচেয়ে নতুনটাকে দেখায় — এভাবেই অনেকক্ষণ টিকে থাকা State তাজা input দেখতে পায়।

**Interviewer কেন জিজ্ঞেস করে:** এটা প্রমাণ করে আপনি widget/element/state-এর ভাগটা বোঝেন। আর আপনি resource ঠিকমতো পরিষ্কার করেন কি না তাও বোঝা যায় — এটা production bug-এর একটা বড় source।

**সাধারণ ভুল:** `build`-এ setup code বা network call রাখা (এটা খুব বেশিবার চলে), অথবা controller ও subscription `dispose` করতে ভুলে যাওয়া। আরেকটা ভুল — `super.dispose()` শেষে না দিয়ে প্রথমে call করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Network call কোথায় শুরু করেন?"* → একবারের load-এর জন্য `initState`, কখনোই `build`-এ নয়।
- *"`mounted` কী?"* → এটা বলে দেয় `State` এখনো যুক্ত আছে কি না। `await`-এর পরে `setState`-এর আগে এটা check করুন। ([Q2](#q2) দেখুন।)

**সম্পর্কিত:** [Q2 — setState](#q2) · [Q5 — InheritedWidget ও didChangeDependencies](#q5)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. "Lifting state up" মানে কী, আর এটা কেন scale করা বন্ধ করে দেয়?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Lifting state up মানে যে widget-গুলোর একই state দরকার, তাদের সবচেয়ে কাছের common parent-এ সেই state সরিয়ে নেওয়া। তারপর data নিচে পাঠানো আর callback উপরে পাঠানো। কাছাকাছি কয়েকটা widget-এর মধ্যে state ভাগ করার এটাই সবচেয়ে সহজ উপায়। এটা scale করা বন্ধ করে দেয়, কারণ tree বড় হলে data আর callback এমন অনেক widget-এর ভেতর দিয়ে টানতে হয় যারা ওগুলো ব্যবহারই করে না। ঠিক এই কষ্টের জন্যই Provider, Riverpod আর BLoC আছে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ধারণাটা: state-কে একটা common parent-এ সরান।**
দুটো sibling widget-এর যদি একই value দরকার হয়, কেউই সেটার মালিক হতে পারে না। কারণ sibling-রা একে অপরকে দেখতে পায় না। তাই আপনি value-টা তাদের common parent-এ উপরে তুলে দেন। Parent state-এর মালিক হয়, value **নিচে** children-কে দেয়, আর children পরিবর্তন **উপরে** পাঠায় callback দিয়ে।

```dart
class _ParentState extends State<Parent> {
  int _count = 0; // ভাগ করা state থাকে common parent-এ

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      CountLabel(count: _count),                       // data যায় নিচে
      IncrementButton(
        onPressed: () => setState(() => _count++),     // পরিবর্তন আসে উপরে
      ),
    ]);
  }
}
```

**ধাপ ২ — ছোট ক্ষেত্রে এটা কেন ভালো।**
বাড়তি কোনো package নেই, কোনো জাদু নেই, আর data flow স্পষ্ট: constructor দিয়ে নিচে, callback দিয়ে উপরে। দুই-তিনটা কাছাকাছি widget-এর জন্য এটাই সঠিক আর সবচেয়ে সহজ উত্তর।

**ধাপ ৩ — কেন এটা scale করা বন্ধ করে (prop drilling)।**
এবার ভাবুন value-টা পাঁচ layer গভীরে দরকার। মাঝের প্রতিটা widget-কে সেটা নিতে হবে আর এগিয়ে দিতে হবে, যদিও সে কখনো ব্যবহার করে না। একে বলে "prop drilling", আর এটা কষ্টের:

```dart
// Screen -> Section -> Card -> Row -> finally the widget that needs 'user'
Section(user: user)        // Section user ব্যবহার করে না, শুধু এগিয়ে দেয়
  -> Card(user: user)      // Card-ও এটা ব্যবহার করে না
    -> ProfileRow(user: user) // ...শুধু এই leaf-এর সত্যিই এটা দরকার
```

নতুন কোনো ভাগ করা data এলেই প্রতিটা layer আবার edit করতে হয়। এটা ঠুনকো আর গোলমেলে।

**ধাপ ৪ — সমাধান: state উপরে provide করুন, সরাসরি পড়ুন।**
State manager prop drilling সমাধান করে এভাবে — যেকোনো descendant ভাগ করা state সরাসরি পড়তে পারে, মাঝের widget-কে সেটা বইতে হয় না। `Provider`/`Riverpod`/`BLoC` সবাই আপনাকে এই "যেখানে দরকার সেখানেই পড়ুন" ক্ষমতা দেয়। এদের থাকার কারণ এটাই — tree গভীর হয়ে গেলে এরা হাতে করা lifting-এর জায়গা নিয়ে নেয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি স্বাভাবিক ধাপগুলো বোঝেন: শুরু করুন সহজভাবে lifting state up দিয়ে, আর state manager-এ যান তখনই যখন prop drilling কষ্ট হয়ে দাঁড়ায়।

**সাধারণ ভুল:** হয় কখনোই state না তোলা (বদলে global ব্যবহার করা), অথবা সবকিছু একদম উপরে তুলে দেওয়া, ফলে বিশাল rebuild হয়। শুধু **সবচেয়ে কাছের** common parent পর্যন্ত তুলুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কখন lifting থামিয়ে state manager আনবেন?"* → যখন এমন widget-এর ভেতর দিয়ে data পাঠাতে হয় যারা সেটা ব্যবহার করে না (prop drilling), অথবা যখন সম্পর্ক নেই এমন screen-এরও সেটা দরকার হয়।
- *"খুব উপরে তুললে খরচ কী?"* → উপরে একটা পরিবর্তন হলে বড় একটা subtree rebuild হয়। State যত নিচে রাখা যায় তত ভালো।

**সম্পর্কিত:** [Q5 — InheritedWidget](#q5) · [Q16 — screen-এর মধ্যে ভাগ করা](#q16) · [Q1 — state কী](#q1)

[↑ উপরে ফিরুন](#toc)

---

# B. ভিত্তি: InheritedWidget ও Provider

---

## <a id="q5"></a>5. `InheritedWidget` কীভাবে data নিচে পাঠায়, আর `updateShouldNotify` কী করে?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`InheritedWidget` হলো Flutter-এর নিজের উপায় data-কে tree-এর নিচে ঠেলে দেওয়ার, যাতে যেকোনো descendant সরাসরি পড়তে পারে, প্রতিটা constructor দিয়ে পাঠাতে না হয়। Descendant এটা পড়ে `dependOnInheritedWidgetOfExactType` দিয়ে, আর এটা ওই widget-কে পরিবর্তনের জন্য subscribe-ও করে দেয়। Data বদলালে Flutter `updateShouldNotify` call করে; এটা true দিলে শুধু নির্ভর করে এমন widget-গুলোই rebuild হয়। `Theme.of(context)` আর Provider-এর নিচের engine এটাই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "ভাগ করা noticeboard"-এর ধারণা।**
`InheritedWidget`-কে ভাবুন tree-এর উপরে বসানো একটা noticeboard হিসেবে। নিচের যেকোনো widget উপরে গিয়ে board পড়তে পারে। চাইলে subscribe করতে পারে, যাতে board বদলালে খবর পায়। কাউকে হাতে করে data নিচে নিয়ে আসতে হয় না — এটাই [Q4](#q4)-এর prop drilling-এর কষ্ট দূর করে।

**ধাপ ২ — Descendant কীভাবে পড়ে আর subscribe করে।**
Descendant call করে `context.dependOnInheritedWidgetOfExactType<MyInherited>()`। এটা দুটো কাজ করে: data ফেরত দেয়, আর এই widget-কে একটা **dependent** হিসেবে নিবন্ধন করে। Dependent হওয়া মানে "এই data বদলালে আমাকে rebuild করো।"

**ধাপ ৩ — Update-এর প্রবাহ।**

1. `InheritedWidget` নতুন data নিয়ে rebuild হয়।
2. Flutter এটার উপরে `updateShouldNotify(oldWidget)` call করে।
3. এটা `true` দিলে Flutter প্রতিটা dependent-এর উপরে `didChangeDependencies()` call করে আর তাদের rebuild-এর জন্য চিহ্নিত করে।
4. এটা `false` দিলে dependent-রা rebuild হয় **না** — যদিও inherited widget নিজে rebuild হয়েছে।

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

**ধাপ ৪ — `updateShouldNotify` হলো performance-এর switch।**
এটা একটাই প্রশ্নের উত্তর দেয়: "data কি সত্যিই এতটা বদলেছে যে listener-দের rebuild করানো দরকার?" পুরোনো আর নতুন value তুলনা করুন, আর দরকার হলেই `true` ফেরত দিন।

```dart
class ThemeInherited extends InheritedWidget {
  final AppTheme theme;
  const ThemeInherited({required this.theme, required super.child});

  static AppTheme of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<ThemeInherited>()!.theme;

  @override
  bool updateShouldNotify(ThemeInherited oldWidget) =>
      theme.primaryColor != oldWidget.theme.primaryColor ||
      theme.fontSize != oldWidget.theme.fontSize; // এগুলো বদলালেই কেবল rebuild
}

// যেকোনো descendant:
final theme = ThemeInherited.of(context);
```

**ধাপ ৫ — Subscribe না করে পড়া।**
দুই ধরনের lookup আছে। `dependOnInheritedWidgetOfExactType` subscribe করে (পরিবর্তনে rebuild হয়)। `getInheritedWidgetOfExactType` শুধু পড়ে, কোনো subscription নেই (পরিবর্তনে rebuild হয় না)। ভুলটা বেছে নিলে হয় update হাতছাড়া হয়, নয়তো দরকার নেই এমন rebuild হয়।

**Interviewer কেন জিজ্ঞেস করে:** `InheritedWidget` হলো `Theme.of`, `MediaQuery.of` আর Provider-এর নিচের ভিত্তি। এটা বুঝলে আপনি বুঝে যাবেন উপরের সব state management ভেতরে কীভাবে কাজ করে।

**সাধারণ ভুল:** `updateShouldNotify` থেকে শর্ত ছাড়াই `true` ফেরত দেওয়া — এতে প্রতিটা পরিবর্তনে প্রতিটা dependent rebuild হয় আর পুরো optimization নষ্ট হয়। আরেকটা ভুল — subscribe করা lookup আর subscribe না করা lookup গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`didChangeDependencies` কে call করে?"* → কোনো dependency বদলালে (যখন `updateShouldNotify` true দেয়)। `initState`-এর পরেও এটা একবার চলে।
- *"Provider কেন এর উপরে বানানো?"* → Provider `InheritedWidget`-কে মুড়ে boilerplate কমায় আর `ChangeNotifier`-এ listening যোগ করে। ([Q6](#q6) দেখুন।)

**সম্পর্কিত:** [Q4 — prop drilling](#q4) · [Q6 — Provider](#q6) · [Q3 — didChangeDependencies](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. Provider ব্যাখ্যা করুন — `ChangeNotifier`, `Consumer`, `Selector`, আর `ProxyProvider`।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Provider হলো `InheritedWidget`-এর উপর একটা পাতলা, বন্ধুত্বপূর্ণ wrapper, যেটা boilerplate সরিয়ে দেয়। আমার model `ChangeNotifier` extend করে। data বদলালে সেটা `notifyListeners()` call করে। model বদলালে `Consumer` শুধু একটা subtree rebuild করে। `Selector` rebuild করে শুধু তখন, যখন বেছে নেওয়া একটা field বদলায়। আর `ProxyProvider` একটা provided value থেকে আরেকটা value বানায়। বেশিরভাগ app-এর জন্য এটাই officially recommended শুরুর জায়গা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `ChangeNotifier` = "আমি বদলালে আমার listener-দের বলে দাও।"**
`ChangeNotifier`-কে একজন ঢোল পেটানো ঘোষকের মতো ভাবুন। আপনার model data ধরে রাখে। data বদলালে সেটা চিৎকার করে `notifyListeners()` বলে। যারা শুনছে, তারা update হয়ে যায়।

```dart
class CartModel extends ChangeNotifier {
  final List<Item> _items = [];
  List<Item> get items => List.unmodifiable(_items);
  int get totalCount => _items.length;
  double get totalPrice => _items.fold(0, (sum, i) => sum + i.price);

  void add(Item item) {
    _items.add(item);
    notifyListeners(); // চিৎকার: "আমি বদলে গেছি!" -> listener-রা rebuild হয়
  }
}
```

**ধাপ ২ — যে widget-গুলোর দরকার, তাদের উপরে model provide করুন।**

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

**ধাপ ৩ — `Consumer` = শুধু এই subtree rebuild করে।**
যে অংশটা rebuild হওয়া দরকার, শুধু সেটাকেই wrap করুন। তাহলে screen-এর বাকি অংশ স্থির থাকে।

```dart
Consumer<CartModel>(
  builder: (context, cart, child) => Text('Items: ${cart.totalCount}'),
)
```

`child` parameter-টা একটা বাড়তি সুবিধা: এমন একটা widget পাঠান যেটা model-এর উপর নির্ভর করে **না**। Provider সেটাকে rebuild না করে আবার ব্যবহার করে।

**ধাপ ৪ — `Selector` = শুধু একটা field বদলালেই rebuild।**
যেকোনো `notifyListeners()`-এ `Consumer` rebuild হয়। `Selector` আরও খুঁটিয়ে বেছে নেয়: আপনি একটা value বেছে নেন, আর সেটা বদলালে তবেই rebuild হয় (`==` দিয়ে তুলনা করে)।

```dart
// শুধু totalPrice বদলালে rebuild হয়, model-এর বাকি সব বাদ দেয়
final price = context.select<CartModel, double>((cart) => cart.totalPrice);
Text('Total: \$${price.toStringAsFixed(2)}');
```

**ধাপ ৫ — `ProxyProvider` = এক value থেকে আরেক value বানানো।**
যখন একটা object-এর ভেতরে আরেকটা object inject করতে হয়, তখন এটা ব্যবহার করুন — যেমন একটা `AuthService`, যার `ApiClient` লাগে।

```dart
MultiProvider(
  providers: [
    Provider<ApiClient>(create: (_) => ApiClient()),
    ProxyProvider<ApiClient, AuthService>(
      update: (_, api, __) => AuthService(api), // ApiClient বদলালে আবার তৈরি হয়
    ),
  ],
  child: const MyApp(),
)
```

**ধাপ ৬ — সবসময় resource ছেড়ে দিন।**
আপনার `ChangeNotifier` tree থেকে চলে গেলে `ChangeNotifierProvider` নিজেই তার `dispose()` call করে। ফলে model-এর ভেতরের timer আর subscription পরিষ্কার হয়ে যায়। আপনি নিজে notifier বানিয়ে `.value` দিয়ে পাঠালে, dispose করার দায়িত্ব আপনার।

**Interviewer কেন জিজ্ঞেস করে:** Provider হলো beginner থেকে intermediate পর্যায়ের officially recommended tool। তাঁরা দেখেন আপনি `Consumer`/`Selector` দিয়ে rebuild সীমিত রাখতে পারেন কি না, নাকি প্রতিবার পুরো screen rebuild করেন।

**সাধারণ ভুল:** একটা বিশাল subtree-কে একটা `Consumer`-এ wrap করা, ফলে সবকিছু rebuild হয়। `Consumer`-কে ছোট পরিসরে রাখুন, অথবা শুধু একটা field-এর জন্য `Selector` ব্যবহার করুন। আরেকটা ভুল: `notifyListeners()` call করা method-এর মধ্য দিয়ে না গিয়ে বাইরে থেকে সরাসরি model-এর list বদলে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`Consumer` vs `Selector`?"* → যেকোনো পরিবর্তনে `Consumer` rebuild হয়; বেছে নেওয়া value বদলালে তবেই `Selector` rebuild হয়।
- *"`child` argument কীসের জন্য?"* → এমন একটা widget যেটা model-এর উপর নির্ভর করে না; Provider সেটা রেখে দেয় আর rebuild এড়িয়ে যায়।

**সম্পর্কিত:** [Q5 — InheritedWidget](#q5) · [Q7 — watch/read/select](#q7) · [Q13 — Riverpod](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. `context.watch`, `context.read`, আর `context.select`-এর পার্থক্য কী?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"তিনটাই একটা provided value পড়ে, কিন্তু শোনার ধরন আলাদা। `watch` subscribe করে আর প্রতিটা পরিবর্তনে widget rebuild করে — এটা `build`-এ ব্যবহার করি। `read` একবার পড়ে, কোনো subscription নেই — এটা `onPressed`-এর মতো callback-এ ব্যবহার করি। `select` সবচেয়ে নিখুঁত: এটা একটা derived value দেখে, আর ঠিক সেই value বদলালেই rebuild করে। চেনা নিয়মটা হলো: `build`-এ `watch`/`select`, callback-এ `read`।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "subscription"-এর ধারণা।**
এই তিনটাকে খবর পড়ার তিনটা উপায় ভাবুন। `watch` মানে "প্রতিটা update-এ আমাকে জানাও।" `select` মানে "শুধু এই একটা শিরোনাম বদলালে আমাকে জানাও।" `read` মানে "আজকের খবরটা একবার বলে দাও, আমার পিছু নিও না।"

**ধাপ ২ — `context.watch<T>()` — যেকোনো পরিবর্তনে rebuild।**
এটা `build`-এর ভেতরে ব্যবহার করুন। `T` যখনই `notifyListeners()` call করে, widget rebuild হয়।

```dart
@override
Widget build(BuildContext context) {
  final cart = context.watch<CartModel>(); // cart-এর যেকোনো পরিবর্তনে rebuild
  return Text('Items: ${cart.totalCount}');
}
```

**ধাপ ৩ — `context.read<T>()` — একবার পড়ে, rebuild নেই।**
এটা callback-এর ভেতরে ব্যবহার করুন (`onPressed`, `onTap`)। আপনি শুধু কাজ করতে চান, subscribe করতে নয়।

```dart
FloatingActionButton(
  onPressed: () => context.read<CartModel>().add(Item('Shoes', 59.99)),
  child: const Icon(Icons.add),
)
```

**ধাপ ৪ — `context.select<T, R>(...)` — একটা derived value দেখে।**
সবচেয়ে খুঁটিয়ে বেছে নেওয়ার option। বেছে নেওয়া value `R` বদলালেই শুধু rebuild হয়, `T`-র অন্য অংশ বদলালেও নয়।

```dart
// শুধু totalPrice বদলালে rebuild হয়, item-এর নাম বদলালে নয়
final price = context.select<CartModel, double>((c) => c.totalPrice);
```

**ধাপ ৫ — সিদ্ধান্তের তালিকা।**

```
context.watch<T>()      -> rebuild on ANY change to T        (use in build)
context.select<T,R>()   -> rebuild only when R (part of T) changes (use in build)
context.read<T>()       -> read once, NO subscription        (use in callbacks)
```

**ধাপ ৬ — callback-এ `watch` কেন error দেয়।**
`watch` পরিবর্তনে subscribe করে, আর subscribe করা শুধু build phase-এ বৈধ। button-এর callback build-এর বাইরে চলে। তাই সেখানে `watch` call করলে error হয়। callback-এ `read` ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটাই Provider-এর সবচেয়ে সাধারণ performance প্রশ্ন। ভুলটা বেছে নিলে হয় update মিস হয় (`build`-এ `read`), নয়তো runtime error হয় (callback-এ `watch`)।

**সাধারণ ভুল:** `onPressed`-এর ভেতরে `context.watch` ব্যবহার করা (runtime error), অথবা `build`-এর ভেতরে `context.read` ব্যবহার করা (data বদলালে widget rebuild হবে না)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`onPressed`-এ `read` কেন সঠিক?"* → callback build-এর বাইরে চলে; আপনি শুধু একবার পড়তে চান, subscription চান না।
- *"`select` কী বাঁচায়?"* → যে field নিয়ে আপনার মাথাব্যথা নেই, সেটা বদলালে rebuild হওয়া এড়ায়।

**সম্পর্কিত:** [Q6 — Provider](#q6) · [Q13 — Riverpod-এর ref.watch/read/listen](#q13)

[↑ উপরে ফিরুন](#toc)

---

# C. BLoC পরিবার

---

## <a id="q8"></a>8. BLoC pattern ব্যাখ্যা করুন — event, state, আর stream।

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"BLoC মানে Business Logic Component। UI ভেতরে event পাঠায় — যেমন 'login pressed'। BLoC ফেরত পাঠায় state-এর একটা stream — যেমন loading, তারপর success বা failure। UI শুধু যে state পায় সেটা থেকে rebuild করে। এতে business logic widget-এর বাইরে থাকে। ফলে সেটা আগে থেকে বোঝা যায় এমন হয় আর test করা সহজ হয়। আধুনিক bloc v8+-এ আমি `on<Event>()` দিয়ে handler register করি, আর `Emitter` দিয়ে নতুন state emit করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "order counter"-এর ধারণা।**
BLoC-কে একটা fast-food counter-এর মতো ভাবুন। আপনি (UI) একটা order slip জমা দেন — সেটাই একটা **event**। রান্নাঘর (BLoC) কাজ করে আর একটা একটা করে plate ফেরত দেয় — সেগুলোই **state** (প্রথমে "cooking", তারপর "ready" বা "দুঃখিত, stock শেষ")। আপনি নিজে কিছু রান্না করেন না; শুধু যে plate পান, তাতে সাড়া দেন।

```
   UI  --event-->  BLoC  --stream of states-->  UI (rebuilds)

   event in  ->  BLoC processes  ->  new state emitted  ->  UI updates
```

**ধাপ ২ — Event আর state সাধারণ class।**
Event হলো input (button tap, page load)। State হলো output (initial, loading, success, failure)। এগুলোকে class বানালে — প্রায়ই `sealed` — type system দেখে নিতে পারে আপনি সবগুলো handle করেছেন কি না (দেখুন [Q15](#q15))।

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

**ধাপ ৩ — BLoC event থেকে state বানায় (আধুনিক v8+ ধরন)।**
constructor-এ `on<Event>()` দিয়ে প্রতি event-এর জন্য একটা handler register করেন। প্রতিটা handler event পায়, আর নতুন state পাঠানোর জন্য একটা `Emitter` পায়।

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

**ধাপ ৪ — পুরোনো `mapEventToState` (চিনে রাখা ভালো)।**
bloc v8-এর আগে আপনি একটা বড় `mapEventToState` method override করতেন, যেটা `async*` আর `yield` ব্যবহার করত। Interviewer এটা দেখাতে পারেন — চিনে নিন যে এটা পুরোনো ধরন, যার জায়গা নিয়েছে `on<Event>()`।

```dart
// পুরোনো (pre-v8) — এর জায়গা নিয়েছে on<Event>():
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

**ধাপ ৫ — এই design কেন এত পছন্দের।**
সবকিছু এক দিকে বয়ে যায় (event in → state out)। তাই logic আগে থেকে বোঝা যায় এমন আর test করা সহজ: একটা event দিন, state-গুলো assert করুন। আর প্রতিটা event একটা object বলে, যা যা ঘটেছে সব event log করা যায় — debugging-এর জন্য দারুণ।

**Interviewer কেন জিজ্ঞেস করে:** Flutter-এ production-এ সবচেয়ে বেশি ব্যবহার করা pattern-গুলোর একটা হলো BLoC, বিশেষ করে BD আর agency team-এ। তাঁরা শুনতে চান আপনি একমুখী, stream-ভিত্তিক flow বোঝেন। আর event থেকে state আলাদা রাখলে code কেন testable হয়, সেটাও বোঝেন।

**সাধারণ ভুল:** পুরোনো `mapEventToState`-এর সাথে নতুন `on<Event>` API মিশিয়ে ফেলা। আরেকটা ভুল: bloc বন্ধ হয়ে যেতে পারে এমন অবস্থায় `await`-এর পরে `emit()` call করা (দেখুন [Q12](#q12))। আর feature অনুযায়ী ভাগ না করে একটা বিশাল bloc বানানো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Event আর state আলাদা কেন?"* → এতে একমুখী flow পাওয়া যায় আর input-এর একটা log থাকে, যা behavior-কে আগে থেকে বোঝা যায় এমন ও testable করে।
- *"`EventTransformer` কী?"* → event কীভাবে process হবে সেটা control করার উপায় — যেমন search-as-you-type-এ debounce বা throttle করা।

**সম্পর্কিত:** [Q9 — Cubit vs BLoC](#q9) · [Q10 — Builder/Listener/Consumer](#q10) · [Q15 — sealed states](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. Cubit কী? এটা BLoC থেকে কীভাবে আলাদা, আর কোনটা কখন পছন্দ করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Cubit হলো সহজ একটা BLoC, যেখান থেকে event layer সরিয়ে দেওয়া হয়েছে। Event পাঠানোর বদলে আমি Cubit-এর উপর সরাসরি method call করি। সেই method-গুলো `emit(newState)` call করে। দুটোরই base class এক, তাই দুটোই `BlocBuilder` আর তার সঙ্গীদের সাথে কাজ করে। counter বা toggle-এর মতো সহজ logic-এ আমি Cubit ব্যবহার করি। আর যখন event-এর log দরকার, বা debounce-এর মতো stream transformation দরকার, তখন পুরো BLoC ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Cubit = "শুধু একটা method call করুন।"**
BLoC-এ আপনি একটা event object add করেন; Cubit-এ আপনি সাধারণ একটা method call করেন। BLoC-কে ভাবুন ticket system দিয়ে order দেওয়া, আর Cubit হলো সরাসরি বাবুর্চিকে বলে দেওয়া। আনুষ্ঠানিকতা কম।

```
BLoC:   UI -> Event -> on<Event> -> emit(State) -> UI
Cubit:  UI -> cubit.method()      -> emit(State) -> UI
```

**ধাপ ২ — একই পরিবার, একই widget।**
`Cubit` আর `Bloc` দুটোই একই base (`BlocBase`) extend করে। সেই base দেয় state stream, `emit`, বর্তমান `state`, আর `isClosed`। তাই Cubit `BlocBuilder`, `BlocListener` আর `BlocConsumer`-এর সাথে ঠিক Bloc-এর মতোই কাজ করে।

```dart
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);
  void increment() => emit(state + 1);
  void decrement() => emit(state - 1);
  void reset() => emit(0);
}

final cubit = CounterCubit();
cubit.increment(); // state এখন 1
cubit.increment(); // state এখন 2
```

**ধাপ ৩ — একই logic Bloc-এ লিখতে বেশি আনুষ্ঠানিকতা লাগে।**

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
bloc.add(Increment()); // আগে একটা event object বানাতেই হবে
```

**ধাপ ৪ — Trade-off-এর তুলনার তালিকা।**

| দিক | Cubit | Bloc |
|---|---|---|
| Input | সরাসরি method call | event object |
| Boilerplate | কম — event class লাগে না | বেশি — event class লাগবেই |
| Traceability | log করা কঠিন | প্রতিটা event একটা log করা object (`onTransition`) |
| Transformations | নেই | debounce, throttle, merge-এর জন্য `EventTransformer` |
| Testing | সরাসরি method call করুন | event add করুন, state stream যাচাই করুন |

**ধাপ ৫ — কোনটা কখন নেবেন।**
- **Cubit বেছে নিন** সরল logic-এর জন্য: counter, toggle, সহজ form state, settings। code কম, পড়তে সহজ।
- **Bloc বেছে নিন** যখন কী ঘটেছে তার log দরকার (event sourcing), বা যখন event debounce/throttle করতেই হবে (search-as-you-type), বা যখন feature এত জটিল যে বাড়তি structure-এর দাম উঠে আসে।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা বাস্তববুদ্ধি দেখতে চান। সহজ ক্ষেত্রে Cubit বেছে নেওয়া দেখায় আপনি সরলতাকে মূল্য দেন। জটিল event flow-এ Bloc বেছে নেওয়া দেখায় আপনি traceability বোঝেন। সবচেয়ে দুর্বল উত্তর হলো "সবসময় Bloc ব্যবহার করি।"

**সাধারণ ভুল:** বলা যে Cubit-কে `BlocBuilder`/`BlocListener`-এর সাথে ব্যবহার করা যায় না — আসলে যায়, কারণ দুটোই `BlocBase` extend করে। আরেকটা ভুল — ভুলে যাওয়া যে Cubit-এ event-level traceability হারায়। জটিল flow debug করার সময় এতে কষ্ট হতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Cubit কি debounce করতে পারে?"* → built-in নেই। Event transformer Bloc-এর feature। Cubit-এ method call করার আগে নিজেই হাতে debounce করতে হবে।
- *"দুটোই কি নিজে থেকে close হয়?"* → `BlocProvider` tree থেকে সরে গেলে bloc/cubit close করে দেয়, ঠিক যেমন Provider একটা `ChangeNotifier` dispose করে।

**সম্পর্কিত:** [Q8 — BLoC pattern](#q8) · [Q12 — emit after close](#q12) · [Q18 — testing](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. `BlocBuilder` vs `BlocListener` vs `BlocConsumer` — কোনটা কখন ব্যবহার করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"State বদলালে `BlocBuilder` UI rebuild করে — data বা spinner দেখাতে এটা ব্যবহার করি। `BlocListener` state বদলালে একবার side-effect চালায়, rebuild করে না — navigation, SnackBar বা dialog-এর জন্য এটা ব্যবহার করি। `BlocConsumer` হলো দুটোই একসাথে, যখন একই state বদলে UI rebuild আর side-effect দুটোই দরকার। মূল কথা: builder দিয়ে rebuild, listener দিয়ে এককালীন action।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "screen vs action" ধারণাটা।**
কিছু state বদল আঁকা জিনিস বদলাবে (welcome text দেখানো)। আর কিছু বদল এককালীন action চালাবে (নতুন screen push করা, একটা SnackBar দেখানো)। Builder আঁকার জন্য; listener এককালীন action-এর জন্য।

```
state change
   |
   +--> BlocBuilder   -> rebuild widget (visual)
   |
   +--> BlocListener  -> fire a side-effect ONCE (navigate, snackbar)
   |
   +--> BlocConsumer  -> both: rebuild + side-effect
```

**ধাপ ২ — `BlocBuilder` UI rebuild করে।**

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

**ধাপ ৩ — `BlocListener` একবার side-effect চালায়।**
এর `child` rebuild হয় **না**। প্রতিটা state বদলে listener একবার চলে — যেসব কাজ বারবার হওয়া চলবে না, তার জন্য একদম মানানসই।

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
  child: const LoginForm(), // listener এটাকে rebuild করে না
)
```

**ধাপ ৪ — `BlocConsumer` দুটোই করে।**
একই state বদলে UI rebuild **আর** side-effect দুটোই দরকার হলে এটা ব্যবহার করুন।

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

**ধাপ ৫ — সহজ নিয়ম।**
Pixel বদলালে → `BlocBuilder`। এককালীন action হলে (navigate, snackbar, dialog) → `BlocListener`। দুটোই একসাথে হলে → `BlocConsumer`।

**Interviewer কেন জিজ্ঞেস করে:** এটা সরাসরি দেখে আপনি জানেন কি না কখন rebuild করতে হয় আর কখন এককালীন action চালাতে হয়। ভুল করলে dialog বারবার খুলতে থাকে, বা navigation কখনোই চলে না।

**সাধারণ ভুল:** `BlocBuilder`-এর ভেতরে SnackBar দেখানো — প্রতিটা rebuild-এ builder আবার চলে, তাই SnackBar বারবার আসতে থাকে। SnackBar হলো side-effect, তাই এর জায়গা `BlocListener`-এ। উল্টোদিকে, screen-এ state দেখানোর জন্য `BlocListener` ব্যবহার করলে কিছুই হবে না, কারণ এর কোনো builder নেই।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Builder-এ navigate করলে সমস্যা কী?"* → Builder অনেকবার চলতে পারে; তাহলে navigation বারবার চলবে। প্রতিটা বদলে listener একবারই চলে।
- *"দরকার নেই এমন rebuild কীভাবে এড়াবেন?"* → `buildWhen`/`listenWhen` ব্যবহার করুন (দেখুন [Q11](#q11))।

**সম্পর্কিত:** [Q8 — BLoC pattern](#q8) · [Q11 — buildWhen/listenWhen](#q11) · [Q15 — sealed states](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. `buildWhen` আর `listenWhen` কী কাজ করে, আর performance-এর জন্য এগুলো কেন গুরুত্বপূর্ণ?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"এগুলো filter। `buildWhen` বসে `BlocBuilder`-এ আর আগের ও বর্তমান state পায়; false return করলে state বদলালেও builder ওই rebuild বাদ দেয়। `listenWhen` একই কাজ করে `BlocListener`-এর জন্য। এগুলো গুরুত্বপূর্ণ কারণ একটা bloc সেকেন্ডে অনেকগুলো state emit করতে পারে। filter না থাকলে প্রতিবার যুক্ত সব widget rebuild হয় — মসৃণ app আর janky app-এর পার্থক্য এখানেই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "এই বদল নিয়ে আমার মাথাব্যথা আছে কি?" ধারণাটা।**
একটা bloc অনেক কারণে state emit করতে পারে। যে widget শুধু name দেখায়, email বদলালে তার rebuild হওয়ার দরকার নেই। `buildWhen` সেই widget-কে বলতে দেয় — "আমি যেটা নিয়ে চিন্তা করি, সেটা বদলালেই কেবল আমাকে rebuild করো।"

**ধাপ ২ — `buildWhen` rebuild filter করে।**
এটা `previous` আর `current` পায় আর একটা `bool` return করে। Rebuild বাদ দিতে `false` return করুন।

```dart
BlocBuilder<FormBloc, FormState>(
  buildWhen: (previous, current) => previous.name != current.name, // শুধু name বদলালে
  builder: (context, state) => Text('Name: ${state.name}'),
)
```

**ধাপ ৩ — `listenWhen` side-effect filter করে।**
`BlocListener`-এর জন্য একই ধারণা। সত্যিকারের transition হলেই SnackBar দেখাতে এটা কাজে লাগে।

```dart
BlocListener<FormBloc, FormState>(
  listenWhen: (prev, curr) => prev.isSubmitting && !curr.isSubmitting, // শুধু submit শেষ হলে
  listener: (context, state) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Form submitted!')),
    );
  },
  child: const FormBody(),
)
```

**ধাপ ৪ — `BlocConsumer`-এ দুটোই একসাথে।**

```dart
BlocConsumer<AuthBloc, AuthState>(
  buildWhen: (prev, curr) => prev.runtimeType != curr.runtimeType, // শুধু type বদলালে rebuild
  listenWhen: (prev, curr) => curr is AuthFailure,                 // শুধু failure-এ listen
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

**ধাপ ৫ — বাস্তবে এর লাভ।**
search-as-you-type-এর কথা ভাবুন: প্রতিটা keystroke-এ bloc নতুন state emit করে। `buildWhen` ছাড়া প্রতিটা keystroke-এ যুক্ত সব widget rebuild হয় — janky। এটা থাকলে শুধু সেই widget-গুলো rebuild হয় যাদের data সত্যিই বদলেছে।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি জানেন `BlocBuilder` নিজে থেকে চালাক **নয়** — এটা প্রতিটা state-এ rebuild করে। আর আপনি performance-এর জন্য filter চালু করতে পারেন।

**সাধারণ ভুল:** ধরে নেওয়া যে `buildWhen`-এর default হলো বাদ দেওয়া; আসলে default হলো `(prev, curr) => true`, মানে "সবসময় rebuild"। আরেকটা ভুল — `buildWhen`-এর ভেতরে ধীর logic রাখা; এটা সস্তা একটা তুলনা হতে হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Default কী?"* → সবসময় rebuild / সবসময় listen। Filter নিজেই চালু করতে হবে।
- *"Provider-এ এর সমতুল্য কী?"* → `Selector` / `context.select` একই রকম কাজ করে (দেখুন [Q7](#q7))।

**সম্পর্কিত:** [Q10 — Builder/Listener/Consumer](#q10) · [Q7 — select](#q7) · [Q8 — BLoC pattern](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. `emit()` আর `setState()`-এর পার্থক্য কী? Cubit close হয়ে যাওয়ার পরে `emit()` call করলে কী হয়?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"দুটোই নতুন state পাঠায় আর UI update করে, কিন্তু দুটো আলাদা system-এ থাকে। `setState` থাকে একটা widget-এর `State`-এ, আর ওই widget-এর নিজের subtree rebuild করে। `emit` থাকে Cubit/Bloc-এ, আর নতুন state তার stream-এ পাঠায়। ফলে যেকোনো `BlocBuilder` যে শুনছে, সেটা rebuild হয়। Cubit close হওয়ার পরে আমি যদি `emit` call করি — সাধারণত একটা `await`-এর পরে, যখন user screen ছেড়ে চলে গেছে — তখন `StateError` throw হয়। আমি `isClosed` check দিয়ে এটা আটকাই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুটো tool, দুটো system।**
`setState` widget layer-এর অংশ; এটা widget-কে dirty চিহ্ন দেয় আর rebuild করে। `emit` bloc layer-এর অংশ; এটা bloc-এর state stream-এ নতুন value যোগ করে, যেটা যত widget শুনছে সবাই পায়।

```
setState() -> marks THIS widget dirty -> rebuilds its own subtree
emit()     -> pushes state onto the stream -> every BlocBuilder rebuilds
```

**ধাপ ২ — তুলনার তালিকা।**

| দিক | `setState()` | `emit()` |
|---|---|---|
| কোথায় থাকে | `State` (StatefulWidget) | `Cubit` / `Bloc` (BlocBase) |
| কী করে | element-কে dirty চিহ্ন দেয়, rebuild schedule করে | stream-এ নতুন state পাঠায় |
| কে rebuild হয় | এই widget-এর নিজের `build()` | যে যে `BlocBuilder`/`BlocListener` শুনছে |
| State-এর scope | এক widget-এর ভেতরেই সীমিত | bloc পড়ে এমন যেকোনো widget-এর সাথে shared |
| Lifecycle guard | `dispose()`-এর পরে call করলে throw করে | `close()`-এর পরে call করলে `StateError` throw করে |

**ধাপ ৩ — "emit after close" crash।**
একটা সাধারণ bug: আপনি একটা async call শুরু করলেন, user অন্য screen-এ চলে গেল (bloc close আর dispose হয়ে গেল), তারপর async call শেষ হয়ে `emit` করার চেষ্টা করল। Bloc close হয়ে যাওয়ায় এটা throw করে "Cannot emit new states after calling close."

```dart
class SearchCubit extends Cubit<SearchState> {
  SearchCubit(this._repo) : super(SearchInitial());
  final SearchRepository _repo;

  Future<void> search(String query) async {
    emit(SearchLoading());
    final results = await _repo.search(query); // কয়েক সেকেন্ড লাগে
    emit(SearchSuccess(results)); // user চলে গেলে -> StateError!
  }
}
```

**ধাপ ৪ — সমাধান: `isClosed` দিয়ে guard করুন।**

```dart
Future<void> search(String query) async {
  emit(SearchLoading());
  try {
    final results = await _repo.search(query);
    if (!isClosed) emit(SearchSuccess(results)); // emit করার আগে guard
  } catch (e) {
    if (!isClosed) emit(SearchFailure(e.toString()));
  }
}
```

এটা widget-এর দিকের `if (!mounted) return;` guard-এর মতোই, যেটা [Q2](#q2)-এ আছে — সমস্যা একই (async object-এর চেয়ে বেশি সময় বাঁচে), শুধু system আলাদা।

**ধাপ ৫ — Bloc handler নিয়ে একটা কথা।**
Bloc-এর `on<Event>` handler-এর ভেতরে framework সাহায্য করে: close-এর পরে emit হলে crash না করে সেটা ignore করা হয় (bloc v8.1+)। কিন্তু স্পষ্ট guard রাখা এখনো ভালো অভ্যাস, বিশেষ করে Cubit-এ আর handler-এর বাইরে emit করা code-এ।

**Interviewer কেন জিজ্ঞেস করে:** এটা widget lifecycle আর bloc lifecycle — দুটোর উপরেই আপনার দখল যাচাই করে। Production-এ bloc app-গুলোতে "emit after close" সবচেয়ে সাধারণ crash-এর একটা কারণ।

**সাধারণ ভুল:** Async gap-এর পরে `emit()` guard না করা আর ধরে নেওয়া "framework সামলে নেবে।" Cubit-এর ক্ষেত্রে সামলায় না — throw করে। আরেকটা ভুল হলো `setState`-এর "after dispose" error আর `emit`-এর "after close" error গুলিয়ে ফেলা; দুটো একই রকম, কিন্তু আলাদা system থেকে আসে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`mounted` vs `isClosed`?"* → `mounted` একটা widget-এ `setState` guard করে; `isClosed` একটা bloc/cubit-এ `emit` guard করে।
- *"এখানে leak কীভাবে এড়াবেন?"* → `close()`/`dispose()`-এ subscription cancel করুন, আর object চলে যাওয়ার পরে emit করবেন না।

**সম্পর্কিত:** [Q2 — setState & mounted](#q2) · [Q9 — Cubit](#q9) · [Q8 — BLoC pattern](#q8)

[↑ উপরে ফিরুন](#toc)

---

# D. Riverpod ও GetX

---

## <a id="q13"></a>13. Riverpod ব্যাখ্যা করুন — এটা Provider থেকে কীভাবে আলাদা, এর provider ধরনগুলো কী, আর `ref.watch` vs `ref.read` vs `ref.listen`।

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Riverpod বানিয়েছেন Provider-এর সেই একই লেখক, আর এটা Provider-এর প্রধান সীমাগুলো ঠিক করে: provider-গুলো global আর widget tree-র উপর নির্ভর করে না। তাই 'provider not found' runtime error থাকে না। এতে typed provider আছে — `StateProvider`, `FutureProvider`, `StreamProvider`, আর জটিল logic-এর জন্য `NotifierProvider`। একটা widget-এর ভেতরে আমি পরিবর্তনে rebuild করার জন্য `ref.watch` ব্যবহার করি, callback-এ একবার access করার জন্য `ref.read`, আর navigation-এর মতো side-effect-এর জন্য `ref.listen`।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Riverpod কেন এলো (Provider-এর কষ্টের জায়গাগুলো)।**

| Provider-এর সমস্যা | Riverpod কীভাবে ঠিক করে |
|---|---|
| Widget tree (`BuildContext`) লাগে | provider-গুলো global, tree-র উপর নির্ভর করে এমন নয় |
| "Provider not found" runtime-এ crash করে | compile time-এই ধরা পড়ে |
| একই type-এর দুটো provider রাখা যায় না | প্রতিটা provider নিজেই একটা আলাদা variable |
| Provider একসাথে মেলানো কঠিন | `ref` দিয়ে built-in dependency |
| Built-in auto-dispose নেই | `autoDispose` modifier |

**ধাপ ২ — Provider global ভাবে declare করা হয়।**
Provider যেহেতু শুধু একটা top-level variable, যেকোনো widget যেকোনো জায়গা থেকে সেটা পড়তে পারে — tree-তে খুঁজে বের করার দরকার নেই।

```dart
final counterProvider = StateProvider<int>((ref) => 0);

final todosProvider = FutureProvider<List<Todo>>((ref) async {
  final repo = ref.watch(todoRepositoryProvider); // provider একে অন্যের উপর নির্ভর করতে পারে
  return repo.fetchAll();
});

final chatProvider = StreamProvider<List<Message>>(
  (ref) => ref.watch(chatRepositoryProvider).messageStream(),
);
```

**ধাপ ৩ — Provider-এর ধরনগুলো (দরকার অনুযায়ী বাছুন)।**
- **`Provider<T>`** — একটা read-only বা computed value।
- **`StateProvider<T>`** — একটা সাধারণ mutable value (int, bool, enum)। জটিল state-এর জন্য ব্যবহার করবেন না।
- **`FutureProvider<T>`** — একটা `Future` থেকে `AsyncValue<T>` দেয়। এক-বারের async load-এর জন্য দারুণ।
- **`StreamProvider<T>`** — একই জিনিস, কিন্তু `Stream` থেকে। Live data-র জন্য (socket, Firestore)।
- **`NotifierProvider<N, T>`** (Riverpod 2.0+) — জটিল logic-এর আধুনিক ঠিকানা, একটা `Notifier` class ব্যবহার করে। এটা `StateNotifierProvider`-এর জায়গা নিয়েছে।

```dart
class TodosNotifier extends Notifier<List<Todo>> {
  @override
  List<Todo> build() => [];                 // শুরুর state

  void add(Todo todo) => state = [...state, todo];
  void toggle(String id) => state = [
        for (final t in state)
          if (t.id == id) t.copyWith(done: !t.done) else t,
      ];
}

final todosProvider = NotifierProvider<TodosNotifier, List<Todo>>(TodosNotifier.new);
```

**ধাপ ৪ — `ref.watch` vs `ref.read` vs `ref.listen`।**
এগুলো Provider-এর `watch`/`read`-এর মতোই, সাথে একটা listener যোগ হয়েছে।

```dart
class TodoPage extends ConsumerWidget {
  const TodoPage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final todos = ref.watch(todosProvider); // todos বদলালে rebuild

    ref.listen<List<Todo>>(todosProvider, (prev, next) { // side-effect, rebuild নয়
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
                onTap: () => ref.read(todosProvider.notifier).toggle(t.id), // callback-এ এক-বারের access
              ))
          .toList(),
    );
  }
}
```

- `ref.watch` → subscribe করে আর rebuild করে (`build`-এ ব্যবহার করুন)।
- `ref.read` → একবার পড়ে, কোনো subscription নেই (callback-এ ব্যবহার করুন)।
- `ref.listen` → পরিবর্তনে একটা side-effect চালায়, `BlocListener`-এর মতো।

**ধাপ ৫ — `AsyncValue` loading/error সহজ করে দেয়।**
`FutureProvider` আর `StreamProvider` একটা `AsyncValue` ফেরত দেয়, যেটা আপনি `.when` দিয়ে খোলেন — হাতে করে loading flag রাখার দরকার নেই।

```dart
final userAsync = ref.watch(userProvider);
return userAsync.when(
  loading: () => const CircularProgressIndicator(),
  error: (err, st) => Text('Error: $err'),
  data: (user) => Text('Hello, ${user.name}'),
);
```

**ধাপ ৬ — `autoDispose` resource ছেড়ে দেয়।**
`.autoDispose` যোগ করুন, তাহলে কেউ না শুনলে provider-টা ধ্বংস হয়ে যাবে — stream বা controller ধরে রাখা provider-এর জন্য এটা গুরুত্বপূর্ণ, leak এড়ানোর জন্য।

**Interviewer কেন জিজ্ঞেস করে:** নতুন Flutter project-এ Riverpod ক্রমেই default হয়ে উঠছে। তাঁরা দেখতে চান আপনি বোঝেন এটা Provider-এর চেয়ে কেন ভালো, আর সঠিক provider ধরন ও ref method ব্যবহার করতে পারেন কি না।

**সাধারণ ভুল:** `build`-এ `ref.read` ব্যবহার করা (পরিবর্তনে widget rebuild হবে না) বা callback-এ `ref.watch` ব্যবহার করা (দরকার নেই এমন subscription তৈরি করে)। আরেকটা ভুল হলো `.autoDispose` ভুলে যাওয়া, আর resource ধরে রাখা provider leak করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"'provider not found' error কেন নেই?"* → Provider হলো global variable, compile time-এ resolve হয়, tree-তে type দিয়ে খোঁজা হয় না।
- *"`StateNotifier` vs `Notifier`?"* → `Notifier` (Riverpod 2.0+) হলো আধুনিক বিকল্প; পুরোনো code-এ `StateNotifierProvider` ব্যবহার হয়।

**সম্পর্কিত:** [Q6 — Provider](#q6) · [Q7 — watch/read/select](#q7) · [Q15 — sealed states](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. GetX ব্যাখ্যা করুন — controllers, `Obx`, `GetBuilder` — আর এর trade-off কী কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"GetX একটা all-in-one package। এটা state management, dependency injection আর routing একসাথে দেয়, খুব কম boilerplate-এ। State থাকে একটা `GetxController`-এ। `.obs` দিয়ে একটা variable-কে reactive করা যায়। যে `Obx(() => ...)` সেটা পড়ে, সেটা নিজে থেকেই rebuild হয়। অথবা `GetBuilder` ব্যবহার করে হাতে `update()` call করা যায়। Trade-off হলো: এটা দিয়ে দ্রুত বানানো যায়, কিন্তু এতে অনেক লুকানো magic আর global singleton আছে। ফলে data flow খুঁজে বের করা কঠিন হয়, testing-ও কঠিন হয় — আর Flutter team এটাকে endorse করে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Controller-এ logic থাকে।**
একটা `GetxController`-এ আপনার state আর method থাকে। এটা Cubit-এর মতোই, তবে সাথে GetX-এর reactive helper আছে।

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

**ধাপ ২ — `.obs` + `Obx` = নিজে থেকেই rebuild।**
`.obs` যোগ করলে একটা value observable হয়ে যায়। যে `Obx` widget সেটা পড়ে, value বদলালে সেটা rebuild হয় — কোনো `notifyListeners` লাগে না, কোনো event লাগে না।

```dart
Get.put(CartController()); // register করুন (dependency injection)

Obx(() {
  final ctrl = Get.find<CartController>();
  return Text('Items: ${ctrl.items.length}, Total: ${ctrl.total}');
})
```

**ধাপ ৩ — `GetBuilder` = হাতে rebuild।**
এটা non-reactive উপায়। `GetBuilder` widget-কে rebuild করাতে আপনি `update()` call করেন — অনেকটা controller-scoped `setState`-এর মতো। এতে memory কম লাগে, কারণ কোনো observable stream নেই।

```dart
class CounterController extends GetxController {
  int count = 0;
  void increment() {
    count++;
    update(); // হাতে rebuild চালু করুন
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

**ধাপ ৪ — Trade-off গুলো।**

| সুবিধা | অসুবিধা |
|---|---|
| খুব কম boilerplate | লুকানো "magic" — data flow খুঁজে বের করা কঠিন |
| দ্রুত prototype বানানো যায় | global singleton testing কঠিন করে |
| Built-in routing + DI | Flutter team endorse করে না |
| বড় community, অনেক উদাহরণ | GetX ecosystem-এর সাথে শক্ত coupling |
| | বড় list-এ `.obs` performance সমস্যা লুকিয়ে ফেলতে পারে |

**ধাপ ৫ — কোথায় মানানসই।**
GetX ভালো কাজ করে একা কাজ করা developer, prototype আর ছোট app-এ। যেখানে কড়া architecture-এর চেয়ে দ্রুত বানানো বেশি জরুরি। বড় team আর জটিল app-এ এর implicit dependency (`Get.find`) আর global state code review ও testing কঠিন করে দেয়।

**Interviewer কেন জিজ্ঞেস করে:** যে team GetX ব্যবহার করে না, তারাও দেখতে চান আপনি একটা tool-কে সমালোচনার চোখে দেখতে পারেন কি না। নির্দিষ্ট শক্তি আর নির্দিষ্ট দুর্বলতার নাম বলা পরিপক্বতার লক্ষণ।

**সাধারণ ভুল:** কোনো nuance ছাড়া "GetX খারাপ" বা "GetX সেরা" বলে দেওয়া। শক্ত উত্তর ছোট app-এ এর গতির প্রশংসা করে। সাথে বড় team-এর জন্য নির্দিষ্ট খরচগুলো বলে (global state, implicit `Get.find`, mock করা কঠিন)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`Obx` vs `GetBuilder`?"* → `Obx` automatic আর reactive; `GetBuilder` হাতে `update()` দিয়ে চলে আর হালকা।
- *"Testing কেন কঠিন?"* → `Get.find` দিয়ে আসা global singleton-কে mock দিয়ে বদলানো কঠিন। Constructor দিয়ে inject করা dependency বদলানো সহজ।

**সম্পর্কিত:** [Q6 — Provider](#q6) · [Q13 — Riverpod](#q13) · [Q17 — কোন solution বাছবেন](#q17)

[↑ উপরে ফিরুন](#toc)

---

# E. Architecture ও senior সিদ্ধান্ত

---

## <a id="q15"></a>15. Sealed union দিয়ে loading, success আর error state কীভাবে পরিষ্কারভাবে model করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`isLoading`, `hasError` আর একটা nullable `data` — এরকম আলাদা boolean নিয়ে খেলার বদলে আমি state-টাকে একটা sealed class হিসেবে model করি। প্রতিটা case-এর জন্য একটা subtype: `Loading`, `Success`, `Failure`। Class-টা sealed বলে compiler আমার `switch`-কে সব case handle করতে বাধ্য করে। তাই কোনোটা ভুলে যাওয়ার সুযোগ নেই, আর `default`-ও লাগে না। এতে অসম্ভব state — যেমন একসাথে loading আর error — আসলেই আর তৈরি করা যায় না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Boolean flag-এর সমস্যা।**
একটা প্রচলিত কিন্তু দুর্বল উপায় হলো কয়েকটা flag ব্যবহার করা:

```dart
// দুর্বল: isLoading=true আর error!=null আর data!=null — এমন অসম্ভব combo-ও সম্ভব
class BadState {
  bool isLoading = false;
  String? error;
  UserProfile? data;
}
```

এখন প্রতিটা widget-কে আন্দাজ করতে হয় কোন flag-টা জেতে। আর ভুল করে মানে নেই এমন state বানিয়ে ফেলাও সম্ভব।

**ধাপ ২ — Sealed union: প্রতি case-এ একটা type।**
একটা `sealed` class এক file-এ হতে পারে এমন সব state-এর তালিকা রাখে। প্রতিটা state ঠিক যতটুকু data দরকার ততটুকুই বহন করে — এর বেশি কিছু নয়।

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

`Loading`-এ কোনো data নেই। `Success`-এ সবসময় data থাকে। `Failure`-এ সবসময় একটা message থাকে। আপনি "error সহ loading" বানাতে পারবেন না — ওই state-টার অস্তিত্বই নেই।

**ধাপ ৩ — Cubit-এ ব্যবহার করুন।**

```dart
class UserProfileCubit extends Cubit<ResultState<UserProfile>> {
  UserProfileCubit(this._repo) : super(const Loading());
  final UserRepository _repo;

  Future<void> load() async {
    emit(const Loading());
    try {
      final profile = await _repo.getProfile();
      if (!isClosed) emit(Success(profile)); // Q12-এর guard
    } catch (e) {
      if (!isClosed) emit(Failure('Failed to load profile', error: e));
    }
  }
}
```

**ধাপ ৪ — বড় লাভ: exhaustive `switch`।**
Class-টা sealed বলে একটা `switch` expression-কে সব subtype cover করতেই হবে। না করলে code compile হবে না। কোনো `default` লাগে না।

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

পরে যদি `class Empty extends ResultState<T> {}` যোগ করেন আর handle করতে ভুলে যান, তাহলে `switch` compile হওয়া বন্ধ করে দেবে। আর ঠিক ফাঁকটা দেখিয়ে দেবে। Bug ধরা পড়ে app চালু হওয়ার আগেই।

**ধাপ ৫ — এটাকে reusable বানান।**
আপনি একটা generic widget লিখতে পারেন, যেটা যেকোনো `ResultState` render করবে। ফলে প্রতিটা screen একইভাবে async handle করে।

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

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি state-কে স্পষ্টভাবে model করেন, দুর্বল boolean combination দিয়ে নয়। আর আপনি type system ব্যবহার করে অবৈধ state-কে অসম্ভব বানিয়ে দেন — এটা শক্ত senior signal।

**সাধারণ ভুল:** `switch`-এ একটা `default` case যোগ করা। এতে বাদ পড়া state চুপচাপ গিলে ফেলে, আর exhaustiveness check নষ্ট হয়ে যায়। আরেকটা ভুল — "দরকার হতে পারে" ভেবে boolean flag গুলো রেখে দেওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"sealed class vs `freezed` union?"* → দুটোই নির্দিষ্ট state model করে। `sealed` Dart 3-এর ভেতরেই আছে, আর exhaustive check বিনামূল্যে দেয় — কোনো code generation ছাড়াই।
- *"Riverpod এটা কীভাবে করে?"* → `AsyncValue` হলো built-in সংস্করণ, সাথে `.when(loading, error, data)` (দেখুন [Q13](#q13))।

**সম্পর্কিত:** [Q8 — BLoC states](#q8) · [Q12 — emit guards](#q12) · [Q13 — AsyncValue](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. সম্পূর্ণ সম্পর্ক নেই এমন দুটি screen-এর মধ্যে state কীভাবে share করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"'সম্পর্ক নেই এমন' মানে কোনো screen-ই অন্যটির ancestor নয়। তাই আমাকে state দুটোরই উপরে রাখতে হবে, অথবা tree-র একদম বাইরে রাখতে হবে। সবচেয়ে পরিষ্কার উপায় হলো `MaterialApp`-এর মতো common ancestor-এ একটা Provider/BLoC রাখা, অথবা একটা Riverpod provider ব্যবহার করা। Riverpod provider global আর tree-নিরপেক্ষ, তাই দুই screen একই instance পড়ে। আমি global mutable variable এড়িয়ে চলি, কারণ data বদলায় কিন্তু UI কখনো update হয় না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কেন এটাকে দুটোরই উপরে তুলতে হয়।**
আলাদা tab-এ থাকা দুটো screen একে অপরকে দেখতে পায় না। তাই shared state এমন জায়গায় থাকতে হবে যেখানে দুটোই পৌঁছাতে পারে: হয় tree-র একটা common ancestor-এ, নয়তো একটা global provider-এ যেটা tree নিয়ে মাথাই ঘামায় না।

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

**ধাপ ২ — কী কী উপায় আছে, সবচেয়ে সহজ থেকে সবচেয়ে decoupled পর্যন্ত।**
1. **Common ancestor-এ Provider / Riverpod / BLoC** — এটাকে `MaterialApp` level-এ রাখুন; দুই screen-ই এটা পড়বে। এটাই standard উত্তর।
2. **Global Riverpod provider** — tree-নিরপেক্ষ, তাই অবস্থান যাই হোক দুই screen একই provider `ref.watch` করে।
3. **Service locator (`get_it`)** — একটা singleton service register করুন, দুই screen সেটা নেয়। সহজ, কিন্তু UI update-এর জন্য এখনো একটা reactive layer (একটা stream বা notifier) লাগবে।
4. **Event bus / shared `StreamController`** — দুই screen একটাই stream শোনে। খুব decoupled, কিন্তু trace করা কঠিন।
5. **Navigator result / callback** — শুধু সহজ ক্ষেত্রে, যেখানে "Screen B, Screen A-কে একটা value ফেরত দেয়"।

**ধাপ ৩ — পরিষ্কার Riverpod version (tree-র উপর কোনো নির্ভরতা নেই)।**

```dart
final sharedCartProvider = NotifierProvider<CartNotifier, CartState>(CartNotifier.new);

// Screen A — tab 1-এর গভীরে
class OrdersScreen extends ConsumerWidget {
  const OrdersScreen({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final cart = ref.watch(sharedCartProvider);
    return Text('You have ${cart.items.length} items in cart');
  }
}

// Screen B — tab 2-এর গভীরে, সম্পূর্ণ সম্পর্ক নেই এমন
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

দুই screen **একই** provider instance ছোঁয়। তাই B-তে add করলে সাথে সাথে A update হয়।

**ধাপ ৪ — যে ফাঁদটা এড়াতে হবে।**
সাধারণ একটা global variable value share করে, কিন্তু UI-কে জানানোর কোনো উপায় তার নেই। তাই screen update হবে না। আপনার reactive কিছু লাগবে (একটা `ChangeNotifier`, bloc, বা Riverpod provider), খালি একটা static field নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা বাস্তব architecture প্রশ্ন। তাঁরা দেখতে চান আপনি scoping আর dependency injection-এর ভাষায় চিন্তা করেন কি না। পনেরোটা widget-এর ভেতর দিয়ে callback পাঠানোর ভাষায় নয়।

**সাধারণ ভুল:** কোনো reactivity ছাড়াই global mutable variable বা static singleton-এর দিকে হাত বাড়ানো — data বদলায় কিন্তু UI বদলায় না। আরেকটা: ভুল করে প্রতিটা screen-এ আলাদা controller instance তৈরি করা, ফলে প্রত্যেকের নিজের আলাদা state হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Provider-টা ঠিক কোথায় রাখবেন?"* → দুই screen-এর সবচেয়ে নিচের common ancestor-এ (প্রায়ই `MaterialApp`), অথবা Riverpod দিয়ে global-ভাবে।
- *"সাধারণ singleton কেন নয়?"* → এটা data ধরে রাখতে পারে, কিন্তু UI-কে জানাতে পারে না; একটা reactive wrapper লাগবে।

**সম্পর্কিত:** [Q4 — lifting state up](#q4) · [Q6 — Provider](#q6) · [Q13 — Riverpod](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q17"></a>17. একটা project-এর জন্য state management solution কীভাবে বাছাই করেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটাই সঠিক উত্তর নেই — এটা state আর team-এর উপর নির্ভর করে। একটা widget-এর ভেতরের local state-এর জন্য আমি `setState` ব্যবহার করি, বেশিরভাগ app-wide state-এর জন্য Provider বা Riverpod, আর কড়া architecture বা debounce-এর মতো জটিল event handling লাগলে BLoC। আর একই app-এ এগুলো মিশিয়ে ব্যবহার করা একদম ঠিক আছে। Senior দৃষ্টিভঙ্গি হলো trade-off বিচার করা — team-এর পরিচিতি, testability, জটিলতা — একটা tool-এর পক্ষে সাফাই গাওয়া নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা সহজ decision flow।**

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

**ধাপ ২ — যে বিষয়গুলো আসলে সিদ্ধান্ত নেয়।**
- **Team-এর পরিচিতি:** BLoC-তে দক্ষ একটা team, project-এর মাঝপথে নতুন tool শেখার চেয়ে BLoC দিয়েই দ্রুত ship করে।
- **Testability:** BLoC আর Riverpod খুব ভালোভাবে testable; GetX mock করা কঠিন।
- **App-এর জটিলতা:** একটা counter-এর জন্য BLoC লাগে না; একটা enterprise banking app এর structure থেকে লাভবান হয়।
- **Onboarding আর review:** BLoC স্পষ্ট বলে নতুনরা code সহজে পড়তে পারে; GetX-এর লুকানো জাদু বিভ্রান্ত করতে পারে।

**ধাপ ৩ — মেশানো শুধু allowed নয়, এটা বুদ্ধিমানের কাজ।**
**একই** app-এ প্রতিটা layer-এর জন্য সঠিক tool ব্যবহার করুন।

```dart
// Ephemeral UI state -> setState
class _DropdownState extends State<Dropdown> {
  bool _isOpen = false;
}

// জটিল auth flow -> BLoC
BlocProvider(create: (_) => AuthBloc(repo));

// সাধারণ theme value -> Riverpod StateProvider
final themeProvider = StateProvider<ThemeMode>((ref) => ThemeMode.system);

// মাঝারি জটিলতার cart -> Riverpod NotifierProvider
final cartProvider = NotifierProvider<CartNotifier, CartState>(CartNotifier.new);
```

**ধাপ ৪ — সমস্যার আকারের সাথে tool মিলিয়ে নিন।**
একটা toggle-এর জন্য BLoC আনবেন না, আর app-wide auth `setState` দিয়ে সামলাবেন না। Over-engineering আর under-engineering দুটোই red flag; সঠিক মাপ বুদ্ধি দেখায়।

**Interviewer কেন জিজ্ঞেস করে:** এটা senior-level প্রশ্ন। তাঁরা কোনো পক্ষপাতী উত্তর চান না — তাঁরা প্রমাণ চান যে আপনি trade-off বিচার করতে পারেন, team-এর অবস্থা ভাবতে পারেন, আর বাস্তবভাবে সিদ্ধান্ত নিতে পারেন।

**সাধারণ ভুল:** গোঁড়ামি নিয়ে একটা tool-এর পক্ষে সাফাই গাওয়া — "BLoC-ই একমাত্র professional পছন্দ" বা "Riverpod সবসময় ভালো" — এগুলো red flag। আরেকটা: কারণ ব্যাখ্যা না করেই ছোট app-এর জন্য ভারী tool বেছে নেওয়া (বা উল্টোটা)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"BLoC আর Riverpod কি মেশানো যায়?"* → হ্যাঁ — যেটা যেখানে মানায় সেটা ব্যবহার করুন; পুরো app-এ একটাই tool ব্যবহারের কোনো বাধ্যবাধকতা নেই।
- *"আজ একদম নতুন app-এর জন্য কী বাছবেন?"* → প্রায়ই app state-এর জন্য Riverpod, আর local UI-এর জন্য `setState`; team পছন্দ করলে বা domain event-ভারী হলে BLoC। উপরের বিষয়গুলো দিয়ে যুক্তি দিন।

**সম্পর্কিত:** [Q1 — state কী](#q1) · [Q9 — Cubit vs BLoC](#q9) · [Q13 — Riverpod](#q13) · [Q14 — GetX](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. BLoC / Cubit-এর state logic কীভাবে test করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-03-state-management.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি `bloc_test` package আর তার `blocTest` helper ব্যবহার করি। Pattern-টা এমন: `build` mock করা dependency দিয়ে bloc তৈরি করে, `act` একটা action চালায় — Bloc-এর জন্য একটা event add করা, Cubit-এর জন্য একটা method call করা — আর `expect` emit হওয়া state-গুলো ঠিক পরপর আসছে কি না assert করে। Dependency আছে এমন Bloc-এর ক্ষেত্রে আমি repository mock করি আর সেটা call হয়েছে কি না verify করি। মূল ফাঁদ হলো `blocTest` initial state বাদ দেয়, তাই আমি শুধু action-এর পরে emit হওয়া state-গুলো লিখি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Testability-ই কেন আসল কথা।**
Team-রা BLoC/Cubit বেছে নেয় মূলত এই কারণে যে logic UI থেকে আলাদা থাকে আর test করা সহজ। আপনি যদি দেখাতে না পারেন কীভাবে test করবেন, তাহলে সুবিধাটা শুধু কাগজেই থেকে যায়। তাই BLoC-এর কথা তুললেই এই প্রশ্নটা আশা করুন।

**ধাপ ২ — `blocTest`-এর গঠন।**

```
build:  () => CounterCubit()         <- create the instance
act:    (cubit) => cubit.increment() <- trigger an action
expect: () => [1]                    <- assert the emitted states
```

**ধাপ ৩ — একটা সাধারণ Cubit test করা।**

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

**ধাপ ৪ — mock করা dependency সহ একটা Bloc test করা।**
Repository mock করুন, একটা event চালান, তারপর state পরপর ঠিক আসছে কি না, আর repo call হয়েছে কি না — দুটোই assert করুন।

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

**ধাপ ৫ — অসুখী path-গুলোও test করুন।**
শুধু success test করবেন না। Failure test করুন, edge case test করুন (যেমন `close()`-এর পরে একটা method call করা), আর mock setup ভাগ করে নিতে `setUp`/`tearDown` ব্যবহার করুন। ভালো candidate-রা error-state-এর test দেখান, শুধু happy path নয়।

**Interviewer কেন জিজ্ঞেস করে:** Team-রা BLoC/Cubit বেছে নেওয়ার প্রধান কারণ testability। তাঁরা আশা করেন আপনি `blocTest`, mocking, আর state পরপর ঠিক আসছে কি না assert করা জানেন।

**সাধারণ ভুল:** `expect`-এ initial state রেখে দেওয়া। `blocTest` নিজে থেকেই এটা বাদ দেয়। তাই 0 থেকে শুরু হওয়া একটা counter-এর জন্য `expect: () => [0, 1]` লিখলে fail করবে — এটা হওয়া উচিত `[1]`। আরেকটা: শুধু happy path test করা আর error state বাদ দেওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Initial state `expect`-এ থাকে না কেন?"* → `blocTest` শুধু action-এর **পরে** emit হওয়া state record করে; initial state তো `super(...)` দিয়ে আগেই set হয়ে গেছে।
- *"Repository কীভাবে mock করেন?"* → `mocktail` বা `mockito` দিয়ে: `when(...)` দিয়ে method stub করি আর `verify(...)` দিয়ে call assert করি।

**সম্পর্কিত:** [Q8 — BLoC pattern](#q8) · [Q9 — Cubit](#q9) · [Q15 — sealed states](#q15)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিউ)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার table, তারপর এক লাইনের মনে করিয়ে দেওয়া পয়েন্ট।

## দ্রুত তুলনার table

**setState vs Provider vs Riverpod vs BLoC**

| | `setState` | Provider | Riverpod | BLoC / Cubit |
|---|---|---|---|---|
| কীসের জন্য ভালো | একটা widget-এর state | ছোট/মাঝারি app | নতুন app, সব আকারের | কড়া architecture, জটিল event |
| Boilerplate | নেই | কম | কম–মাঝারি | মাঝারি (BLoC), কম (Cubit) |
| Tree-এর উপর নির্ভর করে এমন? | হ্যাঁ | হ্যাঁ (`BuildContext`) | না (global) | হ্যাঁ (`BlocProvider`) |
| Testability | দুর্বল | ভালো | শক্তিশালী | শক্তিশালী |
| build-এ পড়া | widget-টি rebuild হয় | `context.watch` | `ref.watch` | `BlocBuilder` |
| একবারের জন্য পড়া | সরাসরি field | `context.read` | `ref.read` | `context.read<Bloc>()` |

**`context.watch` vs `read` vs `select`**

| | rebuild হয়? | কোথায় ব্যবহার |
|---|---|---|
| `watch` | যেকোনো পরিবর্তনে | `build`-এ |
| `select` | শুধু নির্বাচিত value বদলালে | `build`-এ |
| `read` | কখনোই না (একবার) | callback-এ |

**Cubit vs BLoC**

| Cubit | BLoC |
|---|---|
| method call করা | event object add করা |
| কম boilerplate | বেশি structure |
| event log নেই | প্রতিটা event traceable |
| transformer নেই | transformer দিয়ে debounce/throttle |

**BlocBuilder vs BlocListener vs BlocConsumer**

| Widget | কী করে |
|---|---|
| `BlocBuilder` | state বদলালে UI rebuild করে |
| `BlocListener` | একবারের side-effect (navigate, snackbar), rebuild নেই |
| `BlocConsumer` | rebuild আর side-effect দুটোই |

**`emit()` vs `setState()`**

| `setState()` | `emit()` |
|---|---|
| widget-এর `State`-এ | Cubit/Bloc-এ |
| এই widget rebuild করে | state stream-এ push করে |
| `mounted` দিয়ে guard করুন | `isClosed` দিয়ে guard করুন |

## এক লাইনের মনে করিয়ে দেওয়া

- **State** = যে data বদলায় আর screen-এ দেখা যায়। Ephemeral = একটা widget; app state = ভাগ করা। জিজ্ঞেস করুন "আর কার এটা লাগবে?" ([Q1](#q1))
- **`setState`** আপনার function চালায়, widget-কে dirty চিহ্ন দেয়, পরের frame-এ rebuild করে। Async কাজে `mounted` দিয়ে guard করুন। ([Q2](#q2))
- **State থাকে `State` object-এ**, widget-এ নয়। `initState`-এ সেট করুন, `dispose`-এ পরিষ্কার করুন। ([Q3](#q3))
- **Lifting state up** = state-টা সবচেয়ে কাছের common parent-এ সরান; prop drilling-এর কষ্টই state manager-এর জন্ম দেয়। ([Q4](#q4))
- **`InheritedWidget`** data নিচে পাঠায়; `updateShouldNotify` ঠিক করে dependent rebuild হবে কি না। এটাই Provider আর `Theme.of`-এর নিচে আছে। ([Q5](#q5))
- **Provider**: `ChangeNotifier` + `notifyListeners`। `Consumer` rebuild-এর সীমা ছোট করে; `Selector` একটা field বদলালে rebuild করে। ([Q6](#q6))
- **`watch`** build-এ (rebuild হয়), **`read`** callback-এ (একবার), **`select`** একটা value-র জন্য। Callback-এ `watch` করলে throw করে। ([Q7](#q7))
- **BLoC** = event ভেতরে → state-এর stream বাইরে। আধুনিক API: `on<Event>()` + `Emitter`। Logic UI-এর বাইরে থাকে। ([Q8](#q8))
- **Cubit** = event ছাড়া BLoC; method call করুন, state `emit` করুন। সহজ কাজে Cubit, জটিল/traceable কাজে Bloc। ([Q9](#q9))
- **Builder** rebuild করে, **Listener** একবারের কাজ করে, **Consumer** দুটোই করে। SnackBar যায় Listener-এ। ([Q10](#q10))
- **`buildWhen`/`listenWhen`** rebuild/effect ছেঁকে দেয়; default হলো সবসময় rebuild। Check-টা সস্তা রাখুন। ([Q11](#q11))
- **`close()`-এর পরে `emit` করলে throw করে** — `if (!isClosed)` দিয়ে guard করুন, widget-এর `mounted`-এর মতো। ([Q12](#q12))
- **Riverpod** provider global (tree নেই, "not found" crash নেই)। `ref.watch/read/listen`; `AsyncValue.when`; `autoDispose`। ([Q13](#q13))
- **GetX**: `.obs` + `Obx` নিজে থেকে rebuild করে, `GetBuilder` + `update()` হাতে করতে হয়। Boilerplate কম, কিন্তু global magic testing-এ ঝামেলা করে। ([Q14](#q14))
- **Sealed union state** অসম্ভব state-কে প্রকাশই করতে দেয় না আর exhaustive `switch` বাধ্য করে — `default` লাগে না। ([Q15](#q15))
- **সম্পর্ক নেই এমন screen-এর মধ্যে ভাগ করতে** দুটোরই উপরে তুলুন (common ancestor বা global Riverpod)। সাধারণ global variable কখনোই না। ([Q16](#q16))
- **Tool বাছাই** = team, testability, জটিলতা মিলিয়ে দেখা। Tool মেশানো ঠিক আছে। কখনোই গোঁড়া হবেন না। ([Q17](#q17))
- **`blocTest` দিয়ে test করুন**: `build` → `act` → `expect`। এটা initial state বাদ দেয়, তাই ওটা তালিকায় লিখবেন না। ([Q18](#q18))

[↑ উপরে ফিরুন](#toc)

---

# Practice: interviewer কীভাবে আরও গভীরে যায়

Interviewer সাধারণত একটা প্রশ্নে থামেন না। আপনার গভীরতা মাপতে তাঁরা খুঁড়তেই থাকেন। এই শিকলটা মুখে বলে অনুশীলন করুন — শান্তভাবে, ধাপে ধাপে:

1. *"একটা সহজ toggle কীভাবে manage করেন?"* → `setState`; এটা একটা widget-এর ephemeral state।
2. *"এখন login state সব screen-এ ভাগ করতে হবে — কী বদলাবে?"* → বাইরে তুলুন: দুই screen-এর উপরে একটা BLoC/Cubit বা একটা Riverpod provider।
3. *"এখানে `setState`-এর বদলে BLoC কেন?"* → ভাগ করা যায়, testable, logic UI-এর বাইরে; state এক দিকে বয় (event ভেতরে → state বাইরে)।
4. *"আপনি একটা login `await` করছেন, user চলে গেল — কোন bug আসবে?"* → close-এর পরে emit করলে `StateError` throw করে; `if (!isClosed)` দিয়ে guard করুন।
5. *"loading/success/error state কীভাবে model করবেন?"* → একটা sealed union, যাতে `switch` exhaustive হয় আর অসম্ভব state থাকতেই না পারে।
6. *"UI শুধু দরকারের সময়েই rebuild হয় — এটা কীভাবে প্রমাণ করবেন?"* → `buildWhen`/`Selector` দিয়ে সীমা বাঁধুন আর Flutter DevTools-এ "Track Widget Rebuilds" দেখুন।

এভাবে শান্তভাবে ধাপে ধাপে যেতে পারা — আন্দাজ না করে — এটাই আপনাকে **senior** শোনায়, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

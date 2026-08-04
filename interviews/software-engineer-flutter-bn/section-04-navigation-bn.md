# Section 4 — Navigation & Routing

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-04-navigation.md](../software-engineer-flutter/section-04-navigation.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code দিয়ে ধাপে ধাপে পুরো ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন আসে (**Very common / Common / Deeper**) আর তার difficulty কত (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তরটা** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন — "আরও গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলাটাই একটা senior skill — remote আর BD দুই ধরনের কোম্পানিতেই এটা একইভাবে কাজ করে।

---


## <a id="toc"></a>সূচিপত্র

**A. Navigator 1.0 (imperative stack)**
1. [Navigator 1.0 — stack, push/pop/pushReplacement/pushAndRemoveUntil/maybePop](#q1) · *Very common*
2. [`pop` দিয়ে data ফেরত পাঠানো আর result-এর জন্য অপেক্ষা করা](#q2) · *Common*
3. [Named routes — `onGenerateRoute` আর `MaterialApp.routes`](#q3) · *Common*

**B. Navigator 2.0 (declarative model)**
4. [Navigator 2.0 কেন আনা হলো — যে ৩টি সমস্যা এটা সমাধান করে](#q4) · *Very common*
5. [Navigator 2.0 internals — Router, RouteInformationParser, RouterDelegate](#q5) · *Deeper*

**C. go_router (production standard)**
6. [go_router-এর বেসিক — routes, subroutes, path আর query parameter](#q6) · *Very common*
7. [go_router-এ `go()` vs `push()` vs `replace()`](#q7) · *Very common*
8. [`redirect` আর `refreshListenable` দিয়ে auth / login guard](#q8) · *Very common*
9. [`ShellRoute` আর `StatefulShellRoute` — persistent bottom nav](#q9) · *Very common*
10. [Named routes vs typed routes (go_router_builder)](#q10) · *Common*
11. [Argument পাঠানো — নিরাপদ উপায় vs অনিরাপদ `extra`](#q11) · *Very common*
12. [404 / অজানা route handle করা](#q12) · *Common*

**D. বাস্তব জীবনের navigation সমস্যা**
13. [Deep linking — App Links (Android) আর Universal Links (iOS)](#q13) · *Common*
14. [`PopScope` — back button আটকানো](#q14) · *Very common*
15. [Widget tree-র বাইরে থেকে navigate করা (Cubit / service)](#q15) · *Common*
16. [Nested navigator — প্রতিটা tab-এর নিজের stack কেন দরকার](#q16) · *Common*
17. [Custom page transition / animation](#q17) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

১৭টা প্রশ্ন একসাথে পড়তে হবে না। এই পর্যায়গুলো একটার পর একটা শেষ করুন — প্রতিটা আগেরটার উপর দাঁড়ানো। একটা পর্যায় তখনই টিক দিন যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন।

**পর্যায় ১ — Stack-এর বেসিক (এখান থেকে শুরু করুন)।** প্রায় প্রতিটা interview এখান থেকেই শুরু হয়।
→ [Q1 Navigator 1.0 stack](#q1) · [Q2 pop দিয়ে data ফেরত](#q2) · [Q3 Named routes](#q3)

**পর্যায় ২ — Declarative routing কেন আছে।** এটা দেখায় আপনি *কেন*-টা বোঝেন।
→ [Q4 Navigator 2.0 কেন](#q4) · [Q6 go_router-এর বেসিক](#q6) · [Q7 go vs push vs replace](#q7)

**পর্যায় ৩ — আসল production pattern।** দৈনন্দিন কাজ দেখতে এমনই।
→ [Q8 Auth guard](#q8) · [Q9 Persistent bottom nav](#q9) · [Q11 Argument পাঠানো](#q11) · [Q14 PopScope](#q14)

**পর্যায় ৪ — Edge case আর মান।** এগুলোই শক্ত senior-দের আলাদা করে।
→ [Q10 Typed routes](#q10) · [Q12 404 routes](#q12) · [Q13 Deep linking](#q13) · [Q15 Tree-র বাইরে navigate](#q15) · [Q16 Nested navigator](#q16) · [Q17 Custom transition](#q17)

**পর্যায় ৫ — গভীর tie-breaker (সবার শেষে করুন)।** খুব কম মানুষ এটা পরিষ্কার করে বলতে পারে।
→ [Q5 Navigator 2.0 internals](#q5)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই আটটা রিভিশন দিন:
[Q1](#q1) · [Q4](#q4) · [Q6](#q6) · [Q7](#q7) · [Q8](#q8) · [Q9](#q9) · [Q11](#q11) · [Q14](#q14), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Navigator 1.0 (imperative stack)

---

## <a id="q1"></a>1. Navigator 1.0 ব্যাখ্যা করুন। Stack কীভাবে কাজ করে? `push`, `pop`, `pushReplacement`, `pushAndRemoveUntil`, আর `maybePop` ধাপে ধাপে বলুন।

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Navigator 1.0 screen-গুলোকে একটা stack-এ রাখে — last in, first out, ঠিক থালার স্তূপের মতো। `push` উপরে নতুন screen বসায়, `pop` উপরেরটা সরিয়ে দেয়। `pushReplacement` বর্তমান screen-টা বদলে নতুন একটা বসায়, আর `pushAndRemoveUntil` শর্ত না মেলা পর্যন্ত নিচের screen-গুলো মুছে দেয়। `maybePop` হলো নিরাপদ pop, যেটা root screen-এ ভুল করে app বন্ধ করে দেয় না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — থালার স্তূপের ধারণা।**
Navigation stack-কে একটা থালার স্তূপ ভাবুন। আপনি সবসময় উপরের থালাটাই আগে ধরেন। নতুন screen-টা উপরে থাকে, আর user সেটাই দেখে। পুরোনো screen-গুলো নিচে থাকে, memory-তে তখনও জীবিত।

```
Navigator stack (top = visible):

  ┌─────────────┐
  │  Screen C   │  ← top (on screen now)
  ├─────────────┤
  │  Screen B   │
  ├─────────────┤
  │  Screen A   │  ← bottom (the first/root screen)
  └─────────────┘
```

**ধাপ ২ — `push`: উপরে নতুন থালা বসানো।**
নতুন একটা screen উপরে যায়। পুরোনোটা নিচে থেকে যায়, অক্ষত অবস্থায়।

```dart
Navigator.push(
  context,
  MaterialPageRoute(builder: (_) => const DetailScreen()),
);
```

**ধাপ ৩ — `pop`: উপরের থালা সরানো।**
উপরের screen-টা সরে যায়, আর তার নিচেরটা আবার দেখা যায়।

```dart
Navigator.pop(context); // এক screen পেছনে যান
```

**ধাপ ৪ — `pushReplacement`: উপরের থালা বদলে ফেলা।**
এটা বর্তমান screen-টা সরিয়ে তার জায়গায় নতুন একটা বসায়। Stack-এর আকার একই থাকে। login → home-এর জন্য এটাই সঠিক টুল: login করার পরে user যেন back চেপে login screen-এ ফিরতে না পারে।

```dart
Navigator.pushReplacement(
  context,
  MaterialPageRoute(builder: (_) => const HomeScreen()),
);
```

**ধাপ ৫ — `pushAndRemoveUntil`: push করুন, তারপর নিচের থালাগুলো ফেলে দিন।**
এটা নতুন একটা screen push করে, আর একটা test "থামো" না বলা পর্যন্ত নিচের screen-গুলো সরিয়ে দেয়। নিচের *সবকিছু* সরাতে `(route) => false` পাঠান — "home-এ যাও আর পুরো stack পরিষ্কার করো" এর জন্য একদম মানানসই (যেমন logout-এর পরে)।

```dart
Navigator.pushAndRemoveUntil(
  context,
  MaterialPageRoute(builder: (_) => const HomeScreen()),
  (route) => false, // false = নতুনটার নিচের সব route মুছে দেয়
);
```

```
pushAndRemoveUntil with (route) => false:

BEFORE:                      AFTER:
┌─────────────┐
│  Screen D   │              ┌─────────────┐
├─────────────┤              │    Home     │  ← pushed (only this remains)
│  Screen C   │   ───────►   └─────────────┘
├─────────────┤
│  Screen B   │
├─────────────┤
│  Screen A   │
└─────────────┘
```

**ধাপ ৬ — `maybePop`: ভদ্র আর নিরাপদ pop।**
`maybePop` pop করার চেষ্টা করে। কিন্তু নিচে কিছু না থাকলে (মানে আমরা root screen-এ আছি) এটা app বন্ধ না করে কিছুই করে না। এটা `PopScope`-কেও মানে, তাই "unsaved changes" guard এখনও এটাকে আটকাতে পারে। Screen-টা pop করা যাবে কি না নিশ্চিত না হলে এটা ব্যবহার করুন।

```dart
Navigator.maybePop(context); // নিরাপদ: root-এ থাকলে app উড়িয়ে দেবে না
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি stack-কে একটা ধারণা হিসেবে বোঝেন কি না, শুধু কোন method-এর নাম লিখতে হবে সেটা নয়। "login cleanup" বা "সব মুছে ফেলা"-র জন্য সঠিক method বেছে নেওয়া senior signal।

**সাধারণ ভুল:** `pushReplacement` আর `pushAndRemoveUntil` গুলিয়ে ফেলা। `pushReplacement` শুধু *বর্তমান* screen-টা সরায় — নিচের সবকিছু থেকে যায়। `pushAndRemoveUntil` test true না দেওয়া পর্যন্ত সরাতেই থাকে। আরেকটা ভুল হলো `maybePop` বেশি নিরাপদ যেখানে সেখানে `pop` ব্যবহার করা (root screen-এ সরাসরি `pop` app-এর শেষ route-টাই pop করে দিতে পারে)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`pushAndRemoveUntil`-এর predicate মানে কী?"* → এটা নিচের প্রতিটা screen-এর উপর চালানো একটা test; যতক্ষণ এটা `false` দেয় ততক্ষণ pop চলতে থাকে, `true` দিলে থেমে যায়। `(route) => false` সবগুলোই সরিয়ে দেয়।
- *"Pop করা screen কি পরে আবার rebuild হয়?"* → Pop করা route dispose হয়ে যায়। যে route-এর উপরে push হয়েছে (মানে এখনও stack-এ আছে) সেটা জীবিত থাকে, rebuild হয় না।

**সম্পর্কিত:** [Q2 — pop দিয়ে data ফেরত](#q2) · [Q7 — go_router-এ go vs push](#q7) · [Q16 — nested navigator](#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. আগের screen-এ data কীভাবে ফেরত পাঠান? Navigation result await করা কীভাবে কাজ করে?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`Navigator.push` একটা `Future` return করে, যেটা screen pop হলে complete হয়। তাই আমি push-টা `await` করি। আর অন্য screen-এ `Navigator.pop(context, result)` call করে একটা value ফেরত পাঠাই। এটা কাউন্টারে অর্ডার দেওয়ার মতো: আপনি কাউন্টারে অপেক্ষা করেন, আর অন্য screen বন্ধ হলে value-টা ফিরে আসে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `push` আপনাকে একটা Future দেয়।**
একটা screen push করলে আপনি একটা `Future` ফেরত পান। নতুন screen খোলা থাকা অবস্থায় সেই Future অসম্পূর্ণ থাকে। ওই screen pop হওয়ার সাথে সাথে এটা একটা value নিয়ে complete হয়।

```dart
// একটা picker screen খুলুন আর user কী বাছল তার জন্য অপেক্ষা করুন
final selected = await Navigator.push<String>(
  context,
  MaterialPageRoute(builder: (_) => const PickColorScreen()),
);

// এই line চলবে শুধু PickColorScreen pop হওয়ার পরে
if (selected != null) {
  print('User picked $selected');
}
```

**ধাপ ২ — `pop` value-টা ফেরত পাঠায়।**
দ্বিতীয় screen-এ result-টা `pop`-এর দ্বিতীয় argument হিসেবে পাঠান। ওই value-ই await করা Future ফেরত দেয়।

```dart
// PickColorScreen-এর ভেতরে
ElevatedButton(
  onPressed: () => Navigator.pop(context, 'blue'), // 'blue' ফেরত পাঠান
  child: const Text('Pick blue'),
);
```

**ধাপ ৩ — "user back চেপেছে" ক্ষেত্রটা সামলান।**
User যদি swipe করে বা system back button চেপে বের হয় (আপনার button দিয়ে নয়), তাহলে কোনো value যায় না। তাই result হয় `null`। সবসময় `null`-এর জন্য পরিকল্পনা রাখুন।

```dart
final result = await Navigator.push<bool>(...);
final didConfirm = result ?? false; // back-press → "না" ধরে নিন
```

**ধাপ ৪ — go_router-এ একই ধারণা।**
go_router-এও এটা কাজ করে: `push` একটা Future return করে, আর `pop` একটা value বহন করতে পারে।

```dart
final result = await context.push<String>('/pick-color');
// picker screen-এ:
context.pop('blue');
```

**Interviewer কেন জিজ্ঞেস করে:** একটা screen থেকে value ফেরত আনা (picker, confirm dialog, edit form) রোজকার কাজ। তাঁরা দেখতে চান আপনি `await push` / `pop(value)` জোড়াটা জানেন কি না, আর back-press ক্ষেত্রটা সামলান কি না।

**সাধারণ ভুল:** User back করে বের হলে result `null` হতে পারে — এটা ভুলে যাওয়া। সবসময় value আছে ধরে নিয়ে পড়লে crash হয় বা logic ভুল হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`push` কোন type return করে?"* → `Future<T?>`, যেখানে `T` হলো আপনি `pop`-এ যে type পাঠান সেটা। এটা nullable, কারণ user কোনো value না পাঠিয়েই চলে যেতে পারে।
- *"`showDialog` কি একইভাবে কাজ করে?"* → হ্যাঁ। `showDialog<bool>(...)` একটা Future return করে, আর dialog-এর ভেতরে `Navigator.pop(context, true)` result-টা ফেরত পাঠায়।

**সম্পর্কিত:** [Q1 — push/pop-এর বেসিক](#q1) · [Q11 — সামনে argument পাঠানো](#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. Named routes কী? `MaterialApp.routes` আর `onGenerateRoute` কীভাবে কাজ করে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Named routes দিয়ে আমি `/details`-এর মতো একটা string name ব্যবহার করে navigate করতে পারি। প্রতিবার `MaterialPageRoute` বানাতে হয় না। সহজ route-গুলো আমি `MaterialApp.routes`-এ register করি। আর যখন argument পড়তে হয় বা screen dynamic ভাবে ঠিক করতে হয়, তখন `onGenerateRoute` ব্যবহার করি। go_router আসার আগে এটাই ছিল classic উপায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — নামের map (`routes`)।**
`MaterialApp.routes` একটা সাধারণ lookup table। একটা name একটা builder-এর সাথে map হয়। আপনি name দিয়ে navigate করেন।

```dart
MaterialApp(
  initialRoute: '/',
  routes: {
    '/': (context) => const HomeScreen(),
    '/settings': (context) => const SettingsScreen(),
  },
);

// name দিয়ে navigate:
Navigator.pushNamed(context, '/settings');
```

**ধাপ ২ — যে সমস্যা `routes` ভালোভাবে সমাধান করতে পারে না।**
`routes` map সহজে argument পড়তে পারে না। logic দেখে screen বেছে নিতেও পারে না (যেমন একটা অজানা id)। এর জন্য `onGenerateRoute` ব্যবহার করুন।

**ধাপ ৩ — `onGenerateRoute`: logic দিয়ে route বানান।**
`onGenerateRoute` একটাই function। এটা route settings (name + arguments) পায় আর একটা route return করে। কী build হবে সেটা আপনি ঠিক করেন।

```dart
MaterialApp(
  onGenerateRoute: (settings) {
    switch (settings.name) {
      case '/':
        return MaterialPageRoute(builder: (_) => const HomeScreen());
      case '/product':
        // pushNamed-এ পাঠানো argument পড়া হচ্ছে
        final id = settings.arguments as String;
        return MaterialPageRoute(builder: (_) => ProductScreen(id: id));
      default:
        // অজানা name → একটা সাধারণ 404 screen
        return MaterialPageRoute(builder: (_) => const NotFoundScreen());
    }
  },
);

// navigate করা আর একটা argument পাঠানো:
Navigator.pushNamed(context, '/product', arguments: '42');
```

**ধাপ ৪ — Argument নিরাপদে পড়া।**
`arguments` field-এর type হলো `Object?`। তাই এটা type-safe নয় — আপনাকে cast করতেই হবে। type ভুল হলে runtime-এ crash করবে। এই দুর্বলতাই go_router আর typed routes থাকার একটা বড় কারণ।

```dart
final args = settings.arguments;
if (args is String) {
  return MaterialPageRoute(builder: (_) => ProductScreen(id: args));
}
return MaterialPageRoute(builder: (_) => const NotFoundScreen());
```

**Interviewer কেন জিজ্ঞেস করে:** পুরোনো codebase আর ছোট app-এ named routes এখনো খুব চলে। তাঁরা দেখতে চান আপনি সহজ `routes` map আর বেশি flexible `onGenerateRoute` — দুটোই জানেন কি না। আর type-safety-র দুর্বলতাটা বোঝেন কি না।

**সাধারণ ভুল:** `routes` map-এ argument পড়ার logic রাখা (এটা argument-এ পরিষ্কারভাবে পৌঁছাতে পারে না)। Argument আছে এমন যেকোনো কিছুর জন্য `onGenerateRoute` ব্যবহার করুন। আরেকটা ভুল — `settings.arguments`-কে চোখ বন্ধ করে cast করা আর type ভুল হলে crash করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`onGenerateRoute` vs `onUnknownRoute`?"* → `onGenerateRoute` সব named push handle করে। `onUnknownRoute` শুধু তখনই fallback হিসেবে চলে যখন `onGenerateRoute` null return করে — 404 screen-এর জায়গা।
- *"go_router-এ কেন যাব?"* → Named routes string-ভিত্তিক আর untyped। এগুলো web URL বা deep link পরিষ্কারভাবে handle করে না। go_router এসব সব ঠিক করে দেয় ([Q6](#q6))।

**সম্পর্কিত:** [Q1 — Navigator 1.0](#q1) · [Q6 — go_router basics](#q6) · [Q10 — typed routes](#q10)

[↑ উপরে ফিরুন](#toc)

---

# B. Navigator 2.0 (declarative model)

---

## <a id="q4"></a>4. Navigator 2.0 কেন আনা হলো? এটা কোন সমস্যাগুলো সমাধান করে, যা Navigator 1.0 পারত না?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Navigator 1.0 imperative — আপনি একটা একটা করে হাতে push আর pop করেন। Deep link, web URL আর back button-এর ক্ষেত্রে এটা ভেঙে পড়ে। কারণ একটা URL থেকে পুরো stack আবার বানানোর পরিষ্কার উপায় নেই। Navigator 2.0 declarative: আপনি app state থেকে *পুরো* page stack বর্ণনা করেন, আর Flutter transition-গুলো বের করে নেয় — widget-এর `build()`-এর মতোই একই ধারণা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Imperative vs declarative (মূল ধারণা)।**
- **Navigator 1.0 (imperative):** আপনি ধাপে ধাপে হুকুম দেন — "push A, তারপর push B, তারপর push C।" Stack আপনি হাতে সামলান।
- **Navigator 2.0 (declarative):** আপনি শেষ ফলাফলটা বর্ণনা করেন — "stack হওয়া উচিত [A, B, C]" — আর Flutter সেখানে পৌঁছানোর উপায় বের করে।

```
Navigator 1.0 (imperative):
  Link tapped → you write: push(A); push(B); push(C);
  URL changed? You parse and push manually.

Navigator 2.0 (declarative):
  URL / state changed → you declare: "the stack is [A, B, C]"
  Flutter diffs the old and new stack and animates.
```

**ধাপ ২ — সমস্যা ১: deep linking।**
কোনো user যদি `myapp.com/products/42` খোলে, Navigator 1.0-এর কাছে পুরো path (Home → Products → Product 42) আবার বানানোর পরিষ্কার উপায় নেই। ঠিক order-এ কয়েকটা screen push করতে ঠুনকো manual code লিখতে হতো। Declarative routing URL থেকে পুরো stack নিজেই আবার বানায়।

**ধাপ ৩ — সমস্যা ২: web URL মিলিয়ে রাখা।**
Flutter web-এ browser-এর address bar বর্তমান screen-এর সাথে মিলতে হবে। আর URL edit করলে screen বদলাতে হবে। Navigator 1.0-এ stack আর URL-এর মধ্যে কোনো built-in যোগসূত্র নেই। তাই দুটো আলাদা হয়ে যায়। Navigator 2.0 URL আর stack-কে দুই দিক থেকেই জুড়ে দেয়।

**ধাপ ৪ — সমস্যা ৩: আগে থেকে বোঝা যায় এমন back navigation।**
Android-এর back button আর browser-এর back button সবসময় সঠিক কাজটাই করা উচিত। Navigator 1.0-এ "পুরো stack এটাই" বলে ঘোষণা করা একটাও জায়গা নেই, যেখানে ফিরে যাওয়া যায়। Navigator 2.0 সবসময় পুরো intended stack জানে। তাই back যেমন কাজ করার কথা, ঠিক তেমনই কাজ করে।

```dart
// Navigator 2.0 — declarative (ধারণাগত)
Navigator(
  pages: [
    const MaterialPage(child: HomeScreen()),
    if (selectedProductId != null)
      MaterialPage(child: ProductScreen(id: selectedProductId!)),
  ],
  onDidRemovePage: (page) {
    selectedProductId = null; // state update করুন; stack এখান থেকেই আবার তৈরি হয়
  },
);
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান একটা tool *কেন* আছে সেটা আপনি বোঝেন কি না — শুধু কীভাবে call করতে হয় তা নয়। তিনটা যন্ত্রণার জায়গা (deep link, web URL, back button) ব্যাখ্যা করলে architectural পরিপক্বতা দেখা যায়।

**সাধারণ ভুল:** বলা যে Navigator 2.0 Navigator 1.0-কে "replace" করেছে। করেনি — Navigator 1.0 এখনো বৈধ। সাধারণ mobile-only app-এর জন্য এটা সহজও। আরেকটা ভুল — Navigator 2.0-এর raw API আর go_router গুলিয়ে ফেলা। go_router হলো Navigator 2.0-এর *উপরে* বানানো একটা wrapper, যা কঠিন অংশগুলো লুকিয়ে রাখে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"বাস্তব app-এ আমি কি হাতে Navigator 2.0 লিখব?"* → প্রায় কখনোই না। সবাই এর উপরে go_router (বা এমন কোনো package) ব্যবহার করে।
- *"Navigator 1.0 কি মরে গেছে?"* → না। সহজ flow-এর ছোট mobile-only app-এর জন্য এটা একদম ঠিক আছে আর কাজও কম।

**সম্পর্কিত:** [Q5 — Navigator 2.0 internals](#q5) · [Q6 — go_router basics](#q6) · [Q13 — deep linking](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Navigator 2.0-এর মূল internals ব্যাখ্যা করুন — `Router`, `RouteInformationParser`, আর `RouterDelegate`। প্রতিটা কী করে?

> Deeper · Hard — a senior tie-breaker. · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Navigator 2.0-এ তিনটা অংশ আছে। এরা মিলে URL থেকে screen পর্যন্ত একটা pipeline বানায়। `RouteInformationParser` একটা URL string-কে আমার নিজের route object-এ বদলে দেয়। `RouterDelegate` হলো মাথা — এটা ওই object-কে page-এর একটা list-এ বদলায় আর `Navigator` build করে। `Router` widget এদের একসাথে জুড়ে দেয়। বাস্তব code-এ আমি go_router-কে দিয়েই তিনটাই implement করাই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Pipeline: URL ঢোকে, screen বের হয়।**
একটা assembly line কল্পনা করুন। এক দিক দিয়ে কাঁচা URL ঢোকে, অন্য দিক দিয়ে screen-এর একটা stack বের হয়।

```
Platform URL / deep link
          │
          ▼
┌──────────────────────────┐
│  RouteInformationParser  │  URL string  →  your route object
└──────────┬───────────────┘
           │  (route config)
           ▼
┌──────────────────────────┐
│      RouterDelegate      │  route object  →  List<Page> + builds Navigator
│        (the brain)       │  also handles pop and notifies on change
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│        Navigator         │  renders the real widget stack
└──────────────────────────┘
```

**ধাপ ২ — `RouteInformationParser`: URL অনুবাদ করে।**
এটা একটা `RouteInformation` (মূলত একটা URI) নেয়। তারপর আপনার বানানো app-specific config object return করে। উল্টো কাজটাও করে — আপনার config-কে আবার URL-এ বদলায়, যাতে browser bar update হয়।

```dart
class AppRouteParser extends RouteInformationParser<AppRoute> {
  @override
  Future<AppRoute> parseRouteInformation(RouteInformation info) async {
    final uri = info.uri;
    // /products/42 → AppRoute(productId: '42')
    if (uri.pathSegments.length == 2 && uri.pathSegments[0] == 'products') {
      return AppRoute(productId: uri.pathSegments[1]);
    }
    return AppRoute(); // home
  }

  @override
  RouteInformation? restoreRouteInformation(AppRoute config) {
    final path = config.productId == null ? '/' : '/products/${config.productId}';
    return RouteInformation(uri: Uri.parse(path));
  }
}
```

**ধাপ ৩ — `RouterDelegate`: যে মাথা stack বানায়।**
এটা navigation state ধরে রাখে। ঠিক `Page` object-এর list দিয়ে `Navigator` build করে। আর parser নতুন route দিলে সাড়া দেয়। মূল নিয়ম: navigation state বদলালেই `notifyListeners()` call করুন, নইলে UI update হবে না।

```dart
class AppRouterDelegate extends RouterDelegate<AppRoute>
    with ChangeNotifier, PopNavigatorRouterDelegateMixin<AppRoute> {

  String? _productId;

  @override
  final GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();

  @override
  AppRoute get currentConfiguration => AppRoute(productId: _productId);

  @override
  Future<void> setNewRoutePath(AppRoute config) async {
    _productId = config.productId; // parser আমাদের নতুন route দিল
  }

  @override
  Widget build(BuildContext context) {
    return Navigator(
      key: navigatorKey,
      pages: [
        const MaterialPage(child: HomeScreen()),
        if (_productId != null) MaterialPage(child: ProductScreen(id: _productId!)),
      ],
      onDidRemovePage: (page) {
        _productId = null;
        notifyListeners(); // Flutter-কে বলুন state বদলেছে
      },
    );
  }
}
```

**ধাপ ৪ — `Router`: সমন্বয়কারী (আপনি একে খুব কমই ছোঁন)।**
`Router` widget tree-র একদম উপরের দিকে বসে। এটা parser আর delegate-কে জুড়ে দেয়। সাধারণত আপনি এদের `MaterialApp.router(...)`-এ দিয়ে দেন। `Router` নিয়ে সরাসরি কিছু করতে হয় না।

```dart
MaterialApp.router(
  routerDelegate: AppRouterDelegate(),
  routeInformationParser: AppRouteParser(),
);
```

**ধাপ ৫ — এখানে go_router-এর কথা কেন বলবেন।**
তিনটা class হাতে লিখলে অনেক boilerplate হয়। ভুল হওয়াও সহজ। Production-এ go_router আপনার হয়ে parser আর delegate implement করে দেয়। Interview-তে senior চাল হলো — তিনটা ভূমিকা পরিষ্কার করে ব্যাখ্যা করা, তারপর বলা "এটাই go_router মুড়ে রাখে, তাই আমি go_router ব্যবহার করি।"

**Interviewer কেন জিজ্ঞেস করে:** এটা গভীরতা যাচাইয়ের প্রশ্ন। তাঁরা দেখতে চান আপনি architecture বোঝেন কি না (URL parse → state ঠিক করা → stack build করা)। boilerplate মুখস্থ করেছেন কি না, তা নয়।

**সাধারণ ভুল:** raw API-র প্রতিটা method মুখস্থ করার চেষ্টা করা। এর বদলে তিনটা ভূমিকা ব্যাখ্যা করুন। আর সৎভাবে বলুন যে আপনি go_router ব্যবহার করেন। আরেকটা চেনা ভুল — ভুলে যাওয়া যে state বদলালে `RouterDelegate`-কে `notifyListeners()` call করতেই হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`currentConfiguration` কীসের জন্য?"* → এভাবেই delegate বর্তমান route-টা ফিরিয়ে জানায়, যাতে URL মিলিয়ে update করা যায়।
- *"go_router এখানে কোথায় বসে?"* → এটা তৈরি করা parser আর delegate দেয়। ফলে আপনাকে শুধু একটা route table লিখতে হয়।

**সম্পর্কিত:** [Q4 — Navigator 2.0 কেন](#q4) · [Q6 — go_router basics](#q6)

[↑ উপরে ফিরুন](#toc)

---

# C. go_router (the production standard)

---

## <a id="q6"></a>6. go_router কীভাবে কাজ করে? route declaration, subroutes, path parameters আর query parameters ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"go_router হলো Navigator 2.0-এর উপরে বানানো একটা declarative routing package। আমি আমার পুরো route tree একবারে `GoRoute` object-এর একটা list হিসেবে declare করি। এরপর সে নিজেই URL parsing, deep link আর browser-URL sync সামলায়। Path parameter-এর জন্য path-এ `:name` লিখতে হয়। Query parameter declare করতে হয় না, ওগুলো `GoRouterState` থেকে আসে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Route একটা tree, ঠিক folder structure-এর মতো।**
আপনি route-গুলো tree হিসেবে declare করেন। Child route যায় parent-এর `routes` list-এ। আর তাদের path নিজে থেকেই parent-এর path-এর সাথে *যোগ* হয়ে যায়।

```
Route tree:

  /                          → HomeScreen
  ├── products               → ProductListScreen      (/products)
  │   └── :productId         → ProductDetailScreen     (/products/:productId)
  │       └── reviews        → ReviewsScreen           (/products/:productId/reviews)
  └── settings               → SettingsScreen          (/settings)
```

**ধাপ ২ — Tree-টা declare করুন।**
প্রতিটা `GoRoute`-এ একটা `path` আর একটা `builder` থাকে। Subroute বসে `routes`-এর ভেতরে।

```dart
final router = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => const HomeScreen(),
      routes: [
        GoRoute(
          path: 'products', // child path relative → হয়ে যায় /products
          builder: (context, state) => const ProductListScreen(),
          routes: [
            GoRoute(
              path: ':productId', // path parameter → /products/:productId
              builder: (context, state) {
                final id = state.pathParameters['productId']!;
                return ProductDetailScreen(id: id);
              },
            ),
          ],
        ),
        GoRoute(
          path: 'settings',
          builder: (context, state) => const SettingsScreen(),
        ),
      ],
    ),
  ],
);

MaterialApp.router(routerConfig: router);
```

**ধাপ ৩ — Path parameter (`:name`): ঠিকানার একটা অংশ।**
Path parameter হলো URL-এর ভেতরের একটা খালি জায়গা। এটা required — না থাকলে route match-ই করবে না। এটা পড়ুন `state.pathParameters` থেকে।

```dart
context.go('/products/42'); // 42 বসে :productId slot-এ
// builder-এর ভেতরে:
final id = state.pathParameters['productId']!; // '42'
```

**ধাপ ৪ — Query parameter (`?key=value`): বাড়তি optional জিনিস।**
Query parameter আসে `?`-এর পরে। এগুলো declare করতে হয় না, আর সাধারণত optional — যেমন filter বা sorting। এগুলো পড়ুন `state.uri.queryParameters` থেকে।

```dart
context.go('/products?sort=price&category=phones');
// builder-এর ভেতরে:
final sort = state.uri.queryParameters['sort'];         // 'price'
final category = state.uri.queryParameters['category']; // 'phones'
```

সহজ একটা নিয়ম: **path parameter বলে *কোন* জিনিস** (কোন product), **query parameter বলে *কীভাবে* দেখবেন** (sorting, filtering)। দুটোই সাধারণ string। তাই web page refresh আর deep link-এও দুটোই টিকে থাকে।

**Interviewer কেন জিজ্ঞেস করে:** আজকের দিনে Flutter routing-এর কার্যত standard হলো go_router। তাঁরা দেখতে চান আপনি পরিষ্কার একটা route tree design করতে পারেন কি না। আর path আর query parameter-এর পার্থক্য জানেন কি না।

**সাধারণ ভুল:** Subroute-এর path-এ শুরুতে slash বসানো (`'products'`-এর বদলে `'/products'`)। শুরুর slash দিলে সেটা top-level route হয়ে যায়, child নয়। তখন nesting ভেঙে পড়ে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এখানে `pathParameters['productId']` non-null কেন?"* → কারণ ওই segment থাকলে তবেই route match করে। তাই parameter-টা থাকবেই (এই জন্যই `!`)।
- *"Query parameter কোথায় থাকে?"* → `state.uri.queryParameters`-এ, `pathParameters`-এ নয়।

**সম্পর্কিত:** [Q7 — go vs push](#q7) · [Q11 — argument পাঠানো](#q11) · [Q12 — 404 route](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. go_router-এ `go()`, `push()`, আর `replace()`-এর মধ্যে পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`go()` declarative — এটা পুরো stack আবার বানায় target URL-এর সাথে মেলানোর জন্য। `push()` imperative — এটা বর্তমান stack-এর উপরে একটা screen যোগ করে, ঠিক Navigator 1.0-এর মতো। `replace()` উপরের screen-টা বদলে নতুন একটা বসায়, stack বড় হয় না। আমি সাধারণ navigation-এ `go()` ব্যবহার করি। আর `push()` তখনই, যখন একটা screen উপরে স্তরের মতো বসাতে চাই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `go()`: URL থেকে পুরো stack ঠিক করে দেয়।**
`go('/products/42')` go_router-কে বলে — "stack এখন এই URL-এর সাথে মিলবে।" go_router সেটা আবার বানায় Home → Products → Product 42 হিসেবে। এটাই declarative, URL-first উপায়। এটাই web-এ browser bar ঠিক রাখে।

```dart
context.go('/products/42'); // stack হয়ে যায় Home → Products → Product 42
```

**ধাপ ২ — `push()`: উপরে একটা screen বসায়।**
`push('/products/42')` stack আবার বানায় না। যা দেখাচ্ছে তার উপরে শুধু ওই একটা screen যোগ করে — একদম Navigator 1.0-এর `push`-এর মতো। বর্তমান flow-এর "উপরে" বসে থাকা জিনিসের জন্য এটা ব্যবহার করুন। যেমন একটা detail screen, যেখান থেকে pop করে ঠিক আগের জায়গায় ফেরা যায়।

```dart
context.push('/products/42'); // বর্তমান stack-এর উপরে Product 42 যোগ হয়
final result = await context.push<bool>('/confirm'); // value-ও return করতে পারে
```

**ধাপ ৩ — `replace()`: উপরের screen বদলে দেয়।**
`replace()` বর্তমান উপরের screen সরিয়ে সেখানে নতুনটা বসায়। Stack-এর আকার একই থাকে, নতুন কোনো history entry যোগ হয় না। login → home-এর জন্য এটা ভালো, যেখানে back চেপে login-এ ফেরা উচিত নয়।

```dart
context.replace('/home'); // বর্তমান screen বদলে /home বসে
```

**ধাপ ৪ — মনে রাখার জন্য সহজ একটা টেবিল।**

| Method | কী করে | Stack-এ প্রভাব | কখন |
|---|---|---|---|
| `go()` | URL-এর সাথে মেলাতে stack আবার বানায় | matched tree-তে reset হয় | সাধারণ navigation, web URL, deep link |
| `push()` | উপরে একটা screen যোগ করে | stack একটা বাড়ে | স্তরের মতো screen, যেখান থেকে pop করে ফিরবেন |
| `replace()` | উপরের screen বদলায় | stack-এর আকার একই থাকে | login → home, পুরোনো screen-এ back নেই |

**ধাপ ৫ — `push()`-এর web সমস্যা।**
Web-এ `push()` এমন একটা screen যোগ করে, যেটা URL দিয়ে পুরোপুরি বোঝানো যায় না। User refresh করলে ওই push করা screen হারিয়ে যেতে পারে। কারণ শুধু URL দিয়ে সেটা আবার বানানো যায় না। Web-এ URL-চালিত screen-এর জন্য `go()` বেছে নিন।

**Interviewer কেন জিজ্ঞেস করে:** `go()` আর `push()`-এর ভুল বাছাই go_router-এর সবচেয়ে সাধারণ bug-গুলোর একটা। তাঁরা দেখতে চান আপনি "declarative stack rebuild" আর "imperative add on top"-এর পার্থক্য বোঝেন কি না।

**সাধারণ ভুল:** Navigator 1.0-এর মতো সব জায়গায় `push()` ব্যবহার করা। তারপর অবাক হওয়া যে browser URL বদলাচ্ছে না, বা back অদ্ভুত আচরণ করছে। সাধারণ navigation-এর জন্য `go()`-ই সাধারণত সঠিক default।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`Named` version-গুলোর কী হবে?"* → `goNamed`, `pushNamed`, `replaceNamed` একই কাজ করে। শুধু raw path-এর বদলে route name আর parameter নেয় ([Q10](#q10))।
- *"`push()` কি value return করে?"* → হ্যাঁ, `context.push<T>(...)` একটা Future return করে। আপনি `context.pop(value)` করলে সেটা complete হয় ([Q2](#q2))।

**সম্পর্কিত:** [Q1 — Navigator 1.0 push/pop](#q1) · [Q6 — go_router basics](#q6) · [Q11 — argument পাঠানো](#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. go_router-এর `redirect` দিয়ে auth / login guard কীভাবে implement করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"go_router-এর `redirect` callback প্রতিটা navigation-এর আগে চলে। এটা `null` return করলে navigation চলতে দেয়। আর নতুন একটা path return করলে user-কে অন্য জায়গায় পাঠায়। Auth guard-এর জন্য এটাই সঠিক জায়গা: user logged in না থাকলে `/login` return করি। Auth বদলালে (যেমন logout) সাড়া দেওয়ার জন্য আমি `refreshListenable` যুক্ত করি, যাতে redirect আবার চলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দরজায় দাঁড়ানো bouncer।**
`redirect`-কে ভাবুন একজন bouncer হিসেবে, যে ঢোকার আগে সবাইকে check করে। অনুমতি থাকলে সে হাত নেড়ে ঢুকতে দেয় (`return null`)। না থাকলে সে অন্য জায়গায় পাঠিয়ে দেয় (`return '/login'`)।

```
User navigates to /dashboard
          │
          ▼
   redirect() runs
   logged in?  ── no ──►  return '/login'
          │ yes
          ▼
   return null (allow)  →  DashboardScreen shows
```

**ধাপ ২ — সাধারণ guard।**
আপনার auth state পড়ুন, তারপর সিদ্ধান্ত নিন। সবচেয়ে গুরুত্বপূর্ণ বিষয়: `/login` screen-টাকেও অনুমতি দিতে হবে। না হলে একটা অসীম loop তৈরি হবে।

```dart
final router = GoRouter(
  initialLocation: '/',

  // প্রতিটা navigation-এ চলে
  redirect: (context, state) {
    final loggedIn = context.read<AuthCubit>().state.isAuthenticated;
    final goingToLogin = state.matchedLocation == '/login';

    // logged in নয়, আর login-এও যাচ্ছে না → login-এ পাঠান
    if (!loggedIn && !goingToLogin) {
      return '/login?from=${state.matchedLocation}'; // কোথায় যেতে চেয়েছিল মনে রাখুন
    }
    // আগেই logged in, তবু login-এ যাচ্ছে → home-এ পাঠান
    if (loggedIn && goingToLogin) {
      return '/';
    }
    return null; // অনুমতি
  },

  routes: [
    GoRoute(path: '/', builder: (_, __) => const HomeScreen()),
    GoRoute(
      path: '/login',
      builder: (_, state) {
        final from = state.uri.queryParameters['from'] ?? '/';
        return LoginScreen(redirectTo: from);
      },
    ),
    GoRoute(path: '/dashboard', builder: (_, __) => const DashboardScreen()),
  ],
);
```

**ধাপ ৩ — আসল গন্তব্য মনে রাখুন।**
`?from=...` অংশটা খেয়াল করুন। Logged-out একজন user `/dashboard` খুলতে চাইলে আপনি তাকে login-এ পাঠান। কিন্তু সে কোথায় যেতে চেয়েছিল সেটা জমা রাখেন। Login সফল হলে তাকে সেখানেই ফেরত পাঠান।

```dart
void onLoginSuccess(BuildContext context, String from) {
  context.go(from); // যে page-এ যেতে চেয়েছিল সেখানে ফেরত
}
```

**ধাপ ৪ — `refreshListenable` দিয়ে auth পরিবর্তনে সাড়া দিন।**
`redirect` চলে navigation-এর সময়। কিন্তু user একটা screen-এ বসে থাকা অবস্থায় তার token expire হলে কী হবে? আপনার auth source বদলালেই `refreshListenable` redirect আবার চালায়। ফলে logout হলে সাথে সাথে তাকে login-এ পাঠিয়ে দেয়।

```dart
final router = GoRouter(
  refreshListenable: GoRouterRefreshStream(authCubit.stream), // auth বদলালে redirect আবার চলবে
  redirect: (context, state) {
    // ধাপ ২-এর মতোই logic
  },
  routes: [ /* ... */ ],
);
```

`GoRouterRefreshStream` (go_router-এর সাথেই আসে) যেকোনো `Stream`-কে একটা `Listenable`-এ মুড়ে দেয়, যেটা go_router নজরে রাখে।

**Interviewer কেন জিজ্ঞেস করে:** Auth guard করা সব app-এরই দরকার। তাঁরা দেখেন আপনি কঠিন অংশগুলো সামলান কি না: অসীম redirect loop এড়ানো, আসল গন্তব্য মনে রাখা, আর logout-এ সাড়া দেওয়া।

**সাধারণ ভুল:** `goingToLogin` check ভুলে যাওয়া, যেটা একটা অসীম loop বানায় — redirect আপনাকে `/login`-এ পাঠায়, সেটা আবার redirect চালায়, এভাবে চলতেই থাকে। আরেকটা ভুল, `refreshListenable` বাদ দেওয়া। তখন token expire হলে router কোনো সাড়া দেয় না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Top level ছাড়া redirect আর কোথায় রাখা যায়?"* → একটা একক `GoRoute`-এও (route-level `redirect`), শুধু ওই branch-টা guard করার জন্য।
- *"এক বাক্যে loop কীভাবে এড়াবেন?"* → target `/login` হলে `null` return করে login page-এ যাওয়াটা *সবসময়* অনুমতি দিন।

**সম্পর্কিত:** [Q12 — অজানা route](#q12) · [Q9 — shell route](#q9) · [Q15 — tree-এর বাইরে থেকে navigate](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. go_router-এর `ShellRoute` কী? Persistent bottom navigation bar কীভাবে বানাবেন, আর `StatefulShellRoute` কীভাবে আলাদা?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`ShellRoute` child route-গুলোকে একটা shared shell-এর ভেতরে মুড়ে দেয় — সাধারণত একটা `Scaffold` যার bottom bar আছে। ফলে শুধু body বদলায়, bar জায়গায় থেকে যায়। কিন্তু সাধারণ `ShellRoute` একটাই stack share করে। তাই tab বদলালে প্রতিটা tab-এর state হারিয়ে যায়। `StatefulShellRoute.indexedStack` প্রতিটা tab-কে নিজের আলাদা stack দেয়। এটা scroll position আর history ধরে রাখে। বাস্তব app-গুলো এটাই ব্যবহার করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ছবির ফ্রেমের ধারণা।**
Shell হলো ছবির ফ্রেমের মতো। ফ্রেম (bottom bar) স্থির থাকে। শুধু ভেতরের ছবিটা (page) বদলায় যখন আপনি tab বদলান।

```
ShellRoute layout:

┌────────────────────────────┐
│                            │
│     child route content    │  ← changes when navigating
│                            │
├────────────────────────────┤
│  Home  │ Search │ Profile  │  ← persistent shell, doesn't rebuild
└────────────────────────────┘
```

**ধাপ ২ — সাধারণ একটা `ShellRoute`।**
`builder` বর্তমান child পায়। তারপর সেটাকে আপনার shell widget-এর ভেতরে মুড়ে দেয়।

```dart
final router = GoRouter(
  initialLocation: '/home',
  routes: [
    ShellRoute(
      builder: (context, state, child) => ScaffoldWithNav(child: child),
      routes: [
        GoRoute(path: '/home', builder: (_, __) => const HomeScreen()),
        GoRoute(path: '/search', builder: (_, __) => const SearchScreen()),
        GoRoute(path: '/profile', builder: (_, __) => const ProfileScreen()),
      ],
    ),
    // shell-এর বাইরের route-এ কোনো bottom bar নেই (login-এর জন্য ভালো)
    GoRoute(path: '/login', builder: (_, __) => const LoginScreen()),
  ],
);
```

**ধাপ ৩ — সাধারণ `ShellRoute`-এর দুর্বলতা।**
সাধারণ `ShellRoute` *একটাই* navigation stack রাখে। তাই Home-এ scroll করে নিচে গিয়ে Search-এ গেলেন, তারপর ফিরে এলেন — Home reset হয়ে যাবে। প্রতিটা tab নিজের state বা নিজের গভীর screen মনে রাখে না।

**ধাপ ৪ — `StatefulShellRoute.indexedStack`: প্রতি tab-এ আলাদা stack।**
এটা প্রতিটা tab-কে নিজের branch দেয়, আর সেই branch-এর নিজের `Navigator` থাকে। Tab-গুলো একটা `IndexedStack`-এ জীবিত থাকে। ফলে scroll position আর history ধরে থাকে। আপনি `navigationShell.goBranch(index)` দিয়ে tab বদলান।

```dart
StatefulShellRoute.indexedStack(
  builder: (context, state, navigationShell) {
    return Scaffold(
      body: navigationShell, // active branch দেখায়
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: navigationShell.currentIndex,
        onTap: (index) => navigationShell.goBranch(
          index,
          // active tab-এ আবার tap করলে সেটা root-এ reset হয়
          initialLocation: index == navigationShell.currentIndex,
        ),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
        ],
      ),
    );
  },
  branches: [
    StatefulShellBranch(routes: [
      GoRoute(
        path: '/home',
        builder: (_, __) => const HomeScreen(),
        routes: [
          GoRoute(
            path: 'detail/:id',
            builder: (_, state) => HomeDetailScreen(id: state.pathParameters['id']!),
          ),
        ],
      ),
    ]),
    StatefulShellBranch(routes: [
      GoRoute(path: '/search', builder: (_, __) => const SearchScreen()),
    ]),
    StatefulShellBranch(routes: [
      GoRoute(path: '/profile', builder: (_, __) => const ProfileScreen()),
    ]),
  ],
);
```

**ধাপ ৫ — কোনটা বেছে নেবেন।**
- **সাধারণ `ShellRoute`** → একটাই shared stack। Tab-গুলোর নিজের deep state মনে রাখার দরকার না হলে এটা ঠিক আছে।
- **`StatefulShellRoute.indexedStack`** → প্রতি tab-এ আলাদা stack। ক্লাসিক Instagram/YouTube ধরনের bottom nav-এর জন্য এটা ব্যবহার করুন, যেখানে প্রতিটা tab নিজের history আর scroll ধরে রাখে।

**Interviewer কেন জিজ্ঞেস করে:** প্রায় প্রতিটা production app-এ bottom nav bar থাকে। তাঁরা দেখতে চান আপনি shared shell আর per-tab state preservation-এর পার্থক্য জানেন কি না।

**সাধারণ ভুল:** Per-tab memory দরকার হলেও সাধারণ `ShellRoute` ব্যবহার করা। তারপর অবাক হওয়া যে tab বদলানোর পরে Home কেন reset হয়। সমাধান হলো `StatefulShellRoute.indexedStack`। আরেকটা ভুল হলো login route-টা shell-এর *ভেতরে* রাখা, যাতে login screen-এও ভুল করে bottom bar দেখা যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ভেতরে `IndexedStack` কেন?"* → এটা সব tab widget জীবিত রাখে (শুধু লুকানো থাকে)। তাই tab বদলালেও তাদের state আর scroll টিকে থাকে। সাধারণ conditional rebuild হলে সেগুলো নষ্ট হয়ে যেত।
- *"একটা tab-কে root-এ কীভাবে reset করবেন?"* → Tap করা tab-টা যদি আগে থেকেই active হয়, তাহলে `goBranch`-এ `initialLocation: true` পাঠান।

**সম্পর্কিত:** [Q16 — nested navigators](#q16) · [Q6 — go_router basics](#q6) · [Q8 — shell-এর বাইরে auth guard](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. Named routes আর typed routes (go_router_builder)-এর মধ্যে পার্থক্য কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Named routes একটা string name আর parameter-এর map দিয়ে navigate করে — সহজ, কিন্তু একটা typo বা missing parameter শুধু runtime-এ ধরা পড়ে। Typed routes `go_router_builder` package ব্যবহার করে: আপনি route class লেখেন, `build_runner` চালান, আর generated compile-time-safe navigation পান। ছোট app-এর জন্য named routes ঠিক আছে। বড় codebase-এ typed routes অনেক বেশি কাজে দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Named routes: string name দিয়ে navigate করা।**
প্রতিটা `GoRoute`-কে একটা `name` দিন। তারপর `goNamed` দিয়ে navigate করুন। কাঁচা path-এর চেয়ে এটা কম ঠুনকো (path বদলালেও caller ভাঙে না), কিন্তু এটা এখনো string-নির্ভর।

```dart
GoRoute(
  name: 'product',
  path: '/products/:id',
  builder: (context, state) => ProductScreen(id: state.pathParameters['id']!),
);

// navigate — string name, parameter map-এ (compile-time check নেই)
context.goNamed('product', pathParameters: {'id': '42'});
```

**ধাপ ২ — দুর্বলতা: error runtime পর্যন্ত লুকিয়ে থাকে।**
আপনি যদি `'prodcut'` লিখে ফেলেন, বা `id` parameter দিতে ভুলে যান, code লেখার সময় কেউ কিছু বলবে না। User button-এ tap করলে তখন ভাঙবে।

```
Named routes:
  context.goNamed('product', pathParameters: {'id': '42'})
  → typo the name or forget 'id'? crashes at RUNTIME

Typed routes:
  const ProductRoute(id: '42').go(context)
  → anything wrong? error at COMPILE time
```

**ধাপ ৩ — Typed routes: compiler-কে দিয়ে check করান।**
`go_router_builder` দিয়ে প্রতিটা route-কে একটা class হিসেবে লেখেন, যার উপরে `@TypedGoRoute` annotation থাকে। একটা code generator সেটাকে type-safe navigation method-এ বদলে দেয়।

```dart
// Step 1: route-টা class হিসেবে লিখুন
@TypedGoRoute<ProductRoute>(path: '/products/:id')
class ProductRoute extends GoRouteData with _$ProductRoute {
  final String id;
  const ProductRoute({required this.id});

  @override
  Widget build(BuildContext context, GoRouterState state) =>
      ProductScreen(id: id);
}

// Step 2: code generate করুন
//   dart run build_runner build

// Step 3: navigate — পুরো type-safe, compiler 'id' দিতে বাধ্য করে
const ProductRoute(id: '42').go(context);
```

**ধাপ ৪ — Trade-off (এটাই senior উত্তর)।**
Typed routes-এর জন্য `build_runner` setup লাগে, একটা generated file থাকে, আর প্রতি route-এ বেশি boilerplate লাগে। ছোট app-এর জন্য এটা বাড়াবাড়ি। বড় team-এ যেখানে route প্রায়ই বদলায় আর একটা typo-র খরচ অনেক, সেখানে compile-time safety লাভজনক।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি type safety আর maintainability নিয়ে ভাবেন কি না। আর আপনি একটা approach-কে "সবসময় সেরা" না বলে trade-off ওজন করতে পারেন কি না।

**সাধারণ ভুল:** বলা যে typed routes "সব দিক থেকেই ভালো"। এর জন্য build_runner-এর বাড়তি খরচ আর boilerplate দিতে হয়। ছোট-মাঝারি project-এ named routes একদম ঠিক আছে। সঠিক উত্তর trade-off-টা বলে দেয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`go_router_builder` কী generate করে?"* → Extension method আর route class, যেগুলো সঠিক path বানায় আর parameter পড়ে নেয়। ফলে navigation compile time-এ check হয়।
- *"দুটো একসাথে মেশানো যায়?"* → যায়, কিন্তু consistency-র জন্য project-এ একটা style বেছে নিন। মেশালে team বিভ্রান্ত হয়।

**সম্পর্কিত:** [Q3 — Navigator 1.0-এ named routes](#q3) · [Q6 — go_router basics](#q6) · [Q11 — argument পাঠানো](#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. Screen-এর মধ্যে argument কীভাবে পাঠাবেন? নিরাপদ (typed) উপায় আর অনিরাপদ উপায় কোনটা?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"নিরাপদ উপায় হলো path আর query parameter, কারণ সেগুলো URL-এ থাকে — web refresh-এও টিকে যায় আর deep link-এ কাজ করে। অনিরাপদ উপায় হলো go_router-এর `extra`। এটা যেকোনো object বহন করতে পারে, কিন্তু শুধু memory-তে থাকে। তাই web refresh-এ হারিয়ে যায় আর deep link ভেঙে যায়। সবচেয়ে নিরাপদ হলো typed routes, যেখানে compiler argument দিতে বাধ্য করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — অনিরাপদ উপায়: `extra`।**
`state.extra`-র type হলো `Object?`। তাই আপনি যেকোনো object পাঠাতে পারেন। শুনতে সুবিধাজনক, কিন্তু ৩টি সমস্যা আছে: একটা ঝুঁকির cast লাগে, এটা URL-এ থাকে না, আর এটা শুধু memory-তে ধরা থাকে।

```dart
// যেকোনো object পাঠানো
context.go('/detail', extra: Product(id: 42, name: 'Widget'));

// receive করা — cast করতেই হবে, crash হতে পারে
GoRoute(
  path: '/detail',
  builder: (context, state) {
    final data = state.extra as Product; // null বা ভুল type হলে crash
    return DetailScreen(data: data);
  },
);
// সমস্যা:
//   1. extra null বা ভুল type হলে cast throw করে
//   2. web page refresh-এ হারিয়ে যায় (extra শুধু memory-তে)
//   3. URL-এ নেই → এই screen-এ deep linking কাজ করবে না
```

**ধাপ ২ — নিরাপদ উপায়: path আর query parameter।**
এগুলো সবসময় string, আর URL-এ থাকে। তাই refresh আর deep link-এও টিকে যায়। পরিচয়ের জন্য path parameter ব্যবহার করুন, বাড়তি জিনিসের জন্য query parameter।

```dart
context.go('/products/42?name=Widget');

GoRoute(
  path: '/products/:id',
  builder: (context, state) {
    final id = state.pathParameters['id']!;          // সবসময় String
    final name = state.uri.queryParameters['name'];  // nullable String
    return ProductScreen(id: id, name: name);
  },
);
// Web refresh-এ টিকে যায় আর deep link-এ কাজ করে।
```

**ধাপ ৩ — সবচেয়ে নিরাপদ উপায়: typed routes।**
`go_router_builder` দিয়ে argument-গুলো আসল constructor field হয়ে যায়। Compiler আপনাকে required field পাঠাতে বাধ্য করে। আর field-গুলো নিজে থেকেই path/query parameter-এ map হয়।

```dart
@TypedGoRoute<ProductRoute>(path: '/products/:id')
class ProductRoute extends GoRouteData with _$ProductRoute {
  final String id;
  final String? name; // নিজে থেকেই query parameter হয়ে যায়
  const ProductRoute({required this.id, this.name});

  @override
  Widget build(BuildContext context, GoRouterState state) =>
      ProductScreen(id: id, name: name);
}

// compiler required 'id' দিতে বাধ্য করে
const ProductRoute(id: '42', name: 'Widget').go(context);
```

**ধাপ ৪ — `extra` কখন গ্রহণযোগ্য?**
শুধু mobile-only flow-এ, যেখানে object-টা serialize করার মতো দামি নয় আর screen-টা কখনো deep-link হয় না — যেমন, আগে থেকে load করা একটা object পাঠানো যাতে আবার fetch করতে না হয়। তখনও সবসময় `null` guard রাখুন (refresh বা deep link এটা মুছে দিতে পারে)।

```dart
final data = state.extra as Product?; // nullable cast
if (data == null) return const ProductLoaderScreen(); // আবার fetch করার fallback
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা একসাথে দুটো জিনিস যাচাই করেন: type safety-র সচেতনতা আর web compatibility-র সচেতনতা। `extra`-র উপর নির্ভর করা একটা ক্লাসিক bug, যেটা শুধু app web-এ চালালে দেখা যায়।

**সাধারণ ভুল:** সবকিছুর জন্য `extra` ব্যবহার করা, কারণ এটাই সবচেয়ে সহজ। তারপর web refresh আর deep link-এ ভেঙে পড়া। আরেকটা ভুল — `extra`-কে non-null হিসেবে cast করা, আর user page refresh করলে crash করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`extra` web-এ কেন ভাঙে?"* → এটা memory-তে থাকে, URL-এ নয়। Refresh শুধু URL থেকে reload করে, তাই `extra` আর থাকে না।
- *"Path নাকি query parameter — id-র জন্য কোনটা?"* → পরিচয়ের জন্য path parameter (`/products/:id`)। `?sort=price`-এর মতো optional view setting-এর জন্য query parameter।

**সম্পর্কিত:** [Q6 — path ও query parameter](#q6) · [Q10 — typed routes](#q10) · [Q2 — data ফেরত পাঠানো](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. go_router-এ 404 / unknown route কীভাবে handle করেন?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"go_router-এ একটা `errorBuilder` আছে। কোনো navigation যখন কোনো route-এর সাথে মেলে না, তখন এটা চলে — এটাই 404 page। তাই একটা typo, পুরোনো deep link, বা web-এ হাতে লেখা URL crash না করে একটা সুন্দর screen দেখায়। আমি যদি এটা set না করি, তাহলে debug-এ go_router একটা default লাল error screen দেখায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Unknown route কেন হয়।**
Web-এ user যেকোনো URL টাইপ করতে পারেন। Mobile-এ একটা পুরোনো marketing link বা push notification এমন screen-এ পাঠাতে পারে যেটা আপনি সরিয়ে ফেলেছেন। Handle না করলে ওই path কোনো কিছুর সাথেই মেলে না।

**ধাপ ২ — `errorBuilder`: আপনার 404 screen।**
`GoRouter`-এ `errorBuilder` set করুন। যেকোনো unmatched path-এর জন্য এটা চলে। এটা চেষ্টা করা location-টাও পায়। তাই আপনি একটা কাজের message আর একটা "go home" button দেখাতে পারেন।

```dart
final router = GoRouter(
  routes: [ /* ... your routes ... */ ],

  // যেকোনো unmatched route-এর জন্য call হয়
  errorBuilder: (context, state) => Scaffold(
    appBar: AppBar(title: const Text('Page not found')),
    body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text('404', style: TextStyle(fontSize: 64, fontWeight: FontWeight.bold)),
          const SizedBox(height: 12),
          Text('No route for: ${state.uri}'),
          const SizedBox(height: 24),
          ElevatedButton(
            onPressed: () => context.go('/'),
            child: const Text('Go home'),
          ),
        ],
      ),
    ),
  ),
);
```

**ধাপ ৩ — অথবা পুরোনো path-কে নতুন path-এ redirect করুন।**
কখনো কখনো আপনি 404 চান না — পুরোনো URL-কে তার নতুন ঘরে পাঠাতে চান। এই কাজটা `redirect`-এ করুন (যেটা *matched* route আর pattern check-এর জন্য চলে), `errorBuilder`-এ নয়।

```dart
redirect: (context, state) {
  if (state.matchedLocation.startsWith('/old-products')) {
    return '/products'; // নাম বদলানো path forward করে
  }
  return null;
},
```

**ধাপ ৪ — `errorBuilder` বনাম `redirect` (দুটো গুলিয়ে ফেলবেন না)।**
- **`redirect`** → যে route আপনি *বোঝেন* তার জন্য চলে (auth guard, নাম বদলানো path)। এটা ঠিক করে user-কে কোথায় পাঠানো হবে।
- **`errorBuilder`** → শুধু সেই route-এর জন্য চলে যেটা *কোনো কিছুর* সাথে মেলে না। এটা 404 দেখায়।

**Interviewer কেন জিজ্ঞেস করে:** Unknown route সুন্দরভাবে handle করা production-এর একটা দরকার, বিশেষ করে web-এ। তাঁরা দেখতে চান আপনি edge case নিয়ে ভাবেন কি না, নাকি একটা কাঁচা error screen ফেলে রাখেন।

**সাধারণ ভুল:** `errorBuilder` একেবারেই set না করা, ফলে user default debug error screen দেখেন। আরেকটা ভুল — `errorBuilder` (unmatched route) আর `redirect` (matched route) গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`errorBuilder` বনাম `errorPageBuilder`?"* → `errorBuilder` একটা widget return করে (go_router সেটাকে একটা page-এ মুড়ে দেয়)। `errorPageBuilder` আপনাকে custom transition-এর জন্য একটা custom `Page` return করতে দেয়।
- *"নাম বদলানো URL কোথায় forward করেন?"* → `redirect`-এ, `errorBuilder`-এ নয় — path-টা এখনো এমন একটা pattern-এর সাথে "মেলে" যেটা আপনি handle করতে চান।

**সম্পর্কিত:** [Q8 — auth-এর জন্য redirect](#q8) · [Q6 — go_router basics](#q6) · [Q3 — Navigator 1.0-এ onUnknownRoute](#q3)

[↑ উপরে ফিরুন](#toc)

---

# D. বাস্তব জীবনের navigation সমস্যা

---

## <a id="q13"></a>13. Deep linking কী? go_router দিয়ে Android আর iOS-এ এটা কীভাবে configure করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Deep link app-এর বাইরের কোনো কিছুকে — browser URL, push notification, অন্য app — সরাসরি একটা নির্দিষ্ট screen-এ app খুলতে দেয়, home screen-এ নয়। URL একবার চলে এলে go_router app-এর ভেতরের অংশটা বিনা খরচে সামলায়। আসল কাজ হলো platform setup: Android-এ App Links আর iOS-এ Universal Links। দুটোরই পেছনে আপনার domain-এ একটা verification file লাগে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Deep linking কী করে।**
সাধারণভাবে `https://myapp.com/products/42` tap করলে browser খোলে। Deep linking set করা থাকলে OS ওই URL সরাসরি আপনার installed app-এ পাঠায়। তারপর go_router সঠিক stack বানায় (Home → Products → Product 42)।

```
User taps https://myapp.com/products/42
          │
          ▼
   OS checks the link
   app installed?  ── no ──►  open in browser
          │ yes
          ▼
   OS hands '/products/42' to your app
          │
          ▼
   go_router builds the matching page stack
```

**ধাপ ২ — go_router-এর দিক: বাড়তি কিছুই নেই।**
আপনার এখনকার route tree ওই path আগে থেকেই handle করে। go_router আসা URL-টা আর দশটা navigation-এর মতোই পায়।

```dart
GoRoute(
  path: 'products/:productId',
  builder: (context, state) =>
      ProductDetailScreen(id: state.pathParameters['productId']!),
);
```

**ধাপ ৩ — Android: App Links।**
`android/app/src/main/AndroidManifest.xml`-এ `<activity>`-তে একটা intent filter যোগ করুন। `autoVerify="true"` Android-কে বলে আপনার domain verify করতে, যাতে link সরাসরি app খোলে।

```xml
<activity ...>
  <intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="https" android:host="myapp.com" />
  </intent-filter>
</activity>
```

তারপর `https://myapp.com/.well-known/assetlinks.json`-এ একটা `assetlinks.json` file host করুন। এতে আপনার app-এর package name আর SHA-256 signing fingerprint থাকবে। এভাবেই Android প্রমাণ করে link-টা আপনার app-এরই।

**ধাপ ৪ — iOS: Universal Links।**
`ios/Runner/Runner.entitlements`-এ একটা associated domain যোগ করুন:

```xml
<key>com.apple.developer.associated-domains</key>
<array>
  <string>applinks:myapp.com</string>
</array>
```

তারপর `https://myapp.com/.well-known/apple-app-site-association`-এ একটা `apple-app-site-association` (AASA) file host করুন। এতে আপনার app ID আর যে path-গুলো এটা handle করে সেগুলোর তালিকা থাকবে:

```json
{
  "applinks": {
    "details": [
      { "appID": "TEAMID.com.example.myapp", "paths": ["/products/*", "/settings"] }
    ]
  }
}
```

**ধাপ ৫ — `https` link বনাম custom scheme।**
`myapp://product/42`-এর মতো custom scheme সহজ, কিন্তু unverified। এটা সাধারণ web page বা email থেকে খুলবে না। Verified `https` App Links / Universal Links-ই production-এর পছন্দ, কারণ এগুলো বিশ্বস্ত আর browser থেকেও কাজ করে।

**Interviewer কেন জিজ্ঞেস করে:** Marketing campaign, push notification, আর web-to-app flow-এর জন্য deep linking আবশ্যক। তাঁরা দেখতে চান আপনি দুই platform-ই configure করতে পারেন কি না, শুধু Dart-এর দিকটা নয়।

**সাধারণ ভুল:** শুধু go_router-ই যথেষ্ট ভাবা আর platform file-গুলো ভুলে যাওয়া (AndroidManifest + assetlinks.json, entitlements + AASA)। আরেকটা ভুল — custom scheme (`myapp://`) আর verified `https` link গুলিয়ে ফেলা। Custom scheme verification এড়িয়ে যায় আর browser থেকে কাজ করে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`autoVerify` / AASA file আসলে কী করে?"* → এগুলো OS-কে নিশ্চিত করতে দেয় যে domain-টা সত্যিই আপনার। তাই link কোনো chooser dialog ছাড়াই সরাসরি আপনার app খোলে।
- *"Deep link locally কীভাবে test করেন?"* → Android-এ `adb shell am start -a android.intent.action.VIEW -d "https://myapp.com/products/42"` ব্যবহার করুন, আর iOS Simulator-এ `xcrun simctl openurl booted "https://myapp.com/products/42"`।

**সম্পর্কিত:** [Q4 — declarative routing কেন deep link সামলায়](#q4) · [Q6 — go_router routes](#q6) · [Q8 — deep link-এও redirect চলে](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. `PopScope` কীভাবে কাজ করে? Back button কীভাবে intercept করেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`PopScope` একটা screen-কে মুড়ে রাখে আর ঠিক করে সেটা pop করা যাবে কি না। এটা Android back button, iOS back swipe আর `Navigator.pop` — সবই ধরে। Pop আটকাতে আমি `canPop: false` দিই। আর `onPopInvokedWithResult`-এ একটা confirm dialog দেখাই, user রাজি হলে নিজে pop করি। এটা পুরোনো, deprecated `WillPopScope`-এর জায়গা নিয়েছে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Back intercept করার দরকার কেন।**
ধরুন একটা form-এ unsaved changes আছে। User ভুল করে back চাপলে তাঁর কাজ হারিয়ে যাবে। `PopScope` আপনাকে সেটা থামিয়ে আগে জিজ্ঞেস করতে দেয় — "Discard changes?"

**ধাপ ২ — দুটো মূল অংশ।**
- `canPop` — একটা bool। `false` মানে "system gesture বা back button দিয়ে এই screen pop করতে দেবে না।"
- `onPopInvokedWithResult` — একটা callback, যেটা pop-এর চেষ্টা হলে চলে। এটা বলে দেয় pop সত্যিই হয়েছে কি না (`didPop`)।

**ধাপ ৩ — পুরো flow।**
`canPop` যখন `false` আর user back চাপেন, তখন pop *আটকে* যায়। ফলে `didPop` হয় `false` — এটাই আপনার dialog দেখানোর ইশারা। User রাজি হলে আপনি নিজে pop করেন।

```dart
class EditFormScreen extends StatefulWidget {
  const EditFormScreen({super.key});
  @override
  State<EditFormScreen> createState() => _EditFormScreenState();
}

class _EditFormScreenState extends State<EditFormScreen> {
  bool _hasUnsavedChanges = false;

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: !_hasUnsavedChanges, // unsaved changes থাকলে back আটকায়
      onPopInvokedWithResult: (bool didPop, Object? result) async {
        if (didPop) return; // pop হয়ে গেছে (canPop true ছিল) → কিছু করার নেই

        // pop আটকে গেছে → user-কে জিজ্ঞেস করুন
        final leave = await showDialog<bool>(
          context: context,
          builder: (_) => AlertDialog(
            title: const Text('Discard changes?'),
            content: const Text('You have unsaved changes.'),
            actions: [
              TextButton(onPressed: () => Navigator.pop(context, false), child: const Text('Stay')),
              TextButton(onPressed: () => Navigator.pop(context, true), child: const Text('Discard')),
            ],
          ),
        );
        if (leave == true && context.mounted) {
          Navigator.pop(context); // নিশ্চিত হওয়ার পরে নিজেরাই pop করি
        }
      },
      child: Scaffold(
        appBar: AppBar(title: const Text('Edit form')),
        body: TextField(
          onChanged: (_) => setState(() => _hasUnsavedChanges = true),
        ),
      ),
    );
  }
}
```

**ধাপ ৪ — `WillPopScope` কেন চলে গেছে।**
পুরোনো `WillPopScope` pop allow বা block করতে একটা `Future<bool>` return করত। ওই model Android-এর predictive back gesture-এর সাথে মিলত না (swipe করার সময় যে peek animation হয়)। `PopScope` আগেভাগেই `canPop` দিয়ে সিদ্ধান্ত নেয়, যেটা predictive back-এর সাথে কাজ করে। তাই এখন সবসময় `PopScope` ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** Form, checkout flow আর editor-এ এটা খুবই সাধারণ। তাঁরা দেখেন আপনি আধুনিক API জানেন কি না (`PopScope`, `WillPopScope` নয়) আর `didPop` ঠিকভাবে পড়েন কি না।

**সাধারণ ভুল:** এখনো `WillPopScope` ব্যবহার করা (deprecated)। আর একটা চোখে পড়ে না এমন ভুল: `didPop` উল্টো বোঝা। `canPop` যখন `false`, তখন callback-এ `didPop` হয় `false` — ঠিক তখনই আপনি dialog দেখাবেন। `didPop` `true` হলে pop আগেই হয়ে গেছে, তাই আবার pop করবেন না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"সবসময় `canPop: false` দিলে সমস্যা কী?"* → তাহলে screen-টা gesture দিয়ে আর কখনোই বন্ধ হবে না, ফলে predictive back ভেঙে যায়। `canPop`-কে আসল state অনুযায়ী রাখুন (যেমন `!hasUnsavedChanges`)।
- *"এটা go_router-এর সাথে কাজ করে?"* → হ্যাঁ, `PopScope` একইভাবে কাজ করে; manual pop-টা `Navigator.pop`-এর বদলে `context.pop()` হতে পারে।

**সম্পর্কিত:** [Q1 — maybePop আর back button](#q1) · [Q2 — pop-এ result ফেরত দেওয়া](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. Widget tree-এর বাইরে থেকে কীভাবে navigate করবেন — যেমন Cubit, service, বা repository থেকে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"সমস্যাটা হলো `context.go()`-এর একটা `BuildContext` লাগে, যেটা Cubit বা service-এ থাকে না। সবচেয়ে পরিষ্কার উত্তর হলো reactive: Cubit একটা state emit করে, আর UI-এর `BlocListener` navigation-টা করে। যদি সত্যিই context ছাড়া navigate করতে হয়, তাহলে আমি `GoRouter`-এর একটা reference (বা একটা global navigator key) রেখে দিই এবং সরাসরি সেটাকে call করি। আমি কখনোই Cubit-এ `BuildContext` জমা রাখি না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কেন কঠিন।**
Navigation-এর জন্য `context` লাগে। কিন্তু business logic (Cubit, service) widget tree-এর বাইরে থাকে, তাই তার কোনো context নেই। তাই দুটোকে জোড়া দিতে হয়, কিন্তু logic-এর ভেতরে UI ঢুকতে দেওয়া যাবে না।

**ধাপ ২ — Approach 1 (পছন্দের): UI state-এর উপর react করে।**
Navigation widget tree-তেই রাখুন, যেখানে এটা মানায়। Cubit শুধু একটা state emit করে; `BlocListener` সেটা দেখে navigate করে। এতে business logic navigation থেকে মুক্ত থাকে।

```dart
// Cubit-এ — কোনো navigation নেই, শুধু state
class PaymentCubit extends Cubit<PaymentState> {
  PaymentCubit() : super(PaymentInitial());
  Future<void> pay() async {
    // ... payment process করা হচ্ছে ...
    emit(PaymentSuccess()); // শুধু success ঘোষণা করে
  }
}

// widget-এ — UI navigation ঠিক করে
BlocListener<PaymentCubit, PaymentState>(
  listener: (context, state) {
    if (state is PaymentSuccess) context.go('/success');
  },
  child: const PaymentForm(),
);
```

**ধাপ ৩ — Approach 2: router-এর একটা reference রাখুন।**
কখনো কখনো UI-তে react করা বেমানান লাগে (যেমন গভীর service layer-এর একটা event)। তখন `GoRouter` instance-টা ধরে রাখুন — সাধারণত `get_it`-এর মতো service locator দিয়ে — আর সরাসরি call করুন। Router-এর কোনো context লাগে না।

```dart
// একবার register করুন
final getIt = GetIt.instance;
getIt.registerSingleton<GoRouter>(router);

// যেকোনো জায়গা থেকে call — কোনো BuildContext লাগে না
getIt<GoRouter>().go('/success');
```

**ধাপ ৪ — Approach 3: একটা global navigator key।**
একটা `GlobalKey<NavigatorState>` বানান, সেটা go_router-কে দিন, আর tree-এর বাইরে থেকে low-level navigation (এবং dialog-এর মতো কাজ) করতে সেটা ব্যবহার করুন।

```dart
final rootNavigatorKey = GlobalKey<NavigatorState>();

final router = GoRouter(
  navigatorKey: rootNavigatorKey,
  routes: [ /* ... */ ],
);

// tree-এর বাইরে থেকে:
rootNavigatorKey.currentContext?.go('/success');
```

**ধাপ ৫ — কঠিন নিয়ম: `BuildContext` কখনোই জমা রাখবেন না।**
Cubit বা service-এ `context` জমা রাখা বিপজ্জনক — ওই widget dispose হয়ে গেলে context বাসি হয়ে যায়। সেটা ব্যবহার করলে crash হয়, বা ভুল জায়গায় navigate হয়। এটা আপনার logic-কে Flutter-এর সাথে জুড়েও দেয়। এর বদলে router pass করুন বা reactive listener ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা প্রতিটা বাস্তব project-এ আসে। তাঁরা দেখতে চান আপনি separation of concerns মানছেন কি না — আদর্শভাবে business logic navigation-এর উপর নির্ভর করবে না। আর আপনি জানেন কি না যে reactive pattern-টাই সবচেয়ে পরিষ্কার।

**সাধারণ ভুল:** Cubit/service-এ `BuildContext` জমা রাখা। Widget dispose হলে সেটা বাসি হয়ে যায় এবং crash ঘটায়। আরেকটা ভুল — এটা না বোঝা যে `GoRouter` instance কোনো context ছাড়াই সরাসরি call করা যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Architecture-এর দিক থেকে কোন approach সবচেয়ে পরিষ্কার?"* → reactive `BlocListener`-টা — logic state emit করে, UI navigate করে। এতে দুটো layer আলাদা থাকে।
- *"Router-reference approach কখন যুক্তিসঙ্গত?"* → cross-cutting কাজের জন্য, যেমন একটা session-expiry handler যেটাকে service layer-এর গভীর থেকে login-এ redirect করতে হয়।

**সম্পর্কিত:** [Q8 — auth redirect state-এর উপর react করে](#q8) · [Q5 — RouterDelegate-এ navigator key](#q5)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. Nested navigator কখন দরকার হয়? Bottom navigation bar কীভাবে আলাদা navigation stack ব্যবহার করে?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Nested navigator দরকার হয় যখন app-এর আলাদা আলাদা section-কে নিজের history রাখতে হয়। ক্লাসিক উদাহরণ bottom nav bar: প্রতিটা tab-এর নিজের stack আর scroll মনে রাখা উচিত। তাই Home (একটা detail-এ ঢুকে) ছেড়ে ফিরে এলে ওই detail-ই ফিরে আসবে, Home root নয়। এটা বানাতে হয় `IndexedStack`-এর ভেতরে প্রতি tab-এ একটা করে `Navigator` দিয়ে, অথবা go_router-এ `StatefulShellRoute.indexedStack` দিয়ে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা navigator কেন যথেষ্ট নয়।**
একটা navigator-এর একটাই stack থাকে। Bottom bar-এর ক্ষেত্রে এর মানে হলো tab বদলালে হয় history reset হয়, নয়তো bar-টাই মুছে যায়। প্রতিটা tab আসলে *নিজের* stack চায়।

```
Nested navigator — প্রতিটা tab-এর নিজের stack:

Root navigator
├── Tab 0 navigator (Home)
│   ├── HomeScreen
│   └── HomeDetailScreen   ← user এখানে ঢুকেছে
├── Tab 1 navigator (Search)
│   ├── SearchScreen
│   └── SearchResultScreen
└── Tab 2 navigator (Profile)
    └── ProfileScreen

Tab বদলানো মানে শুধু আলাদা একটা navigator দেখানো।
প্রতিটা tab নিজের stack মনে রাখে।
```

**ধাপ ২ — হাতে করার উপায়: `IndexedStack`-এ প্রতি tab-এ একটা Navigator।**
প্রতিটা tab-কে নিজের `GlobalKey<NavigatorState>` আর নিজের `Navigator` দিন। `IndexedStack` সব tab-কে জীবিত রাখে (শুধু লুকিয়ে রাখে), তাই tab বদলালেও তাদের state টিকে থাকে।

```dart
class MainScreen extends StatefulWidget {
  const MainScreen({super.key});
  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _index = 0;
  final _keys = [
    GlobalKey<NavigatorState>(),
    GlobalKey<NavigatorState>(),
    GlobalKey<NavigatorState>(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(
        index: _index,
        children: [
          _tabNavigator(0, const HomeScreen()),
          _tabNavigator(1, const SearchScreen()),
          _tabNavigator(2, const ProfileScreen()),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _index,
        onTap: (i) {
          if (i == _index) {
            // active tab-এ আবার tap করলে সেটা root-এ pop হয়
            _keys[i].currentState?.popUntil((r) => r.isFirst);
          } else {
            setState(() => _index = i);
          }
        },
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
        ],
      ),
    );
  }

  Widget _tabNavigator(int i, Widget root) => Navigator(
        key: _keys[i],
        onGenerateRoute: (_) => MaterialPageRoute(builder: (_) => root),
      );
}
```

**ধাপ ৩ — আধুনিক উপায়: `StatefulShellRoute.indexedStack`।**
go_router আপনার জন্য একই জিনিস বানিয়ে দেয়। প্রতিটা branch নিজের stack, `IndexedStack`-এ জীবিত রাখা হয়। আর আপনি `navigationShell.goBranch` দিয়ে switch করেন। (পুরো setup-এর জন্য [Q9](#q9) দেখুন।)

```dart
StatefulShellRoute.indexedStack(
  builder: (context, state, navigationShell) => Scaffold(
    body: navigationShell,
    bottomNavigationBar: BottomNavigationBar(
      currentIndex: navigationShell.currentIndex,
      onTap: (i) => navigationShell.goBranch(i),
      items: const [ /* ... */ ],
    ),
  ),
  branches: [
    StatefulShellBranch(routes: [GoRoute(path: '/home', builder: (_, __) => const HomeScreen())]),
    StatefulShellBranch(routes: [GoRoute(path: '/search', builder: (_, __) => const SearchScreen())]),
    StatefulShellBranch(routes: [GoRoute(path: '/profile', builder: (_, __) => const ProfileScreen())]),
  ],
);
```

**ধাপ ৪ — কেন ঠিক `IndexedStack`।**
`IndexedStack` সব children একবার build করে আর একসাথে একটাই দেখায়। সাধারণ `Stack` বা একটা condition (`if index == 0`) প্রতিবার switch-এ tab ধ্বংস করে আবার বানাত। এতে scroll position আর history হারিয়ে যেত। `IndexedStack`-ই এগুলো রক্ষা করে।

**Interviewer কেন জিজ্ঞেস করে:** এটা mobile-এর সবচেয়ে সাধারণ UX pattern-গুলোর একটা (Instagram, YouTube, Twitter সবাই এটা ব্যবহার করে)। তাঁরা দেখতে চান আপনি বুঝেছেন কি না একটা navigator কেন ব্যর্থ হয়, আর প্রতি tab-এ আলাদা stack কীভাবে সেটা ঠিক করে।

**সাধারণ ভুল:** সব কিছুর জন্য একটা navigator ব্যবহার করা এবং switch-এ tab state হারানো। অথবা `IndexedStack` ভুলে গিয়ে সাধারণ `Stack` ব্যবহার করা, যেটা tab আবার build করে এবং তাদের state মুছে দেয়। go_router-এ ভুলটা হলো `StatefulShellRoute`-এর বদলে `ShellRoute` ব্যবহার করা, আর তারপর অবাক হওয়া কেন tab state টিকছে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Active tab-এ আবার tap করলে কীভাবে 'pop to root' করবেন?"* → ওই tab-এর navigator key-তে `popUntil((r) => r.isFirst)` call করুন (হাতে করলে), অথবা `goBranch(i, initialLocation: true)` (go_router)।
- *"ShellRoute vs StatefulShellRoute?"* → `ShellRoute` একটাই stack ভাগ করে নেয়; `StatefulShellRoute` প্রতিটা branch-কে নিজের stack দেয় এবং state ধরে রাখে ([Q9](#q9))।

**সম্পর্কিত:** [Q9 — shell route](#q9) · [Q1 — Navigator stack](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q17"></a>17. Screen-এর মাঝে custom page transition / animation কীভাবে বানাবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-04-navigation.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Navigator 1.0-এর জন্য আমি `PageRouteBuilder` ব্যবহার করি। নতুন screen-টা animate করি transition-এর `animation` value দিয়ে — যেমন একটা `SlideTransition` বা `FadeTransition`। go_router-এ আমি `builder`-এর বদলে `pageBuilder` থেকে একটা `CustomTransitionPage` return করি। মূল ধারণা হলো — child-কে একটা transition দিয়ে wrap করা, যেটা route-এর animation দিয়ে চলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Default transition গুলো।**
Default অবস্থায় Flutter platform transition ব্যবহার করে: Android-এ `MaterialPageRoute` উপরের দিকে slide করে, iOS-এ `CupertinoPageRoute` ডান দিক থেকে slide করে আসে। আপনি তখনই customize করবেন যখন অন্যরকম কিছু চান (একটা fade, একটা scale, বা নির্দিষ্ট দিক থেকে slide)।

**ধাপ ২ — Navigator 1.0: `PageRouteBuilder`।**
`PageRouteBuilder` আপনাকে দুটো function দেয়: `pageBuilder` (screen-টা) আর `transitionsBuilder` (কীভাবে animate হয়ে ঢুকবে)। Route ঢোকার সময় `animation` value 0 থেকে 1-এ যায়।

```dart
Navigator.push(
  context,
  PageRouteBuilder(
    pageBuilder: (context, animation, secondaryAnimation) => const DetailScreen(),
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      // ডান দিক থেকে slide করে আসবে
      final tween = Tween(begin: const Offset(1, 0), end: Offset.zero)
          .chain(CurveTween(curve: Curves.easeInOut));
      return SlideTransition(position: animation.drive(tween), child: child);
    },
    transitionDuration: const Duration(milliseconds: 300),
  ),
);
```

**ধাপ ৩ — go_router: `CustomTransitionPage`।**
go_router-এ আপনি `pageBuilder` ব্যবহার করবেন (`builder` নয়) এবং একটা `CustomTransitionPage` return করবেন। `transitionsBuilder` উপরের মতোই কাজ করে।

```dart
GoRoute(
  path: '/details',
  pageBuilder: (context, state) => CustomTransitionPage(
    key: state.pageKey,
    child: const DetailScreen(),
    transitionsBuilder: (context, animation, secondaryAnimation, child) =>
        FadeTransition(opacity: animation, child: child), // fade হয়ে আসবে
  ),
);
```

**ধাপ ৪ — Shared-element transition: `Hero`।**
কোনো image বা card যদি এক screen থেকে আরেক screen-এ *উড়ে* যাওয়া উচিত, তাহলে দুই জায়গাতেই একই `tag` দিয়ে `Hero` দিয়ে wrap করুন। Flutter route-এর মাঝে নিজে থেকেই এটা animate করে — কোনো custom route লাগে না।

```dart
// list screen-এ
Hero(tag: 'product-42', child: Image.network(url));
// detail screen-এ — একই tag
Hero(tag: 'product-42', child: Image.network(url));
```

**ধাপ ৫ — Transition ছোট রাখুন আর একরকম রাখুন।**
প্রায় 200–350 ms duration ব্যবহার করুন। পুরো app জুড়ে একই style রাখুন। লম্বা বা বেমানান transition ধীর আর অপরিপক্ব লাগে — একজন senior এগুলো হালকা রাখেন।

**Interviewer কেন জিজ্ঞেস করে:** Custom transition দেখায় আপনি বোঝেন route আসলে widget, যেগুলো একটা animation দিয়ে চলে। আরও দেখায় আপনি navigation না ভেঙে UX পরিপাটি করতে পারেন।

**সাধারণ ভুল:** go_router-এ custom transition দরকার হলে `pageBuilder`-এর বদলে `builder` ব্যবহার করা (`builder` সবসময় default transition দেয়)। আরেকটা ভুল হলো `key: state.pageKey` দিতে ভুলে যাওয়া। এটা go_router-কে rebuild-এর মাঝে page ঠিকভাবে track করতে সাহায্য করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`secondaryAnimation` কী?"* → পরের screen ঢোকার সময় এটা এই screen-টাকে *বের* করে animate করে। ফলে বের হওয়া আর ঢোকা page দুটোকে মিলিয়ে সাজাতে পারবেন।
- *"প্রতি platform-এ iOS আর Android-এর default transition কীভাবে মেলাবেন?"* → `MaterialPageRoute` / `CupertinoPageRoute` ব্যবহার করুন। অথবা `Theme`-এর `pageTransitionsTheme` দিয়ে পুরো app-এ platform অনুযায়ী builder সেট করুন।

**সম্পর্কিত:** [Q1 — MaterialPageRoute](#q1) · [Q12 — custom error transition-এর জন্য errorPageBuilder](#q12) · [Q6 — go_router routes](#q6)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার table গুলো, তারপর এক লাইনের মনে করিয়ে দেওয়া পয়েন্ট।

## দ্রুত তুলনার table

**Navigator 1.0 vs Navigator 2.0**

| | Navigator 1.0 | Navigator 2.0 |
|---|---|---|
| ধরন | imperative (push/pop) | declarative (পুরো stack বর্ণনা করুন) |
| Deep link | হাতে করতে হয়, ঠুনকো | URL থেকে নিজে থেকেই তৈরি হয় |
| Web URL sync | built in নেই | URL ↔ stack দুই দিকেই |
| বাস্তবে | সহজ mobile app-এর জন্য ঠিক আছে | এর উপরে go_router ব্যবহার করুন |

**go_router: `go` vs `push` vs `replace`**

| | `go()` | `push()` | `replace()` |
|---|---|---|---|
| ফল | URL-এর সাথে মেলাতে stack আবার তৈরি করে | উপরে একটা screen যোগ করে | উপরের screen বদলে দেয় |
| Stack | মিলে যাওয়া tree-তে reset হয় | একটা বাড়ে | আকার একই থাকে |
| কখন ব্যবহার | সাধারণ nav, web, deep link | স্তরে স্তরে screen | login → home |

**`ShellRoute` vs `StatefulShellRoute`**

| `ShellRoute` | `StatefulShellRoute.indexedStack` |
|---|---|
| একটাই shared stack | প্রতি tab-এ আলাদা stack |
| tab বদলালে tab-এর state হারায় | tab-এর state + scroll থেকে যায় |
| সহজ shared shell | চিরচেনা bottom-nav app |

**Argument পাঠানো: নিরাপদ vs অনিরাপদ**

| | Path / query params | `extra` |
|---|---|---|
| URL-এ থাকে? | হ্যাঁ | না (শুধু memory-তে) |
| Web refresh-এ টিকে? | হ্যাঁ | না |
| Deep-link friendly? | হ্যাঁ | না |
| Type | সবসময় String | যেকোনো object (ঝুঁকির cast) |

**`PopScope` vs `WillPopScope`**

| `PopScope` (এখনকার) | `WillPopScope` (deprecated) |
|---|---|
| আগেই `canPop` দিয়ে ঠিক করে | একটা `Future<bool>` return করত |
| predictive back-এর সাথে কাজ করে | predictive back ভেঙে দেয় |
| এটাই ব্যবহার করুন | ব্যবহার করবেন না |

## এক লাইনের মনে করিয়ে দেওয়া

- **Navigator stack** = থালার স্তূপ; `push` যোগ করে, `pop` সরায়, `pushReplacement` উপরেরটা বদলায়। ([Q1](#q1))
- **`push` একটা Future return করে**; `pop(value)` data ফেরত পাঠায় — আর back চাপলে result `null` হতে পারে। ([Q2](#q2))
- **Navigator 2.0** declarative: state থেকে পুরো stack বর্ণনা করুন, deep link আর web URL-এর জন্য। ([Q4](#q4))
- **Parser → Delegate → Navigator**; delegate-কে অবশ্যই `notifyListeners()` call করতে হবে। go_router তিনটাই করে দেয়। ([Q5](#q5))
- **Path params** (`:id`) বলে কোন জিনিস; **query params** (`?sort=`) ঠিক করে কীভাবে দেখবেন। ([Q6](#q6))
- **`go()`** stack আবার তৈরি করে; **`push()`** উপরে একটা screen যোগ করে; **`replace()`** উপরেরটা বদলায়। ([Q7](#q7))
- **Auth guard:** `redirect`-এ `/login` allow করুন যাতে loop না হয়, আর logout-এর জন্য `refreshListenable` ব্যবহার করুন। ([Q8](#q8))
- **`StatefulShellRoute.indexedStack`** প্রতি tab-এর stack আর scroll রেখে দেয়; সাধারণ `ShellRoute` রাখে না। ([Q9](#q9))
- **Typed routes** (go_router_builder) compile time-এই টাইপো ধরে; named route runtime-এ fail করে। ([Q10](#q10))
- **`extra`-র বদলে path/query params ব্যবহার করুন** (URL-safe); `extra` web refresh-এ হারায় আর deep link ভেঙে দেয়। ([Q11](#q11))
- **`errorBuilder`** = না মেলা route-এর জন্য 404; **`redirect`** = মিলে যাওয়া route-এর জন্য সিদ্ধান্ত। ([Q12](#q12))
- **Deep link**-এর জন্য platform setup লাগে: App Links + assetlinks.json (Android), Universal Links + AASA (iOS)। ([Q13](#q13))
- **`PopScope`** `WillPopScope`-এর জায়গা নেয়; আটকানো থাকলে `didPop` হয় `false` — তখনই confirm করবেন। ([Q14](#q14))
- **Cubit-এ কখনোই `BuildContext` রাখবেন না**; state emit করুন আর একটা `BlocListener` দিয়ে navigate করান। ([Q15](#q15))
- **প্রতিটা tab-এর নিজের Navigator লাগে** একটা `IndexedStack`-এর ভেতরে, যাতে তার history আর scroll থাকে। ([Q16](#q16))
- **Custom transition:** `PageRouteBuilder` (Nav 1.0) বা `CustomTransitionPage` (go_router); shared element-এর জন্য `Hero`। ([Q17](#q17))

[↑ উপরে ফিরুন](#toc)

# Section 2 — Flutter Core Internals

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **Bangladesh (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরোপুরি ব্যাখ্যা করা**, আর **link দেওয়া** — যাতে আপনি এদিক-ওদিক ঘুরে ধাপে ধাপে প্রস্তুতি নিতে পারেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-02-flutter-internals-bn.md](../software-engineer-flutter/section-02-flutter-internals.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বিস্তারিত, ধাপে ধাপে ব্যাখ্যা, বাস্তব জীবনের উদাহরণ আর code সহ।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর তার কঠিনতা (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তর** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন "আরও গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলা নিজেই একটা senior skill — আর এটা remote আর BD দুই ধরনের কোম্পানিতেই সমান কাজ করে।

---


## <a id="toc"></a>সূচিপত্র

**A. তিনটি tree ও widget identity**
1. [তিনটি tree — Widget, Element, RenderObject](#q1) · *Very common*
2. [Widget-গুলো immutable কেন?](#q2) · *Common*
3. [Keys — Value, Object, Unique, Global, Local](#q3) · *Very common*
4. [Flutter কীভাবে widget reuse করে (reconciliation)](#q4) · *Common*

**B. Widget ও state**
5. [StatelessWidget বনাম StatefulWidget](#q5) · *Very common*
6. [পুরো StatefulWidget lifecycle](#q6) · *Very common*
7. [`setState` আসলে কী করে?](#q7) · *Very common*
8. [BuildContext কী?](#q8) · *Very common*
9. [InheritedWidget আর তার উপরে Provider কীভাবে বানানো](#q9) · *Very common*

**C. Performance — const, repaint, thread**
10. [`const` কীভাবে rebuild ঠেকায়](#q10) · *Common*
11. [RepaintBoundary — repaint আলাদা করে রাখা](#q11) · *Common*
12. [Flutter কীভাবে 60/120fps ধরে রাখে — UI thread বনাম raster thread](#q12) · *Very common*

**D. Layout ও constraints**
13. [Layout-এর নিয়ম — constraints নিচে যায়, size উপরে আসে, parent position ঠিক করে](#q13) · *Very common*
14. [BoxConstraints — tight, loose, unbounded](#q14) · *Common*
15. ["RenderFlex overflowed" — কেন হয় আর কীভাবে ঠিক করবেন](#q15) · *Very common*
16. [MediaQuery বনাম LayoutBuilder](#q16) · *Common*

**E. Rendering pipeline ও graphics**
17. [Rendering pipeline — tap থেকে pixel পর্যন্ত](#q17) · *Common*
18. [Impeller বনাম Skia — Flutter কেন বদলাল](#q18) · *Common*

**F. Tooling ও dev loop**
19. [Hot Reload বনাম Hot Restart বনাম Full Restart](#q19) · *Very common*
20. [pub.dev, pubspec.yaml ও version constraints](#q20) · *Common*
21. [Flutter SDK channel — stable, beta, master](#q21) · *Common*

**G. Flutter আর Dart একসাথে কীভাবে কাজ করে (গভীর architecture)**
22. [তিনটি layer — Embedder, Engine, Framework](#q22) · *Deeper*
23. [Engine-এর ভেতরে Dart কীভাবে চলে (JIT বনাম AOT)](#q23) · *Deeper*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (আগের রাতের review)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

২৩টা প্রশ্ন একসাথে পড়ার দরকার নেই। এই পর্যায়গুলো ক্রম অনুযায়ী শেষ করুন — প্রতিটা আগেরটার উপরে দাঁড়িয়ে আছে। একটা পর্যায় তখনই টিক দিন, যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন।

**পর্যায় ১ — মূল mental model (এখান থেকেই শুরু)।** এটা ছাড়া বাকি কিছুই বোঝা যাবে না।
→ [Q1 তিনটি tree](#q1) · [Q5 Stateless বনাম Stateful](#q5) · [Q7 setState](#q7) · [Q8 BuildContext](#q8)

**পর্যায় ২ — State ও lifecycle (প্রতিদিনের কাজ)।**
→ [Q6 Lifecycle](#q6) · [Q9 InheritedWidget ও Provider](#q9) · [Q3 Keys](#q3) · [Q2 Widget immutable কেন](#q2)

**পর্যায় ৩ — Layout (যেখানে bug হয়)।**
→ [Q13 Constraints নিচে, size উপরে](#q13) · [Q15 RenderFlex overflow](#q15) · [Q14 BoxConstraints](#q14) · [Q16 MediaQuery বনাম LayoutBuilder](#q16)

**পর্যায় ৪ — Performance (senior হওয়ার লক্ষণ)।**
→ [Q10 const ও rebuild](#q10) · [Q12 60/120fps ও thread](#q12) · [Q11 RepaintBoundary](#q11) · [Q4 Reconciliation](#q4)

**পর্যায় ৫ — গভীর internals (tie-breaker, সবার শেষে)।**
→ [Q17 Rendering pipeline](#q17) · [Q18 Impeller বনাম Skia](#q18) · [Q22 তিনটি layer](#q22) · [Q23 Engine-এর ভেতরে JIT বনাম AOT](#q23) · [Q19 Hot reload](#q19) · [Q20 pubspec](#q20) · [Q21 Channel](#q21)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই আটটা দেখে নিন:
[Q1](#q1) · [Q3](#q3) · [Q5](#q5) · [Q7](#q7) · [Q8](#q8) · [Q12](#q12) · [Q13](#q13) · [Q15](#q15), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. তিনটি tree ও widget identity

---

## <a id="q1"></a>1. Flutter-এর তিনটি tree ব্যাখ্যা করুন — Widget, Element, আর RenderObject। Flutter-এর তিনটাই কেন দরকার?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flutter তিনটা tree রাখে, যারা একসাথে কাজ করে। Widget tree হলো সস্তা blueprint, যেটা আমি code-এ লিখি। Element tree হলো জীবন্ত সেতু, যেটা প্রতিটা widget-এর জায়গা আর state মনে রাখে। RenderObject tree আসল layout আর painting-এর কাজ করে। Flutter-এর তিনটাই দরকার, যাতে সস্তা widget-গুলো বারবার ফেলে দিয়ে নতুন বানানো যায়, আর নিচের ব্যয়বহুল render object-গুলো reuse করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: blueprint, site manager, বিল্ডিং।**
একটা বাড়ি বানানোর কথা ভাবুন:
- **Widget** হলো *blueprint* — এক টুকরো কাগজ, যেখানে লেখা "এখানে নীল দরজা।" কাগজ সস্তা; আপনি বারবার আঁকতে পারেন।
- **Element** হলো *site manager* — একজন আসল মানুষ, যিনি ওই জায়গায় দাঁড়িয়ে থাকেন, মনে রাখেন সেখানে কী বানানো হয়েছিল, আর ঠিক করেন আসলে কী বদলানো দরকার।
- **RenderObject** হলো *আসল বিল্ডিং* — ইট আর দেয়াল। বানাতে ব্যয়বহুল, তাই ছোট একটা পরিবর্তনের জন্য আপনি সেটা ভাঙেন না।

**ধাপ ২ — Widget tree (সস্তা blueprint, immutable)।**
Widget হলো সেই object, যেগুলো আপনি লেখেন। এরা শুধু UI-কে *বর্ণনা* করে। এরা immutable আর সস্তা। তাই Flutter খুশি মনে এগুলো ফেলে দেয় আর প্রতিটা rebuild-এ নতুন বানায়।

```dart
Container(
  color: Colors.blue,
  child: const Text('Hello'),
)
```

**ধাপ ৩ — Element tree (জীবন্ত সেতু)।**
একটা widget প্রথমবার দেখানোর সময়ে Flutter সেটাকে "inflate" করে **Element**-এ পরিণত করে। Element ওই widget-এর tree-তে অবস্থান ধরে রাখে, `State` object রাখে (stateful widget-এর জন্য), আর render object-এর দিকে নির্দেশ করে। Element-রা দীর্ঘজীবী — এরা rebuild-এর পরেও টিকে থাকে। ঠিক এই কারণেই আপনার state টিকে যায়।

**ধাপ ৪ — RenderObject tree (আসল layout আর paint)।**
Render object জানে তার নিজের size আর position, আর জানে কীভাবে paint করতে হয়। এগুলো বানানো ব্যয়বহুল, তাই Flutter নতুন বানানো এড়িয়ে চলে।

```dart
// আপনি যা লেখেন:     Container → Text
// Element tree:      ContainerElement → TextElement   (দীর্ঘজীবী)
// RenderObject tree: RenderDecoratedBox → RenderParagraph (ব্যয়বহুল, reuse হয়)
```

**ধাপ ৫ — তিনটা কেন? মূল কথা হলো গতি।**
প্রতিটা `setState`-এ Flutter একটা নতুন Widget tree বানায় (সস্তা)। Element পুরোনো widget আর নতুন widget-কে দেখে। Type আর key মিলে গেলে সে একই element আর একই render object রেখে দেয়। শুধু যে property বদলেছে সেটাই update করে — যেমন color।

```dart
// setState চলল → নতুন একটা Container widget তৈরি হলো
// Element দেখে: একই type? একই key? → হ্যাঁ
// → আগের RenderDecoratedBox-টাই REUSE করা হলো, শুধু color বদলাল
// → নতুন render object নেই, subtree-র পুরো rebuild নেই
```

অর্থাৎ: widget level-এ সস্তা rebuild, আর render level-এ ব্যয়বহুল object reuse। এভাবেই Flutter সেকেন্ডে ৬০+ বার rebuild করতে পারে, তবু মরে যায় না।

**Interviewer কেন জিজ্ঞেস করে:** এটাই Flutter architecture-এর সবচেয়ে মৌলিক প্রশ্ন। তাঁরা দেখতে চান আপনি performance model-টা বোঝেন কি না — শুধু widget কীভাবে ব্যবহার করতে হয় তা নয়, বরং বারবার rebuild করা কেন সস্তা সেটাও।

**সাধারণ ভুল:** বলা যে "widget হলো screen-এ যা দেখা যায়।" Widget screen-এ **থাকে না** — RenderObject থাকে। Widget শুধু configuration। আরেকটা ভুল হলো Element tree-র অস্তিত্বই না জানা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কোনটা কোথায় থাকে?"* → Widget রাখে config। Element রাখে `State` আর tree-তে অবস্থান। Render object রাখে size, position আর paint।
- *"State Widget-এ না রেখে Element-এ কেন?"* → কারণ প্রতিটা rebuild-এ widget ফেলে দেওয়া হয়। State-কে এমন কিছুতে থাকতে হবে যেটা দীর্ঘজীবী — অর্থাৎ element।

**সম্পর্কিত:** [Q2 — widget immutable কেন](#q2) · [Q4 — reconciliation](#q4) · [Q8 — BuildContext আসলে element](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Flutter widget-গুলো immutable কেন? প্রতি frame-এ নতুন widget বানালে কি memory নষ্ট হয় না?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Widget immutable, কারণ এরা শুধু UI-এর একটা বর্ণনা। আর বর্ণনা আপনার অজান্তে বদলে যাওয়া উচিত নয়। নতুন widget বানানো সস্তা — এরা ছোট্ট config object, আর Dart-এর garbage collector ঠিক এই 'বানাও আর ফেলে দাও' ধরনের জন্যই তৈরি। ব্যয়বহুল জিনিস, মানে render object, আবার বানানো হয় না; element tree-র মাধ্যমে সেগুলো reuse হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Immutable মানে "বানানোর পরে আর বদলানো যায় না।"**
একটা widget-এর সব field-ই `final`। একবার `Text('Hi')` বানালে সেই object আর কখনো বদলায় না। নতুন text দেখাতে হলে আপনি একেবারে নতুন একটা `Text` widget বানান।

```dart
class Greeting extends StatelessWidget {
  final String name;            // final — বদলানো যাবে না
  const Greeting({required this.name});
  // ...
}
```

**ধাপ ২ — Immutable হওয়া কেন ভালো।**
Widget হলো এই মুহূর্তে UI দেখতে কেমন হওয়া উচিত, তার একটা *snapshot*। Widget যদি নিজে নিজে চুপচাপ বদলে যেতে পারত, তাহলে rebuild-এর সময়ে পুরোনো আর নতুন তুলনা করার জন্য Flutter তাকে বিশ্বাস করতে পারত না। Immutability "কিছু কি বদলেছে?" এই check-টাকে সহজ আর নিরাপদ করে।

**ধাপ ৩ — কিন্তু প্রতি frame-এ নতুন object বানানো কি অপচয় নয়?**
এটাই মূল দুশ্চিন্তা, আর উত্তর হলো না — দুটো কারণে:
1. Widget **খুব ছোট** — মাত্র কয়েকটা field। একটা বানানো প্রায় বিনামূল্যে।
2. Dart-এর garbage collector "বেশিরভাগ object অল্প বয়সে মরে" — এই নকশায় চলে। অল্প সময় বাঁচা object (যেমন widget) খুব সস্তায় পরিষ্কার হয়ে যায়।

**ধাপ ৪ — ব্যয়বহুল জিনিসগুলো আবার বানানো হয় না।**
আপনি সস্তা Widget tree rebuild করেন, কিন্তু ব্যয়বহুল RenderObject tree Element tree-র মাধ্যমে reuse হয় ([Q1](#q1) দেখুন)। তাই "প্রতি frame-এ নতুন widget" মানে **এটা নয়** যে "প্রতি frame-এ নতুন layout object।"

```dart
// Rebuild: নতুন Text('1') widget বানানো হলো (সস্তা)
// Element একই RenderParagraph (ব্যয়বহুল) reuse করে আর তার text update করে
```

**ধাপ ৫ — এখান থেকে যে বাস্তব নিয়ম আসে।**
Rebuild সস্তা বলে আপনার এর সাথে লড়াই করা উচিত নয়। বরং rebuild ছোট রাখুন আর `const` ব্যবহার করুন, যাতে অপরিবর্তিত অংশ পুরোপুরি বাদ পড়ে যায় ([Q10](#q10) দেখুন)।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি বোঝেন যে "rebuild" নকশা অনুযায়ীই সস্তা। আর ভয় পেয়ে rebuild এড়াতে আপনি আজেবাজে code লিখবেন না।

**সাধারণ ভুল:** rebuild ব্যয়বহুল ভেবে সব জায়গায় "rebuild এড়ানোর" প্রাণপণ চেষ্টা করা। Rebuild নিজেই সস্তা; আসল ব্যাপার হলো `build()` হালকা রাখা আর `const` ব্যবহার করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Widget যদি immutable হয়, তাহলে UI বদলায় কীভাবে?"* → আপনি একটা নতুন widget tree বানান; element সেটার সাথে পার্থক্য মিলিয়ে দেখে আর শুধু যা বদলেছে তা update করে।
- *"তাহলে বদলে যাওয়া data থাকে কোথায়?"* → `State` object-এ (element-এর উপরে), widget-এ নয়।

**সম্পর্কিত:** [Q1 — তিনটি tree](#q1) · [Q10 — const rebuild বাদ দেয়](#q10) · [Q7 — setState](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. Flutter-এ Keys কী? ValueKey, ObjectKey, UniqueKey, GlobalKey আর LocalKey কখন ব্যবহার করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Keys widget identity-র সমস্যা সমাধান করে। Flutter rebuild করার সময় পুরোনো আর নতুন widget-কে type আর key দিয়ে মেলায়। Key না থাকলে একই type-এর widget-গুলোকে position দিয়ে মেলায়। তাই list reorder করলে ভুল item-এ ভুল state লেগে যায়। আমি list item-এর জন্য stable id সহ `ValueKey` ব্যবহার করি। আর `GlobalKey` শুধু তখনই ব্যবহার করি যখন সত্যিই বাইরে থেকে কোনো widget-এর state-এ পৌঁছাতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সমস্যাটা: একই type, ভুল identity।**
Flutter যখন একই type-এর widget-এর একটা list update করে, আর কোনো key থাকে না, তখন সে position দিয়ে মেলায়। তাই দুটো item জায়গা বদল করলে state (টাইপ করা text, scroll position, animation) পুরোনো position-এই থেকে যায় — ভুল item-এর সাথে লেগে থাকে।

```dart
// key ছাড়া — এই দুটো swap করলে এদের state ভেঙে যায়,
// কারণ Flutter index দিয়ে match করে, item দিয়ে নয়।
Column(children: [
  TextField(),  // টাইপ করা text index 0-তেই থেকে যায়
  TextField(),  // item দুটো swap হলেও
])
```

**ধাপ ২ — Key হলো নাম-ট্যাগের মতো।**
Key Flutter-কে বলে — "এটা আগের *সেই* widget, জায়গা বদলালেও।" এখন Flutter slot-কে নয়, widget-কে অনুসরণ করে।

**ধাপ ৩ — `LocalKey` আর তার তিন ধরন (sibling-দের মধ্যে unique)।**
`LocalKey` হলো সেই key-গুলোর base, যেগুলোর শুধু sibling-দের মধ্যে (একই parent) unique হলেই চলে।
- **`ValueKey<T>`** — একটা value থেকে identity, `==` দিয়ে। যখন স্বাভাবিক একটা id আছে, যেমন database id বা email, তখন এটাই সবচেয়ে ভালো।
- **`ObjectKey`** — একটা object-এর reference থেকে identity (`identical`)। যখন দুটো object `==` হিসেবে সমান হতে পারে, কিন্তু reference দিয়ে আলাদা করতেই হবে, তখন ব্যবহার করুন।
- **`UniqueKey`** — প্রতিটা instance আলাদা। নতুন element/state *জোর করে* বানাতে ব্যবহার করুন ("এটাকে একদম নতুন ধরো")।

```dart
// stable id সহ ValueKey — state item-এর সাথে সাথে যায়
Column(
  children: items.map((item) => Dismissible(
    key: ValueKey(item.id),
    child: ListTile(title: Text(item.name)),
  )).toList(),
)
```

**ধাপ ৪ — `GlobalKey` (পুরো app জুড়ে unique)।**
`GlobalKey` পুরো app-এ unique। এটা দিয়ে বাইরে থেকে কোনো widget-এর `State` বা render object-এ পৌঁছানো যায়। সবচেয়ে পরিচিত ব্যবহার হলো form validation।

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

**ধাপ ৫ — ইচ্ছা করে নতুন widget বানানো।**
Key বদলে দিলে Flutter পুরোনো element ফেলে দেয় এবং নতুন একটা বানায়। `AnimatedSwitcher` এভাবেই বুঝতে পারে কখন animate করতে হবে:

```dart
AnimatedSwitcher(
  duration: const Duration(milliseconds: 300),
  child: Text('$_counter', key: ValueKey<int>(_counter)),
  // নতুন value → নতুন key → নতুন element → animation চলে
)
```

**Interviewer কেন জিজ্ঞেস করে:** এটা আলাদা করে দেয় — কে শুধু layout-এর bug তালি দিয়ে ঠিক করে, আর কে reconciliation algorithm বোঝে। Key-এর ভুল ব্যবহারে list আর animation-এ সূক্ষ্ম, কঠিন-করে-reproduce-করা bug তৈরি হয়।

**সাধারণ ভুল:** "নিরাপদ থাকার জন্য" সব জায়গায় `GlobalKey` ব্যবহার করা। এটা ব্যয়বহুল (global registry-তে lookup করতে হয়) আর কিছু optimization বন্ধ করে দেয়। আরেকটা পরিচিত ভুল: reorderable list-এ list-এর *index*-কে key হিসেবে ব্যবহার করা — reorder করলে index বদলে যায়, তাই পুরো উদ্দেশ্যটাই নষ্ট হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Index-কে key হিসেবে দেওয়া — খারাপ কেন?"* → Reorder করলে index সরে যায়, তাই Flutter আবার position দিয়েই মেলায়। একটা stable id ব্যবহার করুন (`ValueKey(item.id)`)।
- *"`UniqueKey` কখন সঠিক?"* → যখন আপনি *চান* সবকিছু নতুন করে rebuild হোক, যেমন animation আবার চালাতে বা state reset করতে।

**সম্পর্কিত:** [Q4 — reconciliation](#q4) · [Q1 — তিনটা tree](#q1) · [Q6 — state থাকে element-এ](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. Flutter কীভাবে ঠিক করে একটা widget reuse করবে না rebuild করবে? (Reconciliation)

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"প্রতিটা rebuild-এ Flutter নতুন widget tree-টা পুরোনো element tree-র পাশাপাশি ধরে হাঁটে। প্রতিটা জায়গায় একটাই প্রশ্ন করে: নতুন widget-এর type আর key কি পুরোনোটার মতোই? হ্যাঁ হলে element আর render object reuse করে, শুধু property-গুলো update করে। না হলে পুরোনোটা ফেলে দিয়ে নতুন একটা inflate করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Reconciliation হলো "কী বদলালো?" ধাপটা।**
`build()` নতুন widget tree বানানোর পর Flutter-কে ওই সস্তা blueprint-গুলোকে আসল update-এ বদলাতে হয়, সবকিছু নতুন করে না বানিয়ে। এই মেলানোর কাজটাকেই বলে reconciliation (বা diffing)।

**ধাপ ২ — নিয়ম: একই `runtimeType` এবং একই `key` → reuse।**
প্রতিটা position-এ Flutter পুরোনো widget-এর সাথে নতুন widget-কে তুলনা করে:
- একই type আর একই key → element আর render object **reuse**, শুধু যে field বদলেছে সেটা update।
- ভিন্ন type বা ভিন্ন key → পুরোনো element (আর তার state) **ফেলে দেয়** এবং নতুন একটা বানায়।

```dart
// পুরোনো: Container(color: blue)   নতুন: Container(color: red)
// একই type, একই key → RenderDecoratedBox reuse হবে, শুধু color বদলাবে।

// পুরোনো: Container(...)           নতুন: SizedBox(...)
// ভিন্ন type → পুরোনো element + state ফেলে দিয়ে নতুন SizedBox বানাবে।
```

**ধাপ ৩ — এটা হয় position ধরে, উপর থেকে নিচে।**
Flutter মিল খুঁজতে পুরো tree তল্লাশি করে না। সে position ধরে ধরে তুলনা করে। এই কারণেই key ছাড়া list reorder করলে সে গুলিয়ে ফেলে — slot 1-এর widget-কে তুলনা করা হয় আগে slot 1-এ যা ছিল তার সাথে।

**ধাপ ৪ — Keys position-এর মেলানো ছাপিয়ে যায়।**
Key থাকলে Flutter slot-এর বদলে identity দিয়ে মেলাতে পারে। তাই সে element-টাকে নতুন position-এ সরিয়ে নিয়েও তার state ধরে রাখতে পারে (দেখুন [Q3](#q3))।

**ধাপ ৫ — Performance-এর জন্য এটা কেন গুরুত্বপূর্ণ।**
Reuse করলে ব্যয়বহুল render object-গুলো থেকে যায়। তাই একটা rebuild সাধারণত শুধু "কয়েকটা property update" মাত্র। এই ব্যবস্থাটাই তিন-tree-র design-কে (দেখুন [Q1](#q1)) বাস্তবে দ্রুত করে।

**Interviewer কেন জিজ্ঞেস করে:** এটা প্রমাণ করে আপনি বোঝেন keys *কেন* আছে, আর widget-এর type বদলালে তার state *কেন* reset হয়। এটা তিনটা tree-কে বাস্তব আচরণের সাথে যোগ করে।

**সাধারণ ভুল:** এটা ভাবা যে Flutter একটা গভীর "smart diff" করে, যা সরে যাওয়া widget-কে যেকোনো জায়গায় খুঁজে পায়। সে শুধু type আর key দেখে, position ধরে ধরে — এই কারণেই keys লাগে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Type বদলে গেলে State-এর কী হয়?"* → পুরোনো element আর তার `State` ফেলে দেওয়া হয়; একদম নতুন একটা `State` তৈরি হয়।
- *"একটা widget-কে নতুন parent দিয়ে মুড়ে দিলে তার state reset হয় কেন?"* → Tree-তে তার position/type বদলে গেছে, তাই সে আর পুরোনো element-এর সাথে মেলে না।

**সম্পর্কিত:** [Q3 — keys](#q3) · [Q1 — তিনটা tree](#q1) · [Q10 — const এটাকে short-circuit করে](#q10)

[↑ উপরে ফিরুন](#toc)

---

# B. Widgets আর state

---

## <a id="q5"></a>5. StatelessWidget আর StatefulWidget-এর পার্থক্য কী? ভেতরে কী আলাদা?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"StatelessWidget-এ বদলে যাওয়া data থাকে না — parent নতুন input দিলে তবেই সে rebuild হয়। StatefulWidget বদলে যাওয়া data রাখে আলাদা একটা `State` object-এ, আর `setState` call করে নিজেই নিজেকে rebuild করতে পারে। ভেতরের মূল কথাটা হলো: `State` থাকে Element-এ, widget-এ নয়। এই কারণেই rebuild-এর পরেও state টিকে থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — StatelessWidget: output শুধু input-এর উপর নির্ভর করে।**
এটা নিজে থেকে বদলাতে পারে না। একই input দিলে সে সবসময় একই জিনিস build করে। Parent নতুন constructor value পাঠালে তবেই সে rebuild হয়।

```dart
class Greeting extends StatelessWidget {
  final String name;
  const Greeting({required this.name});

  @override
  Widget build(BuildContext context) => Text('Hello, $name');
}
```

**ধাপ ২ — StatefulWidget: বদলে যাওয়া data নিজে রাখে।**
এটা একটা immutable widget-কে একটা দীর্ঘজীবী `State` object-এর সাথে জোড়া লাগায়। `State` নিজের field বদলাতে পারে, আর `setState` call করে rebuild করাতে পারে।

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

**ধাপ ৩ — ভেতরের পার্থক্য (এটাই senior-level কথা)।**
- `StatelessWidget` → একটা `StatelessElement` বানায় → element `widget.build(context)` call করে।
- `StatefulWidget` → একটা `StatefulElement` বানায় → element একবার `createState()` call করে, তারপর `state.build(context)` call করে।

`State` object যুক্ত থাকে **Element**-এর সাথে, যেটা দীর্ঘজীবী। Widget নিজে প্রতিটা rebuild-এ ফেলে দেওয়া হয়। ঠিক এই কারণেই `_count` টিকে থাকে: এটা থাকে element-এর `State`-এ, widget-এ নয়।

**ধাপ ৪ — কোনটা কখন ব্যবহার করবেন।**
- `StatelessWidget` — যখন সবকিছু constructor বা inherited data থেকে আসে (একটা styled label, একটা layout wrapper)।
- `StatefulWidget` — যখন widget নিজের কাছে এমন data রাখে যা তার জীবনকালে বদলায় (একটা form field, একটা `AnimationController`, একটা toggle)।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা state-ownership-এর model শুনতে চান, শুধু syntax নয়। "`State` থাকে element-এ" — এটা বললে আসল বোঝাপড়া দেখা যায়।

**সাধারণ ভুল:** বলা যে "StatelessWidget বদলাতে পারে না।" সে অবশ্যই parent-এর নতুন data নিয়ে rebuild হতে পারে — শুধু নিজে নিজের rebuild চালু করতে পারে না। আরেকটা: `StatelessWidget` আর একটা state manager (Provider, Riverpod, BLoC) দিয়ে পরিষ্কার সমাধান হতো, তবু `StatefulWidget`-এর দিকে হাত বাড়ানো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Widget আর State-কে দুটো class-এ ভাগ করা হয় কেন?"* → যাতে widget immutable আর ফেলে দেওয়ার মতো হতে পারে, আর `State` element-এ বেঁচে থাকতে পারে।
- *"StatelessWidget কি কখনো rebuild হয়?"* → হ্যাঁ, যখনই parent তাকে নতুন configuration দিয়ে rebuild করে, বা সে যে `InheritedWidget`-এর উপর নির্ভর করে সেটা বদলায়।

**সম্পর্কিত:** [Q6 — lifecycle](#q6) · [Q7 — setState](#q7) · [Q2 — immutability](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. পুরো StatefulWidget lifecycle ধাপে ধাপে বলুন। কোন method কখন call হয়, আর সেখানে আপনি কী করেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"ক্রমটা হলো: প্রথমে `createState`, তারপর একবারের setup-এর জন্য `initState`, তারপর `didChangeDependencies` — এখানে inherited widget পড়া নিরাপদ, তারপর `build`। Widget বেঁচে থাকা অবস্থায় parent নতুন config দিলে `didUpdateWidget` চলে, আর প্রতিটা rebuild-এ `build` চলে। শেষে `deactivate`, তারপর `dispose` — সেখানে আমি controller আর subscription পরিষ্কার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `createState()`।**
Framework যখন widget-টি inflate করে তখন একবারই call হয়। এটা `State` object তৈরি করে। আপনি নিজে কখনো এটা call করবেন না।

**ধাপ ২ — `initState()`।**
`State` তৈরি হয়ে tree-তে বসার ঠিক পরেই একবার call হয়। একবারের setup এখানে করুন: `AnimationController` তৈরি, stream-এ subscribe, শুরুর মান বসানো। এখানে inherited-widget lookup আপনি **করতে পারবেন না** (element তখনো পুরোপুরি mount হয়নি)।

**ধাপ ৩ — `didChangeDependencies()`।**
`initState`-এর ঠিক পরেই call হয়। আর আপনি যে `InheritedWidget`-এর উপর নির্ভরশীল, সেটা বদলালে আবারও call হয়। `Theme.of` বা `MediaQuery.of`-এর মতো inherited lookup-এর জন্য `context` ব্যবহারের এটাই প্রথম **নিরাপদ** জায়গা।

**ধাপ ৪ — `build()`।**
Widget-টিকে যখনই render করতে হবে তখনই call হয়: `setState`-এর পরে, `didChangeDependencies`-এর পরে, অথবা parent rebuild হলে। এটা **pure আর দ্রুত** হতেই হবে — কোনো side effect নয়, কোনো ভারী কাজ নয়।

**ধাপ ৫ — `didUpdateWidget(oldWidget)`।**
Parent rebuild হয়ে একই type-এর নতুন widget দিলে call হয়। পুরোনো আর নতুন config তুলনা করুন, তারপর সেই অনুযায়ী কাজ করুন — যেমন duration বদলালে controller-টা update করুন।

**ধাপ ৬ — `deactivate()`, তারপর `dispose()`।**
Element tree থেকে সরে গেলে `deactivate` চলে (`GlobalKey` দিয়ে এটা আবার বসানো হতে পারে)। `State` একেবারে চলে গেলে `dispose` চলে। সব পরিষ্কার `dispose`-এ করুন: timer cancel করুন, controller dispose করুন, stream বন্ধ করুন, listener সরান।

```dart
class _MyWidgetState extends State<MyWidget>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final StreamSubscription _sub;

  @override
  void initState() {
    super.initState();                         // super সবার আগে call করুন
    _controller = AnimationController(
      vsync: this,
      duration: widget.duration,
    );
    _sub = myStream.listen(_onData);
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final locale = Localizations.localeOf(context); // এখানে নিরাপদ
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
    super.dispose();                           // super সবার শেষে call করুন
  }

  @override
  Widget build(BuildContext context) => const SizedBox();
}
```

**Interviewer কেন জিজ্ঞেস করে:** এটা সরাসরি দেখে আপনি leak-মুক্ত code লেখেন কি না। একটা বাদ পড়া `dispose()` হলো memory leak আর "setState called after dispose" crash-এর সবচেয়ে সাধারণ কারণগুলোর একটা।

**সাধারণ ভুল:** `super.initState()` আগে আর `super.dispose()` শেষে দিতে ভুলে যাওয়া। `initState`-এ inherited lookup (`MediaQuery.of`) করা। `dispose`-এ listener cancel না করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"initState-এ MediaQuery পড়া যায় না কেন?"* → Element তখনো mount হয়নি, তাই inherited ancestor-দের কাছে পৌঁছানো যায় না। `didChangeDependencies` ব্যবহার করুন।
- *"`didChangeDependencies` আর `didUpdateWidget`-এর পার্থক্য কী?"* → `didChangeDependencies` inherited-widget বদলের সাড়া দেয়; `didUpdateWidget` parent-এর নতুন config দেওয়ার সাড়া দেয়।

**সম্পর্কিত:** [Q8 — BuildContext](#q8) · [Q7 — setState](#q7) · [Q9 — InheritedWidget](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. `setState` আসলে কী করে? এটা শুধু "screen refresh করা" নয় কেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`setState` দুটো কাজ করে: আমি যে function দিই সেটা চালায়, ফলে আমি আমার state field বদলাতে পারি। তারপর এই element-কে dirty চিহ্নিত করে, ফলে Flutter পরের frame-এ একটা rebuild schedule করে। এটা সাথে সাথে paint করে না, আর পুরো app rebuild করে না — শুধু এই element-এর subtree rebuild হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `setState` মানে "data বদলাও, তারপর dirty চিহ্ন দাও"।**
আপনি যে function pass করেন, সেখানেই field-গুলো বদলান। সেটা চলার পর `setState` element-এর উপর `markNeedsBuild()` call করে। এটা element-টিকে dirty element-এর তালিকায় যোগ করে।

```dart
setState(() {
  _count++;          // data এখানে বদলান
});
// Flutter এখন জানে: এই element dirty, পরের frame-এ rebuild করতে হবে
```

**ধাপ ২ — এটা এখনই rebuild করে না।**
`setState` সাথে সাথে paint করে না। Flutter পরের vsync (frame)-এর জন্য অপেক্ষা করে, তারপর সব dirty element একসাথে rebuild করে। তাই পরপর পাঁচবার `setState` call করলেও rebuild হয় একবারই।

**ধাপ ৩ — শুধু এই subtree rebuild হয়, পুরো app নয়।**
Flutter dirty element থেকে নিচের দিকে rebuild করে। Parent আর sibling-দের হাত দেওয়া হয় না (যদি না তাদেরও dirty চিহ্ন দেওয়া থাকে)। এই কারণেই `const` child বাদ পড়ে যায় — তারা বদলায়নি (দেখুন [Q10](#q10))।

**ধাপ ৪ — function form কেন (শুধু একটা flag নয় কেন)?**
বদলটা `setState(() { ... })`-এর *ভেতরে* রাখলে স্পষ্ট বোঝা যায় কোন state বদলেছে। আর এটা নিশ্চিত করে যে rebuild schedule হওয়ার আগেই বদলটা ঘটে গেছে। বাইরে field বদলে তারপর `setState(() {})` call করলেও কাজ হয়, কিন্তু সেটা খারাপ style ধরা হয়।

**ধাপ ৫ — এক নম্বর bug: dispose-এর পরে `setState`।**
Widget চলে যাওয়ার পরে কোনো async কাজ শেষ হলে, `setState` call করলে crash হয়। `mounted` দিয়ে পাহারা দিন:

```dart
Future<void> load() async {
  final data = await api.fetch();
  if (!mounted) return;      // widget নেই? এখানেই থামুন
  setState(() => _data = data);
}
```

**Interviewer কেন জিজ্ঞেস করে:** অনেকে ভাবেন `setState` সাথে সাথে সবকিছু আবার আঁকে। তাঁরা শুনতে চান: এটা dirty চিহ্ন দেয় আর পরের frame-এ এই subtree-র একটা rebuild schedule করে।

**সাধারণ ভুল:** `setState` callback-এর *ভেতরে* ভারী কাজ করা। Callback-এ শুধু field assign করা উচিত। আগে হিসাব করুন, তারপর ফলাফল assign করতে `setState` করুন। আর async code-এ `mounted` check ভুলে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`setState` কি parent rebuild করে?"* → না। এটা এই element-কে dirty চিহ্ন দেয়; rebuild এখান থেকে শুরু হয়ে নিচে যায়।
- *"দ্রুত ৩ বার setState call করলে কী হয়?"* → পরের frame-এ rebuild হবে একবারই; dirty element-গুলো একসাথে batch হয়।

**সম্পর্কিত:** [Q5 — Stateful state element-এ থাকে](#q5) · [Q10 — const rebuild বাদ দেয়](#q10) · [Q12 — frame](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. BuildContext কী? `initState` শেষ হওয়ার আগে এটা ব্যবহার করা যায় না কেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"BuildContext আসলে Element *নিজেই* — `Element` `BuildContext` implement করে। এটা element tree-তে এই widget-এর ঠিক অবস্থান বোঝায়। এর মাধ্যমেই আপনি উপরে উঠে inherited widget, theme বা media data খুঁজে পান। `initState`-এ inherited lookup-এর জন্য এটা ব্যবহার করা যায় না, কারণ element তখনো tree-তে পুরোপুরি mount হয়নি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বড় রহস্য ফাঁস: context-ই element।**
মানুষ `context`-কে কোনো জাদুর handle ভাবেন। Flutter source-এ লেখা আছে `abstract class Element implements BuildContext`। তাই আপনি যখন `context` ব্যবহার করেন, তখন আপনি সেই element node-এর সাথেই কথা বলছেন, যেটা আপনার widget-এর অবস্থান ধরে রাখে।

**ধাপ ২ — এটা কী বোঝায়: tree-তে আপনার জায়গা।**
এটা আপনারই element, তাই এটা আপনার ancestor-দের চেনে। `Theme.of(context)`, `MediaQuery.of(context)` আর `Navigator.of(context)` এভাবেই কাজ করে — তারা আপনার element থেকে উপরে উঠে সবচেয়ে কাছের মিল-খাওয়া ancestor খুঁজে নেয়।

**ধাপ ৩ — `initState`-এ inherited lookup কেন করা যায় না।**
`initState` চলার সময় element থাকে ঠিকই, কিন্তু tree-তে তখনো পুরোপুরি *active* নয়। তাই তার জন্য inherited-widget ancestor chain-এ পৌঁছানো যায় না। `dependOnInheritedWidgetOfExactType`-এর জন্য element-কে active হতে হয়। ফলে সেখানে lookup crash করে বা null দেয়।

```dart
@override
void initState() {
  super.initState();
  // ভুল — element এখনো পুরোপুরি mount হয়নি:
  // final size = MediaQuery.of(context).size;

  // ঠিক আছে — widget config পড়তে tree-তে হাঁটা লাগে না:
  print(widget.title);
}

@override
void didChangeDependencies() {
  super.didChangeDependencies();
  // সঠিক — tree-তে হাঁটার প্রথম নিরাপদ জায়গা:
  final size = MediaQuery.of(context).size;
}
```

**ধাপ ৪ — async ফাঁদ: "বাসি" context।**
`await`-এর পরে widget-টি হয়তো ইতিমধ্যে dispose হয়ে গেছে। তখন তার context মৃত। সেটা ব্যবহার করলে "looking up a deactivated widget's ancestor" error আসে। সবসময় আগে `mounted` check করুন।

```dart
Future<void> go() async {
  await Future.delayed(const Duration(seconds: 2));
  if (!mounted) return;
  Navigator.of(context).pop();   // এখন নিরাপদ
}
```

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি tree mounting বোঝেন কি না। আর compile-time widget config আর runtime tree সম্পর্কের পার্থক্য বোঝেন কি না।

**সাধারণ ভুল:** বলা যে "context হলো widget-এর একটা reference"। এটা তা নয় — এটা element **নিজেই**। আর widget চলে যাওয়ার সম্ভাবনা থাকা সত্ত্বেও async callback-এ context ব্যবহার করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"initState-এ `context.read` কাজ করে কিন্তু `context.watch` করে না কেন?"* → দুটোরই শেষ পর্যন্ত active element লাগে; `initState`-এ পড়ার কাজ শুধু `context.read` দিয়ে খুব সাবধানে করুন। আর inherited data-র উপর নির্ভরশীল যেকোনো কিছুর জন্য `didChangeDependencies` বেছে নিন।
- *"`mounted` কী?"* → `State`-এর উপর একটা flag, element tree-তে থাকা অবস্থায় এটা true থাকে। `await`-এর পরে `context` ব্যবহারের আগে এটা check করুন।

**সম্পর্কিত:** [Q1 — context-ই element](#q1) · [Q6 — lifecycle](#q6) · [Q9 — InheritedWidget lookup](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. InheritedWidget কী? এটা কীভাবে নিচে data পাঠায়, আর Provider কীভাবে এর উপরে তৈরি?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"InheritedWidget tree-র নিচের দিকে data ঠেলে দেয়। ফলে যেকোনো descendant `dependOnInheritedWidgetOfExactType` দিয়ে O(1)-তে সেটা পড়তে পারে। এটা update হলে শুধু সেই widget-গুলো rebuild হয় যারা এর উপরে dependency *register* করেছে — পুরো subtree নয়। Provider হলো এর উপরে একটা বন্ধুত্বপূর্ণ wrapper। এটা lifecycle, lazy creation আর `context.watch` ও `Consumer`-এর মতো পরিষ্কার API যোগ করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সমস্যা: অনেক layer পার করে data পাঠানো।**
এটা ছাড়া প্রতিটা constructor দিয়ে data নিচে পাঠাতে হতো ("prop drilling")। InheritedWidget একটা গভীর child-কে সরাসরি data ধরতে দেয়।

**ধাপ ২ — Child কীভাবে পড়ে (আর কেন এটা দ্রুত)।**
Framework প্রতিটা element-এ type অনুযায়ী inherited widget-এর একটা map রাখে। তাই সবচেয়ে কাছেরটা খুঁজে পাওয়া O(1) — ধীর কোনো walk নয়। এই call আপনার element-কে dependent হিসেবেও *register* করে।

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

// যেকোনো descendant:
final theme = AppTheme.of(context);   // O(1) lookup + dependency register করে
```

**ধাপ ৩ — শুধু dependent-রাই rebuild হয় (মূল দক্ষতা)।**
InheritedWidget বদলে গেলে আর `updateShouldNotify` true দিলে framework `didChangeDependencies` call করে। তারপর **শুধু register হওয়া dependent-দের** rebuild-এর জন্য mark করে — পুরো subtree নয়।

**ধাপ ৪ — `dependOn...` বনাম `getInheritedWidget...`।**
- `dependOnInheritedWidgetOfExactType` → পড়ে **এবং** একটা dependency register করে (পরিবর্তনে আপনি rebuild হন)।
- `getInheritedWidgetOfExactType` → শুধু পড়ে, কোনো dependency নেই, কোনো rebuild নেই।

**ধাপ ৫ — Provider কীভাবে এর উপরে বসে।**
Provider ভেতরে একটা InheritedWidget বানায় আর আপনাকে সুন্দর API দেয়: `context.watch<T>()` (পড়ে + rebuild), `context.read<T>()` (একবার পড়ে, rebuild নেই), আর `Consumer<T>`। এটা lazy creation, resource dispose করা, আর `ChangeNotifier` দিয়ে change notification-ও সামলায়।

```dart
ChangeNotifierProvider<CartModel>(
  create: (_) => CartModel(),
  child: Consumer<CartModel>(
    builder: (ctx, cart, _) => Text('${cart.itemCount}'),
  ),
)
```

**Interviewer কেন জিজ্ঞেস করে:** InheritedWidget প্রায় প্রতিটা state solution-এর মেরুদণ্ড — Provider, Riverpod-এর `ProviderScope`, Theme, MediaQuery, Navigator। এটা বোঝা মানে Flutter-এ data কীভাবে চলে সেটা বোঝা।

**সাধারণ ভুল:** ভাবা যে এটা পুরো subtree rebuild করে। শুধু register হওয়া dependent-রাই rebuild হয়। আরেকটা ভুল — `dependOn...` (register করে + rebuild করে) আর `get...` (শুধু পড়ে) গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`updateShouldNotify` কী?"* → Inherited data বদলালে dependent-রা rebuild হবে কি না, এটা সেটাই ঠিক করে। মান সত্যিই বদলালে তবেই true দিন।
- *"Lookup কেন O(1)?"* → প্রতিটা element তার inherited widget-গুলো type অনুযায়ী একটা map-এ cache করে রাখে। তাই সবচেয়ে কাছেরটা খুঁজে পাওয়া সরাসরি একটা lookup, কোনো tree walk নয়।

**সম্পর্কিত:** [Q6 — didChangeDependencies](#q6) · [Q8 — BuildContext](#q8) · [Q16 — MediaQuery এটাই ব্যবহার করে](#q16)

[↑ উপরে ফিরুন](#toc)

---

# C. Performance — const, repaint, thread

---

## <a id="q10"></a>10. একটা `const` constructor কীভাবে widget rebuild আটকায়? Tree-র স্তরে `const` মানে কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা `const` widget compile time-এ তৈরি হয় আর canonicalize হয় — app-এর প্রতিটা `const Text('Hello')` memory-তে ঠিক একই object। Reconciliation-এর সময় parent rebuild হলে Flutter দেখে নতুন child পুরোনোটার সাথে *identical* object। তাই ওই পুরো subtree rebuild করা সাথে সাথে বাদ দেয়। কোনো `build` call নেই, কোনো diffing নেই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — app চালু হওয়ার আগেই `const` object বানিয়ে ফেলে।**
Const constructor আর const call থাকলে Dart widget-টা compile time-এ বানায়। তারপর সব জায়গায় একটাই shared instance আবার ব্যবহার করে (canonicalization)।

**ধাপ ২ — Reconciliation-এর short-circuit।**
Parent rebuild হলে Flutter পুরোনো child আর নতুন child তুলনা করে। দুটো যদি **identical** object হয় (যেটা `const` নিশ্চিত করে), Flutter ঠিক সেখানেই থেমে যায় — "কিছু বদলায়নি" — আর subtree বাদ দেয়।

```dart
class _ParentState extends State<Parent> {
  int _counter = 0;

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      const Text('I never rebuild'),     // identical object → skip হয়
      const ExpensiveWidget(),           // এর build() আর চলবে না
      Text('Counter: $_counter'),        // const নয় → প্রতিবার rebuild হয়
      ElevatedButton(
        onPressed: () => setState(() => _counter++),
        child: const Text('Increment'),  // এই child-টাও const
      ),
    ]);
  }
}
```

**ধাপ ৩ — একই data মানে `const` নয়।**
`const` ছাড়া দুটো `Text('Hello')` আসলে দুটো *আলাদা* object। তাই Flutter তখনও `build` call করে আর property তুলনা করে। `const` থাকলে `identical()` check সাথে সাথেই true হয়, তাই এটা দ্রুত বেরিয়ে আসে।

**ধাপ ৪ — একটা widget const হওয়ার ৩টি শর্ত।**
1. এর একটা `const` constructor আছে।
2. এর সব field `final`।
3. আপনি যে argument দেন সবগুলো compile-time constant।

**ধাপ ৫ — সীমা: const শুধু *parent-এর কারণে হওয়া* rebuild আটকায়।**
একটা const widget যদি কোনো `InheritedWidget`-এর উপর নির্ভর করে (যেমন Theme) আর সেটা বদলায়, তবু এটা rebuild হবে — কারণ ওটা dependency change, parent rebuild নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে "সব জায়গায় const ব্যবহার করুন" কথাটা আপনি মুখস্থ করেছেন নাকি বুঝেছেন। আসল কারণ হলো identical object আবার ব্যবহার করা, সাথে reconciliation-এর short-circuit।

**সাধারণ ভুল:** ভাবা যে `const` *সব* rebuild আটকায়। এটা শুধু parent আবার তৈরি হওয়ার কারণে হওয়া rebuild আটকায়। আরেকটা ভুল — শুধু `final` যথেষ্ট ভাবা। `final` পুনরায় assign করা আটকায়, কিন্তু `const` পুরো object-টাকে compile-time constant বানায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা মান যদি network থেকে আসে তখন কী?"* → তখন সেটা `const` হতে পারবে না। যে অংশ বদলায় সেটা আলাদা রাখুন, বাকিটা `const` করুন।
- *"Widget যদি একটা InheritedWidget দেখে, const কি সাহায্য করে?"* → ওই dependency-র বিরুদ্ধে নয় — inherited data বদলালে এটা তখনও rebuild হবে।

**সম্পর্কিত:** [Q4 — reconciliation](#q4) · [Q2 — immutability](#q2) · [Q12 — কম rebuild = মসৃণ frame](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. RepaintBoundary কী? এটা কীভাবে repaint কমায়, আর কখন এটা যোগ করা উচিত?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"RepaintBoundary তার subtree-কে নিজস্ব paint layer-এ বসায়। এটা ছাড়া কিছু repaint দরকার হলে Flutter সবচেয়ে কাছের boundary পর্যন্ত সবকিছু repaint করে, যেটা বড় একটা region হতে পারে। এটা থাকলে ঘন ঘন বদলানো অংশ একা repaint হয়, আর তার পাশের ব্যয়বহুল অংশগুলোকে repaint হতে বাধ্য করে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: আলাদা কাচের পাত।**
ভাবুন, একটার উপর একটা রাখা কাচের পাতে আঁকছেন। সব যদি এক পাতে থাকে, একটা জিনিস বদলানো মানে পুরো পাত আবার আঁকা। RepaintBoundary বদলানো জিনিসটাকে **নিজের** একটা পাত দেয়, তাই শুধু ওটাই আবার আঁকতে হয়।

**ধাপ ২ — Default-এ repaint region কীভাবে কাজ করে।**
একটা render object-এর repaint দরকার হলে Flutter সবচেয়ে কাছের repaint boundary পর্যন্ত উপরে যায় আর তার ভেতরের সবকিছু repaint করে। ওই boundary অনেক উপরে হলে অকারণে একটা বড় region repaint হয়।

**ধাপ ৩ — একটা boundary বসালে পরিবর্তন আলাদা হয়ে যায়।**
আপনি Flutter-কে বলছেন: "ভেতরের অংশ নিজে নিজে বদলায়; ভেতরটা বদলালে বাইরেটা repaint কোরো না।"

```dart
// WITHOUT — spinner পুরো column-কে repaint করতে বাধ্য করে
Column(children: [
  ExpensiveHeader(),
  CircularProgressIndicator(),   // ~60fps-এ animate করে
  ExpensiveFooter(),
])

// WITH — শুধু spinner-এর layer repaint হয়
Column(children: [
  const ExpensiveHeader(),
  RepaintBoundary(child: CircularProgressIndicator()),
  const ExpensiveFooter(),
])
```

**ধাপ ৪ — কখন যোগ করবেন (আর কখন নয়)।**
এমন কিছুর চারপাশে যোগ করুন যেটা ঘন ঘন repaint হয় কিন্তু তার প্রতিবেশীরা হয় না: একটা animation, একটা video, custom canvas drawing। সব জায়গায় **যোগ করবেন না** — প্রতিটা boundary একটা নতুন compositing layer বানায় যেটা GPU memory খরচ করে। তাই বেশি ব্যবহার করলে অবস্থা আরও খারাপ হতে পারে।

**ধাপ ৫ — Flutter নিজেই কিছু যোগ করে রাখে।**
`ListView`-এর item আর `Navigator`-এর route আগে থেকেই RepaintBoundary পায়। তাই ওখানে নিজে থেকে যোগ করার দরকার নেই।

**Interviewer কেন জিজ্ঞেস করে:** এটা উন্নত rendering জ্ঞান যাচাই করে — repaint *কখন* হয় আর কীভাবে সেগুলো আলাদা করা যায় সেটা জানলেই কম ক্ষমতার device-এ 60fps দেওয়া যায়।

**সাধারণ ভুল:** সবকিছু RepaintBoundary দিয়ে মুড়ে দেওয়া। প্রতিটার GPU memory খরচ আছে; বেশি হলে texture memory শেষ হয়ে যেতে পারে আর performance খারাপ হয়। আরেকটা ভুল — ভাবা যে এটা layout-এ সাহায্য করে; করে না। Layout এর ভেতর দিয়ে স্বাভাবিকভাবেই চলে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা কাজে লাগছে কি না কীভাবে দেখবেন?"* → DevTools → "Highlight Repaints"। যে region-গুলো একসাথে জ্বলে ওঠে সেগুলো একটা boundary দিয়ে ভাগ করা উচিত।
- *"এটা কি layout-এর খরচে সাহায্য করে?"* → না, শুধু paint-এ। Layout স্বাভাবিকভাবেই ছড়িয়ে যায়।

**সম্পর্কিত:** [Q12 — raster thread-এর খরচ](#q12) · [Q17 — paint phase](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. Flutter কীভাবে 60/120fps ধরে? UI thread আর raster thread কী?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flutter-এর frame budget 60fps-এ প্রায় 16ms, আর 120fps-এ 8ms। এটা একাধিক thread ব্যবহার করে: UI thread আমার Dart code চালায় — build, layout, আর layer tree বানানো — আর raster thread ওই layer-গুলোকে GPU-তে pixel বানায়। এগুলো সমান্তরালে চলে বলে raster thread frame N আঁকতে পারে যখন UI thread frame N+1 বানাচ্ছে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Frame budget।**
60fps-এ প্রতিটা frame ~16ms-এ শেষ হতে হবে; 120fps-এ ~8ms-এ। Budget মিস করলে একটা frame drop হয় — সেটাই jank।

**ধাপ ২ — UI thread (আপনার Dart code)।**
এটা `build()`, layout, hit-testing, gesture, আর animation tick চালায়। এর ফলাফল একটা **LayerTree** — কিছু paint instruction, *এখনও* pixel নয়।

**ধাপ ৩ — Raster thread (GPU-র কাজ)।**
এটা LayerTree নিয়ে GPU-তে আসল pixel-এ rasterize করে। এটা একটা *আলাদা* thread-এ চলে, তাই ধীর rasterization-ও UI thread আটকায় না।

**ধাপ ৪ — আরও দুটো thread।**
- **Platform thread** — platform message, plugin call, system event।
- **I/O thread** — ভারী I/O, যেমন image decoding, যাতে UI thread আটকে না যায়।

**ধাপ ৫ — যে diagnosis সমাধান বদলে দেয়।**
এটাই senior-level পয়েন্ট। DevTools খুলুন আর দুটো bar দেখুন:
- **UI bar লাল (>16ms)** → সমস্যা আপনার *Dart*-এ: ভারী `build()`, বড় synchronous কাজ। সমাধান — `const`, কম widget, বা CPU-র কাজ একটা isolate-এ সরানো।
- **Raster bar লাল** → সমস্যা *GPU*-তে: অনেক বেশি overdraw, ব্যয়বহুল shadow/clip। সমাধান — `RepaintBoundary`, সহজ effect।

```dart
// Jank: UI thread-এ ভারী কাজ frame আটকে দেয়
void onTap() {
  setState(() {
    _data = expensiveComputation();   // 50ms → ~3টি frame miss করে
  });
}

// সমাধান: CPU-ভারী কাজ isolate দিয়ে UI thread-এর বাইরে নিন
void onTap() async {
  final result = await compute(expensiveComputation, input);
  if (!mounted) return;
  setState(() => _data = result);
}
```

**Interviewer কেন জিজ্ঞেস করে:** এটাই সেরা performance প্রশ্ন। এটা যাচাই করে আপনি jank *কোথায়* সেটা বলতে পারেন কি না — UI thread (আপনার code) নাকি raster thread (GPU) — কারণ সমাধান পুরোপুরি আলাদা।

**সাধারণ ভুল:** বলা যে "Flutter single-threaded"। এতে অন্তত চারটা thread আছে। আরেকটা ভুল — সব jank-এর দোষ GPU-কে দেওয়া; UI bar লাল হলে সমস্যা আপনার Dart code-এ। আর মনে রাখুন, `async`/`await` কোনো নতুন thread **বানায় না**; শুধু isolate সত্যিকারের সমান্তরাল CPU কাজ দেয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Shader jank কেন raster thread আটকে দেয়?"* → পুরোনো Skia runtime-এ shader compile করত, ফলে প্রথমবার ব্যবহারে raster thread আটকে যেত (দেখুন [Q18](#q18))।
- *"আমার 60fps app 120Hz phone-এ কেন jank করে?"* → Budget 16ms থেকে 8ms-এ নেমে আসে, তাই যেটুকু কাজ আগে কোনোমতে হতো সেটা এখন frame miss করে।

**সম্পর্কিত:** [Q11 — RepaintBoundary](#q11) · [Q17 — rendering pipeline](#q17) · [Q18 — Impeller](#q18)

[↑ উপরে ফিরুন](#toc)

---

# D. Layout ও constraints

---

## <a id="q13"></a>13. Flutter-এর layout নিয়মটা ব্যাখ্যা করুন: "constraints নিচে যায়, size উপরে আসে, parent position ঠিক করে।" একটা উদাহরণ দিয়ে দেখান।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Layout হলো একটা মাত্র pass, তিনটা নিয়ম নিয়ে। Parent প্রতিটা child-কে constraints (min/max width আর height) নিচে পাঠায়। প্রতিটা child ওই constraints-এর ভেতরে নিজের size বেছে নেয় আর উপরে জানিয়ে দেয়। তারপর parent child-কে বসায় — child কখনোই নিজের position জানে না। একবার নিচে আর একবার উপরে হাঁটে বলে layout O(n)।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: দর্জি আর খদ্দের।**
Parent হলো দর্জি, যে বলে "তোমার শার্ট S থেকে L-এর মধ্যে হতে হবে" (constraints নিচে)। Child খদ্দের ওই range-এর ভেতর একটা size বেছে বলে "আমি M নেব" (size উপরে)। তারপর দর্জি ঠিক করে ছবিতে খদ্দের কোথায় দাঁড়াবে (parent position ঠিক করে)।

**ধাপ ২ — নিয়ম ১: constraints নিচে যায়।**
Parent প্রতিটা child-কে একটা `BoxConstraints` দেয়: `minWidth, maxWidth, minHeight, maxHeight`। Child-কে *অবশ্যই* এর ভেতরেই থাকতে হবে।

**ধাপ ৩ — নিয়ম ২: size উপরে আসে।**
Child constraints-এর ভেতরে নিজের size বেছে নেয় আর সেটা উপরে জানিয়ে দেয়। অনুমোদিত range-এর বাইরে কোনো size সে নিতে পারে না।

**ধাপ ৪ — নিয়ম ৩: parent position ঠিক করে।**
Child জানে না তাকে কোথায় বসানো হবে; শুধু parent-ই জানে (parent data-তে একটা offset হিসেবে রাখা থাকে)। Child-এর `size` তার position সম্পর্কে কিছুই বলে না।

```dart
// Screen 400 x 800
SizedBox(            // পায় 0≤w≤400, 0≤h≤800
  width: 300,
  height: 200,       // নিচে পাঠায় tight 0≤w≤300, 0≤h≤200
  child: Center(     // পায় 0≤w≤300, 0≤h≤200
                     // নিচে পাঠায় LOOSE 0≤w≤300, 0≤h≤200
    child: Container( // ওই loose constraints পায়
      width: 100,
      height: 50,     // বেছে নেয় 100x50, size উপরে জানায়
      color: Colors.blue,
    ),
    // Center 300x200, child 100x50
    // → Center child-কে offset (100, 75)-এ বসায়, যাতে মাঝখানে থাকে
  ),
)
```

**ধাপ ৫ — কেন এটা একটাই pass (O(n))।**
Constraints একবার নিচে যায় আর size একবার উপরে আসে, একটাই depth-first হাঁটায়। এটা CSS-এর মতো multi-pass **নয়**। Flutter layout দ্রুত হওয়ার এটা একটা বড় কারণ।

**Interviewer কেন জিজ্ঞেস করে:** প্রতিটা layout bug-এর ভিত্তি এটাই। "RenderFlex overflowed," "unbounded constraints," আর size নিয়ে অবাক হওয়া — সবই এই flow না বোঝা থেকে আসে। তাঁরা প্রমাণ চান আপনি আন্দাজে চেষ্টা না করে layout debug করতে পারেন।

**সাধারণ ভুল:** বলা যে "child তার position জানে।" সে জানে না। আরেকটা ভুল — layout-কে CSS-এর মতো multi-pass ভাবা। আর ধরে নেওয়া যে একটা widget-এর একটা fixed size "আছে" — size না দেওয়া `Container()` ভেতরে আসা constraints অনুযায়ী সম্পূর্ণ আলাদা আচরণ করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Child-এর position কোথায় রাখা থাকে?"* → parent data-তে (একটা offset), parent সেট করে — child-এর নিজের ভেতরে নয়।
- *"Layout কেন O(n)?"* → প্রতিটা render object নিচে যাওয়ার সময় একবার (constraints) আর উপরে আসার সময় একবার (size) visit হয়।

**সম্পর্কিত:** [Q14 — BoxConstraints](#q14) · [Q15 — overflow](#q15) · [Q16 — LayoutBuilder constraints দেয়](#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. BoxConstraints কী? tight বনাম loose ব্যাখ্যা করুন, আর "unbounded" মানে কী বলুন।

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"BoxConstraints হলো চারটা সংখ্যা: min আর max width, min আর max height। Tight মানে min আর max সমান, তাই child-এর কোনো পছন্দ নেই। Loose মানে min হলো 0, তাই child max পর্যন্ত যেকোনো size হতে পারে। Unbounded মানে কোনো max হলো infinity, যেটা scrollable-এর ভেতরে হয় — আর যে widget পুরো জায়গা ভরতে চায়, সে তখন অসীম বড় হওয়ার চেষ্টা করে আর error দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — চারটা সংখ্যা।**
প্রতিটা `RenderBox` তার parent থেকে `minWidth, maxWidth, minHeight, maxHeight` পায়। এর ভেতরেই তাকে একটা size বেছে নিতে হয়।

**ধাপ ২ — Tight constraints (কোনো পছন্দ নেই)।**
`minWidth == maxWidth` (এবং/অথবা height জোড়াটাও সমান)। Child-কে ঠিক ওই size-ই হতে হবে। Screen আপনার root-কে tight constraints পাঠায়, তাই সেটা পুরো screen ভরতে বাধ্য হয়।

```dart
BoxConstraints.tight(const Size(200, 200));
// দুই axis-এই min=max=200 → child অবশ্যই 200x200 হবে
```

**ধাপ ৩ — Loose constraints (max পর্যন্ত স্বাধীনতা)।**
`minWidth = 0`, তাই child 0 থেকে max পর্যন্ত যেকোনো জায়গায় থাকতে পারে। `Center` constraints loose করে দেয় — "যত ছোট চাও হও, আমার size পর্যন্ত।"

```dart
BoxConstraints.loose(const Size(200, 200));
// min=0, max=200 → child 0..200 হতে পারে
```

**ধাপ ৪ — Unbounded constraints (max হলো infinity)।**
`ListView`-এর মতো scrollable scroll direction-এ `maxHeight = double.infinity` পাঠায়, কারণ children যেকোনো height-এর হতে পারে। সমস্যা: যে widget যত বড় সম্ভব হতে চায় (খালি `Container()`, বা `Expanded`), সে অসীম বড় হওয়ার চেষ্টা করে আর error দেয়।

```dart
// CRASHES — ListView-এর ভেতরে Column-এর height infinite
ListView(children: [
  Column(children: [
    Expanded(child: Text('Boom')),
    // বাকি জায়গা = infinity → "unbounded height" error
  ]),
])

// FIX — ভেতরের Column-কে একটা bounded height দিন
ListView(children: [
  SizedBox(
    height: 300,
    child: Column(children: [
      Expanded(child: Text('Works')),   // এখন 300 - siblings
    ]),
  ),
])
```

**ধাপ ৫ — Error পড়া।**
"BoxConstraints forces an infinite ... " বা "RenderFlex children have non-zero flex but incoming height constraints are unbounded" — দুটোরই মানে: একটা flex/fill widget infinity-র সাথে দেখা করেছে। ওটাকে একটা bounded size দিন।

**Interviewer কেন জিজ্ঞেস করে:** প্রায় প্রতিটা "RenderBox was not laid out" বা "Infinity" trace শেষে একটা constraints mismatch-এ গিয়ে ঠেকে। তাঁরা দেখতে চান আপনি message পড়েই রোগ ধরতে পারেন কি না, নাকি এলোমেলোভাবে সব `Expanded`-এ মুড়ে দেন।

**সাধারণ ভুল:** `double.infinity`-কেই bug ভাবা। এটা ইচ্ছাকৃত — scrollable এটা ব্যবহার করে। Bug হলো সেই child, যে unbounded constraints সামলাতে জানে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Size ছাড়া `Container()` কখনো ভরে, কখনো ভরে না কেন?"* → এটা *bounded* constraints ভরার জন্য ছড়িয়ে যায়, কিন্তু *unbounded* constraints-এ error দেয়।
- *"Scrollable-এর ভেতরে height কীভাবে দেব?"* → `SizedBox`-এ মুড়ে দিন, অথবা ভেতরের list-এ `shrinkWrap: true` ব্যবহার করুন।

**সম্পর্কিত:** [Q13 — constraints flow](#q13) · [Q15 — overflow fixes](#q15) · [Q16 — LayoutBuilder](#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. "RenderFlex overflowed" কেন হয়, আর আপনি এটা কীভাবে ঠিক করেন?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"RenderFlex হলো Row আর Column-এর পেছনের render object। Overflow মানে main axis বরাবর children-এর মোট size পাওয়া জায়গার চেয়ে বড়। সমাধান নির্ভর করে উদ্দেশ্যের উপর: Flexible বা Expanded দিয়ে children-কে জায়গা ভাগ করতে দিন, লম্বা text-এ ellipsis দিন, অথবা content সত্যিই screen-এর চেয়ে বড় হলে একটা scroll view-তে মুড়ে দিন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Error-টার মানে কী।**
400px screen-এ 200px-এর তিনটা child নিয়ে একটা `Row`-এর দরকার 600px, কিন্তু আছে 400px। বাড়তি 200px overflow করে, আর আপনি হলুদ-কালো ডোরা দেখতে পান।

**ধাপ ২ — মূল কারণ ১: fixed children parent-এর চেয়ে বড়।**
`Expanded` দিয়ে ঠিক করুন (children জায়গা ভাগ করে নেয়, প্রত্যেকে নিজের ভাগ ভরতে বাধ্য) অথবা `Flexible` দিয়ে (children জায়গা ভাগ করে নেয়, কিন্তু ছোটও হতে পারে)।

```dart
// OVERFLOW — 400px row-এ 200px-এর তিনটা fixed item
Row(children: [
  Container(width: 200, height: 50, color: Colors.red),
  Container(width: 200, height: 50, color: Colors.green),
  Container(width: 200, height: 50, color: Colors.blue),
])

// FIX — Expanded জায়গা ভাগ করে নেয়
Row(children: [
  Expanded(child: Container(height: 50, color: Colors.red)),
  Expanded(flex: 2, child: Container(height: 50, color: Colors.green)),
  Expanded(child: Container(height: 50, color: Colors.blue)),
])
```

**ধাপ ৩ — মূল কারণ ২: লম্বা text।**
`Text`-কে `Expanded`-এ মুড়ে দিন আর `overflow: TextOverflow.ellipsis` যোগ করুন।

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

**ধাপ ৪ — মূল কারণ ৩: content-এর scroll করা উচিত।**
Content যদি সত্যিই screen-এর চেয়ে বড় হয়, তাহলে Row/Column-কে একটা `SingleChildScrollView`-এ মুড়ে দিন।

```dart
SingleChildScrollView(
  scrollDirection: Axis.horizontal,
  child: Row(children: tiles),
)
```

**ধাপ ৫ — মূল কারণ ৪: unbounded cascade।**
`ListView`-এর ভেতরে একটা `Column` (দুটোই vertical) Column-কে infinite height দেয়। ভেতরের Column-কে `SizedBox`-এ মুড়ে দিন, অথবা ভেতরের list-এ `shrinkWrap: true` সেট করুন (দেখুন [Q14](#q14))।

**Interviewer কেন জিজ্ঞেস করে:** এটাই Flutter-এর সবচেয়ে সাধারণ layout error। তাঁরা দেখতে চান আপনি উদ্দেশ্য বুঝে *সঠিক* সমাধানটা বেছে নেন, এলোমেলোভাবে wrapper চেষ্টা করেন না।

**সাধারণ ভুল:** Row/Column/Flex-এর বাইরে `Expanded` ব্যবহার করা — এটা শুধু flex container-এর ভেতরেই কাজ করে। সব কিছুকে ঢালাওভাবে `SingleChildScrollView`-এ মুড়ে দেওয়া। `Flexible` (`FlexFit.loose`, ছোট হতে পারে) আর `Expanded` (`FlexFit.tight`, নিজের ভাগ ভরতেই হবে) গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flexible বনাম Expanded?"* → `Expanded` হলো `Flexible(fit: FlexFit.tight)` — তাকে নিজের ভাগ ভরতেই হবে। `Flexible` child-কে ছোট হতে দেয়।
- *"ListView-এর ভেতরে `Expanded` কেন crash করে?"* → main-axis constraint unbounded (infinity), তাই "বাকি জায়গা ভরো" কথাটার কোনো মানে থাকে না।

**সম্পর্কিত:** [Q13 — constraints](#q13) · [Q14 — unbounded](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. MediaQuery আর LayoutBuilder-এর মধ্যে পার্থক্য কী? কোনটা কখন ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"MediaQuery পুরো screen-এর global তথ্য দেয় — full screen size, padding, text scale, orientation। LayoutBuilder দেয় আসল constraints, যেটা আমার widget tree-এর ওই নির্দিষ্ট জায়গায় পেয়েছে। তাই আমার widget যদি একটা 300px box-এর ভেতরে বসে, MediaQuery তবুও full screen width বলবে। কিন্তু LayoutBuilder বলবে 300। Reusable আর responsive widget-এর জন্য LayoutBuilder সাধারণত বেশি সঠিক।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — MediaQuery = পুরো window-এর তথ্য।**
এটা screen size, device pixel ratio, text scale factor, safe-area padding (notch, status bar), orientation আর brightness জানায়। এটা আসে সবচেয়ে কাছের `MediaQuery` ancestor থেকে (সাধারণত `MaterialApp` সেট করে)। আর tree-এর সব জায়গায় এটা **একই**।

```dart
final screenWidth = MediaQuery.of(context).size.width;
if (screenWidth > 600) return TabletLayout();
return PhoneLayout();
```

**ধাপ ২ — LayoutBuilder = আপনি আসলে যত জায়গা পেয়েছেন।**
Parent *এই* জায়গায় যে `BoxConstraints` পাঠিয়েছে, এটা সেটাই দেয়। আপনার widget সত্যিই কতটুকু জায়গা পেয়েছে, এটা তাই — পুরো screen নয়।

```dart
SizedBox(
  width: 300,
  child: LayoutBuilder(
    builder: (context, constraints) {
      // constraints.maxWidth == 300, screen width নয়
      return constraints.maxWidth > 200 ? WideVersion() : NarrowVersion();
    },
  ),
)
```

**ধাপ ৩ — মূল পার্থক্যটা পাশাপাশি।**
400px screen-এ একটা `SizedBox(width: 300)`-এর ভেতরে:
- `MediaQuery.of(context).size.width` → **400** (পুরো screen)।
- `LayoutBuilder` → `maxWidth: 300` (আপনার আসল জায়গা)।

**ধাপ ৪ — একটা বাস্তব responsive উদাহরণ।**
একটা grid যেটা পাওয়া জায়গার সাথে মানিয়ে নেয়। ফলে split-screen-এ বা কোনো panel-এর ভেতরেও এটা কাজ করে:

```dart
LayoutBuilder(
  builder: (context, constraints) {
    final columns = (constraints.maxWidth / 150).floor().clamp(1, 6);
    return GridView.count(crossAxisCount: columns, children: cards);
  },
)
```

**ধাপ ৫ — MediaQuery-র একটা rebuild ফাঁদ।**
`MediaQuery.of(context)` *সব* media property-র উপর নির্ভর করে। তাই এদের যেকোনো একটা বদলালেই আপনার widget rebuild হয় — keyboard আসাও এর মধ্যে পড়ে। শুধু size-এর উপর নির্ভর করতে চাইলে `MediaQuery.sizeOf(context)` ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা বাস্তব responsive-design জ্ঞান যাচাই করে। অনেক app split-screen-এ বা ছোট container-এর ভেতরে ভেঙে যায়। কারণ developer সেখানে MediaQuery ব্যবহার করেছেন, যেখানে LayoutBuilder সঠিক ছিল।

**সাধারণ ভুল:** nested আর reusable widget-এর ভেতরে layout-এর জন্য MediaQuery ব্যবহার করা। একটা widget কখনো constrained parent-এর ভেতরে বসতে পারে (সাধারণত বসেই), তখন LayoutBuilder বেশি সঠিক। আরেকটা ভুল — `MediaQuery.of` যে keyboard show/hide-এ rebuild ঘটায়, সেটা না জানা। `sizeOf` বেছে নিন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"keyboard খুললে `MediaQuery.of` কেন rebuild করে?"* → এটা পুরো MediaQueryData-র উপর নির্ভর করে, view insets সহ। এটা এড়াতে `MediaQuery.sizeOf` ব্যবহার করুন।
- *"Tablet আর phone-এর জন্য কোনটা?"* → পুরো screen-এর breakpoint-এর জন্য MediaQuery; স্থানীয় জায়গার সাথে মানিয়ে নিতে LayoutBuilder।

**সম্পর্কিত:** [Q9 — MediaQuery একটা InheritedWidget](#q9) · [Q13 — LayoutBuilder constraints দেখায়](#q13)

[↑ উপরে ফিরুন](#toc)

---

# E. Rendering pipeline ও graphics

---

## <a id="q17"></a>17. Flutter-এর rendering pipeline বর্ণনা করুন। একটা tap থেকে screen-এর pixel পর্যন্ত একটা frame কীভাবে যায়?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"প্রতিটা frame শুরু হয় একটা vsync signal দিয়ে, তারপর কয়েকটা phase চলে: একটা state change element-কে dirty করে, তারপর build নতুন widget বানায়, তারপর layout render object-এর size আর position ঠিক করে, তারপর paint draw command গুলো layer-এ record করে, তারপর compositing layer গুলো এক করে, তারপর raster thread সেগুলোকে pixel বানায়, আর শেষে GPU frame-টা দেখায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Trigger: একটা state change dirty করে দেয়।**
একটা tap, scroll বা animation tick `setState` (বা এরকম কিছু) call করে। এটা element-কে dirty চিহ্নিত করে আর engine-কে একটা frame schedule করতে বলে।

**ধাপ ২ — Vsync: frame শুরু হয়।**
Platform একটা vsync callback পাঠায় (60fps-এ প্রতি ~16ms পরপর)। Flutter frame-এর কাজ শুরু করে।

**ধাপ ৩ — Build phase।**
Flutter dirty element গুলোতে `build()` call করে rebuild করে। তারপর নতুন widget গুলোকে পুরোনোগুলোর সাথে মিলিয়ে দেখে (দেখুন [Q4](#q4))। দরকার হলে render-object-এর property আপডেট করে।

**ধাপ ৪ — Layout phase।**
Root থেকে শুরু হয়, constraints নিচে নামে আর size উপরে ওঠে — একটাই depth-first pass-এ। Parent তার child-দের position ঠিক করে (দেখুন [Q13](#q13))।

**ধাপ ৫ — Paint phase।**
প্রতিটা render object নিজেকে `Layer` object-এ paint করে *record করা draw command* হিসেবে — এখনো pixel নয়। `RepaintBoundary` node আলাদা layer বানায় (দেখুন [Q11](#q11))।

**ধাপ ৬ — Composite, rasterize, display।**
Layer tree এক করা হয় আর engine-কে দেওয়া হয়। **Raster thread** সেটাকে GPU command আর আসল pixel-এ পরিণত করে। তারপর GPU frame-টা দেখায়।

```dart
// একটা tap-এর পথ:
ElevatedButton(
  onPressed: () => setState(() => _count++), // ১. dirty চিহ্নিত করে
  child: Text('$_count'),
)
// ২. পরের vsync আসে
// ৩. BUILD: build() চলে, Text('0') vs Text('1') → RenderParagraph আপডেট
// ৪. LAYOUT: RenderParagraph text আবার মাপে
// ৫. PAINT: নতুন draw command তার Layer-এ record করে
// ৬. COMPOSITE → RASTERIZE (raster thread) → DISPLAY
// user '1' দেখে
```

**Interviewer কেন জিজ্ঞেস করে:** janky frame debug করতে pipeline বোঝা জরুরি। Layout আর paint আলাদা জানলে আপনি বুঝবেন `RepaintBoundary` paint-এ সাহায্য করে, layout-এ নয়। Rasterization আলাদা thread-এ চলে জানলে বুঝবেন shader compilation কেন jank ঘটায়।

**সাধারণ ভুল:** বলা যে "Flutter প্রতি frame-এ পুরো screen আবার আঁকে।" আসলে এটা dirty region আর repaint boundary track করে। আরেকটা ভুল — build আর paint গুলিয়ে ফেলা। `build()` widget বানায়, pixel নয়। আর rasterization যে আলাদা thread-এ চলে, সেটা ভুলে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Build কোথায় শেষ আর paint কোথায় শুরু?"* → Build widget/element বানায়; layout তাদের size ঠিক করে; paint draw command record করে; raster pixel বানায়।
- *"RepaintBoundary কেন layout-এ সাহায্য করে না?"* → এটা শুধু paint layer আলাদা করে; layout constraints এর ভেতর দিয়ে আগের মতোই যায়।

**সম্পর্কিত:** [Q12 — UI vs raster thread](#q12) · [Q13 — layout phase](#q13) · [Q18 — rasterization ও shader](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. Impeller কী, আর এটা Skia থেকে কীভাবে আলাদা? Flutter কেন এতে সরে এল?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Skia হলো পুরোনো 2D engine, যেটা Flutter ব্যবহার করত; নতুন কোনো drawing operation প্রথমবার পেলে এটা তখনই GPU shader compile করত, আর এতে 'shader jank' হতো — কোনো animation প্রথমবার দেখার সময় একটা আটকে যাওয়া। Impeller হলো Flutter-এর নতুন engine, যেটা সব shader আগেভাগে build time-এ compile করে ফেলে, তাই runtime-এ কোনো shader compilation নেই আর প্রথম frame-এ কোনো jank নেই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Skia আর shader-jank সমস্যা।**
Skia একটা general-purpose 2D graphics library। এটা shader compile করত **runtime-এ, দেরিতে** — কোনো একটা effect প্রথমবার এলে raster thread থেমে যেত (প্রায়ই 50–200ms) shader compile করতে। আপনি `--cache-sksl` দিয়ে shader আগে থেকে গরম করতে পারতেন, কিন্তু সেটা ভঙ্গুর আর হাতে করার কাজ ছিল।

**ধাপ ২ — Impeller-এর মূল ধারণা: shader আগেভাগে compile করা।**
Impeller বানানো হয়েছে শুধু Flutter-এর জন্য। এর সব shader **engine build time-এ precompile করা** থাকে। তাই runtime-এ shader compilation একদম শূন্য। GPU pipeline state আগে থেকেই জানা।

```dart
// Skia দিয়ে:
// একটা জটিল animation প্রথমবার আসে
//   → Skia তখনই shader compile করে → raster thread থেমে যায় → দৃশ্যমান আটকে যাওয়া
//   → পরের frame গুলো মসৃণ (shader cache হয়ে গেছে)

// Impeller দিয়ে:
// একই animation → shader আগেই build time-এ compile করা
//   → raster thread সাথে সাথে এগোয় → প্রথম frame থেকেই মসৃণ
```

**ধাপ ৩ — অন্য পার্থক্যগুলো।**
- Skia: শেয়ার করা, general-purpose codebase। Impeller: Flutter-এর pattern-এর জন্য বিশেষভাবে বানানো।
- Impeller iOS-এ **Metal** আর Android-এ **Vulkan** (OpenGL fallback) ব্যবহার করে।
- Impeller-এর আসল লাভ *পূর্বানুমানযোগ্যতা* — গড় FPS একই হলেও সবচেয়ে খারাপ frame গুলো অনেক ভালো হয়।

**ধাপ ৪ — আপনি app code বদলান না।**
Impeller engine level-এ চালু হয়। সাম্প্রতিক Flutter release অনুযায়ী এটা iOS-এ default (3.16 থেকে) আর Android-এ default (সাধারণভাবে 3.27 থেকে; শুরু হয়েছিল 3.22-তে)।

```bash
flutter run --enable-impeller     # জোর করে Impeller
flutter run --no-enable-impeller  # জোর করে Skia
```

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি Flutter-এর পরিবর্তনের খবর রাখেন আর widget-এর নিচের rendering stack বোঝেন। কম দামের Android-এ ship করা team-রা বিশেষভাবে এটা নিয়ে ভাবেন, কারণ shader jank ছিল তাঁদের user-দের সবচেয়ে বড় অভিযোগ।

**সাধারণ ভুল:** বলা যে Impeller সব ক্ষেত্রেই "দ্রুত"। এর সুবিধা হলো *ধারাবাহিকতা* (কোনো jank spike নেই), কাঁচা throughput নয়। কিছু Skia-optimized path আজও Impeller-এ একটু ধীর হতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Shader jank ঠিক কী?"* → নতুন কোনো drawing operation-এর জন্য Skia-কে প্রথমবার shader compile করতে হলে raster thread-এ যে আটকে যাওয়া হয়, সেটাই।
- *"বেশি গড় FPS-এর চেয়ে পূর্বানুমানযোগ্য frame time কেন ভালো?"* → User *সবচেয়ে খারাপ* frame গুলো (আটকে যাওয়া) খেয়াল করেন, গড় নয়।

**সম্পর্কিত:** [Q12 — raster thread](#q12) · [Q17 — rasterization](#q17)

[↑ উপরে ফিরুন](#toc)

---

# F. Tooling ও dev loop

---

## <a id="q19"></a>19. Hot Reload, Hot Restart আর Full Restart-এর মধ্যে পার্থক্য কী? কোনটা কী reset করে?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Hot Reload চলমান VM-এ নতুন code ঢুকিয়ে দেয় আর সব state রেখে দেয় — এটা শুধু `build` আবার চালায়, প্রায় এক সেকেন্ডে। Hot Restart Dart VM restart করে আর সব state মুছে দেয়, `main` আর `initState` আবার চালায়। Full Restart native code সহ সবকিছু আবার build করে আর app পুনরায় install করে — native code, plugin বা pubspec ছুঁলে এটা লাগে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Hot Reload (state রেখে দেয়)।**
এটা আপডেট করা Dart code চলমান VM-এ পাঠায়, restart **ছাড়াই**। সব `State` object, global, static আর navigation stack ঠিক থাকে। নতুন code দিয়ে `build()` আবার চলে, কিন্তু `main()` বা `initState()` আবার **চলে না**। প্রায় ১ সেকেন্ড।

**ধাপ ২ — Hot Restart (Dart state মুছে দেয়)।**
এটা Dart VM restart করে। Global, static আর `State` object আবার নতুন করে তৈরি হয়; `main()` আর `initState()` আবার চলে। কয়েক সেকেন্ড লাগে। এটা native Kotlin/Swift code আবার compile করে **না**।

**ধাপ ৩ — Full Restart / cold start (native-ও আবার build করে)।**
এটা app বন্ধ করে, native platform code সহ সবকিছু আবার compile করে, আর APK/IPA আবার install করে। Native code বদলালে, plugin যোগ করলে, `pubspec.yaml`-এর dependency বদলালে বা platform config বদলালে এটা লাগে। 30+ সেকেন্ড।

```dart
int globalCounter = 0;

class _MyState extends State<MyWidget> {
  int localCounter = 10;

  @override
  void initState() {
    super.initState();
    globalCounter++;            // শুধু Hot Restart-এ আবার চলে
  }

  @override
  Widget build(BuildContext context) =>
      Text('L:$localCounter G:$globalCounter',
          style: const TextStyle(fontSize: 24)); // 32 করে দিন...
}

// fontSize 32 করার পরে Hot Reload:
//   fontSize → 32, localCounter 10-ই থাকে, initState call হয় না
// Hot Restart:
//   localCounter → নতুন করে 10, globalCounter → 0 তারপর 1, initState call হয়
// Full Restart দরকার যখন:
//   firebase_core যোগ করা, AndroidManifest.xml বদলানো, নতুন method channel
```

**ধাপ ৪ — Hot Reload কখন কাজে আসে না।**
Hot Reload `main()`-এর বদল, global initializer, আগেই চলে যাওয়া `initState` logic, enum-এর সংজ্ঞা, বা কিছু generic type-এর বদল apply করতে পারে না। যখন এটা "কাজ করছে না" মনে হয়, তখন Hot Restart ধরুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা বাস্তব productivity প্রশ্ন। কোন বদলের জন্য কোন restart লাগে জানলে debugging অনেক দ্রুত হয়।

**সাধারণ ভুল:** আশা করা যে Hot Reload `initState`-এর বদল, enum-এর বদল বা native code-এর বদল ধরবে। আরেকটা ভুল — Hot Reload যে `main()` বা global initializer-এর বদল সামলাতে পারে না, সেটা না জানা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Hot Reload কেন initState আবার চালায় না?"* → এটা আগের `State` object গুলো রেখে দেয়, তাই তাদের `initState` আগেই চলে গেছে; শুধু `build` আবার চলে।
- *"Full Restart কখন বাধ্যতামূলক?"* → যেকোনো native বদলে: নতুন plugin, বদলানো manifest/Info.plist, নতুন platform channel।

**সম্পর্কিত:** [Q6 — restart-এ initState চলে](#q6) · [Q23 — JIT hot reload সম্ভব করে](#q23)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q20"></a>20. pub.dev কী? pubspec.yaml কীভাবে dependency manage করে, আর `^`, `>=`, আর `==` কীভাবে কাজ করে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q20)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"pub.dev হলো Dart আর Flutter-এর official package registry, JavaScript-এর npm-এর মতো। pubspec.yaml আমার project-এর dependency আর version-এর নিয়ম ঘোষণা করে। `flutter pub get` version resolve করে আর exact version pubspec.lock-এ lock করে রাখে। `dependencies` app-এর সাথে যায়। `dev_dependencies` শুধু development-এর জন্য। Caret `^1.5.0` মানে `>=1.5.0 <2.0.0`, আর এটাই recommended default।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — pub.dev আর pubspec.yaml।**
pub.dev open-source package host করে, সাথে popularity, health আর maintenance-এর একটা score দেখায়। Project root-এ থাকা `pubspec.yaml` name, version, SDK constraint আর dependency ঘোষণা করে। `flutter pub get` compatible version resolve করে। তারপর resolve হওয়া exact version `pubspec.lock`-এ লিখে রাখে, যাতে build reproducible হয়।

**ধাপ ২ — `dependencies` বনাম `dev_dependencies`।**
- `dependencies` — app **চালাতে** লাগে; এগুলো binary-তে ship হয় (যেমন `http`, `provider`, `flutter_bloc`)।
- `dev_dependencies` — শুধু **development/testing**-এ লাগে; এগুলো release build-এ **থাকে না** (যেমন `flutter_test`, `flutter_lints`, `mockito`, `build_runner`)।

কোনো test tool `dependencies`-এ রাখলে release binary অকারণে ভারী হয়।

**ধাপ ৩ — Semantic versioning: MAJOR.MINOR.PATCH।**
- MAJOR (`2.x.x`) — breaking change।
- MINOR (`x.4.x`) — নতুন feature, backward-compatible।
- PATCH (`x.x.1`) — bug fix, backward-compatible।

**ধাপ ৪ — Constraint-এর syntax।**
- `^1.5.0` (caret) → `>=1.5.0 <2.0.0`। Minor/patch upgrade চলবে, পরের major নয়। এটাই recommended default।
- `>=1.5.0 <3.0.0` → স্পষ্ট range, যখন আপনি জানেন আপনার code একাধিক major-এ কাজ করে।
- `==1.5.0` → exact pin। এটা update আটকায় আর conflict বাড়ায়; খুব কমই সঠিক।
- `>=1.5.0` → উপরের দিকে কোনো সীমা নেই, ঝুঁকিপূর্ণ (ভবিষ্যতের কোনো major আপনার code ভেঙে দিতে পারে)।
- `any` → যেকোনো কিছু নেয়; শুধু ফেলে দেওয়ার মতো prototype-এর জন্য।

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
  flutter_lints: ^5.0.0    # শুধু dev-এর জন্য
  build_runner: ^2.4.0     # শুধু dev-এর জন্য
```

**ধাপ ৫ — Conflict সমাধান।**
দুটো package যদি তৃতীয় একটা package-এর অসামঞ্জস্যপূর্ণ version চায়, তাহলে solver "incompatible version constraints" বলে fail করে। Constraint ঢিলা করে বা upgrade করে ঠিক করুন। শেষ উপায় হিসেবে `dependency_overrides` পুরো project-এ একটা version জোর করে বসায়। এটা শুধু সাময়িকভাবে ব্যবহার করুন, কারণ API না মিললে runtime-এ crash হতে পারে।

```bash
flutter pub deps        # dependency-র tree
flutter pub outdated    # যেসব upgrade পাওয়া যাচ্ছে
flutter pub upgrade     # constraint-এর ভেতরে upgrade
```

**Interviewer কেন জিজ্ঞেস করে:** প্রতিটা project শুরু হয় pubspec.yaml দিয়ে। তাঁরা মাপেন আপনি সত্যিকারের project সামলাতে পারেন কি না — conflict সমাধান, path dependency দিয়ে monorepo সাজানো, আর dev dependency আলাদা রেখে build ছোট রাখা।

**সাধারণ ভুল:** সব জায়গায় `==` ব্যবহার করা, যাতে resolution প্রায় অসম্ভব হয়ে যায়। `build_runner`/`mockito`/`flutter_test`-কে `dependencies`-এ রাখা। আরেকটা: **app**-এর জন্য `pubspec.lock` commit করুন (reproducible build), কিন্তু **package**-এর জন্য নয় (consumer-দের নমনীয় resolution দরকার)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Caret `^` মানে কী?"* → "পরের major পর্যন্ত" — `^1.5.0` মানে `>=1.5.0 <2.0.0`।
- *"pubspec.lock কি commit করা উচিত?"* → App-এর জন্য হ্যাঁ, reusable package-এর জন্য না।

**সম্পর্কিত:** [Q21 — SDK channel ও version](#q21) · [Q23 — SDK constraint](#q23)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q21"></a>21. Flutter-এর SDK channel কী কী — stable, beta আর master? Production-এ কোনটা ব্যবহার করা উচিত?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q21)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Stable হলো production-ready track, প্রায় প্রতি তিন মাসে release হয় আর ভালোভাবে test করা হয় — Google-এর নিজের app দিয়েও। Production-এর জন্য এটাই একমাত্র channel। Beta হলো মাসিক preview, যেখানে feature প্রায় চূড়ান্ত। Master হলো একদম সামনের প্রান্ত, দিনে অনেকবার update হয়, আর যেকোনো সময় ভেঙে যেতে পারে — শুধু Flutter contributor বা পরীক্ষার জন্য।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Stable (production-এ এটাই ব্যবহার করুন)।**
Production-ready release, মোটামুটি প্রতি তিন মাসে (যেমন 3.22, 3.24)। ভালোভাবে test করা হয়, Google Pay আর Google Ads-এও। Patch release-এর মধ্যে API বদলায় না (3.22.0 → 3.22.1)। তাই একই stable line-এর ভেতরে কোনো breaking change নেই।

**ধাপ ২ — Beta (preview / আগেভাগে test)।**
প্রায় প্রতি মাসে update হয়। Feature সম্পূর্ণ, কিন্তু আরও বড় পরিসরে test চলছে। Stable-এ পৌঁছানোর আগে API এখনো বদলাতে পারে। আসন্ন কোনো feature দেখতে বা পরের stable-এর সাথে আপনার app আগেভাগে test করতে এটা ব্যবহার করুন — কিন্তু user-এর কাছে ship করবেন না।

**ধাপ ৩ — Master (bleeding edge)।**
Flutter repo-র `main` branch, প্রতিটা merge-এর সাথে update হয়, দিনে অনেকবার। এটা পরীক্ষামূলক আর যেকোনো সময় ভেঙে যেতে পারে। শুধু Flutter-এ contribute করতে, বা beta-তে না আসা কোনো fix নিতে ব্যবহার করুন।

```bash
flutter channel              # এখনকার channel দেখায়
flutter channel stable       # production-এর জন্য
flutter upgrade              # switch করার পরে সবসময় upgrade করুন

flutter --version
# Flutter 3.24.0 • channel stable • ...
```

**ধাপ ৪ — CI-তে version pin করুন।**
CI-তে "latest stable"-এর উপর ভরসা করবেন না। নির্দিষ্ট একটা version pin করুন, যাতে প্রতিটা machine একই জিনিস build করে। এতে "আমার machine-এ তো চলে" ধরনের সমস্যা এড়ানো যায়।

```bash
flutter version 3.22.2       # CI-তে নির্দিষ্ট version pin করুন
```

**ধাপ ৫ — Channel বনাম version।**
Channel হলো একটা *release track*; version হলো একটা *নির্দিষ্ট build*। আপনি stable channel-এ থেকেও 3.22.2 version-এ থাকতে পারেন। Channel বলে আপনি কোন track অনুসরণ করছেন, ঠিক কোন version নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা পেশাগত পরিপক্বতা মাপে। Junior-রা master-এ চকচকে feature-এর পেছনে ছোটেন। Senior-রা release management, reproducible build, আর feature ship করার বদলে framework-এর bug debug করার খরচ বোঝেন।

**সাধারণ ভুল:** "stable-এ feature নেই" বলে production-এ beta/master ব্যবহার করা। Stable-এ প্রায় সবসময়ই একটা নিরাপদ বিকল্প থাকে। আরেকটা ভুল — CI-তে SDK version pin না করা। আর channel-কে version-এর সাথে গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"পরের release-এর সাথে নিরাপদে test করবেন কীভাবে?"* → মাঝে মাঝে CI beta-তে চালান, যাতে breaking change আগেই ধরা পড়ে, কিন্তু beta ship করবেন না।
- *"Channel বনাম version — পার্থক্য কী?"* → Channel = track (stable/beta/master); version = নির্দিষ্ট build (যেমন 3.22.2)।

**সম্পর্কিত:** [Q20 — version constraint](#q20) · [Q19 — dev loop](#q19)

[↑ উপরে ফিরুন](#toc)

---

# G. Flutter আর Dart একসাথে কীভাবে কাজ করে (গভীর architecture)

---

## <a id="q22"></a>22. Flutter-এর তিনটি architecture layer — Embedder, Engine আর Framework — ব্যাখ্যা করুন। এরা একে অপরের সাথে কীভাবে কথা বলে?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q22)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flutter তিনটি layer-এর। Embedder হলো পাতলা, platform-নির্দিষ্ট host। এটা Flutter-কে একটা window, input event আর vsync দেয়। Engine হলো C++ core, যার ভেতরে Dart runtime, rendering engine আর text layout থাকে। Framework হলো Dart layer, যেটা আমি আসলে ব্যবহার করি — render object, widget আর Material/Cupertino। Framework নিচের দিকে engine-এ layer tree পাঠায়, আর engine উপরের দিকে event ও vsync পাঠায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: মঞ্চ, কলাকুশলী আর script।**
Embedder হলো *মঞ্চ*, যেটা platform দেয়। Engine হলো *পেছনের কলাকুশলী* (আলো, শব্দ, ভারী যন্ত্রপাতি)। Framework হলো *script আর অভিনেতা*, যেটা আপনি লেখেন। আপনি script নিয়ে কাজ করেন; কলাকুশলীরা সেটাকে মঞ্চে সত্যিকারের show বানিয়ে দেন।

**ধাপ ২ — Embedder layer (platform-native, পাতলা)।**
প্রতিটা platform-এ আলাদা (Android-এ Kotlin/Java, iOS-এ Swift/Obj-C, Windows-এ C++, web-এ JS)। এটা native app-এর ভেতরে engine host করে: window/surface বানায়, touch/keyboard/lifecycle event পাঠায়, display-এর vsync দেয়, render surface দেয়, platform channel route করে, আর accessibility (TalkBack/VoiceOver) সংযুক্ত করে।

**ধাপ ৩ — Engine layer (C/C++, precompiled হয়ে ship হয়)।**
মূল runtime, প্রতিটা app-এর সাথে precompiled binary হিসেবে যায়। এর ভেতরে আছে:
- **Dart runtime** (debug/profile-এ VM; release-এ AOT runtime support) — memory, GC, isolate।
- **Rendering engine** — Impeller (বা Skia) layer tree-কে pixel-এ বদলায়।
- **Text layout** — HarfBuzz, ICU, libtxt; এই কারণেই সব platform-এ text একই রকম দেখায়।
- **Platform-channel codec** আর নিচু স্তরের I/O।

**ধাপ ৪ — Framework layer (Dart, যেটা আপনি লেখেন)।**
নিচ থেকে উপরে:
- **`dart:ui`** — পাতলা binding, engine-এর feature খুলে দেয় (Canvas, SceneBuilder)।
- **Rendering** — RenderObject tree, layout, paint, hit-testing।
- **Widgets** — Element tree, reconciliation, Stateless/Stateful/Inherited widget।
- **Material / Cupertino** — উঁচু স্তরের design widget।

**ধাপ ৫ — এরা কীভাবে কথা বলে।**
- Framework → Engine: একটা `LayerTree` বানায় আর `dart:ui` দিয়ে জমা দেয় (`SceneBuilder`, `window.render(scene)`)।
- Engine → Framework: `dart:ui` hook দিয়ে vsync, input আর lifecycle উপরে পাঠায় (`onBeginFrame`, `onPointerDataPacket`)।
- Engine ↔ Embedder: embedder engine-এর C API call করে (surface, input, vsync); engine platform-এর কাজের জন্য ফিরতি call করে (clipboard, haptics)।
- Framework ↔ Native code: platform channel binary message engine হয়ে embedder-এ নিয়ে যায়, আর embedder সেটা plugin code-এ route করে।

```dart
// একটা tap-এর পথ অনুসরণ করুন, hardware → আপনার Dart:
// 1. EMBEDDER: Android একটা MotionEvent পায় → engine-এ pointer data পাঠায়
// 2. ENGINE: একটা PointerDataPacket বানায় → window.onPointerDataPacket call করে
// 3. FRAMEWORK: GestureBinding hit-test করে → আপনার onTap চলে:
GestureDetector(
  onTap: () => setState(() => _tapped = true),
  // setState → build → নতুন LayerTree → নিচে engine-এ → rasterize → দেখা যায়
  child: const Text('Tap me'),
)

// Platform channel: Dart → Engine → Embedder → native code
const platform = MethodChannel('com.example/battery');
final level = await platform.invokeMethod('getBatteryLevel');
```

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি Flutter-কে একটা পুরো system হিসেবে দেখেন, নাকি শুধু একটা widget toolkit হিসেবে। Plugin লেখা, platform-নির্দিষ্ট সমস্যা debug করা আর rendering optimize করার জন্য এটা দরকার — senior পদে ঠিক এটাই আশা করা হয়।

**সাধারণ ভুল:** বলা যে Flutter React Native-এর মতো platform-এর native widget ব্যবহার করে। এটা **করে না** — Flutter নিজের engine দিয়ে প্রতিটা pixel নিজে আঁকে; embedder শুধু একটা canvas আর event দেয়। আরেকটা ভুল — মনে করা `dart:ui` নিজেই engine। এটা শুধু engine-এর একটা পাতলা Dart binding।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter-এর text iOS আর Android-এ একই রকম দেখায় কেন?"* → Text layout থাকে engine-এ (HarfBuzz/ICU), OS-এ নয়।
- *"Embedder কোন কাজটা করে না?"* → এটা widget render করে না; শুধু engine host করে আর event/surface/vsync পাঠায়।

**সম্পর্কিত:** [Q23 — engine-এর ভেতরে Dart runtime](#q23) · [Q12 — thread](#q12) · [Q17 — pipeline](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q23"></a>23. Flutter আর Dart একসাথে কীভাবে কাজ করে? Dart VM কীভাবে embed করা হয়, আর Dart কীভাবে native code-এ পৌঁছায় (JIT বনাম AOT)?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-02-flutter-internals.md#q23)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart runtime সরাসরি Flutter engine-এর ভেতরে compile করা থাকে — Dart আলাদা process হিসেবে চলে না। Debug-এ এটা JIT-compiled, আর এই কারণেই hot reload সম্ভব হয়। Release-এ এটা AOT-compiled হয়ে native machine code হয়ে যায়, তাই কোনো interpreter থাকে না আর startup দ্রুত হয়। Dart engine-এর সাথে কথা বলে `dart:ui` binding দিয়ে, যেগুলো C++ engine call-এ map করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Dart runtime engine-এর ভেতরেই থাকে।**
Flutter app চালু হলে embedder engine চালু করে, আর engine Dart runtime চালু করে। Dart হলো *engine process-এর ভেতরের একটা component* — V8-এর উপর চলা Node-এর মতো আলাদা program নয়।

**ধাপ ২ — Debug mode (JIT — Just-In-Time)।**
পুরো Dart VM তার JIT compiler-সহ থাকে। Source **Kernel bytecode**-এ (`.dill`) compile হয়; runtime-এ VM সেটা চালায় আর গরম path গুলো JIT-compile করে। এটাই **hot reload** সম্ভব করে: VM চলমান isolate-এ নতুন Kernel ঢুকিয়ে দিতে পারে আর `build()` আবার চালাতে পারে। JIT-এর বাড়তি খরচ আর চালু থাকা assertion-এর কারণে এটা release-এর চেয়ে ধীর।

```text
debug:   .dart → Kernel .dill → VM interprets + JIT-compiles at runtime
         → hot reload works, assertions on, slower
```

**ধাপ ৩ — Release mode (AOT — Ahead-Of-Time)।**
`gen_snapshot` **build time**-এ Kernel-কে native ARM/x86-এ compile করে। ফলাফল হলো একটা shared library (Android-এ `.so`, iOS-এ `App.framework`-এর ভেতরে)। Runtime-এ একটা হালকা Dart runtime (JIT নেই, interpreter নেই) শুধু memory, GC আর isolate সামলায় — সব code আগে থেকেই native।

```text
release: .dart → Kernel .dill → gen_snapshot (AOT) → native .so / .framework
         → no VM compile, fast startup, no hot reload, no reflection
profile: AOT like release, but with DevTools/profiling support
```

**ধাপ ৪ — Dart কীভাবে engine-কে call করে (নিচের দিকে)।**
Dart `dart:ui`-এর class call করে (`Canvas.drawRect`, `SceneBuilder.pushTransform`)। এগুলো binding, যেগুলো C++ engine-এর method-এ map করে। একটা frame তৈরি হলে framework `window.render(scene)` call করে, আর composite করা scene rasterize করার জন্য engine-এর হাতে দেয়।

```dart
import 'dart:ui' as ui;
// Framework → Engine (নিচের দিকে):
final recorder = ui.PictureRecorder();
final canvas = ui.Canvas(recorder);
canvas.drawRect(const Rect.fromLTWH(0, 0, 100, 100),
    ui.Paint()..color = const ui.Color(0xFF0000FF)); // C++-এ native call
final scene = (ui.SceneBuilder()..addPicture(ui.Offset.zero, recorder.endRecording())).build();
ui.PlatformDispatcher.instance.views.first.render(scene); // engine-এর হাতে দেওয়া
```

**ধাপ ৫ — Engine কীভাবে Dart-কে call করে (উপরের দিকে)।**
`dart:ui` দিয়ে register করা Dart callback-এর reference engine ধরে রাখে। প্রতিটা vsync-এ এটা `onBeginFrame` তারপর `onDrawFrame` call করে; touch হলে `onPointerDataPacket` call করে। এই callback গুলোই framework-এর frame loop চালায় (আপনি এগুলো কখনো লেখেন না — `WidgetsBinding` সেট করে দেয়)।

**Interviewer কেন জিজ্ঞেস করে:** এটা আলাদা করে দেয় কারা পুরো compile/runtime model বোঝেন, আর কারা শুধু widget লেখেন। এটা ব্যাখ্যা করে hot reload কেন শুধু debug-এ, release কেন দ্রুত, আর reflection (`dart:mirrors`) কেন পাওয়া যায় না।

**সাধারণ ভুল:** বলা "Dart interpreted"। Release-এ এটা পুরোপুরি AOT-compiled native code। আরেকটা ভুল — মনে করা Dart VM Node-এর মতো আলাদা চলে; আসলে এটা engine-এর সাথে statically link করা, একটাই process। আর debug-এর ধীরগতির জন্য শুধু JIT-কে দোষ দেওয়া — assertion আর instrumentation-ও এখানে ভূমিকা রাখে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Release-এ hot reload নেই কেন?"* → AOT code হলো স্থির native machine code; নতুন Kernel ঢোকানোর মতো কোনো VM নেই।
- *"Release-এ reflection পাওয়া যায় না কেন?"* → AOT অব্যবহৃত code tree-shake করে ফেলে, তাই `dart:mirrors` runtime-এ type দেখতে পারে না।

**সম্পর্কিত:** [Q22 — engine layer](#q22) · [Q19 — JIT hot reload সম্ভব করে](#q19)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (আগের রাতের review)

Interview-এর দিন সকালে এটা পড়ুন। আগে দ্রুত তুলনার table-গুলো, তারপর এক লাইনের reminder-গুলো।

## দ্রুত তুলনার table

**তিনটা tree**

| Tree | এটা কী | আয়ু | খরচ |
|---|---|---|---|
| Widget | আপনার লেখা blueprint | প্রতি rebuild-এ ফেলে দেওয়া হয় | সস্তা |
| Element | জীবন্ত সেতু + `State` ধরে রাখে | দীর্ঘজীবী | মাঝারি |
| RenderObject | layout ও paint করে | আবার ব্যবহার হয়, খুব কমই নতুন হয় | ব্যয়বহুল |

**Stateless vs Stateful**

| | StatelessWidget | StatefulWidget |
|---|---|---|
| বদলে যাওয়া data | নেই | আছে, একটা `State` object-এ |
| নিজে rebuild করে | না (শুধু parent rebuild করায়) | হ্যাঁ, `setState` দিয়ে |
| State থাকে | — | Element-এ |

**Keys**

| Key | পরিচয় কীসে | কোন কাজে |
|---|---|---|
| `ValueKey` | একটা value (`==`) | stable id আছে এমন list item |
| `ObjectKey` | reference (`identical`) | value-তে সমান কিন্তু reference-এ আলাদা object |
| `UniqueKey` | সবসময় unique | জোর করে নতুন element/state বানানো |
| `GlobalKey` | পুরো app জুড়ে | বাইরে থেকে state-এ পৌঁছানো (যেমন Form) |

**MediaQuery vs LayoutBuilder**

| MediaQuery | LayoutBuilder |
|---|---|
| পুরো screen-এর তথ্য | আপনার আসল constraints |
| সব জায়গায় একই | আপনার জায়গার উপর নির্ভর করে |
| phone vs tablet breakpoint | আশেপাশের জায়গা অনুযায়ী মানিয়ে নেয় |

**Constraints**

| শব্দ | মানে |
|---|---|
| tight | min == max (কোনো পছন্দ নেই) |
| loose | min = 0 (max পর্যন্ত স্বাধীন) |
| unbounded | max = infinity (scrollable-এর ভেতরে) |

**Hot Reload vs Hot Restart vs Full Restart**

| | Hot Reload | Hot Restart | Full Restart |
|---|---|---|---|
| State | থাকে | মুছে যায় | মুছে যায় |
| `main`/`initState` চলে | না | হ্যাঁ | হ্যাঁ |
| Native code | না | না | আবার build হয় |
| গতি | ~1s | কয়েক সেকেন্ড | 30s+ |

**JIT vs AOT**

| JIT (debug) | AOT (release) |
|---|---|
| চলার সময়ে compile | চালানোর আগে compile |
| hot reload সম্ভব করে | দ্রুত startup, native |
| ধীর (assertion চালু) | reflection নেই, hot reload নেই |

## এক লাইনের reminder

- **তিনটা tree**: Widget = সস্তা blueprint, Element = জীবন্ত সেতু + state, RenderObject = ব্যয়বহুল layout/paint। ([Q1](#q1))
- **Widget immutable** আর সস্তা; ব্যয়বহুল render object-গুলো element-এর মাধ্যমে আবার ব্যবহার হয়। ([Q2](#q2))
- **Key** widget মেলায় পরিচয় দিয়ে, position দিয়ে নয় — list-এ `ValueKey(id)` ব্যবহার করুন, `GlobalKey` খুব কম। ([Q3](#q3))
- **Reconciliation**: একই type + একই key → আবার ব্যবহার; নাহলে ফেলে দিয়ে নতুন করে বানানো। ([Q4](#q4))
- **State থাকে Element-এ**, এই কারণেই rebuild-এর পরেও টিকে যায়। ([Q5](#q5))
- **Lifecycle**: initState (setup) → didChangeDependencies (নিরাপদ context) → build; পরিষ্কার করতে dispose। ([Q6](#q6))
- **`setState`** data বদলায় + dirty চিহ্ন দেয় → পরের frame-এ শুধু এই subtree-র একটা rebuild। `await`-এর পরে `mounted` check করুন। ([Q7](#q7))
- **BuildContext-ই Element** — `initState`-এ inherited lookup নয়; `didChangeDependencies` ব্যবহার করুন। ([Q8](#q8))
- **InheritedWidget** শুধু registered dependent-দের rebuild করে; Provider এটাকে সুন্দর API দিয়ে মুড়ে দেয়। ([Q9](#q9))
- **`const`** widget একই object → reconciliation সাথে সাথে সেগুলো বাদ দিয়ে যায়। ([Q10](#q10))
- **RepaintBoundary** ঘন ঘন repaint-কে আলাদা layer-এ সরিয়ে রাখে — বেশি ব্যবহার করবেন না। ([Q11](#q11))
- **UI thread = আপনার Dart**, **raster thread = GPU**। লাল UI bar → আপনার code ঠিক করুন; লাল raster bar → GPU-র কাজ ঠিক করুন। ([Q12](#q12))
- **Layout**: constraints নিচে যায়, size উপরে আসে, parent position ঠিক করে — এক pass, O(n)। ([Q13](#q13))
- **Unbounded** (infinity) constraints scrollable-এর ভেতরে fill/flex widget ভেঙে দেয় — একটা bounded size দিন। ([Q14](#q14))
- **RenderFlex overflow** → `Expanded`/`Flexible`, ellipsis text, বা একটা scroll view। ([Q15](#q15))
- **MediaQuery** = পুরো screen; **LayoutBuilder** = আপনার আসল জায়গা। পুনরায় ব্যবহারযোগ্য widget-এ LayoutBuilder-ই ভালো। ([Q16](#q16))
- **Pipeline**: build → layout → paint (layers) → composite → rasterize (raster thread) → display। ([Q17](#q17))
- **Impeller** shader আগেই compile করে রাখে (jank নেই); **Skia** সেগুলো runtime-এ compile করত (প্রথম frame-এ jank)। ([Q18](#q18))
- **Hot Reload** state রাখে; **Hot Restart** Dart state মুছে দেয়; **Full Restart** native আবার build করে। ([Q19](#q19))
- **`^1.5.0`** = `>=1.5.0 <2.0.0`; test tool `dev_dependencies`-এ রাখুন; app-এর জন্য `pubspec.lock` commit করুন। ([Q20](#q20))
- Production-এ **stable**; আগে থেকে পরখ করতে **beta**; **master** শুধু contributor-দের জন্য। CI-তে version pin করুন। ([Q21](#q21))
- **তিনটা layer**: Embedder (host) → Engine (C++ core, Dart runtime, rendering) → Framework (আপনার Dart)। ([Q22](#q22))
- **Debug-এ Dart JIT** (hot reload), **release-এ AOT native** (দ্রুত, reflection নেই); runtime থাকে engine-এর ভেতরে। ([Q23](#q23))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যায়

Interviewer সাধারণত এক প্রশ্নে থামেন না। আপনার গভীরতা মাপতে তাঁরা খুঁড়তেই থাকেন। এই chain-টা মুখে বলে অনুশীলন করুন — শান্তভাবে, ধাপে ধাপে:

1. *"তিনটা tree কী কী?"* → Widget (blueprint), Element (জীবন্ত সেতু + state), RenderObject (layout/paint)।
2. *"তাহলে Flutter কীভাবে সেকেন্ডে ৬০ বার widget rebuild করতে পারে?"* → Widget সস্তা; element ব্যয়বহুল render object-গুলো আবার ব্যবহার করে।
3. *"Element কীভাবে ঠিক করে যে আবার ব্যবহার করবে?"* → একই type আর key → আবার ব্যবহার করে property update করে; নাহলে ফেলে দিয়ে নতুন করে বানায়।
4. *"তাহলে list-এ key কেন দরকার?"* → Key ছাড়া মেলানো হয় position দিয়ে, তাই order বদলালে state ভুল item-এ লেগে যায়।
5. *"ঘন ঘন বদলায় এমন item-কে কীভাবে সস্তা করবেন?"* → স্থির অংশে `const`, repaint আলাদা রাখতে `RepaintBoundary`, আর `build()` হালকা রাখা।

এভাবে শান্তভাবে ধাপে ধাপে যেতে পারা — আন্দাজ না করে — ঠিক এটাই আপনাকে **senior** শোনায়, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

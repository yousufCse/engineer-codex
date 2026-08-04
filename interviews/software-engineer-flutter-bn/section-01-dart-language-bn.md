# Section 1 — Dart Language

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যাসহ**, আর **link করা** — তাই এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন।
> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-01-dart-language-bn.md](../software-engineer-flutter/section-01-dart-language.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব জীবনের উদাহরণ আর code দিয়ে ধাপে ধাপে বিস্তারিত ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সংযুক্ত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে আসুন।

প্রতিটা প্রশ্নে tag দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তরটা** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন "আরেকটু গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলা নিজেই একটা senior skill — remote আর BD দুই ধরনের কোম্পানিতেই এটা একইভাবে কাজ করে।

---

<a id="toc"></a>

## সূচিপত্র

**A. Variables, null safety ও types**
1. [Null safety — `?`, `!`, `late`, `required`](#q1) · *Very common*
2. [`var`, `dynamic`, `Object`, `final`, `const`](#q2) · *Very common*
3. [`const` constructor ও Flutter performance](#q3) · *Common*
4. [Equality — `==`, `hashCode`, `identical`](#q4) · *Very common*
5. [Generics ও bounded generics](#q5) · *Common*
6. [Exception vs Error](#q6) · *Common*

**B. Functions ও closures**
7. [Named / positional / optional parameters](#q7) · *Very common*
8. [Closures](#q8) · *Common*
9. [Cascade `..` vs method chaining](#q9) · *Common*
10. [`typedef`, spread `...`, collection if/for](#q10) · *Common*

**C. Classes ও object-oriented Dart**
11. [Constructors — normal / named / factory / const / redirecting](#q11) · *Very common*
12. [`extends` vs `implements` vs `with` vs `on`](#q12) · *Very common*
13. [Mixins গভীরভাবে](#q13) · *Common*
14. [Extension methods](#q14) · *Common*
15. [Enhanced enums](#q15) · *Common*

**D. Dart 3-এর নতুন feature**
16. [Records](#q16) · *Very common*
17. [Patterns ও switch expressions](#q17) · *Very common*
18. [Sealed classes ও class modifiers](#q18) · *Common*

**E. Async ও concurrency**
19. [Future ও async/await](#q19) · *Very common*
20. [Event loop — microtask vs event queue](#q20) · *Deeper*
21. [Streams — single vs broadcast](#q21) · *Very common*
22. [Generators — `sync*` / `async*`](#q22) · *Common*
23. [Isolates ও `compute()`](#q23) · *Very common*

**F. Dart কীভাবে চলে (compile ও memory)**
24. [JIT vs AOT](#q24) · *Common*
25. [Dart VM](#q25) · *Deeper*
26. [Garbage collection](#q26) · *Deeper*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---

<a id="study-plan"></a>

## ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

২৬টা প্রশ্ন একসাথে পড়ার দরকার নেই। নিচের পর্যায়গুলো ক্রম অনুযায়ী শেষ করুন — প্রতিটা আগেরটার উপর দাঁড়ায়। একটা পর্যায় তখনই টিক দিন, যখন না দেখে **সংক্ষিপ্ত উত্তরটা** বলতে পারবেন।

**পর্যায় ১ — মূল ভিত্তি (এখান থেকে শুরু করুন)।** এগুলো প্রায় প্রতিটা interview-এ আসে।
→ [Q1 Null safety](#q1) · [Q2 var/final/const](#q2) · [Q7 Parameters](#q7) · [Q19 Future ও async](#q19) · [Q21 Streams](#q21)

**পর্যায় ২ — Object-oriented Dart।** আপনি class কীভাবে design করেন।
→ [Q11 Constructors](#q11) · [Q12 extends/implements/with/on](#q12) · [Q4 Equality](#q4) · [Q13 Mixins](#q13) · [Q14 Extensions](#q14)

**পর্যায় ৩ — আধুনিক Dart 3 (দেখায় আপনি হালনাগাদ আছেন)।**
→ [Q16 Records](#q16) · [Q17 Patterns](#q17) · [Q18 Sealed classes](#q18) · [Q15 Enhanced enums](#q15)

**পর্যায় ৪ — গভীরতা ও senior signal।**
→ [Q3 const ও performance](#q3) · [Q5 Generics](#q5) · [Q6 Exceptions](#q6) · [Q9 Cascade](#q9) · [Q10 typedef/spread](#q10) · [Q22 Generators](#q22) · [Q23 Isolates](#q23)

**পর্যায় ৫ — গভীর tie-breaker (সবার শেষে)।** এগুলোই শক্ত senior-দের বাকিদের থেকে আলাদা করে।
→ [Q20 Event loop](#q20) · [Q24 JIT vs AOT](#q24) · [Q25 Dart VM](#q25) · [Q26 Garbage collection](#q26)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই আটটা দেখে নিন:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q12](#q12) · [Q19](#q19) · [Q20](#q20) · [Q21](#q21) · [Q23](#q23), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Variables, null safety ও types

---

<a id="q1"></a>
## 1. Dart-এ null safety কী? `?`, `!`, `late`, আর `required` ব্যাখ্যা করুন।

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Null safety মানে একটা variable-এ `null` রাখা যাবে না, যদি না আমি স্পষ্ট করে অনুমতি দিই। Null safety আসার আগে যেকোনো object চুপচাপ null হতে পারত। আর null object ব্যবহার করলে app crash করত। এখন Dart এই ভুলটা ধরে ফেলে code লেখার সময়েই — app চালু হওয়ার অনেক আগে। ফলে একটা পুরো ধরনের crash একেবারে চলে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Null safety কোন সমস্যা সমাধান করে।**
Null safety আসার আগে এই code দেখতে ঠিক লাগত, কিন্তু আসল user-এর কাছে গিয়ে crash করত:

```dart
String name = null;   // পুরোনো Dart-এ এটা allowed ছিল
print(name.length);   // runtime-এ crash: "name is null"
```

Bug ধরা পড়ত app ship করার পরে — সবচেয়ে খারাপ সময়ে। Null safety ভুলটাকে code লেখার সময়ে নিয়ে আসে। সেখানে ঠিক করা সস্তা:

```dart
String name = null;   // সাথে সাথেই editor-এ লাল error
```

মূল কথা এটাই: null-এর ভুল আগেই ধরুন, user-এর সামনে নয়।

**ধাপ ২ — `?` মানে "এটা null হওয়ার অনুমতি আছে।"**
সাধারণ type কখনোই null হতে পারে না। অনুমতি দিতে `?` যোগ করুন:

```dart
String  city = 'Dhaka';   // কখনোই null হতে পারবে না
String? nickname;          // null হতে পারে (শুরুতে null)

print(nickname?.length);   // ?. মানে — null না হলেই .length call করবে, নাহলে null দেবে
```

`?.` operator হলো maybe-null মান ব্যবহারের নিরাপদ উপায়। `nickname` null হলে পুরোটাই null হয়ে যায়, crash করে না।

**ধাপ ৩ — `!` মানে "আমি কথা দিচ্ছি, এটা এখন null নয়।"**
এটা compiler-কে দেওয়া একটা কথা। আপনার কথা ভুল হলে ঠিক ওই line-এ app crash করবে:

```dart
String? email = getEmail();
print(email!.length);   // email null হলে ঠিক এখানেই crash
```

তাই `!` ঝুঁকিপূর্ণ। এটা Dart-এর সুরক্ষা বন্ধ করে দেয়। 100% নিশ্চিত হলে তবেই ব্যবহার করুন।

**ধাপ ৪ — `late` মানে "একটু পরেই বসাব, কেউ পড়ার আগেই।"**
যখন মানটা সাথে সাথে বসানো যায় না, কিন্তু সেটা আসলে কখনোই null নয় — তখন এটা ব্যবহার করুন:

```dart
class ProfilePage {
  late String userId;            // এখনো set করা হয়নি, কিন্তু null-ও নয়

  void init(String id) {
    userId = id;                 // পরে set করা হলো
  }
}
// init() চলার আগে userId পড়লে LateInitializationError হবে
```

`late` lazy loading-এর জন্যও দারুণ — মানটা তৈরি হয় শুধু প্রথমবার ব্যবহারের সময়ে:

```dart
late final result = doExpensiveWork(); // 'result' প্রথমবার পড়ার সময়েই শুধু চলে
```

**ধাপ ৫ — `required` মানে "এই মানটা দিতেই হবে।"**
Flutter widget-এ এটা প্রচুর ব্যবহার হয়:

```dart
class LoginRequest {
  final String username;
  LoginRequest({required this.username}); // username ভুলে যাওয়া যাবে না
}

LoginRequest();                  // error: username দিতেই হবে
LoginRequest(username: 'srana'); // সঠিক
```

**ধাপ ৬ — বুদ্ধিমান অংশ: check-এর পরে Dart "promote" করে।**
একবার check করে ফেললেন মানটা null নয় — Dart এতটাই বুদ্ধিমান যে ওই line-এর নিচে সেটাকে not-null ধরে নেয়। তাই `!` লাগে না:

```dart
String greet(String? name) {
  if (name == null) return 'Hi guest';
  return 'Hi $name';   // Dart এখানে আগেই জানে name null নয়
}
```

**বোনাস — যে helper operator-গুলো আপনার জানা উচিত:**

```dart
final shown = nickname ?? 'Guest';   // ?? = nickname null হলে 'Guest' ব্যবহার করবে
nickname ??= 'Guest';                // ??= = এখন null হলে তবেই 'Guest' বসাবে
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি null safety-কে compiler-এর একটা guarantee হিসেবে নিচ্ছেন কি না। শুধু লাল error চাপা দেওয়ার জিনিস হিসেবে নয়। `!`-এর বদলে `if` check আর `??` ব্যবহার করা পরিপক্বতার লক্ষণ।

**সাধারণ ভুল:** লাল error দূর করতে সব জায়গায় `!` বসিয়ে দেওয়া। এতে crash শুধু আপনার screen (নিরাপদ) থেকে user-এর phone-এ (খারাপ) সরে যায়। প্রতিটা `!` মানে একটা জায়গায় আপনি Dart-এর সাহায্য বন্ধ করে দিলেন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`late` vs `final`?"* → `late` = পরে set করা। `final` = একবারই set করা। `late final` = পরে set করা, আর একবারই।
- *"`??` কী?"* → "null হলে এই default-টা ব্যবহার করো।" উদাহরণ: `final name = nickname ?? 'Guest';`
- *"'sound' null safety মানে কী?"* → "Sound" মানে guarantee-টা 100% নির্ভরযোগ্য — একটা type nullable না হলে Dart সত্যিই নিশ্চিত করে সেটা কখনোই null নয়।

**সম্পর্কিত:** [Q2 — var/dynamic/final/const](#q2)

[↑ উপরে ফিরুন](#toc)

---

<a id="q2"></a>
## 2. `var`, `dynamic`, `Object`, `final`, আর `const`-এর মধ্যে পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"এগুলো তিনটা আলাদা সমস্যার সমাধান করে। `var` Dart-কে type অনুমান করতে দেয়। `dynamic` type checking বন্ধ করে দেয় (ঝুঁকিপূর্ণ)। `Object` হলো সব type-এর নিরাপদ parent। `final` মানে একটা value শুধু একবারই set করা যায়। `const` মানে value নির্দিষ্ট, আর app চালু হওয়ার আগেই সেটা জানা থাকে।"

**এবার পুরোটা বুঝি:**

এই পাঁচটা শব্দ দেখতে একরকম লাগে, কিন্তু এরা তিনটা আলাদা প্রশ্নের উত্তর দেয়:
1. *এটার type কী?* → `var`, `dynamic`, `Object`
2. *এটা কি বদলাতে পারে?* → `final`, `const`

**ধাপ ১ — `var`: Dart-কে type অনুমান করতে দিন।**
আপনি type লিখবেন না; Dart value দেখে সেটা বের করে নেয়। এরপর type আর বদলায় না।

```dart
var count = 10;     // Dart 10 দেখে, তাই count চিরকালের জন্য int
// count = 'hello'; // error: count এখন int হিসেবে locked
```

**ধাপ ২ — `dynamic`: type checking বন্ধ করে দেয় (সাবধান)।**
`dynamic` বলে — "type নিয়ে আমার মাথাব্যথা নেই।" আপনি যেকোনো method call করতে পারবেন। সেই method না থাকলে crash হবে চলার সময়ে, code লেখার সময়ে নয়।

```dart
dynamic value = 'hello';
value = 42;                 // allowed
value.somethingFake();      // compile ঠিকঠাক হয়, কিন্তু চালালে crash
```

`dynamic` প্রায় কখনোই ব্যবহার করবেন না। একটাই বাস্তব কারণ — এলোমেলো JSON পড়া, যেখানে type সত্যিই অজানা।

**ধাপ ৩ — `Object`: সবকিছুর নিরাপদ parent।**
প্রতিটা type-ই একটা `Object`। কিন্তু `dynamic`-এর মতো নয়, এটা নিরাপদ — আসল type check করার আগে আপনি শুধু সেই method call করতে পারবেন যেগুলো সব object-এর আছে (যেমন `toString()`)।

```dart
Object thing = 'hello';
// print(thing.length);     // error: Object-এ 'length' নেই
if (thing is String) {
  print(thing.length);      // এখন Dart জানে এটা String
}
```

দ্রুত তুলনা: `dynamic` = "বিশ্বাস করো, check কোরো না" (বিপজ্জনক)। `Object` = "ব্যবহারের আগে check করো" (নিরাপদ)।

**ধাপ ৪ — `final`: শুধু একবার set হয়।**
একটা `final` variable একবারই assign হয়। Value ঠিক হতে পারে app চলার সময়ে (যেমন এখনকার সময়)। গুরুত্বপূর্ণ: `final` variable-টাকে lock করে, কিন্তু final list-এর ভেতরে এখনও পরিবর্তন করা যায়।

```dart
final now = DateTime.now();  // value ঠিক হয় runtime-এ, সমস্যা নেই
// now = DateTime.now();      // error: একবার set হয়ে গেছে

final items = [1, 2, 3];
items.add(4);                // OK! final বাক্সটা lock করে, ভেতরের জিনিস নয়
```

**ধাপ ৫ — `const`: নির্দিষ্ট, আর চালানোর আগেই জানা।**
একটা `const` value compile time-এ জানা থাকতে হবে (app চালু হওয়ার আগে)। এটা পুরোপুরি জমাট, আর Dart memory-তে একই জিনিস বারবার ব্যবহার করে।

```dart
const pi = 3.14;             // একটা নির্দিষ্ট সংখ্যা, সমস্যা নেই
const list = [1, 2, 3];
// list.add(4);              // error: const পুরোপুরি জমাট

// const bad = DateTime.now(); // error: now() শুধু চলার সময়ে জানা যায়
```

সহজে মনে রাখার উপায়:
- **`final`** = *বাক্সটা lock করা* (একবার set করতে পারবেন, runtime-এও)।
- **`const`** = *কারখানা থেকেই সবকিছু জমাট* (চালানোর আগেই জানা থাকতে হবে)।

**Interviewer কেন জিজ্ঞেস করে:** অনেকেই ভুল করে বলেন "final মানে constant।" তাঁরা আসল পার্থক্যটা শুনতে চান: `final` = একবার set; `const` = চালানোর আগেই জানা।

**সাধারণ ভুল:** ভাবা যে একটা `final List` পুরোপুরি অপরিবর্তনীয়। তা নয় — আপনি এখনও item যোগ বা বাদ দিতে পারবেন। শুধু `const` ভেতরের জিনিসগুলো জমাট করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`dynamic` কখন ব্যবহার করবেন?"* → প্রায় কখনোই না। শুধু অজানা JSON-এর জন্য হতে পারে। `Object` বা আসল একটা type নেওয়াই ভালো।
- *"`final` আর `const` কি একসাথে ব্যবহার করা যায়?"* → হ্যাঁ — class-level constant-এর জন্য `static const`। একটা variable হয় `final`, নাহয় `const` — দুটোই একসাথে নয়।

**সম্পর্কিত:** [Q1 — null safety](#q1) · [Q3 — const constructor](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q3"></a>
## 3. `const` constructor কী, আর এটা Flutter-এর performance-এ কীভাবে সাহায্য করে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`const` constructor Dart-কে পুরো object-টা app চালু হওয়ার আগেই বানিয়ে ফেলতে দেয়। এরপর Dart নতুন copy না বানিয়ে memory-তে একই object বারবার ব্যবহার করে। Flutter-এ `const` widget একবারই তৈরি হয়, আর rebuild-এর সময় বাদ পড়ে যায়। ফলে screen দ্রুত update হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — const constructor জিনিসটা কী।**
সাধারণ constructor প্রতিবার call করলে নতুন object বানায়। `const` constructor Dart-কে object-টা compile time-এ (চলার আগে) বানাতে দেয় — কিন্তু শুধু তখনই, যখন এর সব field `final` হয়।

```dart
class Point {
  final int x;
  final int y;
  const Point(this.x, this.y);  // const constructor (x আর y দুটোই final)
}
```

**ধাপ ২ — জাদুটা: Dart একই object আবার ব্যবহার করে।**
দুটো `const` object-এর value এক হলে Dart শুধু একটাই বানায়, আর সেটাই সব জায়গায় ভাগ করে দেয়। এটাকে বলে *canonicalization* — বড় একটা শব্দ, মানে শুধু "একই জিনিস আবার ব্যবহার করা"।

```dart
const a = Point(1, 2);
const b = Point(1, 2);
print(identical(a, b)); // true, memory-তে একই object (আবার ব্যবহার হলো)

final c = Point(1, 2);
print(identical(a, c)); // false, final নতুন object বানায়
```

**ধাপ ৩ — Flutter-এ এটা কেন গুরুত্বপূর্ণ (আসল সুবিধা)।**
Flutter খুব ঘন ঘন widget rebuild করে। আপনি যখন `const Text('Hello')` লেখেন, Flutter দেখে এটা গতবারের সেই একই object। তাই এটা rebuild করা বাদ দেয়। কম কাজ মানে আরও মসৃণ app, বিশেষ করে লম্বা list-এ।

```dart
// ভালো: এই Text একবার তৈরি হয়, প্রতিটা rebuild-এ আবার ব্যবহার হয়
const Text('Welcome');

// const ছাড়া: প্রতিটা rebuild-এ নতুন Text object তৈরি হয়
Text('Welcome');
```

তাই "যেখানে পারেন `const` ব্যবহার করুন" — এই পরামর্শটা এমনি এমনি নয়। এটা সরাসরি rebuild-এর কাজ কমায়।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান "সব জায়গায় const ব্যবহার করো" কথাটা আপনি শুধু মুখস্থ করেছেন, নাকি বুঝেছেন। আসল কারণ হলো: const object আবার ব্যবহার হয়, তাই Flutter সেগুলো rebuild করা বাদ দিতে পারে।

**সাধারণ ভুল:** কারণ ছাড়াই বলা যে const "দ্রুত করে দেয়"। কারণটা হলো: const object memory-তে ভাগ করে নেওয়া হয়, আর Flutter একই object আবার rebuild করে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"সব field-কে `final` হতে হয় কেন?"* → কারণ const object জমাট। কোনো field বদলাতে পারলে সেটা আর নির্দিষ্ট compile-time value থাকত না।
- *"একটা value যদি network থেকে আসে?"* → তাহলে সেটা `const` হতে পারবে না। বদলানো অংশটা আলাদা রাখুন, বাকিটা `const` করুন।

**সম্পর্কিত:** [Q2 — final vs const](#q2) · [Q26 — garbage collection](#q26)

[↑ উপরে ফিরুন](#toc)

---

<a id="q4"></a>
## 4. দুটো object সমান কি না কীভাবে check করবেন? `==`, `hashCode`, আর `identical` ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"সাধারণভাবে Dart দুটো object-কে সমান বলে শুধু তখনই, যখন সেগুলো হুবহু একই object। Value দিয়ে তুলনা করতে আমি `==` আর `hashCode` দুটোই একসাথে override করি — এদের সবসময় মিলতে হবে। বাস্তব project-এ আমি `Equatable` বা `freezed` ব্যবহার করি, যাতে হাতে লিখে ভুল না করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Default হলো "একই object" equality।**
সাধারণভাবে দুটো object সমান শুধু তখনই, যখন memory-তে সেগুলো আক্ষরিক অর্থে একটাই:

```dart
class User { final String name; User(this.name); }

final a = User('Sara');
final b = User('Sara');
print(a == b); // false! নাম এক, কিন্তু এরা দুটো আলাদা object
```

এটা দেখে অনেকে অবাক হন। Data এক, তবু `==` false। কারণ Dart identity মিলিয়েছে, value নয়।

**ধাপ ২ — তিনটা জিনিস, মানুষ দিয়ে বোঝানো।**
দুজন মানুষের কথা ভাবুন:
- **`identical(a, b)`** জিজ্ঞেস করে: *"এরা কি একই একজন মানুষ?"* (memory-তে একই object)
- **`==`** (value equality) জিজ্ঞেস করে: *"এরা কি দুই যমজ, যাদের সব তথ্য হুবহু এক?"*
- **`hashCode`** হলো একজনের ID নম্বরের মতো, যেটা দ্রুত খোঁজার কাজে লাগে।

**ধাপ ৩ — Value দিয়ে কীভাবে তুলনা করবেন (`==` আর `hashCode` override করা)।**
দুটোই একসাথে override করতে হবে। নিয়ম: `a == b` হলে `a.hashCode` আর `b.hashCode` অবশ্যই সমান হতে হবে।

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
  int get hashCode => Object.hash(amount, currency); // সহজ আর সঠিক
}

print(Money(100, 'BDT') == Money(100, 'BDT')); // এখন true
```

Field মেলাতে `Object.hash(...)` ব্যবহার করুন — নিজের বানানো হিসাব লিখবেন না।

**ধাপ ৪ — `hashCode` কেন গুরুত্বপূর্ণ (লুকানো bug)।**
`Set` আর `Map` আগে `hashCode` দিয়ে item দ্রুত খোঁজে, তারপর `==` দিয়ে নিশ্চিত হয়। আপনি `==` override করে `hashCode` ভুলে গেলে আপনার object `Set` বা `Map` থেকে "হারিয়ে" যেতে পারে:

```dart
final seen = <Money>{};
seen.add(Money(100, 'BDT'));
print(seen.contains(Money(100, 'BDT'))); // hashCode না থাকলে false!
```

**ধাপ ৫ — State management-এ এটা কেন গুরুত্বপূর্ণ।**
BLoC বা Riverpod-এ নতুন state object পুরোনোটার সাথে `==` হলে UI ঠিকভাবেই rebuild করে না। আপনার equality ভুল হলে হয় অতিরিক্ত rebuild হবে, নাহয় কখনোই rebuild হবে না। এই কারণেই `Equatable` আর `freezed` এত জনপ্রিয় (এরা `==` আর `hashCode` নিজে থেকেই তৈরি করে দেয়)।

**Interviewer কেন জিজ্ঞেস করে:** ভুল equality দুটো পরিচিত bug তৈরি করে: Set বা Map-এ item হারিয়ে যাওয়া, আর state management-এ screen ভুলভাবে rebuild হওয়া। তাঁরা জানতে চান আপনি `==` আর `hashCode`-এর contract-টা বোঝেন কি না।

**সাধারণ ভুল:** `==` override করে `hashCode` ভুলে যাওয়া (বা উল্টোটা)। সবসময় দুটোই করুন। আর `hashCode`-এ কখনোই বদলানো (mutable) field ব্যবহার করবেন না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`hashCode`-এ শুধু অপরিবর্তনীয় field কেন ব্যবহার করবেন?"* → Object-টা Set-এ ঢোকার পরে কোনো field বদলালে তার "ID" বদলে যায়। তখন Set আর সেটা খুঁজে পায় না।
- *"হাতে না লিখে এটা কীভাবে এড়াবেন?"* → `Equatable` বা `freezed` ব্যবহার করুন; এরা আপনার জন্য সঠিক `==` আর `hashCode` তৈরি করে দেয়।

**সম্পর্কিত:** [Q16 — records (built-in value equality)](#q16) · [Q3 — const & identical](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q5"></a>
## 5. আমরা generics কেন ব্যবহার করি? `<T>` আর bounded generics ব্যাখ্যা করুন।

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Generics দিয়ে আমি একবার code লিখে যেকোনো type-এর সাথে নিরাপদে সেটা আবার ব্যবহার করতে পারি। `List<int>` মানে শুধু int ঢুকবে আর int-ই বের হবে। Dart এটা code লেখার সময়েই check করে। `<T extends Comparable>`-এর মতো একটা bound একটা নিয়ম যোগ করে। ফলে আমি T-এর উপর নির্দিষ্ট কিছু method নিরাপদে ব্যবহার করতে পারি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Generics ছাড়া কী সমস্যা।**
Generics ছাড়া আপনাকে `dynamic` ব্যবহার করতে হতো। তাতে নিরাপত্তা চলে যায়:

```dart
List things = [1, 2, 'oops']; // মেশানো type, কোনো নিরাপত্তা নেই
int total = 0;
for (var t in things) total += t; // চলার সময়ে 'oops'-এ গিয়ে crash
```

**ধাপ ২ — Generics = লেবেল লাগানো একটা container।**
Generic-কে লেবেল লাগানো একটা বাক্স ভাবুন। "`int`-এর বাক্স"-এ শুধু int থাকে। লেবেলটা ভুল জিনিস ঢুকতে দেয় না — আর Dart সেটা code লেখার সময়েই check করে:

```dart
List<int> numbers = [1, 2, 3];
// numbers.add('oops'); // সাথে সাথেই ধরা পড়বে, runtime-এ নয়
```

**ধাপ ৩ — নিজের generic class লেখা।**
`<T>` হলো একটা placeholder। মানে — "caller যে একটা type বেছে নেবে।"

```dart
class Box<T> {
  final T value;
  const Box(this.value);
  T get content => value;
}

final intBox = Box<int>(5);        // T এখানে int
final textBox = Box<String>('hi'); // T এখানে String
```

**ধাপ ৪ — Bounded generics = লেবেলের উপর একটা নিয়ম।**
কখনো কখনো T-এর কিছু নির্দিষ্ট ক্ষমতা লাগে। Bound বলে দেয় "T-কে এই ধরনের type হতে হবে।" যেমন, মান তুলনা করতে হলে T-কে `Comparable` হতে হবে:

```dart
// T অবশ্যই comparable হতে হবে (যেমন number বা text), তাই compareTo() allowed
T bigger<T extends Comparable<T>>(T a, T b) =>
    a.compareTo(b) >= 0 ? a : b;

print(bigger<int>(5, 9));         // 9
print(bigger<String>('a', 'z'));  // 'z'
```

`extends Comparable` bound না থাকলে Dart জানত না যে T তুলনা করা যায়। তখন `compareTo` একটা error হতো।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি type-safe আর পুনরায় ব্যবহারযোগ্য code লেখেন কি না। নাকি `dynamic` ব্যবহার করে আশা করেন যে কিছু ভাঙবে না।

**সাধারণ ভুল:** `List<int>` কাজ করে এমন জায়গায় `List<dynamic>` বা খালি `List` ব্যবহার করা। এতে Dart-এর নিরাপত্তা ফেলে দেওয়া হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Bound কেন যোগ করবেন?"* → Bound ছাড়া Dart T-কে সাধারণ `Object` ধরে নেয়। তখন শুধু মৌলিক method ব্যবহার করা যায়। Bound আরও method খুলে দেয়।
- *"বাস্তব Flutter উদাহরণ?"* → `Future<User>`, `List<Widget>`, `StreamBuilder<int>` — generics সব জায়গায় আছে।

**সম্পর্কিত:** [Q2 — types](#q2)

[↑ উপরে ফিরুন](#toc)

---

<a id="q6"></a>
## 6. Dart-এ `Exception` আর `Error`-এর মধ্যে পার্থক্য কী?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`Exception` হলো এমন একটা সমস্যা যেটা আমি আগে থেকেই আশা করতে পারি এবং handle করতে পারি — যেমন network call fail করা। `Error` সাধারণত মানে আমার code-এ একটা bug — যেমন ভুল list index। তাই আমি exception ধরি আর handle করি। কিন্তু error লুকাই না, ঠিক করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সহজ পার্থক্য।**
- **Exception** = সঠিক code-এও যা ভুল হতে পারে (internet নেই, server-এর খারাপ response)। → ধরুন এবং handle করুন।
- **Error** = programmer-এর ভুল (ভুল index, কোনো কিছু ভুলভাবে call করা)। → code ঠিক করুন, ধরবেন না।

```dart
// Exception, আশা করা যায়, handle করুন:
throw const FormatException('Bad date format');

// Error, একটা bug, ঠিক করুন:
final list = [1, 2];
print(list[5]); // RangeError, আপনার code ভুল, ঠিক করুন
```

**ধাপ ২ — Exception ঠিকভাবে কীভাবে ধরবেন।**

```dart
Future<User> loadUser() async {
  try {
    return await api.fetchUser();
  } on TimeoutException {
    rethrow;                         // উপরে পাঠান, যাতে retry করা যায়
  } catch (e, stackTrace) {
    log('Failed to load user', e, stackTrace);
    throw UserLoadException();       // পরিষ্কার একটা app error-এ বদলে দিন
  } finally {
    print('done trying');            // 'finally' সবসময় চলে
  }
}
```

**ধাপ ৩ — জানা দরকার এমন তিনটি keyword।**
- **`on Type`** → শুধু একটা নির্দিষ্ট exception type ধরে।
- **`catch (e, stackTrace)`** → error আর সেটা কোথা থেকে এসেছে, দুটোই দেয়।
- **`rethrow`** → একই error আবার throw করে, মূল stack trace না হারিয়ে। (এর বদলে `throw e;` লিখলে ওই তথ্য হারিয়ে যায় — একটা সাধারণ ভুল।)
- **`finally`** → যাই হোক না কেন চলে (file বন্ধ করা, loading spinner লুকানোর জন্য ভালো)।

**ধাপ ৪ — নিজের exception বানান।**

```dart
class UserLoadException implements Exception {
  final String message;
  UserLoadException([this.message = 'Could not load user']);
  @override
  String toString() => 'UserLoadException: $message';
}
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি সব কিছু একটা খালি `catch (e) {}`-এ মুড়ে দেন কি না, যেটা আসল bug লুকিয়ে ফেলে।

**সাধারণ ভুল:** শুধু crash থামানোর জন্য সব error ধরে ফেলা। এতে bug লুকিয়ে যায় এবং পরে খুঁজে পাওয়া খুব কঠিন হয়। যা handle করতে পারেন সেটাই ধরুন। আসল bug development-এ সামনে আসতে দিন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`rethrow` বনাম `throw e`?"* → `rethrow` মূল stack trace রাখে (যেখানে আসলে শুরু হয়েছিল)। `throw e` সেটা reset করে দেয়, তাই সূত্রটা হারিয়ে যায়।
- *"`Error` type ধরা উচিত কি?"* → সাধারণত না। এগুলো মানে আপনার code ভুল — বরং code ঠিক করুন।

**সম্পর্কিত:** [Q19 — async-এর সাথে error handling](#q19)

[↑ উপরে ফিরুন](#toc)

---

# B. Functions ও closures

---

<a id="q7"></a>
## 7. Named, positional আর optional parameter কী? কোনটা কখন ব্যবহার করবেন?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Positional parameter order-এর উপর নির্ভর করে। এক-দুটো স্পষ্ট মানের জন্য এটা ভালো। Named parameter একটা label ব্যবহার করে, তাই code পড়তে পরিষ্কার লাগে — এই কারণেই Flutter widget সব জায়গায় এগুলো ব্যবহার করে। `required` একটা named parameter-কে বাধ্যতামূলক করে। আর `[ ]` একটা positional parameter-কে optional করে, একটা default মান সহ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Positional parameter (order গুরুত্বপূর্ণ)।**

```dart
int add(int a, int b) => a + b;
add(2, 3); // 5, order মেনেই pass করতে হবে
```

**ধাপ ২ — Default সহ optional positional (`[ ]` ব্যবহার করুন)।**

```dart
int increase(int x, [int by = 1]) => x + by;
increase(5);     // 6  (by-এর default 1)
increase(5, 10); // 15
```

**ধাপ ৩ — Named parameter (label ব্যবহার করে, খুব পড়ার উপযোগী)।**

```dart
void createUser({required String name, bool isAdmin = false}) {}

createUser(name: 'Sara');                 // isAdmin-এর default false
createUser(name: 'Sara', isAdmin: true);  // পরিষ্কার আর পড়ার উপযোগী
```

**ধাপ ৪ — অনেক মানের ক্ষেত্রে named parameter কেন ভালো।**
এই দুটো call তুলনা করুন:

```dart
createUser('Sara', true, false);                       // এই true/false মানে কী?
createUser(name: 'Sara', isAdmin: true, sendEmail: false); // নিজেই নিজেকে বোঝায়
```

সহজ নিয়ম: অনেকগুলো মান থাকলে, বা কোনো `true/false` মান থাকলে, named parameter ব্যবহার করুন। এগুলো নিজেই নিজেকে ব্যাখ্যা করে। আর code বদলালেও টিকে থাকে (order গুরুত্বপূর্ণ নয়)।

**Interviewer কেন জিজ্ঞেস করে:** ভালো parameter design একজন senior-এর লক্ষণ, যিনি পড়ার উপযোগী আর রক্ষণাবেক্ষণযোগ্য API লেখেন।

**সাধারণ ভুল:** খালি একটা `true` positional মান হিসেবে pass করা। ছয় মাস পরে কেউ মনে রাখে না ওই `true`-এর মানে কী।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা parameter কি required আর named দুটোই হতে পারে?"* → হ্যাঁ: `{required String name}`। এটাই সবচেয়ে সাধারণ Flutter style।
- *"Named parameter-এর default মান?"* → `{bool isAdmin = false}`।

**সম্পর্কিত:** [Q11 — constructor named param ব্যবহার করে](#q11)

[↑ উপরে ফিরুন](#toc)

---

<a id="q8"></a>
## 8. Closure কী? সহজ করে উদাহরণ দিয়ে ব্যাখ্যা করুন।

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Closure হলো এমন একটা function যেটা তার আশেপাশের variable মনে রাখে। বাইরের code শেষ হয়ে যাওয়ার পরেও মনে রাখে। এভাবেই callback তার data-তে হাত রাখতে পারে। মূল কথা: closure variable-টাকেই মনে রাখে, তার মানের জমে যাওয়া copy নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Backpack-এর ধারণা।**
Closure-কে একটা backpack ভাবুন। আপনি যখন একটা function বানান, সে কাছের variable-গুলো তার backpack-এ ভরে নেয়। তারপর সব জায়গায় সেগুলো নিয়ে ঘোরে — বাইরের function শেষ হয়ে যাওয়ার পরেও।

```dart
Function makeCounter() {
  var count = 0;            // এটা function-এর "backpack"-এ চলে যায়
  return () => ++count;     // return করা function count মনে রাখে
}

final next = makeCounter();
print(next()); // 1
print(next()); // 2  (call-এর মাঝে count মনে থাকে!)
print(next()); // 3
```

বাইরের function `makeCounter` আগেই শেষ হয়ে গেছে। তবু `count` return করা function-এর ভেতরে বেঁচে আছে। এটাই closure।

**ধাপ ২ — এটা variable মনে রাখে, copy নয়।**
এটা গুরুত্বপূর্ণ। Variable বদলে গেলে closure নতুন মানটাই দেখে:

```dart
int value = 10;
final show = () => print(value); // 'value' variable-টাকে মনে রাখে
value = 99;
show(); // 99 print করে, 10 নয় — সর্বশেষ মানটা পড়েছে
```

**ধাপ ৩ — Flutter-এ closure সব জায়গায় আছে।**
প্রতিটা button callback একটা closure। সে আশেপাশের data মনে রাখে:

```dart
ElevatedButton(
  onPressed: () => context.read<AuthBloc>().add(LoginPressed(user)),
  // এই closure context আর user "মনে রাখে"
  child: const Text('Login'),
);
```

**Interviewer কেন জিজ্ঞেস করে:** Closure-ই সব callback, `.then()` আর event handler চালায়। তাঁরা দেখতে চান আপনি বোঝেন data কীভাবে হাতের কাছে থেকে যায়।

**সাধারণ ভুল:** ভাবা যে closure মানটা copy করে রাখে। আসলে সে জীবন্ত variable-টাকেই মনে রাখে। তাই মান বদলাতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Closure নিয়ে কোনো বিপদ আছে?"* → হ্যাঁ। ভুল করে বড় object বা `context` বাঁচিয়ে রাখলে memory leak হতে পারে। দীর্ঘজীবী object-এর ভেতরে closure নিয়ে সাবধান থাকুন।

**সম্পর্কিত:** [Q19 — async callback](#q19) · [Q21 — stream listener](#q21)

[↑ উপরে ফিরুন](#toc)

---

<a id="q9"></a>
## 9. Cascade notation (`..`) কী? Method chaining থেকে এটা কীভাবে আলাদা?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Cascade (`..`) দিয়ে আমি একই object-এর উপর অনেক কাজ চালাতে পারি, বারবার তার নাম না লিখেই। প্রতিটা `..` কাজটার return করা জিনিস উপেক্ষা করে এবং মূল object-টাই ফেরত দেয়। Method chaining আলাদা — সেটা কাজ করে কারণ প্রতিটা method এমন কিছু return করে যার উপর পরেরটা call করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "আর সেই সাথে..." ধারণা।**
`..` মানে একই object নিয়ে বলা "...আর সেই সাথে...আর সেই সাথে..."।

```dart
// Cascade ছাড়া, প্রতিবার নাম লিখতে হয়:
final paint = Paint();
paint.color = Colors.red;
paint.strokeWidth = 4;
paint.style = PaintingStyle.stroke;

// Cascade দিয়ে, পরিষ্কার, একই object:
final paint2 = Paint()
  ..color = Colors.red
  ..strokeWidth = 4
  ..style = PaintingStyle.stroke;
```

দুটোই একই কাজ করে। কিন্তু cascade version ছোট আর পরিষ্কার।

**ধাপ ২ — Cascade বনাম method chaining (আসল পার্থক্য)।**
- **Cascade (`..`)** → return করা মান উপেক্ষা করে, সবসময় মূল object-টাই ফেরত দেয়। অনেক property set করার জন্য ভালো।
- **Method chaining (`a.b().c()`)** → কাজ করে শুধু এই কারণে যে প্রতিটা method একটা object return করে, যাতে চালিয়ে যাওয়া যায়।

```dart
// Method chaining: প্রতি ধাপে একটা String return হয়, তাই চলতে থাকে
final result = 'hello world'.toUpperCase().trim().substring(0, 5);

// Cascade: property set করলে কাজের কিছু return হয় না, তাই .. একদম ঠিক
final list = <int>[]..add(1)..add(2)..add(3);
```

**ধাপ ৩ — Null-safe cascade (`?..`)।**

```dart
paint?..color = Colors.blue; // paint null হলে কিছুই করে না
```

**Interviewer কেন জিজ্ঞেস করে:** এটা ছোট বিষয়। কিন্তু এতে বোঝা যায় আপনি return type পড়েন কি না, আর পরিষ্কার Dart লেখেন কি না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`?..` কী?"* → `..`-এর মতোই। তবে object null হলে এটা কিছুই করে না।

**সম্পর্কিত:** [Q10 — আরও syntax sugar](#q10)

[↑ উপরে ফিরুন](#toc)

---

<a id="q10"></a>
## 10. `typedef`, spread operator (`...`) আর collection `if`/`for` কী?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`typedef` একটা type-কে ডাকনাম দেয় — সাধারণত function type-কে — যাতে code পড়তে সহজ হয়। Spread operator আর collection `if`/`for` দিয়ে আমি পরিষ্কার ও পড়ার মতো করে list বানাতে পারি। Flutter-এর widget list-এর জন্য এটা খুব কাজের।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `typedef`: type-এর একটা ডাকনাম।**
Function type লম্বা হলে আর অনেকবার ব্যবহার হলে, তাকে একটা পরিষ্কার নাম দিন:

```dart
// typedef ছাড়া, লম্বা আর বারবার একই জিনিস:
void setValidator(String? Function(String value) check) {}

// typedef দিয়ে, পরিষ্কার:
typedef Validator = String? Function(String value);
void setValidator(Validator check) {}
```

`typedef` দিয়ে function ছাড়া অন্য type-এরও নাম দেওয়া যায়: `typedef Json = Map<String, dynamic>;`

**ধাপ ২ — Spread (`...`): এক list-কে আরেকটার ভেতরে ঢালা।**

```dart
final first = [1, 2];
final second = [3, 4];
final all = [...first, ...second]; // [1, 2, 3, 4]
```

`...?` হলো null-safe version (null না হলেই ঢালে):

```dart
final all = [...first, ...?maybeNullList];
```

**ধাপ ৩ — Collection `if` আর `for`: ভেতরে logic রেখেই list বানানো।**
Flutter-এর widget list-এ এটা অসম্ভব কাজের:

```dart
final widgets = [
  const Header(),
  if (isLoggedIn) const ProfileButton(),   // logged in হলেই যোগ হবে
  for (final item in items) ItemTile(item), // প্রতি item-এ একটা যোগ হবে
  ...?footerWidgets,                         // null না হলে list যোগ হবে
];
```

এটা না থাকলে `return`-এর আগে অনেক `if` block আর `.add()` call দিয়ে list বানাতে হতো — এলোমেলো আর পড়তে কঠিন।

**Interviewer কেন জিজ্ঞেস করে:** দেখতে চান আপনি পরিষ্কার, আধুনিক, declarative Dart লেখেন কি না। নাকি পুরোনো imperative কায়দায় list বানান।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Collection `if-else` আছে কি?"* → হ্যাঁ: list-এর ভেতরে `if (cond) WidgetA() else WidgetB()`।

**সম্পর্কিত:** [Q9 — cascade](#q9)

[↑ উপরে ফিরুন](#toc)

---

# C. Classes ও object-oriented Dart

---

<a id="q11"></a>
## 11. Dart-এর constructor ব্যাখ্যা করুন: normal, named, factory, const আর redirecting।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Normal constructor সবসময় নতুন object বানায়। Named constructor object বানানোর একটা পরিষ্কার দ্বিতীয় পথ দেয়। Factory constructor-কে নতুন object বানাতেই হবে না — সে cache করা object ফেরত দিতে পারে, এমনকি subtype-ও দিতে পারে। Redirecting মানে এক constructor আরেকটাকে call করে, যাতে একই code বারবার লিখতে না হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Normal (generative) constructor।**
প্রতিবার নতুন object বানায়। `this.x` shortcut সরাসরি field-এ মান বসিয়ে দেয়।

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name); // normal constructor
}
```

**ধাপ ২ — Named constructor (পরিষ্কার নাম দেওয়া দ্বিতীয় পথ)।**

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name);
  User.guest() : id = '0', name = 'Guest'; // named constructor
}

final u = User.guest(); // এটা কী করে, পরিষ্কার বোঝা যায়
```

**ধাপ ৩ — Initializer list (`:`-এর পরের অংশ)।**
`:`-এর পরের code constructor body-র আগে চলে। `final` field বসানো, `super(...)` call করা আর `assert` ব্যবহার করা — এগুলোর একমাত্র জায়গা এটাই।

```dart
User(String id, String name)
    : id = id,
      assert(id.isNotEmpty, 'id cannot be empty') {
  // initializer list-এর পরে body চলে
}
```

**ধাপ ৪ — Redirecting constructor (আরেকটা constructor call করা)।**
আরেকটা constructor-এ পাঠিয়ে দিয়ে একই logic বারবার লেখা এড়ায়:

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name);
  User.anonymous() : this('0', 'Anonymous'); // User(...)-এ redirect করে
}
```

**ধাপ ৫ — Factory constructor (বিশেষ জিনিসটা)।**
Factory-কে নতুন object বানাতেই হবে না। সে পারে:
- cache করা object ফেরত দিতে,
- subtype ফেরত দিতে,
- অথবা বানানোর সময়ে fail করতে (throw)।

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

`fromJson` ঠিক এই কারণেই factory — এটা fail করতে পারে, cache করা object দিতে পারে, বা subtype দিতে পারে। Normal constructor এসব পারে না।

**ধাপ ৬ — const constructor।**
Object-টা চলার আগেই বানিয়ে ফেলে (সব field `final` হতে হবে)। দেখুন [Q3](#q3)।

**Interviewer কেন জিজ্ঞেস করে:** অনেকে শুধু `fromJson` চেনেন, কিন্তু এটা কেন factory তা বলতে পারেন না। তাঁরা আসল কারণটা শুনতে চান: factory "এক call = এক নতুন object" নিয়মটা ভাঙতে পারে।

**সাধারণ ভুল:** ভাবা যে factory সবসময় নতুন object বানায়। তার দরকার নেই। আরেকটা ভুল — factory-র ভেতরে `this` ব্যবহার করার চেষ্টা। ওই সময়ে object-টা এখনো তৈরিই হয়নি।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Factory কি null ফেরত দিতে পারে?"* → না (null safety-তে return type non-null হতে হবে, যদি না nullable ঘোষণা করা হয়)। তাকে একটা বৈধ object ফেরত দিতেই হবে।
- *"Named নাকি factory — কখন কোনটা?"* → Named = object বানানোর সহজ বিকল্প পথ। Factory = যখন নিয়ন্ত্রণ দরকার (caching, subtype, validation)।

**সম্পর্কিত:** [Q3 — const constructor](#q3) · [Q12 — OOP keyword](#q12) · [Q7 — named parameter](#q7)

[↑ উপরে ফিরুন](#toc)

---

<a id="q12"></a>
## 12. Dart-এ `interface` keyword নেই। তাহলে interface কীভাবে পান? আর `extends`, `implements`, `with`, আর `on`-এর পার্থক্য কী?

> Very common · Medium — সবচেয়ে সাধারণ Dart OOP প্রশ্ন। · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart-এ প্রতিটা class নিজে থেকেই interface হিসেবে ব্যবহার করা যায়। `extends` হলো code inherit করার জন্য — parent মাত্র একটাই। `implements` শুধু নিয়মগুলো (contract) নেয়, আর সব code আমাকেই লিখতে বাধ্য করে। `with` reusable behavior যোগ করে (একটা mixin)। `on` ঠিক করে দেয় কোন class-এর সাথে একটা mixin ব্যবহার করা যাবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Dart-এ `interface` keyword নেই, কারণ প্রতিটা class নিজেই একটা interface।**
Java-তে আপনি `interface` লেখেন। Dart-এ প্রতিটা class নিজে থেকেই একটা interface তৈরি করে (তার method-এর তালিকা)। তাই আপনি যেকোনো class-কে `implements` করতে পারেন।

**ধাপ ২ — `extends`: parent-এর code inherit করা (parent শুধু একটাই)।**
আপনি parent-এর চলতি code বিনামূল্যে পান। সেটা reuse করতে পারেন, বা override করতে পারেন।

```dart
class Animal {
  void breathe() => print('breathing');
}

class Dog extends Animal {
  void bark() => print('woof');
}

Dog().breathe(); // Animal থেকে বিনামূল্যে inherit করা
```

**ধাপ ৩ — `implements`: শুধু নিয়ম নেওয়া, সব code নিজে লেখা।**
আপনি কোনো code পান না — শুধু প্রতিটা method দেওয়ার বাধ্যবাধকতা পান।

```dart
class Animal {
  void breathe() => print('breathing');
}

class Robot implements Animal {
  // breathe() নিজেকেই লিখতে হবে; কিছুই inherit হয় না
  @override
  void breathe() => print('robot pretends to breathe');
}
```

আপনি একসাথে অনেক class-কে `implements` করতে পারেন (অনেক contract)।

**ধাপ ৪ — `with`: reusable behavior যোগ করা (mixin)।**

```dart
mixin Swimmer {
  void swim() => print('swimming');
}

class Duck extends Animal with Swimmer {} // breathe() আর swim() দুটোই পায়
```

**ধাপ ৫ — `on`: একটা mixin কোথায় ব্যবহার করা যাবে তা সীমিত করা।**

```dart
mixin Validating on Form {
  // শুধু Form ধরনের class-এ যোগ করা যাবে
}
```

**ধাপ ৬ — একটা পরিষ্কার তুলনার টেবিল।**

| Keyword | কী পান | কয়টা | কখন ব্যবহার করবেন |
|---|---|---|---|
| `extends` | parent-এর **code** | শুধু **একটা** | "is-a" + code reuse |
| `implements` | শুধু **নিয়ম** (সব code লিখতে হবে) | অনেক | একটা contract মানা |
| `with` | reusable **behavior** | অনেক | অনেক class-এর মধ্যে behavior ভাগ করা |
| `on` | mixin-এর জন্য একটা **নিয়ম** | — | একটা mixin-কে একটা type-এ সীমিত করা |

মনে রাখার সহজ উপায়:
- **`extends`** = "আমি আমার parent-এর code বিনামূল্যে পাই।"
- **`implements`** = "আমি কথা দিচ্ছি এই নিয়মগুলো মানব, কিন্তু code আমি নিজেই লিখব।"

**Interviewer কেন জিজ্ঞেস করে:** আপনি Dart OOP সত্যিই বোঝেন কি না, এটা তার সবচেয়ে পরিষ্কার পরীক্ষা।

**সাধারণ ভুল:** "Dart-এ interface নেই" বলা। এটা ভুল — প্রতিটা class একই সাথে একটা interface-ও। আরেকটা ভুল হলো `extends` (code inherit) আর `implements` (সব আবার লেখা) গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Testing-এ `implements` কেন ব্যবহার করবেন?"* → আপনি একটা class-এর fake version বানিয়ে আসল code ছাড়াই test করতে পারেন। Mocking-এর জন্য দারুণ।
- *"একটা class কি একটাকে extend আর অনেককে implement করতে পারে?"* → হ্যাঁ: `class A extends B implements C, D {}`।

**সম্পর্কিত:** [Q13 — mixin গভীরভাবে](#q13) · [Q11 — constructor](#q11)

[↑ উপরে ফিরুন](#toc)

---

<a id="q13"></a>
## 13. Mixin কী? `with`, `on` ব্যাখ্যা করুন, আর দুটো mixin-এ একই method থাকলে কী হয়?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Mixin হলো reusable behavior, যা `with` দিয়ে একটা class-এ যোগ করা যায় — inheritance ছাড়াই। অনেকগুলো mixin যোগ করা যায়। দুটো mixin-এ একই method থাকলে শেষেরটা জেতে। `on` keyword একটা mixin-কে সীমিত করে, যাতে সেটা শুধু একটা নির্দিষ্ট type-এ ব্যবহার করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Mixin হলো একটা class-এর "বাড়তি দক্ষতা"।**
Mixin-কে ভাবুন এমন ক্ষমতা হিসেবে, যা আপনি একটা class-এ জুড়ে দেন। একটা `Duck` "Swimmer" দক্ষতা আর "Walker" দক্ষতা পেতে পারে — ওদের থেকে inherit না করেই।

```dart
mixin Swimmer {
  void swim() => print('swimming');
}
mixin Walker {
  void walk() => print('walking');
}

class Duck with Swimmer, Walker {}

Duck()..swim()..walk(); // দুটো দক্ষতাই আছে
```

**ধাপ ২ — দুটো mixin-এ একই method থাকলে কী হয়?**
Dart ওদের বাঁ দিক থেকে ডান দিকে সাজায়, আর শেষেরটা জেতে:

```dart
mixin A { void greet() => print('Hello from A'); }
mixin B { void greet() => print('Hello from B'); }

class C with A, B {}   // B শেষে আছে
C().greet();           // "Hello from B"  (শেষ mixin জেতে)
```

এই সাজানোকে বলে *linearization* — Dart mixin-গুলোকে একটা পরিষ্কার সরল line-এ চ্যাপ্টা করে ফেলে, ফলে কোনো বিভ্রান্তি থাকে না।

**ধাপ ৩ — `on`: একটা mixin-কে নির্দিষ্ট type-এ সীমিত করা।**
`on` বলে — "এই mixin শুধু এই type-এর class-এ যোগ করা যাবে।" এতে mixin নিরাপদে ওই type-এর method ব্যবহার করতে পারে:

```dart
class Animal {
  void breathe() => print('breathing');
}

mixin Pet on Animal {
  void play() {
    breathe();        // নিরাপদ — আমরা জানি host একটা Animal
    print('playing');
  }
}

class Cat extends Animal with Pet {} // Cat একটা Animal, তাই Pet allowed
```

**ধাপ ৪ — Mixin-এ constructor থাকতে পারে না কেন।**
Mixin মূল class-এর সাথে মিশে যায়, আর সেই class আগে থেকেই object তৈরির কাজ সামলায়। তাই mixin-এর নিজের আলাদা কোনো object নেই যেটা construct করতে হবে — এই কারণেই এতে constructor থাকতে পারে না।

**Interviewer কেন জিজ্ঞেস করে:** আপনি mixin-এর order (শেষেরটা জেতে) আর `on`-এর উদ্দেশ্য বোঝেন কি না, তা যাচাই করতে।

**সাধারণ ভুল:** Mixin-কে "multiple inheritance" বলা। এটা বিভ্রান্তিকর diamond সমস্যা নয় — Dart ওদের order অনুযায়ী সাজায় আর শেষেরটা জেতে। পরিষ্কার আর অনুমানযোগ্য।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Mixin vs interface (`implements`)?"* → Mixin আপনাকে চলতি code দেয়। `implements` শুধু নিয়ম দেয়, code আপনি লেখেন।
- *"`with` vs `extends`?"* → `extends` = একটা parent-এর code। `with` = অনেক reusable behavior যোগ করা।

**সম্পর্কিত:** [Q12 — extends/implements/with/on](#q12)

[↑ উপরে ফিরুন](#toc)

---

<a id="q14"></a>
## 14. Extension method কী? এটা কী কী করতে পারে না?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Extension দিয়ে আমি এমন type-এ method যোগ করতে পারি যেটা আমার নয় — যেমন `String` বা `int` — সেটাকে বদলানো বা wrap করা ছাড়াই। প্রধান সীমা দুটো: এগুলো variable-এর লেখা type দেখে বাছাই হয় (আসল type দেখে নয়), আর এগুলো নতুন field যোগ করতে পারে না (কোনো state নেই)।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — পুরোনো একটা tool-এ নতুন একটা "button" যোগ করা।**
Extension হলো এমন একটা type-এ নতুন helper method যোগ করার মতো, যেটা আপনি edit করতে পারেন না:

```dart
extension StringHelpers on String {
  bool get isValidEmail => contains('@') && contains('.');
  String capitalize() =>
      isEmpty ? this : '${this[0].toUpperCase()}${substring(1)}';
}

'a@b.com'.isValidEmail; // true
'hello'.capitalize();   // 'Hello'
```

এখন মনে হবে `String`-এ এই method-গুলো সবসময়ই ছিল। খুব পরিষ্কার।

**ধাপ ২ — বাস্তব Flutter উদাহরণ (খুব সাধারণ)।**

```dart
extension ContextX on BuildContext {
  double get width => MediaQuery.of(this).size.width;
  ThemeData get theme => Theme.of(this);
}

// একটা widget-এর ভেতরে ব্যবহার:
final w = context.width;     // MediaQuery.of(context).size.width-এর বদলে
final t = context.theme;     // Theme.of(context)-এর বদলে
```

**ধাপ ৩ — সীমা ১: নতুন field নেই (কোনো জমা করা data নেই)।**
Extension method আর getter যোগ করতে পারে, কিন্তু instance variable নয়। এগুলো behavior যোগ করে, state নয়।

**ধাপ ৪ — সীমা ২: লেখা type দেখে বাছাই হয়, আসল type দেখে নয়।**
এই অংশটাই কঠিন। Extension compile time-এ declared type দেখে বেছে নেওয়া হয়:

```dart
String text = 'hi';
text.capitalize();   // কাজ করে — declared type হলো String

Object thing = 'hi';
// thing.capitalize(); // error — declared type হলো Object, String নয়
```

তাই extension override করা method-এর মতো নয় (ওগুলো আসল runtime type ব্যবহার করে)।

**Interviewer কেন জিজ্ঞেস করে:** আপনি জানেন কি না যে extension লেখা type দেখে resolve হয়, আর এগুলো state ধরে রাখতে পারে না।

**সাধারণ ভুল:** Extension polymorphic আচরণ করবে (আসল type অনুযায়ী) — এমন আশা করা। এটা declared type দেখে বাছাই হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"দুটো extension কি একই method define করতে পারে?"* → হ্যাঁ, কিন্তু তখন সেটা অস্পষ্ট হয়ে যায়; আপনাকে একটাকে স্পষ্ট করে call করতে হবে: `StringHelpers('hi').capitalize()`।

**সম্পর্কিত:** [Q12 — OOP keyword](#q12)

[↑ উপরে ফিরুন](#toc)

---

<a id="q15"></a>
## 15. Enhanced enum কী? একটা enum-এ কি field আর method থাকতে পারে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"হ্যাঁ। Dart 2.17 থেকে enum-এ field, const constructor আর method রাখা যায়। তাই enum-এর সাথে আলাদা helper না বানিয়ে, আমি data আর behavior দুটোই enum-এর ভেতরেই রাখি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সাধারণ enum মানে নির্দিষ্ট কিছু option-এর তালিকা।**

```dart
enum Status { active, paused, cancelled }
```

**ধাপ ২ — পুরোনো, কষ্টের উপায় (2.17-এর আগে)।**
প্রতিটা value-তে data যোগ করতে মানুষ `switch` helper ব্যবহার করত — এলোমেলো, আর case ভুলে যাওয়া সহজ:

```dart
int priceOf(Plan p) {
  switch (p) {
    case Plan.free: return 0;
    case Plan.pro: return 12;
    // একটা case ভুলে গেলেই bug
  }
}
```

**ধাপ ৩ — আধুনিক উপায়: data আর method enum-এর ভেতরেই রাখুন।**

```dart
enum Plan {
  free(price: 0, maxProjects: 1),
  pro(price: 12, maxProjects: 50),
  team(price: 40, maxProjects: 1000);

  // const constructor + final field
  const Plan({required this.price, required this.maxProjects});
  final int price;
  final int maxProjects;

  // enum-এর উপর method আর getter
  bool get isPaid => price > 0;
}

Plan.pro.price;     // 12
Plan.pro.isPaid;    // true
```

**ধাপ ৪ — enum-এর কাজের built-in সুবিধা।**

```dart
Plan.values;                 // [Plan.free, Plan.pro, Plan.team]
Plan.pro.index;              // 1
Plan.pro.name;               // 'pro'
Plan.values.byName('free');  // Plan.free  (text দিয়ে খুঁজে বের করা)
```

**Interviewer কেন জিজ্ঞেস করে:** দেখতে চান আপনি পুরোনো enum + switch helper-এর বদলে আধুনিক Dart লেখেন কি না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"enum vs sealed class?"* → enum = নির্দিষ্ট কিছু single value-র তালিকা, সবার গঠন একই। sealed class = নির্দিষ্ট কিছু type-এর তালিকা, প্রতিটা আলাদা data রাখতে পারে (দেখুন [Q18](#q18))।

**সম্পর্কিত:** [Q18 — sealed class](#q18)

[↑ উপরে ফিরুন](#toc)

---

# D. Dart 3-এর নতুন feature (record, pattern, sealed class)

> এই তিনটা feature দেখায় আপনি **আজকের** Dart লেখেন, কয়েক বছর আগের Dart নয়। এর মধ্যে অন্তত একটা প্রশ্ন আসবেই।

---

<a id="q16"></a>
## 16. Dart 3-এ record কী?

> Very common (Dart 3) · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Record হলো class না বানিয়েই কয়েকটা value একসাথে রাখার দ্রুত উপায়। এটা immutable (বদলানো যায় না), আর একই value-র দুটো record সমান হয়। সবচেয়ে সাধারণ ব্যবহার — একটা function থেকে একের বেশি value return করা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Record আসার আগের সমস্যা।**
দুটো value return করতে হলে হয় পুরো একটা class বানাতে হতো (অনেক কাজ), নয়তো `List`/`Map` return করতে হতো (কোনো safety নেই):

```dart
// পুরোনো, অনিরাপদ উপায়:
List getResponse() => [200, 'OK'];
final r = getResponse();
final code = r[0]; // কোন index-এ কী? গুলিয়ে ফেলা সহজ
```

**ধাপ ২ — Record = কয়েকটা value-র ছোট ব্যাগ।**
Record-কে ভাবুন একটা ছোট ব্যাগ, যেটা কয়েকটা জিনিস একসাথে বয়ে নেয়। কোনো class লাগে না।

```dart
// দুটো value পরিষ্কারভাবে return করা:
(int, String) getResponse() => (200, 'OK');

final result = getResponse();
print(result.$1); // 200  (position দিয়ে access: $1, $2, ...)
print(result.$2); // OK
```

**ধাপ ৩ — এক line-এ unpack (destructure) করা।**

```dart
final (code, body) = getResponse();
print('$code $body'); // 200 OK
```

**ধাপ ৪ — Named field ($1, $2-এর চেয়ে পরিষ্কার)।**

```dart
({double lat, double lng}) getLocation() => (lat: 23.8, lng: 90.4);

final loc = getLocation();
print(loc.lat); // 23.8
print(loc.lng); // 90.4
```

**ধাপ ৫ — Record value দিয়ে তুলনা করে (built-in equality)।**

```dart
print((1, 'a') == (1, 'a')); // true, একই value মানে সমান
```

কখন ব্যবহার করবেন: দ্রুত, সাময়িকভাবে কয়েকটা value একসাথে রাখতে record ব্যবহার করুন। Data-র একটা স্পষ্ট নাম থাকলে আর method দরকার হলে আসল class বানান।

**Interviewer কেন জিজ্ঞেস করে:** দেখতে চান আপনি `Tuple2` package বা `Map` return করার মতো পুরোনো কৌশলের বদলে record ব্যবহার করেন কি না।

**সাধারণ ভুল:** সব জায়গায় record-কেই মূল data model বানিয়ে ফেলা। Data-র আসল মানে তৈরি হলে (যেমন `User`), ঠিকমতো একটা class বানান।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Record-এর value কি বদলানো যায়?"* → না, record immutable।
- *"Record vs class?"* → Record = দ্রুত, নাম নেই, method নেই। Class = নাম আছে, method রাখা যায়, আসল model-এর জন্য ভালো।

**সম্পর্কিত:** [Q4 — value equality](#q4) · [Q17 — destructuring pattern](#q17)

[↑ উপরে ফিরুন](#toc)

---

<a id="q17"></a>
## 17. Pattern matching, destructuring আর switch expression কী?

> Very common (Dart 3) · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Pattern দিয়ে আমি data-র গঠন check করতে পারি, আর একই সাথে ভেতরের value বের করে আনতে পারি। switch *expression* একটা value return করে, যেটা লম্বা switch দিয়ে variable বসানোর চেয়ে অনেক পরিষ্কার। আর `if-case` দিয়ে এক line-এই গঠন check করে unpack করা যায় — JSON নিরাপদে পড়ার জন্য দারুণ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Destructuring: এক ধাপেই value বের করে আনা।**

```dart
final (a, b) = (1, 2);            // a = 1, b = 2
final [first, second] = [10, 20]; // first = 10, second = 20
final {'name': name} = {'name': 'Sara'}; // name = 'Sara'
```

**ধাপ ২ — switch expression: যে switch একটা value RETURN করে।**
পুরোনো switch *statement* (variable বসায়):

```dart
String label;
switch (status) {
  case Status.active: label = 'Active'; break;
  case Status.paused: label = 'Paused'; break;
  default: label = 'Unknown';
}
```

নতুন switch *expression* (সরাসরি value return করে, বেশি পরিষ্কার):

```dart
final label = switch (status) {
  Status.active => 'Active',
  Status.paused => 'Paused',
  _ => 'Unknown',          // _ মানে "বাকি যা কিছু"
};
```

**ধাপ ৩ — switch-এর ভেতরে pattern (গঠন মেলানো + unpack)।**

```dart
String describe(Object o) => switch (o) {
  (int x, int y) => 'point $x, $y',          // record-এর সাথে মেলে
  [final first, ...] => 'list starts with $first', // list-এর সাথে মেলে
  int n when n > 0 => 'positive number',     // 'when' একটা শর্ত যোগ করে
  String s => 'text: $s',                     // String-এর সাথে মেলে + bind করে
  _ => 'something else',
};
```

**ধাপ ৪ — `if-case`: এক line-এ গঠন check করে unpack করা।**
JSON নিরাপদে পড়ার জন্য এটা চমৎকার:

```dart
final json = {'token': 'abc123'};

if (json case {'token': final String token}) {
  saveToken(token); // token ব্যবহারের জন্য তৈরি এবং নিশ্চিতভাবে String
}
```

গঠন না মিললে (`token` নেই, বা সেটা String নয়), `if` শুধু বাদ পড়ে যায় — কোনো crash নেই।

**Interviewer কেন জিজ্ঞেস করে:** পুরোনো লম্বা `if (x is Type) { final t = x as Type; ... }` code-এর বদলে পরিষ্কার pattern matching লেখা হচ্ছে কি না, সেটা দেখতে।

**সাধারণ ভুল:** switch *statement* (একটা কাজ করে) আর switch *expression* (একটা value return করে) — এই দুটোর পার্থক্য না জানা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`User(:final id)` মানে কী?"* → এটা একটা `User` object-এর সাথে মেলে, আর তার `id` field-টা `id` নামের variable-এ বের করে আনে।
- *"`when` কী?"* → Pattern-এর সাথে যোগ করা একটা অতিরিক্ত শর্ত, যেমন `int n when n > 0`।

**সম্পর্কিত:** [Q16 — record](#q16) · [Q18 — sealed + exhaustive switch](#q18)

[↑ উপরে ফিরুন](#toc)

---

<a id="q18"></a>
## 18. Sealed class কী? আর নতুন class modifier গুলো (`sealed`, `final`, `base`, `interface`) কী?

> Common (Dart 3) · Hard · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা `sealed` class-এর subclass গুলো নির্দিষ্ট আর জানা, সবগুলোই একই file-এ। বড় সুবিধা: আমি যখন এটার উপর `switch` করি, Dart check করে আমি প্রতিটা case handle করেছি কি না। পরে নতুন subclass যোগ করে handle করতে ভুলে গেলে code compile-ই হবে না। বাকি modifier গুলো — `final`, `base`, `interface` — ঠিক করে দেয় একটা class অন্য file-এ কীভাবে reuse করা যাবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `sealed` হলো একটা নির্দিষ্ট menu-র মতো।**
Sealed class বলে — "শুধু এই option গুলোই আছে।" App state-এর জন্য এটা একদম উপযুক্ত, যেমন *loading / success / error*:

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

**ধাপ ২ — বড় সুবিধা: Dart আপনাকে প্রতিটা case handle করতে বাধ্য করে।**

```dart
String show(Result r) => switch (r) {
  Loading() => 'Loading...',
  Success(:final data) => 'Got: $data',
  Failure(:final error) => 'Error: $error',
  // "default" লাগে না — Dart জানে এগুলোই সব option।
};
```

পরে `class Empty extends Result {}` যোগ করে handle করতে ভুলে গেলে code compile হবে না। Dart ঠিক missing case-টা দেখিয়ে দেয়। এতে একটা পুরো ধরনের bug বন্ধ হয়ে যায়।

**ধাপ ৩ — এটা পুরোনো পদ্ধতির চেয়ে কেন ভালো।**
পুরোনো পদ্ধতি: একটা class-এ তিনটা nullable field আর একটা `type` flag — এতে invalid state সহজেই তৈরি হয় (data আর error একসাথে?)। Sealed class invalid state-কে অসম্ভব করে দেয়। আর নিশ্চিত করে প্রতিটা state handle হয়েছে।

**ধাপ ৪ — বাকি class modifier গুলো (অন্য file-এ reuse নিয়ন্ত্রণ করে)।**

| Modifier | `extend` করা যায়? | `implement` করা যায়? | মানে |
|---|:---:|:---:|---|
| (কোনোটা নয়) | হ্যাঁ | হ্যাঁ | সাধারণ class |
| `final` | না | না | পুরো বন্ধ, extend বা implement কিছুই নয় |
| `base` | হ্যাঁ | না | extend করা যাবে, কিন্তু আবার implement করা যাবে না |
| `interface` | না | হ্যাঁ | শুধু একটা contract, implement করুন, extend করবেন না |
| `sealed` | না | না | subclass নির্দিষ্ট, নিরাপদ ও সম্পূর্ণ `switch` |

(খেয়াল রাখুন: এখানে `final` হলো *class modifier*, যা variable-এর `final` keyword থেকে আলাদা।)

**Interviewer কেন জিজ্ঞেস করে:** দেখতে চান আপনি bug ঠেকাতে type system ব্যবহার করেন কি না — যেমন প্রতিটা app state handle হয়েছে তা নিশ্চিত করা।

**সাধারণ ভুল:** এটা না জানা যে "প্রতিটা case handle" সুবিধাটা শুধু `sealed`-এর জন্যই আসে। সাধারণ class এই check দেয় না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"sealed class vs freezed union?"* → দুটোই নির্দিষ্ট state model করে। `sealed` ভাষার ভেতরেই আছে। আর code generation ছাড়াই compile-time-এ "সব case handle" free-তে দেয়।
- *"`interface` modifier কেন?"* → এটা স্পষ্ট করে বলে "আমাকে implement করো, extend কোরো না"। আর Dart সব file জুড়ে এটা মানতে বাধ্য করে।

**সম্পর্কিত:** [Q15 — enum vs sealed](#q15) · [Q17 — switch patterns](#q17)

[↑ উপরে ফিরুন](#toc)

---

# E. Async ও concurrency (Future, Stream, Isolate)

---

<a id="q19"></a>
## 19. `Future` কী? `async`/`await` কীভাবে কাজ করে? `await` কি app জমিয়ে দেয়?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`Future` হলো এমন একটা value যা পরে তৈরি হবে — অর্ডার করা খাবারের রসিদের মতো। `async`/`await` আমাকে এটা সহজ উপর-থেকে-নিচে ধরনে লিখতে দেয়। খুব গুরুত্বপূর্ণ কথা: `await` app জমিয়ে দেয় না। এটা শুধু ওই একটা function থামায়। বাকি app চলতেই থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — রেস্টুরেন্টের উদাহরণ।**
ভাবুন আপনি রেস্টুরেন্টে খাবার অর্ডার করছেন:
- আপনি অর্ডার করলেন আর এখনই একটা রসিদ পেলেন → এটাই `Future`।
- খাবার আসে পরে → এটাই value।
- আপনি অপেক্ষা করার সময় রান্নাঘর অন্য customer-দের খাবার দিতে থাকে → এটাই app-এর responsive থাকা।

`await` শুধু আপনার অর্ডারের জন্য অপেক্ষা করে — পুরো রেস্টুরেন্ট থামায় না।

**ধাপ ২ — async/await ছাড়া আর async/await সহ।**

```dart
// Future মানে "পরে আসবে এমন একটা value"
Future<String> fetchName() async {
  await Future.delayed(const Duration(seconds: 2)); // network ধরে নিন
  return 'Sara';
}

void main() async {
  print('start');
  final name = await fetchName(); // শুধু এই function 2s থামে
  print('Hello $name');           // value আসার পরে চলে
  print('end');
}
// Output: start, তারপর 2s পরে, Hello Sara, তারপর end
```

ওই 2 সেকেন্ডে app জমে থাকে না — button কাজ করে, animation চলে। শুধু এই function-টা থেমে থাকে।

**ধাপ ৩ — সবচেয়ে গুরুত্বপূর্ণ কথা: `await` blocking নয়।**
`await` মানে "এখানে থামো, আর value তৈরি না হওয়া পর্যন্ত app-কে অন্য কাজ করতে দাও।" এটা screen থামায় না। (থামালে প্রতিটা network call-এ প্রতিটা app জমে যেত।)

**ধাপ ৪ — কাজগুলো একসাথে চালানো (senior level-এর একটা detail)।**
দুটো কাজ একে অন্যের উপর নির্ভর না করলে, একটার পর একটা `await` করবেন না — এটা ধীর। `Future.wait` দিয়ে একসাথে চালান:

```dart
// ধীর: 2s + 2s = মোট 4s
final a = await fetchA();
final b = await fetchB();

// দ্রুত: দুটোই একসাথে চলে = মোট প্রায় 2s
final results = await Future.wait([fetchA(), fetchB()]);
```

কিন্তু B-এর জন্য যদি A-এর result লাগে, তাহলে একটার পর একটা `await` করাই সঠিক।

**Interviewer কেন জিজ্ঞেস করে:** async নিয়ে এক নম্বর ভুল হলো `await` পুরো app জমিয়ে দেয় ভাবা। তাঁরা শুনতে চান: এটা শুধু ওই function থামায়, app চলতেই থাকে।

**সাধারণ ভুল:** একে অন্যের উপর নির্ভর না করা call গুলো একটার পর একটা await করা (ধীর)। একসাথে চালাতে `Future.wait` ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`Future.wait` vs `Future.any`?"* → `wait` শেষ হয় যখন সবগুলো শেষ হয়। `any` শেষ হয় যখন প্রথমটা শেষ হয়।
- *"await-এর সাথে error কীভাবে handle করেন?"* → `await`-টা `try/catch`-এ মুড়ে দিন, তাহলে Future-এর error ধরা পড়বে।

**সম্পর্কিত:** [Q20 — event loop](#q20) · [Q21 — Streams](#q21) · [Q6 — error handling](#q6)

[↑ উপরে ফিরুন](#toc)

---

<a id="q20"></a>
## 20. Event loop ব্যাখ্যা করুন: microtask queue vs event queue।

> Deeper question · Hard — senior-দের জন্য একটা tie-breaker · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q20)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart একটাই event loop-এ চলে, যেখানে দুটো লাইন আছে: microtask লাইন (উচ্চ priority) আর event লাইন (সাধারণ)। পরের event নেওয়ার আগে Dart সব microtask শেষ করে। Future আর `await`-এর পরের code microtask লাইন ব্যবহার করে। আর timer, tap আর network result event লাইন ব্যবহার করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুই লাইনের ব্যাংক।**
ভাবুন একটা ব্যাংকে দুটো লাইন আছে:
- **Microtask লাইন = VIP লাইন।** সবসময় আগে পুরোপুরি সেবা পায়।
- **Event লাইন = সাধারণ লাইন।** VIP লাইন খালি হওয়ার পরেই সেবা পায়।

Dart ঠিক এভাবেই কাজ করে: event (সাধারণ) লাইন থেকে একটা জিনিস নেওয়ার আগেও পুরো microtask (VIP) লাইন খালি করে ফেলে।

**ধাপ ২ — কে কোন লাইনে যায়?**
- **Microtask (VIP):** `Future.microtask(...)`, `scheduleMicrotask(...)`, আর `await` শেষ হওয়ার পরে যে code চলে।
- **Event (সাধারণ):** `Future(...)`, `Timer`, user-এর tap, network response, file read।

**ধাপ ৩ — output অনুমান করুন (ঠিক এই প্রশ্নটা খুব সাধারণ)।**

```dart
void main() {
  print('1');                          // এখনই চলে (synchronous)
  Future(() => print('2'));            // সাধারণ লাইন (event)
  Future.microtask(() => print('3'));  // VIP লাইন (microtask)
  print('4');                          // এখনই চলে (synchronous)
}
```

Output-এর order:
1. `1` আর `4` — সাধারণ synchronous code আগে চলে, উপর থেকে নিচে।
2. `3` — এরপর VIP (microtask) লাইন খালি হয়।
3. `2` — শেষে সাধারণ (event) লাইন।

তাই output হলো: **`1, 4, 3, 2`।**

**ধাপ ৪ — বাস্তব app-এ এটা কেন গুরুত্বপূর্ণ।**
আপনি যদি loop-এ একের পর এক microtask যোগ করতে থাকেন, VIP লাইন কখনোই খালি হয় না। তখন সাধারণ লাইন (যেখানে rendering আর tap থাকে) সেবা পায় না — app জমে যায়। তাই microtask queue ভাসিয়ে দেবেন না।

**Interviewer কেন জিজ্ঞেস করে:** আপনি যদি ঠিকভাবে `1, 4, 3, 2` অনুমান করতে পারেন, তাহলে আপনি Dart-এর async model সত্যিই বোঝেন। এটা senior level-এর একটা শক্ত signal।

**সাধারণ ভুল:** ভাবা যে timer বা Future microtask-এর আগে চলে। Microtask (VIP) সবসময় আগে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`await`-এর পরের code কোথায় চলতে থাকে?"* → microtask (VIP) লাইনে, তাই এটা পরের সাধারণ event-এর আগে চলে।
- *"কী কী UI জমিয়ে দিতে পারে?"* → লম্বা synchronous কাজ, বা microtask queue ভাসিয়ে দেওয়া। দুটোই rendering আটকে দেয়।

**সম্পর্কিত:** [Q19 — async/await](#q19) · [Q23 — single-threaded ও isolate](#q23)

[↑ উপরে ফিরুন](#toc)

---

<a id="q21"></a>
## 21. `Stream` কী? single-subscription vs broadcast, `StreamController`, আর `StreamBuilder` ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q21)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`Future` একটা value দেয়; `Stream` সময়ের সাথে অনেক value দেয়। Single-subscription stream-এ শুধু একজন listener থাকতে পারে (এটাই default)। Broadcast stream-এ অনেক listener থাকতে পারে। `StreamController` একটা stream তৈরি করে আর তাতে value দেয়। আর নতুন value এলেই `StreamBuilder` widget-টা rebuild করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Future vs Stream।**
- **Future = একবার delivery।** (একটা pizza আসে, একবারই।)
- **Stream = একটা subscription।** (একটা YouTube channel সময়ের সাথে নতুন video দিতে থাকে।)

```dart
Future<int> oneValue() async => 42;        // একটা value
Stream<int> manyValues() async* {          // অনেক value
  yield 1;
  yield 2;
  yield 3;
}
```

**ধাপ ২ — Single-subscription vs broadcast।**
- **Single-subscription (default):** শুধু একজন listener allowed। দুইবার listen করার চেষ্টা করলে error দেয়। একবারের data flow-এর জন্য ভালো (যেমন একটা file পড়া)।
- **Broadcast:** অনেক listener allowed। কিন্তু নতুন listener পুরোনো value দেখে না — শুধু যোগ দেওয়ার পরের value গুলো পায়।

```dart
// Single-subscription:
final controller = StreamController<int>();
controller.stream.listen((v) => print('A: $v')); // একজন listener
// controller.stream.listen(...);                  // দ্বিতীয়বার listen করলে error

// Broadcast:
final bus = StreamController<int>.broadcast();
bus.stream.listen((v) => print('A: $v'));
bus.stream.listen((v) => print('B: $v')); // অনেক listener allowed
```

**ধাপ ৩ — StreamController = stream-এর "feed" দিক।**
এটা আপনাকে listen করার জন্য একটা `stream` দেয়। আর আপনি `add(...)` দিয়ে value পাঠান। কাজ শেষে সবসময় `close()` করুন।

```dart
final controller = StreamController<int>();
controller.stream.listen((v) => print(v));
controller.add(1);  // listener 1 print করে
controller.add(2);  // listener 2 print করে
controller.close(); // resource ছাড়তে সবসময় close করুন
```

**ধাপ ৪ — StreamBuilder = প্রতিটা value-তে widget নিজে থেকেই rebuild।**

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

**ধাপ ৫ — stream-এর এক নম্বর bug: পরিষ্কার না করা।**
প্রতিটা subscription cancel করতে হবে, আর প্রতিটা controller close করতে হবে, সাধারণত `dispose()`-এ। এটা ভুলে যাওয়া খুব সাধারণ একটা memory leak:

```dart
late final StreamSubscription _sub;

@override
void initState() {
  super.initState();
  _sub = myStream.listen(_onData);
}

@override
void dispose() {
  _sub.cancel();    // listen করা বন্ধ
  super.dispose();
}
```

**Interviewer কেন জিজ্ঞেস করে:** দেখতে চান আপনি single vs broadcast জানেন কি না, আর ঠিকভাবে পরিষ্কার করেন কি না।

**সাধারণ ভুল:** subscription cancel বা controller close করতে ভুলে যাওয়া, ফলে memory leak হয়। আরেকটা ভুল — শুধু `stream`-এর বদলে পুরো `StreamController` বাইরে খুলে দেওয়া (এতে অন্যরা এটা নিয়ে গোলমাল করতে পারে)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"broadcast কি নতুন listener-দের পুরোনো value আবার দেয়?"* → না। নতুন listener শুধু listen শুরু করার পরের value গুলো পায়। (শেষ value আবার দরকার হলে RxDart-এর `BehaviorSubject` ব্যবহার করুন।)
- *"FutureBuilder vs StreamBuilder?"* → FutureBuilder = একটা value। StreamBuilder = সময়ের সাথে অনেক value।

**সম্পর্কিত:** [Q19 — Future vs Stream](#q19) · [Q22 — generator stream তৈরি করে](#q22)

[↑ উপরে ফিরুন](#toc)

---

<a id="q22"></a>
## 22. Generator কী — `sync*`/`yield` আর `async*`/`yield*`?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q22)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Generator একটা value-এর sequence বানায় lazily, একবারে একটা করে। `sync*` একটা `Iterable` বানায় আর চাইলে তবেই value দেয়। `async*` একটা `Stream` বানায় আর দুই value-এর মাঝে `await` করতে পারে। `yield` একটা value দেয়; `yield*` অন্য একটা sequence-এর সব value দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `sync*` একটা lazy `Iterable` বানায়।**
"Lazy" মানে আপনি প্রতিটা value না চাওয়া পর্যন্ত কিছুই চলে না। এতে memory বাঁচে:

```dart
Iterable<int> firstNumbers(int n) sync* {
  for (var i = 0; i < n; i++) {
    print('making $i');
    yield i;            // একটা value দেয়, তারপর আবার চাওয়ার আগ পর্যন্ত থামে
  }
}

final nums = firstNumbers(3); // এখনো কিছুই print হয়নি!
print('created');             // "created" আগে print হয়
for (final n in nums) {       // এখন চলে, একবারে একটা করে
  print('got $n');
}
```

**ধাপ ২ — `async*` একটা `Stream` বানায় (সময়ের সাথে আসা value)।**
এটা দুই value-এর মাঝে `await` করতে পারে — timer বা live update-এর জন্য একদম ঠিক:

```dart
Stream<int> ticks(int n) async* {
  for (var i = 0; i < n; i++) {
    await Future.delayed(const Duration(seconds: 1));
    yield i;            // প্রতি সেকেন্ডে একটা করে value দেয়
  }
}
```

**ধাপ ৩ — `yield` বনাম `yield*`।**
- `yield value` → একটা value দেয়।
- `yield* anotherSequence` → অন্য একটা iterable বা stream-এর সব value দেয় (সেটাকে ভেতরে মিলিয়ে দেয়):

```dart
Iterable<int> combined() sync* {
  yield 0;
  yield* firstNumbers(3); // অন্য generator থেকে 0, 1, 2 দেয়
  yield 99;
}
// ফলাফল: 0, 0, 1, 2, 99
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি laziness বোঝেন কি না (`sync*` ব্যবহার না করা পর্যন্ত কিছুই করে না)। আর `Iterable` ও `Stream`-এর পার্থক্য জানেন কি না।

**সাধারণ ভুল:** দুটোকে গুলিয়ে ফেলা। মনে রাখুন: `sync*` → `Iterable` (চাইলে তবেই টেনে আনে)। `async*` → `Stream` (সময়ের সাথে push হয়)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`sync*` কেন কাজে লাগে?"* → বড় বা এমনকি অসীম sequence-এর জন্য — আপনি যতটুকু আসলে ব্যবহার করেন ততটুকুই হিসাব হয়, তাই memory বাঁচে।

**সম্পর্কিত:** [Q21 — async* stream বানায়](#q21)

[↑ উপরে ফিরুন](#toc)

---

<a id="q23"></a>
## 23. Dart কেন single-threaded? Isolate কী, আর `compute()` / `Isolate.run` কী?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q23)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart আপনার code একটা thread-এ চালায়, তাই কোনো lock নেই আর কোনো race condition নেই — সহজ আর নিরাপদ। খারাপ দিক: ভারী কাজ screen জমিয়ে দেয়। Isolate হলো আলাদা একটা worker, যার নিজের memory আছে। Isolate-রা memory share করে না; তারা message পাঠায়। `compute()` আর `Isolate.run` হলো সহজ shortcut, যা ভারী কাজ অন্য isolate-এ চালায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Single-threaded = এক টেবিলে একজন worker।**
Dart একটা thread-এ একবারে একটা কাজ করে। ভালো খবর: দুই টুকরো code একসাথে একই data ছোঁয় না। তাই কোনো race condition নেই আর lock-এরও দরকার নেই। সহজ আর নিরাপদ।

**ধাপ ২ — সমস্যা: ভারী কাজ screen জমিয়ে দেয়।**
যেহেতু worker মাত্র একজন, একটা ধীর CPU কাজ সবকিছু আটকে দেয় — screen আঁকাও থেমে যায়। App জমে যায় (jank হয়):

```dart
// এই ভারী loop চলার সময় UI জমে যায়
int slowSum() {
  var total = 0;
  for (var i = 0; i < 1000000000; i++) total += i;
  return total;
}
```

(খেয়াল রাখুন: network call কিন্তু app জমায় না — সেটা I/O, যা আগে থেকেই non-blocking। শুধু ভারী CPU কাজ জমিয়ে দেয়।)

**ধাপ ৩ — Isolate = আলাদা টেবিলে দ্বিতীয় একজন worker রাখা।**
Isolate হলো আলাদা একটা worker, যার নিজের memory আছে। তারা কাগজ (memory) share করতে পারে না — তারা একে অন্যকে চিরকুট (message) পাঠায়। এই কারণেই কোনো lock নেই: কিছুই share হয় না।

**ধাপ ৪ — Isolate ব্যবহারের সহজ উপায়গুলো।**

```dart
// সবচেয়ে সহজ, আধুনিক উপায় (Dart 2.19+):
final result = await Isolate.run(() => slowSum()); // অন্য worker-এ চলে

// Flutter-এর পুরোনো shortcut (top-level বা static function লাগে):
final parsed = await compute(parseBigJson, rawText);
```

Isolate যখন ভারী কাজটা করে, UI thread তখন খালি থাকে। তাই screen মসৃণ থাকে।

**ধাপ ৫ — দাম: data copy হয়।**
Memory share হয় না বলে input আর result isolate-এর মাঝে copy হয়। এই copy-র একটা খরচ আছে। তাই isolate শুধু বড় কাজের জন্য ব্যবহার করুন, ছোট কাজের জন্য নয়।

সাধারণ নিয়ম: যে CPU-ভারী কাজ প্রায় 16ms-এর বেশি সময় নেয়, তার জন্য isolate ব্যবহার করুন — বড় JSON parsing, image processing, encryption। Network call-এর জন্য ব্যবহার করবেন না (সেটা আগে থেকেই non-blocking)। খুব ছোট কাজের জন্যও নয় (copy-র খরচ পোষায় না)।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি "no shared memory" model বোঝেন কি না। আর isolate কখন আসলেই দরকার, সেটা জানেন কি না।

**সাধারণ ভুল:** বলা যে "network call দ্রুত করতে isolate ব্যবহার করব।" Network I/O আগে থেকেই non-blocking — isolate কোনো সাহায্য করবে না, শুধু copy-র খরচ বাড়াবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Isolate-রা একে অন্যের সাথে কীভাবে কথা বলে?"* → `SendPort` আর `ReceivePort` দিয়ে (message পাঠিয়ে)। `compute`/`Isolate.run` সহজ ক্ষেত্রে এটা আড়ালে রাখে।
- *"Dart-এ lock নেই কেন?"* → কারণ isolate-দের মাঝে কিছুই share হয় না — প্রত্যেকের নিজের memory আছে।

**সম্পর্কিত:** [Q20 — event loop / single-threaded](#q20) · [Q19 — async/await](#q19)

[↑ উপরে ফিরুন](#toc)

---

# F. Dart কীভাবে চলে (compile ও memory)

---

<a id="q24"></a>
## 24. JIT আর AOT কী? Flutter-এর জন্য এটা কেন গুরুত্বপূর্ণ?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q24)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Development-এর সময় Dart JIT ব্যবহার করে (চলার সময়ে compile করে), আর এটাই hot reload-কে এত দ্রুত করে। Release build-এ Dart AOT ব্যবহার করে (চলার আগেই native code-এ compile করা), তাই app দ্রুত চালু হয় আর মসৃণ চলে। এই কারণেই আমরা কখনো debug build দেখে performance বিচার করি না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — শব্দ দুটোর মানে কী।**
- **JIT = Just-In-Time:** app চলার সময়েই code compile হয়। নমনীয় আর দ্রুত বদলানো যায়, যা hot reload সম্ভব করে।
- **AOT = Ahead-Of-Time:** app চলার আগেই code native machine code-এ compile হয়। Runtime-এ কোনো compile নেই, তাই startup দ্রুত হয় আর performance মসৃণ থাকে।

**ধাপ ২ — Flutter-এ কোনটা কখন ব্যবহার হয়।**

| | JIT (debug mode) | AOT (release mode) |
|---|---|---|
| কখন | development | production (আসল user) |
| কীসের জন্য ভালো | hot reload, দ্রুত code লেখা | দ্রুত startup, আসল performance |
| গতি | ধীর (বাড়তি check) | দ্রুত (native code) |

**ধাপ ৩ — বাস্তবে এটা কেন গুরুত্বপূর্ণ।**
Debug mode-এ app ধীর চলে, কারণ JIT আর বাড়তি debug check থাকে। তাই debug-এ app ধীর লাগলে ঘাবড়াবেন না — performance বিচার করার আগে release mode-এ test করুন (`flutter run --release`)। অনেক "performance bug" release-এ একেবারে মিলিয়ে যায়।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি জানেন কি না যে debug mode-এ কখনোই performance মাপা যাবে না।

**সাধারণ ভুল:** Debug build-এ lag নিয়ে অভিযোগ করা আর সেটাকে "optimize" করার চেষ্টা করা। গতি সবসময় আগে release mode-এ test করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter web-এর ক্ষেত্রে কী হয়?"* → Web-এর জন্য Dart JavaScript-এ compile হয় (বা নতুন WebAssembly-তে), native ARM code-এ নয়।
- *"Profile mode কী?"* → এটা মাঝামাঝি একটা mode: release-এর মতো performance, কিন্তু কিছু profiling tool চালু থাকে, আসল performance মাপার জন্য।

**সম্পর্কিত:** [Q25 — Dart VM](#q25)

[↑ উপরে ফিরুন](#toc)

---

<a id="q25"></a>
## 25. Dart VM কী?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q25)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart VM হলো সেই system, যা Dart চালায়। Development-এ এটা আপনার code compile করে আর চালায় (JIT)। Release build-এ আপনার code আগেই native-এ compile হয়ে থাকে (AOT), কিন্তু VM-এর একটা ছোট অংশ তখনো থাকে — garbage collection, isolate আর event loop সামলানোর জন্য। তাই 'VM' মানে 'ধীর' বা 'interpreted' নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — VM-এর দুটো কাজ: compiler + runtime helper।**
Dart VM-এর দুটো অংশ আছে:
1. একটা compiler (development-এ JIT-এর জন্য ব্যবহার হয়)।
2. Runtime helper — garbage collection (memory পরিষ্কার), isolate management, event loop।

**ধাপ ২ — Release-এ (AOT) কী হয়।**
Release build-এ compiler অংশটা আর দরকার হয় না (code আগেই native)। কিন্তু runtime helper-গুলো তখনো app-এর ভেতরে থাকে, কারণ app-এর তখনো memory পরিষ্কার, isolate আর event loop লাগে।

তাই: AOT compiler সরিয়ে দেয়, কিন্তু runtime helper রেখে দেয়।

**ধাপ ৩ — সাধারণ ভুল বোঝাবুঝি।**
"VM" শুনলে মানুষ ভাবে "পুরোনো Java-র মতো ধীর বা interpreted।" Release Flutter-এর জন্য এটা ভুল — আপনার code native machine code হিসেবে চলে। VM runtime শুধু পেছনে সহায়ক সেবা দেয়।

**সাধারণ ভুল:** ভাবা যে AOT মানে "VM একেবারেই নেই।" Release-এ compiler চলে যায়, কিন্তু runtime support থেকে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Snapshot কী?"* → এটা আপনার program-এর সংরক্ষিত, load করার জন্য তৈরি একটা রূপ। App দ্রুত চালু করতে এটা ব্যবহার হয়।

**সম্পর্কিত:** [Q24 — JIT বনাম AOT](#q24) · [Q26 — garbage collection](#q26)

[↑ উপরে ফিরুন](#toc)

---

<a id="q26"></a>
## 26. Dart কীভাবে memory manage করে (garbage collection)?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-01-dart-language.md#q26)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart নিজে থেকেই সেই memory ছেড়ে দেয় যেটা আপনি আর ব্যবহার করছেন না — এটাই garbage collection (GC)। এটা একটা 'generational' design ব্যবহার করে, যার ভিত্তি একটা সহজ ধারণা: বেশিরভাগ object অল্প বয়সেই মরে যায়। নতুন object যায় একটা ছোট জায়গায়, যেটা দ্রুত পরিষ্কার হয়। যেসব object টিকে যায়, সেগুলো পুরোনো একটা জায়গায় সরে যায়, যেটা কম ঘন ঘন পরিষ্কার হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Garbage collection কী।**
Dart-এ আপনি হাতে করে memory ছাড়েন না। GC নিজেই খুঁজে বের করে কোন object আপনি আর ব্যবহার করছেন না, আর সেগুলো ছেড়ে দেয়। এতে বেশিরভাগ memory bug ঠেকানো যায়।

**ধাপ ২ — মূল ধারণা: "বেশিরভাগ object অল্প বয়সেই মরে যায়।"**
বাস্তব app-এ বেশিরভাগ object খুব দ্রুত তৈরি হয় আর ফেলে দেওয়া হয় (বিশেষ করে Flutter widget, যেগুলো বারবার rebuild হয়)। Dart-এর GC এই কথা মাথায় রেখেই বানানো:
- **Young area (new space):** নতুন object এখানে আসে। এটা দ্রুত আর ঘন ঘন পরিষ্কার হয় (সস্তা)।
- **Old area (old space):** যেসব object কিছুক্ষণ টিকে যায়, সেগুলো এখানে সরে আসে। এটা কম ঘন ঘন পরিষ্কার হয়।

এটাকে বলে generational GC — "young" (অল্প সময় বাঁচে) আর "old" (অনেকক্ষণ বাঁচে) object আলাদা করা।

**ধাপ ৩ — Flutter-এর জন্য এটা কেন গুরুত্বপূর্ণ।**
Flutter প্রতি frame-এ বিশাল সংখ্যক অল্প সময়ের widget object বানায়। Young area পরিষ্কার করা সস্তা বলে এটা design অনুযায়ী ঠিক আছে — widget rebuild করা যে মেনে নেওয়া যায়, তার একটা বড় কারণ এটাই।

**ধাপ ৪ — বাস্তব নিয়ম।**
GC-তে এখনো সামান্য সময় লাগে। আপনি যদি `build()`-এর ভেতরে বা scroll/animation callback-এ (যেগুলো প্রতি সেকেন্ডে 60–120 বার চলে) প্রচুর object বানান, তাহলে এই পরিষ্কারের সময় জমতে থাকে। এতে ছোট ছোট আটকে যাওয়া (jank) হতে পারে। তাই এই "hot path"-এ ভারী object তৈরি করা এড়িয়ে চলুন।

```dart
// ভুল: প্রতি build/frame-এ একটা নতুন ভারী object বানানো
Widget build(BuildContext context) {
  final formatter = DateFormat('yyyy-MM-dd'); // প্রতি rebuild-এ তৈরি হয়
  return Text(formatter.format(date));
}

// ভালো: একবার বানিয়ে বারবার ব্যবহার করুন
static final _formatter = DateFormat('yyyy-MM-dd');
```

**Interviewer কেন জিজ্ঞেস করে:** Memory-র আচরণকে একটা বাস্তব Flutter নিয়মের সাথে জুড়তে — hot path-এ ভারী allocation করবেন না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"GC কীসে trigger হয়?"* → বেশিরভাগ সময় young area ভরে গেলে। GC-কে সরাসরি নিয়ন্ত্রণ করা যায় না, কিন্তু আপনি কত object বানাচ্ছেন সেটা আপনার হাতে।
- *"Dart-এ কি এখনো memory leak হতে পারে?"* → হ্যাঁ — যদি আপনি অপ্রয়োজনীয় reference ধরে রাখেন (cancel না করা stream subscription, listener, closure-এর ভেতরে বড় object)। যেটা এখনো reference করা আছে, GC সেটা ছাড়তে পারে না।

**সম্পর্কিত:** [Q25 — Dart VM](#q25) · [Q3 — const allocation কমায়](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার table, তারপর এক লাইনের মনে করিয়ে দেওয়া কথাগুলো।

## দ্রুত তুলনার table

**`final` vs `const`**

| | `final` | `const` |
|---|---|---|
| কখন সেট হয় | একবার, runtime-এ হলেও চলে | compile time-এ (চালু হওয়ার আগে) |
| ভেতরের জিনিস | ভেতরে বদলাতে পারে (যেমন একটা list) | পুরোপুরি জমাট |
| Memory | প্রতিবার নতুন object | একই object আবার ব্যবহার হয় |

**`extends` vs `implements` vs `with`**

| | কী পাবেন | কতগুলো |
|---|---|---|
| `extends` | parent-এর code | একটা |
| `implements` | শুধু নিয়ম (সব নিজে লিখতে হবে) | অনেকগুলো |
| `with` (mixin) | reusable behavior | অনেকগুলো |

**`Future` vs `Stream`**

| `Future` | `Stream` |
|---|---|
| একটা value, একবার | সময়ের সাথে অনেক value |
| `await` / `.then()` | `listen()` / `await for` |
| `FutureBuilder` | `StreamBuilder` |

**`sync*` vs `async*`**

| `sync*` | `async*` |
|---|---|
| একটা `Iterable` ফেরত দেয় | একটা `Stream` ফেরত দেয় |
| lazy — চাইলে তবেই টেনে আনে | সময়ের সাথে push করে |

**JIT vs AOT**

| JIT (debug) | AOT (release) |
|---|---|
| চলার সময়ে compile | চালু হওয়ার আগে compile |
| hot reload সম্ভব করে | দ্রুত startup, মসৃণ |
| development | production |

## এক লাইনের মনে করিয়ে দেওয়া কথা

- **Null safety** = একটা variable null হতে পারবে না, যদি না আপনি `?` দিয়ে অনুমতি দেন। প্রতিটা `!` একটা ঝুঁকিপূর্ণ প্রতিশ্রুতি। ([Q1](#q1))
- **`final`** বাক্সটা লক করে (একবার সেট); **`const`** সবকিছু জমাট করে আর একই object আবার ব্যবহার করে। ([Q2](#q2), [Q3](#q3))
- **`==` আর `hashCode`** সবসময় একসাথে override করতে হবে, এমন field দিয়ে যেগুলো বদলায় না। ([Q4](#q4))
- **`extends`** = code inherit করা (একটা)। **`implements`** = নিয়ম মানা, সব code নিজে লেখা (অনেকগুলো)। **`with`** = behavior যোগ করা। ([Q12](#q12))
- **Factory** constructor একটা cache করা object বা subtype ফেরত দিতে পারে; সাধারণ constructor সবসময় নতুন object বানায়। ([Q11](#q11))
- **Records** = দ্রুত value-র থলে। **Patterns** = আকার মিলিয়ে দেখা + খুলে নেওয়া। **Sealed** class = "প্রতিটা case handle করো" — এই নিরাপত্তা। ([Q16](#q16), [Q17](#q17), [Q18](#q18))
- **`await` app জমিয়ে দেয় না** — এটা একটা function থামায়, বাকি কাজ চলতে দেয়। ([Q19](#q19))
- **Microtask (VIP) event-এর (সাধারণ) আগে চলে** → output `1, 4, 3, 2`। ([Q20](#q20))
- **Single-subscription** stream = একজন listener; **broadcast** = অনেকজন। সবসময় cancel আর close করুন। ([Q21](#q21))
- **`sync*`** → lazy `Iterable`; **`async*`** → `Stream`। `yield` = একটা value; `yield*` = অন্য একটা থেকে সবগুলো। ([Q22](#q22))
- **Isolate** = আলাদা worker, আলাদা memory, message পাঠানো। ভারী CPU কাজে ব্যবহার করুন, network-এ নয়। ([Q23](#q23))
- **JIT** (debug) = hot reload; **AOT** (release) = দ্রুত native। Debug-এ কখনোই speed test করবেন না। ([Q24](#q24))
- **Generational GC**: বেশিরভাগ object অল্প বয়সে মরে, তাই পরিষ্কার করা সস্তা। `build()`-এর ভেতরে allocate করবেন না। ([Q26](#q26))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যায়

Interviewer সাধারণত একটা প্রশ্নে থামেন না। আপনার গভীরতা যাচাই করতে তাঁরা খুঁড়তে থাকেন। এই chain-টা মুখে বলে উত্তর দেওয়ার অনুশীলন করুন — শান্তভাবে, ধাপে ধাপে:

1. *"`final` আর `const`-এর পার্থক্য কী?"* → একবার সেট (runtime হলেও চলে) vs চালু হওয়ার আগেই জানা (জমাট)।
2. *"তাহলে `const` Flutter-কে কীভাবে সাহায্য করে?"* → const object memory-তে আবার ব্যবহার হয়, তাই Flutter সেগুলো rebuild করা বাদ দেয়।
3. *"Flutter কীভাবে বোঝে যে বাদ দেওয়া যাবে?"* → এটা আগের সেই একই object, তাই widget-টি update করার দরকার নেই।
4. *"একটা value যদি runtime-এ ঠিক হয়, তখন কী?"* → তখন সেটা `const` হতে পারবে না; বদলানো অংশটা আলাদা রাখুন আর বাকিটা `const` করুন।
5. *"Rebuild বাদ পড়েছে সেটা কীভাবে প্রমাণ করবেন?"* → Flutter DevTools ব্যবহার করুন, "Track Widget Rebuilds"।

এভাবে শান্তভাবে ধাপে ধাপে যেতে পারা — অনুমান না করে — এটাই আপনাকে **senior** শোনায়, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

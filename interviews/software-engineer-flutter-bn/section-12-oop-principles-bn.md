# Section 12 — OOP ও Design Principles

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** এবং **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি ঘুরে ঘুরে পড়তে পারবেন এবং ধীরে ধীরে প্রস্তুতি নিতে পারবেন।
> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-12-oop-principles-bn.md](../software-engineer-flutter/section-12-oop-principles.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার জন্য ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code সহ ধাপে ধাপে বিস্তারিত ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সংযুক্ত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর তার কঠিনতা (**Easy / Medium / Hard**)।

> **Interview Tip:** OOP আর SOLID-এর ক্ষেত্রে আগে এক লাইনে সংজ্ঞা বলুন, তারপর ছোট একটা বাস্তব উদাহরণ, তারপর code। উদাহরণটাই interviewer-কে মাথা নাড়ায়।

---

<a id="toc"></a>

## সূচিপত্র

**A. OOP-এর চারটি স্তম্ভ**
1. [চারটি স্তম্ভ — সারসংক্ষেপ](#q1) · *Very common*
2. [Encapsulation](#q2) · *Very common*
3. [Inheritance — `extends`, `super`, `@override`](#q3) · *Very common*
4. [Polymorphism](#q4) · *Very common*
5. [Abstraction — abstract class বনাম interface](#q5) · *Very common*

**B. Class-এর সম্পর্ক ও design**
6. [Inheritance-এর বদলে Composition](#q6) · *Very common*
7. [Mixin বনাম Abstract Class বনাম Interface](#q7) · *Common*
8. [Class বনাম Object বনাম Instance](#q8) · *Common*
9. [Coupling ও Cohesion](#q9) · *Very common*

**C. SOLID principles**
10. [S — Single Responsibility](#q10) · *Very common*
11. [O — Open/Closed](#q11) · *Very common*
12. [L — Liskov Substitution](#q12) · *Common*
13. [I — Interface Segregation](#q13) · *Common*
14. [D — Dependency Inversion](#q14) · *Very common*

**D. আরও কিছু গুরুত্বপূর্ণ principle**
15. [DRY — Don't Repeat Yourself](#q15) · *Common*
16. [KISS — Keep It Simple](#q16) · *Common*
17. [YAGNI — You Aren't Gonna Need It](#q17) · *Common*

**E. Dart OOP-এর খুঁটিনাটি**
18. [Constructor-এর ধরন](#q18) · *Common*
19. [`static` member](#q19) · *Common*
20. [Covariance ও contravariance](#q20) · *Deeper*
21. [Method overriding বনাম method hiding](#q21) · *Deeper*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---

<a id="study-plan"></a>

## ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

এই পর্যায়গুলো ক্রমে অনুসরণ করুন। একটা পর্যায় তখনই শেষ ধরুন, যখন না দেখে **সংক্ষিপ্ত উত্তর** বাস্তব উদাহরণসহ বলতে পারবেন।

**পর্যায় ১ — চারটি স্তম্ভ (এখান থেকে শুরু করুন)।** সব OOP প্রশ্নের ভিত্তি এটাই।
→ [Q1 সারসংক্ষেপ](#q1) · [Q2 Encapsulation](#q2) · [Q3 Inheritance](#q3) · [Q4 Polymorphism](#q4) · [Q5 Abstraction](#q5)

**পর্যায় ২ — Class-গুলো একে অন্যের সাথে কীভাবে যুক্ত হয়।**
→ [Q6 Inheritance-এর বদলে composition](#q6) · [Q9 Coupling ও cohesion](#q9) · [Q7 Mixin বনাম abstract বনাম interface](#q7) · [Q8 Class বনাম object](#q8)

**পর্যায় ৩ — SOLID (senior-দের প্রিয় বিষয়)।**
→ [Q10 SRP](#q10) · [Q11 OCP](#q11) · [Q14 DIP](#q14) · [Q12 LSP](#q12) · [Q13 ISP](#q13)

**পর্যায় ৪ — ছোট principle-গুলো।**
→ [Q15 DRY](#q15) · [Q16 KISS](#q16) · [Q17 YAGNI](#q17)

**পর্যায় ৫ — Dart-এর নিজস্ব খুঁটিনাটি।**
→ [Q18 Constructor](#q18) · [Q19 static](#q19) · [Q20 Covariance](#q20) · [Q21 Overriding বনাম hiding](#q21)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** এই আটটা দেখে নিন:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q6](#q6) · [Q9](#q9) · [Q10](#q10) · [Q11](#q11) · [Q14](#q14), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. OOP-এর চারটি স্তম্ভ

---

<a id="q1"></a>
## 1. Object-Oriented Programming-এর চারটি স্তম্ভ কী কী?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"চারটি স্তম্ভ হলো Encapsulation, Abstraction, Inheritance আর Polymorphism। Encapsulation ভেতরের খুঁটিনাটি লুকায়, abstraction শুধু দরকারি জিনিস দেখায় আর জটিলতা লুকায়, inheritance এক class-কে আরেক class-এর code আবার ব্যবহার করতে দেয়, আর polymorphism একই কাজকে ভিন্ন type-এর জন্য ভিন্নভাবে চলতে দেয়। এই চারটা মিলে বাস্তব জিনিসকে পরিষ্কার ও পুনরায় ব্যবহারযোগ্য code-এ রূপ দিতে সাহায্য করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — প্রতিটার এক লাইনের ছবি।**

| স্তম্ভ | এক লাইনে | বাস্তব জীবনের উদাহরণ |
|---|---|---|
| **Encapsulation** | ভেতরের state লুকান, নিরাপদ API দিন | TV remote তারের জট লুকায়; আপনি শুধু button চাপেন |
| **Abstraction** | যা দরকার শুধু তাই দেখান, জটিলতা লুকান | engine না জেনেই গাড়ি চালানো |
| **Inheritance** | child class parent-এর code আবার ব্যবহার করে | সন্তান বাবা-মায়ের বৈশিষ্ট্য পায় |
| **Polymorphism** | এক কাজ, অনেক রূপ | "draw()" circle, square, triangle সবার জন্য কাজ করে |

**ধাপ ২ — ছোট একটা code উদাহরণ, যেখানে সবগুলো একসাথে আছে।**

```dart
// Abstraction: shape শুধু area-এর কথা দেয়, হিসাবটা লুকায়
abstract class Shape {
  double area(); // কী, কীভাবে নয়
}

// Inheritance + Polymorphism: প্রতিটা shape নিজের মতো করে area() লেখে
class Circle extends Shape {
  final double r;
  Circle(this.r);
  @override
  double area() => 3.14 * r * r;
}

class Square extends Shape {
  final double side;
  Square(this.side);
  @override
  double area() => side * side;
}

// Polymorphism কাজের মধ্যে: একই call, ভিন্ন behaviour
void printArea(Shape s) => print(s.area());
```

**ধাপ ৩ — একই ধারণায় Encapsulation।**
`Circle` যদি `r`-কে private রাখত আর শুধু একটা getter দিত, সেটাই encapsulation — field-টা বাইরের পরিবর্তন থেকে সুরক্ষিত থাকত।

**Interviewer কেন জিজ্ঞেস করে:** এটা OOP-এর ভিত্তি। তাঁরা চান পরিষ্কার সংজ্ঞা, সাথে প্রতিটার একটা বাস্তব উদাহরণ — শুধু মুখস্থ শব্দ নয়।

**সাধারণ ভুল:** উদাহরণ ছাড়া শুধু চারটা শব্দ বলে দেওয়া। অথবা abstraction (জটিলতা লুকানো) আর encapsulation (data লুকানো) গুলিয়ে ফেলা। দুটোতে মিল আছে, কিন্তু দৃষ্টিকোণ আলাদা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Abstraction বনাম encapsulation?"* → Abstraction হলো *design* নিয়ে (শুধু দরকারি জিনিস দেখানো)। Encapsulation হলো *implementation* নিয়ে (data রক্ষা করা)। দেখুন [Q2](#q2) আর [Q5](#q5)।

**সম্পর্কিত:** [Q2 — encapsulation](#q2) · [Q3 — inheritance](#q3) · [Q4 — polymorphism](#q4) · [Q5 — abstraction](#q5)

[↑ উপরে ফিরুন](#toc)

---

<a id="q2"></a>
## 2. Encapsulation কী, Dart-এ এটা কীভাবে করবেন, আর এটা কেন গুরুত্বপূর্ণ?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Encapsulation মানে একটা object-এর ভেতরের data লুকিয়ে রাখা। বাইরের code শুধু নিরাপদ method দিয়ে সেটা ছুঁতে পারবে। Dart-এ শুরুতে underscore দিয়ে field private করা হয়, তারপর getter বা method দিয়ে access নিয়ন্ত্রণ করা হয়। এটা গুরুত্বপূর্ণ কারণ object-কে ভুল অবস্থায় চলে যাওয়া থেকে বাঁচায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব ছবি: ওষুধের capsule।**
Capsule ওষুধটাকে একটা নিরাপদ খোলসের ভেতরে মুড়ে রাখে। আপনি গুঁড়ো সরাসরি ছোঁন না; পুরো capsule-টাই খান। Encapsulation ঠিক এভাবেই data-কে নিরাপদ খোলসে মুড়ে রাখে।

**ধাপ ২ — Dart-এ `_` জিনিসকে private করে (file/library-এর জন্য)।**

```dart
class BankAccount {
  double _balance = 0; // private — file-এর বাইরে থেকে ছোঁয়া যাবে না

  double get balance => _balance; // শুধু পড়ার view

  void deposit(double amount) {
    if (amount <= 0) throw ArgumentError('must be positive'); // একটা নিরাপদ gate
    _balance += amount;
  }
}
```

বাইরের code `deposit` করতে পারবে, কিন্তু সরাসরি `_balance = -999` বসাতে পারবে না। Class নিজের state নিজেই নিয়ন্ত্রণ করে।

**ধাপ ৩ — কেন গুরুত্বপূর্ণ: invariant রক্ষা করা।**
Encapsulation ছাড়া যে কেউ balance-এ ভুল মান বসিয়ে দিতে পারত। এটা থাকলে প্রতিটা পরিবর্তন এমন একটা method দিয়ে যায়, যেটা যাচাই করতে পারে। ফলে bug ঠেকে আর object সবসময় বৈধ থাকে।

**ধাপ ৪ — Dart-এর privacy নিয়ে একটা কথা।**
Dart-এ `_` private হয় *library*-এর জন্য (মানে file-এর জন্য), class-এর জন্য নয়। একই file-এর ভেতরে অন্য class-গুলো এটা দেখতে পায়। ভিন্ন file থেকে এটা লুকানো থাকে।

**Interviewer কেন জিজ্ঞেস করে:** এটা সবচেয়ে ব্যবহারিক স্তম্ভ। তাঁরা দেখতে চান আপনি state রক্ষা করেন, নাকি সব জায়গায় public field খুলে রাখেন।

**সাধারণ ভুল:** সব field public আর mutable রেখে দেওয়া, তারপর এমন getter/setter দিয়ে "encapsulate" করা যেগুলো আসলে কিছুই করে না। আসল encapsulation হয় validation যোগ করে, নয়তো field-টা পুরোপুরি লুকিয়ে ফেলে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Getter আর setter?"* → `get` পড়ার একটা view দেয়; `set` লেখার সময় যাচাই করতে দেয়। এগুলো access নিয়ন্ত্রণের জন্য ব্যবহার করুন, প্রতিটা field মুড়ে দেওয়ার জন্য নয়।
- *"`_` কি সত্যিই private?"* → এটা library (file)-এর জন্য private, তাই একই file-এর code এটা ব্যবহার করতে পারে।

**সম্পর্কিত:** [Q1 — চারটি স্তম্ভ](#q1) · [Q9 — low coupling](#q9)

[↑ উপরে ফিরুন](#toc)

---

<a id="q3"></a>
## 3. Dart-এ Inheritance কীভাবে কাজ করে? `extends`, `super`, আর `@override` ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Inheritance-এর মাধ্যমে একটা class `extends` দিয়ে আরেকটা class-এর code পুনরায় ব্যবহার করতে পারে। Child parent-এর field আর method পেয়ে যায়। `super` দিয়ে parent-এর version call করা যায়। আর `@override` দিয়ে একটা method-কে নিজের version দিয়ে বদলানো যায়। Dart-এ parent মাত্র একটাই হতে পারে (single inheritance)।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: সন্তান আর বাবা-মা।**
সন্তান বাবা-মার কাছ থেকে কিছু বৈশিষ্ট্য পায়। তার নিজের আলাদা বৈশিষ্ট্যও থাকতে পারে। Parent হলো ভিত্তি। Child নতুন জিনিস যোগ করে বা বদলে দেয়।

**ধাপ ২ — `extends` parent-এর code পুনরায় ব্যবহার করে।**

```dart
class Animal {
  void breathe() => print('breathing');
  void describe() => print('I am an animal');
}

class Dog extends Animal {
  void bark() => print('woof');     // নতুন behaviour
}

Dog().breathe(); // বিনা খরচে inherit হলো
```

**ধাপ ৩ — `@override` parent-এর method বদলে দেয়।**

```dart
class Dog extends Animal {
  @override
  void describe() => print('I am a dog'); // parent-এর version বদলে দেয়
}
```

`@override` লেখা বাধ্যতামূলক নয়, কিন্তু খুব জোরালোভাবে সুপারিশ করা হয় — এটা compiler-কে বলে "আমি এটা বদলাতে চাইছি"। ফলে method-এর নামে typo হলে সেটা error হয়ে যায়। চুপচাপ একটা নতুন method তৈরি হয় না।

**ধাপ ৪ — `super` parent-এর version call করে।**

```dart
class Dog extends Animal {
  @override
  void describe() {
    super.describe();          // আগে parent-এর version চালান
    print('...specifically a dog');
  }
}
```

Constructor-এও `super` ব্যবহার হয় — parent-এর কাছে value পাঠানোর জন্য।

**ধাপ ৫ — Dart-এ parent মাত্র একটাই।**
আপনি ঠিক একটা class-ই `extends` করতে পারবেন। একাধিক জায়গা থেকে code পুনরায় ব্যবহার করতে চাইলে mixin (`with`) বা composition ব্যবহার করুন (দেখুন [Q6](#q6), [Q7](#q7))।

**Interviewer কেন জিজ্ঞেস করে:** Flutter-এ inheritance সব জায়গায় (প্রতিটা widget আরেকটা widget extends করে)। তাঁরা দেখেন আপনি `super`, `@override` আর single-parent নিয়মটা জানেন কি না।

**সাধারণ ভুল:** সম্পর্কহীন class-এর মধ্যে code ভাগ করতে inheritance-এর অতিরিক্ত ব্যবহার। সত্যিকারের "is-a" সম্পর্ক না হলে composition বেছে নিন ([Q6](#q6))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Inheritance vs composition?"* → Inheritance = "is-a"; composition = "has-a"। নমনীয়তার জন্য composition বেছে নিন ([Q6](#q6))।
- *"`@override` কেন ব্যবহার করবেন?"* → এটা typo ধরে ফেলে আর উদ্দেশ্য স্পষ্ট করে।

**সম্পর্কিত:** [Q6 — inheritance-এর বদলে composition](#q6) · [Q7 — mixin](#q7) · [Q4 — polymorphism](#q4)

[↑ উপরে ফিরুন](#toc)

---

<a id="q4"></a>
## 4. Polymorphism কী? Compile-time বনাম runtime ব্যাখ্যা করুন, আর Dart overloading কীভাবে সামলায়।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Polymorphism মানে একটা কাজ অনেক রূপ নেয় — একই method call object-এর আসল type অনুযায়ী ভিন্নভাবে আচরণ করে। Runtime polymorphism হলো method overriding, যেটা program চলার সময়ে ঠিক হয়। Dart-এর একটা গুরুত্বপূর্ণ বিষয়: Dart method overloading (একই নাম, ভিন্ন parameter) support করে না। তাই আমরা এর বদলে optional বা named parameter ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: "run" শব্দটা।**
মানুষ, app আর নদীর জন্য "run" মানে ভিন্ন ভিন্ন জিনিস। একটা শব্দ, অনেক আচরণ — এটাই polymorphism।

**ধাপ ২ — Runtime polymorphism = method overriding।**
আপনার হাতে থাকে parent type। কিন্তু আসল object ঠিক করে কোন method চলবে।

```dart
abstract class Shape { double area(); }
class Circle extends Shape { final double r; Circle(this.r); double area() => 3.14 * r * r; }
class Square extends Shape { final double s; Square(this.s); double area() => s * s; }

void show(Shape shape) => print(shape.area()); // একই call...
show(Circle(2)); // 12.56  ...ভিন্ন behaviour
show(Square(3)); // 9
```

Variable-এর type হলো `Shape`। কিন্তু আসল object (Circle বা Square) ঠিক করে কোন `area()` চলবে। এই সিদ্ধান্ত runtime-এ হয়।

**ধাপ ৩ — Dart-এ method overloading নেই।**
Java-তে একই নামের দুটো method রাখা যায়, শুধু parameter আলাদা হবে। Dart এটা allow করে না। তার বদলে optional বা named parameter ব্যবহার করুন:

```dart
// Dart-এ এটা allowed নয়:
// void greet() {}
// void greet(String name) {}

// এর বদলে এটা করুন:
void greet([String? name]) {
  print(name == null ? 'Hi' : 'Hi $name');
}
```

**ধাপ ৪ — Compile-time polymorphism।**
যেসব ভাষায় overloading আছে, সেখানে কোন overloaded method call হবে তা compile time-এ ঠিক হয় ("compile-time polymorphism")। Dart-এ overloading নেই। তাই আপনি যে polymorphism ব্যবহার করেন সেটা প্রধানত runtime (overriding) ধরনের। Dart-এর generics-ও এক ধরনের compile-time polymorphism দেয়।

**Interviewer কেন জিজ্ঞেস করে:** Polymorphism-ই code-কে extensible করে। "Dart-এ overloading নেই" — এই পয়েন্টটা তাঁদের প্রিয় ফাঁদ।

**সাধারণ ভুল:** বলা যে Dart overloading support করে। করে না — optional/named parameter ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"বাস্তব Flutter উদাহরণ?"* → `Widget build()` প্রতিটা widget override করে — একই call, ভিন্ন UI।
- *"Overloading নকল করবেন কীভাবে?"* → Named/optional parameter, বা ভিন্ন নামের factory constructor।

**সম্পর্কিত:** [Q3 — inheritance (overriding)](#q3) · [Q1 — চারটি স্তম্ভ](#q1) · [Q21 — overriding vs hiding](#q21)

[↑ উপরে ফিরুন](#toc)

---

<a id="q5"></a>
## 5. Abstraction কী? Dart-এ `abstract class` আর interface (`implements`)-এর মধ্যে পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Abstraction মানে কোনো জিনিস কী করে শুধু সেটা দেখানো, আর কীভাবে করে সেটা লুকিয়ে রাখা। Dart-এ `abstract class`-এ অসম্পূর্ণ method আর shared code দুটোই থাকতে পারে, আর এটাকে `extends` করতে হয়। যেকোনো class-কে `implements` দিয়ে interface হিসেবেও ব্যবহার করা যায়। সেখানে শুধু method signature পাওয়া যায়, সব code নিজেকে লিখতে হয়। Dart-এ আলাদা কোনো `interface` keyword নেই — প্রতিটা class-ই একটা interface।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: গাড়ি চালানো।**
আপনি steering wheel আর pedal ব্যবহার করেন (এটাই interface)। Engine কীভাবে জ্বালানি পোড়ায় তা জানার দরকার নেই (এটাই implementation)। Abstraction engine-টাকে লুকিয়ে রাখে।

**ধাপ ২ — `abstract class` = আংশিক blueprint (shared code থাকতে পারে)।**

```dart
abstract class Payment {
  void pay(double amount);     // abstract: body নেই, পরে ভরতে হবে
  void logReceipt() => print('receipt saved'); // shared code, inherit হয়
}

class CardPayment extends Payment {
  @override
  void pay(double amount) => print('paid \$amount by card');
}
```

আপনি সরাসরি `Payment()` বানাতে পারবেন না — এটা abstract। এটাকে `extends` করে বাকি method-গুলো ভরতে হয়।

**ধাপ ৩ — `implements` = শুধু contract নিন, সবকিছু নিজে লিখুন।**

```dart
class WalletPayment implements Payment {
  // implements কোনো code দেয় না — প্রতিটা method নিজে লিখতে হবে, এমনকি logReceipt()
  @override
  void pay(double amount) => print('paid by wallet');
  @override
  void logReceipt() => print('wallet receipt');
}
```

**ধাপ ৪ — এক লাইনে পার্থক্য।**
- `extends` (abstract class) → code + contract দুটোই inherit হয়। Parent একটাই।
- `implements` (interface) → শুধু contract, কোনো code নয়। একসাথে অনেকগুলো।

**ধাপ ৫ — Dart-এ `interface` keyword নেই।**
প্রতিটা class নিজে থেকেই একটা interface তৈরি করে। তাই যেকোনো class-কে `implements` করা যায়। কিছু code ভাগ করতে চাইলে abstract class ব্যবহার করুন। শুধু একটা contract চাপাতে চাইলে pure interface (`implements`) ব্যবহার করুন — fake দিয়ে testing-এর জন্য এটা দারুণ।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি contract-এর উপর ভিত্তি করে design করতে পারেন কি না। নমনীয় ও testable code-এর মূল কথাই এটা।

**সাধারণ ভুল:** ভাবা যে Dart-এ আলাদা একটা `interface` keyword আছে (নেই)। অথবা ভাবা যে `implements` code inherit করে (করে না — সবকিছু নতুন করে লিখতে হয়)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কখন abstract class, কখন interface?"* → Code ভাগ করতে চাইলে abstract class। শুধু contract দরকার আর সহজে mock করতে চাইলে interface (`implements`)।

**সম্পর্কিত:** [Q7 — mixin vs abstract vs interface](#q7) · [Q1 — abstraction স্তম্ভ](#q1) · [Q14 — DIP](#q14)

[↑ উপরে ফিরুন](#toc)

---

# B. Class-এর সম্পর্ক ও design

---

<a id="q6"></a>
## 6. "Composition over Inheritance" কী? কখন আর কেন এটা বেছে নেবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Composition মানে একটা class অন্য কিছু object দিয়ে তৈরি হয়, যেগুলো তার *আছে*। Parent থেকে inherit করে নয়, যেটা সে *হয়*। 'inheritance-এর বদলে composition বেছে নিন' পরামর্শের মানে: গভীর class tree না বানিয়ে class-কে তার দরকারি টুকরোগুলো field হিসেবে দিন। এটা বেশি নমনীয় — কঠিন hierarchy ছাড়াই আচরণ মেশানো আর বদলানো যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — "is-a" vs "has-a"।**
- Inheritance = "is-a": একটা Dog **হলো একটা** Animal।
- Composition = "has-a": একটা Car-এর **আছে একটা** Engine।

**ধাপ ২ — গভীর inheritance-এর সমস্যা।**
ধরুন `Animal → Bird → FlyingBird`। এখন আপনার দরকার একটা penguin (এমন bird যে উড়তে পারে না) আর একটা bat (এমন mammal যে ওড়ে)। Tree ভেঙে পড়ে — "উড়তে পারে" গুণটা একটা parent chain-এ সুন্দরভাবে বসে না।

**ধাপ ৩ — Composition সমস্যাটা মেটায়: আচরণটা class-কে একটা টুকরো হিসেবে দিন।**

```dart
// Behaviour-গুলো ছোট, বদলে-নেওয়া-যায় এমন টুকরো হিসেবে
class FlyAbility { void fly() => print('flying'); }
class SwimAbility { void swim() => print('swimming'); }

// একটা Duck-এর কাছে দরকারি ability-গুলো আছে
class Duck {
  final _fly = FlyAbility();
  final _swim = SwimAbility();
  void move() { _fly.fly(); _swim.swim(); }
}
```

এখন যেকোনো class ঠিক যে ability দরকার সেটাই নিতে পারে — কোনো কঠিন tree নেই।

**ধাপ ৪ — কেন এটা বেশি নমনীয়।**
- Runtime-এ আচরণ বদলানো যায় (টুকরোটা বদলে দিন)।
- "fragile base class" সমস্যা এড়ানো যায়, যেখানে parent বদলালে অনেক child ভেঙে যায়।
- এটা class-গুলোকে ছোট আর নির্দিষ্ট রাখে।

**ধাপ ৫ — কখন inheritance-ই ঠিক।**
সত্যিকারের, স্থায়ী "is-a" সম্পর্কের জন্য inheritance ব্যবহার করুন (প্রতিটা Flutter widget `Widget` extends করে)। শুধু আচরণ পুনরায় ব্যবহার করতে চাইলে composition ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা senior design-এর সহজাত বোধ। Composition-এর দিকে হাত বাড়ানো দেখায় আপনি কঠিন, বদলাতে-কষ্টকর hierarchy এড়িয়ে চলেন।

**সাধারণ ভুল:** Code ভাগ করার জন্য লম্বা inheritance tree বানানো। এটা সত্যিকারের "is-a" না হলে সেটা একটা লাল পতাকা — বরং compose করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter কীভাবে composition ব্যবহার করে?"* → Widget-গুলো compose করা হয়: subclass না বানিয়ে ছোট widget একটার ভেতরে আরেকটা রাখা হয় (Padding-এর ভেতরে Center, তার ভেতরে Text)।
- *"Mixin?"* → Dart-এর mixin মাঝামাঝি একটা পথ — parent ছাড়াই পুনরায় ব্যবহারযোগ্য আচরণ ([Q7](#q7))।

**সম্পর্কিত:** [Q3 — inheritance](#q3) · [Q7 — mixin](#q7) · [Q9 — coupling](#q9)

[↑ উপরে ফিরুন](#toc)

---

<a id="q7"></a>
## 7. Dart-এ Mixin, Abstract Class আর Interface-এর পার্থক্য কী? কখন কোনটা ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Abstract class হলো একটা আংশিক blueprint, যেটা আমি `extends` করি — এটা code শেয়ার করতে পারে, কিন্তু parent পাই মাত্র একটা। Mixin হলো পুনরায় ব্যবহারযোগ্য behaviour, যেটা `with` দিয়ে যোগ করি — অনেকগুলো যোগ করা যায়, আর inheritance ছাড়াই কাজ করা code পাওয়া যায়। Interface (যেকোনো class যেটা `implements` দিয়ে ব্যবহার হয়) শুধু একটা contract — কোনো code নেই, কিন্তু অনেকগুলো implement করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটা tool, পাশাপাশি।**

| Tool | Keyword | Code দেয়? | কয়টা? |
|---|---|---|---|
| Abstract class | `extends` | হ্যাঁ (শেয়ার করা) | একটা parent |
| Mixin | `with` | হ্যাঁ (behaviour) | অনেক |
| Interface | `implements` | না (শুধু contract) | অনেক |

**ধাপ ২ — Abstract class — code শেয়ার করে + contract বাধ্য করে।**

```dart
abstract class Repository {
  Future<void> save(String data);   // contract
  void log(String m) => print(m);   // শেয়ার করা code
}
```

**ধাপ ৩ — Mixin — সম্পর্কহীন অনেক class-এ behaviour যোগ করে।**

```dart
mixin Logger {
  void log(String m) => print('[LOG] $m');
}

class ApiService with Logger {}   // এখন বিনা খরচে log() পেল
class CacheService with Logger {} // এটারও log() আছে
```

Mixin-এ constructor রাখা যায় না। কারণ এটা host class-এর সাথে মিশে যায়।

**ধাপ ৪ — Interface — শুধু একটা contract (testing-এর জন্য দারুণ)।**

```dart
class FakeRepository implements Repository {
  @override
  Future<void> save(String data) async {} // test-এর জন্য একটা fake
  @override
  void log(String m) {}
}
```

**ধাপ ৫ — কীভাবে বাছবেন।**
- শেয়ার করা code দরকার + সত্যিকারের "is-a" সম্পর্ক? → abstract class।
- সম্পর্কহীন class-গুলোর মধ্যে behaviour পুনরায় ব্যবহার করা দরকার? → mixin।
- শুধু একটা contract দরকার (swap বা mock করার জন্য)? → interface (`implements`)।

**Interviewer কেন জিজ্ঞেস করে:** এটা গভীর Dart OOP জ্ঞান আর ভালো design judgment যাচাই করে।

**সাধারণ ভুল:** যেখানে interface (contract) দরকার সেখানে mixin ব্যবহার করা। অথবা ভাবা যে `implements` আপনাকে code দেয় (দেয় না)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Mixin কি কোনো base type দাবি করতে পারে?"* → হ্যাঁ, `on` দিয়ে: `mixin X on Animal` শুধু Animal-এর উপরেই ব্যবহার করা যাবে।

**সম্পর্কিত:** [Q5 — abstract vs interface](#q5) · [Q6 — composition](#q6) · [Q3 — inheritance](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q8"></a>
## 8. Class, Object আর Instance-এর মধ্যে পার্থক্য কী?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Class হলো blueprint। Object হলো সেই blueprint থেকে বানানো আসল জিনিস। 'Instance' object-এরই আরেকটা নাম — আমরা বলি একটা object কোনো class-এর 'একটা instance'। তাই `class User` হলো পরিকল্পনা, আর `User('Sara')` একটা instance বানায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: blueprint আর বাড়ি।**
- **class** হলো স্থপতির আঁকা বাড়ির blueprint।
- **object** হলো সেটা থেকে বানানো একটা আসল বাড়ি।
- "Instance" মানে object-ই — বানানো প্রতিটা বাড়ি ওই blueprint-এর "একটা instance"।

**ধাপ ২ — Code-এ।**

```dart
class User {              // class (blueprint)
  final String name;
  User(this.name);
}

final a = User('Sara');   // একটা object / instance
final b = User('Rahim');  // আরেকটা instance — একই class, ভিন্ন data
```

একটা class, অনেক instance। প্রতিটা instance-এর নিজের data থাকে। কিন্তু structure আর method একই থাকে।

**ধাপ ৩ — "Instance of"।**
`a is User` সত্য — `a` হলো `User`-এর একটা instance। "Instance" শব্দটা শুধু জোর দেয় যে "class থেকে বানানো একটা নির্দিষ্ট জিনিস।"

**Interviewer কেন জিজ্ঞেস করে:** এটা দ্রুত দেখে নেয় যে আপনার মৌলিক শব্দভাণ্ডার ঠিক আছে কি না — শুরুর দিকের বা screening round-এ খুব সাধারণ।

**সাধারণ ভুল:** "class" আর "object" একই অর্থে ব্যবহার করা। Class হলো পরিকল্পনা; object হলো বানানো জিনিস।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`new` কী করে?"* → এটা একটা instance বানায়। আধুনিক Dart-এ `new` ঐচ্ছিক এবং সাধারণত বাদ দেওয়া হয়।

**সম্পর্কিত:** [Q1 — OOP basics](#q1) · [Q18 — constructors](#q18)

[↑ উপরে ফিরুন](#toc)

---

<a id="q9"></a>
## 9. Coupling আর Cohesion কী? আমরা কেন low coupling আর high cohesion চাই?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Coupling মানে একটা অংশ আরেকটার উপর কতটা নির্ভর করে; cohesion মানে একটা অংশ একটা কাজে কতটা মনোযোগী। আমরা চাই low coupling (অংশগুলো আলাদাভাবে বদলানো যাবে) আর high cohesion (প্রতিটা class একটা পরিষ্কার কাজ করবে)। দুটো মিলে code বদলানো, test করা আর পুনরায় ব্যবহার করা সহজ করে দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি।**
- **Low coupling** = দেয়ালের socket-এ লাগানো যন্ত্রপাতি। পুরো বাড়ির তার না বদলে toaster-টা বদলে ফেলতে পারবেন।
- **High cohesion** = একটা toolbox, যার ভেতরের সব জিনিস একসাথেই মানায় (সব tool)। এলোমেলো জিনিসের drawer নয়।

**ধাপ ২ — Coupling: অংশগুলো কতটা জট পাকানো?**
High (খারাপ) coupling: একটা class আরেকটার ভেতরে গভীরে হাত দেয়। ফলে একটা বদলালে অন্যটা ভেঙে যায়।

```dart
// High coupling — OrderService নিজেই database বানায়, বদলানো/test করা কঠিন
class OrderService {
  final db = MySqlDatabase(); // একটা নির্দিষ্ট database-এর সাথে শক্তভাবে বাঁধা
}

// Low coupling — abstraction-এর উপর নির্ভর করুন, বাইরে থেকে দিন
class OrderService {
  final Database db;
  OrderService(this.db); // যেকোনো Database চলবে; swap বা test-এ fake করা সহজ
}
```

**ধাপ ৩ — Cohesion: class কি একটাই কাজ করে?**
Low (খারাপ) cohesion: একটা `User` class যেটা email-ও পাঠায়, file-ও save করে, আর date-ও format করে। High cohesion: `User` শুধু user-এর data রাখে; email, storage আর formatting আলাদা class সামলায়।

**ধাপ ৪ — দুটোই কেন গুরুত্বপূর্ণ।**
- Low coupling → অন্যগুলো না ভেঙে একটা অংশ বদলাতে বা বদলে ফেলতে পারবেন (আর fake দিয়ে test করতে পারবেন)।
- High cohesion → প্রতিটা class ছোট, পরিষ্কার আর পুনরায় ব্যবহারযোগ্য।

এই দুটো ধারণাই SOLID-এর বেশিরভাগ নিয়মের পেছনের "কেন" (বিশেষ করে [SRP](#q10) আর [DIP](#q14))।

**Interviewer কেন জিজ্ঞেস করে:** এগুলো ভালো design-এর মূল মাপকাঠি। Senior engineer-রা এই ভাষাতেই কথা বলেন।

**সাধারণ ভুল:** "god class" বানানো, যেটা সব কাজ করে (low cohesion)। আর ভেতরে `new` দিয়ে dependency শক্ত করে বেঁধে ফেলা (high coupling)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Coupling কীভাবে কমাবেন?"* → Abstraction-এর উপর নির্ভর করুন আর dependency inject করুন ([Q14](#q14))।
- *"SOLID-এর সাথে সম্পর্ক?"* → SRP cohesion বাড়ায়; DIP coupling কমায়।

**সম্পর্কিত:** [Q10 — SRP](#q10) · [Q14 — DIP](#q14) · [Q6 — composition](#q6)

[↑ উপরে ফিরুন](#toc)

---

# C. SOLID principles

> SOLID হলো class-এর জন্য ৫টা নিয়ম, যেগুলো code বদলানো আর test করা সহজ করে। অন্তত একটা প্রশ্ন আশা করুন — প্রায়ই পাঁচটাই আসে।

---

<a id="q10"></a>
## 10. SOLID — S: Single Responsibility Principle (SRP)

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা class বদলানোর কারণ একটাই থাকা উচিত — একটাই কাজ। একটা class যদি দুটো আলাদা বিষয় সামলায়, তাহলে একটার পরিবর্তন অন্যটা ভেঙে দিতে পারে। তাই আমি মেশানো দায়িত্বগুলো আলাদা করে মনোযোগী class-এ ভাগ করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একজনের একটা কাজ।**
একটা restaurant-এ একজন chef, একজন waiter আর একজন cashier থাকেন। আপনি চাইবেন না একজনই তিনটা কাজ করুক — cashier-এর নিয়ম বদলালে রান্না ভেঙে পড়ুক, এটা কেউ চায় না।

**ধাপ ২ — নিয়ম ভাঙার উদাহরণ: একটা class অনেক কিছু করছে।**

```dart
// খারাপ: User data রাখছে, save-ও করছে, email-ও পাঠাচ্ছে — বদলানোর তিনটা কারণ
class User {
  String name;
  User(this.name);
  void saveToDatabase() {/* ... */}
  void sendWelcomeEmail() {/* ... */}
}
```

**ধাপ ৩ — সমাধান: দায়িত্ব অনুযায়ী ভাগ করুন।**

```dart
class User {
  final String name;
  User(this.name); // শুধু user-এর data রাখে
}

class UserRepository {
  void save(User user) {/* saving logic */}
}

class EmailService {
  void sendWelcome(User user) {/* email logic */}
}
```

এখন প্রতিটা class-এর বদলানোর কারণ একটাই।

**ধাপ ৪ — "বদলানোর একটাই কারণ" — এটাই আসল পরীক্ষা।**
SRP-কে "একটা method" হিসেবে পড়বেন না। পড়ুন "একটা দায়িত্ব / বদলানোর একটা কারণ" হিসেবে। একটা class-এ অনেক method থাকতে পারে, যদি সবগুলো একই কাজে লাগে।

**Interviewer কেন জিজ্ঞেস করে:** SRP হলো সবচেয়ে বেশি ব্যবহৃত SOLID নিয়ম। আর clean architecture-এর layer-গুলোর ভিত্তি।

**সাধারণ ভুল:** একটা "god class" বানানো, যেটা data রাখে, network-এ কথা বলে, আর UI-ও বানায়। অথবা অতিরিক্ত ভাগ করে কয়েক ডজন ছোট class বানিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"SRP-এর সাথে cohesion-এর সম্পর্ক কী?"* → SRP high cohesion দেয় — প্রতিটা class একটা জিনিসেই মনোযোগ দেয় ([Q9](#q9))।

**সম্পর্কিত:** [Q9 — cohesion](#q9) · [Q11 — OCP](#q11)

[↑ উপরে ফিরুন](#toc)

---

<a id="q11"></a>
## 11. SOLID — O: Open/Closed Principle (OCP)

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Class-গুলো extension-এর জন্য খোলা থাকবে, কিন্তু modification-এর জন্য বন্ধ। মানে নতুন behaviour যোগ করব নতুন code লিখে, পুরোনো tested code edit করে নয়। সাধারণ উপায় হলো একটা abstraction-এর উপর নির্ভর করা, আর নতুন implementation যোগ করা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা multiplug।**
নতুন device লাগাতে হলে নতুন socket-এ plug করে দেন — দেয়ালের তার নতুন করে টানেন না। নতুন behaviour যোগ হলো, পুরোনো তার অক্ষত থাকল।

**ধাপ ২ — নিয়ম ভাঙার উদাহরণ: প্রতিটা নতুন case-এর জন্য class edit করা।**

```dart
// খারাপ: নতুন প্রতিটা shape-এর জন্য এই method edit করতে হয়
double area(Object shape) {
  if (shape is Circle) return 3.14 * shape.r * shape.r;
  if (shape is Square) return shape.s * shape.s;
  // Triangle যোগ করবেন? আবার এই function EDIT করতেই হবে
  return 0;
}
```

**ধাপ ৩ — সমাধান: abstraction দিয়ে extend করুন।**

```dart
abstract class Shape { double area(); }
class Circle extends Shape { final double r; Circle(this.r); double area() => 3.14 * r * r; }
class Square extends Shape { final double s; Square(this.s); double area() => s * s; }

// Triangle যোগ করতে হলে নতুন একটা class ADD করুন — পুরোনো code বদলায় না।
class Triangle extends Shape { final double b, h; Triangle(this.b, this.h); double area() => 0.5 * b * h; }

double totalArea(List<Shape> shapes) =>
    shapes.fold(0, (sum, s) => sum + s.area()); // কখনোই edit লাগে না
```

**ধাপ ৪ — কেন এটা গুরুত্বপূর্ণ।**
Tested code edit করলে সেটা ভাঙার ঝুঁকি থাকে। নতুন code যোগ করলে (নতুন একটা class) পুরোনো, চলমান code-এ হাত পড়ে না। এটা বেশি নিরাপদ, আর extend করাও সহজ।

**Interviewer কেন জিজ্ঞেস করে:** এতে বোঝা যায় আপনি পরিবর্তনের কথা ভেবে design করেন। দীর্ঘদিন টিকে থাকা code-এ এটাই সবচেয়ে দামি গুণ।

**সাধারণ ভুল:** type-এর উপর বড় `if/else` বা `switch` chain, যা প্রতিবার নতুন case এলে বাড়তে থাকে — এটা OCP ভাঙার ক্লাসিক উদাহরণ।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"sealed class + switch কি নিয়ম ভাঙে না?"* → এটা একটা ভারসাম্যপূর্ণ trade-off: sealed class compile-time safety দেয় (কোনো case ভুলে যাওয়া যায় না), বিনিময়ে switch edit করতে হয়। দুই ধরনই বৈধ; set কত ঘন ঘন বদলায় সেটা দেখে বেছে নিন।

**সম্পর্কিত:** [Q10 — SRP](#q10) · [Q14 — DIP](#q14) · [Q5 — abstraction](#q5)

[↑ উপরে ফিরুন](#toc)

---

<a id="q12"></a>
## 12. SOLID — L: Liskov Substitution Principle (LSP)

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"যেকোনো subclass-কে তার parent-এর জায়গায় বসিয়ে দিলে কাজ চলতে হবে, কিছু ভাঙবে না। Parent-এর বদলে child বসালে যদি program উল্টাপাল্টা করে, তাহলে আপনি LSP ভেঙেছেন। সাধারণত এর মানে inheritance-টাই ভুল ছিল।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একজন stand-in অভিনেতা।**
মূল অভিনেতা যেখানে যেখানে অভিনয় করতেন, stand-in-কেও সেখানে সেই role করতে পারতে হবে। Stand-in যদি মৌলিক role-টাই করতে না পারেন, তাহলে বদলি দিয়ে show ভেঙে যায়।

**ধাপ ২ — ক্লাসিক নিয়ম ভাঙা: Square extends Rectangle।**
গণিতে square "is a" rectangle, কিন্তু code-এ এটা প্রত্যাশা ভেঙে দেয়:

```dart
class Rectangle {
  int width, height;
  Rectangle(this.width, this.height);
  int area() => width * height;
}

class Square extends Rectangle {
  Square(int size) : super(size, size);
  // কেউ যদি width আর height আলাদা করে set করে (Rectangle-এর জন্য বৈধ),
  // Square সেই প্রত্যাশা ভাঙে — width আর height সমান থাকতেই হবে।
}

void resizeAndCheck(Rectangle r) {
  r.width = 4;
  r.height = 5;
  assert(r.area() == 20); // r আসলে Square হলে FAILS
}
```

যে code `Rectangle`-এর জন্য কাজ করে, সেটাই `Square` দিলে ভেঙে যায় — এটাই LSP লঙ্ঘন।

**ধাপ ৩ — সমাধান: জোর করে খারাপ "is-a" বানাবেন না।**
`Square extends Rectangle` করবেন না। এর বদলে একটা common abstraction (`Shape`) ব্যবহার করুন, অথবা composition ব্যবহার করুন। শিক্ষা হলো: inheritance-কে parent-এর দেওয়া কথাগুলো রক্ষা করতে হবে।

**ধাপ ৪ — আরেকটা সাধারণ লক্ষণ।**
কোনো subclass যদি parent-এর method-এ "not supported" throw করে (যেমন একটা read-only list, যেটা `add`-এ throw করে), সেটাও LSP ভাঙে — সে সত্যিকার অর্থে parent-এর জায়গায় দাঁড়াতে পারে না।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি বোঝেন কি না যে inheritance একটা *প্রতিশ্রুতি*, শুধু code reuse নয়।

**সাধারণ ভুল:** শুধু field reuse করার জন্য inherit করা, তারপর method override করে সেগুলোকে ফাঁকা রাখা বা throw করানো। এতে substitution ভেঙে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Square/Rectangle-এর সমস্যাটা কীভাবে ঠিক করবেন?"* → `area()` সহ একটা `Shape` interface ব্যবহার করুন, আর Square ও Rectangle-কে আলাদা implementation বানান।

**সম্পর্কিত:** [Q3 — inheritance](#q3) · [Q11 — OCP](#q11) · [Q6 — composition](#q6)

[↑ উপরে ফিরুন](#toc)

---

<a id="q13"></a>
## 13. SOLID — I: Interface Segregation Principle (ISP)

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"যে method একটা class-এর দরকার নেই, সেটা implement করতে জোর করবেন না। একটা বিশাল মোটা interface-এর বদলে কয়েকটা ছোট, নির্দিষ্ট interface রাখুন। তাহলে একটা class শুধু সেই method-গুলোর উপর নির্ভর করে, যেগুলো সে আসলেই ব্যবহার করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: সহজ একটা menu।**
ছোট café-র menu ২০০ item-এর menu-র চেয়ে সহজ, যেখানে বেশিরভাগ জিনিস পাওয়াই যায় না। ছোট, নির্দিষ্ট interface ছোট menu-র মতো — যতটুকু দরকার শুধু ততটুকু নেবেন।

**ধাপ ২ — নিয়ম ভাঙার উদাহরণ: একটা মোটা interface।**

```dart
// খারাপ: প্রতিটা worker-কে এই সবগুলো implement করতেই হবে, দরকার না হলেও
abstract class Worker {
  void work();
  void eat();
  void sleep();
}

class Robot implements Worker {
  @override void work() {}
  @override void eat() {}   // robot খায় না — জোর করে fake করতে হচ্ছে
  @override void sleep() {} // robot ঘুমায় না — জোর করে fake করতে হচ্ছে
}
```

**ধাপ ৩ — সমাধান: ছোট ছোট interface-এ ভাগ করুন।**

```dart
abstract class Workable { void work(); }
abstract class Eatable  { void eat(); }

class Robot implements Workable {           // যতটুকু দরকার শুধু ততটুকু
  @override void work() {}
}
class Human implements Workable, Eatable {  // দুটোই নেয়
  @override void work() {}
  @override void eat() {}
}
```

**ধাপ ৪ — কেন এটা গুরুত্বপূর্ণ।**
মোটা interface ফাঁকা বা নকল method লিখতে বাধ্য করে। আর class-কে এমন জিনিসের সাথে জুড়ে দেয়, যা সে ব্যবহারই করে না। ফলে অব্যবহৃত একটা method বদলালেও তার ধাক্কা ছড়িয়ে পড়তে পারে। ছোট interface নির্ভরতা আঁটসাঁট রাখে।

**Interviewer কেন জিজ্ঞেস করে:** এতে বোঝা যায় আপনি হালকা contract design করেন। এতে code decoupled থাকে আর mock করা সহজ হয়।

**সাধারণ ভুল:** ২০টা method-ওয়ালা একটা বিশাল "service" interface, যেটা সবাই আংশিকভাবে implement করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা SRP-র সাথে কীভাবে সম্পর্কিত?"* → ISP হলো interface-এ প্রয়োগ করা SRP — প্রতিটা interface-এর একটাই নির্দিষ্ট উদ্দেশ্য থাকে।

**সম্পর্কিত:** [Q10 — SRP](#q10) · [Q5 — interfaces](#q5)

[↑ উপরে ফিরুন](#toc)

---

<a id="q14"></a>
## 14. SOLID — D: Dependency Inversion Principle (DIP)

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"High-level code abstraction-এর উপর নির্ভর করবে, কোনো concrete detail-এর উপর নয়। কোনো class নিজের ভেতরে নিজেই database বা API client বানাবে না; বাইরে থেকে একটা interface পাবে। এতে code নমনীয় আর testable হয় — class না বদলে আসলটার জায়গায় নকল বসানো যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: দেয়ালের socket।**
আপনার lamp সরাসরি power station-এ তার দিয়ে জোড়া লাগে না। এটা একটা standard socket-এ (একটা interface) plug হয়। Lamp-টা আপনি যেকোনো socket-এ নিতে পারেন। DIP মানে "socket-এর উপর নির্ভর করুন, power station-এর উপর নয়।"

**ধাপ ২ — নিয়ম ভাঙার উদাহরণ: concrete detail-এর উপর নির্ভর করা।**

```dart
// খারাপ: high-level OrderService একটা নির্দিষ্ট API class-এর সাথে আটকানো
class OrderService {
  final api = HttpApiClient(); // hard-wired — swap বা fake করা যায় না
  void placeOrder() => api.post('/order');
}
```

**ধাপ ৩ — সমাধান: abstraction-এর উপর নির্ভর করুন, সেটা inject করুন।**

```dart
abstract class ApiClient {       // abstraction (সেই "socket")
  void post(String path);
}

class OrderService {
  final ApiClient api;           // interface-এর উপর নির্ভর করে, class-এর উপর নয়
  OrderService(this.api);        // বাইরে থেকে inject করা
  void placeOrder() => api.post('/order');
}

// আসল app:
OrderService(HttpApiClient());
// Test:
OrderService(FakeApiClient());   // test করা সহজ, আসল network লাগে না
```

**ধাপ ৪ — "inversion" কেন?**
সাধারণত high-level code নিজেই low-level detail তৈরি করত। DIP সেটাকে *উল্টে* দেয়: দুই পক্ষই মাঝখানের একটা abstraction-এর উপর নির্ভর করে। Flutter-এ `get_it` আর `injectable`-এর মতো dependency injection tool ঠিক এই কাজটাই করে।

**Interviewer কেন জিজ্ঞেস করে:** DIP হলো testable, layered architecture-এর মেরুদণ্ড — এটা শক্ত senior signal।

**সাধারণ ভুল:** class-এর ভেতরে `new`/constructor দিয়ে dependency তৈরি করা (hard-wired)। এর বদলে সেগুলো inject করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"DIP আর dependency injection-এর পার্থক্য?"* → DIP হলো নীতি (abstraction-এর উপর নির্ভর করা)। DI হলো কৌশল (সেগুলো ভেতরে পাঠানো, প্রায়ই `get_it` দিয়ে)।
- *"এটা testing-এ কীভাবে সাহায্য করে?"* → আপনি একটা fake implementation inject করেন। ফলে আসল network বা database ছাড়াই test চলে।

**সম্পর্কিত:** [Q9 — low coupling](#q9) · [Q11 — OCP](#q11) · [Q5 — abstraction](#q5)

[↑ উপরে ফিরুন](#toc)

---

# D. আরও কিছু গুরুত্বপূর্ণ principle

---

<a id="q15"></a>
## 15. DRY principle কী?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"DRY মানে Don't Repeat Yourself — প্রতিটা knowledge-এর একটাই জায়গা থাকা উচিত। একই logic যদি কয়েক জায়গায় copy-paste করা থাকে, তাহলে একটা পরিবর্তন মানে সব জায়গায় ঠিক করা, আর একটা জায়গা ভুলে যাওয়া। তাই আমি পুনরাবৃত্তি হওয়া logic একটা function বা class-এ নিয়ে আসি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা violation: copy-paste করা logic।**

```dart
// খারাপ: একই discount-এর হিসাব বারবার
double priceA(double p) => p - (p * 0.1);
double priceB(double p) => p - (p * 0.1); // rate বদলাবেন? দুই জায়গায় ঠিক করতে হবে
```

**ধাপ ২ — সমাধান: একটাই source of truth।**

```dart
double applyDiscount(double price, double rate) => price - (price * rate);
// নিয়ম একবার বদলান, সব জায়গায় update হয়ে যাবে।
```

**ধাপ ৩ — সাবধানতা: DRY knowledge নিয়ে, শুধু text নিয়ে নয়।**
দুই টুকরো code এখন *দেখতে* এক লাগছে বলেই সেগুলো এক করে দেবেন না। যদি সেগুলো আলাদা নিয়ম বোঝায়, আর আজ কাকতালীয়ভাবে মিলে যায়, তাহলে জোর করে এক করলে আরও খারাপ coupling তৈরি হয়। DRY মানে duplicate *knowledge* সরানো, দেখতে এক রকম line সরানো নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা মৌলিক মানের অভ্যাস। তাঁরা দেখতে চান আপনি পুনরাবৃত্তি সঠিক উপায়ে সরান কি না।

**সাধারণ ভুল:** DRY বেশি প্রয়োগ করা — শুধু দেখতে এক রকম বলে সম্পর্কহীন code এক করে ফেলা, আর একটা জট পাকানো shared function তৈরি করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"DRY vs WET?"* → WET = "Write Everything Twice" (উল্টোটা)। অল্প duplication মাঝে মাঝে ঠিক আছে; খুব আগেভাগে এক করে ফেলা ক্ষতি করতে পারে।

**সম্পর্কিত:** [Q16 — KISS](#q16) · [Q10 — SRP](#q10)

[↑ উপরে ফিরুন](#toc)

---

<a id="q16"></a>
## 16. KISS principle কী?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"KISS মানে Keep It Simple, Stupid — যে সমাধান কাজ করে, তার মধ্যে সবচেয়ে সহজটা বেছে নিন। চালাক আর জটিল code পড়া, test করা আর বদলানো কঠিন। জটিলতা যোগ করার সত্যিকারের কারণ না থাকলে আমি সাদামাটা, পরিষ্কার version-টাই নিই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা violation: চালাক কিন্তু পড়া যায় না।**

```dart
// খারাপ: এক নজরে পড়ার জন্য বেশি চালাক
bool isEven(int n) => (n & 1) == 0 ? true : false;
```

**ধাপ ২ — সমাধান: সাদামাটা আর পরিষ্কার।**

```dart
bool isEven(int n) => n % 2 == 0;
```

দুটোই কাজ করে, কিন্তু দ্বিতীয়টা সাথে সাথে পড়া যায়। সহজ code নিজেই একটা feature।

**ধাপ ৩ — KISS কোথায় সবচেয়ে বেশি দরকার।**
- এখনো দরকার নেই এমন layer, pattern বা abstraction যোগ করবেন না।
- কেউ পড়তে পারে না এমন চালাক one-liner-এর বদলে পরিষ্কার `if` ব্যবহার করুন।
- একজন junior-এর আপনার code বোঝা উচিত।

**Interviewer কেন জিজ্ঞেস করে:** Senior engineer-রা চালাকির চেয়ে স্পষ্টতাকে বেশি মূল্য দেন। KISS পরিপক্বতা দেখায়।

**সাধারণ ভুল:** Over-engineering — "যদি লাগে" ভেবে design pattern আর indirection যোগ করা, আর সহজ জিনিসকে জটিল করে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"KISS vs YAGNI?"* → KISS = সমাধানটা সহজ রাখুন। YAGNI = এখনো দরকার নেই এমন জিনিস বানাবেন না ([Q17](#q17))। দুটো একসাথে কাজ করে।

**সম্পর্কিত:** [Q17 — YAGNI](#q17) · [Q15 — DRY](#q15)

[↑ উপরে ফিরুন](#toc)

---

<a id="q17"></a>
## 17. YAGNI principle কী?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"YAGNI মানে You Aren't Gonna Need It — সত্যি দরকার না হওয়া পর্যন্ত feature বা flexibility বানাবেন না। কল্পনার ভবিষ্যৎ চাহিদার জন্য লেখা code প্রায়ই ভুল হয়, ব্যবহারই হয় না, আর শুধু maintain করার বাড়তি বোঝা হয়ে থাকে। আজকের আসল প্রয়োজনের জন্য বানান।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের একটা ছবি।**
একদিন বড় পরিবার *হতে পারে* বলে ১০ সিটের van কিনবেন না। এখন যা দরকার তাই কিনুন; প্রয়োজন সত্যি হলে upgrade করুন।

**ধাপ ২ — একটা Flutter উদাহরণ।**

```dart
// খারাপ (YAGNI violation): ৫টা payment provider-এর support বানানো
// যখন app-এর আজ একটাই দরকার, "যদি লাগে" ভেবে।

// ভালো: এখন যেটা দরকার সেটাই বানান, একটা সহজ interface-এর পেছনে
abstract class PaymentGateway { Future<void> pay(double amount); }
class BkashGateway implements PaymentGateway {
  @override
  Future<void> pay(double amount) async {/* আজ যতটুকু দরকার শুধু ততটুকু */}
}
// পরে আরও gateway যোগ করুন, যখন সত্যিকারের প্রয়োজন আসবে।
```

**ধাপ ৩ — কেন এটা গুরুত্বপূর্ণ।**
অনুমানের উপর বানানো feature বানাতে, test করতে আর maintain করতে সময় লাগে — আর সেগুলো সাধারণত ভুল হয়, কারণ আপনি ভবিষ্যৎ অনুমান করেছেন। YAGNI codebase-কে হালকা আর লক্ষ্যে স্থির রাখে।

**ধাপ ৪ — ভারসাম্য।**
YAGNI মানে "যেমন তেমন code লেখা" নয়। এর মানে *অপ্রয়োজনীয়* flexibility যোগ না করা। আপনি তবুও পরিষ্কার, সহজ code design করবেন (KISS)। সেটা প্রয়োজন এলে সহজে বাড়ানো যাবে (OCP)।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি আসল প্রয়োজনে মন দেন আর over-engineering এড়ান — দ্রুত চলা team-এ এটা মূল্যবান।

**সাধারণ ভুল:** কখনো না আসা প্রয়োজনের জন্য বিশাল "configurable" system বানানো, আর delivery ধীর করে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"YAGNI vs designing for change?"* → Code পরিষ্কার আর extensible রাখুন (OCP), কিন্তু কেউ চায়নি এমন নির্দিষ্ট feature আগেভাগে বানাবেন না।

**সম্পর্কিত:** [Q16 — KISS](#q16) · [Q11 — OCP](#q11)

[↑ উপরে ফিরুন](#toc)

---

# E. Dart OOP-এর খুঁটিনাটি

---

<a id="q18"></a>
## 18. Dart-এ কী কী ধরনের constructor আছে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart-এ default (generative) constructor আছে, যেটা সবসময় নতুন object বানায়। named constructor আছে, যেটা object বানানোর দ্বিতীয় একটা স্পষ্ট নামের উপায়। factory constructor আছে, যেটা cache করা object বা একটা subtype ফেরত দিতে পারে। আর const constructor আছে, যেটা compile time-এ object বানায়। কোলনের পরের অংশ, মানে initializer list, body চলার আগেই final field-গুলো set করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Default আর named constructor।**

```dart
class User {
  final String id;
  final String name;
  User(this.id, this.name);                 // default (generative)
  User.guest() : id = '0', name = 'Guest';  // named
}
```

**ধাপ ২ — Factory constructor — নতুন object বানাতেই হবে এমন নয়।**
এটা cache করা instance, একটা subtype, বা parse করার ফলাফল ফেরত দিতে পারে।

```dart
class User {
  final String id, name;
  User(this.id, this.name);
  factory User.fromJson(Map<String, dynamic> j) => User(j['id'], j['name']);
}
```

**ধাপ ৩ — const constructor — compile time-এ তৈরি হয়।**
সব field অবশ্যই `final` হতে হবে; সমান const object memory-তে ভাগ করে ব্যবহার হয় (Flutter widget-এর performance-এর জন্য ভালো)।

```dart
class Point {
  final int x, y;
  const Point(this.x, this.y);
}
const a = Point(1, 2); // compile-time constant হতে পারে
```

**ধাপ ৪ — Initializer list।**
`:`-এর পরের code body-র আগে চলে। `final` field set করা আর `super` call করার একমাত্র জায়গা এটাই।

```dart
class Circle {
  final double radius;
  Circle(double d) : radius = d / 2; // initializer list
}
```

**Interviewer কেন জিজ্ঞেস করে:** Constructor সারাক্ষণই ব্যবহার হয় (প্রতিটা `fromJson`)। তাঁরা দেখেন আপনি factory-র বিশেষ ক্ষমতা আর const-এর performance সুবিধা জানেন কি না।

**সাধারণ ভুল:** ভাবা যে factory সবসময় নতুন object বানায় — সেটা বাধ্যতামূলক নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`fromJson` কেন একটা factory?"* → কারণ এটা fail করতে পারে, cache করা object ফেরত দিতে পারে, বা একটা subtype ফেরত দিতে পারে — সাধারণ constructor সেটা পারে না।

**সম্পর্কিত:** [Q8 — class vs object](#q8) · [Q2 — encapsulation](#q2)

[↑ উপরে ফিরুন](#toc)

---

<a id="q19"></a>
## 19. Dart-এ `static` member কখন আর কেন ব্যবহার করবেন?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা `static` member class-এর নিজের, কোনো একটা object-এর নয়। আমি এটা ব্যবহার করি shared constant-এর জন্য, এমন utility/helper function-এর জন্য যেগুলোর instance data লাগে না, আর factory-ধরনের helper-এর জন্য। এটা class-এর নাম দিয়ে call করি, instance দিয়ে নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Static = পুরো class মিলে ভাগ করে নেওয়া।**
সাধারণ field প্রতিটা object-এর নিজের। `static` field class-এর — শুধু একটাই copy থাকে, সবাই সেটাই ভাগ করে নেয়।

```dart
class AppConfig {
  static const String baseUrl = 'https://api.example.com'; // একটাই shared value
  static int requestCount = 0;                              // একটাই shared counter
}

print(AppConfig.baseUrl);   // class দিয়ে call, instance দিয়ে নয়
AppConfig.requestCount++;    // পুরো app জুড়ে shared
```

**ধাপ ২ — Static method — যেসব utility-র কোনো object লাগে না।**

```dart
class MathUtils {
  static int square(int n) => n * n; // কোনো instance data লাগে না
}
print(MathUtils.square(5)); // 25
```

**ধাপ ৩ — কখন ব্যবহার করবেন।**
- পুরো app-জুড়ে থাকা **constant** (`static const`)।
- এমন **helper/utility** function, যেগুলো instance field ছোঁয় না।
- সব instance মিলে ভাগ করে নেওয়া **counter বা cache**।

**ধাপ ৪ — কখন ব্যবহার করবেন না।**
Static থাকলে code test আর mock করা কঠিন হয়ে যায় (একটা static call-কে সহজে fake দিয়ে বদলানো যায় না)। আসল dependency-র জন্য (database, API) static নয় — DIP দিয়ে inject করা instance ব্যবহার করুন ([Q14](#q14))।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখেন আপনি class-level আর instance-level-এর পার্থক্য জানেন কি না। আরও দেখেন আপনি static-এর অতিরিক্ত ব্যবহার করেন কি না (যেটা testability নষ্ট করে)।

**সাধারণ ভুল:** business logic আর dependency static method-এ রেখে দেওয়া। এতে test-এ code mock করা অসম্ভব হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"static vs singleton?"* → static class shared, কিন্তু সেটা interface implement করতে পারে না, inject-ও করা যায় না। Singleton একটা object, যেটা দুটোই পারে। যে service mock করতে হতে পারে, তার জন্য singleton ভালো।

**সম্পর্কিত:** [Q14 — DIP (কঠিন static এড়ান)](#q14) · [Q18 — constructor](#q18)

[↑ উপরে ফিরুন](#toc)

---

<a id="q20"></a>
## 20. Dart-এ covariance আর contravariance কী?

> Deeper · Hard · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q20)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Covariance মানে যেখানে general type চাওয়া হয়েছে, সেখানে আরও specific type ব্যবহার করা যায় — যেমন একটা `List<Cat>`-কে `List<Animal>` হিসেবে ধরা যায়। Dart-এর generics ডিফল্টে covariant, যেটা সুবিধাজনক কিন্তু একটু অনিরাপদ। তাই Dart runtime check যোগ করে দেয়। `covariant` keyword দিয়ে override-এ ইচ্ছা করে parameter type সরু করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি।**
একটা recipe-তে যদি "ফল" চাওয়া হয়, তাহলে "আপেল" (আরও specific) দিলে চলে — এটাই covariance (general-এর জায়গায় specific)। উল্টোটা (যেখানে "আপেল" লাগবে সেখানে "খাবার" দেওয়া) হলো contravariance, আর সেটা সাধারণত নিরাপদ নয়।

**ধাপ ২ — Dart-এর generics covariant।**

```dart
class Animal {}
class Cat extends Animal {}

List<Cat> cats = [Cat()];
List<Animal> animals = cats; // allowed — covariant
```

এটা কাজে লাগে, কিন্তু কারিগরিভাবে অনিরাপদ (আপনি `animals`-এ একটা `Dog` add করার চেষ্টা করতে পারেন, যেটা আসলে `Cat`-এর list)। Dart একটা runtime check বসিয়ে দেয় সেটা ধরার জন্য। ফলে জিনিসটা নিরাপদ থাকে, তবে দাম হলো একটা সম্ভাব্য runtime error।

**ধাপ ৩ — `covariant` keyword (parameter সরু করা)।**
সাধারণত একটা override-কে একই বা আরও চওড়া parameter type নিতে হয়। `covariant` আপনাকে আরও সরু type নিতে দেয়, বিনিময়ে একটা runtime check মেনে নিতে হয়।

```dart
class Animal {}
class Cat extends Animal {}

class Vet {
  void treat(Animal a) {}
}
class CatVet extends Vet {
  @override
  void treat(covariant Cat a) {} // Cat-এ সরু করা — Dart একটা runtime check যোগ করে
}
```

**ধাপ ৪ — বাস্তবে এটার সাথে কখন দেখা হয়।**
বেশিরভাগ developer নিজের হাতে `covariant` খুব কমই লেখেন। এটা দেখা যায় advanced generic API আর কিছু framework code-এ। বেশিরভাগ interview-র জন্য ধারণাটা জানাই (general-এর জায়গায় specific) যথেষ্ট।

**Interviewer কেন জিজ্ঞেস করে:** এটা "আপনি type system-এর গভীর কোণাগুলো জানেন কি না?" ধরনের প্রশ্ন। শক্ত senior-দের আলাদা করতে এটা ব্যবহার হয়।

**সাধারণ ভুল:** দিক গুলিয়ে ফেলা — covariance মানে general-এর জায়গায় specific (Animal চাওয়া হলে Cat)। Contravariance ঠিক উল্টোটা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Dart-এর covariance কি নিরাপদ?"* → বেশিরভাগ ক্ষেত্রেই হ্যাঁ। compile time-এ যে অনিরাপদ কেসগুলো ফসকে যায়, সেগুলো ধরতে Dart runtime check যোগ করে।

**সম্পর্কিত:** [Q4 — polymorphism](#q4) · [Q3 — inheritance](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q21"></a>
## 21. Dart-এ method overriding আর method hiding-এর পার্থক্য কী?

> Deeper · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-12-oop-principles.md#q21)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Overriding subclass-এ একটা instance method-কে বদলে দেয়, আর object-এর আসল type ঠিক করে runtime-এ কোন version চলবে — এটাই সত্যিকারের polymorphism। Method 'hiding' হয় static method-এর ক্ষেত্রে: সেগুলো class-এর, object-এর নয়। তাই subclass-এর static method শুধু নামে parent-এরটাকে ঢেকে দেয় — এখানে কোনো runtime dispatch নেই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Overriding (instance method) — runtime ঠিক করে।**

```dart
class Animal {
  void speak() => print('some sound');
}
class Dog extends Animal {
  @override
  void speak() => print('woof'); // override করে
}

Animal a = Dog();
a.speak(); // 'woof' — আসল type (Dog) runtime-এ ঠিক করে
```

এটাই polymorphism: variable-এর type `Animal` হওয়া সত্ত্বেও `Dog`-এর version চলে।

**ধাপ ২ — Hiding (static method) — type ঠিক করে, কোনো polymorphism নেই।**
Static method class-এর নিজের। Parent আর child দুজনেই যদি একই নামে static method লেখে, তাহলে কোনটা ব্যবহার হবে সেটা নির্ভর করে আপনি কোন class-এর নাম লিখেছেন তার উপর — এখানে কোনো runtime dispatch নেই।

```dart
class Parent {
  static void hello() => print('parent');
}
class Child extends Parent {
  static void hello() => print('child'); // hide করে, override নয়
}

Parent.hello(); // 'parent'
Child.hello();  // 'child' — class-এর নাম দিয়ে বাছা হয়, object দিয়ে নয়
```

**ধাপ ৩ — মূল পার্থক্য।**
- **Override** → instance method, object-এর আসল type দিয়ে runtime-এ ঠিক হয় (polymorphism)।
- **Hide** → static method (আর field shadowing), declare করা class/type দিয়ে ঠিক হয়, object দিয়ে নয়।

**ধাপ ৪ — Field shadowing-ও একইরকম।**
Subclass যদি parent-এর সমান নামে একটা field declare করে, তাহলে সেটা ঢেকে দেয়। এটা declare করা type দিয়ে access হয়, method-এর মতো polymorphic নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা পরীক্ষা করে আপনি সত্যিই বোঝেন কি না যে polymorphism instance method-এ খাটে, static-এ নয়।

**সাধারণ ভুল:** static method-কে polymorphic (override করা যায়) ভাবা। সেগুলো নয় — সেগুলো class-এর নাম দিয়ে resolve হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"static method কি override করা যায়?"* → না। Static method hide/shadow হয়, override হয় না।

**সম্পর্কিত:** [Q4 — polymorphism](#q4) · [Q19 — static member](#q19) · [Q3 — overriding](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (শেষ রাতের রিভিশন)

Interview-র দিন সকালে এটা পড়ুন। আগে table, তারপর এক-লাইনের মনে করিয়ে দেওয়া কথাগুলো।

## চারটি স্তম্ভ

| Pillar | মানে | মনে রাখুন |
|---|---|---|
| Encapsulation | data লুকান, নিরাপদ API খোলা রাখুন | ওষুধের capsule |
| Abstraction | কী দেখান, কীভাবে লুকান | engine না জেনেই গাড়ি চালানো |
| Inheritance | parent-এর code আবার ব্যবহার | সন্তান আর বাবা-মা |
| Polymorphism | এক কাজ, অনেক রূপ | যেকোনো shape-এর জন্য "draw()" |

## SOLID — প্রতিটা এক লাইনে

| Letter | Principle | এক লাইনে |
|---|---|---|
| S | Single Responsibility | এক class, বদলানোর একটাই কারণ |
| O | Open/Closed | নতুন code যোগ করুন, পুরোনো code বদলাবেন না |
| L | Liskov Substitution | parent যেখানে চলে, child-কে সেখানেই চলতে হবে |
| I | Interface Segregation | অনেক ছোট interface, একটা মোটা নয় |
| D | Dependency Inversion | abstraction-এর উপর নির্ভর করুন, সেগুলো inject করুন |

## Composition vs inheritance

| | Inheritance | Composition |
|---|---|---|
| সম্পর্ক | "is-a" | "has-a" |
| নমনীয়তা | শক্ত tree | বদলে নেওয়া যায় এমন টুকরো |
| কখন বেছে নেবেন | সত্যিকারের, স্থির is-a | behaviour আবার ব্যবহার |

## এক লাইনের মনে রাখার তালিকা

- **Encapsulation** = private field (`_`) + নিরাপদ method যা validate করে। ([Q2](#q2))
- **Inheritance** = `extends` (একটাই parent), বদলাতে `@override`, উপরে call করতে `super`। ([Q3](#q3))
- **Polymorphism** = একই call, ভিন্ন আচরণ; Dart-এ method overloading নেই। ([Q4](#q4))
- **Abstraction**: `abstract class` (code শেয়ার করে, `extends`) বনাম interface (`implements`, শুধু contract)। ([Q5](#q5))
- **Inheritance-এর বদলে composition বেছে নিন** — গভীর "is-a" tree-এর চেয়ে "has-a" বেশি নমনীয়। ([Q6](#q6))
- **Low coupling + high cohesion** = বদলানো, test করা, reuse করা সহজ। ([Q9](#q9))
- **SRP** = বদলানোর একটাই কারণ; **OCP** = extend করতে খোলা, modify করতে বন্ধ। ([Q10](#q10), [Q11](#q11))
- **LSP** = subclass-কে parent-এর জায়গায় বসানো যেতে হবে; **ISP** = ছোট interface। ([Q12](#q12), [Q13](#q13))
- **DIP** = abstraction-এর উপর নির্ভর করুন, সেগুলো inject করুন (testable code-এর ভিত্তি)। ([Q14](#q14))
- **DRY** (সত্যের একটাই উৎস), **KISS** (সহজ রাখুন), **YAGNI** (এখনো দরকার নেই এমন জিনিস বানাবেন না)। ([Q15](#q15), [Q16](#q16), [Q17](#q17))
- **Factory** constructor cache করা object বা subtype return করতে পারে; **static** class-এর নিজের জিনিস। ([Q18](#q18), [Q19](#q19))
- **Override** = instance method, runtime dispatch; **hiding** = static, class-এর নাম দিয়ে। ([Q21](#q21))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer-রা কীভাবে গভীরে যান

Interviewer-রা OOP প্রশ্নগুলো concept থেকে design পর্যন্ত চেইন করে জিজ্ঞেস করেন। মুখে বলে অনুশীলন করুন:

1. *"SRP কী?"* → একটা class, বদলানোর একটাই কারণ।
2. *"একটা violation দেখান।"* → একটা `User` class যেটা DB-তে save-ও করে আর email-ও পাঠায়।
3. *"এটা ঠিক করুন।"* → ভাগ করে ফেলুন `User`, `UserRepository`, `EmailService`-এ।
4. *"এখন repository আসল database ব্যবহার করে — আপনি এটা test করবেন কীভাবে?"* → একটা `Database` abstraction-এর উপর নির্ভর করুন আর একটা fake inject করুন (এটাই DIP)।
5. *"এটা ভালো কেন?"* → low coupling: `UserRepository`-তে হাত না দিয়েই আপনি database বদলাতে বা mock করতে পারবেন।

একটা principle → একটা violation → একটা fix → testing — এই পথে সহজভাবে এগোনোই সেই senior signal, যেটা interviewer-রা খোঁজেন। remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

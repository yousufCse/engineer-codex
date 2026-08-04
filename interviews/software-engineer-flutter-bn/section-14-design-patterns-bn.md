# Section 14 — Design Patterns (Gang of Four)

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন। সব উদাহরণ Dart-এ, সাথে বাস্তব Flutter use case।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-14-design-patterns.md](../software-engineer-flutter/section-14-design-patterns.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা pattern-এর গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — এটা কোন সমস্যা সমাধান করে, কীভাবে কাজ করে (Dart code সহ), আর একটা বাস্তব Flutter use case।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত pattern-এ যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা pattern-এ tag দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** প্রতিটা pattern-এর ক্ষেত্রে আগে বলুন *এটা কোন সমস্যা সমাধান করে*, তারপর এক লাইনে একটা বাস্তব উদাহরণ। Pattern-এর নাম বলা সহজ; *কখন* ব্যবহার করবেন সেটা ব্যাখ্যা করাই senior-এর লক্ষণ।

---


## <a id="toc"></a>সূচিপত্র

**A. Creational patterns** (object কীভাবে তৈরি হয়)
1. [Singleton](#q1) · *Very common*
2. [Factory Method](#q2) · *Very common*
3. [Abstract Factory](#q3) · *Common*
4. [Builder](#q4) · *Common*

**B. Structural patterns** (object কীভাবে জোড়া লাগে)
5. [Adapter](#q5) · *Common*
6. [Decorator](#q6) · *Common*
7. [Facade](#q7) · *Common*
8. [Proxy](#q8) · *Deeper*
9. [Composite](#q9) · *Common*

**C. Behavioral patterns** (object কীভাবে কথা বলে আর আচরণ করে)
10. [Observer](#q10) · *Very common*
11. [Strategy](#q11) · *Very common*
12. [Command](#q12) · *Common*
13. [State](#q13) · *Common*
14. [Template Method](#q14) · *Common*
15. [Iterator](#q15) · *Common*

**Quick links:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

এই পর্যায়গুলো ধরে এগোন। একটা পর্যায় তখনই শেষ ধরুন, যখন না দেখে **সংক্ষিপ্ত উত্তর** আর একটা বাস্তব Flutter উদাহরণ বলতে পারবেন।

**পর্যায় ১ — যেগুলো অবশ্যই জানতে হবে (এখান থেকে শুরু)।** সবচেয়ে বেশি জিজ্ঞেস করা হয়।
→ [Q1 Singleton](#q1) · [Q2 Factory Method](#q2) · [Q10 Observer](#q10) · [Q11 Strategy](#q11)

**পর্যায় ২ — বাকি creational আর structural।**
→ [Q4 Builder](#q4) · [Q5 Adapter](#q5) · [Q6 Decorator](#q6) · [Q7 Facade](#q7)

**পর্যায় ৩ — বাকি behavioral।**
→ [Q12 Command](#q12) · [Q13 State](#q13) · [Q14 Template Method](#q14) · [Q15 Iterator](#q15)

**পর্যায় ৪ — আরও গভীর যেগুলো।**
→ [Q3 Abstract Factory](#q3) · [Q8 Proxy](#q8) · [Q9 Composite](#q9)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** এই ছয়টা দেখে নিন:
[Q1](#q1) · [Q2](#q2) · [Q6](#q6) · [Q10](#q10) · [Q11](#q11) · [Q13](#q13), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Creational patterns

---

## <a id="q1"></a>1. Singleton

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Singleton নিশ্চিত করে যে পুরো app-এ একটা class-এর মাত্র একটাই instance থাকবে। আর সেটাতে পৌঁছানোর একটাই জায়গা দেয়। Dart-এ আমি একটা factory constructor ব্যবহার করি, যেটা সবসময় একই private instance ফেরত দেয়। Config store বা service locator-এর মতো shared service-এর জন্য এটা ভালো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
কিছু জিনিস একবারই থাকা উচিত — একটা app config, একটা database connection, একটা logger। Singleton সেটা নিশ্চিত করে। আর যেকোনো code একই instance-এ পৌঁছাতে পারে।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
class AppConfig {
  static final AppConfig _instance = AppConfig._internal(); // একটাই instance
  AppConfig._internal();                  // private constructor
  factory AppConfig() => _instance;       // সবসময় একই জিনিস ফেরত দেয়

  String baseUrl = 'https://api.example.com';
}

void main() {
  print(identical(AppConfig(), AppConfig())); // true — একই object
}
```

**ধাপ ৩ — বাস্তব Flutter use case।**
`GetIt` (service locator) নিজেই একটা singleton। আর `SharedPreferences.getInstance()` একটাই shared instance ফেরত দেয়। App-wide logger বা analytics service-এও এটা দেখবেন।

**Dart isolate নিয়ে একটা সাবধানতা:** singleton প্রতি isolate-এ একটা। আপনি আরেকটা isolate spawn করলে, সেটা নিজের আলাদা instance পাবে (shared memory নেই)।

**Interviewer কেন জিজ্ঞেস করে:** এটা সবচেয়ে পরিচিত pattern। আর Dart-এর factory constructor-এর দ্রুত একটা পরীক্ষা।

**সাধারণ ভুল:** সব কিছুর জন্য singleton ব্যবহার করা (global state)। এতে code test করা কঠিন হয়ে যায়, আর লুকানো dependency তৈরি হয়। বরং dependency inject করা ভালো ([DI](#q2))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Dart-এ এটা কি thread-safe?"* → একটা isolate-এর ভেতরে হ্যাঁ — Dart single-threaded, তাই `static final` init নিরাপদ। আলাদা isolate-এ প্রত্যেকের নিজের copy থাকে।
- *"Global singleton test-এর জন্য খারাপ কেন?"* → এটাকে fake দিয়ে বদলানো কঠিন; inject করা dependency mock করা সহজ।

**সম্পর্কিত:** [Q2 — Factory Method](#q2) · [Q7 — Facade](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Factory Method

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Factory Method এমন একটা method দেয়, যেটা ঠিক করে কোন object তৈরি হবে আর সেটা ফেরত দেয়। ফলে caller সরাসরি constructor ব্যবহার করে না। Input অনুযায়ী আলাদা আলাদা subtype ফেরত দেওয়া যায়, আর caller concrete class-টা জানে না। Dart-এ `factory` constructor আর `fromJson` হলো রোজকার উদাহরণ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
কখনো কখনো ঠিক কোন class তৈরি হবে সেটা input বা শর্তের উপর নির্ভর করে। Caller-রা `if/else` লিখে class বাছুক — সেটা আপনি চান না। তাই ওই সিদ্ধান্তটা একটা method-এর পেছনে লুকিয়ে রাখুন।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class Button {
  void render();
}
class AndroidButton extends Button {
  @override void render() => print('Material button');
}
class IosButton extends Button {
  @override void render() => print('Cupertino button');
}

class ButtonFactory {
  static Button create(String platform) {
    return platform == 'ios' ? IosButton() : AndroidButton(); // সিদ্ধান্ত লুকানো
  }
}

ButtonFactory.create('ios').render(); // caller concrete class জানে না
```

**ধাপ ৩ — বাস্তব Flutter use case।**
`User.fromJson(...)` একটা factory method — এটা ঠিক করে data থেকে object কীভাবে বানানো হবে, আর একটা subtype-ও ফেরত দিতে পারে। Platform অনুযায়ী widget ফেরত দেওয়া (Material vs Cupertino) আরেকটা উদাহরণ।

**Interviewer কেন জিজ্ঞেস করে:** Dart-এ এটা সব জায়গায় আছে (`factory`, `fromJson`)। আর এটা দেখে আপনি object তৈরি লুকাতে পারেন কি না।

**সাধারণ ভুল:** একে Abstract Factory-র সাথে গুলিয়ে ফেলা। Factory Method *একটা* product বানায়; Abstract Factory সম্পর্কিত product-এর *পরিবার* বানায় ([Q3](#q3))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Factory method vs constructor?"* → Constructor সবসময় ওই class-টাই বানায়; factory method একটা subtype, একটা cache করা object ফেরত দিতে পারে, বা runtime-এ সিদ্ধান্ত নিতে পারে।

**সম্পর্কিত:** [Q3 — Abstract Factory](#q3) · [Q1 — Singleton](#q1) · [Q4 — Builder](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. Abstract Factory

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Abstract Factory সম্পর্কিত object-এর পুরো *পরিবার* তৈরি করে, যেগুলো একসাথে ব্যবহারের জন্য বানানো। এতে concrete class-এর নাম বলতে হয় না। একটা পরিচিত উদাহরণ হলো UI kit: light-theme factory light button আর light text field বানায়, আর dark-theme factory dark version বানায় — এরা সবসময় মিলে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
যখন কয়েকটা সম্পর্কিত product থাকে যেগুলো মিলতে হবে (সব light-themed, বা সব iOS-styled), তখন প্রতিটা আলাদা করে বাছতে চাইবেন না। কারণ মিশে যাওয়ার ঝুঁকি থাকে। একটা factory মিলে যাওয়া একটা সেট বানিয়ে দেয়।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class Button {}
abstract class Checkbox {}

abstract class UIFactory {            // abstract factory
  Button createButton();
  Checkbox createCheckbox();
}

class LightFactory implements UIFactory {
  @override Button createButton() => LightButton();
  @override Checkbox createCheckbox() => LightCheckbox();
}
class DarkFactory implements UIFactory {
  @override Button createButton() => DarkButton();
  @override Checkbox createCheckbox() => DarkCheckbox();
}

class LightButton implements Button {}
class LightCheckbox implements Checkbox {}
class DarkButton implements Button {}
class DarkCheckbox implements Checkbox {}

void buildUI(UIFactory factory) {
  factory.createButton();   // সবসময় মিলে যায়...
  factory.createCheckbox(); // ...একই theme-এর সাথে
}
```

**ধাপ ৩ — বাস্তব Flutter use case।**
Theming system আর adaptive UI kit: প্রতি theme/platform-এ একটা factory একসাথে মানানসই widget-এর সেট বানায়। ফলে light button-এর সাথে dark checkbox কখনো মিশে যায় না।

**Interviewer কেন জিজ্ঞেস করে:** এটা পরীক্ষা করে একটা object বানানো (Factory Method) আর একটা মিলে যাওয়া পরিবার বানানোর (Abstract Factory) পার্থক্য।

**সাধারণ ভুল:** যেখানে সাধারণ Factory Method-ই যথেষ্ট, সেখানে এটা ব্যবহার করা। Abstract Factory product-এর *পরিবার*-এর জন্য; একটা product-এর জন্য এত জটিলতা যোগ করবেন না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Factory Method vs Abstract Factory?"* → Factory Method = একটা method দিয়ে একটা product; Abstract Factory = কয়েকটা method আছে এমন একটা object দিয়ে সম্পর্কিত product-এর সেট।

**সম্পর্কিত:** [Q2 — Factory Method](#q2) · [Q4 — Builder](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. Builder

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Builder একটা জটিল object ধাপে ধাপে তৈরি করে। অনেক parameter দেওয়া একটা বিশাল constructor-এর বদলে এটা ব্যবহার হয়। আমি যে অংশগুলো চাই সেগুলো set করি, তারপর build call করি। কোনো object-এ অনেক optional field থাকলে এটা খুব কাজে দেয়। Dart-এর cascade operator আর named parameter প্রায়ই ক্লাসিক Builder-এর জায়গা নিয়ে নেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
10টা parameter-এর একটা constructor (অনেকগুলো optional) পড়া কঠিন আর ভুল হওয়ার ঝুঁকি বেশি। Builder দিয়ে শুধু দরকারি অংশগুলোই পড়ার মতো করে set করা যায়। তারপর শেষ object-টা তৈরি হয়।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
class Pizza {
  final String size;
  final List<String> toppings;
  Pizza(this.size, this.toppings);
}

class PizzaBuilder {
  String _size = 'medium';
  final List<String> _toppings = [];

  PizzaBuilder setSize(String s) { _size = s; return this; }  // this ফেরত দেয় → chain করা যায়
  PizzaBuilder addTopping(String t) { _toppings.add(t); return this; }
  Pizza build() => Pizza(_size, _toppings);
}

final pizza = PizzaBuilder()
    .setSize('large')
    .addTopping('cheese')
    .addTopping('mushroom')
    .build();
```

**ধাপ ৩ — বাস্তব Flutter use case।**
Flutter-এর named parameter আগে থেকেই builder-এর মতো অভিজ্ঞতা দেয় (`Container(padding: ..., color: ...)`)। cascade `..` ও object ধাপে ধাপে তৈরি করে (`Paint()..color = ...`)। ক্লাসিক builder দেখা যায় query builder আর notification builder-এ।

**Interviewer কেন জিজ্ঞেস করে:** অনেক optional অংশওয়ালা object আপনি কীভাবে সামলান, সেটা এটা পরীক্ষা করে। সাথে Dart-এর idiomatic বিকল্পগুলো আপনি জানেন কি না, সেটাও।

**সাধারণ ভুল:** লম্বা একটা Builder class লেখা, যেখানে Dart-এর named/optional parameter বা cascade আগেই সহজভাবে সমাধান দিয়ে দেয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Dart কীভাবে Builder-এর জায়গা নেয়?"* → optional config-এর জন্য named parameter, আর ধাপে ধাপে setup-এর জন্য cascade (`..`)।

**সম্পর্কিত:** [Q2 — Factory Method](#q2) · [Q3 — Abstract Factory](#q3)

[↑ উপরে ফিরুন](#toc)

---

# B. Structural patterns

---

## <a id="q5"></a>5. Adapter

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Adapter দুটো বেমানান interface-কে একসাথে কাজ করায়। একটাকে wrap করে অন্যটার মতো দেখায়। এটা travel plug adapter-এর মতো। কোনো third-party library বা legacy class-কে আপনার app যেমন interface চায়, সেই interface-এ বসাতে এটা ব্যবহার করি। কোনো দিকই বদলাতে হয় না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
আপনার app একটা নির্দিষ্ট interface আশা করে, কিন্তু library দেয় অন্যরকম একটা। নিজের code বা library নতুন করে লেখার বদলে মাঝখানে একটা adapter বসান। সেটাই অনুবাদ করে দেয়।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
// আপনার app যা আশা করে:
abstract class PaymentProcessor {
  void pay(double amount);
}

// অন্য method নামওয়ালা একটা third-party class:
class StripeApi {
  void makePayment(int cents) => print('Stripe charged $cents cents');
}

// adapter দুটোর মাঝে অনুবাদ করে:
class StripeAdapter implements PaymentProcessor {
  final StripeApi stripe;
  StripeAdapter(this.stripe);
  @override
  void pay(double amount) => stripe.makePayment((amount * 100).round());
}

void checkout(PaymentProcessor p) => p.pay(9.99); // app code পরিষ্কার থাকে
checkout(StripeAdapter(StripeApi()));
```

**ধাপ ৩ — বাস্তব Flutter use case।**
কোনো third-party SDK (payment, analytics, database) নিজের interface-এর পেছনে wrap করা। ফলে পরে provider বদলাতে গেলে app code ছুঁতে হয় না। Data layer-এর বাইরের type-গুলো Domain থেকে দূরে রাখার উপায়ও এটাই।

**Interviewer কেন জিজ্ঞেস করে:** বাইরের code পরিষ্কারভাবে যুক্ত করার বাস্তব pattern এটাই। আর এটা app-কে vendor থেকে আলাদা রাখে।

**সাধারণ ভুল:** Adapter আর Facade গুলিয়ে ফেলা। Adapter একটা interface *বদলে* দেয় আপনার দরকার মতো; Facade জটিল কয়েকটা class-কে *সহজ* করে ([Q7](#q7))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Vendor বদলালে এটা কীভাবে সাহায্য করে?"* → শুধু adapter বদলায়; app-এর বাকি অংশ আপনার interface-এর উপর নির্ভর করে, তাই একই থাকে।

**সম্পর্কিত:** [Q7 — Facade](#q7) · [Q6 — Decorator](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. Decorator

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Decorator একটা object-কে একই interface-এর অন্য object দিয়ে wrap করে নতুন আচরণ যোগ করে, subclass বানানোর বদলে। coffee-তে topping যোগ করার কথা ভাবুন। Flutter এই ধারণার উপরেই তৈরি — একটা widget-কে Padding-এ, তারপর Center-এ, তারপর GestureDetector-এ wrap করেন, প্রতিটা একটা করে feature যোগ করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
আপনি object-এ সহজে feature যোগ করতে চান, নানা রকম মিশ্রণে। প্রতিটা মিশ্রণের জন্য আলাদা subclass বানাতে চান না। wrap করলে feature-গুলো স্তরে স্তরে সাজানো যায়।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class Coffee {
  double cost();
  String description();
}
class PlainCoffee implements Coffee {
  @override double cost() => 2.0;
  @override String description() => 'coffee';
}

// একটা decorator Coffee-কে wrap করে আর তাতে যোগ করে
class MilkDecorator implements Coffee {
  final Coffee inner;
  MilkDecorator(this.inner);
  @override double cost() => inner.cost() + 0.5;
  @override String description() => '${inner.description()} + milk';
}

Coffee order = MilkDecorator(MilkDecorator(PlainCoffee()));
print(order.description()); // coffee + milk + milk
print(order.cost());        // 3.0
```

**ধাপ ৩ — বাস্তব Flutter use case।**
পুরো widget tree-টাই decorator ধাঁচের: `GestureDetector(child: Padding(child: Center(child: Text('Hi'))))`। প্রতিটা wrapper একটা করে feature যোগ করে (tap handling, spacing, alignment)। `Text`-এর subclass বানাতে হয় না।

**Interviewer কেন জিজ্ঞেস করে:** Flutter-এর "সবকিছু সবকিছুকে wrap করে" composition model এই pattern দিয়েই বোঝা যায়।

**সাধারণ ভুল:** এটাকে inheritance-এর সাথে গুলিয়ে ফেলা। Decorator runtime-এ wrap করে (flexible মিশ্রণ); subclass বানালে আচরণ compile time-এ আটকে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter কীভাবে decorator-এর উদাহরণ?"* → widget wrap করা (Padding, Center, Opacity) ভেতরের widget-এর subclass না বানিয়েই আচরণ যোগ করে।

**সম্পর্কিত:** [Q9 — Composite](#q9) · [Q5 — Adapter](#q5)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. Facade

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Facade জটিল কয়েকটা class-এর সামনে একটা সহজ interface দেয়। ফলে caller-কে এলোমেলো খুঁটিনাটি নিয়ে ভাবতে হয় না। এটা hotel-এর reception desk-এর মতো, যে সব কাজ আপনার হয়ে সামলায়। কয়েকটা subsystem-কে একটা সহজ method-এর পেছনে wrap করতে এটা ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
একটা কাজে কয়েকটা class একসাথে লাগতে পারে (auth, network, cache, parsing)। প্রতিটা caller-কে সেগুলো জোড়া লাগাতে বাধ্য করলে ভুল হওয়ার ঝুঁকি বাড়ে। Facade সেটা একটা পরিষ্কার call-এর পেছনে লুকিয়ে দেয়।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
// জটিল subsystem-গুলো
class AuthService { String token() => 'abc'; }
class ApiService { String fetch(String token) => 'data'; }
class CacheService { void save(String data) {} }

// Facade — একটাই সহজ entry point
class UserFacade {
  final _auth = AuthService();
  final _api = ApiService();
  final _cache = CacheService();

  String getUserData() {                 // একটাই সহজ method
    final token = _auth.token();
    final data = _api.fetch(token);
    _cache.save(data);
    return data;
  }
}

UserFacade().getUserData(); // caller ভেতরের ধাপগুলো নিয়ে ভাবে না
```

**ধাপ ৩ — বাস্তব Flutter use case।**
একটা repository প্রায়ই কয়েকটা data source-এর (API + cache + database) উপরে একটা facade। এটা একটাই `getUser()` খুলে দেয়। কয়েকটা plugin (location + permissions + maps) wrap করা "service" class আরেকটা উদাহরণ।

**Interviewer কেন জিজ্ঞেস করে:** জটিলতাকে একটা সহজ, স্থির interface-এর পেছনে লুকাতে পারেন কি না, এটা তা পরীক্ষা করে।

**সাধারণ ভুল:** এটাকে Adapter-এর সাথে গুলিয়ে ফেলা। Facade অনেক class-কে একটা interface-এ *সহজ* করে; Adapter একটা interface-কে আরেকটায় *বদলে ফেলা* করে ([Q5](#q5))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Facade vs Repository?"* → repository হলো data access-এর জন্য বিশেষায়িত একটা facade, যেটা data source-ও লুকিয়ে রাখে।

**সম্পর্কিত:** [Q5 — Adapter](#q5) · [Q1 — Singleton](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. Proxy

> Deeper · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Proxy হলো একটা বদলি object, যেটা আসল object-এ পৌঁছানোর পথ control করে — interface একই থাকে, কিন্তু আগে বা পরে কিছু যোগ করে, যেমন caching, lazy loading, বা access check। ভাবুন একজন receptionist-এর কথা, যিনি ঠিক করেন আপনি manager-এর কাছে যেতে পারবেন কি না। Lazy-loading image placeholder একটা সাধারণ proxy।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
কখনো কখনো আপনি আসল object সরাসরি ব্যবহার করতে চান না — হয়তো সেটা তৈরি করা খরচ বেশি, বা caching লাগে, বা permission check লাগে। Proxy সেটাকে মুড়ে দেয় আর ওই control-টা যোগ করে। বাইরে থেকে দেখতে আসল জিনিসের মতোই লাগে।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class Image {
  void display();
}
class RealImage implements Image {
  final String file;
  RealImage(this.file) { print('loading $file from disk'); } // ভারী
  @override void display() => print('showing $file');
}

// Proxy ভারী load-টা দেরি করায়, যতক্ষণ না সত্যিই দরকার হয় (lazy loading)
class ImageProxy implements Image {
  final String file;
  RealImage? _real;
  ImageProxy(this.file);
  @override
  void display() {
    _real ??= RealImage(file); // প্রথম display-এ তবেই আসলটা তৈরি হয়
    _real!.display();
  }
}

final img = ImageProxy('photo.png'); // এখনো load হয়নি
img.display();                        // এখন load হয়, তারপর দেখায়
```

**ধাপ ৩ — বাস্তব Flutter use case।**
Lazy-loading image (scroll করে চোখের সামনে এলে তবেই load), একটা caching proxy যেটা network-এ যাওয়ার আগে cache করা data ফেরত দেয়, বা একটা access-control proxy যেটা call-এর আগে auth check করে।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা গভীর structural pattern। এটা যাচাই করে আপনি cross-cutting control (caching, lazy load) স্বচ্ছভাবে যোগ করতে পারেন কি না।

**সাধারণ ভুল:** Decorator-এর সাথে গুলিয়ে ফেলা। দুটোই মুড়ে দেয় আর একই interface ব্যবহার করে। কিন্তু Proxy আসল object-এ *পৌঁছানো control করে*; Decorator *আচরণ/feature যোগ করে*।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Proxy-র ধরনগুলো কী?"* → Virtual (lazy load), caching, protection (access control), remote (দূরের object-এর বদলি হয়ে দাঁড়ায়)।

**সম্পর্কিত:** [Q6 — Decorator](#q6) · [Q7 — Facade](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. Composite

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Composite দিয়ে একটা single object আর object-এর একটা group-কে একইভাবে ব্যবহার করা যায়, কারণ দুটোকে একটা common interface দেওয়া হয়। ভাবুন folder-এর কথা, যেটা file *আর* অন্য folder দুটোই রাখতে পারে। Flutter-এর widget tree ঠিক এটাই — একটা widget leaf হতে পারে, আবার অন্য widget ধরে রাখতে পারে। দুটোকেই আপনি একইভাবে ব্যবহার করেন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
যখন আপনার কাছে object-এর একটা tree থাকে (part-whole hierarchy), তখন "একটা item" আর "একটা group"-এর জন্য আলাদা code লিখতে চাইবেন না। Composite দুটোকেই একই interface দেয়। ফলে client code সহজ থাকে।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class FileSystemItem {
  int size();
}
class FileItem implements FileSystemItem {       // leaf
  final int bytes;
  FileItem(this.bytes);
  @override int size() => bytes;
}
class Folder implements FileSystemItem {          // composite
  final List<FileSystemItem> children = [];
  @override int size() => children.fold(0, (sum, c) => sum + c.size());
}

final root = Folder()
  ..children.add(FileItem(100))
  ..children.add(Folder()..children.add(FileItem(50)));
print(root.size()); // 150 — একই size() call file আর folder দুটোতেই কাজ করে
```

**ধাপ ৩ — বাস্তব Flutter use case।**
Widget tree: একটা `Column` (composite) এমন children রাখে যেগুলো leaf হতে পারে (`Text`), আবার আরও composite হতে পারে (`Row`, `Column`)। আপনি সেগুলো একইভাবে build আর traverse করেন। Menu আর nested comment thread আরও দুটো উদাহরণ।

**Interviewer কেন জিজ্ঞেস করে:** এটা widget tree-র মতো tree structure ব্যাখ্যা করে। আর অংশ ও পুরোটাকে একইভাবে handle করা যাচাই করে।

**সাধারণ ভুল:** একটা shared interface না দিয়ে single item আর group-এর জন্য আলাদা logic লেখা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter-এর widget tree কীভাবে composite?"* → একটা parent widget প্রতিটা child-কে একইভাবে দেখে, সেটা single widget হোক বা একটা পুরো subtree হোক।

**সম্পর্কিত:** [Q6 — Decorator](#q6) · [Q15 — Iterator (tree traverse করা)](#q15)

[↑ উপরে ফিরুন](#toc)

---

# C. Behavioral patterns

---

## <a id="q10"></a>10. Observer

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Observer দিয়ে অনেক object একটা subject-এ subscribe করতে পারে। Subject বদলালে সবাই নিজে থেকেই খবর পায়। এটা খবরের কাগজের subscription-এর মতো — একবার publish হয়, সব subscriber সেটা পায়। Flutter সব জায়গায় এটা ব্যবহার করে: `ChangeNotifier`/`Listenable`, `ValueNotifier`, আর Stream — সবই Observer।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
একটা object বদলালে আরও কয়েকটাকে সাড়া দিতে হয়। কিন্তু আপনি চান না subject প্রত্যেকটাকে সরাসরি চিনুক। Observer-রা subscribe করে; subject শুধু জানিয়ে দেয় "কিছু একটা বদলেছে।"

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
class Subject {
  final List<void Function(int)> _listeners = [];
  int _value = 0;

  void subscribe(void Function(int) listener) => _listeners.add(listener);

  set value(int v) {
    _value = v;
    for (final l in _listeners) l(v); // সবাইকে জানানো হয়
  }
}

final s = Subject();
s.subscribe((v) => print('A saw $v'));
s.subscribe((v) => print('B saw $v'));
s.value = 5; // A আর B দুজনেই খবর পায়
```

**ধাপ ৩ — বাস্তব Flutter use case।**
`ChangeNotifier` + `notifyListeners()` (Provider এটা ব্যবহার করে) হলো Observer। `ValueNotifier`/`ValueListenableBuilder`, আর `listen` সহ Dart-এর `Stream` — সবই Observer। Widget-রা subscribe করে, আর data বদলালে rebuild হয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা Flutter-এর reactive state management-এর মেরুদণ্ড। এটা জানা থাকলে `setState` ছাড়া rebuild কীভাবে হয় তা বোঝা যায়।

**সাধারণ ভুল:** `dispose()`-এ unsubscribe করতে ভুলে যাওয়া (listener সরানো / stream subscription cancel করা)। এতে memory leak হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter-এ Observer কোথায় আছে?"* → ChangeNotifier, ValueNotifier, Stream, আর যেকোনো `Listenable`।
- *"Push না pull?"* → Observer সাধারণত পরিবর্তনটা subscriber-দের কাছে push করে।

**সম্পর্কিত:** [Q11 — Strategy](#q11) · [Q13 — State](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. Strategy

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Strategy দিয়ে runtime-এ algorithm বদলানো যায়, কারণ প্রতিটা option একটা common interface-এর পিছনে থাকে। আচরণ বেছে নিতে বড় if/else লেখার বদলে, আপনি যে strategy চান সেটা inject করেন। উদাহরণ: আলাদা আলাদা sorting method, validation rule, বা payment option।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
একটা কাজ করার কয়েকটা উপায় আছে (sort, validate, pay)। আপনি runtime-এ একটা বেছে নিতে বা বদলাতে চান। কিন্তু বিশাল conditional ছাড়া, আর নতুন option যোগ করার সময় class-টা প্রতিবার না বদলে।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class PaymentStrategy {
  void pay(double amount);
}
class CardPayment implements PaymentStrategy {
  @override void pay(double a) => print('paid \$a by card');
}
class BkashPayment implements PaymentStrategy {
  @override void pay(double a) => print('paid \$a by bKash');
}

class Checkout {
  PaymentStrategy strategy;
  Checkout(this.strategy);
  void process(double amount) => strategy.pay(amount); // কাজটা strategy-কে দিয়ে দেয়
}

Checkout(BkashPayment()).process(9.99); // ইচ্ছেমতো strategy বদলানো যায়
```

**ধাপ ৩ — বাস্তব Flutter use case।**
বদলানো যায় এমন repository (real বনাম fake), form-এর জন্য আলাদা validation strategy, list-এ sorting option, বা pluggable pricing rule। এটা dependency injection-এর সাথে দারুণ মেলে।

**Interviewer কেন জিজ্ঞেস করে:** বাড়তে থাকা if/else chain-এর এটাই পরিষ্কার বিকল্প। Open/closed design দেখানোর জন্য এটা তাঁদের প্রিয়।

**সাধারণ ভুল:** State-এর সাথে গুলিয়ে ফেলা। Strategy বেছে নেয় *caller*, একটা কাজ অন্যভাবে করার জন্য। আর State object-এর আচরণ বদলায় যখন তার *internal state* বদলায় ([Q13](#q13))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Strategy বনাম সাধারণ if/else?"* → Strategy-তে নতুন option যোগ করতে শুধু একটা class যোগ করলেই হয় (open/closed)। পুরোনো code edit করতে হয় না।

**সম্পর্কিত:** [Q13 — State](#q13) · [Q2 — Factory Method](#q2) · [Q10 — Observer](#q10)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. Command

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Command একটা request-কে object-এ পরিণত করে। কাজটা করার জন্য যা যা দরকার, সব ওই object-এ থাকে। কাজটা এখন object, তাই আমি সেটাকে queue করতে পারি, log করতে পারি, বা undo করতে পারি। এটা অনেকটা লিখিত order ticket-এর মতো। সবচেয়ে পরিচিত ব্যবহার হলো undo/redo।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
আপনি action-গুলোকে data-এর মতো ব্যবহার করতে চান — জমা রাখা, queue করা, schedule করা, বা undo করা। সরাসরি method call করে এটা করা যায় না। কিন্তু action-টাকে একটা object-এ মুড়ে দিলে করা যায়।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class Command {
  void execute();
  void undo();
}

class AddTextCommand implements Command {
  final StringBuffer doc;
  final String text;
  AddTextCommand(this.doc, this.text);
  @override void execute() => doc.write(text);
  @override void undo() => print('remove "$text"'); // কাজটা উল্টে দেয়
}

// invoker undo/redo-র জন্য history রাখতে পারে
final history = <Command>[];
void run(Command c) { c.execute(); history.add(c); }
void undoLast() => history.removeLast().undo();
```

**ধাপ ৩ — বাস্তব Flutter use case।**
Editor-এ undo/redo, action queue (যেমন offline action পরে replay করা), আর keyboard shortcut-এর জন্য Flutter-এর নিজের `Intent`/`Action` system — প্রতিটা shortcut একটা command-ধাঁচের action object-এ map হয়।

**Interviewer কেন জিজ্ঞেস করে:** undo/redo আর action history বানানোর এটাই standard উপায়।

**সাধারণ ভুল:** command object-এর বদলে এলোমেলো flag দিয়ে undo বানানো। এতে code খুব দ্রুত জটিল হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Command কীভাবে undo সম্ভব করে?"* → প্রতিটা command জানে নিজেকে কীভাবে উল্টাতে হয়। execute হওয়া command-গুলোর একটা stack রাখুন।

**সম্পর্কিত:** [Q11 — Strategy](#q11) · [Q5 — Stack (undo history)](section-11-data-structure-bn.md#q5)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. State

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"State pattern একটা object-কে তার ভেতরের state বদলালে আচরণ বদলাতে দেয়। মনে হয় যেন object-টা অন্য একটা class হয়ে গেছে। একটা status field-এর উপর বড় if/else লেখার বদলে প্রতিটা state নিজেই একটা object। সেই object জানে কীভাবে আচরণ করতে হবে আর পরের state কোনটা। Traffic light হলো এর সবচেয়ে পরিচিত উদাহরণ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
একটা object আলাদা আলাদা mode-এ আলাদাভাবে আচরণ করে (একটা media player: playing, paused, stopped)। পুরোটা এক class-এ `if (status == ...)` দিয়ে লিখলে জট পাকিয়ে যায়। State pattern প্রতিটা mode-কে নিজের আলাদা class-এ রাখে।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class PlayerState {
  void press(MediaPlayer player);
}
class PlayingState implements PlayerState {
  @override void press(MediaPlayer p) { print('pause'); p.state = PausedState(); }
}
class PausedState implements PlayerState {
  @override void press(MediaPlayer p) { print('play'); p.state = PlayingState(); }
}

class MediaPlayer {
  PlayerState state = PausedState();
  void pressPlayPause() => state.press(this); // আচরণ নির্ভর করে বর্তমান state-এর উপর
}

final player = MediaPlayer();
player.pressPlayPause(); // play
player.pressPlayPause(); // pause
```

**ধাপ ৩ — বাস্তব Flutter use case।**
Screen-এর status model করা (loading / loaded / error) — সাধারণত sealed class আর BLoC state দিয়ে করা হয়। ভাবনার দিক থেকে এটাই State pattern। Form wizard আর onboarding flow-ও এটা ব্যবহার করে।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি state machine পরিষ্কারভাবে handle করতে পারেন কি না। BLoC/sealed state কীভাবে কাজ করে, তার সাথেও মিল আছে।

**সাধারণ ভুল:** Strategy-র সাথে গুলিয়ে ফেলা। State আচরণ বদলায় object-এর *ভেতরের* state-এর উপর ভিত্তি করে (আর state নিজেরাই নিজেদের বদলাতে পারে)। Strategy বেছে দেয় *বাইরের* caller ([Q11](#q11))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা BLoC-এর সাথে কীভাবে সম্পর্কিত?"* → BLoC-এর sealed state (Loading/Loaded/Error) হলো State-pattern ধাঁচের একটা state machine।

**সম্পর্কিত:** [Q11 — Strategy](#q11) · [Q10 — Observer](#q10)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. Template Method

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Template Method একটা algorithm-এর নির্দিষ্ট structure base class-এ ঠিক করে দেয়। কিন্তু নির্দিষ্ট step-গুলো subclass পূরণ করে। পুরো order আটকানো থাকে; শুধু customizable অংশটুকু বদলায়। এটা একটা recipe-র মতো — ধাপগুলো fixed, কিন্তু উপকরণ আপনি বেছে নেন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
কয়েকটা process-এর মোট ধাপ একই, কিন্তু অল্প কিছু ধাপে পার্থক্য থাকে। আপনি shared structure-টা একবার লিখতে চান। আর প্রতিটা variant শুধু আলাদা অংশটুকু override করবে।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে।**

```dart
abstract class DataProcessor {
  // template method — order fixed, overridable step-গুলো call করে
  void process() {
    final raw = readData();      // এই step আলাদা হয়
    final clean = transform(raw); // এই step আলাদা হয়
    save(clean);                  // সবার জন্য এক
  }
  String readData();            // subclass এটা পূরণ করে
  String transform(String raw); // subclass এটা পূরণ করে
  void save(String data) => print('saved: $data'); // সবার জন্য default
}

class CsvProcessor extends DataProcessor {
  @override String readData() => 'a,b,c';
  @override String transform(String raw) => raw.toUpperCase();
}

CsvProcessor().process(); // fixed structure চলে, CSV-এর নিজের step দিয়ে
```

**ধাপ ৩ — বাস্তব Flutter use case।**
`StatelessWidget`/`StatefulWidget` একটা template ব্যবহার করে: framework lifecycle control করে আর আপনার `build()` call করে (এই step-টা আপনি পূরণ করেন)। fixed flow আর overridable hook সহ abstract base class সব জায়গায় আছে।

**Interviewer কেন জিজ্ঞেস করে:** এটা ব্যাখ্যা করে framework (Flutter সহ) কীভাবে আপনাকে hook method দেয়, অথচ পুরো flow নিজের হাতে রাখে।

**সাধারণ ভুল:** Strategy-র সাথে গুলিয়ে ফেলা। Template Method *inheritance* ব্যবহার করে (step override করা)। Strategy *composition* ব্যবহার করে (পুরো algorithm inject করা)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`build()` কীভাবে একটা template method?"* → Framework render pipeline চালায় (fixed) আর ঠিক সময়ে আপনার `build()` call করে (আপনার step)।

**সম্পর্কিত:** [Q11 — Strategy](#q11) · [Q3 — Abstract Factory](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. Iterator

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-14-design-patterns.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Iterator একটা collection-এর item একটা একটা করে ঘুরে দেখার standard উপায় দেয়। Collection সেগুলো কীভাবে জমা রাখে, তা প্রকাশ করতে হয় না। Dart-এ এটা built-in: যা কিছু `Iterable`, তা `for-in`, `map`, `where` ইত্যাদির সাথে কাজ করে। চাইলে নিজের iterator-ও বানানো যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
আলাদা আলাদা collection (list, set, tree) data আলাদাভাবে জমা রাখে। Iterator সেগুলো ঘুরে দেখার একটা সাধারণ উপায় দেয়। ফলে আপনার loop-এর code ভেতরের storage-এর উপর নির্ভর করে না।

**ধাপ ২ — Dart-এ এটা কীভাবে কাজ করে (built in)।**

```dart
final items = [1, 2, 3];
for (final x in items) print(x); // ভেতরে iterator-ই ব্যবহার হয়

// generator (sync*) দিয়ে বানানো custom iterable
Iterable<int> evens(int max) sync* {
  for (var i = 0; i <= max; i += 2) yield i; // চাহিদামতো value দেয়
}
for (final e in evens(6)) print(e); // 0, 2, 4, 6
```

যেকোনো class `Iterable` implement করে iterable হতে পারে (বা আরও সহজে, একটা `sync*` generator প্রকাশ করে)।

**ধাপ ৩ — বাস্তব Flutter use case।**
প্রতিটা `for-in` loop, `ListView.builder`-এর item access, আর chained collection method (`.map().where().toList()`) Dart-এর Iterator-এর উপর নির্ভর করে। নিজে হাতে খুব কমই লিখতে হয়, কারণ Dart-এর `Iterable` আর generator কাজটা সেরে দেয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি Dart-এর collection আর `for-in` আসলে কীভাবে কাজ করে তা বোঝেন কি না।

**সাধারণ ভুল:** হাতে iterator লেখা, যেখানে একটা `sync*` generator বা Dart-এর built-in `Iterable` অনেক সহজ হতো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা class-কে iterable কীভাবে বানাবেন?"* → `Iterable<T>` implement করুন (একটা `iterator` দিন), অথবা একটা `sync*` generator method প্রকাশ করুন।

**সম্পর্কিত:** [Q9 — Composite (ঘুরে দেখা)](#q9) · [Q3 (DSA) — Lists](section-11-data-structure-bn.md#q3)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। আগে table, তারপর এক লাইনের মনে করানো পয়েন্ট।

## সব ১৫টি pattern, প্রতিটি এক লাইনে

| Pattern | Family | এক লাইনে | Flutter উদাহরণ |
|---|---|---|---|
| Singleton | Creational | শুধু একটাই instance | GetIt, SharedPreferences |
| Factory Method | Creational | কোন object বানাবে সেটা একটা method ঠিক করে | `fromJson`, platform widget |
| Abstract Factory | Creational | মানানসই object-এর একটা family বানায় | theme/UI kit |
| Builder | Creational | জটিল object ধাপে ধাপে বানানো | named param, cascade |
| Adapter | Structural | দুটো interface মিলিয়ে দেয় | 3rd-party SDK wrap করা |
| Decorator | Structural | feature যোগ করতে wrap করা | widget-এর চারপাশে Padding/Center |
| Facade | Structural | অনেক class-এর জন্য একটা সহজ সামনের মুখ | API+cache-এর উপরে repository |
| Proxy | Structural | বদলি, যে access control করে | lazy image, caching |
| Composite | Structural | এক আর অনেককে একইভাবে দেখা | widget tree |
| Observer | Behavioral | পরিবর্তন হলে subscriber-রা খবর পায় | ChangeNotifier, Streams |
| Strategy | Behavioral | runtime-এ algorithm বদলে ফেলা | বদলানো যায় এমন repo/validator |
| Command | Behavioral | action-কে object হিসেবে রাখা (undo) | undo/redo, action queue |
| State | Behavioral | ভেতরের state অনুযায়ী আচরণ বদলায় | BLoC state, media player |
| Template Method | Behavioral | structure fixed, ধাপগুলো override করা যায় | `build()` hook |
| Iterator | Behavioral | collection একইভাবে ঘুরে দেখা | `for-in`, Iterable |

## যেগুলো নিয়ে মানুষ গুলিয়ে ফেলে

- **Factory Method vs Abstract Factory** → একটা product বনাম মানানসই একটা family। ([Q2](#q2), [Q3](#q3))
- **Adapter vs Facade** → interface বদলে দেওয়া বনাম অনেক class সহজ করা। ([Q5](#q5), [Q7](#q7))
- **Decorator vs Proxy** → feature যোগ করা বনাম access control করা। ([Q6](#q6), [Q8](#q8))
- **Strategy vs State** → caller নিজে algorithm বেছে নেয় বনাম ভেতরের state অনুযায়ী আচরণ বদলায়। ([Q11](#q11), [Q13](#q13))
- **Strategy vs Template Method** → algorithm inject করা (composition) বনাম ধাপ override করা (inheritance)। ([Q11](#q11), [Q14](#q14))

## এক লাইনের মনে রাখার কথা

- **Creational** = object কীভাবে তৈরি হয় (Singleton, Factory, Abstract Factory, Builder)।
- **Structural** = object কীভাবে জোড়া লাগানো হয় (Adapter, Decorator, Facade, Proxy, Composite)।
- **Behavioral** = object কীভাবে কথা বলে আর আচরণ করে (Observer, Strategy, Command, State, Template Method, Iterator)।
- **Flutter হলো decorator + composite** — widget widget-কে wrap করে আর একটা tree বানায়। ([Q6](#q6), [Q9](#q9))
- **Flutter-এর state management হলো Observer** — ChangeNotifier, ValueNotifier, Streams। ([Q10](#q10))
- নাম বলার আগে বলুন **প্রতিটা pattern কোন সমস্যা সমাধান করে**। এটাই senior signal।

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যান

Interviewer "সংজ্ঞা দিন" থেকে ঠেলে নিয়ে যান "কোথায় ব্যবহার করেছেন" পর্যন্ত। জোরে বলে অনুশীলন করুন:

1. *"Flutter-এ প্রতিদিন ব্যবহার করেন এমন একটা pattern-এর নাম বলুন।"* → Observer (ChangeNotifier/Streams) আর Decorator (widget wrap করা)।
2. *"বাস্তব একটা ক্ষেত্রে Strategy দেখান।"* → DI দিয়ে inject করা বদলানো যায় এমন repository; পুরোনো code না বদলেই নতুন একটা যোগ করা যায়।
3. *"Strategy আর State-এর পার্থক্য কী?"* → Strategy-তে caller বেছে নেয়; State ভেতরের state দেখে নিজেই বদলে যায়।
4. *"undo/redo কীভাবে বানাবেন?"* → একটা stack-এ Command object; প্রতিটা জানে নিজেকে কীভাবে undo করতে হয়।
5. *"এটা কি over-engineering নয়?"* → জোর করে করলে হ্যাঁ; pattern তখনই ব্যবহার করুন যখন এটা বাস্তব সমস্যা সমাধান করে (বুদ্ধি, মুখস্থ নয়)।

*কখন* আর *কেন* ব্যাখ্যা করা — শুধু *কী* নয় — এটাই senior signal এনে দেয়। remote আর BD, দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

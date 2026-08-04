# Section 6 — Flutter-এ Testing

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরোপুরি ব্যাখ্যা করা**, আর **link করা** — যাতে আপনি এদিক-ওদিক ঘুরে ধাপে ধাপে প্রস্তুতি নিতে পারেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-06-testing-bn.md](../software-engineer-flutter/section-06-testing.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বিস্তারিত, ধাপে ধাপে ব্যাখ্যা, বাস্তব জীবনের উদাহরণ আর code সহ।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সংশ্লিষ্ট প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর তার কঠিনতা (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তর** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন "আরও গভীরে যেতে পারেন?" সহজ আর পরিষ্কারভাবে বলাটাই একটা senior skill — আর এটা remote আর BD দুই ধরনের কোম্পানিতেই সমানভাবে কাজ করে।

---


## <a id="toc"></a>সূচিপত্র

**A. Test-এর ধরন ও strategy**
1. [তিন ধরনের test — unit, widget, integration](#q1) · *Very common*
2. [Test pyramid ও test-এর ভারসাম্য](#q2) · *Very common*
3. [Test-driven development (TDD)](#q3) · *Common*

**B. Unit testing-এর মূল বিষয়**
4. [মূল primitive — `test`, `expect`, `group`, `setUp`, `tearDown`](#q4) · *Very common*
5. [Matcher — `equals`, `throwsA`, `isA`, আর বাকিরা](#q5) · *Common*

**C. Widget testing**
6. [Widget testing — `pumpWidget`, `find`, `tap`, `pump`, `pumpAndSettle`](#q6) · *Very common*
7. [Finder গভীরভাবে — `find.byType`, `byKey`, `text`, `widgetWithText`](#q7) · *Common*

**D. Test-এ async ও সময়**
8. [Async code test করা — `async` test, `fakeAsync`, সময় এগিয়ে নেওয়া](#q8) · *Very common*

**E. Test double (mock ও fake)**
9. [Mockito দিয়ে mocking — `@GenerateMocks`, `when`/`thenReturn`, `verify`](#q9) · *Very common*
10. [Mocktail vs Mockito — আর কোনটা কখন বেছে নেবেন](#q10) · *Common*
11. [Fake vs Mock — কোনটা কখন ব্যবহার করবেন](#q11) · *Common*

**F. আসল app layer test করা**
12. [`bloc_test` দিয়ে BLoC বা Cubit test করা](#q12) · *Very common*
13. [Cubit-এর উপর নির্ভরশীল একটা screen test করা](#q13) · *Very common*
14. [HTTP API call করে এমন repository test করা (mock Dio / http)](#q14) · *Very common*

**G. Visual ও end-to-end testing**
15. [Golden test — তৈরি করা, update করা, আর কখন ব্যবহার করবেন](#q15) · *Common*
16. [`integration_test` দিয়ে integration testing](#q16) · *Common*

**H. Coverage ও test সুস্থ রাখা**
17. [Code coverage — তৈরি করা আর মাপা](#q17) · *Common*
18. [Codebase বড় হলেও test maintainable রাখা](#q18) · *Deeper*

**দ্রুত লিংক:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের review)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

১৮টা প্রশ্ন একসাথে পড়ার দরকার নেই। এই পর্যায়গুলো ক্রম মেনে চলুন — প্রতিটা আগেরটার উপরে দাঁড়ায়। কোনো পর্যায় তখনই শেষ ধরুন, যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন।

**পর্যায় ১ — মূল ভিত্তি (এখান থেকে শুরু করুন)।** এগুলো প্রায় প্রতিটা interview-এ আসে।
→ [Q1 তিন ধরনের test](#q1) · [Q2 Test pyramid](#q2) · [Q4 Unit primitive](#q4) · [Q6 Widget testing](#q6)

**পর্যায় ২ — Test double (testing-এর প্রাণ)।** যেটা test করছেন, সেটাকে আলাদা করার উপায়।
→ [Q9 Mockito](#q9) · [Q10 Mocktail vs Mockito](#q10) · [Q11 Fake vs Mock](#q11) · [Q5 Matcher](#q5)

**পর্যায় ৩ — আসল app layer test করা (প্রতিদিন যা করেন)।**
→ [Q12 BLoC/Cubit test করা](#q12) · [Q13 Cubit সহ screen test করা](#q13) · [Q14 Repository test করা (HTTP)](#q14) · [Q7 Finder](#q7)

**পর্যায় ৪ — Async, সময়, আর visual test।**
→ [Q8 Async ও সময় test করা](#q8) · [Q15 Golden test](#q15) · [Q16 Integration test](#q16)

**পর্যায় ৫ — Senior signal (সবার শেষে)।** এগুলোই শক্ত senior-দের বাকিদের থেকে আলাদা করে।
→ [Q3 TDD](#q3) · [Q17 Code coverage](#q17) · [Q18 বড় স্কেলে maintainable test](#q18)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই আটটা দেখে নিন:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q6](#q6) · [Q9](#q9) · [Q11](#q11) · [Q12](#q12) · [Q13](#q13), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Test-এর ধরন ও strategy

---

## <a id="q1"></a>1. Flutter test-এর তিনটি ধরন — unit, widget, আর integration — কী, আর কোনটা কখন ব্যবহার করবেন?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flutter-এ test-এর তিনটা layer আছে। Unit test একটা function বা class check করে, কোনো UI ছাড়াই — এগুলো দ্রুত। Widget test একটা widget বা screen-এর ছোট অংশ একটা fake engine-এ render করে — মাঝারি গতি। Integration test পুরো app আসল device বা emulator-এ চালায় — ধীর, কিন্তু সবচেয়ে বাস্তব। আমি যতটা সম্ভব testing unit level-এ নামিয়ে আনি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Unit test: শুধু pure logic check করে, কোনো screen নেই।**
Unit test একটা ছোট জিনিস আলাদাভাবে check করে — একটা function, একটা method, বা একটা class। এটা কখনো screen-এ কিছু আঁকে না, তাই এটাই সবচেয়ে দ্রুত। Business logic, হিসাব, parsing, আর repository/service method-এর জন্য এটা ব্যবহার করুন।

```dart
// Unit test — শুধু pure logic test করে, কোনো widget নেই
test('Counter increments', () {
  final counter = Counter();
  counter.increment();
  expect(counter.value, 1);
});
```

**ধাপ ২ — Widget test: একটা widget fake engine-এ render করে।**
Widget test একটা widget (বা ছোট একটা subtree) একটা simulated rendering environment-এ render করে। এটা মাঝারি গতির — unit test-এর চেয়ে ধীর, কারণ এটা widget tree build করে। কিন্তু আসল device-এর চেয়ে অনেক দ্রুত। UI behavior check করতে এটা ব্যবহার করুন: button-এ tap করলে কি text update হয়? List কি সঠিক item দেখাচ্ছে?

```dart
// Widget test — widget render হয় আর সাড়া দেয় কি না test করে
testWidgets('Tap increments counter text', (tester) async {
  await tester.pumpWidget(const MaterialApp(home: CounterPage()));
  expect(find.text('0'), findsOneWidget);
  await tester.tap(find.byIcon(Icons.add));
  await tester.pump();                       // একটা frame rebuild
  expect(find.text('1'), findsOneWidget);
});
```

গুরুত্বপূর্ণ: widget test কোনো phone বা emulator চালু করে **না**। এগুলো Dart VM-এর ভেতরে একটা test rendering engine দিয়ে চলে। এই কারণেই এগুলো দ্রুত।

**ধাপ ৩ — Integration test: পুরো app আসল device-এ চালায়।**
Integration test পুরো app আসল device বা emulator-এ চালায়। এটা সবকিছু একসাথে যাচাই করে — UI, logic, navigation, আর platform code। এটাই সবচেয়ে ধীর, কিন্তু এটা প্রমাণ করে যে সব অংশ ঠিকমতো জোড়া লেগেছে। Login, checkout, বা onboarding-এর মতো গুরুত্বপূর্ণ user flow-এর জন্য এটা ব্যবহার করুন।

```dart
// Integration test — integration_test package দিয়ে আসল device-এ চলে
void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('Full counter flow', (tester) async {
    app.main();
    await tester.pumpAndSettle();
    await tester.tap(find.byIcon(Icons.add));
    await tester.pumpAndSettle();
    expect(find.text('1'), findsOneWidget);
  });
}
```

**ধাপ ৪ — ঘর বানানোর check-এর মতো করে ভাবুন।**
- **Unit test** = একটা ইট শক্ত কি না দেখা। দ্রুত আর সস্তা।
- **Widget test** = একটা তৈরি হওয়া ঘর দেখা। একটু ধীর।
- **Integration test** = চাবি হস্তান্তরের আগে পুরো বাড়ি ঘুরে দেখা। ধীর, কিন্তু ছোট check যা ধরতে পারে না, এটা তা ধরে।

| ধরন | পরিধি | গতি | আস্থা | খরচ |
|---|---|---|---|---|
| Unit | একটা function/class | সবচেয়ে দ্রুত | কম–মাঝারি | সবচেয়ে সস্তা |
| Widget | একটা widget/subtree | মাঝারি | মাঝারি–বেশি | মাঝারি |
| Integration | পুরো app | সবচেয়ে ধীর | সবচেয়ে বেশি | সবচেয়ে ব্যয়বহুল |

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা শুধু নাম নয়, *tradeoff* শুনতে চান। একজন senior সবচেয়ে সস্তা test-টাই বেছে নেন, যেটা তবুও behavior প্রমাণ করে।

**সাধারণ ভুল:** বলা যে "unit test unit test করে, widget test widget test করে" — এতে কিছুই বলা হয় না। আরেকটা ভুল হলো ভাবা যে widget test emulator চালু করে; আসলে এটা Dart VM-এ একটা test engine দিয়ে চলে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কোনটা আপনি সবচেয়ে বেশি লিখবেন?"* → Unit test — এগুলো দ্রুত আর সস্তা, তাই বেশিরভাগ logic ওখানেই cover করা উচিত।
- *"Widget test কি navigation cover করতে পারে?"* → হ্যাঁ, সাধারণ `Navigator.push` widget test-এ কাজ করে। আসল device-এ পুরো multi-screen flow-এর জন্য integration test ব্যবহার করুন।

**সম্পর্কিত:** [Q2 — test pyramid](#q2) · [Q6 — widget testing](#q6) · [Q16 — integration test](#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Test pyramid কী, আর unit, widget, আর integration test-এর মধ্যে ভারসাম্য কীভাবে রাখবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Test pyramid বলে: নিচে অনেক সস্তা আর দ্রুত test রাখুন (unit), মাঝে কম (widget), আর উপরে মাত্র কয়েকটা ধীর ও ব্যয়বহুল test (integration)। কারণটা খরচ — unit test দ্রুত feedback দেয় আর maintain করা সহজ, অন্যদিকে integration test ধীর আর flaky। মূল নিয়ম হলো: testing-কে সবচেয়ে নিচের level-এ নামিয়ে আনুন, যেখানে behavior প্রমাণ করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা দালানের ছবি ভাবুন।**
দালানের দরকার চওড়া, শক্ত ভিত আর ছোট ছাদ — উল্টোটা নয়। Testing-ও একই রকম:
- **ভিত (চওড়া) = unit test।** অনেকগুলো। দ্রুত আর সস্তা।
- **দেয়াল (মাঝারি) = widget test।** কম সংখ্যায়।
- **ছাদ (ছোট) = integration test।** মাত্র কয়েকটা, সবচেয়ে গুরুত্বপূর্ণ flow-এর জন্য।

```
          /\
         /  \
        / IT \          (few)    integration tests, critical paths
       /------\
      / Widget \        (some)   widget tests, UI interactions
     /----------\
    /    Unit     \     (many)   unit tests, logic, models, repos
   /----------------\
```

**ধাপ ২ — এই আকার কেন (অর্থনীতিটা)।**
- Unit test চলে **মিলিসেকেন্ডে**। কী ভাঙল, সেটা এরা ঠিকঠাক বলে দেয়। এরা প্রায় কখনোই flaky হয় না।
- Integration test চলে **সেকেন্ড থেকে মিনিটে**। এরা flaky (timing, device state) আর ধীর। একটা fail করলে কারণ app-এর যেকোনো জায়গায় থাকতে পারে।

তাই আপনি চান দ্রুত সস্তা test বেশিরভাগ সমস্যা ধরুক। আর মাত্র কয়েকটা ধীর test নিশ্চিত করুক যে পুরো জিনিসটা end to end কাজ করে।

**ধাপ ৩ — একটা মোটামুটি লক্ষ্য (নির্দেশনা, আইন নয়)।**
একটা সুস্থ Flutter project প্রায়ই লক্ষ্য রাখে প্রায় **70% unit, 20% widget, 10% integration**। নিজের app অনুযায়ী মিলিয়ে নিন: UI-ভারী app widget test-এর উপর বেশি নির্ভর করে; data-processing app বেশিরভাগই unit test।

**ধাপ ৪ — মনে রাখার একটাই নিয়ম: testing নিচে নামান।**
ধীর test লেখার আগে জিজ্ঞেস করুন: "সস্তা কোনো test কি একই জিনিস প্রমাণ করতে পারে?"

```
Feature: "Add to Cart" button

Unit tests (many):
  - CartBloc emits the right state when AddToCart fires
  - CartRepository.addItem() calls the API correctly
  - price calculation handles discounts

Widget tests (some):
  - the button shows enabled/disabled correctly
  - tapping it dispatches the AddToCart event
  - a snackbar shows on success

Integration tests (one or two):
  - user opens product, taps Add, sees the cart badge update
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি *পরিশ্রমের বিনিময়ে লাভ* নিয়ে ভাবেন কি না — testing-এর প্রতিটা ঘণ্টা কোথায় সবচেয়ে বেশি মূল্য দেয় — শুধু "সবকিছু test করো" নয়।

**সাধারণ ভুল:** Pyramid-টাকে উল্টে দেওয়া — অনেক ধীর integration test আর অল্প unit test লেখা। ফল হলো ধীর CI, flaky pipeline, আর এমন failure যেগুলো debug করা কষ্টকর।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"100% coverage কি লক্ষ্য?"* → না। Coverage শুধু ইঙ্গিত দেয় কোনটা test করা হয়নি, আপনার test ভালো তার প্রমাণ নয়। দেখুন [Q17](#q17)।
- *"Golden test কোথায় বসে?"* → এগুলো widget test-এর পাশে বসে — নির্দিষ্ট widget-এর জন্য একটা visual check। দেখুন [Q15](#q15)।

**সম্পর্কিত:** [Q1 — তিন ধরনের test](#q1) · [Q17 — code coverage](#q17) · [Q18 — maintainable test](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. Test-driven development (TDD) কী, আর Flutter-এ এটা ব্যবহার করবেন কি?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"TDD মানে আমি আগে test লিখি, সেটা fail হতে দেখি, তারপর pass করার মতো ঠিক যতটুকু দরকার ততটুকু code লিখি, তারপর পরিষ্কার করি — এটাই red, green, refactor loop। এটা আমাকে implementation-এর আগে behavior আর design নিয়ে ভাবতে বাধ্য করে। আমি এটা সবচেয়ে বেশি ব্যবহার করি business logic আর bug fix-এ, আর UI-তে একটু ঢিলেঢালাভাবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Red, green, refactor loop।**
TDD হলো একটা ছোট বারবার ঘোরা cycle:
- **Red** — এমন behavior-এর জন্য একটা ছোট test লিখুন যেটা এখনো নেই। চালান। এটা fail করবে (red)। এতে প্রমাণ হয় test সত্যিই কিছু একটা check করছে।
- **Green** — test pass করানোর জন্য সবচেয়ে কম code লিখুন (green)। বেশি বানাবেন না।
- **Refactor** — এখন যেহেতু green, code আর test পরিষ্কার করুন। জানেন যে test যেকোনো ভুল ধরে ফেলবে।

ব্যাপারটা এমন — safety net আগে থেকেই টাঙিয়ে তারপর কাজ শুরু করা: আগে net (fail করা test) বসান, তারপর উপরে ওঠেন।

**ধাপ ২ — একটা ছোট বাস্তব উদাহরণ।**
ধরুন আমাদের একটা `Discount` class দরকার, যেটা 1000 BDT-র উপরে 10% ছাড় দেয়।

```dart
// RED: আগে test লিখুন (class এখনো নেই)
test('applies 10% discount above 1000', () {
  expect(Discount().apply(2000), 1800);
});

// GREEN: pass করানোর মতো সবচেয়ে ছোট code
class Discount {
  double apply(double amount) => amount > 1000 ? amount * 0.9 : amount;
}

// REFACTOR: আরেকটা test যোগ করুন, দরকার হলে পরিষ্কার করুন
test('no discount at or below 1000', () {
  expect(Discount().apply(1000), 1000);
});
```

**ধাপ ৩ — এটা design-এ কীভাবে সাহায্য করে।**
নিজের code তৈরি হওয়ার আগেই আপনি সেটা call করছেন। তাই বাজে API আগেভাগেই খারাপ লাগে। Test setup করা কঠিন হলে design সম্ভবত বেশি জট পাকানো। TDD আপনাকে ছোট, injectable, testable অংশের দিকে ঠেলে দেয় — আর এটাই এই section-এর বাকি সব সহজ করে তোলে।

**ধাপ ৪ — কোথায় ব্যবহার করবেন (সৎভাবে বলুন)।**
- **খুব ভালো মানায়:** business logic, parsing, হিসাব, repository, আর bug ঠিক করা (আগে এমন test লিখুন যেটা bug-টা আবার ঘটায়, তারপর ঠিক করুন যাতে সেটা আর কখনো ফিরে না আসে)।
- **ঢিলেঢালা মানায়:** pixel-level UI। সাধারণত আপনি আগে widget বানান, তারপর widget আর golden test যোগ করেন। দেখতে-কেমন লাগে এমন জিনিসে কড়া test-first ধীর আর কম কাজের।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি red, green, refactor loop বলতে পারেন কি না। আর সেটা *বাস্তব বুদ্ধি* দিয়ে ব্যবহার করেন কি না — ধর্ম হিসেবে নয়, বরং যে জায়গায় লাভ হয় সেখানে হাতে তুলে নেওয়া একটা tool হিসেবে।

**সাধারণ ভুল:** বলা যে TDD মানে "সব কিছুতে 100% test-first"। আসল senior-রা এটা সেখানেই লাগান যেখানে লাভ হয় (logic, bug fix)। আর ঘাঁটাঘাঁটির UI কাজে ঢিল দেন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আগে test লেখার লাভ কী?"* → এতে প্রমাণ হয় test fail করতে পারে। আর implementation-এর প্রতি মায়া পড়ার আগেই behavior পাকা হয়ে যায়।
- *"TDD bug-এ কীভাবে সাহায্য করে?"* → একটা fail করা test দিয়ে bug-টা আবার ঘটান, code ঠিক করুন। Test পাহারাদার হয়ে থেকে যায়, তাই bug আর ফিরতে পারে না (একটা regression test)।

**সম্পর্কিত:** [Q2 — test pyramid](#q2) · [Q4 — unit primitives](#q4)

[↑ উপরে ফিরুন](#toc)

---

# B. Unit testing-এর মূল বিষয়

---

## <a id="q4"></a>4. মূল unit testing primitive-গুলো ব্যাখ্যা করুন — `test`, `expect`, `group`, `setUp`, `tearDown`।

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`test` একটা test case ঠিক করে দেয়। `expect` একটা value-কে matcher দিয়ে check করে। `group` সম্পর্কিত test-গুলোকে একটা label-এর নিচে বেঁধে রাখে। `setUp` প্রতিটা test-এর আগে চলে, তাই পরিষ্কার শুরু পাওয়া যায়। আর `tearDown` প্রতিটা test-এর পরে চলে পরিষ্কার করার জন্য। `setUpAll` আর `tearDownAll`-ও আছে, যেগুলো পুরো group-এর জন্য একবার চলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `test`: একটা test case।**
এটা একটা বর্ণনা নেয় আর একটা function নেয়, যার ভেতরে আপনার check-গুলো থাকে।

```dart
test('adds two numbers', () {
  expect(2 + 3, 5);
});
```

**ধাপ ২ — `expect`: check করার জায়গা।**
`expect(actual, matcher)` আসল value-র সাথে আপনার প্রত্যাশার তুলনা করে। খালি একটা value দিলে মানে "equals"। Flutter আরও সমৃদ্ধ matcher দেয়, যেমন `equals`, `isTrue`, `throwsA`, `isA<Type>()`, আর `contains` (দেখুন [Q5](#q5))।

```dart
expect(calc.add(2, 3), equals(5));   // value matcher
expect(list, contains('Alice'));     // collection matcher
```

**ধাপ ৩ — `group`: সম্পর্কিত test একসাথে বাঁধা।**
`group` সম্পর্কিত test-গুলোকে এক label-এর নিচে রাখে। এতে output পড়তে সুবিধা হয়, আর তারা setup ভাগাভাগি করতে পারে। Group-এর ভেতরে group রাখা যায়।

**ধাপ ৪ — `setUp` আর `tearDown`: প্রতিবার পরিষ্কার শুরু।**
নির্ভরযোগ্য test-এর জন্য এটাই সবচেয়ে গুরুত্বপূর্ণ ধারণা। `setUp` চলে **প্রতিটা test-এর আগে**। তাই প্রতিটা test নতুন করে শুরু হয়, আর তারা পুরোনো state ভাগাভাগি করে না। `tearDown` চলে **প্রতিটা test-এর পরে**, resource ছেড়ে দেওয়ার জন্য।

`setUp`-কে ভাবুন প্রতিটা নতুন অঙ্কের আগে whiteboard মুছে ফেলার মতো — যাতে আগের test-এ যা লিখেছিলেন সেটা পরেরটাকে গুলিয়ে না দেয়।

```dart
import 'package:test/test.dart';

void main() {
  group('Calculator', () {
    late Calculator calc;

    setUp(() {
      calc = Calculator();   // প্রতিটা test-এর আগে নতুন instance
    });

    tearDown(() {
      calc.dispose();        // প্রতিটা test-এর পরে পরিষ্কার
    });

    test('adds two numbers', () {
      expect(calc.add(2, 3), equals(5));
    });

    test('throws on division by zero', () {
      expect(() => calc.divide(10, 0), throwsA(isA<ArgumentError>()));
    });

    group('subtraction', () {          // ভেতরের group
      test('subtracts positives', () {
        expect(calc.subtract(5, 3), equals(2));
      });
      test('handles negative results', () {
        expect(calc.subtract(3, 5), equals(-2));
      });
    });
  });
}
```

**ধাপ ৫ — `setUpAll` / `tearDownAll`: পুরো group-এর জন্য একবার চলে।**
ব্যয়বহুল এককালীন কাজে এগুলো ব্যবহার করুন, যেমন একটা fixture file load করা বা fallback value register করা — যে জিনিস প্রতিটা test-এ নতুন লাগবে, তার জন্য নয়।

```dart
setUpAll(() => loadFixtures());   // group-এর সব test-এর আগে একবার চলে
tearDownAll(() => closeDb());     // সব test-এর পরে একবার চলে
```

**Interviewer কেন জিজ্ঞেস করে:** এগুলোই ভিত্তি। ঠিকভাবে isolation রেখে এগুলো ব্যবহার করতে না পারলে testing-এর বাকি সব বিষয় ভেঙে পড়ে।

**সাধারণ ভুল:** `setUp`-এর বাইরে ভাগাভাগি করা object বানানো (যেমন top-level variable হিসেবে)। এতে test-গুলো একই mutable instance আবার ব্যবহার করে। তখন test order-এর উপর নির্ভরশীল হয়ে যায় আর এলোমেলো fail করে। সবসময় `setUp`-এ নতুন state বানান।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`setUp` বনাম `setUpAll`?"* → `setUp` চলে *প্রতিটা* test-এর আগে (নতুন state)। `setUpAll` চলে পুরো group-এর জন্য *একবার* (ব্যয়বহুল ভাগাভাগি করা setup)।
- *"কোনো কিছু throw করে কি না সেটা কীভাবে test করবেন?"* → `expect`-এ একটা function পাঠান `throwsA` দিয়ে: `expect(() => calc.divide(1, 0), throwsA(isA<ArgumentError>()))`।

**সম্পর্কিত:** [Q5 — matchers](#q5) · [Q3 — TDD](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Matcher কী? `equals`, `throwsA`, `isA`, `contains`, আর async matcher ব্যাখ্যা করুন।

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Matcher হলো `expect`-এর দ্বিতীয় argument — এটা বলে দেয় value-টাকে কোন নিয়ম মানতে হবে, শুধু একটা নির্দিষ্ট value নয়। সহজগুলো হলো `equals`, `isTrue`, `isNull`। `isA<T>()` type check করে, `contains` collection check করে, আর `throwsA` দেখে function throw করে কি না। Future-এর জন্য আমি `expectLater` ব্যবহার করি `completion` বা `throwsA`-র সাথে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Matcher একটা নিয়ম, শুধু একটা value নয়।**
`expect(actual, matcher)` পড়তে প্রায় English-এর মতো: "expect actual to ..."। খালি একটা value দিলে সেটা `equals`-এর সংক্ষিপ্ত রূপ।

```dart
expect(2 + 2, 4);            // equals(4)-এর সমান
expect(2 + 2, equals(4));    // স্পষ্ট করে লেখা
```

**ধাপ ২ — সাধারণ value আর type matcher।**

```dart
expect(name, isNotNull);
expect(isReady, isTrue);
expect(user, isA<User>());           // runtime type check করে
expect(0.1 + 0.2, closeTo(0.3, 0.0001)); // double-এর জন্য (হুবহু == এড়ান)
```

**ধাপ ৩ — Collection matcher।**

```dart
expect([1, 2, 3], contains(2));
expect([1, 2, 3], hasLength(3));
expect(<int>[], isEmpty);
expect([1, 2, 3], containsAll([3, 1]));   // order-এ কিছু আসে যায় না
```

**ধাপ ৪ — Code throw করে কি না test করা (`throwsA`)।**
একটা *function* পাঠান (call-এর ফলাফল নয়), যাতে `expect` সেটা চালিয়ে error ধরতে পারে।

```dart
expect(() => int.parse('abc'), throwsFormatException);
expect(() => calc.divide(1, 0), throwsA(isA<ArgumentError>()));

// error-এর message-ও check করুন:
expect(
  () => login(''),
  throwsA(isA<AuthException>().having((e) => e.message, 'message', 'empty user')),
);
```

`.having(...)` দিয়ে throw হওয়া object-এর একটা field assert করা যায় — পরিষ্কার আর নির্ভুল।

**ধাপ ৫ — Async matcher (খুব গুরুত্বপূর্ণ)।**
`Future`-এর জন্য `expectLater` ব্যবহার করুন (এটা একটা future ফেরত দেয়, যেটা আপনাকে `await` করতে হবে), সাথে `completion` বা `throwsA`।

```dart
await expectLater(repo.fetchUser(1), completion(isA<User>()));
await expectLater(repo.fetchUser(-1), throwsA(isA<NotFoundException>()));

// Stream-এর জন্য, কোন value কোন order-এ আসে সেটা check করুন:
await expectLater(counterStream, emitsInOrder([1, 2, 3]));
```

**Interviewer কেন জিজ্ঞেস করে:** ভালো matcher fail-এর কারণ পড়ার মতো করে তোলে। `expect(user, isA<User>())` একটা স্পষ্ট বার্তা দেখায়; হাতে লেখা `if` আর `fail()` সেটা দেয় না।

**সাধারণ ভুল:** `throwsA`-তে function পাঠানোর বদলে function-টা call করে ফেলা: `expect(int.parse('abc'), ...)` throw-টা ঘটায় `expect` ধরার *আগেই*। সবসময় `() => int.parse('abc')` পাঠান। আরেকটা ভুল: future-এর জন্য `expectLater`-এর বদলে `expect` ব্যবহার করা। তখন future শেষ হওয়ার আগেই test pass হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Future-এর জন্য `expectLater` কেন?"* → এটা এমন একটা future ফেরত দেয় যেটা matcher মিলে গেলে complete হয়। আপনি সেটা `await` করেন, তাই test আসল ফলাফলের জন্য অপেক্ষা করে।
- *"Double কীভাবে তুলনা করবেন?"* → `closeTo(value, delta)` ব্যবহার করুন, কারণ floating-point হিসাব খুব কমই হুবহু মেলে।

**সম্পর্কিত:** [Q4 — `test`/`expect`](#q4) · [Q8 — async tests](#q8)

[↑ উপরে ফিরুন](#toc)

---

# C. Widget testing

---

## <a id="q6"></a>6. Widget testing কীভাবে কাজ করে — `pumpWidget`, `find`, `tap`, `pump`, আর `pumpAndSettle` ব্যাখ্যা করুন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Widget test একটা `WidgetTester` ব্যবহার করে। এটা widget-কে একটা headless test engine-এ render করে, আর তার সাথে interact করে। `pumpWidget` tree build আর render করে। `find` widget খুঁজে বের করে। `tap` একটা gesture চালায়। মূল ব্যাপারটা হলো: tap বা state change-এর পরে UI নিজে থেকে rebuild হয় না — আমাকে `pump` call করে এক frame এগোতে হয়, অথবা `pumpAndSettle` দিয়ে animation শেষ না হওয়া পর্যন্ত সব frame চালাতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `pumpWidget`: screen চালু করা।**
`pumpWidget(widget)` আপনার widget tree-কে inflate আর render করে — ভাবুন এটা "এই screen-টা খোলো"। আপনি প্রায় সবসময় widget-টাকে `MaterialApp`-এ মুড়ে দেবেন। কারণ অনেক widget-এর `MediaQuery`, `Theme`, বা `Navigator`-এর মতো ancestor দরকার হয়।

```dart
await tester.pumpWidget(const MaterialApp(home: LoginScreen()));
```

**ধাপ ২ — `find`: tree-তে widget খুঁজে বের করা।**
`find` আপনাকে finder দেয়, যা widget-এর দিকে নির্দেশ করে (পুরোটা আছে [Q7](#q7)-এ)।

```dart
find.byType(ElevatedButton);            // widget type দিয়ে
find.byKey(const Key('email_field'));   // key দিয়ে
find.text('Login');                     // দৃশ্যমান text দিয়ে
find.byIcon(Icons.add);                 // icon দিয়ে
```

**ধাপ ৩ — `tap` / `enterText`: interact করা।**
এগুলো user-এর কাজ নকল করে। একটা finder যদি একাধিক widget-এর সাথে মেলে, তাহলে সেটাকে সরু করুন (যেমন `.first`) — নাহলে error দেবে।

```dart
await tester.tap(find.byType(ElevatedButton));
await tester.enterText(find.byKey(const Key('email_field')), 'user@test.com');
```

**ধাপ ৪ — সবচেয়ে জরুরি ধারণা: পরিবর্তন দেখতে `pump` করতেই হবে।**
আসল app-এ Flutter নিজেই screen rebuild করে। Test-এ কিন্তু **সময় জমে থাকে** যতক্ষণ না আপনি একটা frame চান। তাই tap বা `setState`-এর পরে আপনি `pump()` call করেন। এটা ঠিক এক frame এগোয়, আর নতুন UI দেখায়।

Widget test-কে সিনেমা নয়, comic book ভাবুন। কিছুই নিজে থেকে নড়ে না — আপনি প্রতিটা পাতা উল্টান (`pump`), তখন পরের ছবিটা দেখেন।

```dart
await tester.tap(find.byIcon(Icons.add));
await tester.pump();                 // একটা পাতা উল্টান (এক frame)
expect(find.text('1'), findsOneWidget);
```

**ধাপ ৫ — `pumpAndSettle`: সব থামা পর্যন্ত frame চালানো।**
আপনার action যদি animation চালু করে (page transition, একটা `AnimatedContainer`), তাহলে একটা `pump` যথেষ্ট নয়। `pumpAndSettle()` frame চালাতেই থাকে যতক্ষণ না কোনো animation বা scheduled frame বাকি থাকে। এর একটা timeout আছে, তাই এটা অসীম loop-এ পড়ে না।

```dart
await tester.tap(find.text('Next'));
await tester.pumpAndSettle();        // page transition শেষ হওয়ার অপেক্ষা
expect(find.byType(HomePage), findsOneWidget);
```

সাধারণ নিয়ম: `pump()` ব্যবহার করুন যখন আপনি ঠিক জানেন কয়টা frame দরকার (বা একটা নির্দিষ্ট duration এগোতে হবে)। `pumpAndSettle()` ব্যবহার করুন যখন আগে একটা animation শেষ হতেই হবে। অসীম animation-এর সাথে (যেমন loading spinner) `pumpAndSettle` **কখনোই** ব্যবহার করবেন না — এটা timeout করবে।

**ধাপ ৬ — সব একসাথে।**

```dart
testWidgets('Login button enables when the form is valid', (tester) async {
  await tester.pumpWidget(const MaterialApp(home: LoginScreen()));

  final button = find.byType(ElevatedButton);
  expect(tester.widget<ElevatedButton>(button).enabled, isFalse); // শুরুতে disabled

  await tester.enterText(find.byKey(const Key('email_field')), 'user@test.com');
  await tester.enterText(find.byKey(const Key('password_field')), 'Secure123!');
  await tester.pump();                 // টাইপ করার পরে rebuild

  expect(tester.widget<ElevatedButton>(button).enabled, isTrue);   // এখন enabled

  await tester.tap(button);
  await tester.pumpAndSettle();        // navigation animation-এর অপেক্ষা
  expect(find.byType(HomePage), findsOneWidget);
});
```

**Interviewer কেন জিজ্ঞেস করে:** Widget testing-এ Flutter-এর testing story সবচেয়ে ভালো ফোটে। তাঁরা দেখতে চান আপনি manual frame-pumping model বুঝেছেন কি না — এই জিনিসটাই নতুনদের অবাক করে।

**সাধারণ ভুল:** `tap()`-এর পরে `pump()` দিতে ভুলে যাওয়া, তারপর `expect` fail করলে অবাক হওয়া — UI তো এখনো rebuild-ই হয়নি। আরেকটা পরিচিত ভুল: `MaterialApp`-এ না মোড়া, তারপর "No MediaQuery ancestor" error খাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`pump` vs `pumpAndSettle`?"* → `pump` এক frame এগোয় (বা দেওয়া duration অনুযায়ী)। `pumpAndSettle` animation শেষ না হওয়া পর্যন্ত pump করতে থাকে।
- *"`pumpAndSettle` timeout করলে কী?"* → সম্ভবত একটা অসীম animation আছে (যেমন spinner)। তার বদলে নির্দিষ্ট `pump(duration)` ব্যবহার করুন।

**সম্পর্কিত:** [Q7 — finders](#q7) · [Q8 — duration সহ `pump`](#q8) · [Q13 — Cubit সহ screen test করা](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. Finder কীভাবে কাজ করে — `find.byType`, `byKey`, `text`, `byIcon`, আর `widgetWithText`?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Finder হলো test tree-তে কোন widget খুঁজতে হবে তার একটা বর্ণনা — যতক্ষণ না একটা `WidgetTester` এটা ব্যবহার করে, ততক্ষণ এটা কিছুই আনে না। বেশি ব্যবহৃতগুলো হলো `byType`, `byKey`, `text`, আর `byIcon`। আমি ফলাফল check করি `findsOneWidget`, `findsNothing`, বা `findsNWidgets(n)` দিয়ে। একাধিক widget মিলে গেলে আমি একটা `Key` যোগ করি, যাতে ঠিক একটাকে ধরা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Finder একটা query, widget নয়।**
`find.text('Hi')` অনেকটা search query-র মতো — "Hi লেখা `Text` widget খোঁজো"। `tester` যখন এটা চালায় (`tap`, `expect` ইত্যাদিতে), তখনই কেবল খোঁজাটা হয়।

**ধাপ ২ — প্রতিদিনের finder-গুলো।**

```dart
find.byType(ElevatedButton);          // widget type দিয়ে
find.byKey(const Key('submit'));      // widget-এ আপনার বসানো Key দিয়ে
find.text('Welcome');                 // ঠিক এই text-ওয়ালা একটা Text widget
find.textContaining('Wel');           // যে text-এ এই অংশটা আছে
find.byIcon(Icons.add);               // একটা Icon widget
find.byWidget(myExactWidgetInstance); // নির্দিষ্ট একটা widget instance
```

**ধাপ ৩ — নিখুঁত করতে finder মেলানো।**
আসল screen-এ অনেক button আর text থাকে। ঠিকঠাক ধরতে মিলিয়ে নিন:

```dart
// যে button-এ 'Save' text আছে
find.widgetWithText(ElevatedButton, 'Save');
// যে icon button-এ delete icon আছে
find.widgetWithIcon(IconButton, Icons.delete);
// descendant: নির্দিষ্ট একটা Card-এর ভেতরের 'Total' Text
find.descendant(of: find.byType(Card), matching: find.text('Total'));
```

**ধাপ ৪ — Match-count matcher (কীভাবে assert করবেন)।**

```dart
expect(find.text('Welcome'), findsOneWidget);    // ঠিক একটা
expect(find.text('Error'), findsNothing);        // একটাও না
expect(find.byType(ListTile), findsNWidgets(3)); // ঠিক তিনটা
expect(find.byType(ListTile), findsWidgets);     // এক বা তার বেশি
```

**ধাপ ৫ — একাধিক মিলে গেলে `Key` ব্যবহার করুন।**
দুটো widget যদি finder-এর চোখে একইরকম দেখায় (যেমন দুটো `ElevatedButton`), তাহলে যেটা দরকার সেটাকে একটা `Key` দিন। তারপর সরাসরি সেটাই খুঁজুন। ভঙ্গুর `.at(2)` indexing এড়ানোর সবচেয়ে পরিষ্কার উপায় এটাই।

```dart
// widget-এ:
ElevatedButton(key: const Key('login_button'), onPressed: ..., child: ...);

// test-এ:
await tester.tap(find.byKey(const Key('login_button')));
```

`.first` / `.last` / `.at(index)` তখনই ব্যবহার করুন যখন key দিলে জিনিসটা এলোমেলো লাগবে, আর order সত্যিই স্থির।

**Interviewer কেন জিজ্ঞেস করে:** প্রতিটা widget test-এর অর্ধেক কাজই হলো widget খুঁজে বের করা। এলোমেলো finder flaky test তৈরি করে, যা ছোট UI পরিবর্তনেই ভেঙে যায়।

**সাধারণ ভুল:** অনেক `Text` widget থাকা অবস্থায় `find.byType(Text)` ব্যবহার করা। তখন finder একাধিক widget-এর সাথে মেলে, আর test error দেয়। একটা `Key` যোগ করুন, বা `find.widgetWithText` ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`findsOneWidget` vs `findsWidgets`?"* → `findsOneWidget`-এ ঠিক একটা লাগবেই; `findsWidgets` এক বা তার বেশি মেনে নেয়।
- *"একটা widget-এর property কীভাবে পড়বেন?"* → `tester.widget<ElevatedButton>(finder).enabled` পাওয়া widget-টাকে cast করে, ফলে আপনি সেটা পরীক্ষা করতে পারেন।

**সম্পর্কিত:** [Q6 — widget testing](#q6) · [Q18 — key বুদ্ধি করে ব্যবহার](#q18)

[↑ উপরে ফিরুন](#toc)

---

# D. Test-এ async ও সময়

---

## <a id="q8"></a>8. Async code আর time-based logic কীভাবে test করেন — `async` test, `fakeAsync`, আর সময় এগিয়ে নেওয়া?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Mock করা API call-এর মতো দ্রুত async কাজের জন্য আমি শুধু test-টাকে `async` বানাই আর future-টা `await` করি। Debounce, polling, বা timeout-এর মতো time-based logic-এর জন্য আমি সত্যিকারের অপেক্ষা করি না — সময়টাকেই নিয়ন্ত্রণ করি। Unit test-এ `fakeAsync` আর `async.elapse(...)`, আর widget test-এ `tester.pump(duration)`। লক্ষ্য হলো দ্রুত ও deterministic test, কোনো আসল `sleep` ছাড়া।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সহজ ক্ষেত্র: `await` দিয়ে আসল async।**
Test function-টাকে `async` চিহ্নিত করুন আর future-টা `await` করুন। Test runner এর জন্য অপেক্ষা করে। কাজটা দ্রুত হলে (mock করা) এটুকুই যথেষ্ট।

```dart
test('fetchUser returns user from API', () async {
  when(() => mockApi.getUser(1)).thenAnswer((_) async => User(id: 1, name: 'Alice'));

  final user = await repository.fetchUser(1);

  expect(user.name, 'Alice');
});
```

**ধাপ ২ — সমস্যা: আসল delay test-কে ধীর আর flaky করে।**
ধরুন আপনার search box API call করার আগে 500ms অপেক্ষা করে (debounce)। আপনার test যদি সত্যিই 500ms অপেক্ষা করত, তাহলে পুরো suite হামাগুড়ি দিত। আর timing-এর কারণে এটা flaky হতো। তার বদলে আমাদের *ঘড়িটাকে নিয়ন্ত্রণ* করতে হবে।

`fakeAsync`-কে ভাবুন fast-forward বোতামওয়ালা একটা TV remote হিসেবে। অনুষ্ঠানটা (আপনার timer আর delay) আসল সময়ে চলে না — আপনি ঠিক যতটা চান ততটা fast-forward চাপেন, সাথে সাথে।

**ধাপ ৩ — খাঁটি unit test-এ `fakeAsync`।**
Test-টাকে `fakeAsync`-এ মুড়ে দিন। ভেতরে `Timer`, `Future.delayed`, আর `Stream.periodic` সত্যিই অপেক্ষা করে না — আপনি `async.elapse(duration)` দিয়ে সময় এগিয়ে নেন।

```dart
test('retry logic retries after 2 seconds', () {
  fakeAsync((async) {
    final service = RetryService();
    var attempts = 0;
    service.doWithRetry(() {
      attempts++;
      if (attempts < 3) throw Exception('fail');
    });

    async.elapse(Duration.zero);              // প্রথম চেষ্টা
    expect(attempts, 1);

    async.elapse(const Duration(seconds: 2)); // দ্বিতীয় চেষ্টা পর্যন্ত fast-forward
    expect(attempts, 2);

    async.elapse(const Duration(seconds: 2)); // আর তৃতীয়টা
    expect(attempts, 3);
  });
});
```

**ধাপ ৪ — Widget test-এ `pump(duration)` দিয়ে সময় এগিয়ে নেওয়া।**
Widget test-এ আপনি সরাসরি `fakeAsync` call করেন না — `testWidgets` আগে থেকেই ঘড়িটা fake করে রাখে। আপনি `pump`-এ একটা `Duration` পাঠিয়ে সময় এগিয়ে নেন।

```dart
testWidgets('Debounced search waits 500ms before calling the API', (tester) async {
  await tester.pumpWidget(MaterialApp(home: SearchScreen()));

  await tester.enterText(find.byType(TextField), 'flutter');

  // 200ms পরে API এখনো call হওয়ার কথা নয়
  await tester.pump(const Duration(milliseconds: 200));
  verifyNever(() => mockSearchApi.search(any()));

  // আরও 300ms পরে (মোট 500ms) এটা ঠিক একবার চলে
  await tester.pump(const Duration(milliseconds: 300));
  verify(() => mockSearchApi.search('flutter')).called(1);
});
```

**ধাপ ৫ — কোন সময় কোনটা ব্যবহার করবেন, দ্রুত গাইড।**

| পরিস্থিতি | যা ব্যবহার করবেন |
|---|---|
| দ্রুত mock করা future | `async` test + `await` |
| খাঁটি Dart-এ timer/debounce/timeout | `fakeAsync` + `async.elapse(...)` |
| Widget test-এ সময় পার হওয়া | `tester.pump(duration)` |

**Interviewer কেন জিজ্ঞেস করে:** আসল app async আর timer-এ ভরা। তাঁরা দেখতে চান আপনি সময়-নির্ভর আচরণ *deterministic*ভাবে test করেন কি না — কোনো আসল অপেক্ষা নয়, ঘড়ির উপর পূর্ণ নিয়ন্ত্রণ।

**সাধারণ ভুল:** Debounce-এর জন্য "অপেক্ষা করতে" test-এ `await Future.delayed(Duration(seconds: 2))` ব্যবহার করা। এতে suite ধীর আর flaky হয়। সবসময় তার বদলে fake সময় এগিয়ে নিন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আসল delay-এর চেয়ে `fakeAsync` ভালো কেন?"* → এটা তাৎক্ষণিক আর deterministic — প্রতিবার একই ফলাফল, মাইক্রোসেকেন্ডে।
- *"Widget test-এ সময় কীভাবে এগিয়ে নেবেন?"* → `pump`-এ একটা `Duration` পাঠান, যেমন `await tester.pump(const Duration(seconds: 1))`।

**সম্পর্কিত:** [Q5 — async matchers](#q5) · [Q6 — `pump`](#q6) · [Q12 — bloc_test](#q12)

[↑ উপরে ফিরুন](#toc)

---

# E. Test double (mock আর fake)

---

## <a id="q9"></a>9. Mockito দিয়ে mocking কীভাবে কাজ করে — `@GenerateMocks`, `when`/`thenReturn`, আর `verify`?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Mockito আপনার dependency-গুলোর নকল version বানায়। ফলে একটা class আলাদা করে test করা যায়। এটা code generation ব্যবহার করে: আমি `@GenerateMocks` দিয়ে annotate করি, build_runner চালাই, আর এটা mock class-গুলো বানিয়ে দেয়। তারপর চক্রটা হলো: `when(...).thenReturn(...)` দিয়ে stub করা, code চালানো, আর `verify(...)` দিয়ে call check করা। Async method-এর জন্য আমি `thenReturn` নয়, `thenAnswer` ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Mock করার দরকার কেন?**
ধরুন একটা `UserRepository` test করছেন, যেটা আসল API call করে। আসল call ধীর, network লাগে, আর আপনার code-এর সাথে সম্পর্ক নেই এমন কারণেও fail করতে পারে। Mock হলো সিনেমার **stunt double**-এর মতো: আসল ঝুঁকিপূর্ণ actor-এর জায়গায় দাঁড়ায়, আর director (আপনার test) যা বলে ঠিক তাই করে।

**ধাপ ২ — Mock generate করা।**
একটা test-এ `@GenerateMocks([...])` annotate করুন আর build_runner চালান। Mockito আপনার জন্য একটা `MockApiClient` class বানিয়ে দেয়।

```dart
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';
import 'package:test/test.dart';

@GenerateMocks([ApiClient])            // MockApiClient generate করে
import 'user_repository_test.mocks.dart';
```

তারপর চালান:

```bash
dart run build_runner build --delete-conflicting-outputs
```

**ধাপ ৩ — তিন ধাপের চক্র: stub, act, verify।**
- **Stub** — `when(...).thenReturn(...)` দিয়ে mock-কে বলুন কী return করবে।
- **Act** — test-এর আসল code চালান।
- **Verify** — `verify(...)` দিয়ে check করুন mock প্রত্যাশা মতো call হয়েছে কি না।

```dart
void main() {
  late MockApiClient mockApi;
  late UserRepository repo;

  setUp(() {
    mockApi = MockApiClient();
    repo = UserRepository(api: mockApi);     // mock inject করা হলো
  });

  test('getUser calls the API and returns a parsed user', () async {
    // STUB
    when(mockApi.get('/users/1'))
        .thenAnswer((_) async => Response(data: {'id': 1, 'name': 'Alice'}));

    // ACT
    final user = await repo.getUser(1);

    // মান ASSERT করা
    expect(user.name, 'Alice');

    // interaction VERIFY করা
    verify(mockApi.get('/users/1')).called(1);
    verifyNoMoreInteractions(mockApi);
  });

  test('getUser throws when the API fails', () {
    when(mockApi.get(any)).thenThrow(NetworkException());
    expect(() => repo.getUser(1), throwsA(isA<NetworkException>()));
  });
}
```

**ধাপ ৪ — `thenReturn` বনাম `thenAnswer` (একটা গুরুত্বপূর্ণ খুঁটিনাটি)।**
সাধারণ মানের জন্য `thenReturn` ব্যবহার করুন। `Future` (async) হলে `thenAnswer((_) async => value)` ব্যবহার করুন। কারণ: `thenReturn(Future.value(x))` future-টা *একবারই* বানায়, আর প্রতিবার সেই একই instance ফেরত দেয়। এতে সূক্ষ্ম bug হয়। `thenAnswer` প্রতিবার নতুন করে চলে।

```dart
when(mockApi.ping()).thenReturn(true);                       // sync মান: ঠিক আছে
when(mockApi.get('/x')).thenAnswer((_) async => Response()); // async: thenAnswer ব্যবহার করুন
```

**ধাপ ৫ — Interaction নিখুঁতভাবে verify করা।**

```dart
verify(mockApi.get('/users/1')).called(1);   // ঠিক একবার
verifyNever(mockApi.delete(any));            // কখনোই call হয়নি
verifyNoMoreInteractions(mockApi);           // আর কিছুই call হয়নি
```

**Interviewer কেন জিজ্ঞেস করে:** Mockito হলো Dart-এর সবচেয়ে বেশি ব্যবহৃত mocking library। stub, act, verify চক্রটা যেকোনো testable architecture-এর জন্য অপরিহার্য।

**সাধারণ ভুল:** Async method-এ `thenAnswer`-এর বদলে `thenReturn` ব্যবহার করা। আরেকটা: `@GenerateMocks` যোগ করার পরে build_runner চালাতে ভুলে যাওয়া, তারপর "MockApiClient is undefined" error দেখে বিভ্রান্ত হওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Async-এর জন্য `thenAnswer` কেন?"* → এটা প্রতিবার call-এ নতুন future ফেরত দেয়; `thenReturn` একটাই future instance বারবার ব্যবহার করে, ফলে call-গুলোর মধ্যে state ছড়িয়ে পড়তে পারে।
- *"`verifyNoMoreInteractions` কী করে?"* → আপনি স্পষ্ট করে verify করেননি এমনভাবে mock-টা ছোঁয়া হলে এটা test fail করে দেয়।

**সম্পর্কিত:** [Q10 — Mocktail](#q10) · [Q11 — fake বনাম mock](#q11) · [Q14 — HTTP mocking](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. Mocktail আর Mockito-র মধ্যে পার্থক্য কী, আর কখন আপনি Mocktail বেছে নেবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Mocktail Mockito-র মতোই কাজ করে, কিন্তু কোনো code generation লাগে না — build_runner নেই, generated file নেই। আপনি শুধু `class MockX extends Mock implements X {}` লিখে দেন। Syntax-এ একটা closure ব্যবহার হয়: `when(() => mock.method())`। আর custom type-এর সাথে `any()` ব্যবহার করলে আগে একটা fallback value register করতে হয়। Setup সহজ রাখতে আর build দ্রুত রাখতে আমি Mocktail বেছে নিই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বড় পার্থক্য: কোনো code generation নেই।**
Mockito build_runner দিয়ে mock class generate করে। Mocktail এসবের কিছুই করে না — আপনি এক line-এ নিজে হাতে mock লিখে ফেলেন।

```dart
import 'package:mocktail/mocktail.dart';

// @GenerateMocks নেই, build_runner নেই, generated file নেই:
class MockApiClient extends Mock implements ApiClient {}
```

**ধাপ ২ — Closure syntax।**
সবচেয়ে চোখে পড়া পার্থক্য হলো `when` আর `verify`-এর ভেতরের `() =>` lambda। Code generation ছাড়া Mocktail এভাবেই call-টা ধরে নেয়।

```dart
// Mockito:  when(mockApi.getUser(1)).thenAnswer(...)
// Mocktail: when(() => mockApi.getUser(1)).thenAnswer(...)
when(() => mockApi.getUser(1)).thenAnswer((_) async => User(id: 1, name: 'Alice'));
verify(() => mockApi.getUser(1)).called(1);
```

**ধাপ ৩ — Custom type-এর জন্য `any()`-র fallback লাগে।**
`any()` দিয়ে কোনো argument match করছেন, আর সেই argument একটা custom class (`int`/`String` নয়) হলে Mocktail-এর ভেতরে ব্যবহারের জন্য একটা নমুনা মান লাগে। `registerFallbackValue` দিয়ে একবার register করে দিন, সাধারণত `setUpAll`-এ।

```dart
class FakeUserRequest extends Fake implements UserRequest {}

setUpAll(() {
  registerFallbackValue(FakeUserRequest());   // UserRequest-এ any() ব্যবহারের জন্য দরকার
});
```

**ধাপ ৪ — একটা পূর্ণ উদাহরণ।**

```dart
import 'package:mocktail/mocktail.dart';
import 'package:test/test.dart';

class MockApiClient extends Mock implements ApiClient {}
class FakeUserRequest extends Fake implements UserRequest {}

void main() {
  late MockApiClient mockApi;
  late UserRepository repo;

  setUpAll(() => registerFallbackValue(FakeUserRequest()));

  setUp(() {
    mockApi = MockApiClient();
    repo = UserRepository(api: mockApi);
  });

  test('creates a user via the API', () async {
    when(() => mockApi.createUser(any())).thenAnswer((_) async => User(id: 1, name: 'Alice'));

    final user = await repo.createUser(UserRequest(name: 'Alice'));

    expect(user.id, 1);
    verify(() => mockApi.createUser(any())).called(1);
  });
}
```

**ধাপ ৫ — কখন কোনটা বেছে নেবেন।**
- **Mocktail বেছে নিন** যখন সহজ setup চান, দ্রুত iteration চান (code gen নেই), বা নতুন project-এ কম ঝামেলা চান — বিশেষ করে যখন আপনি ইতিমধ্যে freezed আর json_serializable-এর মতো ভারী generator চালাচ্ছেন আর build time কমাতে চান।
- **Mockito বেছে নিন** যখন আপনার team আগে থেকেই এটা ব্যবহার করে, আপনি generated ও কঠোরভাবে typed mock পছন্দ করেন, বা build_runner pipeline আগে থেকেই বসানো আছে।

| | Mockito | Mocktail |
|---|---|---|
| Code generation | হ্যাঁ (`@GenerateMocks` + build_runner) | নেই |
| Mock বানানো | generated `MockX` | `class MockX extends Mock implements X {}` |
| Stub syntax | `when(mock.m())` | `when(() => mock.m())` |
| Custom type-এ `any()` | কাজ করে | `registerFallbackValue` লাগে |

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি একটা tool *কেন* বাছেন সেটা ব্যাখ্যা করতে পারেন কি না, শুধু কীভাবে ব্যবহার করতে হয় তা নয়। দুটোই জানা বাস্তব পরিপক্বতার লক্ষণ।

**সাধারণ ভুল:** Custom type-এর সাথে `any()` ব্যবহারের সময় `registerFallbackValue` দিতে ভুলে যাওয়া — তখন fallback না থাকা নিয়ে একটা স্পষ্ট runtime error পাবেন। আরেকটা: Mocktail-এ Mockito-র syntax (`when(mock.m())`) মিশিয়ে ফেলা, অথচ Mocktail closure form আশা করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Mocktail-এ closure কেন?"* → Code generation না থাকায় `() =>` Mocktail-কে বুঝিয়ে দেয় আপনি কোন method আর কোন argument বোঝাচ্ছেন।
- *"Mocktail কি type safety দেয়?"* → হ্যাঁ — `implements X` mock-টাকে আসল interface-এর সাথে বেঁধে দেয়, তাই ভুল method signature compile হবে না।

**সম্পর্কিত:** [Q9 — Mockito](#q9) · [Q11 — fake বনাম mock](#q11) · [Q12 — bloc_test mock ব্যবহার করে](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. Fake আর Mock-এর পার্থক্য কী — কোনটা কখন ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"দুটোই test double — আসল dependency-র জায়গায় বসা বিকল্প। Mock মনে রাখে তাকে কীভাবে call করা হয়েছে। তাই আমি `when` দিয়ে stub করি আর `verify` দিয়ে call check করি। যখন আমার দরকার dependency *কীভাবে* ব্যবহার হলো তা দেখা, তখন mock ব্যবহার করি। Fake হলো আসল, সরল একটা working implementation — যেমন in-memory database। এতে stubbing বা verifying নেই। Test-এর সময় শুধু কাজ করে এমন কিছু দরকার হলে fake ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুই ধরনের double, সহজ কথায়।**
- **Mock** = এমন একটা বিকল্প যে **মনে রাখে আপনি তাকে কী জিজ্ঞেস করেছেন**। আপনি তাকে বলে দেন কী return করবে (`when/thenReturn`)। পরে check করেন কী call হয়েছিল (`verify`)। এটা *behavior verification*-এর ব্যাপার।
- **Fake** = এমন একটা বিকল্প যে **সত্যিই কাজ করে**, শুধু সরল উপায়ে। যেমন একটা repository যা user-দের memory-তে একটা `List`-এ রাখে। কোনো stubbing নেই, কোনো verifying নেই — এটা ছোট আকারে আসল জিনিসের মতোই আচরণ করে।

উপমা: **mock** হলো sensor লাগানো crash-test dummy — কী তাকে আঘাত করল তা ঠিকঠাক check করেন। **Fake** হলো আসল machine-এর একটা সস্তা working prototype — এটা চলে, শুধু সরলভাবে।

**ধাপ ২ — একটা Fake: কাজ করা in-memory implementation।**

```dart
class FakeUserRepository implements UserRepository {
  final List<User> _users = [];

  @override
  Future<void> addUser(User user) async => _users.add(user);

  @override
  Future<User?> getUser(int id) async =>
      _users.where((u) => u.id == id).firstOrNull;

  @override
  Future<List<User>> getAllUsers() async => List.unmodifiable(_users);
}

// Test-এ ব্যবহার — stubbing লাগে না, এটা সত্যিই data রাখে:
test('UserService adds and retrieves a user', () async {
  final service = UserService(repository: FakeUserRepository());

  await service.registerUser('Alice');
  final users = await service.listUsers();

  expect(users, hasLength(1));
  expect(users.first.name, 'Alice');
});
```

**ধাপ ৩ — একটা Mock: interaction verify করা।**

```dart
test('UserService calls repository.addUser exactly once', () async {
  final mockRepo = MockUserRepository();
  when(() => mockRepo.addUser(any())).thenAnswer((_) async {});

  final service = UserService(repository: mockRepo);
  await service.registerUser('Alice');

  verify(() => mockRepo.addUser(any())).called(1);   // কীভাবে call হলো সেটাই আমাদের দরকার
});
```

**ধাপ ৪ — কীভাবে বাছবেন।**

```
Do you need to verify HOW the dependency was called?
   |
   Yes -> use a Mock  (call count, arguments, order)
   |
   No  -> Do you need a working implementation with simple behavior?
          |
          Yes -> use a Fake  (in-memory DB, local cache)
          |
          No  -> you probably don't need a test double at all
```

- **Fake ব্যবহার করুন** যখন কয়েকটা call-এর মধ্য দিয়ে behavior জমা হয় (state গুরুত্বপূর্ণ)। অথবা যখন প্রতিটা method stub করলে code এলোমেলো লাগবে।
- **Mock ব্যবহার করুন** যখন নিশ্চিত করতে হবে একটা method call হয়েছে (কতবার, কী argument দিয়ে)। অথবা side effect (network, disk) আটকাতে। অথবা `thenThrow` দিয়ে একটা failure বানাতে।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি জানেন "mocking" সব জায়গায় এক নয়। সঠিক double বাছলে test পরিষ্কার হয় আর কম ভাঙে — এটা testing পরিপক্বতার লক্ষণ।

**সাধারণ ভুল:** সব কিছু mock করা, এমনকি যেখানে ছোট একটা fake ভালো পড়া যায়। বেশি mock করলে test implementation detail-এর সাথে বাঁধা পড়ে। ফলে নিরীহ একটা refactor অনেক test ভেঙে দেয়, যদিও behavior বদলায়নি।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Fake কখন স্পষ্টভাবে ভালো?"* → stateful জিনিসের জন্য, যেমন in-memory store। সেখানে অনেক call-এর মধ্য দিয়ে data জমা হওয়া test করেন।
- *"তাহলে stub কী?"* → Stub শুধু আগে থেকে ঠিক করা উত্তর return করে (কোনো verification নেই)। Mockito/Mocktail-এ `when(...).thenReturn(...)` অংশটা stubbing। `verify` যোগ করলে সেটা mocking হয়ে যায়।

**সম্পর্কিত:** [Q9 — Mockito](#q9) · [Q10 — Mocktail](#q10) · [Q14 — HTTP mock করা](#q14)

[↑ উপরে ফিরুন](#toc)

---

# F. আসল app layer test করা

---

## <a id="q12"></a>12. `bloc_test` দিয়ে একটা BLoC বা Cubit কীভাবে test করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`bloc_test` package একটা `blocTest` helper দেয়, যার গঠন নির্দিষ্ট: build, দরকার হলে seed, act, expect, দরকার হলে verify। `act`-এর সময় BLoC যত state emit করে সব রেকর্ড করে। তারপর আমার expected list-এর সাথে মেলায়। দুটো জিনিস মনে রাখতে হয়: initial state expect list-এ থাকে না, আর state class-গুলো equatable হতে হবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `blocTest`-এর গঠন।**
`blocTest` একটা পরিষ্কার ধারাবাহিকতায় চলে:
- **build** — BLoC/Cubit বানান (mock করা dependency দিয়ে)।
- **seed** *(optional)* — `act`-এর আগে একটা শুরুর state বসান (নির্দিষ্ট state থেকে behavior test করতে)।
- **act** — কাজটা করুন: একটা event add করুন (BLoC) বা একটা method call করুন (Cubit)।
- **expect** — initial state-এর **পরে** emit হওয়া state-গুলোর তালিকা।
- **verify** *(optional)* — test-এর পরে বাড়তি check, যেমন একটা mock call নিশ্চিত করা।

**ধাপ ২ — happy path।**

```dart
import 'package:bloc_test/bloc_test.dart';
import 'package:mocktail/mocktail.dart';
import 'package:test/test.dart';

class MockUserRepository extends Mock implements UserRepository {}

void main() {
  late MockUserRepository mockRepo;
  setUp(() => mockRepo = MockUserRepository());

  group('UserCubit', () {
    blocTest<UserCubit, UserState>(
      'emits [loading, loaded] when fetchUser succeeds',
      build: () {
        when(() => mockRepo.getUser(1))
            .thenAnswer((_) async => User(id: 1, name: 'Alice'));
        return UserCubit(repository: mockRepo);
      },
      act: (cubit) => cubit.fetchUser(1),
      expect: () => [
        UserLoading(),                          // প্রথম emit হওয়া state
        UserLoaded(User(id: 1, name: 'Alice')), // দ্বিতীয়
      ],
    );
```

**ধাপ ৩ — failure path।**

```dart
    blocTest<UserCubit, UserState>(
      'emits [loading, error] when fetchUser fails',
      build: () {
        when(() => mockRepo.getUser(any())).thenThrow(ServerException('500'));
        return UserCubit(repository: mockRepo);
      },
      act: (cubit) => cubit.fetchUser(1),
      expect: () => [
        UserLoading(),
        const UserError('Failed to load user'),
      ],
    );
```

**ধাপ ৪ — `seed` আর `verify` ব্যবহার।**
`seed` cubit-কে বেছে নেওয়া একটা state থেকে শুরু করায়। `verify` পরে assertion চালায়।

```dart
    blocTest<UserCubit, UserState>(
      'refresh from a loaded state re-fetches the user',
      build: () {
        when(() => mockRepo.getUser(1))
            .thenAnswer((_) async => User(id: 1, name: 'Bob'));
        return UserCubit(repository: mockRepo);
      },
      seed: () => UserLoaded(User(id: 1, name: 'Alice')), // এখান থেকে শুরু
      act: (cubit) => cubit.fetchUser(1),
      expect: () => [
        UserLoading(),
        UserLoaded(User(id: 1, name: 'Bob')),
      ],
      verify: (_) {
        verify(() => mockRepo.getUser(1)).called(1);
      },
    );
  });
}
```

**ধাপ ৫ — equatable-এর নিয়ম (এখানে অনেকে আটকে যান)।**
`expect` আপনার expected state-গুলোকে emit হওয়া state-এর সাথে `==` দিয়ে মেলায়। Default অবস্থায় একই data-র দুটো আলাদা `UserLoaded` object সমান নয় (দেখুন Section 1, Q4)। তাই আপনার state class-গুলোতে value equality থাকতে হবে — `Equatable` বা `freezed` ব্যবহার করুন। এটা না থাকলে value মিললেও তুলনা fail করবে।

**Interviewer কেন জিজ্ঞেস করে:** Production Flutter-এ BLoC আর Cubit সবচেয়ে সাধারণ state management। `bloc_test` এগুলো test করার আদর্শ উপায়। তাঁরা আশা করেন আপনি এর গঠন মুখস্থ জানেন।

**সাধারণ ভুল:** `expect` তালিকায় initial state রেখে দেওয়া। `blocTest` শুধু initial/seed state-এর *পরে* emit হওয়া state check করে। আরেকটা চেনা ভুল হলো state class-গুলোকে equatable করতে ভুলে যাওয়া। ফলে value মিললেও `expect` fail করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`act`-এ BLoC আর Cubit-এর পার্থক্য?"* → BLoC-এর ক্ষেত্রে `act` একটা event add করে (`bloc.add(...)`)। Cubit-এর ক্ষেত্রে `act` একটা method call করে (`cubit.doThing()`)।
- *"Emit হওয়া error state আর throw হওয়া error কীভাবে test করেন?"* → emit হওয়া error *state*-এর জন্য `expect` ব্যবহার করুন। আর bloc থেকে *বেরিয়ে আসা* error assert করতে `errors` parameter ব্যবহার করুন।

**সম্পর্কিত:** [Q13 — Cubit দিয়ে একটা screen test করা](#q13) · [Q10 — Mocktail](#q10) · [Q8 — async test](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. যে screen (widget) একটা Cubit-এর উপর নির্ভর করে, সেটা কীভাবে test করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি Cubit-টা mock করি আর `BlocProvider.value` দিয়ে inject করি। ফলে widget test শুধু UI-তেই সীমিত থাকে। আমি Cubit-এর `state`-কে আমার দরকারি state-এ stub করি, screen render করি, তারপর UI মিলছে কি না assert করি। সবচেয়ে সহজ উপায় হলো `bloc_test`-এর `MockCubit` helper — এটা `state` আর `stream` দুটোই আমার হয়ে সামলায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Cubit কেন mock করবেন (আসলটা কেন নয়)?**
Widget test-এ আপনি *screen* test করতে চান, business logic নয়। আসল Cubit ব্যবহার করলে তার repository, network — সবই সাথে চলে আসে। তখন এটা একটা ছোট integration test হয়ে যায়। Cubit mock করলে আপনি বলতে পারেন "ধরো state এখন loading"। তারপর screen ঠিকভাবে সাড়া দিচ্ছে কি না দেখতে পারেন।

**ধাপ ২ — `bloc_test`-এর `MockCubit` ব্যবহার করুন।**
`MockCubit` সঠিকভাবে `state` getter আর `stream` — দুটোই fake করে। widget-গুলো এই দুটোই শোনে।

```dart
import 'package:bloc_test/bloc_test.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mocktail/mocktail.dart';

class MockUserCubit extends MockCubit<UserState> implements UserCubit {}

void main() {
  late MockUserCubit mockCubit;
  setUp(() => mockCubit = MockUserCubit());
```

**ধাপ ৩ — state stub করুন, তারপর `BlocProvider.value` দিয়ে Cubit দিন।**
`.value` ব্যবহার করুন (`create:` নয়)। তাহলে mock-এর lifecycle test-এর হাতে থাকে।

```dart
  testWidgets('shows a spinner when state is UserLoading', (tester) async {
    when(() => mockCubit.state).thenReturn(UserLoading());

    await tester.pumpWidget(
      MaterialApp(
        home: BlocProvider<UserCubit>.value(
          value: mockCubit,
          child: const UserScreen(),
        ),
      ),
    );

    expect(find.byType(CircularProgressIndicator), findsOneWidget);
  });

  testWidgets('shows the user name when state is UserLoaded', (tester) async {
    when(() => mockCubit.state).thenReturn(UserLoaded(User(id: 1, name: 'Alice')));

    await tester.pumpWidget(
      MaterialApp(
        home: BlocProvider<UserCubit>.value(value: mockCubit, child: const UserScreen()),
      ),
    );

    expect(find.text('Alice'), findsOneWidget);
  });
```

**ধাপ ৪ — UI action সত্যিই Cubit-কে call করছে কি না test করুন।**
Error state-এর ক্ষেত্রে "retry" tap করলে সঠিক method call হচ্ছে কি না, সেটাও দেখুন।

```dart
  testWidgets('error state shows a retry button that calls the cubit', (tester) async {
    when(() => mockCubit.state).thenReturn(const UserError('Connection failed'));

    await tester.pumpWidget(
      MaterialApp(
        home: BlocProvider<UserCubit>.value(value: mockCubit, child: const UserScreen()),
      ),
    );

    expect(find.text('Connection failed'), findsOneWidget);
    expect(find.byKey(const Key('retry_button')), findsOneWidget);

    await tester.tap(find.byKey(const Key('retry_button')));
    verify(() => mockCubit.fetchUser(any())).called(1);   // UI cubit-এর সাথে যুক্ত
  });
}
```

**ধাপ ৫ — যদি `MockCubit` ব্যবহার না করেন।**
নিজে হাতে `class MockUserCubit extends Mock implements UserCubit {}` লিখলে আপনাকে `state` আর `stream` — **দুটোই** stub করতে হবে। না করলে `BlocBuilder` throw করবে, কারণ সে listen করতে পারে না। `MockCubit` এই কাজটা আপনার হয়ে করে দেয় — তাই এটাই পছন্দের উপায়।

**Interviewer কেন জিজ্ঞেস করে:** বাস্তব Flutter test-এ এটা সবচেয়ে সাধারণ পরিস্থিতিগুলোর একটা। BLoC/Cubit দিয়ে চলা প্রতিটা screen-এ এই pattern লাগে। তাঁরা আপনাকে সাথে সাথে লিখে দেখাতে বলতে পারেন।

**সাধারণ ভুল:** আসল Cubit ব্যবহার করে *তার* dependency-গুলো mock করা — এতে একটা লক্ষ্যভিত্তিক widget test ভঙ্গুর আধা-integration test হয়ে যায়। আরেকটা ভুল: `BlocProvider.value(...)`-এর বদলে `BlocProvider(create: ...)` ব্যবহার করা — `create` lifecycle নিজের হাতে নেয়, কিন্তু test-এ আপনি mock-টা নিজে নিয়ন্ত্রণ করতে চান।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`.value` আর `create:`-এর পার্থক্য?"* → `.value` আপনার নিয়ন্ত্রণে থাকা একটা তৈরি instance দেয় (mock)। `create:` নিজেই একটা বানায় আর dispose করে — test-এর জন্য ভুল।
- *"State-এর একটা ধারা (loading তারপর loaded) কীভাবে test করবেন?"* → `bloc_test`-এর `whenListen(mockCubit, Stream.fromIterable([...]))` ব্যবহার করে emit হওয়া state-গুলো সাজিয়ে দিন।

**সম্পর্কিত:** [Q12 — bloc_test](#q12) · [Q6 — widget testing](#q6) · [Q11 — mocks](#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. যে repository একটা HTTP API call করে, সেটা কীভাবে test করবেন — Dio বা `http` কীভাবে mock করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Unit test-এ কখনোই আসল network call করবেন না। এর বদলে আমি HTTP client-টা repository-তে inject করি আর ঠিক ওই সীমানায় mock করি। `http` package-এর জন্য আমি `package:http/testing`-এর `MockClient` ব্যবহার করি। Dio-র জন্য আমি Mocktail দিয়ে `Dio` instance mock করি। সবচেয়ে ভালো হলো client-টাকে আমার নিজের interface-এর পেছনে লুকিয়ে রাখা — তখন mock বসানো খুব সহজ হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সোনালি নিয়ম: সীমানায় mock করুন, client inject করুন।**
Repository তার client constructor-এর মাধ্যমে পাবে, ভেতরে কখনোই বানাবে না। তখন test-এ আপনি একটা fake client পাস করবেন। Repository যদি ভেতরে `Dio()` করে, আপনি সেটা বদলাতে পারবেন না — তখন এটা untestable হয়ে যায়।

**ধাপ ২ — `MockClient` দিয়ে `http` package mock করা।**
`MockClient` একটা function নেয়: সেটা request পায় আর একটা fake response ফেরত দেয়। আপনি ভেতরেই request-টা assert করতে পারেন।

```dart
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';

test('fetchUser parses the response', () async {
  final mockClient = MockClient((request) async {
    expect(request.url.path, '/api/users/1');   // request assert করুন
    expect(request.method, 'GET');
    return http.Response('{"id": 1, "name": "Alice"}', 200,
        headers: {'content-type': 'application/json'});
  });

  final repo = UserRepository(client: mockClient);
  final user = await repo.fetchUser(1);

  expect(user.name, 'Alice');
});
```

**ধাপ ৩ — Mocktail দিয়ে Dio mock করা।**
`Dio` instance mock করুন আর `get`/`post` stub করুন। Dio-র response-এ একটা `requestOptions` লাগে। আর `RequestOptions`-এ `any()` ব্যবহার করতে হলে একটা fallback দরকার।

```dart
import 'package:dio/dio.dart';
import 'package:mocktail/mocktail.dart';

class MockDio extends Mock implements Dio {}

void main() {
  late MockDio mockDio;
  late UserRepository repo;

  setUpAll(() => registerFallbackValue(RequestOptions(path: '')));
  setUp(() {
    mockDio = MockDio();
    repo = UserRepository(dio: mockDio);
  });

  test('fetchUser returns a user on 200', () async {
    when(() => mockDio.get('/users/1')).thenAnswer((_) async => Response(
          data: {'id': 1, 'name': 'Alice'},
          statusCode: 200,
          requestOptions: RequestOptions(path: '/users/1'),
        ));

    final user = await repo.fetchUser(1);
    expect(user.name, 'Alice');
  });

  test('fetchUser throws on 404', () async {
    when(() => mockDio.get('/users/999')).thenThrow(DioException(
      type: DioExceptionType.badResponse,
      requestOptions: RequestOptions(path: '/users/999'),
      response: Response(statusCode: 404, requestOptions: RequestOptions(path: '/users/999')),
    ));

    expect(() => repo.fetchUser(999), throwsA(isA<UserNotFoundException>()));
  });
}
```

**ধাপ ৪ — Clean architecture-এর কৌশল: client-কে interface-এর পেছনে লুকান।**
নিজের একটা abstract `ApiClient` বানান। Repository সেটার উপর নির্ভর করবে, সরাসরি Dio/http-এর উপর নয়। এখন mock এক line-এই হয়ে যায়। আর repository-তে হাত না দিয়েই Dio-র বদলে http বসাতে পারবেন।

```dart
abstract class ApiClient {
  Future<Map<String, dynamic>> get(String path);
}

class DioApiClient implements ApiClient { /* wraps Dio */ }
class MockApiClient extends Mock implements ApiClient {}  // mock করা খুব সহজ
```

**Interviewer কেন জিজ্ঞেস করে:** HTTP mocking data layer-এর প্রতিদিনের দক্ষতা। তাঁরা দেখতে চান আপনি অনিশ্চিত network call ছাড়াই test করতে পারেন কি না। আর dependency injection-ই যে এটা সম্ভব করে, সেটা আপনি বোঝেন কি না।

**সাধারণ ভুল:** Repository-র ভেতরে `Dio()` বা `http.Client()` hardcode করা, যেখানে mock inject করার কোনো উপায় নেই। Client ভেতরে `new` করলে repository-কে আলাদাভাবে test করা যায় না। সবসময় constructor দিয়ে inject করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"সরাসরি Dio mock না করে interface কেন?"* → এটা আপনার code-কে HTTP library থেকে আলাদা রাখে, mock সহজ করে, আর test না বদলেই client বদলাতে দেয়।
- *"Timeout বা retry কীভাবে test করবেন?"* → Client-কে stub করে একটা timeout throw করান, তারপর repository-র retry/fallback আচরণ assert করুন (সময় নিয়ন্ত্রণের জন্য [Q8](#q8)-এর সাথে মিলিয়ে নিন)।

**সম্পর্কিত:** [Q9 — Mockito](#q9) · [Q11 — fake বনাম mock](#q11) · [Q8 — async/time](#q8)

[↑ উপরে ফিরুন](#toc)

---

# G. Visual ও end-to-end testing

---

## <a id="q15"></a>15. Golden test কী — কীভাবে এগুলো তৈরি আর update করবেন, আর কখন ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা golden test render হওয়া widget-এর snapshot image নেয়। তারপর সেটা একটা saved reference image-এর সাথে pixel-by-pixel মিলিয়ে দেখে। Pixel আলাদা হলে test fail করে — তাই এটা অনাকাঙ্ক্ষিত visual পরিবর্তন ধরে ফেলে। আমি `--update-goldens` দিয়ে reference তৈরি বা update করি, আর সাধারণ run সেটার সাথে তুলনা করে। আমি এগুলো custom-painted আর design-system widget-এর জন্য ব্যবহার করি, সব কিছুর জন্য নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Golden test জিনিসটা কী।**
"Golden" (বা snapshot) মানে একটা saved সঠিক image। Test আপনার widget render করে, ছবি তোলে, আর সেই saved image-এর সাথে মিলিয়ে দেখে। আলাদা হলে বুঝতে হবে দেখতে কিছু একটা বদলেছে — হয়তো ইচ্ছা করে, হয়তো ভুলে।

এটাকে "spot the difference" ধাঁধার মতো ভাবুন: আপনি আসল ছবিটা রেখে দেন, আর test বদলে যাওয়া প্রতিটা pixel ধরিয়ে দেয়।

**ধাপ ২ — পুরো lifecycle।**

```
First time:   flutter test --update-goldens
                  |
              renders the widget -> saves a PNG as the reference
                  |
CI / later:   flutter test
                  |
              renders the widget -> compares pixel-by-pixel to the PNG
                  |
              match? -- yes -> pass
                  |
                  no -> FAIL (visual regression detected)
```

**ধাপ ৩ — একটা লিখে দেখা।**
Widget render করুন, তারপর `expectLater(finder, matchesGoldenFile('...'))` লিখুন।

```dart
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('ProfileCard golden', (tester) async {
    await tester.pumpWidget(
      const MaterialApp(
        home: Scaffold(
          body: ProfileCard(name: 'Alice', role: 'Engineer'),
        ),
      ),
    );

    await expectLater(
      find.byType(ProfileCard),
      matchesGoldenFile('goldens/profile_card.png'),
    );
  });
}
```

**ধাপ ৪ — Golden file তৈরি আর update করা।**

```bash
# golden PNG তৈরি বা update করুন:
flutter test --update-goldens

# সাধারণ run — saved golden-এর সাথে তুলনা করে:
flutter test
```

আপনি যখন *ইচ্ছা করে* কোনো widget-এর চেহারা বদলান, তখন `--update-goldens` দিয়ে আবার run করুন। তারপর নতুন image commit করুন।

**ধাপ ৫ — কখন ব্যবহার করবেন (আর কখন করবেন না)।**
- **যেখানে ভালো:** custom-painted widget (`CustomPainter`), জটিল layout যেখানে spacing গুরুত্বপূর্ণ, design-system component যেগুলো pixel-perfect থাকতেই হবে, chart আর data visualization।
- **যেখানে এড়িয়ে যান:** standard Material widget (Flutter নিজেই সেগুলো test করে), development-এর সময় ঘন ঘন বদলায় এমন screen, আর যেসব widget-এর text বদলায় (localization বা dynamic data) — সেগুলো সারাক্ষণ fail করবে।

**ধাপ ৬ — Platform-এর ফাঁদ।**
Golden image platform-এর উপর নির্ভর করে। কারণ macOS, Linux আর Windows-এ font একটু আলাদাভাবে render হয়। আপনি যদি নিজের Mac-এ golden তৈরি করেন আর CI Linux-এ চলে, তাহলে প্রতিটা golden fail করতে পারে। **একই** platform-এ তৈরি করুন আর তুলনা করুন — সাধারণত CI environment-এ।

**Interviewer কেন জিজ্ঞেস করে:** Golden test দেখায় আপনি visual regression testing বোঝেন। Design-ভারী app-এর জন্য এটা গুরুত্বপূর্ণ। তাঁরা দেখতে চান আপনি জানেন কখন golden মূল্য যোগ করে আর কখন এটা maintenance-এর বোঝা হয়ে যায়।

**সাধারণ ভুল:** Mac-এ golden তৈরি করা, অথচ CI চলে Linux-এ — font-এর পার্থক্যে প্রতিটা golden fail করে। সবসময় একই platform-এ তৈরি করুন আর তুলনা করুন (সাধারণত CI)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Golden platform ভেদে আলাদা হয় কেন?"* → OS ভেদে font rendering আর anti-aliasing আলাদা, তাই exact pixel বদলে যায়।
- *"এগুলো stable রাখবেন কীভাবে?"* → CI-তে তৈরি করুন, একটা fixed test font load করুন, আর dynamic text-এর golden test করা এড়ান।

**সম্পর্কিত:** [Q6 — widget testing](#q6) · [Q2 — golden কোথায় বসে](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. Flutter-এ integration testing কীভাবে কাজ করে — `integration_test` package আর আসল device-এ চালানো?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`integration_test` package পুরো app-এর test আসল device বা emulator-এ চালায়। Widget test-এর মতো নয় — এটা সম্পূর্ণ rendering pipeline, navigation আর platform channel চালায়। আপনি `IntegrationTestWidgetsFlutterBinding` initialize করেন, app চালু করেন, তারপর সেই একই `tester` API দিয়ে চালান। এটা পুরোনো `flutter_driver` পদ্ধতির জায়গা নিয়েছে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Widget test থেকে এটা আলাদা কীসে।**
Widget test একটা headless engine-এ একটা widget render করে। Integration test *পুরো app* একটা device-এ চালু করে। ফলে সব কিছু একসাথে জোড়া অবস্থায় test হয়: আসল navigation, আসল platform code, পুরো UI। আসল user-এর app ব্যবহারের সবচেয়ে কাছাকাছি জিনিস এটাই।

**ধাপ ২ — Setup।**
1. `integration_test` আর `flutter_test` dev dependency হিসেবে যোগ করুন।
2. Project root-এ একটা `integration_test/` folder বানান।
3. `main`-এর শুরুতে `IntegrationTestWidgetsFlutterBinding.ensureInitialized()` call করুন।

```
my_app/
├── lib/
│   └── main.dart
├── test/                  <- unit and widget tests
│   └── widget_test.dart
├── integration_test/      <- integration tests
│   └── app_test.dart
└── pubspec.yaml
```

**ধাপ ৩ — একটা flow test লেখা।**
`app.main()` দিয়ে আসল app চালু করুন, তারপর সেটা চালান। আসল frame আর navigation animation শেষ হতে দিতে `pumpAndSettle` ব্যবহার করুন।

```dart
// integration_test/app_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:my_app/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  group('end-to-end', () {
    testWidgets('user can log in and see the home screen', (tester) async {
      app.main();
      await tester.pumpAndSettle();

      await tester.enterText(find.byKey(const Key('email_field')), 'user@test.com');
      await tester.enterText(find.byKey(const Key('password_field')), 'password123');
      await tester.pumpAndSettle();

      await tester.tap(find.byKey(const Key('login_button')));
      await tester.pumpAndSettle();

      expect(find.text('Welcome back!'), findsOneWidget);
    });
  });
}
```

**ধাপ ৪ — এটা চালানো।**

```bash
# যুক্ত থাকা device বা emulator-এ:
flutter test integration_test/app_test.dart

# নির্দিষ্ট একটা device-এ:
flutter test integration_test/app_test.dart -d <device_id>

# Chrome-এ (web):
flutter test integration_test/app_test.dart -d chrome
```

**ধাপ ৫ — `integration_test` বনাম পুরোনো `flutter_driver`।**
`flutter_driver` (legacy) একটা *আলাদা* process-এ চলে আর একটা protocol দিয়ে app-এর সাথে কথা বলে — ধীর আর বেশি সীমিত। `integration_test` app-এর *একই* process-এ চলে। তাই এটা দ্রুত, আর স্বাভাবিক `tester` API দিয়ে widget tree-তে সরাসরি হাত দেওয়া যায়। নতুন project-এ `integration_test` ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** Ship করার আগে integration test হলো শেষ নিরাপত্তা জাল। তাঁরা জানতে চান আপনি আলাদা আলাদা unit-এর বাইরেও test করেছেন কি না। বিশেষ করে login আর checkout-এর মতো গুরুত্বপূর্ণ flow-এর জন্য।

**সাধারণ ভুল:** `flutter_driver` আর `integration_test` গুলিয়ে ফেলা, অথবা নতুন project-এ `flutter_driver` ধরা। `integration_test` ব্যবহার করুন — একই process, দ্রুত, tree-তে সরাসরি access।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা widget test থেকে আলাদা কীভাবে?"* → Widget test headless আর আলাদা করা; integration test পুরো app আসল device-এ platform channel সহ চালায়।
- *"এগুলো CI-তে কীভাবে চালান?"* → আসল device farm-এ (যেমন Firebase Test Lab) অথবা CI job-এ চালু করা একটা emulator-এ।

**সম্পর্কিত:** [Q1 — তিন ধরনের test](#q1) · [Q6 — `pumpAndSettle`](#q6)

[↑ উপরে ফিরুন](#toc)

---

# H. Coverage ও test সুস্থ রাখা

---

## <a id="q17"></a>17. Flutter-এ code coverage কীভাবে তৈরি আর মাপবেন — আর এটা আসলে কী বলে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flutter-এ coverage built-in আছে: `flutter test --coverage` চালালে `coverage/lcov.info` তৈরি হয়। আমি `genhtml` দিয়ে সেটাকে একটা HTML report বানাই। কিন্তু coverage শুধু মাপে কোন line গুলো চলেছে, test ভালো কি না তা নয়। তাই আমি এটাকে কোনটা untested তার একটা ইঙ্গিত হিসেবে দেখি, quality score হিসেবে নয়। আর আমি কখনোই 100%-এর পেছনে ছুটি না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Coverage data তৈরি করুন।**

```bash
flutter test --coverage
# তৈরি হয়: coverage/lcov.info
```

**ধাপ ২ — HTML report হিসেবে দেখুন।**

```bash
# আগে lcov install করুন (macOS: brew install lcov, Linux: apt-get install lcov)
genhtml coverage/lcov.info -o coverage/html
open coverage/html/index.html
```

**ধাপ ৩ — Generated file বাদ দিন।**
Generated file (`*.g.dart`, `*.freezed.dart`) গোনা উচিত নয় — ওগুলো আপনি লেখেননি।

```bash
lcov --remove coverage/lcov.info \
  '**/*.g.dart' \
  '**/*.freezed.dart' \
  '**/generated/**' \
  -o coverage/lcov_filtered.info
```

**ধাপ ৪ — Coverage আসলে কী মাপে (মূল কথা)।**
Line coverage বলে **কোন line গুলো চলেছে** test-এর সময়। এটা **বলে না** যে test গুলো *ভালো*। আপনি প্রতিটা line চালিয়েও অর্থপূর্ণ কিছুই assert না করতে পারেন।

তুলনা: coverage হলো একটা বাড়ির প্রতিটা ঘরে একবার আলো জ্বলেছে কি না তা দেখার মতো — এতে প্রমাণ হয় না কেউ সত্যিই প্রতিটা ঘর পরীক্ষা করেছে। ধারালো assertion সহ 80% coverage খালি assertion সহ 100% coverage-এর চেয়ে ভালো।

```dart
// 100% line coverage, কিন্তু test-টা অকেজো:
test('runs the code', () {
  service.process();   // কোনো expect() নেই — কিছুই প্রমাণ করে না
});
```

**ধাপ ৫ — বাস্তব target (নির্দেশনা)।**
- business logic / domain layer-এর জন্য 80%+
- repository / data layer-এর জন্য 70%+
- UI-এর জন্য 50%+ (widget test-এর খরচ বেশি)
- 100%-এর পেছনে ছুটবেন না — লাভ দ্রুত কমে যায়

**ধাপ ৬ — CI-তে যুক্ত করা (ধারণা)।**
একটা সাধারণ pipeline coverage সহ test চালায়, generated file বাদ দেয়, একটা minimum threshold চাপিয়ে দেয়, আর Codecov বা Coveralls-এর মতো service-এ upload করে। ফলে প্রতিটা PR-এ trend দেখা যায়।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখেন আপনি coverage-কে একটা *metric* হিসেবে নেন কি না, *লক্ষ্য* হিসেবে নয়। আর আপনি tooling সাজাতে পারেন কি না এবং বুদ্ধি খাটিয়ে ফলটা পড়তে পারেন কি না।

**সাধারণ ভুল:** Coverage-এর শতাংশকে quality score ভাবা। 95% coverage মানে test গুলো ভালো নয়; অর্থপূর্ণ assertion ছাড়াও আপনি প্রতিটা line ছুঁতে পারেন। Coverage দেখায় কোনটা test করা *হয়নি*, এটা দেখায় না যে যা test করা *হয়েছে* তা ভালোভাবে হয়েছে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"100% coverage কি করার মতো?"* → খুব কমই। শেষ কয়েক শতাংশে খরচ অনেক বেশি হয় আর তুচ্ছ code বাঁচে; সেই পরিশ্রম edge case-এ দিলে ভালো।
- *"Coverage কী কী ধরতে পারে না?"* → দুর্বল assertion, বাদ পড়া edge case, আর ভুল behavior যেটা তবুও line-টা চালায়।

**সম্পর্কিত:** [Q2 — test pyramid](#q2) · [Q18 — maintainable test](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. Codebase বড় হওয়ার সাথে সাথে test-গুলো maintainable রাখেন কীভাবে?

> Deeper · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-06-testing.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Maintainable test আসলে একটা architecture-এর সমস্যা। আমি logic-কে নিচে নামিয়ে দ্রুত unit test-এ নিয়ে যাই। Setup-কে helper function-এ বের করে আনি, যাতে widget tree বারবার লিখতে না হয়। প্রতি test-এ একটাই behavior check করি। শুধু সরাসরি dependency-কে mock করি। আর test code-কে production code-এর মতো যত্ন করি। এছাড়া আমি test করি *কী* ঘটে, *কীভাবে* ভেতরে ঘটে তা নয় — তাই একটা refactor-এ সব ভেঙে পড়ে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Pyramid ঠিকমতো মেনে চলুন।**
বেশিরভাগ logic unit test দিয়ে cover করুন। একটা unit test যদি জিনিসটা verify করতে পারে, তাহলে সেই একই check ধীর widget বা integration test-এ আবার করবেন না ([Q2](#q2) দেখুন)।

**ধাপ ২ — Setup-কে helper-এ বের করে আনুন।**
অনেক test যখন একই widget tree বানায়, তখন সেটাকে একটা helper-এ নিয়ে যান। এতে duplication শেষ হয়। আর test-এর উদ্দেশ্যও স্পষ্ট হয়।

```dart
// খারাপ — এই বিশাল tree ২০টা test-এ copy করা হয়েছে
await tester.pumpWidget(
  MaterialApp(
    home: MultiBlocProvider(
      providers: [
        BlocProvider.value(value: mockUserCubit),
        BlocProvider.value(value: mockAuthCubit),
      ],
      child: const MyScreen(),
    ),
  ),
);

// ভালো — একটাই helper, সব জায়গায় ব্যবহার
Future<void> pumpMyScreen(
  WidgetTester tester, {
  UserState? userState,
  AuthState? authState,
}) async {
  when(() => mockUserCubit.state).thenReturn(userState ?? UserLoading());
  when(() => mockAuthCubit.state).thenReturn(authState ?? Authenticated());

  await tester.pumpWidget(
    MaterialApp(
      home: MultiBlocProvider(
        providers: [
          BlocProvider<UserCubit>.value(value: mockUserCubit),
          BlocProvider<AuthCubit>.value(value: mockAuthCubit),
        ],
        child: const MyScreen(),
      ),
    ),
  );
}
```

**ধাপ ৩ — `Key` বুদ্ধি করে ব্যবহার করুন।**
একই type-এর অনেকগুলো widget থাকলে `Key` দিয়ে খুঁজুন। তাহলে ছোট layout পরিবর্তনে test ভাঙবে না। কিন্তু সব কিছুতে key বসাবেন না — ওটা শুধু noise ([Q7](#q7) দেখুন)।

**ধাপ ৪ — প্রতি test-এ একটাই behavior।**
`'everything works'` নামের একটা test যদি ১৫টা জিনিস check করে, সেটা maintainable নয় — fail করলে কী ভেঙেছে বোঝা যায় না। Test-এর নাম behavior হিসেবে দিন: `'emits error state when the repository throws'`, `'test 3'` নয়।

**ধাপ ৫ — বেশি mock করবেন না; শুধু সরাসরি boundary-তে mock করুন।**
`ServiceA` যদি `RepoB` ব্যবহার করে, আর `RepoB` ব্যবহার করে `ApiClientC`, তাহলে `ServiceA`-র test-এ `RepoB` mock করা উচিত — নিচে নেমে `ApiClientC` নয়। অনেক layer গভীরে mock করলে test ভঙ্গুর হয়ে যায়।

**ধাপ ৬ — Test code-কে production code-এর মতো ভাবুন।**
পরিষ্কার naming, DRY আর refactoring প্রয়োগ করুন। `group()` দিয়ে গুছিয়ে রাখুন। State class-গুলোকে equatable বানান, যাতে তুলনা কাজ করে ([Q12](#q12) দেখুন)।

**ধাপ ৭ — প্রতিটা PR-এ CI-তে test চালান, আর flaky test কখনোই সহ্য করবেন না।**
যে test নিয়মিত চলে না, সেটা পচে যায়। একটা flaky test সাথে সাথেই ঠিক করতে হবে বা মুছে ফেলতে হবে — কখনো এড়িয়ে যাবেন না, নাহলে পুরো suite-এর উপর বিশ্বাস চলে যায়।

```
Maintainability checklist:

  [x] each test verifies ONE behavior
  [x] helpers reduce duplication without hiding intent
  [x] mocks only at the immediate dependency boundary
  [x] state classes implement Equatable
  [x] no magic numbers — use named constants or factories
  [x] tests run in under ~2 minutes on CI
  [x] flaky tests are fixed, not skipped
  [x] golden tests generated on CI, not local machines
```

**Interviewer কেন জিজ্ঞেস করে:** প্রথমে সব team-ই test লেখে। শক্তিশালী team আর হিমশিম খাওয়া team-এর পার্থক্য হলো, সেই test-গুলো বড় হওয়ার পরেও maintainable *থাকে* কি না। এই প্রশ্ন যাচাই করে আপনি test-suite পচে যাওয়ার অভিজ্ঞতা পেয়েছেন কি না, আর তা থেকে শিখেছেন কি না।

**সাধারণ ভুল:** Behavior-এর বদলে implementation-এর প্রতিচ্ছবি এমন test লেখা। আপনি যদি assert করেন "method A আগে B তারপর C call করে", তাহলে যেকোনো refactor-এ test ভেঙে যাবে — যদিও বাইরে থেকে behavior একই থাকে। Test করুন *কী* ঘটে, *কীভাবে* নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flaky test কীভাবে সামলান?"* → আসল কারণ খুঁজুন (সাধারণত timing বা shared state), সেটা ঠিক করুন, নয়তো test-টা সরিয়ে দিন। কখনো `skip` করে ভুলে যাবেন না — এতে suite-এর উপর বিশ্বাস নষ্ট হয়।
- *"Implementation-এর প্রতিচ্ছবি বানানো খারাপ কেন?"* → এতে test ভেতরের structure-এর সাথে আটকে যায়। ফলে নিরাপদ refactor-এও test fail করে, আর cleanup করার উৎসাহ কমে যায়।

**সম্পর্কিত:** [Q2 — test pyramid](#q2) · [Q7 — keys](#q7) · [Q11 — over-mocking](#q11)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের review)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার table-গুলো, তারপর এক লাইনের মনে-করিয়ে-দেওয়া পয়েন্টগুলো।

## দ্রুত তুলনার table

**Unit vs Widget vs Integration**

| | Unit | Widget | Integration |
|---|---|---|---|
| পরিধি | একটা function/class | একটা widget/subtree | পুরো app |
| কোথায় চলে | Dart VM | test engine (headless) | আসল device/emulator |
| গতি | সবচেয়ে দ্রুত | মাঝারি | সবচেয়ে ধীর |
| কীসের জন্য | logic, repo | UI behavior | গুরুত্বপূর্ণ flow |

**`pump` vs `pumpAndSettle`**

| `pump()` | `pumpAndSettle()` |
|---|---|
| এক frame (বা একটা duration) এগিয়ে দেয় | animation না থামা পর্যন্ত pump করতে থাকে |
| frame সংখ্যা জানা থাকলে ব্যবহার করুন | transition/animation শেষ করতে ব্যবহার করুন |
| অন্তহীন animation-এ নিরাপদ | অন্তহীন animation-এ timeout হয় |

**Mockito vs Mocktail**

| | Mockito | Mocktail |
|---|---|---|
| Code generation | হ্যাঁ (build_runner) | লাগে না |
| Mock বানানো | generate করা `MockX` | `class MockX extends Mock implements X {}` |
| Stub syntax | `when(mock.m())` | `when(() => mock.m())` |
| `any()` + custom type | কাজ করে | `registerFallbackValue` লাগে |

**Mock vs Fake**

| Mock | Fake |
|---|---|
| call রেকর্ড করে; `when` + `verify` | সত্যিকারের কাজ করা code, সহজ করা |
| check করে *কীভাবে* call হয়েছে | শুধু *আচরণ* করে (in-memory) |
| side effect আর failure-এর জন্য ভালো | অনেক call জুড়ে stateful data-র জন্য ভালো |

**`thenReturn` vs `thenAnswer`**

| `thenReturn(x)` | `thenAnswer((_) async => x)` |
|---|---|
| sync value-র জন্য | async (`Future`) method-এর জন্য |
| প্রতি call-এ একই instance | প্রতি call-এ নতুন result |

## এক লাইনের মনে-করিয়ে-দেওয়া পয়েন্ট

- **তিন ধরনের test**: unit (logic, সবচেয়ে দ্রুত), widget (headless engine-এ UI), integration (device-এ পুরো app)। ([Q1](#q1))
- **Test pyramid**: অনেক unit, কিছু widget, খুব কম integration। Test-কে *নিচে* নামান। ([Q2](#q2))
- **TDD** = red, green, refactor। Logic আর bug fix-এর জন্য আগে test লিখুন। ([Q3](#q3))
- **`setUp`** *প্রতিটা* test-এর আগে চলে (নতুন state); **`setUpAll`** প্রতি group-এ *একবার* চলে। ([Q4](#q4))
- **`throwsA`**-র একটা *function* লাগে: `expect(() => f(), throwsA(...))`। Future-এর জন্য `expectLater` ব্যবহার করুন। ([Q5](#q5))
- **Widget test সময় থামিয়ে রাখে** — tap বা `setState`-এর পরে `pump()` call করুন, নাহলে UI update হবে না। ([Q6](#q6))
- **একটা finder-এ অনেক widget মিললে একটা `Key` দিন** আর `find.byKey` ব্যবহার করুন। ([Q7](#q7))
- **Timer-এর জন্য সত্যিকারে অপেক্ষা করবেন না** — `fakeAsync` + `async.elapse`, নয়তো `tester.pump(duration)` ব্যবহার করুন। ([Q8](#q8))
- **Mockito** = generate, stub (`when`), act, verify। async-এর জন্য `thenAnswer` ব্যবহার করুন। ([Q9](#q9))
- **Mocktail** = code gen নেই, closure syntax `when(() => ...)`, `any()`-র জন্য `registerFallbackValue`। ([Q10](#q10))
- **Mock** = verify করে *কীভাবে* call হয়েছে; **Fake** = সত্যিকারের একটা সহজ implementation। ([Q11](#q11))
- **`blocTest`**: build → seed → act → expect → verify। Initial state `expect`-এ থাকে না; state-গুলো equatable হতে হবে। ([Q12](#q12))
- **একটা screen test করুন** `MockCubit` দিয়ে Cubit-টা mock করে, আর `BlocProvider.value` দিয়ে inject করে। ([Q13](#q13))
- **HTTP mock করুন boundary-তে**: `http`-র জন্য `MockClient`, `Dio` mock করুন Mocktail দিয়ে; client সবসময় inject করুন। ([Q14](#q14))
- **Golden test** pixel তুলনা করে; save করতে `--update-goldens`। Font না মেলার সমস্যা এড়াতে CI-তে generate করুন। ([Q15](#q15))
- **`integration_test`** পুরো app in-process চালায় — পুরোনো `flutter_driver`-এর চেয়ে দ্রুত। ([Q16](#q16))
- **Coverage** দেখায় কোনটা test করা *হয়নি*, test-গুলো ভালো কি না তা নয়। 100%-এর পিছনে ছুটবেন না। ([Q17](#q17))
- **Maintainable test**: প্রতিটায় একটা behavior, setup-এর জন্য helper, শুধু সবচেয়ে কাছের boundary-তে mock, implementation নয় behavior test করুন। ([Q18](#q18))

[↑ উপরে ফিরুন](#toc)

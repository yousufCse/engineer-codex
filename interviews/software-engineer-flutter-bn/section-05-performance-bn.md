# Section 5 — Performance Optimization

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **Bangladesh (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যা সহ**, আর **link করা** — যাতে আপনি ঘুরে ঘুরে পড়তে পারেন এবং ধীরে ধীরে প্রস্তুতি নিতে পারেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-05-performance-bn.md](../software-engineer-flutter/section-05-performance.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code সহ বিস্তারিত, ধাপে ধাপে ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে ট্যাগ দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তরটা** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন "আরও গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলা নিজেই একটা senior skill — আর এটা remote আর BD দুই ধরনের কোম্পানিতেই একইভাবে কাজ করে। Performance-এর জন্য আরও একটা নিয়ম: কোনো কিছু "faster" বলবেন না যদি না বলেন *আপনি কীভাবে মেপেছেন*। "আমি DevTools-এ profile করেছি" বলাটা শক্ত senior signal।

---


## <a id="toc"></a>সূচিপত্র

**A. ধীরগতি খুঁজে বের করা আর মাপা**
1. [Jank কী, আর আপনি এটা কীভাবে খুঁজে পান?](#q1) · *Very common*
2. [Flutter DevTools — Performance, Rebuild, Memory tab](#q2) · *Very common*
3. [Debug mode-এ কখনোই performance মাপবেন না কেন?](#q3) · *Common*

**B. Rebuild কমানো**
4. [`const` widget কীভাবে rebuild এড়িয়ে যায়](#q4) · *Very common*
5. [আলাদা করা widget বনাম helper method](#q5) · *Very common*
6. [`build()`-এর golden rule (pure, দ্রুত, কোনো side effect নয়)](#q6) · *Very common*
7. [Tree-এর উপরের দিকে `setState` call করবেন না কেন?](#q7) · *Very common*
8. [`Selector` বনাম `Consumer` (Provider)](#q8) · *Common*
9. [`BlocBuilder`-এ `buildWhen`](#q9) · *Common*
10. [ব্যয়বহুল কাজে debounce আর throttle](#q10) · *Common*

**C. লম্বা list আর scrolling**
11. [`ListView` বনাম `.builder` বনাম `.separated` বনাম `.custom`](#q11) · *Very common*
12. [Lazy loading আর pagination (infinite scroll)](#q12) · *Common*
13. [List-এ key আর `AutomaticKeepAliveClientMixin`](#q13) · *Common*

**D. Painting, image আর GPU**
14. [`RepaintBoundary` — কখন উপকার করে আর কখন ক্ষতি করে](#q14) · *Common*
15. [Image optimize করা (cache, resize, WebP, precache)](#q15) · *Very common*
16. [Shader compilation jank (প্রথমবার চালানোর সময় আটকে যাওয়া)](#q16) · *Deeper*

**E. ভারী কাজ আর startup**
17. [Isolate আর `compute()` — ভারী কাজ UI থেকে সরানো](#q17) · *Very common*
18. [Memory leak আর `dispose()`](#q18) · *Very common*
19. [App startup time মাপা আর কমানো](#q19) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিউ)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

১৯টা প্রশ্ন একসাথে পড়ার দরকার নেই। এই পর্যায়গুলো ক্রম অনুযায়ী অনুসরণ করুন — প্রতিটা আগেরটার উপর দাঁড়ায়। একটা পর্যায় তখনই শেষ ধরুন, যখন না দেখে **সংক্ষিপ্ত উত্তর** দিতে পারবেন।

**পর্যায় ১ — মানসিকতা: আগে মাপুন (এখান থেকে শুরু করুন)।** এটা ছাড়া বাকি সব উত্তর অনুমানের মতো শোনায়।
→ [Q1 Jank কী](#q1) · [Q2 DevTools](#q2) · [Q3 Debug বনাম profile/release](#q3)

**পর্যায় ২ — এত বেশি rebuild বন্ধ করুন।** Flutter-এর বাস্তব performance bug-এর 80% এখানেই থাকে।
→ [Q4 const widget](#q4) · [Q5 Widget বনাম method](#q5) · [Q6 build()-এর golden rule](#q6) · [Q7 setState-এর scope](#q7)

**পর্যায় ৩ — লম্বা list (প্রায় প্রতিটা app-এ একটা থাকে)।**
→ [Q11 ListView-এর ধরন](#q11) · [Q12 Pagination](#q12) · [Q13 Key আর keep-alive](#q13)

**পর্যায় ৪ — State management আর painting।** শুধু সঠিক widget-টাই কীভাবে rebuild করবেন, আর painting কীভাবে কাজ করে।
→ [Q8 Selector বনাম Consumer](#q8) · [Q9 buildWhen](#q9) · [Q10 Debounce/throttle](#q10) · [Q14 RepaintBoundary](#q14) · [Q15 Image](#q15)

**পর্যায় ৫ — গভীর senior signal (সবার শেষে করুন)।** এগুলোই শক্ত senior-দের বাকিদের থেকে আলাদা করে।
→ [Q16 Shader jank](#q16) · [Q17 Isolate](#q17) · [Q18 Memory leak](#q18) · [Q19 Startup time](#q19)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই আটটা রিভিউ করুন:
[Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q5](#q5) · [Q7](#q7) · [Q11](#q11) · [Q17](#q17) · [Q18](#q18), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. ধীরগতি খুঁজে বের করা আর মাপা

---

## <a id="q1"></a>1. Flutter-এ jank কেন হয়, আর আপনি এটা কীভাবে খুঁজে পান?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Jank হলো screen আটকে আটকে যাওয়া, কারণ একটা frame আঁকতে বেশি সময় লেগেছে। 60fps-এ মসৃণ থাকতে হলে প্রতিটা frame প্রায় 16ms-এর মধ্যে শেষ হতে হবে। Jank দুই জায়গা থেকে আসে: UI thread-এ অনেক বেশি কাজ (ভারী build, বড় computation), অথবা raster thread-এ অনেক বেশি কাজ (জটিল painting, বড় image)। আমি এটা খুঁজি profile mode-এ চালিয়ে, আর Flutter DevTools দিয়ে ধীর frame-গুলো বের করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Frame পড়ে যাওয়ার তুলনা।**
App-কে একটা video হিসেবে ভাবুন, যেটা প্রতি সেকেন্ডে 60 frame-এ চলছে। প্রতিটা frame-এর সময়ের বাজেট খুব ছোট, প্রায় 16ms (কারণ 1 সেকেন্ড ÷ 60 ≈ 16ms)। একটা frame-এ 16ms-এর বেশি লাগলে phone পুরোনো frame-টাই আবার দেখায় — আপনি একটা ঝাঁকুনি দেখেন। ওই দেখা যাওয়া ঝাঁকুনিটাই **jank**। 120Hz phone-এ বাজেট আরও কম, প্রায় 8ms।

**ধাপ ২ — Flutter প্রতিটা frame আঁকে একটা assembly line-এ।**
একটা frame কয়েকটা পর্যায়ে তৈরি হয়, ঠিক assembly line-এর মতো:

```
Build   →   Layout   →   Paint   →   Composite (raster)
(make    (decide     (record     (turn layers into
 widgets) sizes)      drawing)     real pixels on GPU)
```

প্রথম তিনটা (build, layout, paint) চলে **UI thread**-এ। শেষেরটা (composite/raster) চলে **raster thread**-এ। Jank যেকোনো thread থেকেই শুরু হতে পারে।

**ধাপ ৩ — UI thread কীসে ধীর হয়।**
এই thread আপনার Dart code চালায়। এটা ধীর হয় যখন:
- `build()` method অনেক বেশি কাজ করে, বা অনেক বেশি widget rebuild হয়।
- আপনি main isolate-এ ভারী synchronous কাজ করেন (বড় JSON parse করা, লম্বা loop)।
- আপনি tree-এর উপরের দিকে `setState` call করেন, ফলে বিশাল একটা subtree rebuild হয় ([Q7](#q7) দেখুন)।

**ধাপ ৪ — Raster thread কীসে ধীর হয়।**
এই thread আঁকা জিনিসটাকে GPU-তে pixel-এ পরিণত করে। এটা ধীর হয় যখন:
- আপনি অনেক `Opacity`, `ClipRRect`, বা shadow ব্যবহার করেন, যেগুলো `saveLayer` চালাতে বাধ্য করে (একটা ব্যয়বহুল "offscreen buffer-এ আঁকা" ধাপ)।
- আপনি বিশাল image দেখান, যেগুলো resize করা হয়নি ([Q15](#q15) দেখুন)।
- আপনার অনেকগুলো overlapping layer আছে, যেগুলো GPU-কে জোড়া লাগাতে হয়।

**ধাপ ৫ — আসলে কীভাবে খুঁজবেন (যে ধাপগুলো মুখে বলবেন)।**

1. **Profile mode-এ চালান।** Debug mode ইচ্ছে করেই ধীর, তাই এর সংখ্যাগুলো মিথ্যা বলে ([Q3](#q3) দেখুন)।
   ```bash
   flutter run --profile
   ```
2. দ্রুত একবার দেখার জন্য **Performance Overlay চালু করুন**। এটা দুটো graph উপর-নিচে দেখায়: UI thread (উপরে) আর raster thread (নিচে)। লাল bar মানে frame মিস হয়েছে।
   ```dart
   MaterialApp(
     showPerformanceOverlay: true, // release-এর আগে সরিয়ে ফেলুন!
     home: const HomePage(),
   );
   ```
3. **Flutter DevTools → Performance tab খুলুন।** Record করুন, ঝাঁকুনিটা আবার ঘটান, থামান, তারপর একটা লাল frame-এ click করে flame chart পড়ুন ([Q2](#q2) দেখুন)।
4. সন্দেহজনক code-এ **নিজের timing marker যোগ করুন**, যাতে timeline-এ দেখতে পান:
   ```dart
   import 'dart:developer';

   void processData(List<Map<String, dynamic>> raw) {
     Timeline.startSync('processData'); // DevTools-এ দেখা যাবে
     // ... ভারী কাজ ...
     Timeline.finishSync();
   }
   ```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি rendering pipeline বোঝেন কি না (build → layout → paint → composite)। আর jank-কে অনুমান করে এলোমেলো optimization যোগ না করে tool দিয়ে *নির্ণয়* করেন কি না।

**সাধারণ ভুল:** Debug mode-এ test করে jank আছে বলে রিপোর্ট করা। Debug mode ধীর JIT compilation আর বাড়তি check ব্যবহার করে, তাই এটা 5–10x ধীর। সবসময় আসল device-এ `--profile` mode-এ profile করুন, emulator-এ নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"UI thread বনাম raster thread — কোনটা সমস্যা তা আপনি কীভাবে বুঝবেন?"* → Overlay-এর দুটো graph দেখুন। উপরের (UI) bar লাল হলে আপনার Dart/build code ধীর। নিচের (raster) bar লাল হলে আপনার painting/image ধীর।
- *"ভালো frame budget কত?"* → 60fps-এর জন্য প্রায় 16ms, 120fps-এর জন্য প্রায় 8ms।

**সম্পর্কিত:** [Q2 — DevTools](#q2) · [Q3 — debug বনাম profile](#q3) · [Q14 — RepaintBoundary](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Flutter DevTools কীভাবে ব্যবহার করেন — Performance, Rebuild, আর Memory tab?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"DevTools হলো performance মাপার জন্য Flutter-এর প্রধান toolbox। Performance tab আমাকে দেখায় কোন frame ধীর আর কেন। Rebuild inspector দেখায় কোন widget বেশি বেশি rebuild হচ্ছে। Memory tab heap-এর ব্যবহার দেখায়, আর snapshot তুলনা করে leak ধরতে সাহায্য করে। মূল কথা এটাই: optimize করার আগে আমি মাপি।"

**এবার পুরোটা বুঝি:**

DevTools একজন ডাক্তারের যন্ত্রপাতির সেটের মতো। প্রতিটা যন্ত্র app-এর স্বাস্থ্য নিয়ে একটা প্রশ্নের উত্তর দেয়। `flutter run --profile` চালিয়ে আর terminal-এ ছাপা DevTools URL খুলে আপনি এটা connect করেন।

**ধাপ ১ — Performance tab: "কোন frame ধীর ছিল, আর কেন?"**
এটা frame-এর একটা timeline record করে। প্রতিটা frame-এ build time (UI thread) আর raster time দেখায়। Frame chart bar আঁকে — সবুজ bar মানে সময়মতো render হয়েছে, লাল bar মানে বাজেট ছাড়িয়ে গেছে।

যে workflow-টা মুখে বলবেন:
1. **record** চাপুন।
2. Jank হওয়া কাজটা আবার ঘটান (list scroll করুন, animation চালান)।
3. **stop** চাপুন।
4. একটা **লাল bar**-এ click করুন।
5. **Flame chart** নিচ থেকে উপরে পড়ুন, যে function সময় খেয়েছে সেটা খুঁজে বের করতে।

**ধাপ ২ — Rebuild inspector: "কোন widget বেশি rebuild হচ্ছে?"**
এটা Flutter Inspector-এর নিচে থাকে, প্রায়ই একে বলা হয় **"Track Widget Rebuilds"**। এটা প্রতিটা widget-এর পাশে rebuild count দেখায়। কোনো widget যদি তার পরিবর্তনের তুলনায় অনেক বেশি rebuild হয়, সেটা নষ্ট কাজ — সাধারণত একটা `const` বাদ পড়েছে ([Q4](#q4)) অথবা tree-এর অনেক উপরে `setState` আছে ([Q7](#q7))।

Debug করার সময় আপনি rebuild গুলো console-এও print করতে পারেন:

```dart
import 'package:flutter/widgets.dart';

void main() {
  debugPrintRebuildDirtyWidgets = true; // শুধু debug-এ — কী rebuild হলো তা print করে
  runApp(const MyApp());
}
```

**ধাপ ৩ — Memory tab: "কিছু কি leak করছে?"**
এটা Dart heap-এর একটা live graph দেখায় (কতটা memory ব্যবহার হচ্ছে)। Leak খুঁজতে ([Q18](#q18) দেখুন):
1. **Snapshot A** নিন।
2. একটা কাজ করুন — একটা screen খুলুন, তারপর বন্ধ করুন।
3. **GC** button চেপে garbage collection চালাতে বাধ্য করুন।
4. **Snapshot B** নিন।
5. দুটোর **diff** করুন। বন্ধ করা screen-এর object যদি এখনো থাকে, তাহলে leak আছে।

**ধাপ ৪ — Workflow-এর একটা সহজ মানসিক মানচিত্র।**

```
1. Performance tab   → record, reproduce, stop, click the red frame, read flame chart
2. Rebuild inspector → find high rebuild counts on widgets that should be stable
3. Memory tab        → snapshot → action → GC → snapshot → diff to find leaks
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা প্রমাণ চান যে আপনি শুধু code লিখে আশা করেন না যে এটা দ্রুত হবে। আপনি মাপেন, profile করেন, আর বারবার ঠিক করেন। DevTools-এর নাম ধরে জানাটা আসল production অভিজ্ঞতার লক্ষণ।

**সাধারণ ভুল:** Debug build থেকে DevTools-এর সংখ্যা পড়া আর সেগুলো বিশ্বাস করা। Debug-এ build time profile-এর চেয়ে কয়েক গুণ ধীর। সবসময় **profile-mode** build-এ, **আসল device**-এ DevTools attach করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flame chart কীভাবে পড়েন?"* → প্রতিটা bar একটা function call; প্রস্থ মানে খরচ হওয়া সময়। নিচ থেকে উপরে পড়ুন: সবচেয়ে চওড়া গভীর bar-টাই আপনার hot spot।
- *"Repaint rainbow কী?"* → DevTools-এর একটা toggle, যেটা কোনো layer repaint হলেই নতুন রঙ ঝলকায়, ফলে কী repaint হচ্ছে তা আপনি *দেখতে* পান ([Q14](#q14) দেখুন)।

**সম্পর্কিত:** [Q1 — jank খুঁজে বের করা](#q1) · [Q3 — debug বনাম profile](#q3) · [Q18 — memory leak](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. Debug mode-এ কেন কখনোই performance মাপা উচিত নয়?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Debug mode বানানো হয়েছে দ্রুত code লেখার জন্য, গতির জন্য নয়। এটা JIT compilation ব্যবহার করে, বাড়তি check আর assertion চালু রাখে, আর আসল app-এর চেয়ে প্রায়ই 5–10x ধীর। তাই release build একদম মসৃণ হলেও debug build দেখতে janky লাগতে পারে। আমি সবসময় profile বা release mode-এ, আসল device-এ মাপি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটি mode।**
Flutter আপনার app তিনটি mode-এর যেকোনো একটিতে build করে:

| Mode | কী দিয়ে compile হয় | কার জন্য | গতি |
|---|---|---|---|
| **debug** | JIT (চলার সময়ে compile) | hot reload, দ্রুত code লেখা | সবচেয়ে ধীর |
| **profile** | AOT (native-এ compile করা) | আসল performance মাপা | দ্রুত, tools চালু থাকে |
| **release** | AOT (native-এ compile করা) | আসল user | সবচেয়ে দ্রুত |

**ধাপ ২ — Debug ইচ্ছে করেই ধীর কেন।**
Debug mode গতি ছেড়ে developer-এর সুবিধা নেয়। এটা যোগ করে:
- **JIT compilation** — code চলার সময়ে compile হয়, যা আগে থেকে compile করা native code-এর চেয়ে ধীর।
- **Assertions** — বাড়তি নিরাপত্তা check (যেমন সেই বিখ্যাত "is this widget tree valid?") যা সময় খরচ করে।
- **Service hooks** — যেগুলো hot reload আর inspector চালু রাখে।

Code লেখার সময়ে এগুলো দারুণ, কিন্তু এগুলো timing-এর সংখ্যাগুলোকে অর্থহীন করে দেয়।

**ধাপ ৩ — মাপার জন্য profile mode ব্যবহার করুন।**
Profile mode release-এর মতোই native code-এ compile করে। কিন্তু DevTools-এর দরকারি tracing hook গুলো রেখে দেয়। মাপার জন্য এটাই সেরা জায়গা।

```bash
flutter run --profile      # DevTools দিয়ে আসল performance মাপুন
flutter run --release      # চূড়ান্ত, সবচেয়ে দ্রুত build, কোনো debug tool নেই
```

**ধাপ ৪ — সবসময় আসল device-এ test করুন।**
Emulator আর simulator-এ আসল phone-এর GPU আর CPU-র সীমা থাকে না। শক্তিশালী laptop emulator-এ একটা list মসৃণভাবে scroll হতে পারে, কিন্তু সস্তা Android phone-এ আটকে যাবে — আর BD-র অনেক user-এর কাছে ঠিক এই ধরনের device-ই থাকে। আসল, mid-range hardware-এ মাপুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা পরিপক্বতা যাচাইয়ের একটা দ্রুত filter। যে developer debug mode-এর lag "optimize" করেন, তিনি এমন একটা সমস্যায় সময় নষ্ট করছেন যা production-এ নেই।

**সাধারণ ভুল:** Debug build দেখে "app-টা janky" রিপোর্ট করা, অথবা শুধু high-end emulator-এ মাপা। দুটোই ভুল ফল দেয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Profile mode কী রাখে যা release ফেলে দেয়?"* → DevTools-এর দরকারি tracing আর timeline hook। সর্বোচ্চ গতির জন্য release এগুলো ছেঁটে ফেলে।
- *"Hot reload শুধু debug-এ কাজ করে কেন?"* → কারণ debug JIT ব্যবহার করে, যা চলার সময়েই নতুন code বসাতে পারে। Release আগে থেকে compile করা native, তাই এটা hot reload করতে পারে না।

**সম্পর্কিত:** [Q1 — jank খুঁজে বের করা](#q1) · [Q2 — DevTools](#q2)

[↑ উপরে ফিরুন](#toc)

---

# B. Rebuild কমানো

---

## <a id="q4"></a>4. `const` widget কীভাবে অপ্রয়োজনীয় rebuild ঠেকায়?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি যখন একটা widget-কে `const` করি, Dart সেটা compile time-এ একবার বানায় এবং সব জায়গায় ঠিক একই object আবার ব্যবহার করে। Rebuild-এর সময় Flutter পুরোনো আর নতুন widget-কে identity দিয়ে তুলনা করে। `const` widget আক্ষরিক অর্থেই আগের সেই একই object, তাই check-টা সাথে সাথে পাস হয়। ফলে Flutter ওই পুরো subtree-র rebuild বাদ দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `const` মানে "একবার বানানো, চিরকাল পুনরায় ব্যবহার।"**
সাধারণ widget constructor প্রতিবার `build()` চললে নতুন object বানায়। `const` constructor Dart-কে app চালু হওয়ার আগেই object বানাতে দেয়। তারপর যেখানে যেখানে সেটা আছে, সব জায়গায় ওই একটা object-ই শেয়ার হয়। এই শেয়ার করাকে বলে **canonicalization** — বড় শব্দ, মানে শুধু "একই জিনিস আবার ব্যবহার করা।"

```dart
const a = Text('Hello');
const b = Text('Hello');
print(identical(a, b)); // true — memory-তে ঠিক একই object
```

**ধাপ ২ — Flutter এটা দিয়ে কীভাবে কাজ বাদ দেয়।**
Parent rebuild হলে Flutter তার child-গুলোর উপর দিয়ে যায় আর প্রতিটার জন্য জিজ্ঞেস করে: "নতুন widget-টা কি পুরোনোটার *একই object*?" — এটা `identical()` check দিয়ে করে। উত্তর হ্যাঁ হলে কিছুই বদলায়নি। তাই Flutter ওই child-এর `build()` call করে না, আর তার subtree-তেও হাত দেয় না।

```
new widget == old widget (identical)?
        │
   yes  │  no
   ┌────┴─────┐
 skip       rebuild
 subtree    subtree
```

`const` widget সবসময় এই check পাস করে, কারণ এটা সেই একই শেয়ার করা object। তাই এটা বাদ পড়ে যায়।

**ধাপ ৩ — "সস্তা" widget-এর জন্যও এটা কেন জরুরি।**
একটা `Text` বাদ পড়া কিছুই না। কিন্তু scroll বা animation-এর সময় tree প্রতি সেকেন্ডে 60+ বার rebuild হতে পারে, হাজার হাজার widget জুড়ে। প্রতি frame-এ অপরিবর্তিত widget গুলো বাদ দিলে সব মিলিয়ে app অনেক বেশি মসৃণ হয়।

```dart
// const ছাড়া — প্রতি rebuild-এ নতুন Padding+Icon object, subtree আবার check হয়
Padding(
  padding: EdgeInsets.all(16),
  child: Icon(Icons.star, size: 48),
)

// const সহ — প্রতিবার একই object, Flutter পুরোটাই বাদ দেয়
const Padding(
  padding: EdgeInsets.all(16),
  child: Icon(Icons.star, size: 48),
)
```

**ধাপ ৪ — প্রমাণ করুন।**
DevTools-এ **"Track Widget Rebuilds"** চালু করুন ([Q2](#q2))। `const` widget-এর rebuild count বাড়া থেমে যায়, আর তার sibling গুলো rebuild হতেই থাকে। এটাই সেই optimization, চোখে দেখা যাচ্ছে।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান আপনি Flutter-এর reconciliation (সেই identity check) বোঝেন কি না। শুধু linter বলেছে বলে সব জায়গায় `const` ছিটিয়ে দেন কি না, সেটা নয়।

**সাধারণ ভুল:** বলা যে "`const` জিনিসটাকে immutable করে।" Flutter-এর প্রতিটা widget নকশা অনুযায়ীই আগে থেকে immutable। `const`-এর আসল দাম হলো **compile-time canonicalization** — একই object আবার ব্যবহার হয়, তাই identity check পাস করে আর rebuild বাদ পড়ে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Network থেকে আসা value `const` হতে পারে না কেন?"* → কারণ `const` app চালু হওয়ার আগেই জানা থাকতে হয়। Runtime value জানা থাকে না। যে অংশটা বদলায় সেটা আলাদা রাখুন, বাকিটা `const` করুন।
- *"Child-এ `const` দিলে কি parent-এর rebuild থামে?"* → না। এটা শুধু *child*-কে বাদ দিতে দেয়। Parent থামাতে হলে state নিচে নামাতে হয় ([Q7](#q7))।

**সম্পর্কিত:** [Q5 — widget বনাম method](#q5) · [Q7 — setState-এর scope](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Performance-এর জন্য helper method-এর চেয়ে ছোট widget class আলাদা করা কেন ভালো?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আলাদা widget class tree-তে নিজের একটা Element পায়, যেটা একটা rebuild boundary — input না বদলালে Flutter সেটা বাদ দিতে পারে। Helper method-এ এমন কোনো boundary নেই; তার widget গুলো parent-এর ভেতরেই inline হয়ে যায়। তাই parent rebuild হলে প্রতিবারই সেগুলো আবার চলে। এছাড়া আসল widget class `const` হতে পারে; method কখনোই পারে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — মূল ধারণা: widget class হলো একটা "checkpoint"।**
প্রতিটা widget-এর পেছনে Flutter-এর element tree-তে একটা **Element** থাকে। এই Element-ই Flutter-কে ঠিক করতে দেয় "এই অংশটা কি সত্যিই বদলেছে?" আলাদা widget class আলাদা Element বানায় — একটা checkpoint, যেখানে Flutter থেমে কাজ বাদ দিতে পারে।

`Widget _buildHeader()`-এর মতো helper method **কোনো** Element বানায় না। তার widget গুলো সরাসরি parent-এর output-এ ঢেলে দেওয়া হয়, মাঝখানে কোনো checkpoint থাকে না।

**ধাপ ২ — পার্থক্যটা দেখুন।**

```
Helper method approach:            Extracted widget approach:
ParentWidget.build()               ParentWidget.build()
 ├── _buildHeader()  ← inlined,     ├── HeaderWidget()  ← own Element,
 │     re-runs every parent build   │     can be skipped if unchanged
 ├── _buildBody()    ← inlined      ├── BodyWidget()    ← own Element
 └── _buildFooter()  ← inlined      └── FooterWidget()  ← own Element
   (all re-run together)              (each can skip independently)
```

Parent rebuild হলে method version তার *সব* inline widget আবার চালায়। Class version Flutter-কে প্রতিটা child check করতে দেয়, আর যাদের input মেলে তাদের বাদ দিতে দেয়।

**ধাপ ৩ — বোনাস: শুধু class-ই `const` হতে পারে।**
Helper method সবসময় তার body চালায় আর নতুন object বানায়। `const` constructor সহ widget *class* একই object হিসেবে আবার ব্যবহার হতে পারে এবং পুরোটাই বাদ পড়তে পারে ([Q4](#q4))। Method কখনোই `const` হতে পারে না।

**ধাপ ৪ — একটা পরিষ্কার before/after।**

```dart
// BAD — helper method, parent rebuild হলেই আবার চলে
class _ProductPageState extends State<ProductPage> {
  int quantity = 1;

  Widget _buildProductInfo() {       // quantity বদলালেই প্রতিবার আবার চলে
    return const Column(
      children: [
        Text('Product Name'),
        Text('Some long description...'),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        _buildProductInfo(),          // কিছু না বদলালেও rebuild হয়
        Text('Quantity: $quantity'),
        ElevatedButton(
          onPressed: () => setState(() => quantity++),
          child: const Text('+'),
        ),
      ],
    );
  }
}

// GOOD — আলাদা করা widget, নিজের Element, আর const তাই বাদ পড়ে
class ProductInfo extends StatelessWidget {
  const ProductInfo({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      children: [
        Text('Product Name'),
        Text('Some long description...'),
      ],
    );
  }
}

// Parent-এ:
Column(
  children: [
    const ProductInfo(),             // rebuild-এর সময় বাদ পড়ে
    Text('Quantity: $quantity'),
    ElevatedButton(
      onPressed: () => setState(() => quantity++),
      child: const Text('+'),
    ),
  ],
);
```

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি Element tree আর rebuild boundary বোঝেন কি না। শুধু মুখস্থ করা "best practices" নয়।

**সাধারণ ভুল:** বলা যে "method খারাপ কারণ এটা নতুন object বানায়।" এটা অর্ধেক গল্প মাত্র। আসল কারণ হলো method **কোনো Element boundary** বানায় না, তাই ওই অংশটা বাদ দেওয়ার কোনো উপায় Flutter-এর থাকে না। বাকি অর্ধেক: কেউ কেউ আবার বেশি extract করে ফেলেন — এক line-এর প্রতিটা widget-কে class-এ মুড়ে দিলে শুধু জঞ্জাল বাড়ে, লাভ হয় না। সেখানেই extract করুন যেখানে একটা boundary, একটা `const`, বা পুনরায় ব্যবহার পাওয়া যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"তাহলে কি build helper method কখনোই ব্যবহার করব না?"* → ছোট, সস্তা অংশের জন্য এগুলো ঠিক আছে। শুধু জেনে রাখুন এগুলো rebuild boundary দেয় না। তাই অংশটা ব্যয়বহুল বা স্থির হলে class-ই ভালো।
- *"আলাদা করা widget-এ কি `const` লাগবেই?"* → `const` হলো উপরের সাজসজ্জা — এটা Flutter-কে identity-equal check পর্যন্ত বাদ দিতে দেয়। `const` ছাড়াও input মিলে গেলে আলাদা Element-টা সাহায্য করে।

**সম্পর্কিত:** [Q4 — const widget](#q4) · [Q6 — build() golden rule](#q6) · [Q7 — setState-এর scope](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. `build()` method-এর golden rule কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`build()` অবশ্যই একটা pure function হতে হবে: দ্রুত, আর কোনো side effect ছাড়া। একই state আর props দিলে এটা একই widget tree ফেরত দেবে, আর অন্য কিছুই করবে না। এর ভেতরে কোনো network call নয়, কোনো timer নয়, কোনো analytics নয়। কারণ Flutter যেকোনো সময় আর সেকেন্ডে অনেকবার `build()` call করতে পারে। তাই এর ভেতরে বাড়তি যা কিছু আছে, সব কয়েক ডজন বার করে চলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটা শব্দ: pure, fast, no side effects।**
- **Pure** — একই input (state + props) সবসময় একই widget tree দেয়। এটা শুধু state *পড়ে* আর widget *ফেরত দেয়*।
- **No side effects** — এটা বাইরের জগৎ বদলায় না: কোনো HTTP call নয়, কোনো database write নয়, কোনো timer নয়, কোনো stream subscription নয়, কোনো analytics event log করা নয়।
- **Fast** — animation-এর সময় এটা সেকেন্ডে 60–120 বার চলতে পারে। তাই 16ms-এর অনেক নিচে শেষ হতে হবে।

**ধাপ ২ — এই নিয়মটা কেন আছে।**
Flutter যখন খুশি আর যত খুশি বার `build()` call করার অধিকার রাখে। তাই ধরুন side effect-টা একটা network request:

```dart
// BAD — প্রতিটা rebuild-এ এগুলো সবই চলে
@override
Widget build(BuildContext context) {
  fetchUser().then((u) => setState(() => user = u)); // প্রতি frame-এ network call!
  final cfg = jsonDecode(hugeJsonString);             // প্রতি frame-এ ধীর parse
  analytics.logScreenView('profile');                 // duplicate event
  return Text(user?.name ?? 'Loading');
}
```

একটামাত্র animation-এর সময় এটা কয়েক ডজন duplicate request পাঠাতে পারে। আর JSON-টা কয়েক ডজন বার parse করতে পারে। Screen frame drop করে। আর backend-এ spam হয়।

**ধাপ ৩ — Side effect-এর জায়গা কোথায়।**
একবারের কাজ `initState`-এ রাখুন। আর প্রতি action-এর কাজ event handler বা অন্য lifecycle method-এ রাখুন।

```dart
// GOOD — build() pure আর দ্রুত
class _UserProfileState extends State<UserProfile> {
  User? user;

  @override
  void initState() {
    super.initState();
    _loadUser();                       // side effect এখানে, একবার চলে
    analytics.logScreenView('profile'); // lifecycle, একবার চলে
  }

  Future<void> _loadUser() async {
    final u = await fetchUser();
    if (mounted) setState(() => user = u); // setState-এর আগে mounted check করুন
  }

  @override
  Widget build(BuildContext context) {
    // Pure: state পড়ুন, widget ফেরত দিন। আর কিছু নয়।
    return user == null
        ? const CircularProgressIndicator()
        : Text(user!.name);
  }
}
```

**ধাপ ৪ — পুরোনো ফাঁদ: `build()`-এর ভেতরে Future/Stream তৈরি করা।**
যে `FutureBuilder` বা `StreamBuilder`-এর future/stream `build()`-এর *ভেতরে* তৈরি হয়, সেটা প্রতি rebuild-এ একদম নতুন একটা বানায়। পুরোনো result ফেলে দিয়ে আবার fetch করে।

```dart
// BAD — প্রতি rebuild-এ নতুন future
FutureBuilder(future: fetchUser(), builder: ...);

// GOOD — একবার তৈরি করুন, রেখে দিন, পাস করুন
late final Future<User> _userFuture = fetchUser(); // State-এর ভেতরে
FutureBuilder(future: _userFuture, builder: ...);
```

**Interviewer কেন জিজ্ঞেস করে:** এটা Flutter-এ পরিপক্বতার একটা litmus test। এই নিয়ম ভাঙলে সবচেয়ে খারাপ bug আসে: duplicate request, infinite loop, flicker, আর এমন ধীরগতি যার কারণ খুঁজে বের করা কঠিন।

**সাধারণ ভুল:** `build()`-এর ভেতরে সরাসরি একটা `async` function call করা, আর বুঝতে না পারা যে এটা প্রতি rebuild-এ চলে। আর উপরের future-inside-build ফাঁদটা। Future/stream সবসময় `build()`-এর বাইরে তৈরি করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"তাহলে timer বা subscription কোথায় শুরু করব?"* → `initState`-এ, আর `dispose()`-এ cancel করুন ([Q18](#q18))।
- *"Screen খোলার সময় সত্যিই data দরকার হলে কী করব?"* → `initState`-এ load শুরু করুন, result state-এ রাখুন, আর `build()` শুধু সেটা পড়বে।

**সম্পর্কিত:** [Q5 — widget vs method](#q5) · [Q7 — setState scope](#q7) · [Q18 — dispose](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. Tree-এর উপরের দিকে `setState` call করা কেন এড়ানো উচিত, আর কীভাবে ঠিক করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`setState` যে widget-এ call করা হয়, সেটা আর তার পুরো subtree rebuild করে। আমি যদি screen-level widget-এ এটা call করি, তাহলে একটা ছোট পরিবর্তনের জন্য শত শত child rebuild হয় — যেগুলো বদলায়নি সেগুলোও। সমাধান হলো state-টাকে নিচে নামিয়ে সবচেয়ে ছোট widget-এ নিয়ে যাওয়া, যেটা সত্যিই এটা ব্যবহার করে। অথবা এমন state-management tool ব্যবহার করা, যেটা শুধু সঠিক consumer-গুলোই rebuild করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `setState` আসলে কী করে।**
`setState` বর্তমান widget-এর Element-কে "dirty" চিহ্নিত করে। তারপর Flutter-কে বলে এটা আর এর নিচের সবকিছু rebuild করতে। ওই subtree যত বড় আর যত গভীর, খরচ তত বাড়ে।

**ধাপ ২ — সমস্যাটা এঁকে দেখানো।**

```
setState at the top:               setState pushed down:
AppRoot  ← setState                AppRoot
 ├── Header   (rebuilt)             ├── Header   (untouched)
 ├── Body     (rebuilt)             ├── Body     (untouched)
 │   ├── List (rebuilt)             │   ├── List (untouched)
 │   └── Cards(rebuilt)             │   └── Cards(untouched)
 └── Footer   (rebuilt)             └── Footer
     └── CartBadge (rebuilt)            └── CartBadge ← setState (only this)
  Everything rebuilds                Only CartBadge rebuilds
```

উপরে একটামাত্র boolean toggle শত শত rebuild ঘটাতে পারে। ওই একই toggle যদি ছোট একটা leaf widget-এর হয়, তাহলে শুধু ওই leaf-টাই rebuild হয়।

**ধাপ ৩ — সমাধান ১: state নিচে নামান।**
`StatefulWidget`-টাকে tree-র সবচেয়ে ছোট অংশে সরান, যে অংশ এটার উপর নির্ভর করে।

```dart
// BAD — একটা heart icon-এর জন্য পুরো page stateful
class _ProductPageState extends State<ProductPage> {
  bool isFavorite = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Product')),   // অকারণে rebuilt
      body: Column(children: [
        const ProductImage(),                          // অকারণে rebuilt
        const ProductReviews(),                        // অকারণে rebuilt
        IconButton(
          icon: Icon(isFavorite ? Icons.favorite : Icons.favorite_border),
          onPressed: () => setState(() => isFavorite = !isFavorite),
        ),
      ]),
    );
  }
}

// GOOD — শুধু button-টাই stateful
class FavoriteButton extends StatefulWidget {
  const FavoriteButton({super.key});
  @override
  State<FavoriteButton> createState() => _FavoriteButtonState();
}

class _FavoriteButtonState extends State<FavoriteButton> {
  bool isFavorite = false;
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: Icon(isFavorite ? Icons.favorite : Icons.favorite_border),
      onPressed: () => setState(() => isFavorite = !isFavorite),
    );
  }
}

// এখন page একটা পরিষ্কার StatelessWidget:
class ProductPage extends StatelessWidget {
  const ProductPage({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Product')),
      body: const Column(children: [
        ProductImage(),
        ProductReviews(),
        FavoriteButton(), // tap করলে শুধু এটাই rebuild হয়
      ]),
    );
  }
}
```

**ধাপ ৪ — সমাধান ২: state-management tool বা `ValueNotifier`।**
Shared state-এর জন্য Provider/Riverpod/Bloc rebuild-কে নির্দিষ্ট consumer-এ সীমিত রাখে ([Q8](#q8), [Q9](#q9))। একটামাত্র সহজ value-র জন্য `ValueNotifier` + `ValueListenableBuilder` শুধু builder-টাই rebuild করে:

```dart
final isFavorite = ValueNotifier(false);

ValueListenableBuilder<bool>(
  valueListenable: isFavorite,
  builder: (context, fav, _) => Icon(fav ? Icons.favorite : Icons.favorite_border),
);
// isFavorite.value = true;  → শুধু এই builder rebuild হয়, আর কিছু নয়
```

**Interviewer কেন জিজ্ঞেস করে:** মাঝারি স্তরের developer-দের লেখা app-এ এটাই সবচেয়ে সাধারণ performance সমস্যা। এটা যাচাই করে আপনি rebuild-এর *scope* আর ভালো widget decomposition বোঝেন কি না।

**সাধারণ ভুল:** Child-গুলোতে `const` দিলেই সমস্যা পুরোপুরি ঠিক হয়ে যায় — এটা ভাবা। `const` child-গুলোকে skip করতে দেয়। কিন্তু parent-এর `build()` তবুও উপর থেকে নিচ পর্যন্ত চলে, আর প্রতিটা non-const child rebuild করে। কাঠামোগত সমাধান হলো state নিচে নামানো, যাতে rebuild আরও নিচ থেকে শুরু হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`ValueNotifier` না কি পুরো state-management package?"* → একটা বা দুটো সহজ local value-র জন্য `ValueNotifier` একদম ঠিক। State যখন অনেক widget বা screen-এ shared, তখন Provider/Riverpod/Bloc নিন।
- *"State নিচে নামালে readability কি খারাপ হয়?"* → সাধারণত উল্টো ভালো হয় — প্রতিটা widget শুধু নিজের কাজটাই সামলায়।

**সম্পর্কিত:** [Q4 — const widget](#q4) · [Q5 — widget vs method](#q5) · [Q8 — Selector vs Consumer](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. Provider-এ `Selector` আর `Consumer`-এর পার্থক্য কী, আর `Selector` কেন বেশি performant?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"provide করা object যখনই `notifyListeners()` call করে, `Consumer` তখনই rebuild হয় — তাই যেকোনো field-এর যেকোনো পরিবর্তনে এটা rebuild হয়। `Selector` আগে একটা নির্দিষ্ট value বেছে নেয়। শুধু *সেই* value বদলালেই rebuild হয়। তাই কোনো widget-এর যদি শুধু cart count লাগে, `Selector` promo code-এর মতো সম্পর্কহীন পরিবর্তন উপেক্ষা করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `Consumer` সব কিছুতেই react করে।**
`Consumer<T>` পুরো object `T`-কে শোনে। প্রতিটা `notifyListeners()` এর builder-কে rebuild করায়। এই widget যে field নিয়ে চিন্তিত, সেটা না বদলালেও rebuild হয়। এটা `context.watch<T>()`-এর মতোই।

**ধাপ ২ — `Selector` একটা filter যোগ করে।**
`Selector<T, S>` একটা `selector` function নেয়। সেই function `T` থেকে একটা value `S` বের করে আনে। এরপর পুরোনো আর নতুন `S`-কে `==` দিয়ে তুলনা করে। `S` সত্যিই বদলালে তবেই builder rebuild হয়। একে বলে fine-grained বা granular reactivity।

**ধাপ ৩ — একটা বাস্তব উদাহরণ।**

```dart
class CartModel extends ChangeNotifier {
  final List<Item> _items = [];
  String _promoCode = '';

  int get itemCount => _items.length;
  String get promoCode => _promoCode;

  void addItem(Item item) {
    _items.add(item);
    notifyListeners(); // count বদলে গেছে
  }

  void setPromoCode(String code) {
    _promoCode = code;
    notifyListeners(); // count বদলায়নি, তবু Consumer rebuild হবে
  }
}

// BAD — শুধু promo code বদলালেও cart badge rebuild হয়
Consumer<CartModel>(
  builder: (context, cart, child) =>
      Badge(label: Text('${cart.itemCount}'), child: child!),
  child: const Icon(Icons.shopping_cart),
)

// GOOD — শুধু itemCount বদলালে rebuild হয়
Selector<CartModel, int>(
  selector: (context, cart) => cart.itemCount,
  builder: (context, count, child) =>
      Badge(label: Text('$count'), child: child!),
  child: const Icon(Icons.shopping_cart),
)
```

`setPromoCode('SAVE10')`-এর পরে `Selector` দেখে `itemCount` এখনো একই সংখ্যা। তাই এটা badge-টা rebuild করে **না**। `Consumer` হলে অকারণেই rebuild করত।

**ধাপ ৪ — `child` কৌশল (দুটোতেই কাজ করে)।**
builder-এর ভেতরে `child:` parameter আর `child!` খেয়াল করুন। `child` হিসেবে পাঠানো widget একবার build হয় আর প্রতিটা rebuild-এ পুনরায় ব্যবহার হয় — ছোট একটা built-in `const`-এর মতো। builder-এর ভেতরের যে অংশ কখনো বদলায় না, তার জন্য এটা ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি state management-কে basic-এর বাইরে গিয়ে tune করতে পারেন কি না। shared state-ওয়ালা বড় app-এ `Selector` প্রতিটা interaction-এ কয়েক ডজন rebuild বাঁচাতে পারে।

**সাধারণ ভুল:** `cart.items`-এর মতো mutable object বা list select করা। `Selector` যেহেতু `==` দিয়ে তুলনা করে, একই mutate করা list reference-কে "অপরিবর্তিত" মনে হয় (বা identity অনুযায়ী "পরিবর্তিত" মনে হয়)। ফলে আচরণ ভুল হয়। তাই derived primitive (যেমন `itemCount`) বা একটা immutable copy select করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা Bloc-এর সাথে কীভাবে মেলে?"* → `Selector` হলো Bloc-এর `buildWhen`-এর Provider সংস্করণ ([Q9](#q9)) — দুটোই ঠিক করে কোন পরিবর্তনে widget react করবে।
- *"`context.select` কী করে?"* → এটা `build` method-এর ভেতরে একটা shorthand, যা একটা value watch করে। কাজটা `Selector`-এর মতোই।

**সম্পর্কিত:** [Q7 — setState-এর scope](#q7) · [Q9 — buildWhen](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. `BlocBuilder`-এ `buildWhen` কীভাবে অপ্রয়োজনীয় rebuild কমায়?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Default-এ Bloc যত নতুন state emit করে, `BlocBuilder` ততবারই rebuild হয়। `buildWhen` এমন একটা function যা previous আর current state পায় এবং একটা bool return করে। এটা false return করলে নতুন state আসা সত্ত্বেও builder skip হয়। ফলে একটা widget state-এর শুধু যে অংশ নিয়ে চিন্তিত, সেটাতেই react করতে পারে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Default আচরণ।**
Bloc যখনই নতুন state emit করে, `BlocBuilder<Bloc, State>` তখনই তার builder rebuild করে। আপনার state class-এ অনেক field থাকলে *যেকোনো* একটা field-এর update ওই state-এর *প্রতিটা* `BlocBuilder` rebuild করায়।

**ধাপ ২ — `buildWhen` একটা gate।**
`buildWhen: (previous, current) => ...` প্রতিটা emission-এ ঠিক করে এই builder চলবে কি না। rebuild করাতে `true` return করুন, skip করতে `false`। এটাই সেই filter, যেটা বলে "শুধু orders বদলালে react করো।"

```dart
class DashboardState {
  final List<Order> orders;
  final UserProfile profile;
  const DashboardState({this.orders = const [], required this.profile});
}

// BAD — profile বদলালেও rebuild হয়
BlocBuilder<DashboardBloc, DashboardState>(
  builder: (context, state) => OrderList(orders: state.orders),
)

// GOOD — শুধু orders list বদলালে rebuild হয়
BlocBuilder<DashboardBloc, DashboardState>(
  buildWhen: (prev, curr) => prev.orders != curr.orders,
  builder: (context, state) => OrderList(orders: state.orders),
)

// profile section নিজের field-এর উপর gate বসায়:
BlocBuilder<DashboardBloc, DashboardState>(
  buildWhen: (prev, curr) => prev.profile != curr.profile,
  builder: (context, state) => ProfileCard(profile: state.profile),
)
```

**ধাপ ৩ — এর জুড়িদার: `listenWhen`।**
`BlocListener`-এ একই ধারণা কাজ করে side effect-এর জন্য (যেমন snackbar দেখানো)। `listenWhen` ঠিক করে listener কখন চলবে:

```dart
BlocListener<DashboardBloc, DashboardState>(
  listenWhen: (prev, curr) => prev.isLoading && !curr.isLoading,
  listener: (context, state) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Loaded!')),
    );
  },
)
```

**ধাপ ৪ — এটা সঠিক equality-র উপর নির্ভর করে।**
`buildWhen` state-গুলো `!=` দিয়ে তুলনা করে। তাই আপনার state class-এ ঠিকঠাক value equality থাকতে হবে (সাধারণত `Equatable` বা `freezed` দিয়ে)। এটা না থাকলে একই data-র দুটো state আলাদা মনে হয়। আর `buildWhen` সবসময় true return করে।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি Bloc *বড় পরিসরে* ব্যবহার করতে পারেন কি না — শুধু state emit করা নয়, কোন widget কোন পরিবর্তনে react করবে সেটাও নিয়ন্ত্রণ করা। বড় app-এ `buildWhen` না থাকলে পুরো screen জুড়ে rebuild cascade হয়।

**সাধারণ ভুল:** list-টা জায়গাতেই mutate করা আর একই list reference নিয়ে state emit করা। তখন `prev.orders != curr.orders` হয় `false` (একই reference) আর UI কখনোই update হয় না। সবসময় নতুন list emit করুন, যেমন `copyWith(orders: [...state.orders, newOrder])`।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`buildWhen` vs `Selector`?"* → আলাদা library-তে একই লক্ষ্য: কোন state পরিবর্তনে rebuild হবে সেটা filter করা। `buildWhen` হলো Bloc-এর; `Selector` হলো Provider-এর ([Q8](#q8))।
- *"equality কোথা থেকে আসে?"* → `Equatable`/`freezed` থেকে, যেগুলো আপনার state-এ সঠিক `==` আর `hashCode` generate করে।

**সম্পর্কিত:** [Q8 — Selector vs Consumer](#q8) · [Q7 — setState-এর scope](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. search-as-you-type-এর মতো ব্যয়বহুল কাজ আপনি কীভাবে debounce বা throttle করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Debounce মানে 'user কাজটা থামানো পর্যন্ত অপেক্ষা করো, তারপর একবার চালাও।' Throttle মানে 'যত ঘন ঘনই ঘটুক, প্রতি X millisecond-এ সর্বোচ্চ একবার চালাও।' search box-এর জন্য আমি API call debounce করি, যাতে প্রতিটা keystroke-এ request না যায় — টাইপ থামা পর্যন্ত অপেক্ষা করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দৈনন্দিন উপমা।**
- **Debounce** হলো lift-এর দরজার মতো: কেউ ঢুকলেই timer আবার শুরু হয়; মানুষ আসা *বন্ধ* হলে তবেই দরজা বন্ধ হয়।
- **Throttle** হলো turnstile-এর মতো, যা প্রতি ২ সেকেন্ডে একজনকে যেতে দেয় — একসাথে কতজন ধাক্কা দিচ্ছে তাতে কিছু যায় আসে না।

**ধাপ ২ — performance-এর জন্য এটা কেন গুরুত্বপূর্ণ।**
যে search field প্রতিটা keystroke-এ server call করে, সেটা "f", "fl", "flu", "flut"... প্রতিটার জন্য request পাঠায়। এতে network আর backend ভেসে যায়, আর অনেক rebuild ঘটে। Debounce দশটা keystroke-কে একটা request-এ নামিয়ে আনে, user থামার পরে।

**ধাপ ৩ — `Timer` দিয়ে debounce।**

```dart
import 'dart:async';

class _SearchState extends State<SearchBar> {
  Timer? _debounce;

  void _onChanged(String query) {
    _debounce?.cancel(); // প্রতিটা keystroke-এ timer reset
    _debounce = Timer(const Duration(milliseconds: 400), () {
      _runSearch(query); // 400ms টাইপ না করলে তবেই চলে
    });
  }

  @override
  void dispose() {
    _debounce?.cancel(); // পরিষ্কার করুন — দেখুন Q18
    super.dispose();
  }
}
```

**ধাপ ৪ — stream-এ debounce (Rx ধরন)।**
আপনি stream বা RxDart ব্যবহার করলে built-in operator আছে:

```dart
// RxDart
queryStream
    .debounceTime(const Duration(milliseconds: 400))
    .distinct() // একই text বারবার এলে উপেক্ষা করো
    .listen(_runSearch);
```

**ধাপ ৫ — Throttle (একটা স্থির সর্বোচ্চ হারে চালানো)।**
যেসব জিনিস অনবরত ঘটে, তাদের জন্য throttle ব্যবহার করুন। যেমন একটা scroll handler, যেটা "scroll progress" bar update করে:

```dart
DateTime _last = DateTime.fromMillisecondsSinceEpoch(0);

void _onScroll() {
  final now = DateTime.now();
  if (now.difference(_last) < const Duration(milliseconds: 100)) return;
  _last = now;
  _updateProgressBar(); // প্রতি 100ms-এ সর্বোচ্চ একবার
}
```

**Interviewer কেন জিজ্ঞেস করে:** search আর live-filter screen সব জায়গায় আছে। তাঁরা দেখতে চান আপনি network আর UI-কে প্রতিটা ছোট event-এ কাজ করা থেকে বাঁচান কি না।

**সাধারণ ভুল:** `dispose()`-এ debounce timer `cancel()` করতে ভুলে যাওয়া। এতে leak হয় আর widget চলে যাওয়ার পরেও timer চলতে পারে ([Q18](#q18))। আরেকটা: যেখানে throttle দরকার সেখানে debounce করা (বা উল্টোটা) — "থামার পরে" চাইলে debounce, "স্থির হারে" চাইলে throttle বেছে নিন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এক লাইনে debounce vs throttle?"* → Debounce = চুপ হওয়া পর্যন্ত অপেক্ষা, তারপর একবার চালানো। Throttle = event আসতে থাকলেও একটা নির্দিষ্ট সময়সূচিতে চালানো।
- *"timer কোথায় cancel করেন?"* → `dispose()`-এ, অন্য যেকোনো resource-এর মতোই।

**সম্পর্কিত:** [Q6 — build() golden rule](#q6) · [Q18 — dispose](#q18)

[↑ উপরে ফিরুন](#toc)

---

# C. লম্বা list আর scrolling

---

## <a id="q11"></a>11. `ListView` vs `ListView.builder` vs `ListView.separated` vs `ListView.custom` — কোনটা কখন ব্যবহার করবেন, আর performance-এর পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"মূল পার্থক্য হলো eager বনাম lazy building। ডিফল্ট `ListView` সব child আগেই build করে ফেলে — ছোট list-এর জন্য ঠিক আছে। `ListView.builder` child-গুলো lazily build করে, শুধু যখন সেগুলো screen-এ আসে। তাই এটা হাজার হাজার item পর্যন্ত scale করে। `.separated` হলো সেই lazy builder, সাথে item-এর মাঝে একটা separator। `.custom` দেয় পুরো নিয়ন্ত্রণ — child কীভাবে তৈরি আর recycle হবে তার উপর।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Eager বনাম lazy, মূল ধারণা।**
- **Eager** = সব child এখনই build করা, screen-এ থাকুক বা না থাকুক।
- **Lazy** = একটা child তখনই build করা, যখন সেটা দেখা যাওয়ার মুহূর্ত আসে।

ধরুন 10,000 item-এর একটা list, যার মাত্র 10টা screen-এ ধরে। Eager 10,000টা widget-ই build করে। Lazy build করে প্রায় 10টা (সাথে সামান্য buffer)।

**ধাপ ২ — চারটা constructor।**

- **`ListView(children: [...])`** — **সব** child একসাথে build করে। শুধু ছোট, নির্দিষ্ট list-এর জন্য ব্যবহার করুন (মোটামুটি 20 item-এর নিচে)। এর বেশি হলে সময় আর memory দুটোই নষ্ট হয়।
- **`ListView.builder`** — শুধু দৃশ্যমান item-এর জন্য `itemBuilder` call করে। খরচ O(visible), O(total) নয়। যেকোনো লম্বা বা dynamic list-এ ব্যবহার করুন।
- **`ListView.separated`** — একই lazy আচরণ, সাথে divider/spacing-এর জন্য একটা `separatorBuilder`। এতে আপনার item builder পরিষ্কার থাকে আর index সহজ থাকে।
- **`ListView.custom`** — সরাসরি একটা `SliverChildDelegate` নেয়। তাই child কীভাবে build হবে, size পাবে, আর alive থাকবে — সব আপনি নিয়ন্ত্রণ করেন। উন্নত ক্ষেত্রে ব্যবহার করুন (আলাদা আলাদা ধরনের source, custom keep-alive)।

**ধাপ ৩ — একটা তুলনার তালিকা।**

| Constructor | Build cost | Memory | কখন ব্যবহার করবেন |
|---|---|---|---|
| `ListView(children:)` | O(n) — সব আগেই | সবই memory-তে | ছোট, নির্দিষ্ট list (<~20) |
| `ListView.builder` | O(visible) | শুধু দৃশ্যমানগুলো | লম্বা / dynamic list |
| `ListView.separated` | O(visible) | শুধু দৃশ্যমানগুলো | item-এর মাঝে divider লাগলে |
| `ListView.custom` | O(visible)* | নিজের মতো সাজানো যায় | custom child management |

\* আপনার delegate-এর উপর নির্ভর করে

**ধাপ ৪ — প্রতিটার code।**

```dart
// লম্বা list-এর জন্য খারাপ — এখনই 10,000টা build করে
ListView(
  children: List.generate(10000, (i) => ListTile(title: Text('Item $i'))),
);

// ভালো — শুধু যা দৃশ্যমান তাই build করে
ListView.builder(
  itemCount: 10000,
  itemBuilder: (context, index) => ListTile(title: Text('Item $index')),
);

// ভালো — lazy + পরিষ্কার divider
ListView.separated(
  itemCount: 10000,
  itemBuilder: (context, index) => ListTile(title: Text('Item $index')),
  separatorBuilder: (context, index) => const Divider(height: 1),
);

// উন্নত — delegate দিয়ে পুরো নিয়ন্ত্রণ
ListView.custom(
  childrenDelegate: SliverChildBuilderDelegate(
    (context, index) => MyItem(index: index),
    childCount: 10000,
  ),
);
```

**Interviewer কেন জিজ্ঞেস করে:** লম্বা list-এ ডিফল্ট `ListView` ব্যবহার করা Flutter-এর সবচেয়ে সাধারণ performance bug-গুলোর একটা। এই প্রশ্নটা দ্রুত আলাদা করে দেয় — কে list virtualization বোঝেন আর কে বোঝেন না।

**সাধারণ ভুল:** 3–5 item-এর ছোট static list-এ `.builder` ব্যবহার করা — সেখানে lazy যন্ত্রপাতিটা অকারণ overhead। আর `itemCount` ভুলে যাওয়া: সেটা না দিলে builder ধরে নেয় list অসীম, আর scrollbar অদ্ভুত আচরণ করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`GridView`-এর ক্ষেত্রে কী?"* → একই ধারণা: `GridView.builder` হলো lazy version। একই নিয়ম খাটে।
- *"Sliver কী?"* → scrollable-এর একটা নিচু স্তরের অংশ। `CustomScrollView` + sliver দিয়ে এক scroll view-এ list, grid আর header মেশানো যায়।

**সম্পর্কিত:** [Q12 — pagination](#q12) · [Q13 — keys আর keep-alive](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. Lazy loading আর pagination (কার্যকর infinite scroll) কীভাবে implement করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Infinite scroll একটা page load করে। User নিচের দিকে এলে পরের page fetch করে। আমি position ধরার জন্য `ScrollController` ব্যবহার করি, lazy item building-এর জন্য `ListView.builder`, আর ডাবল fetch থামাতে একটা flag। আমি 'আর data নেই' অবস্থাটাও handle করি এবং controller dispose করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — রেসিপি।**
তিনটা উপকরণ:
1. Scroll position দেখার জন্য একটা **`ScrollController`**।
2. একটা **loading flag**, যাতে দুটো fetch একসাথে না চলে।
3. একটা **`ListView.builder`**, যাতে শুধু দৃশ্যমান item build হয় ([Q11](#q11))।

**ধাপ ২ — Trigger।**
Scroll position শুনুন। User একটা সীমা পার করলে (ধরুন 80% নিচে নামলে) পরের page load করুন — তবে যদি আগের একটা load চলতে না থাকে এবং আর data বাকি থাকে।

**ধাপ ৩ — পূর্ণ, নিরাপদ উদাহরণ।**

```dart
class _InfiniteListState extends State<InfiniteList> {
  final _controller = ScrollController();
  final _items = <Article>[];
  int _page = 1;
  bool _isLoading = false;
  bool _hasMore = true;

  @override
  void initState() {
    super.initState();
    _loadMore();                         // প্রথম page
    _controller.addListener(_onScroll);
  }

  void _onScroll() {
    final pos = _controller.position;
    if (pos.pixels >= pos.maxScrollExtent * 0.8) {
      _loadMore();                       // প্রায় নিচে চলে এসেছে
    }
  }

  Future<void> _loadMore() async {
    if (_isLoading || !_hasMore) return; // ডাবল fetch ঠেকানোর guard
    setState(() => _isLoading = true);
    try {
      final next = await api.fetchArticles(page: _page);
      setState(() {
        _items.addAll(next);
        _page++;
        _hasMore = next.isNotEmpty;      // খালি page = data শেষ
        _isLoading = false;
      });
    } catch (_) {
      setState(() => _isLoading = false); // user আবার চেষ্টা করতে পারবে
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      controller: _controller,
      itemCount: _items.length + (_hasMore ? 1 : 0), // spinner-এর জন্য +1
      itemBuilder: (context, index) {
        if (index == _items.length) {
          return const Center(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: CircularProgressIndicator(),
            ),
          );
        }
        return ArticleCard(article: _items[index]);
      },
    );
  }

  @override
  void dispose() {
    _controller.removeListener(_onScroll);
    _controller.dispose();               // leak এড়ান — দেখুন Q18
    super.dispose();
  }
}
```

**ধাপ ৪ — যে edge case-গুলো বলা দরকার।**
- **ডাবল fetch:** `_isLoading` guard সেগুলো থামায়।
- **Data শেষ:** `_hasMore` নিচের spinner বন্ধ করে দেয়।
- **Error:** `_isLoading` reset করুন, যাতে user আবার scroll করে চেষ্টা করতে পারেন।
- **Cleanup:** listener সরান আর controller dispose করুন।

**Interviewer কেন জিজ্ঞেস করে:** Pagination প্রায় সব production app-এর দরকার। তাঁরা দেখতে চান আপনি edge case-গুলো handle করেন, শুধু happy path নয়।

**সাধারণ ভুল:** `_isLoading` guard না রাখা। তখন দ্রুত scroll করলে একই page-এর জন্য কয়েকটা request যায়, আর duplicate item আসে। আর `ScrollController` dispose করতে ভুলে যাওয়া, যা leak করে ([Q18](#q18))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Bloc/Riverpod দিয়ে এটা কীভাবে করবেন?"* → একই logic, তবে page state আর loading flag থাকে Bloc/notifier-এ। Widget শুধু সেগুলো পড়ে।
- *"কোনো package আছে?"* → `infinite_scroll_pagination` boilerplate সামলায়, কিন্তু interviewer আগে হাতে করে দেখাতে পারাটা পছন্দ করেন।

**সম্পর্কিত:** [Q11 — ListView-এর ধরন](#q11) · [Q13 — keys আর keep-alive](#q13) · [Q18 — dispose](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. Key আর `AutomaticKeepAliveClientMixin` ব্যবহার করে scroll-এর সময়ের সমস্যা কীভাবে এড়াবেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`.builder`-এ list item screen-এর বাইরে গেলে Flutter memory বাঁচাতে তাদের state ধ্বংস করে দেয়। ফিরে এলে আবার নতুন করে build করে। Item সরলে বা নতুন item ঢুকলে Key নিশ্চিত করে যে Flutter প্রতিটা item-কে ঠিক state-এর সাথে মেলাচ্ছে। `AutomaticKeepAliveClientMixin` list-কে বলে দেয় — একটা নির্দিষ্ট item-এর state screen-এর বাইরে থাকলেও alive রাখো। তাই সেটা data হারায় না, flicker-ও করে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ডিফল্টে screen-এর বাইরে কী হয়।**
`ListView.builder`-এ যেসব item দৃশ্যের বাইরে চলে যায়, memory খালি করতে তাদের State ফেলে দেওয়া হয়। ফিরে এলে সেগুলো নতুন করে build হয়। সাধারণত এটা ঠিকই আছে, কিন্তু এতে দুটো সমস্যা হয়:
1. যেসব item-এর setup ব্যয়বহুল (network image, জটিল layout), সেগুলো ফিরে আসার সময় **flicker** করে।
2. যেসব item-এ user state থাকে (text field, checkbox), সেগুলো নিজের মান **হারায়**।

**ধাপ ২ — Key: ঠিক item-কে ঠিক state-এর সাথে মেলানো।**
Reconciliation-এর সময় পুরোনো আর নতুন widget কীভাবে জোড়া লাগবে, তা একটা `Key` Flutter-কে বলে দেয়। Key না থাকলে Flutter position দেখে মেলায়। Item insert, remove বা reorder করলে সেটা ভেঙে যায়, আর ভুল state ভুল item-এ লেগে যায়। Item-এর unique id দিয়ে বানানো একটা `ValueKey` এটা ঠিক করে দেয়।

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => ProductCard(
    key: ValueKey(items[index].id), // স্থায়ী পরিচয়, reorder-এও টিকে থাকে
    product: items[index],
  ),
);
```

**ধাপ ৩ — `AutomaticKeepAliveClientMixin`: একটা item-কে alive রাখা।**
এই mixin screen-এর বাইরে থাকা item-এর State ধ্বংস না করে memory-তে রেখে দেয়। Render object detach হয়ে যায় (তাই GPU resource মুক্ত হয়), কিন্তু State টিকে থাকে। ফলে item সাথে সাথে ফিরে আসে, নতুন করে build করতে হয় না।

```dart
class _ChatMessageState extends State<ChatMessage>
    with AutomaticKeepAliveClientMixin {

  @override
  bool get wantKeepAlive => true; // এই item-কে off-screen-এও alive রাখো

  @override
  Widget build(BuildContext context) {
    super.build(context); // বাধ্যতামূলক — keep-alive সংকেত পাঠায়
    return Card(child: CachedNetworkImage(imageUrl: widget.message.imageUrl));
  }
}
```

**ধাপ ৪ — Trade-off-টা ছবিতে দেখুন।**

```
Normal ListView:                With keep-alive:
on-screen  → built               on-screen  → built
off-screen → State DESTROYED     off-screen → State KEPT in memory
           (rebuilt on return)              (snaps back instantly)
```

Keep-alive **memory** দিয়ে **scroll-এর মসৃণতা** কেনে। শুধু সেখানেই ব্যবহার করুন, যেখানে state হারানো ব্যয়বহুল — প্রতিটা item-এ নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি memory আর rebuild খরচের মধ্যে trade-off বোঝেন কি না। সাথে widget reconciliation কীভাবে key ব্যবহার করে, সেটাও। Production-মানের list বানাতে দুটোই দরকার।

**সাধারণ ভুল:** keep-alive widget-এর `build`-এ `super.build(context)` call করতে ভুলে যাওয়া — এটা ছাড়া keep-alive সংকেত কখনো যায় না, আর item আগের মতোই ধ্বংস হয়। আর 10,000 item-এর list-এ প্রতিটা item-এ keep-alive ব্যবহার করা, যা lazy building-কে অর্থহীন করে দেয় এবং memory শেষ করে ফেলতে পারে। বেছে বেছে ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`ValueKey` vs `ObjectKey` vs `GlobalKey`?"* → `ValueKey` একটা মান (একটা id) দেখে মেলায়। `ObjectKey` object identity দেখে মেলায়। `GlobalKey` ভারী — এটা যেকোনো জায়গা থেকে widget-এর state-এ ঢোকার সুযোগ দেয়; কম ব্যবহার করুন।
- *"কখন key দরকার হয় না?"* → যে static list-এর item কখনো reorder হয় না, সেখানে position দিয়ে মেলানোই যথেষ্ট।

**সম্পর্কিত:** [Q11 — ListView-এর ধরন](#q11) · [Q12 — pagination](#q12)

[↑ উপরে ফিরুন](#toc)

---

# D. Painting, images, আর GPU

---

## <a id="q14"></a>14. `RepaintBoundary` কী, কখন এটা যোগ করবেন, আর কখন এটা ক্ষতি করে?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"ডিফল্টে একটা parent আর তার children একই layer-এ paint হয়। তাই এক অংশ repaint হলে পুরো layer repaint হয়। `RepaintBoundary` তার child-কে আলাদা layer-এ বসায়। তখন যে widget বারবার বদলায় সেটা একা repaint হয়, আর তার আশেপাশের static অংশ cache-এ থাকে। কিন্তু প্রতিটা boundary GPU memory খরচ করে। তাই সব জায়গায় বসালে উল্টো ক্ষতি হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Layer, সহজ ভাষায়।**
Flutter যখন paint করে, তখন widget-গুলোকে **layer**-এ ভাগ করে (স্বচ্ছ কাগজের পাতার মতো)। একটা পাতার কোনো widget বদলালে Flutter পুরো পাতাটাই আবার আঁকে। ডিফল্টে parent আর তার children একই পাতা ভাগ করে নেয়।

**ধাপ ২ — `RepaintBoundary` কী করে।**
এটা তার child-কে নিজস্ব একটা পাতা দেয়। ফলে:
- শুধু child বদলালে (একটা animation), শুধু child-এর পাতাটাই আবার আঁকা হয় — parent-এরটা যেমন ছিল তেমনই থাকে।
- শুধু parent বদলালে, child-এর পাতাটা cache থেকে আবার ব্যবহার হয়।

```
Without RepaintBoundary:          With RepaintBoundary:
one shared layer                  separate layers
 ┌──────────────────┐             ┌──────────────────┐
 │ animating widget │  any change │ animating widget │ ← own layer,
 │ static content   │  repaints   ├──────────────────┤   repaints alone
 └──────────────────┘  the whole  │ static content   │ ← cached
                       layer       └──────────────────┘
```

**ধাপ ৩ — কখন যোগ করবেন।**
যে widget বারবার repaint হয় কিন্তু তার পাশে static content থাকে, সেটাকে wrap করুন — একটা animation, চলমান ঘড়ি, video player, বা বারবার আপডেট হওয়া custom painter।

```dart
Column(
  children: [
    const StaticHeader(),     // কখনো বদলায় না
    RepaintBoundary(
      child: LiveTickerWidget(), // প্রতি সেকেন্ডে আপডেট — আলাদা করুন
    ),
    const StaticFooter(),     // কখনো বদলায় না
  ],
);
```

**ধাপ ৪ — কখন এটা ক্ষতি করে।**
প্রতিটা `RepaintBoundary` GPU memory-তে একটা offscreen buffer নেয়। আর compositor-কে সব layer জোড়া লাগাতে হয়। সব জায়গায় বসালে memory আর compositing খরচ দুটোই বাড়ে। পুরো screen এমনিতেই repaint হলে boundary শুধু overhead বাড়ায়, কোনো লাভ দেয় না।

**ধাপ ৫ — কীভাবে সিদ্ধান্ত নেবেন: repaint rainbow।**
DevTools-এ **"Show Repaint Rainbow"** চালু করুন ([Q2](#q2))। প্রতিটা layer repaint হলে নতুন রঙে ঝলকায়। প্রতি frame-এ যদি বড় একটা এলাকা একসাথে ঝলকাতে দেখেন, তাহলে `RepaintBoundary` সেটাকে ভাগ করতে পারে। এলাকাগুলো আগে থেকেই আলাদা আলাদা repaint হলে boundary যোগ করবেন না।

খেয়াল রাখুন: Flutter কিছু জায়গায় **নিজেই** `RepaintBoundary` বসিয়ে দেয় — প্রতিটা list item, প্রতিটা route, আর app root-এর চারপাশে। তাই ওগুলো আবার wrap করার দরকার নেই।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি compositing layer system বোঝেন কি না। আর অন্ধভাবে optimization না বসিয়ে *সূক্ষ্ম* সিদ্ধান্ত নিতে পারেন কি না।

**সাধারণ ভুল:** প্রতিটা widget-কে `RepaintBoundary`-তে wrap করা। এতে জিনিস আরও ধীর হতে পারে। কারণ প্রতিটা boundary GPU memory খায় আর জোড়া লাগানোর layer বাড়ায়। নিয়ম: আগে repaint rainbow দিয়ে মাপুন। তারপর শুধু সেখানেই boundary দিন যেখানে repaint এলাকা স্পষ্টভাবে ছোট হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা `const`-এর থেকে কীভাবে আলাদা?"* → `const` *build* ধাপ বাদ দেয় ([Q4](#q4))। `RepaintBoundary` *paint* ধাপ সীমিত করে। pipeline-এর আলাদা পর্যায়।
- *"`saveLayer` কী আর এটা ব্যয়বহুল কেন?"* → এটা একটা অস্থায়ী offscreen buffer-এ আঁকে (`Opacity`, clip, blur এটা ব্যবহার করে)। এটা ব্যয়বহুল। তাই পারলে সস্তা বিকল্প নিন (যেমন `Image`-এর নিজস্ব opacity, বা দরকার হলেই `AnimatedOpacity`)।

**সম্পর্কিত:** [Q1 — raster thread jank](#q1) · [Q15 — images](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. Flutter-এ image কীভাবে optimize করবেন — caching, resizing, WebP, আর `precacheImage`?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Image সাধারণত memory bloat আর jank-এর সবচেয়ে বড় উৎস। আমি চার দিক থেকে optimize করি: download করা image disk-এ cache করি, display size-এ decode করি (original size-এ নয়), file size কমাতে WebP দিই, আর যে image একটু পরেই দেখা যাবে সেটা precache করি। সবচেয়ে বড় প্রভাব ফেলে decode-এর সময় resize করা। কারণ বিশাল bitmap বিশাল memory খায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Image কেন বিপজ্জনক।**
একটা ছবির file size ছোট। কিন্তু memory-তে bitmap হিসেবে decode হওয়ার পরে সেটা হয় `width × height × 4 bytes`। একটা 4000×3000 ছবি memory-তে প্রায় **45MB**। এমনকি আপনি সেটা ছোট 200×150 thumbnail-এ দেখালেও। এমন কয়েকটা হলেই app-এর memory শেষ হয়, বা decode করার সময় jank হয়।

**ধাপ ২ — স্তম্ভ ১: caching।**
`cached_network_image` ব্যবহার করুন। এতে image একবার download হয়, তারপর disk থেকে পড়া হয়। সাথে বিনামূল্যে placeholder আর error widget-ও পাওয়া যায়।

```dart
CachedNetworkImage(
  imageUrl: 'https://example.com/photo.webp',
  placeholder: (context, url) => const CircularProgressIndicator(),
  errorWidget: (context, url, error) => const Icon(Icons.error),
);
```

**ধাপ ৩ — স্তম্ভ ২: decode-এর সময় resize (সবচেয়ে বড়টা)।**
Flutter-কে বলুন আপনি আসলে যে size-এ দেখাবেন সেই size-এ decode করতে। তাহলে বিশাল bitmap কখনো memory-তেই আসে না। `cacheWidth`/`cacheHeight` ব্যবহার করুন।

```dart
Image.network(
  'https://example.com/large_photo.jpg',
  cacheWidth: 400,   // 400 logical px চওড়ায় decode করবে
  cacheHeight: 300,
);

// cached_network_image-এ একই জিনিস:
CachedNetworkImage(
  imageUrl: '...',
  memCacheWidth: 400,
  memCacheHeight: 300,
);
```

**ধাপ ৪ — স্তম্ভ ৩: WebP format।**
একই quality-তে WebP file JPEG-এর চেয়ে প্রায় 25–35% ছোট। তাই download দ্রুত হয় আর disk cache-ও ছোট থাকে। Flutter WebP নিজে থেকেই support করে — শুধু backend বা CDN থেকে `.webp` দিন। ধীর mobile network-এর user-দের জন্য এটা সত্যিকারের লাভ (BD-তে খুব সাধারণ ব্যাপার)।

**ধাপ ৫ — স্তম্ভ ৪: precache।**
Image দেখানোর *আগেই* সেটা cache-এ load করে রাখুন। তাহলে widget build হওয়ার সাথে সাথেই সেটা দেখা যায় — পরের screen বা fold-এর নিচের image-এর জন্য দারুণ।

```dart
@override
void didChangeDependencies() {
  super.didChangeDependencies();
  precacheImage(const NetworkImage('https://example.com/hero.webp'), context);
}
```

**Interviewer কেন জিজ্ঞেস করে:** বাস্তব app-এ image optimization প্রায়ই সবচেয়ে বেশি প্রভাব ফেলা performance fix। তাঁরা দেখতে চান আপনি network efficiency (cache, WebP) আর memory efficiency (decode-এর সময় resize) — দুটোই বলছেন কি না, শুধু একটা নয়।

**সাধারণ ভুল:** `cacheWidth`/`cacheHeight`-এ physical pixel দেওয়া। এগুলো **logical** pixel নেয় — Flutter নিজেই device pixel ratio দিয়ে গুণ করে দেয়। আরেকটা ভুল: বিশাল image-এ `cacheWidth` ছাড়া `BoxFit.cover` ব্যবহার করা। এতে পুরো bitmap decode হয়ই, শুধু দেখতে clip হয়। পুরো memory-টাই নষ্ট হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Decode হওয়া image memory-তে কত বড়?"* → প্রায় width × height × 4 bytes। disk-এ file size যাই হোক।
- *"Asset image বনাম network?"* → `cacheWidth`/`cacheHeight` `Image.asset`-এও কাজ করে। Asset-এর জন্য resolution variant-ও দিন (1x/2x/3x folder)।

**সম্পর্কিত:** [Q1 — raster jank](#q1) · [Q14 — RepaintBoundary](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. Shader compilation jank কী, আর এটা কীভাবে ঠিক করবেন?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"কোনো animation বা effect প্রথমবার চলার সময় engine-কে মাঝে মাঝে তখনই তার shader (একটা ছোট GPU program) compile করতে হয়। এতে একবারের জন্য একটা আটকে যাওয়া ভাব হয়। User এটাকে animation-এর একদম প্রথম চালানোর jank হিসেবে দেখে। সমাধান হলো shader আগেভাগে warm up করা। আর নতুন Flutter-এ Impeller engine shader আগেই precompile করে বলে সমস্যাটা প্রায় থাকেই না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Shader কী।**
**Shader** হলো একটা ছোট program যা GPU-তে চলে আর একটা effect আঁকে — gradient, blur, page transition, বা জটিল animation। GPU shader ব্যবহার করার আগে সেটাকে device-এর machine code-এ compile করতে হয়।

**ধাপ ২ — এটা কেন jank তৈরি করে।**
পুরোনো Skia engine-এ shader প্রায়ই **প্রথমবার** দরকার হওয়ার সময় compile হতো — frame-এর মাঝখানেই। ওই compilation অনেক millisecond নিতে পারে, যা 16ms budget ভেঙে দেয়। তাই animation-এর প্রথম চালানোতে আটকে যায়। এরপর compile হওয়া shader cache-এ থাকে আর সব মসৃণ হয়। তাই চেনার লক্ষণ হলো: "এই screen প্রথমবার খুললে / এই animation প্রথমবার চললে jank হয়, তারপর ঠিক থাকে।"

**ধাপ ৩ — সমাধান ১: Impeller engine ব্যবহার করুন (আধুনিক উত্তর)।**
Flutter-এর নতুন rendering engine **Impeller** app build করার সময়েই shader precompile করে। ফলে runtime-এ compilation-এর আটকে যাওয়া থাকে না। iOS-এ Impeller ডিফল্ট, আর সাম্প্রতিক Flutter version-গুলোতে Android-এও ছড়িয়ে পড়ছে। "আমি আগে দেখব Impeller চালু আছে কি না" — এটাই হালনাগাদ senior উত্তর।

**ধাপ ৪ — সমাধান ২: shader warm up করুন (পুরোনো Skia পদ্ধতি)।**
Skia ব্যবহার করতেই হলে, আপনার মূল animation-গুলোতে ব্যবহৃত shader record করে bundle করতে পারেন। তখন সেগুলো animation-এর মাঝে নয়, startup-এ compile হবে:

```bash
# চালানোর সময় app কোন shader ব্যবহার করে তা record করুন:
flutter run --profile --cache-sksl --purge-persistent-cache
# প্রতিটা animation চালান, তারপর bundle save করুন:
# terminal-এ 'M' চাপলে একটা *.sksl.json file লেখা হয়

# তারপর এটা ship করুন যেন launch-এ shader warm হয়:
flutter build apk --bundle-sksl-path flutter_01.sksl.json
```

**ধাপ ৫ — এটা shader jank কি না কীভাবে নিশ্চিত হবেন।**
DevTools-এর Performance view-তে একটা ধীর প্রথম frame, যার সময় shader compilation-এ যাচ্ছে — এটাই লক্ষণ। সবচেয়ে শক্ত সূত্র হলো: এটা শুধু effect-এর *প্রথম* চালানোতেই হয়, আর কখনো হয় না।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা গভীর, senior-level বিষয়। এটা জানা (আর বিশেষ করে Impeller-ই আধুনিক সমাধান — এটা জানা) বোঝায় আপনি Flutter engine-এর খোঁজ রাখেন, শুধু widget layer নয়।

**সাধারণ ভুল:** প্রথমবারের shader jank (GPU/raster সমস্যা) আর ধীর `build()` (UI-thread সমস্যা) গুলিয়ে ফেলা। দেখতে এক লাগে, কিন্তু ধরার পদ্ধতি আলাদা — shader jank একবারই হয় আর raster thread-এ হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Skia বনাম Impeller — এক লাইনে?"* → Skia দরকার হলে তখন shader compile করত (প্রথম ব্যবহারে jank হতে পারত)। Impeller আগেই precompile করে, ওই আটকে যাওয়া সরিয়ে দেয়।
- *"SkSL warm-up কি এখনো লাগে?"* → দিন দিন কম লাগছে — Impeller সব জায়গায় ডিফল্ট হওয়ার সাথে সাথে ম্যানুয়াল SkSL warm-up বাদ পড়ছে।

**সম্পর্কিত:** [Q1 — raster jank](#q1) · [Q3 — measure in profile](#q3)

[↑ উপরে ফিরুন](#toc)

---

# E. ভারী কাজ আর startup

---

## <a id="q17"></a>17. Isolate আর `compute()` কী? কোন কাজ আলাদা isolate-এ চালানো উচিত?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart আমার সব code — `build()` আর event handler সহ — একটাই UI thread-এ চালায়। ওই thread-এ ভারী synchronous কাজ করলে screen জমে যায়। Isolate হলো আলাদা একটা worker, যার নিজস্ব memory আছে। Isolate-রা memory ভাগ করে না, তারা message পাঠায়। `compute()` হলো একটা শর্টকাট — এটা একটা function নতুন isolate-এ চালায় আর result ফেরত দেয়। ফলে ভারী কাজ UI-এর বাইরে থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা thread = রান্নাঘরে একজন রাঁধুনি।**
ডিফল্টে আপনার সব Dart একটা thread-এ চলে। ভাবুন একজন রাঁধুনি, যাকে order নিতে হয়, রান্না করতে হয়, আবার পরিবেশনও করতে হয়। একটা পদে যদি লম্বা, থামা ছাড়া পরিশ্রম লাগে (পাহাড়সমান পেঁয়াজ কাটা), তাহলে বাকি সব order অপেক্ষা করে — screen repaint পর্যন্ত হয় না। ওই লম্বা কাজটাই UI জমিয়ে দেয়।

**ধাপ ২ — গুরুত্বপূর্ণ: `async`/`await` কোনো background thread নয়।**
এখানে অনেকে হোঁচট খান। `await` কাজটাকে অন্য thread-এ সরায় না — এটা শুধু ওই একজন রাঁধুনিকে একটা কাজ থামিয়ে *অপেক্ষার* সময়ে অন্য কাজ করতে দেয় (যেমন oven-এর জন্য অপেক্ষা)। network call-এর মতো I/O-এর জন্য এটা দারুণ। কিন্তু `Future`-এর ভেতরে CPU-ভারী synchronous loop এখনো UI আটকে দেয়। কারণ সেটা কখনো থামে না।

```dart
// এটা এখনো UI জমিয়ে দেয় — এটা CPU-এর কাজ, অপেক্ষা নয়
Future<int> bad() async {
  var total = 0;
  for (var i = 0; i < 1000000000; i++) total += i; // await নেই = yield নেই
  return total;
}
```

**ধাপ ৩ — Isolate = আলাদা রান্নাঘর সহ দ্বিতীয় রাঁধুনি রাখা।**
Isolate হলো আলাদা একটা worker, যার **নিজস্ব memory** আছে। দুই রান্নাঘর কোনো উপকরণ ভাগ করে না — তারা চিরকুট (message) পাঠায়। কিছুই ভাগ হয় না বলে কোনো lock নেই, কোনো race condition নেই। খরচ: input আর result দুই isolate-এর মধ্যে **copy** হয়।

**ধাপ ৪ — এটা ব্যবহারের সহজ উপায়।**

```dart
import 'package:flutter/foundation.dart'; // compute()-এর জন্য

// Function-টা অবশ্যই top-level বা static হতে হবে — নতুন isolate parent-এর
// variable বা closure দেখতে পায় না।
List<Product> _parseProducts(String jsonString) {
  final decoded = jsonDecode(jsonString) as List<dynamic>;
  return decoded.map((e) => Product.fromJson(e)).toList();
}

// compute(): একটা function নতুন isolate-এ চালায়, result ফেরত দেয়
final products = await compute(_parseProducts, response.body);

// অথবা আধুনিক, আরও সহজ API (Dart 2.19+):
final products2 = await Isolate.run(() => _parseProducts(response.body));
```

**ধাপ ৫ — কোন কাজ isolate-এ যাবে, আর কোনটা যাবে না।**

| Isolate-এ সরান | UI isolate-এ রাখুন |
|---|---|
| বড় JSON parse করা (>~1MB) | ছোট JSON parsing |
| Image processing / resizing | Network request (এমনিতেই non-blocking) |
| Cryptography, hashing | `setState`, সাধারণ logic |
| ভারী গণিত, বড় sort | widget বা `BuildContext` ছোঁয় এমন যেকোনো কিছু |

মোটা দাগে নিয়ম: যে CPU-ভারী কাজে প্রায় 16ms-এর বেশি লাগবে, তার জন্য isolate ব্যবহার করুন। Network call-এর জন্য নয় (এমনিতেই async)। ছোট কাজের জন্যও নয় (copy-এর খরচ পোষায় না)।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান আপনি Dart-এর concurrency model বোঝেন কি না — async (এক thread, cooperative) আর isolate (সত্যিকারের parallelism)-এর পার্থক্য। আর কখন কোনটা সঠিক টুল।

**সাধারণ ভুল:** ভাবা যে `async`/`await` code-টা background-এ চালায়। চালায় না — `await` একই thread-এ yield করে। আরেকটা ভুল: `compute()`-এ closure বা instance method পাঠানো। এতে crash হয়, কারণ নতুন isolate parent-এর memory ছুঁতে পারে না। Function-টা top-level বা static হতেই হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Isolate-রা কীভাবে কথা বলে?"* → `SendPort` আর `ReceivePort` দিয়ে (message)। সহজ ক্ষেত্রে `compute`/`Isolate.run` এটা আড়াল করে রাখে।
- *"Isolate কি ধীর API call দ্রুত করবে?"* → না — ওটা I/O আর এমনিতেই non-blocking। Isolate শুধু CPU-ভারী কাজে সাহায্য করে।

**সম্পর্কিত:** [Q1 — UI-thread jank](#q1) · [Q6 — build() golden rule](#q6) · [Q18 — leaks](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. Controller আর subscription থেকে memory leak কেন হয়, আর এগুলো কীভাবে dispose করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Leak তখন হয় যখন widget চলে যাওয়ার পরেও কিছু একটা ওই widget-এর `State`-এর reference ধরে রাখে। ফলে garbage collector সেটা free করতে পারে না। সাধারণ দোষী তিনটা: cancel না করা `StreamSubscription`, dispose না করা `AnimationController`, আর dispose না করা `TextEditingController`/`ScrollController`। নিয়মটা সহজ: `initState`-এ আমি যা তৈরি করি, `dispose()`-এ তা পরিষ্কার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Leak কেন হয়।**
যে object-এর আর কোনো reference নেই, Dart সেটা free করে দেয় ([garbage collection])। Leak মানে — মরে যাওয়া widget-এর `State`-এর reference এখনো কেউ ধরে আছে। তাই GC সেটা collect করতে পারে না। `State` memory-তে থেকে যায়। আর তার callback-গুলো চলতেও থাকতে পারে।

**ধাপ ২ — তিনটা চিরাচরিত দোষী।**
- **`StreamSubscription`** — `stream.listen(...)` করলে stream আপনার callback ধরে রাখে। সেই callback সাধারণত `this` (মানে `State`) capture করে। Cancel না করলে widget চলে যাওয়ার পরেও `State` বেঁচে থাকে। তখন callback একটা মৃত `State`-এ `setState` call করতে পারে — সেই বিখ্যাত "setState() called after dispose()" crash।
- **`AnimationController`** — এর ticker সেকেন্ডে ~60 বার fire করে। `vsync: this` দিয়ে তৈরি করে dispose না করলে ticker চলতেই থাকে। এটা `State` ধরে রাখে আর CPU পোড়ায়।
- **`TextEditingController` / `ScrollController`** — এগুলো `ChangeNotifier`, এদের listener থাকে। আর text-এর ক্ষেত্রে একটা native input connection থাকে। Dispose না করলে ওগুলো লেগে থাকে।

**ধাপ ৩ — নিয়ম, আর ক্রম।**
`initState`-এ (বা `State`-এর constructor-এ) কিছু তৈরি করলে `dispose()`-এ সেটা dispose করুন। **আগে** subscription cancel করুন, তারপর controller dispose করুন, আর `super.dispose()` call করুন **সবার শেষে**।

```dart
class _ChatScreenState extends State<ChatScreen>
    with TickerProviderStateMixin {

  late final AnimationController _fade;
  late final TextEditingController _input;
  StreamSubscription<Message>? _sub;

  @override
  void initState() {
    super.initState();
    _fade = AnimationController(vsync: this, duration: const Duration(milliseconds: 300));
    _input = TextEditingController();
    _sub = chatService.messageStream.listen((msg) {
      if (mounted) {                 // guard: বেঁচে থাকলে তবেই setState
        setState(() {/* update */});
      }
    });
  }

  @override
  void dispose() {
    _sub?.cancel();   // 1. আগে callback থামান
    _fade.dispose();  // 2. তারপর controller dispose
    _input.dispose();
    super.dispose();  // 3. সবসময় সবার শেষে
  }

  @override
  Widget build(BuildContext context) => const Placeholder();
}
```

**ধাপ ৪ — Leak কীভাবে ধরবেন।**
DevTools-এর **Memory tab** ব্যবহার করুন ([Q2](#q2)): snapshot → screen খুলুন আর বন্ধ করুন → force GC → snapshot → diff। বন্ধ করা screen-এর object-গুলো এখনো থাকলে বুঝবেন কোথাও `dispose`/`cancel` ভুলে গেছেন।

**Interviewer কেন জিজ্ঞেস করে:** Memory leak production bug-এর সবচেয়ে বড় ধরনগুলোর একটা। তাঁরা দেখতে চান আপনি প্রতিটা resource নেওয়ার সাথে সাথেই তার cleanup জুড়ে দেন কি না। আর আপনি বোঝেন কি না — যার reference এখনো আছে, GC সেটা free করতে পারে না।

**সাধারণ ভুল:** cancel/dispose করার আগেই `super.dispose()` call করা — এটা সবার শেষে থাকতে হবে। আরেকটা ভুল হলো ধরে নেওয়া যে `dispose()` সবসময় চলে। এটা তখনই চলে যখন widget tree থেকে সরে যায়। লুকানো tab-এ বা কোনো route-এর পেছনে থাকা widget বেঁচে থাকতে পারে। তাই তার timer চলতেই থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`setState`-এর আগে `mounted` check করেন কেন?"* → কারণ widget dispose হওয়ার পরেও একটা async callback ফিরে আসতে পারে। মৃত `State`-এ `setState` করলে throw করে।
- *"অনেকগুলো subscription থাকলে কী করবেন?"* → সেগুলো একটা `List<StreamSubscription>`-এ রাখুন। আর `dispose()`-এ loop চালিয়ে সব cancel করুন।

**সম্পর্কিত:** [Q12 — scroll controller dispose করা](#q12) · [Q10 — debounce timer cancel করা](#q10) · [Q17 — isolate](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q19"></a>19. App-এর startup time কীভাবে measure করবেন আর কমাবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-05-performance.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি startup measure করি `flutter run --trace-startup` দিয়ে। এটা প্রথম frame পর্যন্ত সময় record করে। সাথে আমার নিজের একটা marker রাখি — আসল content কখন দেখা যায়। কমানোর জন্য `main()`-এ শুধু ততটুকুই `await` করি, যতটুকু প্রথম screen-এর সত্যিই দরকার। বাকি সব কাজ প্রথম frame-এর পরে সরিয়ে দিই। আর app size ছোট করি। মূল কথা: দ্রুত কিছু একটা দেখান, বাকি initialization background-এ শেষ করুন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Startup-এর timeline।**
Startup কয়েকটা পর্যায় ধরে চলে। এর সবগুলো আপনি control করতে পারবেন না:

```
Native boot  →  Engine init  →  Framework init  →  Your app code
(can't        (fewer           (your main() and the
 control)      plugins help)    first widgets)  ← optimize here
```

**ধাপ ২ — কীভাবে measure করবেন।**
- **Trace startup:** `flutter run --trace-startup --profile` একটা `start_up_info.json` লেখে। এতে milestone থাকে — যেমন framework init পর্যন্ত সময় আর প্রথম rasterized frame পর্যন্ত সময়।
- "First meaningful frame"-এর জন্য **আপনার নিজের marker** (যখন spinner নয়, আসল content দেখা যায়):

```dart
void main() {
  final sw = Stopwatch()..start();
  WidgetsFlutterBinding.ensureInitialized();
  WidgetsBinding.instance.addPostFrameCallback((_) {
    debugPrint('First frame in ${sw.elapsedMilliseconds}ms');
  });
  runApp(const MyApp());
}
```

**ধাপ ৩ — কমান: `main()`-কে block করবেন না।**
সবচেয়ে বড় লাভ আসে `runApp`-এর আগে প্রতিটা service await করা বন্ধ করলে। প্রথম frame-এর যা দরকার, শুধু সেটাই await করুন। বাকিটা প্রথম frame-এর পরে সরিয়ে দিন।

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();        // সত্যিই আগে দরকার

  runApp(const MyApp());

  WidgetsBinding.instance.addPostFrameCallback((_) async {
    await Analytics.init();              // প্রথম frame-এর জন্য দরকার নেই
    await RemoteConfig.fetch();
  });
}
```

**ধাপ ৪ — কমান: দ্রুত একটা shell দেখান, তারপর navigate করুন।**
সাথে সাথেই একটা হালকা screen (skeleton বা spinner) render করুন। User সেটার দিকে তাকিয়ে থাকার সময়েই ভারী init চালান। তারপর সেটা বদলে দিন।

```dart
class _AppShellState extends State<AppShell> {
  @override
  void initState() {
    super.initState();
    _init();
  }

  Future<void> _init() async {
    final user = await AuthService.getCurrentUser(); // ভারী কাজ, UI-এর পেছনে লুকানো
    if (mounted) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => user != null ? const HomePage() : const LoginPage()),
      );
    }
  }

  @override
  Widget build(BuildContext context) =>
      const Scaffold(body: Center(child: CircularProgressIndicator()));
}
```

**ধাপ ৫ — কমান: deferred loading আর ছোট build।**
- **Deferred import** একটা বড় ও কম ব্যবহৃত feature শুধু তখনই download করে, যখন সেটা খোলা হয়:
  ```dart
  import 'package:myapp/admin_panel.dart' deferred as admin;
  Future<void> open() async {
    await admin.loadLibrary(); // দরকার হলে তবেই load
    // ... navigate to admin.AdminPanel()
  }
  ```
- **ছোট release build** দ্রুত load হয়:
  ```bash
  flutter build apk --split-per-abi      # প্রতি CPU arch-এর জন্য একটা APK
  flutter build apk --tree-shake-icons   # অব্যবহৃত Material icon বাদ
  # আরও: --obfuscate --split-debug-info দিলে build ছোট ও নিরাপদ হয়
  ```

**Interviewer কেন জিজ্ঞেস করে:** Startup time সরাসরি retention-এ প্রভাব ফেলে — cold start-এর প্রতিটা বাড়তি সেকেন্ডে user হারায়। তাঁরা একটা নিয়মমাফিক loop দেখতে চান: measure করুন, আসল bottleneck ঠিক করুন, আবার measure করুন। অনুমান নয়।

**সাধারণ ভুল:** পরপর পাঁচটা service await করে `main()` block করে রাখা। ফলে user সাদা screen-এর দিকে তাকিয়ে থাকে। প্রথম frame-এর যা দরকার, শুধু সেটাই await করুন। বাকিটা পরে করুন। আরেকটা ভুল — debug mode-এ startup measure করা, যেটা release-এর চেয়ে কয়েক গুণ ধীর ([Q3](#q3))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Time to first frame আর first meaningful frame-এর পার্থক্য কী?"* → First frame = engine কিছু একটা এঁকেছে। First meaningful frame = আপনার আসল content দেখা যাচ্ছে।
- *"App size কীভাবে ছোট করবেন?"* → ABI অনুযায়ী split করুন, icon tree-shake করুন, বড় feature defer করুন, asset compress করুন, আর অব্যবহৃত package বাদ দিন।

**সম্পর্কিত:** [Q3 — debug vs release](#q3) · [Q17 — ভারী init-এর জন্য isolate](#q17) · [Q6 — build() golden rule](#q6)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের review)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার table, তারপর এক line-এর reminder।

## দ্রুত তুলনার table

**Frame budget**

| Refresh rate | প্রতি frame-এ সময় | বেশি হয়ে গেলে |
|---|---|---|
| 60fps | ~16ms | jank (frame বাদ পড়ে) |
| 120fps | ~8ms | jank (frame বাদ পড়ে) |

**UI thread vs raster thread**

| UI thread (Dart) | Raster thread (GPU) |
|---|---|
| build → layout → paint | layer-গুলো composite করে pixel বানায় |
| ধীর = ভারী build/`setState` | ধীর = `saveLayer`, বড় image, অনেক layer |
| সমাধান: const, state নিচে নামানো, isolate | সমাধান: RepaintBoundary, image resize |

**তিনটা build mode**

| debug | profile | release |
|---|---|---|
| JIT, ধীর, hot reload | AOT + tools, measure করার জন্য | AOT, সবচেয়ে দ্রুত, user-দের জন্য |
| এখানে কখনোই measure করবেন না | এখানে measure করুন | এটাই ship করুন |

**ListView constructor**

| Constructor | Build খরচ | কখন ব্যবহার করবেন |
|---|---|---|
| `ListView(children:)` | O(all) | ছোট, fixed তালিকা |
| `ListView.builder` | O(visible) | লম্বা/dynamic তালিকা |
| `ListView.separated` | O(visible) | divider দরকার হলে |
| `ListView.custom` | O(visible) | custom child control দরকার হলে |

**Rebuild ছেঁকে নেওয়া**

| Tool | Library | কখন rebuild হয় |
|---|---|---|
| `const` | core | object একদম একই হলে (skip হয়) |
| `Selector` | Provider | নির্বাচিত value বদলালে |
| `buildWhen` | Bloc | আপনার শর্ত true হলে |
| `ValueListenableBuilder` | core | `ValueNotifier`-এর value বদলালে |

**async vs isolate**

| `async`/`await` | isolate |
|---|---|
| একই thread, I/O-এর সময় অপেক্ষা করে | আলাদা thread, সত্যিকারের parallel |
| network/disk-এর জন্য ভালো | ভারী CPU কাজের জন্য ভালো |
| CPU-এর কাজ unblock করে না | input/result copy করা হয় |

## এক লাইনের মনে রাখার কথা

- **Jank** = একটা frame তার ~16ms budget মিস করেছে; DevTools দিয়ে profile mode-এ খুঁজুন, অনুমান করে নয়। ([Q1](#q1))
- **DevTools**: Performance (slow frames), Rebuild inspector (over-rebuilds), Memory (leaks)। Optimize করার আগে মাপুন। ([Q2](#q2))
- **কখনোই debug-এ মাপবেন না** — এটা 5–10x ধীর; আসল device-এ profile/release ব্যবহার করুন। ([Q3](#q3))
- **`const` widget** প্রতিবার একই object, তাই Flutter সেগুলো rebuild করা বাদ দেয়। ([Q4](#q4))
- **Extract করা widget** = তার নিজের Element (একটা skip করার মতো সীমানা); **helper method**-এর কোনো Element নেই। ([Q5](#q5))
- **`build()`** অবশ্যই pure, দ্রুত, side effect ছাড়া হতে হবে — এর ভেতরে কখনোই network call বা timer শুরু করবেন না। ([Q6](#q6))
- **`setState` পুরো subtree rebuild করে** — state-টা নিচে নামিয়ে সবচেয়ে ছোট widget-এ নিন, যার এটা দরকার। ([Q7](#q7))
- **`Selector`** শুধু select করা value বদলালে rebuild করে; **`Consumer`** যেকোনো পরিবর্তনে rebuild করে। ([Q8](#q8))
- **`buildWhen`** ঠিক করে কোন Bloc state পরিবর্তনে widget rebuild হবে; এর জন্য সঠিক value equality দরকার। ([Q9](#q9))
- **Debounce** = চুপ হওয়া পর্যন্ত অপেক্ষা করে একবার চালানো; **throttle** = একটা নির্দিষ্ট সর্বোচ্চ হারে চালানো। ([Q10](#q10))
- **`ListView.builder`** লম্বা list-এর জন্য (lazy); সাধারণ `ListView` শুধু ছোট fixed list-এর জন্য। ([Q11](#q11))
- **Pagination**: ScrollController + একটা loading guard + `ListView.builder`; "আর data নেই" অবস্থাটাও handle করুন। ([Q12](#q12))
- **Key** reorder-এর সময় item-কে সঠিক state-এর সাথে মেলায়; **keep-alive** screen-এর বাইরের state ধরে রাখে (memory খরচ হয়)। ([Q13](#q13))
- **`RepaintBoundary`** একটা repaint হওয়া widget-কে আলাদা layer-এ সরিয়ে দেয় — কম ব্যবহার করুন, repaint rainbow দেখে নিন। ([Q14](#q14))
- **Image**: cache করুন, display size-এ decode করুন (`cacheWidth`), WebP দিন, precache করুন। Resize করাই সবচেয়ে বড় লাভ। ([Q15](#q15))
- **Shader jank** = একবারের first-run আটকে যাওয়া; Impeller shader আগেই compile করে রাখে আর এটা প্রায় পুরোটাই দূর করে। ([Q16](#q16))
- **Isolate** ভারী CPU কাজের জন্য (আলাদা memory, message পাঠানো); `async`/`await` CPU-র কাজ unblock করে **না**। ([Q17](#q17))
- **Dispose**: subscription আর controller `dispose()`-এ বন্ধ করুন (আগে cancel, সবার শেষে `super.dispose()`) যাতে leak না হয়। ([Q18](#q18))
- **Startup**: প্রথম frame-এর যা দরকার শুধু সেটাই `await` করুন, বাকিটা পরে করুন, build ছোট করুন; `--trace-startup` দিয়ে মাপুন। ([Q19](#q19))

[↑ উপরে ফিরুন](#toc)

---

# Practice: interviewer কীভাবে আরও গভীরে যান

Interviewer সাধারণত একটা প্রশ্নে থামেন না। তাঁরা আপনার গভীরতা মাপতে খুঁড়তেই থাকেন। এই চেইনটা মুখে বলে practice করুন — ঠান্ডা মাথায়, ধাপে ধাপে:

1. *"আমার list খারাপভাবে scroll করছে। আপনি প্রথমে কী check করবেন?"* → Profile mode-এ চালিয়ে DevTools খুলুন; UI thread লাল না raster thread লাল? ([Q1](#q1), [Q3](#q3))
2. *"এটা UI thread। এখন কী?"* → Rebuild inspector ব্যবহার করুন; widget-গুলো কি আসল পরিবর্তনের চেয়ে অনেক বেশি rebuild হচ্ছে? ([Q2](#q2))
3. *"হ্যাঁ, ছোট একটা পরিবর্তনে পুরো list rebuild হচ্ছে।"* → `setState` নিচে নামান, `const` যোগ করুন, আর স্থির row-গুলো আলাদা widget-এ বের করুন। ([Q4](#q4), [Q5](#q5), [Q7](#q7))
4. *"তবুও সব item একসাথে build হচ্ছে।"* → `ListView(children:)` থেকে `ListView.builder`-এ যান, যাতে শুধু দৃশ্যমান item build হয়। ([Q11](#q11))
5. *"এখন image load হওয়ার সময় raster thread লাল।"* → `cacheWidth` দিয়ে display size-এ image decode করুন, cache করুন, আর WebP দিন। ([Q15](#q15))
6. *"একটা animation প্রথমবার চললে এখনও আটকে যায়।"* → এটা সম্ভবত shader compilation jank; Impeller চালু আছে কি না দেখুন। ([Q16](#q16))

এই চেইনটা ঠান্ডা মাথায় হেঁটে যেতে পারা — আগে মাপা, তারপর আসল bottleneck ঠিক করা — ঠিক এটাই আপনাকে **senior** শোনায়, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

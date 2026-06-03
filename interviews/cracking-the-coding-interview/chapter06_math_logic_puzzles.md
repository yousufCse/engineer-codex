# Chapter 6 — Math & Logic Puzzles (প্রশ্ন 6.1 – 6.10)

> **Cracking the Coding Interview — বাংলা গাইড**
> এই chapter-এ কোনো coding নেই — আছে **যুক্তির খেলা**। সঠিক উত্তর মুখস্থ নয়, সঠিক **চিন্তার পদ্ধতি** শিখতে হবে।

> 🏠 [মূল Index](README.md) · 📘 [Foundation](chapter00_foundation.md) · ⬅️ [আগের: Bit Manipulation](chapter05_bit_manipulation.md) · ➡️ [পরের: Object-Oriented Design](chapter07_object_oriented_design.md)

---

<a id="toc"></a>
## 📑 এই Chapter-এর সূচি

- [6.1 — The Heavy Pill](#q6-1)
- [6.2 — Basketball](#q6-2)
- [6.3 — Dominos](#q6-3)
- [6.4 — Ants on a Triangle](#q6-4)
- [6.5 — Jugs of Water](#q6-5)
- [6.6 — Blue-Eyed Island](#q6-6)
- [6.7 — The Apocalypse](#q6-7)
- [6.8 — The Egg Drop Problem](#q6-8)
- [6.9 — 100 Lockers](#q6-9)
- [6.10 — Poison](#q6-10)

---

## 📚 Background — Logic Puzzle-এ কীভাবে ভাবতে হয়

Interview-তে Math & Logic Puzzle দেওয়া হয় কারণ interviewer দেখতে চান আপনি চাপে পড়েও **পদ্ধতিগতভাবে (systematically)** ভাবতে পারেন কিনা। উত্তর না জানলেও চলে — কীভাবে ভাবছেন সেটাই দেখা হয়।

এই ধরনের puzzle-এ চারটা কৌশল সবচেয়ে বেশি কাজে লাগে:

### ১. Rule Out (বাদ দিয়ে দিয়ে এগোনো)
যা সম্ভব নয় সেটা বাদ দিন। বাকি থাকলেই উত্তর। Sherlock Holmes-এর পদ্ধতি: "অসম্ভব সব বাদ দিলে যেটা বাকি থাকে, সেটাই সত্য — যত অদ্ভুতই হোক।"

### ২. Base Case + Build (ছোট থেকে বড়ো)
ছোট সংখ্যা (n=1, n=2) দিয়ে শুরু করুন। Pattern খুঁজুন। তারপর প্রমাণ করুন এটা n থেকে n+1-এ কাজ করে। এই পদ্ধতি অনেক puzzle-এ magical।

### ৩. Work Backwards (পিছন থেকে ভাবুন)
শেষ অবস্থা থেকে শুরু করুন এবং পিছনের দিকে হাঁটুন। অনেক সময় forward চিন্তা করতে গেলে আটকে যান, কিন্তু backwards হলে পথ পরিষ্কার দেখা যায়।

### ৪. Be Algorithmic ("Algorithm-এর মতো করে ভাবুন")
Random অনুমান নয় — নিজেকে জিজ্ঞেস করুন: "আমি যদি computer হতাম, এটা solve করতে কোন নিয়ম follow করতাম?" সিস্টেমেটিক approach দেখালে interviewer impress হন, এমনকি যদি সব ধাপ ঠিক নাও হয়।

### ৫. সংখ্যা নিয়ে quick sanity check
গণনা করার সময় approximation করুন। সঠিক calculation-এর আগে "কি এটা reasonable?" — এই প্রশ্নটা করুন।

---
---

<a id="q6-1"></a>
# 6.1 — The Heavy Pill

> Type: **Logic Puzzle · Scale & Measurement** · Difficulty: **Easy**

> **বইয়ের ভাষায়:** You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one bottle has pills of 1.1 grams. Given a scale that provides an exact weight, how would you find the heavy bottle? You can only use the scale once.

## 🔹 সমস্যাটা সহজ বাংলায়

২০টা বোতলে pill আছে। ১৯টা বোতলের প্রতিটা pill-এর ওজন ১.০ গ্রাম, কিন্তু একটা বোতলের pill ১.১ গ্রাম (ভারী)। আপনার কাছে একটা **scale আছে যেটা exact ওজন দেখায়** — কিন্তু **মাত্র একবার** ব্যবহার করতে পারবেন। কোন বোতলে ভারী pill সেটা বের করুন।

## 🔹 মূল কৌশল / Insight

**Scale মাত্র একবার ব্যবহার করা যাবে** — তাই প্রতিটা বোতলকে একটা করে করে তুলে দেখার উপায় নেই। চাবি হলো: **প্রতিটা বোতল থেকে আলাদা সংখ্যায় pill নিন।** তাহলে মোট ওজনই বলে দেবে কোন বোতলটা ভারী।

## 🔹 ধাপে ধাপে যুক্তি

বোতলগুলোকে নম্বর দিন: ১ থেকে ২০।

বোতল নম্বর `i` থেকে ঠিক `i`টা pill নিন:

```
বোতল ১  → ১টা pill নিন
বোতল ২  → ২টা pill নিন
বোতল ৩  → ৩টা pill নিন
...
বোতল ২০ → ২০টা pill নিন
```

এখন সব pill একসাথে scale-এ রাখুন।

**যদি সব pill সাধারণ (১.০ গ্রাম) হতো**, তাহলে মোট ওজন হতো:
```
১ + ২ + ৩ + ... + ২০ = (২০ × ২১) / ২ = ২১০ গ্রাম
```

কিন্তু ধরুন বোতল নম্বর `k` ভারী। তাহলে সেই বোতল থেকে নেওয়া `k`টা pill প্রতিটা ০.১ গ্রাম বেশি — অতিরিক্ত ওজন হবে `k × ০.১` গ্রাম।

তাহলে:
```
actual weight = 210 + (k × 0.1)

extra = actual weight − 210

k = extra / 0.1 = extra × 10
```

**উদাহরণ:** scale দেখাল ২১১.৪ গ্রাম।
```
extra = 211.4 − 210 = 1.4
k = 1.4 / 0.1 = 14

উত্তর: বোতল নম্বর ১৪
```

## 🔹 উত্তর

বোতল `i` থেকে `i`টা pill নিন, সব একসাথে মাপুন। scale-এর দেখানো ওজন থেকে ২১০ বাদ দিয়ে ১০ দিয়ে গুণ করলেই ভারী বোতলের নম্বর পাওয়া যাবে।

## 🔹 যে নীতি শিখলাম

**"একটা পরিমাপে n-টা unknown আলাদা করো" — প্রতিটা জিনিসকে একটা unique সংখ্যায় encode করুন।** এই ধারণাটা অনেক measurement puzzle-এর ভিত্তি।

## 🔹 Follow-up

- **Scale যদি exact ওজন না দিয়ে শুধু "বাম ভারী / ডান ভারী / সমান" বলতো?** — তাহলে সমস্যা সম্পূর্ণ আলাদা (ternary search / balance scale problem)।
- **বোতলের সংখ্যা ১০০ হলে?** — একই পদ্ধতি। বোতল `i` থেকে `i`টা pill, base sum = `100×101/2 = 5050`।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-2"></a>
# 6.2 — Basketball

> Type: **Logic Puzzle · Probability** · Difficulty: **Medium**

> **বইয়ের ভাষায়:** You have a basketball hoop and someone says that you can play one of two games. Game 1: You get one shot to make the hoop. Game 2: You get three shots and you have to make two of three shots. If p is the probability of making a particular shot, for which values of p should you pick one game or the other?

## 🔹 সমস্যাটা সহজ বাংলায়

Basketball-এ একটা shot করার সম্ভাবনা `p`। দুটো game-এর মধ্যে একটা বেছে নিন:
- **Game 1:** ১টা shot, জিততে হলে সেটা লাগাতে হবে।
- **Game 2:** ৩টা shot, জিততে হলে কমপক্ষে ২টা লাগাতে হবে।

কোন `p`-র মান-এ কোন game বেছে নেবেন?

## 🔹 মূল কৌশল / Insight

প্রতিটা game-এর **জেতার সম্ভাবনা** গণনা করুন, তারপর তুলনা করুন। যেটায় জেতার সম্ভাবনা বেশি, সেটা বেছে নিন।

## 🔹 ধাপে ধাপে যুক্তি

**Game 1:**
```
P(win₁) = p
```

**Game 2:** ৩টা shot-এ কমপক্ষে ২টা লাগাতে হবে।

সম্ভাব্য জয়ের ঘটনাগুলো হলো:
- ঠিক ২টা: HHM, HMH, MHH (যেকোনো ২টা hit, ১টা miss)
- ঠিক ৩টা: HHH

```
P(exactly 2 hits) = C(3,2) × p² × (1-p)  =  3p²(1-p)
P(exactly 3 hits) = p³

P(win₂) = 3p²(1-p) + p³
         = 3p² − 3p³ + p³
         = 3p² − 2p³
```

এখন Game 1 vs Game 2 তুলনা — কখন `P(win₁) > P(win₂)`?

```
p > 3p² − 2p³

(উভয় দিক থেকে p বাদ দিয়ে, p > 0 ধরে)

1 > 3p − 2p²

2p² − 3p + 1 > 0

(2p − 1)(p − 1) > 0
```

এই inequality solve করলে:
```
(2p − 1)(p − 1) > 0

শর্ত পূরণ হয় যখন উভয় factor একই চিহ্নের:

Case A: 2p−1 > 0 AND p−1 > 0  →  p > 1/2 AND p > 1  →  p > 1 (অসম্ভব)
Case B: 2p−1 < 0 AND p−1 < 0  →  p < 1/2 AND p < 1  →  p < 1/2
```

**ফলাফল:**
```
p < 1/2  →  Game 1 বেছে নিন (এক shot ভালো)
p = 1/2  →  দুটো game সমান
p > 1/2  →  Game 2 বেছে নিন (তিন shot-এ ২ ভালো)
```

## 🔹 উত্তর

**Intuition দিয়েও বোঝা যায়:**
- যদি `p = 0.9` (আপনি দারুণ খেলোয়াড়) — Game 2 ভালো, কারণ ৩ chance পেলে ২টা লাগানো সহজ।
- যদি `p = 0.1` (আপনি খুব খারাপ) — Game 1 ভালো, কারণ ৩ chance-এ ২টা লাগানো প্রায় অসম্ভব; ১টা chance-এ ওই ০.১ সম্ভাবনাই ভালো।
- `p = 0.5`-এ সমান।

## 🔹 যে নীতি শিখলাম

**Probability comparison: দুটো option-এর exact probability বের করুন, তারপর inequality solve করুন।** Intuition দিয়ে শুরু করুন — তারপর গণিত দিয়ে confirm করুন।

## 🔹 Follow-up

- **`p`-র মান না দিয়ে শুধু "weak player"-এর জন্য কোনটা?" — Game 1।**
- **৪টা shot-এ কমপক্ষে ২টা Game 3 হলে?** — আবার probability তুলনা করুন (Binomial distribution)।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-3"></a>
# 6.3 — Dominos

> Type: **Logic Puzzle · Combinatorics / Proof** · Difficulty: **Medium**

> **বইয়ের ভাষায়:** There is an 8×8 chessboard in which two diagonally opposite corners have been cut off. You are given 31 dominoes, and a single domino can cover exactly two squares. Can you use the 31 dominoes to cover the entire board?

## 🔹 সমস্যাটা সহজ বাংলায়

একটা ৮×৮ দাবার বোর্ড আছে। দুটো **কোনাকুনি বিপরীত কোণের ঘর** কেটে বাদ দেওয়া হয়েছে — ৬৪ − ২ = ৬২টা ঘর বাকি। একটা domino ঠিক দুটো পাশাপাশি ঘর ঢাকে। ৩১টা domino দিয়ে কি পুরো বোর্ড ঢাকা সম্ভব?

## 🔹 ধাপে ধাপে যুক্তি

সরাসরি চেষ্টা করলে — মাথা ঘুরে যাবে। চাবি হলো: **দাবার বোর্ডের রং** চিন্তা করা।

দাবার বোর্ডে সাদা আর কালো ঘর পাল্টা পাল্টা থাকে:

```
  কালো  সাদা  কালো  সাদা  কালো  সাদা  কালো  সাদা
  সাদা  কালো  সাদা  কালো  সাদা  কালো  সাদা  কালো
  কালো  সাদা  কালো  সাদা  কালো  সাদা  কালো  সাদা
  ...
```

**মূল observation:** দাবার বোর্ডে যেকোনো domino সবসময় **একটা সাদা + একটা কালো ঘর** ঢাকে। কারণ domino পাশাপাশি দুটো ঘর ঢাকে, আর পাশাপাশি ঘরের রং সবসময় আলাদা।

এখন বাদ দেওয়া দুটো কোণার ঘরের রং দেখুন:

```
  [K]  S   K   S   K   S   K   S        [K] = বাদ দেওয়া কোণ (কালো)
   S   K   S   K   S   K   S   K
   K   S   K   S   K   S   K   S
   ...
   S   K   S   K   S   K   S  [K]       [K] = বাদ দেওয়া কোণ (কালো)
```

**কোনাকুনি বিপরীত কোণ দুটো সবসময় একই রঙের!** (দাবার বোর্ডে (১,১) এবং (৮,৮) — উভয়ই কালো অথবা উভয়ই সাদা।)

তাই বাদ দেওয়ার পর বোর্ডে থাকে:
```
কালো ঘর: 32 − 2 = 30টা
সাদা ঘর: 32টা
```

কিন্তু প্রতিটা domino ১টা কালো + ১টা সাদা ঢাকে। ৩১টা domino ঢাকবে:
```
৩১টা কালো + ৩১টা সাদা ঘর
```

কিন্তু বোর্ডে আছে ৩০টা কালো আর ৩২টা সাদা — **mismatch!**

## 🔹 উত্তর

**না, ৩১টা domino দিয়ে পুরো বোর্ড ঢাকা সম্ভব নয়।**

কারণ: বিপরীত কোণের ঘর দুটো একই রঙের। বাদ দেওয়ার পর সাদা ও কালো ঘরের সংখ্যা সমান থাকে না। কিন্তু domino সবসময় একটা সাদা + একটা কালো ঢাকে — তাই সংখ্যার পার্থক্য মেটানো অসম্ভব।

## 🔹 যে নীতি শিখলাম

**"Coloring argument" বা "Invariant proof":** যখন সরাসরি সমাধান খোঁজা কঠিন, তখন এমন একটা **invariant** (অপরিবর্তনীয় সম্পত্তি) খুঁজুন যেটা দেখিয়ে দেয় কাজটা কখনোই সম্ভব নয়। দাবার বোর্ডের রং এই puzzle-এর invariant।

## 🔹 Follow-up

- **যদি দুটো বিপরীত কোণ কালো-সাদা (আলাদা রং) হতো?** — তাহলে সমান সংখ্যা থাকত এবং ঢাকা সম্ভব হতো।
- **N×N বোর্ড সাধারণভাবে কখন domino দিয়ে ঢাকা যাবে?** — যদি N জোড় হয় এবং কাটা ঘর দুটোর রং আলাদা হয়।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-4"></a>
# 6.4 — Ants on a Triangle

> Type: **Logic Puzzle · Probability** · Difficulty: **Medium**

> **বইয়ের ভাষায়:** There are three ants on different vertices of a triangle. What is the probability of collision (i.e., two or more ants are on the same path) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed. Similarly, find the probability of collision with n ants on an n-vertex polygon.

## 🔹 সমস্যাটা সহজ বাংলায়

একটা triangle-এর তিনটা কোণে তিনটা পিঁপড়া আছে। প্রতিটা পিঁপড়া randomly clockwise বা counterclockwise — দুই দিকের যেকোনো একটায় হাঁটতে শুরু করে (প্রতিটা direction-এর সম্ভাবনা ১/২)। সবাই একই speed-এ হাঁটে।

**collision** হবে যদি দুই বা তার বেশি পিঁপড়া **একই edge-এ বিপরীত দিক থেকে** আসে।

**Collision-এর সম্ভাবনা কত?**

## 🔹 মূল কৌশল / Insight

Collision হওয়ার চেয়ে **না হওয়ার** সম্ভাবনা হিসাব করা সহজ।

Collision হবে **না** শুধুমাত্র যদি:
- সবাই **clockwise** যায়, অথবা
- সবাই **counterclockwise** যায়।

## 🔹 ধাপে ধাপে যুক্তি

প্রতিটা পিঁপড়ার দুটো choice আছে (CW বা CCW)। তিনটা পিঁপড়া মিলিয়ে মোট:
```
২ × ২ × ২ = ৮ রকম সম্ভাব্য outcome
```

No collision-এর ক্ষেত্র:
```
১. সবাই CW:  CW, CW, CW   → ১টা outcome
২. সবাই CCW: CCW, CCW, CCW → ১টা outcome
মোট: ২টা no-collision outcome
```

```
P(no collision) = 2/8 = 1/4

P(collision) = 1 − 1/4 = 3/4
```

**N-vertex polygon-এর জন্য:**

N টা পিঁপড়া থাকলে মোট outcome = `2ᴺ`।
No collision = ২ (সবাই CW বা সবাই CCW)।

```
P(no collision) = 2 / 2ᴺ = 1 / 2^(N-1)

P(collision) = 1 − 1 / 2^(N-1)
```

Triangle (N=3) check:
```
P(collision) = 1 − 1/2² = 1 − 1/4 = 3/4  ✅
```

## 🔹 উত্তর

```
Triangle (N=3) : P(collision) = 3/4 = 75%
N-vertex polygon: P(collision) = 1 − 1/2^(N-1)
```

## 🔹 যে নীতি শিখলাম

**"Complement counting" — সরাসরি গোনা কঠিন হলে বিপরীতটা গুনুন।** P(A) = 1 − P(not A)। এই trick probability-র অসংখ্য puzzle-এ কাজে লাগে।

## 🔹 Follow-up

- **Square (N=4)-এ collision-এর সম্ভাবনা?** → `1 − 1/2³ = 7/8`।
- **N → ∞ হলে?** → P(collision) → 1 (প্রায় নিশ্চিত collision)।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-5"></a>
# 6.5 — Jugs of Water

> Type: **Logic Puzzle · State Space / BFS** · Difficulty: **Medium**

> **বইয়ের ভাষায়:** You have a five-quart jug, a three-quart jug, and an unlimited supply of water (but no measuring cups). How would you come up with exactly four quarts of water? Note that the jugs are oddly shaped, such that filling up exactly "half" of the jug would be impossible.

## 🔹 সমস্যাটা সহজ বাংলায়

আপনার কাছে:
- **৫ লিটারের একটা জগ** (JUG A)
- **৩ লিটারের একটা জগ** (JUG B)
- পানির অসীম supply

**মাপার কোনো cup নেই।** জগ দুটো অদ্ভুত আকারের — তাই "অর্ধেক ভরা" অনুমান করা যাবে না। শুধু সম্পূর্ণ ভরা বা সম্পূর্ণ খালি করা যাবে।

লক্ষ্য: **ঠিক ৪ লিটার পানি পরিমাপ করুন।**

## 🔹 ধাপে ধাপে যুক্তি

State = (JUG A-তে কত, JUG B-তে কত)। শুরু: (0, 0)।

প্রতি ধাপে যা করা যায়:
- যেকোনো জগ সম্পূর্ণ ভরা
- যেকোনো জগ সম্পূর্ণ খালি
- একটা জগ থেকে আরেকটায় ঢালা (যতক্ষণ না এক জগ ভরে বা খালি হয়)

**পদ্ধতি ১:**

```
ধাপ  | JUG A (5L) | JUG B (3L) | কী করলাম
-----|------------|------------|------------------
  ০  |     0      |     0      | শুরু
  ১  |     5      |     0      | A পূর্ণ ভরলাম
  ২  |     2      |     3      | A থেকে B-তে ঢাললাম (B ভরে গেল)
  ৩  |     2      |     0      | B খালি করলাম
  ৪  |     0      |     2      | A থেকে B-তে ঢাললাম (A খালি হলো, B-তে ২)
  ৫  |     5      |     2      | A পূর্ণ ভরলাম
  ৬  |     4      |     3      | A থেকে B-তে ঢাললাম (B ভরে গেল, A-তে ৪ বাকি)
```

**ধাপ ৬-এ JUG A-তে ঠিক ৪ লিটার!**

**পদ্ধতি ২ (বিকল্প — কম ধাপে):**

```
ধাপ  | JUG A (5L) | JUG B (3L) | কী করলাম
-----|------------|------------|------------------
  ০  |     0      |     0      | শুরু
  ১  |     0      |     3      | B পূর্ণ ভরলাম
  ২  |     3      |     0      | B থেকে A-তে ঢাললাম
  ৩  |     3      |     3      | B আবার ভরলাম
  ৪  |     5      |     1      | B থেকে A-তে ঢাললাম (A ভরে গেল, B-তে ১ বাকি)
  ৫  |     0      |     1      | A খালি করলাম
  ৬  |     1      |     0      | B থেকে A-তে ঢাললাম
  ৭  |     1      |     3      | B পূর্ণ ভরলাম
  ৮  |     4      |     0      | B থেকে A-তে ঢাললাম (A-তে ১+৩=৪!)
```

**ধাপ ৮-এ JUG A-তে ঠিক ৪ লিটার!**

## 🔹 উত্তর

পদ্ধতি ১ ব্যবহার করুন (৬ ধাপে): A ভরো → B-তে ঢালো → B খালি করো → A থেকে B-তে বাকি ঢালো → A ভরো → B ভরিয়ে দাও → A-তে ৪ লিটার থাকে।

## 🔹 যে নীতি শিখলাম

**"State space search"** — এই ধরনের puzzle আসলে একটা graph problem। প্রতিটা state (জগে কত পানি) একটা node, প্রতিটা action একটা edge। BFS দিয়ে সব সম্ভাব্য state explore করলে যেকোনো Water Jug problem solve করা যায়। **GCD rule:** `d` লিটার পরিমাপ করা সম্ভব যদি `d`, জগ দুটোর সংখ্যার GCD-এর গুণিতক হয়। এখানে GCD(5,3) = 1, তাই ১ থেকে ৫ লিটার পর্যন্ত যেকোনো পরিমাণ পরিমাপ করা সম্ভব।

## 🔹 Follow-up

- **৪ লিটার জগ আর ৬ লিটার জগ দিয়ে ৩ লিটার পরিমাপ করা কি সম্ভব?** → GCD(4,6) = 2; ৩ হলো 2-এর গুণিতক নয় → **সম্ভব নয়।**

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-6"></a>
# 6.6 — Blue-Eyed Island

> Type: **Logic Puzzle · Induction / Common Knowledge** · Difficulty: **Hard**

> **বইয়ের ভাষায়:** A bunch of people are living on an island, when a visitor comes and makes an announcement that everyone can hear: "I can see someone with blue eyes." It is known that there are 100 people with blue eyes on the island, 100 people with brown eyes, and the Guru (the visitor), who has green eyes. People can see each other's eye color, but cannot see their own. If they ever figure out their own eye color, they must leave on the midnight ferry that night. Before the Guru's announcement, no one ever left the island. How many people leave, and on which night?

## 🔹 সমস্যাটা সহজ বাংলায়

একটা দ্বীপে ১০০ জন blue eyes, ১০০ জন brown eyes মানুষ আছে (আর একজন green-eyed Guru)। নিয়ম:
- প্রত্যেকে অন্যের চোখের রং দেখতে পায়, **কিন্তু নিজের রং দেখতে পায় না।**
- কেউ নিজের চোখের রং বের করতে পারলে, সেই রাতেই (midnight ferry-তে) দ্বীপ ছেড়ে যাবে।
- দ্বীপে কেউ কারো চোখের রং সরাসরি বলে না।

একদিন Guru ঘোষণা দিলেন: **"আমি অন্তত একজন blue-eyed মানুষ দেখতে পাচ্ছি।"**

প্রশ্ন: কতজন কোন রাতে দ্বীপ ছাড়বে?

## 🔹 মূল কৌশল / Insight

এটা **induction (Base case + Build)** এবং **common knowledge** দিয়ে সমাধান হয়।

## 🔹 ধাপে ধাপে যুক্তি

**Base case — ধরুন মাত্র ১ জন blue-eyed মানুষ (n=1):**

সে নিজে দেখছে — আর কোনো blue-eyed নেই। Guru বললেন "আমি blue eyes দেখছি।" সে বুঝল — সেটা নিজেই! তাই **রাত ১-এ** সে চলে গেল।

**n=2 (দুজন blue-eyed, A এবং B):**

- A দেখছে B-এর blue eyes, B দেখছে A-এর blue eyes।
- A ভাবছে: "যদি আমার blue না হয়, তাহলে B মাত্র ১জন blue দেখছে → রাত ১-এ B চলে যাবে।"
- কিন্তু রাত ১ আসে, B চলে যায় না (কারণ B-ও একই চিন্তা করছে A নিয়ে)।
- রাত ১-এ কেউ না গেলে — A বুঝে গেল, B-ও নিজেকে blue দেখছে, তাই আমাকেও blue দেখছে → আমারও blue eyes।
- **রাত ২-এ** A এবং B দুজনেই চলে গেল।

**n জনের জন্য:**

একইভাবে induction করলে:

> **সব n জন blue-eyed মানুষ রাত n-এ দ্বীপ ছেড়ে যাবে।**

## 🔹 উত্তর

**১০০ জন blue-eyed মানুষ ঠিক ১০০তম রাতে একসাথে দ্বীপ ছেড়ে যাবে।**

Brown-eyed মানুষ কেউ যাবে না (Guru "blue eyes দেখছি" বলেছেন, brown eyes নিয়ে কোনো নতুন তথ্য নেই)।

## 🔹 সবচেয়ে কঠিন প্রশ্ন — Guru আগে কি জানত না?

হ্যাঁ! Guru-র announcement-এর আগে সবাই জানত যে blue-eyed মানুষ আছে। তাহলে নতুন কী হলো?

Guru যা দিলেন সেটা হলো **"common knowledge"** — এমন তথ্য যেটা সবাই জানে, **এবং সবাই জানে যে সবাই জানে, এবং সবাই জানে যে সবাই জানে যে সবাই জানে...** (infinite chain)।

এই common knowledge-ই induction-এর base case শুরু করতে পারে। এটাই পার্থক্য।

## 🔹 যে নীতি শিখলাম

**Mathematical Induction as a puzzle tool:** base case সত্য, inductive step সত্য → সব n-এর জন্য সত্য। "Common knowledge" — epistemic logic-এর একটা গুরুত্বপূর্ণ ধারণা।

## 🔹 Follow-up

- **Guru যদি "আমি অন্তত ২ জন blue-eyed দেখছি" বলতেন?** — তাহলে n=1 আর n=2 রাত ১ ও রাত ২-এ যেত না; ১০০ জন ৯৮তম রাতে যেত।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-7"></a>
# 6.7 — The Apocalypse

> Type: **Logic Puzzle · Probability / Expected Value** · Difficulty: **Medium**

> **বইয়ের ভাষায়:** In the new post-apocalyptic world, the world leader has decreed that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy — that is, they have children until they have one girl and then they stop — what will the gender ratio of the new generation be?

## 🔹 সমস্যাটা সহজ বাংলায়

এক দেশে নিয়ম: প্রতিটা পরিবার **একটি মেয়ে সন্তান হওয়া পর্যন্ত** বাচ্চা নেবে, তারপর থামবে।

যেমন: মেয়ে হলেই থামো। ছেলে হলে আরেকটা নাও। আবার ছেলে হলে আবার নাও। মেয়ে হলে থামো।

পরিবারগুলো হতে পারে:
- G (মেয়ে, থামো)
- BG (ছেলে, মেয়ে, থামো)
- BBG (ছেলে, ছেলে, মেয়ে, থামো)
- ...

**প্রশ্ন: ছেলে ও মেয়ের অনুপাত কী হবে?**

## 🔹 মূল কৌশল / Insight

অনেকে ভাবেন: "বেশি বেশি ছেলে হলে থামবে না, মানে মেয়ের সংখ্যা বাড়বে।" কিন্তু এটা ভুল। **গাণিতিকভাবে** দেখা যাক।

## 🔹 ধাপে ধাপে যুক্তি

ধরুন `N` টা পরিবার। প্রতিটা পরিবার ঠিক **১টা মেয়ে** পাবে (rule অনুযায়ী)।

তাহলে মোট মেয়ে = N।

মোট ছেলে কত? প্রতিটা পরিবারে শূন্য বা তার বেশি ছেলে হতে পারে।

**Expected value দিয়ে:**

একটা পরিবারে ছেলেদের সংখ্যার expected value:

```
P(০ ছেলে) = 1/2     (প্রথমেই মেয়ে, ০ ছেলে)
P(১ ছেলে) = 1/4     (B, G)
P(২ ছেলে) = 1/8     (B, B, G)
P(k ছেলে) = (1/2)^(k+1)

E(ছেলে) = Σ k × (1/2)^(k+1) , k=0 থেকে ∞

এই series = 1  (Geometric series-এর derivative ব্যবহার করে)
```

**তাই প্রতিটা পরিবারে গড়ে ১টা ছেলে এবং ১টা মেয়ে।**

**ভিন্নভাবে বোঝার উপায়:**

প্রতিটা জন্ম independent event। প্রতিটা বাচ্চার জন্য ছেলে/মেয়ে সম্ভাবনা সমান (১/২)। পরিবারের policy এই probability পরিবর্তন করে না। মোট জন্ম ধরলে, half হবে ছেলে, half মেয়ে।

এটা আরও সহজে দেখা যায়: কল্পনা করুন প্রতিটা "জন্ম" একটা coin flip। তাহলে সব coin flip মিলিয়ে half heads, half tails। কোন pattern-এ flip করা থামাচ্ছেন সেটা overall ratio পরিবর্তন করে না।

## 🔹 উত্তর

**ছেলে ও মেয়ের অনুপাত ১:১ থাকবে।** অর্থাৎ এই policy gender ratio পরিবর্তন করে না।

(Intuition: policy ছেলেদের বেশি বা কম হওয়ার probability পরিবর্তন করতে পারে না — প্রতিটা সন্তানের জন্মের সময় probability সমানই থাকে।)

## 🔹 যে নীতি শিখলাম

**"Stopping rule-এর পক্ষপাত নেই"** — কোনো sampling strategy (কখন থামবেন) random independent events-এর overall distribution পরিবর্তন করতে পারে না। এটা Probability তত্ত্বের একটা গুরুত্বপূর্ণ ধারণা যেটা অনেক real-world mistake-এর উৎস।

## 🔹 Follow-up

- **"সব পরিবার girl-first policy মানলে জনসংখ্যা বাড়বে?"** — না, গড়ে প্রতিটা পরিবারের সন্তান সংখ্যা ২ (১ ছেলে + ১ মেয়ে), যেটা আগের মতোই।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-8"></a>
# 6.8 — The Egg Drop Problem

> Type: **Logic Puzzle · Dynamic Programming / Math** · Difficulty: **Hard**

> **বইয়ের ভাষায়:** There is a building of 100 floors. If an egg drops from the Nth floor or above, it will break. If it's dropped from any floor below N, it will not break. You're given two eggs. Find N, while minimizing the number of drops for the worst case.

## 🔹 সমস্যাটা সহজ বাংলায়

একটা ১০০ তলা বিল্ডিং আছে। একটা **critical floor N** আছে:
- N বা তার উপর থেকে ফেললে ডিম ভাঙবে।
- N-এর নিচে থেকে ফেললে ভাঙবে না।

আপনার কাছে **ঠিক ২টা ডিম**। N বের করুন — **worst case-এ কমপক্ষে কত drop লাগবে?**

## 🔹 মূল কৌশল / Insight

দুটো চরম approach:
- **একটা একটা করে** (১ থেকে ১০০) → worst case ১০০ drops।
- **Binary search** → প্রথম ডিম ভাঙলে ২য় ডিম দিয়ে linear scan → worst case ~৫০+এর বেশি।

**চাবি:** দুটো ডিমের ক্ষেত্রে সঠিক strategy হলো **ব্যবধান কমিয়ে আনা** — প্রতিটা drop-এর পর interval ছোট করুন।

## 🔹 ধাপে ধাপে যুক্তি

ধরুন প্রথম ডিম দিয়ে **ব্যবধান x** করে drop করব:
```
x তম floor, 2x তম, 3x তম, ... floor
```

কিন্তু সমস্যা: প্রতিবার প্রথম ডিম drop করলে, দ্বিতীয় ডিম দিয়ে linear scan বাড়তে থাকে।

**Optimal idea:** প্রতিবার প্রথম ডিম drop করার পর, interval **১ করে কমাই।**

যদি প্রথম drop `k` তলায়:
```
Drop ১: k তম floor
  → ভাঙলে: ২য় ডিম দিয়ে ১ থেকে k-1 → সর্বোচ্চ k-1 drop
Drop ২: k + (k-1) তম floor
  → ভাঙলে: ২য় ডিম দিয়ে k+1 থেকে k+(k-1)-1 → সর্বোচ্চ k-2 drop
...
```

Worst case সর্বদা = k drops।

ব্যবধানের সমষ্টি ≥ ১০০ হতে হবে:
```
k + (k-1) + (k-2) + ... + 1 ≥ 100

k(k+1)/2 ≥ 100

k² + k − 200 ≥ 0

k ≥ 13.65...  →  k = 14
```

**যাচাই:** 14 + 13 + 12 + 11 + 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 105 ≥ 100 ✅

```
Strategy (k=14):
  Drop ১: floor 14   (ভাঙলে: 1-13 linear scan → সর্বোচ্চ 13 + 1 = 14 drops)
  Drop ২: floor 27   (ভাঙলে: 15-26 linear scan → সর্বোচ্চ 12 + 2 = 14 drops)
  Drop ৩: floor 39   (ভাঙলে: 28-38 linear scan → সর্বোচ্চ 11 + 3 = 14 drops)
  ...
```

Worst case সবসময় **১৪ drops**!

```python
# Python — verification / generalization
import math

def min_drops(floors: int, eggs: int = 2) -> int:
    """Minimum drops needed in worst case (2 eggs, n floors)"""
    # k(k+1)/2 >= floors
    k = math.ceil((-1 + math.sqrt(1 + 8 * floors)) / 2)
    return k

print(min_drops(100))   # → 14
print(min_drops(1000))  # → 45
```

## 🔹 উত্তর

**১৪ drops** (worst case)।

Strategy: প্রথম ডিম floor 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100 এ drop করুন (interval প্রতিবার ১ কমছে)। প্রথম ডিম ভাঙলে, দ্বিতীয় ডিম দিয়ে আগের floor থেকে linear scan।

## 🔹 যে নীতি শিখলাম

**"Load balancing" — worst case সব পথে সমান করুন।** প্রতিটা possible failure point-এ total drops ধ্রুবক রাখতে interval ক্রমশ কমান। এটা Dynamic Programming-এর "egg drop" DP problem-এর বিশেষ ক্ষেত্র (2 eggs)।

## 🔹 Follow-up

- **৩টা ডিম, ১০০০ floor?** → DP দিয়ে solve করুন। `dp[e][f]` = e ডিম ও f floor-এ worst case minimum drops।
- **n ডিম, m floor?** → Binary search on dp table।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-9"></a>
# 6.9 — 100 Lockers

> Type: **Logic Puzzle · Number Theory / Pattern** · Difficulty: **Medium**

> **বইয়ের ভাষায়:** There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers. Next, he closes every 2nd locker. Then, on his third pass, he toggles every 3rd locker (closes it if it is open or opens it if it is closed). This process continues for 100 passes, such that on pass i, the man toggles every ith locker. After his 100th pass in the hallway, which lockers are open?

## 🔹 সমস্যাটা সহজ বাংলায়

১০০টা locker আছে, সব বন্ধ। একজন মানুষ ১০০ বার হলওয়েতে হাঁটে:
- **Pass 1:** সব locker খোলে (১, ২, ৩, ..., ১০০)
- **Pass 2:** প্রতিটা ২য় locker toggle করে (২, ৪, ৬, ...)
- **Pass 3:** প্রতিটা ৩য় locker toggle করে (৩, ৬, ৯, ...)
- ...
- **Pass k:** প্রতিটা k-তম locker toggle করে

১০০ pass শেষে কোন locker গুলো **খোলা** থাকবে?

## 🔹 মূল কৌশল / Insight

কোনো locker কতবার toggle হবে? **যতবার তার নম্বর-এর divisor আছে।**

```
Locker 12 → divisors: 1, 2, 3, 4, 6, 12 → ৬ বার toggle
  শুরু: বন্ধ → ১ বার → খোলা → ২ বার → বন্ধ → ... → ৬ বার → বন্ধ
```

**কখন locker খোলা থাকবে?** শুরুতে বন্ধ ছিল। বিজোড় সংখ্যকবার toggle হলে খোলা থাকবে।

তাহলে প্রশ্ন: **কোন সংখ্যার divisor-এর সংখ্যা বিজোড়?**

সাধারণত divisor জোড়ায় আসে: যদি `a` divisor হয়, তাহলে `n/a`-ও divisor। তারা আলাদা, তাই সংখ্যা জোড়।

**ব্যতিক্রম:** যখন `a = n/a`, অর্থাৎ `a² = n` → **n হলো perfect square!**

Perfect square-এ একটা divisor নিজেই জোড়া বানায় নিজের সাথে — তাই মোট divisor সংখ্যা বিজোড়।

```
উদাহরণ:
n = 9  → divisors: 1, 3, 9 → ৩টা (বিজোড়) → locker 9 খোলা থাকবে
n = 16 → divisors: 1, 2, 4, 8, 16 → ৫টা (বিজোড়) → locker 16 খোলা থাকবে
n = 12 → divisors: 1,2,3,4,6,12 → ৬টা (জোড়) → locker 12 বন্ধ থাকবে
```

১ থেকে ১০০ পর্যন্ত perfect square:
```
1, 4, 9, 16, 25, 36, 49, 64, 81, 100
(1², 2², 3², 4², 5², 6², 7², 8², 9², 10²)
```

```python
# Python — verification
open_lockers = [i*i for i in range(1, 11) if i*i <= 100]
print(open_lockers)
# → [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Cross-check by simulation
lockers = [False] * 101   # index 1-100 ব্যবহার করব
for pass_num in range(1, 101):
    for locker in range(pass_num, 101, pass_num):
        lockers[locker] = not lockers[locker]

result = [i for i in range(1, 101) if lockers[i]]
print(result)
# → [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  ✅
```

## 🔹 উত্তর

**১০টা locker খোলা থাকবে: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100** — অর্থাৎ ১ থেকে ১০০ পর্যন্ত সব **perfect square**।

## 🔹 যে নীতি শিখলাম

**"Pattern recognition through small examples":** ছোট সংখ্যা দিয়ে (locker 1-10) pattern দেখুন → সাধারণ নিয়ম বের করুন। Divisor-এর বিজোড়/জোড় সংখ্যা → perfect square — এই সংযোগ Number Theory-র একটা সুন্দর result।

## 🔹 Follow-up

- **১০০০টা locker?** → ১ থেকে ১০০০ পর্যন্ত perfect square: `floor(√1000) = 31`টা locker খোলা।
- **প্রতিটা locker শুরুতে খোলা থাকলে?** → বিজোড় divisor → বন্ধ। Perfect square গুলো বন্ধ, বাকি সব খোলা।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

<a id="q6-10"></a>
# 6.10 — Poison

> Type: **Logic Puzzle · Binary Encoding / Information Theory** · Difficulty: **Hard**

> **বইয়ের ভাষায়:** You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which can be used to detect poison. A single strip can be dipped in as many bottles as you'd like, and it will turn positive if it ever touches a poisoned bottle. You can run as many tests as you want, but you only get the results after one week, and you only have one week to find the answer. Figure out the poisoned bottle.

## 🔹 সমস্যাটা সহজ বাংলায়

১০০০টা বোতল, একটাতে বিষ আছে। আপনার কাছে **১০টা test strip**।

- একটা strip অনেক বোতলে ডোবানো যাবে।
- কোনো বোতলে বিষ থাকলে সেই strip **positive** হবে।
- পরীক্ষার ফলাফল **এক সপ্তাহ পরে** পাওয়া যাবে।
- আপনার হাতে **এক সপ্তাহ** — তাই **একটাই পরীক্ষার round** করতে পারবেন।

কীভাবে বিষাক্ত বোতল বের করবেন?

## 🔹 মূল কৌশল / Insight

**Binary encoding!** ১০টা strip মানে ১০টা bit। ১০ bit-এ কতগুলো সংখ্যা express করা যায়?

```
2¹⁰ = 1024 > 1000  ✅
```

১০০০টা বোতলকে 1 থেকে 1000 নম্বর দিন। প্রতিটা নম্বরকে **10-bit binary**-তে লিখুন।

Strip number `i` (1 থেকে 10)-এ সেই বোতলগুলো ডোবান যাদের binary representation-এর `i`-তম bit **1**।

## 🔹 ধাপে ধাপে যুক্তি

বোতল নম্বরকে binary-তে রূপান্তর:

```
বোতল   বাইনারি (10 bit)
------  ------------------
  1   = 0000000001
  2   = 0000000010
  3   = 0000000011
  7   = 0000000111
 13   = 0000001101
100   = 0001100100
999   = 1111100111
1000  = 1111101000
```

**Strip assignment:**
```
Strip 1  (bit 0, সবচেয়ে ডান): যেসব বোতলের নম্বরে bit 0 = 1 (বিজোড় নম্বর: 1, 3, 5, ...)
Strip 2  (bit 1): যেসব বোতলে bit 1 = 1 (2, 3, 6, 7, 10, 11, ...)
Strip 3  (bit 2): যেসব বোতলে bit 2 = 1 (4, 5, 6, 7, 12, 13, ...)
...
Strip 10 (bit 9): যেসব বোতলে bit 9 = 1 (512–1000)
```

**Result পড়া:**

এক সপ্তাহ পরে যেসব strip positive হলো — তাদের bit-pattern মিলিয়ে নিন:

```
ধরুন Strip 1, 3, 7 positive হলো (বাকি negative)।

Binary: bit 0 = 1, bit 2 = 1, bit 6 = 1 → 0001000101 (MSB to LSB)

বোতল নম্বর = 2⁰ + 2² + 2⁶ = 1 + 4 + 64 = 69

উত্তর: বোতল ৬৯ বিষাক্ত।
```

```python
# Python — কীভাবে প্রতিটা strip-এ কোন বোতল রাখবেন
def assign_strips(num_bottles: int = 1000, num_strips: int = 10):
    strips = {i: [] for i in range(num_strips)}
    for bottle in range(1, num_bottles + 1):
        for bit in range(num_strips):
            if bottle & (1 << bit):        # এই bit set আছে?
                strips[bit].append(bottle) # এই strip-এ রাখুন
    return strips

# Result decode করা
def find_poisoned(positive_strips: list) -> int:
    """positive_strips: 0-indexed list of which strips turned positive"""
    bottle_number = 0
    for strip in positive_strips:
        bottle_number |= (1 << strip)     # bit set করুন
    return bottle_number

# উদাহরণ: strip 0, 2, 6 positive হলো
print(find_poisoned([0, 2, 6]))           # → 69
```

## 🔹 উত্তর

প্রতিটা বোতলের নম্বরকে 10-bit binary-তে encode করুন। প্রতিটা strip-কে একটা bit হিসেবে treat করুন — যে strip-গুলো positive হবে সেগুলোর bit set করে বোতল নম্বর বের করুন।

**মাত্র ১টা round-এ ১০২৪টা পর্যন্ত বোতল থেকে বিষাক্ত বোতল identify করা সম্ভব।**

## 🔹 যে নীতি শিখলাম

**Binary encoding as parallel testing:** পরীক্ষার ফলাফলকে bit হিসেবে treat করলে n টা strip দিয়ে `2ⁿ` টা পর্যন্ত বোতল এক round-এ identify করা যায়। এটা **information theory**-র একটা সরাসরি প্রয়োগ — n bit-এ `2ⁿ` টা unique state express করা যায়।

## 🔹 Follow-up

- **দুই সপ্তাহ থাকলে?** (দুটো round) — ৩২টা strip দিয়ে ১ মিলিয়ন বোতল identify করা যেত এক round-এ, কিন্তু sequential round-এ আরও কম strip দিয়ে চলে।
- **কতটা strip সর্বনিম্ন দরকার ১০ মিলিয়ন বোতলের জন্য?** → `ceil(log₂(10,000,000)) = 24` টা strip।

<sub>[⬆️ এই chapter-এর সূচি](#toc) · [🏠 মূল Index](README.md)</sub>

---
---

## ✅ Chapter সারসংক্ষেপ — Puzzle Solving Techniques Cheat Sheet

| # | প্রশ্ন | মূল কৌশল | মূল নীতি |
|---|---|---|---|
| 6.1 | The Heavy Pill | আলাদা সংখ্যায় pill নিন | Unique encoding দিয়ে একবার মাপ |
| 6.2 | Basketball | Probability তুলনা করুন | Inequality solve → threshold বের করুন |
| 6.3 | Dominos | রঙের invariant | Coloring argument — অসম্ভব প্রমাণ |
| 6.4 | Ants on Triangle | Complement counting | P(event) = 1 − P(opposite) |
| 6.5 | Jugs of Water | State space / BFS | GCD rule, ধাপে ধাপে state বদলান |
| 6.6 | Blue-Eyed Island | Induction + Common knowledge | Base case → n → n+1 |
| 6.7 | The Apocalypse | Expected value | Stopping rule ratio পরিবর্তন করে না |
| 6.8 | Egg Drop | Load balancing | Decreasing intervals → worst case সমান |
| 6.9 | 100 Lockers | Divisor count | Perfect square → বিজোড় divisor |
| 6.10 | Poison | Binary encoding | n bit → 2ⁿ unique states |

### "এটা দেখলে → এটা ভাবো" (Logic Puzzle সংস্করণ)

```
"একবার মাপ / একটা action"       →  Unique encoding (pill, binary)
"কোনটা বেছে নেবেন?"             →  Probability তুলনা করুন, inequality solve করুন
"সম্ভব কিনা প্রমাণ করো"          →  Invariant খুঁজুন (রং, জোড়/বিজোড়, সংখ্যা)
"কমপক্ষে কত সম্ভাবনা?"          →  Complement: 1 − P(বিপরীত ঘটনা)
"ধাপে ধাপে পৌঁছানো"             →  State space, BFS, Work backwards
"সবাই জানলে কী হয়?"            →  Common knowledge + Induction
"কত drops / কত tries?"          →  Worst case analysis, Load balancing
"কোনটা খোলা / বন্ধ?"           →  Pattern খুঁজুন (ছোট উদাহরণ দিয়ে)
"parallel test করা"             →  Binary encoding (bit = yes/no test)
```

### ৫টা সোনার নিয়ম (Logic Puzzle-এর জন্য)

1. **ছোট উদাহরণ দিয়ে শুরু করুন** (n=1, n=2, n=3) — pattern বের হয়ে আসে।
2. **Invariant খুঁজুন** — কী জিনিস পরিবর্তন হয় না? এটাই অসম্ভব প্রমাণের চাবি।
3. **Complement ব্যবহার করুন** — সরাসরি হিসাব কঠিন হলে বিপরীতটা হিসাব করুন।
4. **Information-কে encode করুন** — n bit → 2ⁿ possibilities। এটা measurement ও testing puzzle-এর মূল।
5. **Worst case সমান করুন** — optimization problem-এ সব path-এ cost ধ্রুবক রাখুন।

---

> **পরের ধাপ:** [Chapter 7 — Object-Oriented Design](chapter07_object_oriented_design.md) — যেখানে class design, inheritance, আর real-world system modeling শিখব।

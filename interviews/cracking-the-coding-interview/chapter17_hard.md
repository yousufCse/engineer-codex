# Chapter 17 — Hard (প্রশ্ন 17.1 – 17.26)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। Code **Dart + Python** দুটোতেই।
> এই chapter-গুলো hard, কিন্তু সবই চেনা technique-এর combination — ভয় পাবেন না, ধাপে ধাপে এগোব।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: Moderate](chapter16_moderate.md) · পরের: — (শেষ; [মূল Index](README.md))

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
এগুলো "hard" — কিন্তু প্রতিটা আসলে আগের chapter-এর technique মিলিয়ে বানানো।
bit, DP, trie, heap, binary search, graph — এই কয়টা টুলই বারবার ঘুরেফিরে আসে।
```

- [17.1 — Add Without Plus](#q17-1)
- [17.2 — Shuffle](#q17-2)
- [17.3 — Random Set](#q17-3)
- [17.4 — Missing Number](#q17-4)
- [17.5 — Letters and Numbers](#q17-5)
- [17.6 — Count of 2s](#q17-6)
- [17.7 — Baby Names](#q17-7)
- [17.8 — Circus Tower](#q17-8)
- [17.9 — Kth Multiple](#q17-9)
- [17.10 — Majority Element](#q17-10)
- [17.11 — Word Distance](#q17-11)
- [17.12 — BiNode](#q17-12)
- [17.13 — Re-Space](#q17-13)
- [17.14 — Smallest K](#q17-14)
- [17.15 — Longest Word](#q17-15)
- [17.16 — The Masseuse](#q17-16)
- [17.17 — Multi Search](#q17-17)
- [17.18 — Shortest Supersequence](#q17-18)
- [17.19 — Missing Two](#q17-19)
- [17.20 — Continuous Median](#q17-20)
- [17.21 — Volume of Histogram](#q17-21)
- [17.22 — Word Transformer](#q17-22)
- [17.23 — Max Black Square](#q17-23)
- [17.24 — Max Submatrix](#q17-24)
- [17.25 — Word Rectangle](#q17-25)
- [17.26 — Sparse Similarity](#q17-26)

প্রতিটা প্রশ্ন এই কাঠামোয়: **সহজ বাংলায় সমস্যা → উদাহরণ → Listen → Brute force → Optimize (BUD) → Code (Dart+Python) → Complexity → Pattern → Common mistake → Follow-up।**

---
---

# Background — Hard প্রশ্নে যাওয়ার আগে

Hard প্রশ্ন মানে নতুন জাদু নয়। মানে হলো — **একাধিক চেনা technique একসাথে**, অথবা একটা চেনা technique-কে একটু অপ্রত্যাশিত জায়গায় লাগানো। তাই আগের chapter-গুলোর tool গুলো হাতের কাছে রাখুন:

```
Technique            কোথায় শেখা         এই chapter-এ কোন প্রশ্নে লাগবে
─────────────────────────────────────────────────────────────────────
Bit manipulation     Ch5                17.1 (add), 17.4/17.19 (XOR missing)
Dynamic Programming  Ch8                17.8 (LIS), 17.16 (house robber),
                                        17.13 (word break), 17.24 (max subarray 2D)
Trie (prefix tree)   Ch4/Ch8            17.13, 17.17, 17.25
Heap / two heaps     Ch10               17.14 (Smallest K), 17.20 (median)
Binary search        Ch10               17.9-এর বিকল্প, 17.24-এর tighten
Graph / BFS          Ch4                17.7 (union), 17.22 (word ladder)
Hashing              Ch1                17.5, 17.11, 17.26
Quickselect          Ch10               17.14 (Smallest K)
Stack                Ch3                17.21 (histogram)
```

**মূল মন্ত্র:** problem পড়ে আগে জিজ্ঞেস করুন — "এটা কোন পরিচিত problem-এর ছদ্মবেশ?" বেশিরভাগ সময় উত্তর পাওয়া যায়। নিচের প্রতিটা প্রশ্নে আমরা ঠিক সেই কাজটাই করব: hard মোড়ক খুলে চেনা core বের করব।

---
---

<a id="q17-1"></a>
# 17.1 — Add Without Plus

> Pattern: **Bit Manipulation (XOR = sum, AND<<1 = carry)** · Difficulty: **Hard** · খুব common

> **বইয়ের ভাষায়:** Write a function that adds two numbers. You should not use `+` or any arithmetic operators.

## সমস্যাটা সহজ বাংলায়
দুটো integer যোগ করতে হবে, কিন্তু `+`, `-`, `*`, `/` — কোনো arithmetic operator ব্যবহার করা যাবে না। শুধু **bit operation** (`&`, `|`, `^`, `<<`, `>>`) দিয়ে।

## মূল insight — হাতে যোগ করার নিয়মই bit-এ
ছোটবেলায় যেভাবে যোগ করতাম: প্রতিটা ঘরে যোগফল লিখি, আর carry পরের ঘরে নিয়ে যাই। Binary-তে এটা ঠিক দুই ভাগে ভাগ হয়:

```
যোগফল (carry বাদে) = a XOR b        কারণ:  0+0=0, 1+0=1, 0+1=1, 1+1=0 (carry)
carry              = (a AND b) << 1  কারণ:  শুধু 1+1=1 হলে carry, আর carry এক ঘর বামে যায়
```

তারপর `a` কে XOR-result, `b` কে carry বানিয়ে আবার করি — যতক্ষণ না carry শূন্য হয়।

## উদাহরণ
```
  a = 5 = 101
  b = 3 = 011

ধাপ 1:  sum (XOR) = 110 (=6),  carry (AND<<1) = (001)<<1 = 010 (=2)
ধাপ 2:  a=110, b=010 → sum=100 (=4), carry=(010)<<1=100 (=4)
ধাপ 3:  a=100, b=100 → sum=000,      carry=(100)<<1=1000 (=8)
ধাপ 4:  a=000, b=1000 → sum=1000 (=8), carry=0  → শেষ
উত্তর = 8 = 5+3  (ঠিক)
```

## ধাপ ১: Listen
- Negative number আসবে কি? → এলে two's complement এমনিতেই কাজ করে, কিন্তু Python-এ int unbounded বলে একটু সাবধানতা লাগে (নিচে দেখুন)।
- শুধু integer তো? float হলে সম্পূর্ণ অন্য আলোচনা।

## ভাবনা ১: Brute Force
`+` ছাড়া যোগ করার "naive" উপায় নেই — তাই সরাসরি bit insight-এ যাই। (এটাই এই প্রশ্নের সৌন্দর্য: brute force বলে কিছু নেই, core trick-টাই উত্তর।)

## ভাবনা ২: Iterative bit add
উপরের দুই সূত্র loop-এ চালাই, carry শূন্য হলে থামি।

## Code

```dart
// Dart
int addWithoutPlus(int a, int b) {
  while (b != 0) {
    final carry = (a & b) << 1;  // যেখানে দুটোই 1 → carry, এক ঘর বামে
    a = a ^ b;                   // carry বাদে যোগফল
    b = carry;                   // এখন carry টাকেই যোগ করতে হবে
  }
  return a;
}
```
```python
# Python — int unbounded বলে 32-bit mask লাগে
def add_without_plus(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    while b & MASK:                       # carry শূন্য না হওয়া পর্যন্ত
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    a &= MASK
    # 32-bit sign bit set থাকলে negative-এ ফেরাও
    return a if a <= 0x7FFFFFFF else ~(a ^ MASK)
```
> Dart-এ int fixed-width (native-এ 64-bit) বলে সরাসরি কাজ করে। Python-এ int যত খুশি বড় হতে পারে, তাই carry অসীম loop করতে পারে — তাই 32-bit `MASK` দিয়ে আটকাতে হয়।

## Complexity
**Time: O(1)** (বড়জোর ৩২ বার loop, word size fixed) · **Space: O(1)**।

## Pattern চিনুন
> **"arithmetic operator ছাড়া যোগ" → XOR দিয়ে carry-বিহীন sum, AND<<1 দিয়ে carry; carry শূন্য না হওয়া পর্যন্ত repeat।** এটা half-adder/full-adder-এর software রূপ।

## Common mistake
- carry আর sum-এর ক্রম উল্টে ফেলা (`a` আপডেট করার আগেই carry হিসাব করতে হবে — নাহলে পুরোনো `a` হারিয়ে যায়)।
- Python-এ MASK ভুলে infinite loop।

## Follow-up
- **বিয়োগ (subtract) করো** → `a - b = a + (~b + 1)` (two's complement) — কিন্তু `+1` করতেও এই function লাগবে।
- **recursive লেখো** → `b==0 ? a : add(a^b, (a&b)<<1)`।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-2"></a>
# 17.2 — Shuffle

> Pattern: **Fisher-Yates Shuffle** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Write a method to shuffle a deck of cards. It must be a perfect shuffle — in other words, each of the 52! permutations of the deck has to be equally likely. Assume that you are given a random number generator which is perfect.

## সমস্যাটা সহজ বাংলায়
একটা array (যেমন ৫২টা তাস) এমনভাবে এলোমেলো (shuffle) করতে হবে যাতে **প্রতিটা সম্ভাব্য সাজানো (permutation) সমান probability**-তে আসে। অর্থাৎ কোনো একটা সাজানো বেশি favored হওয়া যাবে না।

## মূল insight — Fisher-Yates
সহজ উপায়: শেষ থেকে শুরুর দিকে যাই। প্রতিটা position `i`-এর জন্য, `0..i`-এর মধ্যে একটা random index বেছে নিয়ে swap করি।

```
i কে 0..i-এর মধ্যে যেকোনো একটার সাথে swap করি (নিজের সাথেও হতে পারে)।

arr = [A B C D]
i=3: rand(0..3)=1 → swap(3,1) → [A D C B]
i=2: rand(0..2)=2 → swap(2,2) → [A D C B]  (নিজের সাথে, ঠিক আছে)
i=1: rand(0..1)=0 → swap(1,0) → [D A C B]
i=0: শেষ, কিছু করার নেই
```

**কেন সব permutation সমান?** induction দিয়ে প্রমাণ হয়: প্রতিটা element সমান probability-তে প্রতিটা position-এ যায়, এবং মোট n! সমান সম্ভাবনায় বিন্যাস তৈরি হয়।

## ধাপ ১: Listen
- Random generator "perfect" ও uniform ধরে নিচ্ছি।
- In-place shuffle চাই (extra array নয়)।

## ভাবনা ১: Brute Force (ভুল উপায়)
প্রতিটা position-এ `rand(0..n-1)` দিয়ে swap — দেখতে একইরকম, কিন্তু এটা **biased**! কারণ n^n রকম outcome আছে যা n!-এর গুণিতক নয়, তাই কিছু permutation বেশি আসে। এটাই common ফাঁদ।

## ভাবনা ২: Fisher-Yates (সঠিক)
`rand(0..i)` ব্যবহার করা key — `0..n-1` নয়।

## Code

```dart
// Dart
import 'dart:math';

void shuffle(List<int> arr) {
  final rng = Random();
  for (int i = arr.length - 1; i > 0; i--) {
    final j = rng.nextInt(i + 1);   // 0..i (i সহ) থেকে random
    final t = arr[i]; arr[i] = arr[j]; arr[j] = t;
  }
}
```
```python
# Python
import random

def shuffle(arr: list) -> None:
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)     # 0..i inclusive
        arr[i], arr[j] = arr[j], arr[i]
```

## Complexity
**Time: O(n)** · **Space: O(1)** (in-place)।

## Pattern চিনুন
> **"uniform random permutation / perfect shuffle" → Fisher-Yates, প্রতি i-তে rand(0..i) দিয়ে swap।** `rand(0..n-1)` ব্যবহার = biased।

## Common mistake
- `rand(0..n-1)` ব্যবহার করে biased shuffle বানানো।
- "shuffle করে sort করব random key দিয়ে" — কাজ করে কিন্তু O(n log n) ও tie-handling tricky।

## Follow-up
- **prove করো uniform** → induction: ধরো n-1 element ঠিকঠাক shuffled, তাহলে n-th element প্রতিটা slot-এ 1/n probability পায়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-3"></a>
# 17.3 — Random Set

> Pattern: **Reservoir Sampling / Fisher-Yates partial** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Write a method to randomly generate a set of m integers from an array of size n. Each element must have equal probability of being chosen.

## সমস্যাটা সহজ বাংলায়
n size-এর একটা array থেকে **m টা element** এমনভাবে বাছতে হবে যাতে প্রতিটা element বাছাই হওয়ার probability সমান (`m/n`)। এটা আগের shuffle-এরই ছোট ভাই।

## উদাহরণ
```
arr = [10 20 30 40 50], m=2
সম্ভাব্য উত্তর: {20,50}, {10,30}, ...  প্রতিটা element 2/5 প্রায় সমান probability পাবে।
```

## ভাবনা ১: পুরো shuffle করে প্রথম m নাও
Fisher-Yates দিয়ে পুরোটা shuffle, তারপর প্রথম m টা নাও। কাজ করে কিন্তু পুরো array shuffle করা অপ্রয়োজনীয় — **partial shuffle**-ই যথেষ্ট।

## ভাবনা ২: Partial Fisher-Yates (m known, array পুরোটা আছে)
শুধু প্রথম m position-এর জন্য swap করি — বাকিটা ছোঁয়ার দরকার নেই।

## ভাবনা ৩: Reservoir Sampling (stream / n অজানা হলে)
প্রথম m element সরাসরি নিই। তারপর i-th (i≥m) element-এর জন্য `rand(0..i)` বের করি; সেটা < m হলে reservoir-এর সেই slot replace করি। এতে stream-এও কাজ করে, n আগে জানার দরকার নেই।

```
reservoir = প্রথম m টা
i = m, m+1, ...:
   j = rand(0..i)
   if j < m:  reservoir[j] = arr[i]   (নতুন element ঢুকে পুরোনোটা সরায়)
```

## Code

```dart
// Dart — reservoir sampling
import 'dart:math';

List<int> pickRandomSet(List<int> arr, int m) {
  final rng = Random();
  final reservoir = List<int>.from(arr.take(m));   // প্রথম m
  for (int i = m; i < arr.length; i++) {
    final j = rng.nextInt(i + 1);                  // 0..i
    if (j < m) reservoir[j] = arr[i];
  }
  return reservoir;
}
```
```python
# Python — reservoir sampling
import random

def pick_random_set(arr: list, m: int) -> list:
    reservoir = list(arr[:m])                 # প্রথম m
    for i in range(m, len(arr)):
        j = random.randint(0, i)              # 0..i
        if j < m:
            reservoir[j] = arr[i]
    return reservoir
```

## Complexity
**Time: O(n)** · **Space: O(m)**।

## Pattern চিনুন
> **"n থেকে m uniform বাছো (especially stream, n অজানা)" → Reservoir Sampling।** array পুরোটা থাকলে partial Fisher-Yates-ও চলে।

## Common mistake
- `rand(0..i)` এর বদলে `rand(0..n-1)` দিয়ে bias আনা।
- m টা element আর m টা **index** গুলিয়ে ফেলা।

## Follow-up
- **n অজানা / infinite stream** → reservoir sampling-ই একমাত্র উপায়।
- **weighted sampling** → weighted reservoir (A-Res algorithm)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-4"></a>
# 17.4 — Missing Number

> Pattern: **Bit by bit / XOR** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** An array A contains all the integers from 0 to n, except for one number which is missing. In this problem, we cannot access an entire integer in A with a single operation. The elements of A are represented in binary, and the only operation we can use to access them is "fetch the j-th bit of A[i]", which takes constant time. Write code to find the missing integer. Can you do it in O(n) time?

## সমস্যাটা সহজ বাংলায়
`0..n` এর সব সংখ্যা array-তে আছে, শুধু একটা missing। কিন্তু পুরো integer একবারে পড়া যায় না — শুধু **একটা একটা bit** পড়া যায়। O(n)-এ missing সংখ্যা বের করতে হবে।

## সহজ version আগে (যদি পুরো int পড়তে পারতাম)
`0..n`-এর sum = `n(n+1)/2`। array-এর sum বিয়োগ করলেই missing। অথবা সব XOR করলে missing থেকে যায়। কিন্তু এখানে **bit-only access**, তাই ভিন্ন চিন্তা লাগবে।

## মূল insight — least significant bit দিয়ে অর্ধেক করা
`0..n`-এ LSB (bit 0) দেখুন: শূন্য-শেষ আর এক-শেষ সংখ্যার count নিয়ে একটা নিয়ম আছে।

```
0..n এর মধ্যে যত সংখ্যা:
  count(LSB=0)  ≥  count(LSB=1)    সবসময় (0,2,4... একটা বেশি বা সমান)

missing সংখ্যাটা যদি LSB=0 হয় → বাকিদের মধ্যে LSB=0 count কমে যাবে
                  LSB=1 হয় → LSB=1 count কমে যাবে

প্রতিটা bit-position দেখে missing number-এর সেই bit নির্ধারণ করি, তারপর
শুধু সেই bit-এ মেলা সংখ্যাগুলো রেখে সমস্যাটা অর্ধেক করি।
```

প্রতি pass-এ অর্ধেক element বাদ → `n + n/2 + n/4 + ... = O(n)` (geometric series)।

## ভাবনা ১: Brute Force
প্রতিটা সংখ্যার সব bit পড়ে set বানিয়ে missing খোঁজা — O(n log n) bit-access। কাজ করে কিন্তু target O(n)।

## ভাবনা ২: Bit-position দিয়ে অর্ধেক (O(n))
LSB থেকে শুরু করে প্রতিটা bit নির্ধারণ করি।

## Code

```dart
// Dart
int findMissing(List<int> nums) {
  return helper(nums, 0);
}

int helper(List<int> nums, int column) {
  if (nums.isEmpty) return 0;
  final ones = <int>[], zeros = <int>[];
  for (final x in nums) {
    if (((x >> column) & 1) == 0) {
      zeros.add(x);
    } else {
      ones.add(x);
    }
  }
  if (zeros.length <= ones.length) {
    // missing-এর এই bit 0 → zeros-এর মধ্যে খুঁজে যাও
    final v = helper(zeros, column + 1);
    return (v << 1) | 0;
  } else {
    final v = helper(ones, column + 1);
    return (v << 1) | 1;
  }
}
```
```python
# Python
def find_missing(nums: list) -> int:
    def helper(nums, column):
        if not nums:
            return 0
        zeros, ones = [], []
        for x in nums:
            if (x >> column) & 1 == 0:
                zeros.append(x)
            else:
                ones.append(x)
        if len(zeros) <= len(ones):       # missing-এর এই bit = 0
            return helper(zeros, column + 1) << 1 | 0
        else:                             # missing-এর এই bit = 1
            return helper(ones, column + 1) << 1 | 1
    return helper(nums, 0)
```
> এখানে শুধু `(x >> column) & 1` দিয়ে **একটা bit** পড়ছি — যা problem-এর constraint মেনে চলে।

## Complexity
**Time: O(n)** (n + n/2 + ... = 2n) · **Space: O(n)** (partition list; in-place করলে O(log n) recursion)।

## Pattern চিনুন
> **"bit-only access / একটা missing খুঁজো" → bit-position ধরে অর্ধেক করো (divide & conquer on bits)।** পুরো int পড়তে পারলে XOR/sum trick যথেষ্ট।

## Common mistake
- `count(0) <= count(1)` শর্তে সমান-এর case ভুল করা (সমান হলে missing-এর bit 0)।
- recursion-এ bit shift-এর ক্রম গুলিয়ে ফেলা।

## Follow-up
- **পুরো int পড়া গেলে** → `sum(0..n) - sum(arr)` বা সব XOR — দুটোই O(n), O(1) space।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-5"></a>
# 17.5 — Letters and Numbers

> Pattern: **Prefix sum + Hash (longest balanced subarray)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers.

## সমস্যাটা সহজ বাংলায়
একটা array-তে কিছু letter আর কিছু number মেশানো। এমন সবচেয়ে **লম্বা subarray** খুঁজতে হবে যেখানে letter আর number-এর সংখ্যা **সমান**।

## মূল insight — letter=+1, number=−1 ধরে prefix sum
letter কে +1, number কে −1 ধরি। তাহলে যেকোনো subarray-তে সমান সংখ্যক হওয়া মানে সেই subarray-র sum = 0।

```
arr:    a  1  b  c  4  d
value: +1 -1 +1 +1 -1 +1
prefix:  1  0  1  2  1  2     (running sum)
         ↑     ↑
   index -1 আর কোথাও prefix সমান হলে মাঝের অংশের sum=0
```

> **মূল trick:** যদি `prefix[i] == prefix[j]` হয় (i<j), তাহলে `i+1..j` subarray-র sum = 0 → balanced। তাই প্রতিটা prefix-value প্রথম কোথায় দেখলাম সেটা hash-এ রাখি; আবার একই value পেলে দূরত্ব মাপি।

## ভাবনা ১: Brute Force
সব subarray ধরে count মেলানো — O(n²) (running count রাখলে)। কাজ করে কিন্তু slow।

## ভাবনা ২: Prefix sum + Hash (O(n))
প্রতিটা prefix-sum প্রথম যে index-এ দেখলাম তা map-এ রাখি। আবার সেই sum এলে → এই দুই index-এর মাঝের অংশ balanced; দৈর্ঘ্য আপডেট করি।

## Code

```dart
// Dart
// isLetter(x) true হলে letter, নাহলে number ধরছি
List<dynamic> longestBalanced(List<dynamic> arr, bool Function(dynamic) isLetter) {
  final firstIndex = <int, int>{0: -1};   // sum 0 কে index -1-এ ধরি
  int sum = 0, bestStart = 0, bestLen = 0;
  for (int i = 0; i < arr.length; i++) {
    sum += isLetter(arr[i]) ? 1 : -1;
    if (firstIndex.containsKey(sum)) {
      final len = i - firstIndex[sum]!;
      if (len > bestLen) { bestLen = len; bestStart = firstIndex[sum]! + 1; }
    } else {
      firstIndex[sum] = i;                // প্রথমবার এই sum দেখলাম
    }
  }
  return arr.sublist(bestStart, bestStart + bestLen);
}
```
```python
# Python
def longest_balanced(arr: list, is_letter) -> list:
    first_index = {0: -1}     # sum 0 → index -1
    s = best_start = best_len = 0
    for i, x in enumerate(arr):
        s += 1 if is_letter(x) else -1
        if s in first_index:
            length = i - first_index[s]
            if length > best_len:
                best_len = length
                best_start = first_index[s] + 1
        else:
            first_index[s] = i            # প্রথমবার এই sum
    return arr[best_start:best_start + best_len]
```

## Complexity
**Time: O(n)** · **Space: O(n)** (hash-এ prefix sum)।

## Pattern চিনুন
> **"sum/count সমান এমন longest subarray" → +1/−1 ধরে prefix sum, একই prefix-value-এর প্রথম index hash-এ রাখো।** ("equal 0s and 1s", "subarray sum = k" — সব একই পরিবার।)

## Common mistake
- `{0: -1}` initial entry ভুলে যাওয়া (শুরু থেকে balanced হলে মিস হয়)।
- প্রতিটা sum-এর **প্রথম** index রাখার বদলে শেষেরটা রাখা (longest পাওয়া যায় না)।

## Follow-up
- **letter আর number-এর exact সংখ্যা return করো** → length/2 করে পাওয়া যায়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-6"></a>
# 17.6 — Count of 2s

> Pattern: **Digit DP / counting by place value** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Write a method to count the number of 2s that appear in all the numbers between 0 and n (inclusive). Example: input 25 → output 9 (2,12,20,21,22,23,24,25 — মনে রাখুন 22-তে দুটো 2)।

## সমস্যাটা সহজ বাংলায়
`0` থেকে `n` পর্যন্ত সব সংখ্যা লিখলে, তাতে digit **2** মোট কতবার আসে? (যেমন 22-তে 2 দুইবার গোনা হবে।)

## মূল insight — প্রতিটা digit-position আলাদা করে গোনো
প্রতিটা স্থান (একক, দশক, শতক...) ধরে আলাদাভাবে গুনি: "এই position-এ কতবার 2 আসবে"। প্রতিটা position-এ digit আসে চক্রাকারে (০,১,...,৯,০,১,...)।

```
এই position-এর digit d ধরে তিনটা case:
  d < 2 :  count = (higher) * 10^pos
  d == 2:  count = (higher) * 10^pos + (lower + 1)
  d > 2 :  count = (higher + 1) * 10^pos

higher = এই position-এর বামের সব digit
lower  = এই position-এর ডানের সব digit
```

```
উদাহরণ n=25, দশকের ঘর (pos=1, 10^1):
  digit এখানে = 2, higher = 0, lower = 5
  d==2 → 0*10 + (5+1) = 6   (20..25 — ৬টা সংখ্যায় দশকে 2)
এককের ঘর (pos=0):
  digit = 5 (>2), higher = 2 → (2+1)*1 = 3   (2,12,22 — এককে 2)
মোট = 6 + 3 = 9  (ঠিক)
```

## ভাবনা ১: Brute Force
0..n প্রতিটা সংখ্যার প্রতিটা digit দেখে 2 গোনা — O(n · log n)। n বড় হলে অসম্ভব।

## ভাবনা ২: Place-value counting (O(log n))
উপরের সূত্র প্রতিটা digit-position-এ লাগাই।

## Code

```dart
// Dart
int countOf2s(int n) {
  int count = 0;
  for (int pos = 1; pos <= n; pos *= 10) {
    final divider = pos * 10;
    final higher = n ~/ divider;
    final cur = (n ~/ pos) % 10;
    final lower = n % pos;
    if (cur < 2) {
      count += higher * pos;
    } else if (cur == 2) {
      count += higher * pos + lower + 1;
    } else {
      count += (higher + 1) * pos;
    }
  }
  return count;
}
```
```python
# Python
def count_of_2s(n: int) -> int:
    count = 0
    pos = 1
    while pos <= n:
        divider = pos * 10
        higher = n // divider
        cur = (n // pos) % 10
        lower = n % pos
        if cur < 2:
            count += higher * pos
        elif cur == 2:
            count += higher * pos + lower + 1
        else:
            count += (higher + 1) * pos
        pos *= 10
    return count
```

## Complexity
**Time: O(log n)** (digit সংখ্যার সমান pass) · **Space: O(1)**।

## Pattern চিনুন
> **"0..n-এ একটা digit কতবার আসে" → প্রতিটা place-value আলাদা করে গোনো, higher/current/lower দিয়ে case ভাগ করো (digit DP-র সরল রূপ)।**

## Common mistake
- প্রতিটা সংখ্যা লুপ করে গোনা (n বড় হলে fail)।
- `cur == 2`-এ `lower + 1` (`+1` কারণ lower==0-ও একটা valid সংখ্যা)।

## Follow-up
- **যেকোনো digit d (1..9)** → একই code, শুধু 2-এর জায়গায় d। (0 একটু আলাদা — leading zero বাদ দিতে হয়।)

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-7"></a>
# 17.7 — Baby Names

> Pattern: **Union-Find / Graph connected components** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Each year, the government releases a list of the 10000 most common baby names and their frequencies. Some names have variant spellings of the same name (e.g., John and Jon are the same). Given two lists — one of names/frequencies, one of pairs of equivalent names — print a new list of the true frequency of each name. Note: if John/Jon and Jon/Johnny are synonyms, then John/Johnny are synonyms too (transitive)। Choose any spelling as the canonical name.

## সমস্যাটা সহজ বাংলায়
কিছু নাম আর তাদের frequency দেওয়া। আর কিছু "এই দুটো নাম একই" জোড়া দেওয়া (synonym)। এই সম্পর্ক transitive — A=B আর B=C হলে A=C। প্রতিটা group-এর মোট frequency বের করে, group-প্রতি একটা নাম দিয়ে রিপোর্ট করতে হবে।

## মূল insight — এটা connected components
নামগুলো node, synonym জোড়া edge। একই component-এর সব নাম একই person → frequency যোগ করো। **Union-Find (Disjoint Set)** এর জন্য আদর্শ।

```
John ── Jon ── Johnny       (একটা component)
Kari ── Carrie              (আরেকটা)

প্রতিটা component-এ একটা representative (root) বাছি,
ওই root-এ পুরো group-এর frequency জমাই।
```

## ভাবনা ১: Graph + BFS/DFS
নামগুলো দিয়ে graph বানিয়ে প্রতিটা component traverse করে frequency যোগ করা — কাজ করে, O(নাম + জোড়া)।

## ভাবনা ২: Union-Find (পরিষ্কার ও দ্রুত)
প্রতিটা synonym-এ দুই নাম union করি; শেষে প্রতিটা নামের root বের করে frequency জমাই।

## Code

```dart
// Dart — Union-Find
class UnionFind {
  final Map<String, String> parent = {};
  String find(String x) {
    parent.putIfAbsent(x, () => x);
    if (parent[x] != x) parent[x] = find(parent[x]!);  // path compression
    return parent[x]!;
  }
  void union(String a, String b) { parent[find(a)] = find(b); }
}

Map<String, int> trueFrequencies(
    Map<String, int> names, List<List<String>> synonyms) {
  final uf = UnionFind();
  for (final n in names.keys) uf.find(n);            // সব নাম register
  for (final s in synonyms) { uf.find(s[0]); uf.find(s[1]); uf.union(s[0], s[1]); }
  final result = <String, int>{};
  names.forEach((name, freq) {
    final root = uf.find(name);
    result[root] = (result[root] ?? 0) + freq;       // root-এ জমাও
  });
  return result;
}
```
```python
# Python — Union-Find
def true_frequencies(names: dict, synonyms: list) -> dict:
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])     # path compression
        return parent[x]
    def union(a, b):
        parent[find(a)] = find(b)

    for n in names:
        find(n)
    for a, b in synonyms:
        find(a); find(b); union(a, b)

    result = {}
    for name, freq in names.items():
        root = find(name)
        result[root] = result.get(root, 0) + freq
    return result
```

## Complexity
**Time: ~O((N + P) · α(N))** (α = inverse Ackermann, প্রায় constant) · **Space: O(N)**।

## Pattern চিনুন
> **"equivalent / same group / transitive মিল" → Union-Find (বা connected components)।** "এই দুটো একই" + "transitive" শুনলেই Union-Find।

## Common mistake
- transitive সম্পর্ক হাতে handle করতে গিয়ে গোলমাল (Union-Find নিজেই transitivity সামলায়)।
- synonym-এ এমন নাম যা frequency list-এ নেই — তবুও register করতে হবে।

## Follow-up
- **canonical নাম alphabetically smallest চাই** → union-এ root হিসেবে ছোট নামটা রাখো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-8"></a>
# 17.8 — Circus Tower

> Pattern: **Longest Increasing Subsequence (LIS) on 2D** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** A circus is designing a tower routine consisting of people standing atop one another's shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below them. Given the heights and weights of each person, write a method to compute the largest possible number of people in such a tower.

## সমস্যাটা সহজ বাংলায়
প্রত্যেকের একটা (height, weight) আছে। একজন আরেকজনের কাঁধে দাঁড়াতে পারে যদি সে **height-এও ছোট, weight-এও কম**। সবচেয়ে লম্বা টাওয়ার (সর্বোচ্চ মানুষ) কত?

## মূল insight — sort করে 1D LIS-এ নামাও
দুটো dimension একসাথে সামলানো কঠিন। তাই:

```
ধাপ 1: height অনুযায়ী ascending sort করো।
        (height সমান হলে weight descending — যাতে একই height দুজন একসাথে না নেওয়া যায়)
ধাপ 2: এখন height এমনিতেই sorted; শুধু weight-এর উপর
        Longest Increasing Subsequence (strictly increasing) বের করো।
```

> sort করার পর height-এর শর্ত আপনাআপনি মিটে যায় (বাম থেকে ডানে height বাড়ছে), তাই শুধু weight-এর LIS-ই বাকি কাজ। এটাই hard থেকে চেনা LIS-এ নামানোর ট্রিক।

## উদাহরণ
```
(65,100) (70,150) (56,90) (75,190) (60,95) (68,110)
height sort: (56,90)(60,95)(65,100)(68,110)(70,150)(75,190)
weight:        90    95    100    110    150    190   → পুরোটাই increasing
→ tower height = 6
```

## ভাবনা ১: Brute Force
সব subset ধরে valid কিনা দেখা — O(2^n)। অসম্ভব।

## ভাবনা ২: Sort + O(n²) LIS
weight-এর উপর classic DP LIS।

## ভাবনা ৩: Sort + O(n log n) LIS
patience sorting / binary search দিয়ে LIS।

## Code

```dart
// Dart — sort + O(n²) LIS
int largestTower(List<List<int>> people) {
  people.sort((a, b) =>
      a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);   // height asc, weight desc
  final n = people.length;
  final dp = List<int>.filled(n, 1);
  int best = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (people[j][0] < people[i][0] && people[j][1] < people[i][1]) {
        if (dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
      }
    }
    if (dp[i] > best) best = dp[i];
  }
  return best;
}
```
```python
# Python — sort + O(n²) LIS
def largest_tower(people: list) -> int:
    people.sort(key=lambda p: (p[0], -p[1]))    # height asc, weight desc
    n = len(people)
    dp = [1] * n
    best = 0
    for i in range(n):
        for j in range(i):
            if people[j][0] < people[i][0] and people[j][1] < people[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
        best = max(best, dp[i])
    return best
```

## Complexity
**Time: O(n²)** (sort O(n log n) + DP O(n²); binary-search LIS দিয়ে O(n log n)) · **Space: O(n)**।

## Pattern চিনুন
> **"দুই dimension-এ strictly বাড়তে হবে / nesting (envelope, tower, Russian doll)" → একটা dimension sort করে অন্যটায় LIS।** tie-handling (weight desc) খুব গুরুত্বপূর্ণ।

## Common mistake
- tie-তে weight descending না করা → একই height-এর দুজন ভুল করে একসাথে নেওয়া হয়।
- `<` vs `<=` গুলিয়ে strictly-শর্ত ভাঙা।

## Follow-up
- **O(n log n) চাও** → weight-এর উপর patience-sorting LIS (binary search)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-9"></a>
# 17.9 — Kth Multiple

> Pattern: **Multi-pointer merge (3,5,7-smooth numbers)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors. For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, ...

## সমস্যাটা সহজ বাংলায়
এমন k-তম সংখ্যা চাই যার **prime factor শুধু 3, 5, 7**। মানে সংখ্যাটা `3^a · 5^b · 7^c` রূপে লেখা যায়। ছোট থেকে বড় ক্রমে: 1, 3, 5, 7, 9, 15, 21, 25, ...

## মূল insight — প্রতিটা নতুন সংখ্যা পুরোনো একটাকে 3/5/7 দিয়ে গুণ
প্রতিটা valid সংখ্যা আসলে আগের কোনো valid সংখ্যাকে 3, 5, বা 7 দিয়ে গুণ করে পাওয়া। তিনটা "queue"-এর মতো three-pointer রাখি।

```
list শুরু: [1]
তিনটা multiplier 3,5,7 — প্রতিটার একটা pointer (q3,q5,q7) যা list-এ index দেখায়।

প্রতি ধাপে: list[q3]*3, list[q5]*5, list[q7]*7 — এদের minimum নাও (= পরের সংখ্যা)।
যে pointer-গুলো সেই min produce করল, তাদের এগোও (duplicate এড়াতে একাধিকও এগোতে পারে)।
```

```
list: 1
v3=1*3=3, v5=1*5=5, v7=1*7=7 → min=3 → list:[1,3], q3++
v3=3*3=9, v5=5,    v7=7      → min=5 → list:[1,3,5], q5++
v3=9,    v5=5*5=25,v7=7      → min=7 → [1,3,5,7], q7++
v3=9, v5=25, v7=7*5? না — v7=list[q7]*7 ... → min=9 → [1,3,5,7,9]
```

## ভাবনা ১: Brute Force
1,2,3,... প্রতিটা সংখ্যা বারবার 3/5/7 দিয়ে ভাগ করে check — অনেক নষ্ট কাজ, slow।

## ভাবনা ২: Min-heap
heap-এ 1 রাখি, pop করে ×3,×5,×7 push (set দিয়ে duplicate এড়াই)। O(k log k)।

## ভাবনা ৩: Three-pointer (O(k), best)
উপরের multi-pointer merge — কোনো heap বা duplicate-set লাগে না।

## Code

```dart
// Dart — three pointers
int kthMultiple(int k) {
  final list = List<int>.filled(k, 0);
  list[0] = 1;
  int q3 = 0, q5 = 0, q7 = 0;
  for (int i = 1; i < k; i++) {
    final v3 = list[q3] * 3, v5 = list[q5] * 5, v7 = list[q7] * 7;
    final m = [v3, v5, v7].reduce((a, b) => a < b ? a : b);
    list[i] = m;
    if (m == v3) q3++;     // একই min একাধিক হলে সবগুলো এগোও → duplicate বাদ
    if (m == v5) q5++;
    if (m == v7) q7++;
  }
  return list[k - 1];
}
```
```python
# Python — three pointers
def kth_multiple(k: int) -> int:
    nums = [0] * k
    nums[0] = 1
    q3 = q5 = q7 = 0
    for i in range(1, k):
        v3, v5, v7 = nums[q3] * 3, nums[q5] * 5, nums[q7] * 7
        m = min(v3, v5, v7)
        nums[i] = m
        if m == v3: q3 += 1
        if m == v5: q5 += 1
        if m == v7: q7 += 1
    return nums[k - 1]
```

## Complexity
**Time: O(k)** · **Space: O(k)**। (heap version O(k log k)।)

## Pattern চিনুন
> **"prime factor শুধু কয়েকটা / ugly numbers" → multi-pointer merge অথবা min-heap।** তিনটা multiplier = তিনটা pointer।

## Common mistake
- duplicate handle না করা — min হলে **যত pointer** সেই min দেয় **সবগুলো** এগোতে হবে (`if`, `elif` নয়)।
- 1-কে শুরুতে না রাখা (3^0·5^0·7^0 = 1)।

## Follow-up
- **শুধু 3,5,7 নয়, যেকোনো prime set** → প্রতিটা prime-এর জন্য একটা pointer (generalized)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-10"></a>
# 17.10 — Majority Element

> Pattern: **Boyer-Moore Voting** · Difficulty: **Hard** · খুব common

> **বইয়ের ভাষায়:** A majority element is an element that makes up more than half of the items in an array. Given an array, find the majority element. If there is no majority element, return -1. Do this in O(N) time and O(1) space.

## সমস্যাটা সহজ বাংলায়
যে element array-র **অর্ধেকের বেশি** জুড়ে আছে, সেটাই majority। না থাকলে −1। শর্ত: **O(N) time, O(1) space** — তাই hash count (O(N) space) চলবে না।

## মূল insight — Boyer-Moore Voting
একটা candidate আর একটা count রাখি। একই element এলে count বাড়াই, ভিন্ন এলে কমাই; count 0 হলে নতুন candidate নিই।

```
ভাবুন: প্রতিটা ভিন্ন element majority-র একটা "ভোট কাটে"। majority অর্ধেকের বেশি,
তাই সব কাটাকাটির পরও সে টিকে থাকবে।

arr = [3 3 4 2 3 3 3]
cand=3,cnt=1 → 3:cnt2 → 4:cnt1 → 2:cnt0 → 3:cand3,cnt1 → 3:cnt2 → 3:cnt3
candidate = 3
```

কিন্তু candidate সবসময় majority নয় (majority না থাকলেও কেউ একটা টিকে যায়) — তাই **দ্বিতীয় pass**-এ গুনে verify করতেই হবে।

## ভাবনা ১: Brute Force / Hash count
hash-এ count → O(N) time কিন্তু **O(N) space** (শর্ত ভাঙে)।

## ভাবনা ২: Boyer-Moore (O(N) time, O(1) space)
candidate বের করো, তারপর verify করো।

## Code

```dart
// Dart
int majorityElement(List<int> nums) {
  // pass 1: candidate খুঁজি
  int candidate = 0, count = 0;
  for (final x in nums) {
    if (count == 0) candidate = x;
    count += (x == candidate) ? 1 : -1;
  }
  // pass 2: verify (majority আদৌ আছে কিনা)
  int c = 0;
  for (final x in nums) if (x == candidate) c++;
  return c > nums.length ~/ 2 ? candidate : -1;
}
```
```python
# Python
def majority_element(nums: list) -> int:
    candidate, count = None, 0
    for x in nums:                       # pass 1: candidate
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    if sum(1 for x in nums if x == candidate) > len(nums) // 2:  # pass 2: verify
        return candidate
    return -1
```

## Complexity
**Time: O(N)** (দুই pass) · **Space: O(1)**।

## Pattern চিনুন
> **"অর্ধেকের বেশি / majority, O(1) space" → Boyer-Moore voting (cancel out), তারপর verify।** count cancel = একই candidate বারবার "ভোট" দিচ্ছে।

## Common mistake
- verify pass বাদ দেওয়া (majority না থাকলেও candidate পাওয়া যায় — verify ছাড়া ভুল উত্তর)।
- "অর্ধেকের বেশি" (strictly `> n/2`) — `>=` নয়।

## Follow-up
- **n/3-এর বেশি যারা (সর্বোচ্চ ২টা)** → দুটো candidate দিয়ে generalized Boyer-Moore।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-11"></a>
# 17.11 — Word Distance

> Pattern: **Single-pass min distance / preprocessing** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** You have a large text file containing words. Given any two words, find the shortest distance (in terms of number of words) between them in the file. If the operation will be repeated many times for the same file (but different pairs of words), can you optimize your solution?

## সমস্যাটা সহজ বাংলায়
একটা বড় ফাইলে অনেক word। দুটো word দিলে — তারা ফাইলে সবচেয়ে কাছাকাছি (কত word-এর দূরত্বে) কোথায় আছে বলতে হবে। আর follow-up: **একই ফাইলে বহুবার** query এলে কীভাবে দ্রুত করবেন?

## ভাবনা ১: Single query — one pass, দুটো last-seen index
ফাইল একবার হাঁটি। word1 বা word2 দেখলে তার last position আপডেট করি; প্রতিবার দুটোরই last index থাকলে দূরত্ব মাপি।

```
words: a w1 b c w2 d w1 e
       0  1 2 3  4 5  6 7
w1@1, w2@4 → dist 3
w1@6, w2@4 → dist 2   ← ছোট, এটাই রাখি
```

## ভাবনা ২: বহু query — preprocess (word → sorted index list)
প্রতিটা word কোন কোন position-এ আছে তার তালিকা একবার বানিয়ে রাখি (hash → sorted list)। query-তে দুই তালিকা দুটো pointer দিয়ে merge করে নিকটতম জোড়া খুঁজি — O(A+B)।

```
location["w1"] = [1, 6]
location["w2"] = [4]
দুই sorted list-এ two-pointer → সবচেয়ে কাছের জোড়া
```

## Code

```dart
// Dart — single query, one pass
int wordDistance(List<String> words, String w1, String w2) {
  int last1 = -1, last2 = -1, best = 1 << 30;
  for (int i = 0; i < words.length; i++) {
    if (words[i] == w1) {
      last1 = i;
      if (last2 != -1 && i - last2 < best) best = i - last2;
    } else if (words[i] == w2) {
      last2 = i;
      if (last1 != -1 && i - last1 < best) best = i - last1;
    }
  }
  return best;
}
```
```python
# Python — single query, one pass
def word_distance(words: list, w1: str, w2: str) -> int:
    last1 = last2 = -1
    best = float('inf')
    for i, w in enumerate(words):
        if w == w1:
            last1 = i
            if last2 != -1:
                best = min(best, i - last2)
        elif w == w2:
            last2 = i
            if last1 != -1:
                best = min(best, i - last1)
    return best
```
```python
# Python — many queries: preprocess word -> [positions], then two-pointer
def build_index(words: list) -> dict:
    idx = {}
    for i, w in enumerate(words):
        idx.setdefault(w, []).append(i)
    return idx

def closest(idx: dict, w1: str, w2: str) -> int:
    a, b = idx[w1], idx[w2]     # দুটোই sorted (append order)
    i = j = 0
    best = float('inf')
    while i < len(a) and j < len(b):
        best = min(best, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return best
```

## Complexity
- Single query: **Time O(N)**, Space O(1)।
- Many queries: preprocess **O(N)**; প্রতি query **O(A+B)** (দুই word-এর occurrence সংখ্যা); Space O(N)।

## Pattern চিনুন
> **"একবার vs বহুবার query" শুনলেই → preprocess করে index বানাও।** নিকটতম জোড়া দুই sorted list-এ two-pointer merge।

## Common mistake
- প্রতি query-তে পুরো ফাইল আবার scan করা (বহু query হলে দুর্বল)।
- two-pointer-এ ছোট value-র pointer এগোতে ভুলে যাওয়া।

## Follow-up
- **দুইয়ের বেশি word-এর সবচেয়ে ছোট window** → "smallest range covering k lists" (heap)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-12"></a>
# 17.12 — BiNode

> Pattern: **In-order traversal → Doubly Linked List** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Consider a simple data structure called BiNode, which has pointers to two other nodes (node1 and node2). It could represent both a binary tree (node1=left, node2=right) and a doubly linked list (node1=prev, node2=next). Implement a method to convert a binary search tree (implemented with BiNode) into a doubly linked list. The values should be kept in order and the operation should be performed in place.

## সমস্যাটা সহজ বাংলায়
একই `BiNode` structure (দুটো pointer: node1, node2) দিয়ে BST বানানো আছে। সেটাকে **in-place** এমন doubly linked list বানাতে হবে যেখানে মান **sorted order**-এ থাকে। (BST-তে node1=left, node2=right; list-এ node1=prev, node2=next।)

## মূল insight — in-order traversal-ই sorted order দেয়
BST-তে **in-order** (left → node → right) traverse করলে মান বাড়ার ক্রমে আসে। তাই in-order ক্রমে প্রতিটা node-কে আগেরটার সাথে জুড়ে দিলেই sorted doubly linked list।

```
        4
       / \
      2   5
     / \
    1   3

in-order: 1 2 3 4 5
→ 1 <-> 2 <-> 3 <-> 4 <-> 5   (node1=prev, node2=next)
```

## ভাবনা ১: in-order করে list-এ জমাও, পরে জোড়ো
সহজ কিন্তু O(n) extra space।

## ভাবনা ২: Recursive merge (in-place, head/tail track)
প্রতিটা subtree কে DLL বানিয়ে left-list + node + right-list জোড়ো। একটা পরিচ্ছন্ন উপায়: in-order traverse করে একটা `prev` pointer রাখি, প্রতিটা node-এ prev আর cur দুই দিকে জুড়ি।

## Code

```dart
// Dart
class BiNode {
  int data;
  BiNode? node1, node2;   // BST: left,right | DLL: prev,next
  BiNode(this.data);
}

BiNode? bstToDll(BiNode? root) {
  BiNode? head, prev;
  void inorder(BiNode? node) {
    if (node == null) return;
    inorder(node.node1);            // left
    if (prev == null) {
      head = node;                  // সবচেয়ে বাম = head
    } else {
      prev.node2 = node;            // prev.next = node
      node.node1 = prev;            // node.prev = prev
    }
    prev = node;
    inorder(node.node2);            // right
  }
  inorder(root);
  return head;
}
```
```python
# Python
class BiNode:
    def __init__(self, data):
        self.data = data
        self.node1 = None   # left / prev
        self.node2 = None   # right / next

def bst_to_dll(root):
    head = None
    prev = None
    def inorder(node):
        nonlocal head, prev
        if not node:
            return
        inorder(node.node1)         # left
        if prev is None:
            head = node             # leftmost = head
        else:
            prev.node2 = node       # prev.next = node
            node.node1 = prev       # node.prev = prev
        prev = node
        inorder(node.node2)         # right
    inorder(root)
    return head
```

## Complexity
**Time: O(n)** (প্রতিটা node একবার) · **Space: O(h)** (recursion stack, h = height)।

## Pattern চিনুন
> **"BST → sorted sequence / sorted DLL" → in-order traversal, একটা prev pointer দিয়ে জোড়া।** in-order = sorted, এটাই BST-র প্রাণভোমরা।

## Common mistake
- head ধরতে ভুলে যাওয়া (সবচেয়ে বাম node = head)।
- prev আর cur-এর দুই দিকের pointer (prev.next আর cur.prev) — একটা সেট করে অন্যটা ভুলে যাওয়া।

## Follow-up
- **circular DLL চাও** → শেষে head.prev = tail, tail.next = head জুড়ে দাও।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-13"></a>
# 17.13 — Re-Space

> Pattern: **DP + Trie / dictionary (word break with min unmatched)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a lengthy document. A sentence like "I reset the computer. It still didn't boot!" became "iresetthecomputeritstilldidntboot". Given a dictionary (a list of strings), design an algorithm to re-insert spaces into the document in a way that minimizes the number of unrecognized characters. Return the number of unrecognized characters.

## সমস্যাটা সহজ বাংলায়
সব space উড়ে গেছে। একটা dictionary দেওয়া আছে। string-এ আবার space বসিয়ে এমনভাবে শব্দ ভাগ করতে হবে যাতে **dictionary-তে নেই এমন অক্ষরের সংখ্যা সবচেয়ে কম** হয়। সেই সর্বনিম্ন সংখ্যাটা return করতে হবে।

## মূল insight — DP, প্রতিটা start থেকে best
`dp[i]` = `i` index থেকে শুরু করে বাকি string-এ সর্বনিম্ন কত unrecognized অক্ষর।

```
"jess looked just like tim her brother"  → "jesslookedjustliketimherbrother"

প্রতিটা position i থেকে:
  case A: index i-কে unrecognized ধরো → 1 + dp[i+1]
  case B: i থেকে শুরু কোনো dictionary-word w থাকলে → dp[i + len(w)]
dp[i] = এই সব option-এর minimum
```

right-to-left ভরি; `dp[n] = 0`।

```
i ───►  "j e s s l o o k e d ..."
        i থেকে "jess" dictionary-তে → dp[i] = dp[i+4]
        অথবা 'j' unrecognized → 1 + dp[i+1]
        min নাও
```

## ভাবনা ১: Brute Force
প্রতিটা position-এ space দেব কি দেব না — 2^n ভাগ। অসম্ভব।

## ভাবনা ২: DP + dictionary set
`dp[i]` right-to-left; প্রতি i-তে substring গুলো dictionary-তে আছে কিনা দেখি।

## ভাবনা ৩: DP + Trie
substring lookup দ্রুত করতে Trie — প্রতি start থেকে এক character করে trie-তে নেমে valid word খুঁজি, অপ্রয়োজনীয় substring বানানো বাঁচে।

## Code

```dart
// Dart — DP + dictionary set
int reSpace(String s, Set<String> dict) {
  final n = s.length;
  final dp = List<int>.filled(n + 1, 0);   // dp[n]=0
  for (int i = n - 1; i >= 0; i--) {
    dp[i] = 1 + dp[i + 1];                  // case A: i-কে unrecognized ধরি
    for (int j = i + 1; j <= n; j++) {      // case B: i..j-1 কোনো word?
      if (dict.contains(s.substring(i, j))) {
        if (dp[j] < dp[i]) dp[i] = dp[j];
      }
    }
  }
  return dp[0];
}
```
```python
# Python — DP + dictionary set
def re_space(s: str, dictionary: set) -> int:
    n = len(s)
    dp = [0] * (n + 1)        # dp[n] = 0
    for i in range(n - 1, -1, -1):
        dp[i] = 1 + dp[i + 1]               # case A: i unrecognized
        for j in range(i + 1, n + 1):       # case B: s[i:j] কোনো word?
            if s[i:j] in dictionary:
                dp[i] = min(dp[i], dp[j])
    return dp[0]
```
> বড় string + dictionary-তে substring বানানো O(n²) substring + lookup। **Trie** দিয়ে ভেতরের loop দ্রুত করা যায় (word-এর সর্বোচ্চ length পর্যন্ত)।

## Complexity
**Time: O(n²)** (set lookup সহ; Trie দিয়ে O(n·maxWordLen)) · **Space: O(n)** (dp)।

## Pattern চিনুন
> **"string ভেঙে dictionary word বানাও / word break" → DP (`dp[i]` = suffix-এর best), substring lookup-এ Trie।** "minimize unrecognized" = word break-এর optimization রূপ।

## Common mistake
- left-to-right/right-to-left দিক গুলিয়ে dp definition ভুল করা।
- প্রতিবার `substring` বানিয়ে O(n³)-এ পৌঁছানো (Trie বা early-break দিয়ে এড়ান)।

## Follow-up
- **আসল spaced string return করো** → dp-র সাথে choice track করে reconstruct করো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-14"></a>
# 17.14 — Smallest K

> Pattern: **Max-heap (size k) / Quickselect** · Difficulty: **Hard** · খুব common

> **বইয়ের ভাষায়:** Design an algorithm to find the smallest K numbers in an array.

## সমস্যাটা সহজ বাংলায়
একটা array থেকে সবচেয়ে ছোট **K**টা সংখ্যা বের করতে হবে (order জরুরি নয়, শুধু কোনগুলো)।

## ভাবনা ১: Sort করে প্রথম K
পুরোটা sort → প্রথম K নাও। O(n log n)। সহজ, কিন্তু পুরোটা sort করা অপচয়।

## ভাবনা ২: Max-heap of size K (O(n log K))
সর্বোচ্চ K element-এর একটা **max-heap** রাখি। নতুন element heap-এর top (সবচেয়ে বড়) থেকে ছোট হলে — top বের করে নতুনটা ঢোকাই। শেষে heap-এ থাকা K টাই smallest K।

```
heap সর্বদা k সাইজ, top = এই k-এর মধ্যে সবচেয়ে বড়
নতুন x আসে:
  heap size < k → ঢোকাও
  নাহলে x < top → top সরাও, x ঢোকাও   (top বড়, তাই বাদ)
```

## ভাবনা ৩: Quickselect (average O(n))
quicksort-এর partition দিয়ে K-th smallest-এর চারপাশে partition করি; বাঁ পাশের K টাই উত্তর। average O(n), worst O(n²)।

## Code

```dart
// Dart — max-heap of size k (SplayTreeMap/PriorityQueue থাকলে সহজ; এখানে list-heap)
import 'dart:collection';

List<int> smallestK(List<int> nums, int k) {
  if (k <= 0) return [];
  // PriorityQueue ডিফল্টে min-heap; max-heap পেতে comparator উল্টাই
  final maxHeap = PriorityQueue<int>((a, b) => b - a);
  for (final x in nums) {
    if (maxHeap.length < k) {
      maxHeap.add(x);
    } else if (x < maxHeap.first) {     // first = সবচেয়ে বড়
      maxHeap.removeFirst();
      maxHeap.add(x);
    }
  }
  return maxHeap.toList();
}
```
```python
# Python — max-heap (heapq min-heap, তাই value negate করি)
import heapq

def smallest_k(nums: list, k: int) -> list:
    if k <= 0:
        return []
    max_heap = []                       # ভেতরে -value রাখি
    for x in nums:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -x)
        elif x < -max_heap[0]:          # -heap[0] = বর্তমান সবচেয়ে বড়
            heapq.heapreplace(max_heap, -x)
    return [-v for v in max_heap]
```
```python
# Python — quickselect (average O(n))
import random
def smallest_k_quickselect(nums: list, k: int) -> list:
    nums = nums[:]
    def partition(lo, hi, pivot_idx):
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
        store = lo
        for i in range(lo, hi):
            if nums[i] < pivot:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[hi] = nums[hi], nums[store]
        return store
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        p = partition(lo, hi, random.randint(lo, hi))
        if p == k: break
        elif p < k: lo = p + 1
        else: hi = p - 1
    return nums[:k]
```

## Complexity
- Max-heap: **Time O(n log K)** · Space O(K)।
- Quickselect: **Time O(n) average** (worst O(n²)) · Space O(1)।

## Pattern চিনুন
> **"top/smallest K" → size-K heap (stream-friendly) অথবা quickselect (one-shot, দ্রুততম average)।** smallest K → **max**-heap; largest K → min-heap।

## Common mistake
- smallest K-র জন্য min-heap ব্যবহার (উল্টো — max-heap লাগে যাতে সবচেয়ে বড়টা বের করা যায়)।
- quickselect-এ random pivot না নিয়ে worst-case O(n²)-এ পড়া।

## Follow-up
- **stream / infinite data** → heap-ই উপযুক্ত (quickselect পুরো array চায়)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-15"></a>
# 17.15 — Longest Word

> Pattern: **Recursion + memo on dictionary (composed words)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Given a list of words, write a program to find the longest word made of other words in the list.

## সমস্যাটা সহজ বাংলায়
একটা word-list দেওয়া। এমন সবচেয়ে লম্বা word খুঁজতে হবে যা list-এর **অন্য word জোড়া দিয়ে** বানানো যায়। যেমন `["cat","banana","dog","nana","walk","walker","dogwalker"]` → `"dogwalker"` (dog+walker)।

## মূল insight — word break, কিন্তু নিজেকে বাদ দিয়ে
প্রতিটা word-এর জন্য check: এটা কি list-এর অন্য word দিয়ে গঠিত? এটা word-break (17.13-র আত্মীয়), শুধু পুরো word নিজে বাদ দিতে হবে।

```
ধাপ 1: লম্বা থেকে ছোট — length অনুযায়ী descending sort।
        (প্রথম যেটা composed পাবো সেটাই longest)
ধাপ 2: প্রতিটা word w-এর জন্য canBuild(w, নিজেকে বাদ দিয়ে):
        w-কে দুই ভাগে ভাগ করার সব জায়গা চেষ্টা করো;
        prefix dictionary-তে থাকলে, বাকি suffix recursively buildable?
```

## ভাবনা ১: Brute Force
প্রতিটা word-এর সব ভাগ — exponential। memo ছাড়া slow।

## ভাবনা ২: Sort + recursive canBuild + memo
length-desc sort করে প্রথম buildable word-ই উত্তর।

## Code

```dart
// Dart
String longestCompoundWord(List<String> words) {
  final dict = words.toSet();
  words.sort((a, b) => b.length - a.length);   // লম্বা আগে
  for (final w in words) {
    if (canBuild(w, true, dict)) return w;
  }
  return '';
}

bool canBuild(String w, bool isOriginal, Set<String> dict) {
  if (!isOriginal && dict.contains(w)) return true;
  for (int i = 1; i < w.length; i++) {
    final prefix = w.substring(0, i);
    if (dict.contains(prefix) && canBuild(w.substring(i), false, dict)) {
      return true;
    }
  }
  return false;
}
```
```python
# Python
def longest_compound_word(words: list) -> str:
    dictionary = set(words)
    words.sort(key=len, reverse=True)            # লম্বা আগে
    memo = {}
    def can_build(w, is_original):
        if w in memo and not is_original:
            return memo[w]
        if not is_original and w in dictionary:
            return True
        for i in range(1, len(w)):
            if w[:i] in dictionary and can_build(w[i:], False):
                memo[w] = True
                return True
        if not is_original:
            memo[w] = False
        return False
    for w in words:
        if can_build(w, True):
            return w
    return ''
```
> `isOriginal` flag-টা key: পুরো word নিজে dictionary-তে আছে বলেই "composed" নয় — অন্তত একবার ভাঙতে হবে।

## Complexity
**Time: ~O(n · L²)** (n word, প্রতিটা length L, memo সহ) · **Space: O(n + L)**।

## Pattern চিনুন
> **"অন্য word দিয়ে গঠিত / compound word" → word break recursion + memo, লম্বা আগে দেখার জন্য length-desc sort।**

## Common mistake
- পুরো word নিজেকেই একটা "অংশ" ধরে ভুলে true বলা (isOriginal flag দরকার)।
- memo না রেখে exponential হয়ে যাওয়া।

## Follow-up
- **সব compound word return করো** → প্রথমটায় না থেমে সব scan করো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-16"></a>
# 17.16 — The Masseuse

> Pattern: **DP (House Robber: no two adjacent)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. She needs a 15-minute break between appointments and therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appointment requests (all multiples of 15 minutes, none overlap, and none can be moved), find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.

## সমস্যাটা সহজ বাংলায়
পরপর কিছু appointment-এর সময় (minute) দেওয়া। দুটো **পাশাপাশি (adjacent)** appointment নেওয়া যাবে না (মাঝে break লাগে)। মোট minute সর্বোচ্চ করতে হলে কোন কোনগুলো নেবেন? — সেই max মান।

## মূল insight — এটাই classic "House Robber"
প্রতিটা i-তে দুই option: এই appointment **নাও** (তাহলে আগেরটা বাদ, i−2 থেকে best) অথবা **নিও না** (i−1 থেকে best)।

```
best[i] = max( nums[i] + best[i-2],   // নিলাম: i-2 পর্যন্ত best
               best[i-1] )            // নিলাম না: i-1 পর্যন্ত best
```

```
[30, 15, 60, 75, 45, 15, 15, 45]
চিন্তা: 30 + 60 + 45 + 45 ... ভেঙে ভেঙে best track করি → 180
```

দুটো রোলিং variable (`oneBack`, `twoBack`) দিয়ে O(1) space।

## ভাবনা ১: Brute Force (recursion)
প্রতিটা-তে নেব/নেব না — 2^n। memo ছাড়া slow।

## ভাবনা ২: DP (rolling, O(1) space)
উপরের recurrence iterative-এ।

## Code

```dart
// Dart — O(1) space DP
int maxMinutes(List<int> nums) {
  int oneBack = 0, twoBack = 0;   // best ending at i-1, i-2
  for (final x in nums) {
    final best = (twoBack + x) > oneBack ? (twoBack + x) : oneBack;
    twoBack = oneBack;
    oneBack = best;
  }
  return oneBack;
}
```
```python
# Python — O(1) space DP
def max_minutes(nums: list) -> int:
    one_back = two_back = 0     # best up to i-1, i-2
    for x in nums:
        best = max(two_back + x, one_back)
        two_back = one_back
        one_back = best
    return one_back
```

## Complexity
**Time: O(n)** · **Space: O(1)**।

## Pattern চিনুন
> **"পাশাপাশি দুটো একসাথে নেওয়া যাবে না, total max করো" → House Robber DP: `best[i]=max(nums[i]+best[i-2], best[i-1])`।** rolling দিয়ে O(1) space।

## Common mistake
- greedy (সবচেয়ে বড়টা আগে নাও) — ভুল উত্তর দেয়।
- `twoBack` আপডেটের ক্রম গুলিয়ে ফেলা।

## Follow-up
- **কোন appointment গুলো** চাই (শুধু sum নয়) → choice array রেখে back-track।
- **circular** (প্রথম+শেষ adjacent) → দুইবার চালাও (একবার প্রথম বাদ, একবার শেষ বাদ)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-17"></a>
# 17.17 — Multi Search

> Pattern: **Trie of patterns / suffix scan** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Given a string b and an array of smaller strings T, design a method to search b for each small string in T.

## সমস্যাটা সহজ বাংলায়
একটা বড় string `b` আর কতগুলো ছোট string `T` (pattern) দেওয়া। প্রতিটা pattern `b`-তে কোন কোন position-এ আছে — সব বের করতে হবে।

## ভাবনা ১: Brute Force
প্রতিটা pattern `b`-তে আলাদা খোঁজা — O(|T| · |b| · maxLen)। কাজ করে কিন্তু pattern বেশি হলে slow।

## ভাবনা ২: Trie of patterns + b-এর প্রতিটা suffix স্ক্যান
সব pattern দিয়ে একটা **Trie** বানাই। তারপর `b`-এর প্রতিটা index থেকে শুরু করে Trie ধরে যতদূর যায় নামি; পথে কোনো pattern-end পেলে — ওই pattern সেই index-এ পাওয়া গেল।

```
patterns: "is","ppi","hi","sip"
Trie:
  i-s*        (is)
  p-p-i*      (ppi)
  h-i*        (hi)
  s-i-p*      (sip)

b = "mississippi"
index 1: i→s*  → "is" at 1
index 4: i→s*  → "is" at 4
index 8: p→p→i* → "ppi" at 8 ...
```

প্রতিটা suffix-এ trie ধরে নামা = O(|b| · maxPatternLen)।

## Code

```dart
// Dart — Trie of patterns
class TrieNode {
  final Map<String, TrieNode> children = {};
  String? word;   // pattern শেষ হলে এখানে সেই pattern
}

Map<String, List<int>> multiSearch(String b, List<String> patterns) {
  final root = TrieNode();
  for (final p in patterns) {                 // Trie বানাই
    var node = root;
    for (final ch in p.split('')) {
      node = node.children.putIfAbsent(ch, () => TrieNode());
    }
    node.word = p;
  }
  final result = {for (final p in patterns) p: <int>[]};
  for (int i = 0; i < b.length; i++) {        // প্রতিটা suffix
    var node = root;
    int j = i;
    while (j < b.length && node.children.containsKey(b[j])) {
      node = node.children[b[j]]!;
      if (node.word != null) result[node.word!]!.add(i);
      j++;
    }
  }
  return result;
}
```
```python
# Python — Trie of patterns
def multi_search(b: str, patterns: list) -> dict:
    root = {}
    for p in patterns:                         # Trie বানাই
        node = root
        for ch in p:
            node = node.setdefault(ch, {})
        node['$'] = p                          # pattern-end marker
    result = {p: [] for p in patterns}
    for i in range(len(b)):                    # প্রতিটা suffix
        node = root
        j = i
        while j < len(b) and b[j] in node:
            node = node[b[j]]
            if '$' in node:
                result[node['$']].append(i)
            j += 1
    return result
```

## Complexity
**Time: O(Σ|pattern| + |b|·maxPatternLen)** (Trie build + scan) · **Space: O(Σ|pattern|)**।

## Pattern চিনুন
> **"অনেক pattern একসাথে এক text-এ খোঁজো (multi-pattern matching)" → সব pattern Trie-তে রেখে text-এর প্রতিটা suffix scan।** (পূর্ণ optimal = Aho-Corasick automaton।)

## Common mistake
- প্রতিটা pattern আলাদা search (Trie-র সুবিধা হারানো)।
- pattern-end marker না রাখা — তাহলে কোন node-এ pattern শেষ বোঝা যায় না।

## Follow-up
- **আরও দ্রুত / overlapping** → Aho-Corasick (Trie + failure link), O(|b| + matches)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-18"></a>
# 17.18 — Shortest Supersequence

> Pattern: **Sliding window (smallest covering window)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** You are given two arrays, one shorter (with all distinct elements) and one longer. Find the shortest subarray in the longer array that contains all the elements in the shorter array. The items can appear in any order. Return the start and end index.

## সমস্যাটা সহজ বাংলায়
একটা বড় array, আর একটা ছোট array (সব distinct element)। বড় array-তে সবচেয়ে ছোট এমন subarray খুঁজতে হবে যাতে ছোট array-র **সব element** (যেকোনো order-এ) আছে। সেই window-এর start, end index দাও।

## মূল insight — sliding window with count
দুটো pointer দিয়ে একটা window রাখি। ডান pointer এগিয়ে সব element cover করি; cover হলে বাঁ pointer এগিয়ে window ছোট করার চেষ্টা করি — সব cover থাকা অবস্থায় সবচেয়ে ছোট window রাখি।

```
need = {ছোট array-র element → কতটা লাগবে}
window-এ প্রতিটা element-এর count রাখি; "কতগুলো requirement মিটেছে" track করি।

right এগোও → নতুন element যোগ → requirement মিটলে count বাড়াও
সব মিটলে → left এগিয়ে window ছোট করো (requirement না ভেঙে), best রাখো
```

```
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
→ window [9,1,1,5] বা ছোটটা... index খুঁজে নিকটতম covering নাও
```

## ভাবনা ১: Brute Force
প্রতিটা start থেকে কত দূর গেলে সব cover হয় — O(n²) বা বেশি।

## ভাবনা ২: Sliding window (O(n))
উপরের two-pointer।

## Code

```dart
// Dart — sliding window
List<int> shortestSupersequence(List<int> big, List<int> small) {
  final need = <int, int>{};
  for (final x in small) need[x] = 1;          // distinct, তাই 1
  final window = <int, int>{};
  int required = need.length, formed = 0;
  int left = 0, bestLen = 1 << 30, bestL = -1, bestR = -1;
  for (int right = 0; right < big.length; right++) {
    final c = big[right];
    if (need.containsKey(c)) {
      window[c] = (window[c] ?? 0) + 1;
      if (window[c] == need[c]) formed++;
    }
    while (formed == required) {               // সব cover → ছোট করো
      if (right - left < bestLen) {
        bestLen = right - left; bestL = left; bestR = right;
      }
      final lc = big[left];
      if (need.containsKey(lc)) {
        window[lc] = window[lc]! - 1;
        if (window[lc]! < need[lc]!) formed--;
      }
      left++;
    }
  }
  return [bestL, bestR];
}
```
```python
# Python — sliding window
def shortest_supersequence(big: list, small: list) -> list:
    need = {x: 1 for x in small}
    window = {}
    required, formed = len(need), 0
    left = 0
    best_len, best = float('inf'), [-1, -1]
    for right, c in enumerate(big):
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                formed += 1
        while formed == required:               # সব cover → ছোট করো
            if right - left < best_len:
                best_len = right - left
                best = [left, right]
            lc = big[left]
            if lc in need:
                window[lc] -= 1
                if window[lc] < need[lc]:
                    formed -= 1
            left += 1
    return best
```

## Complexity
**Time: O(n)** (প্রতিটা element বড়জোর দুবার ছোঁয়া) · **Space: O(m)** (m = small-এর size)।

## Pattern চিনুন
> **"সব কিছু cover করে এমন সবচেয়ে ছোট window" → sliding window + count + formed/required।** ("minimum window substring" — হুবহু একই প্যাটার্ন।)

## Common mistake
- window ছোট করার সময় `formed` ঠিকমতো না কমানো।
- best update বাইরের loop-এ করা (cover-অবস্থায় ভেতরের `while`-এ করতে হবে)।

## Follow-up
- **small-এ duplicate থাকলে** → `need[x]` count রাখো (1 নয়), একই code কাজ করে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-19"></a>
# 17.19 — Missing Two

> Pattern: **Sum + sum-of-squares / XOR split** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** You are given an array with all the numbers from 1 to N appearing exactly once, except for one number that is missing. How can you find the missing number in O(N) time and O(1) space? What if there were two numbers missing?

## সমস্যাটা সহজ বাংলায়
`1..N` এর সব সংখ্যা ঠিক একবার করে আছে, কিন্তু **দুটো** missing। O(N) time, O(1) space-এ দুটোই বের করতে হবে।

## একটা missing হলে (সহজ)
`expected_sum − actual_sum` = missing। কিন্তু দুটো missing হলে একটা equation দুটো অজানা — তাই **দ্বিতীয় equation** লাগে।

## মূল insight — দুটো equation
ধরা যাক missing দুটো `a`, `b`।

```
equation 1:  a + b = S    (expected sum − actual sum)
equation 2:  a² + b² = Q  (expected sq-sum − actual sq-sum)

দুই equation থেকে:
  a + b = S
  a·b = (S² − Q) / 2          (কারণ (a+b)² = a²+b²+2ab)
→ এটা একটা quadratic; a,b = root দুটো।
```

## ভাবনা ২: XOR দিয়ে split (overflow-free)
সব XOR করলে `a XOR b` পাই। এর কোনো একটা set-bit ধরে সংখ্যাগুলোকে দুই দলে ভাগ করি (ওই bit 0/1)। প্রতিটা দলে ঠিক একটা missing — আলাদা XOR করে দুটো পাই। বড় N-এ overflow এড়ায়।

## Code

```dart
// Dart — sum + sum of squares
List<int> missingTwo(List<int> nums, int n) {
  int sum = 0, sqSum = 0;
  for (int i = 1; i <= n; i++) { sum += i; sqSum += i * i; }
  for (final x in nums) { sum -= x; sqSum -= x * x; }
  // sum = a+b, sqSum = a²+b²
  final s = sum;
  final prod = (s * s - sqSum) ~/ 2;     // a·b
  // a,b = quadratic root: t² - s t + prod = 0
  final disc = sqrtInt(s * s - 4 * prod);
  final a = (s + disc) ~/ 2;
  final b = s - a;
  return [a, b];
}

int sqrtInt(int x) {
  int r = 0;
  while ((r + 1) * (r + 1) <= x) r++;
  return r;
}
```
```python
# Python — sum + sum of squares
def missing_two(nums: list, n: int) -> list:
    s = sum(range(1, n + 1)) - sum(nums)            # a + b
    sq = sum(i * i for i in range(1, n + 1)) - sum(x * x for x in nums)  # a²+b²
    prod = (s * s - sq) // 2                          # a·b
    disc = int((s * s - 4 * prod) ** 0.5)
    a = (s + disc) // 2
    b = s - a
    return [a, b]
```
```python
# Python — XOR split (overflow-free বিকল্প)
def missing_two_xor(nums: list, n: int) -> list:
    xor_all = 0
    for i in range(1, n + 1): xor_all ^= i
    for x in nums: xor_all ^= x                       # = a ^ b
    bit = xor_all & (-xor_all)                        # সবচেয়ে ডানের set bit
    a = b = 0
    for i in range(1, n + 1):
        (a := a ^ i) if (i & bit) else (b := b ^ i)
    for x in nums:
        (a := a ^ x) if (x & bit) else (b := b ^ x)
    return [a, b]
```

## Complexity
**Time: O(N)** · **Space: O(1)**।

## Pattern চিনুন
> **"k টা missing/duplicate, O(1) space" → k টা independent equation (sum, sum-of-squares) অথবা XOR-bit দিয়ে দুই দলে ভাগ।** দুই অজানা = দুই equation।

## Common mistake
- একটাই equation দিয়ে দুটো অজানা solve করার চেষ্টা।
- sum-of-squares-এ বড় N-এ overflow (XOR version বা big-int দিয়ে এড়ান)।

## Follow-up
- **তিন বা তার বেশি missing** → sum-of-cubes... যোগ করতে হয়; বা bucket/marking ভিত্তিক approach।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-20"></a>
# 17.20 — Continuous Median

> Pattern: **Two heaps (max-heap + min-heap)** · Difficulty: **Hard** · খুব common

> **বইয়ের ভাষায়:** Numbers are randomly generated and passed to a method. Write a program to find and maintain the median value as new values are generated.

## সমস্যাটা সহজ বাংলায়
একের পর এক সংখ্যা আসছে (stream)। প্রতিবার নতুন সংখ্যা আসার পর **এখন পর্যন্ত সব সংখ্যার median** দ্রুত বলতে হবে।

## মূল insight — দুই heap-এ অর্ধেক অর্ধেক
ছোট অর্ধেক একটা **max-heap**-এ (top = ছোট অর্ধেকের সবচেয়ে বড়), বড় অর্ধেক একটা **min-heap**-এ (top = বড় অর্ধেকের সবচেয়ে ছোট)। median মাঝখানে — দুই top থেকে।

```
        max-heap (ছোট অর্ধেক)      min-heap (বড় অর্ধেক)
            ... 3 5 |               | 7 9 ...
                  ↑                   ↑
               top=5               top=7
size সমান → median = (5+7)/2
max-heap বড় → median = 5
```

balance নিয়ম: দুই heap-এর size-এর পার্থক্য বড়জোর 1। নতুন সংখ্যা সঠিক heap-এ ঢুকিয়ে দরকারে একটা element অন্য heap-এ সরাই।

## ভাবনা ১: Brute Force
প্রতিবার পুরোটা sort করে মাঝখান — O(n log n) প্রতি insert। slow।

## ভাবনা ২: Two heaps (O(log n) insert, O(1) median)
উপরের কাঠামো।

## Code

```dart
// Dart — two heaps
import 'dart:collection';

class MedianFinder {
  final maxHeap = PriorityQueue<int>((a, b) => b - a);  // ছোট অর্ধেক
  final minHeap = PriorityQueue<int>((a, b) => a - b);  // বড় অর্ধেক

  void add(int num) {
    if (maxHeap.isEmpty || num <= maxHeap.first) {
      maxHeap.add(num);
    } else {
      minHeap.add(num);
    }
    // rebalance: size পার্থক্য ≤ 1
    if (maxHeap.length > minHeap.length + 1) {
      minHeap.add(maxHeap.removeFirst());
    } else if (minHeap.length > maxHeap.length) {
      maxHeap.add(minHeap.removeFirst());
    }
  }

  double median() {
    if (maxHeap.length > minHeap.length) return maxHeap.first.toDouble();
    return (maxHeap.first + minHeap.first) / 2.0;
  }
}
```
```python
# Python — two heaps
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []   # ছোট অর্ধেক (negated for max behavior)
        self.min_heap = []   # বড় অর্ধেক

    def add(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        # rebalance
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
```

## Complexity
**Time: O(log n) প্রতি insert**, **O(1) median** · **Space: O(n)**।

## Pattern চিনুন
> **"running/streaming median" → দুই heap (max-heap ছোট অর্ধেক, min-heap বড় অর্ধেক), balance রাখো।** "stream-এ মাঝের element" শুনলেই two-heap।

## Common mistake
- rebalance ভুল (এক heap অন্যটার চেয়ে 2+ বড় হয়ে যাওয়া)।
- median-এ even/odd case ভুল (সমান size → দুই top-এর গড়)।

## Follow-up
- **k-th percentile চাও** → দুই heap-এর size ratio বদলে রাখো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-21"></a>
# 17.21 — Volume of Histogram

> Pattern: **Two pointer / precomputed max (trapping rain water)** · Difficulty: **Hard** · খুব common

> **বইয়ের ভাষায়:** Imagine a histogram (bar graph). Design an algorithm to compute the volume of water it could hold if someone poured water across the top. You can assume that each histogram bar has width 1.

## সমস্যাটা সহজ বাংলায়
কতগুলো bar-এর উচ্চতা দেওয়া (histogram)। উপর থেকে পানি ঢাললে দুই bar-এর মাঝের গর্তে কত পানি জমবে? (প্রতিটা bar-এর প্রস্থ 1)। এটাই বিখ্যাত "Trapping Rain Water"।

## মূল insight — প্রতিটা ঘরে জমা পানি
যেকোনো index `i`-তে পানির উচ্চতা = `min(বাঁ দিকের সর্বোচ্চ, ডান দিকের সর্বোচ্চ) − height[i]`। কারণ পানি দুই পাশের সবচেয়ে নিচু "দেয়াল" পর্যন্ত উঠতে পারে।

```
   █          █
   █~~~~█~~~~~█      ~ = জমা পানি
   █~~~~█~~█~~█
   █ ▓ █ █ ▓█ █
  height = [4,1,3,1,4]
  index2-তে: leftMax=4, rightMax=4 → min=4, height=3 → পানি=1
```

## ভাবনা ১: প্রতিটা i-তে দুই দিকে scan
প্রতি i-তে leftMax/rightMax খুঁজতে আবার scan — O(n²)।

## ভাবনা ২: Precompute leftMax[], rightMax[]
দুটো array-তে আগে থেকে leftMax, rightMax — O(n) time, O(n) space।

## ভাবনা ৩: Two pointer (O(n) time, O(1) space)
দুই pointer; যে পাশের max ছোট, সেই পাশ এগোই (কারণ ওই পাশের max-ই water সীমিত করে)।

## Code

```dart
// Dart — two pointer
int trap(List<int> height) {
  int l = 0, r = height.length - 1;
  int leftMax = 0, rightMax = 0, water = 0;
  while (l < r) {
    if (height[l] < height[r]) {
      leftMax = leftMax > height[l] ? leftMax : height[l];
      water += leftMax - height[l];      // বাঁ পাশ ছোট → বাঁ দিকেই জমা
      l++;
    } else {
      rightMax = rightMax > height[r] ? rightMax : height[r];
      water += rightMax - height[r];
      r--;
    }
  }
  return water;
}
```
```python
# Python — two pointer
def trap(height: list) -> int:
    l, r = 0, len(height) - 1
    left_max = right_max = water = 0
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]    # বাঁ পাশই সীমা
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1
    return water
```

## Complexity
**Time: O(n)** · **Space: O(1)** (two-pointer)।

## Pattern চিনুন
> **"trap water / দুই পাশের wall-এর min - height" → প্রতিটা ঘরে `min(leftMax,rightMax)-h`; two pointer-এ O(1) space।**

## Common mistake
- প্রতি ঘরে নতুন করে দুই দিকে scan (O(n²))।
- two-pointer-এ কোন পাশ এগোবে — ছোট max-এর পাশ — এটা ভুল করা।

## Follow-up
- **2D version (trapping rain water II)** → border থেকে min-heap দিয়ে ভেতরে এগোও।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-22"></a>
# 17.22 — Word Transformer

> Pattern: **BFS on word graph (word ladder)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Given two words of equal length that are in a dictionary, write a method to transform one word into another word by changing only one letter at a time. The new word you get in each step must be in the dictionary. Example: DAMP → LAMP → LIMP → LIME → LIKE।

## সমস্যাটা সহজ বাংলায়
দুটো সমান-length word (start, end) দেওয়া। একবারে **একটা অক্ষর** বদলে start থেকে end-এ যেতে হবে, আর প্রতিটা মধ্যবর্তী word dictionary-তে থাকতে হবে। এমন একটা পথ (transformation sequence) বের করো।

## মূল insight — এটা shortest-path / reachability graph
প্রতিটা word একটা node; দুই word-এর edge আছে যদি ঠিক **এক অক্ষরে** পার্থক্য। সবচেয়ে ছোট পথ = **BFS** (level-by-level)।

```
DAMP ─ LAMP ─ LIMP ─ LIME ─ LIKE
     1 অক্ষর  1 অক্ষর ...

BFS: start থেকে এক-অক্ষর-ভিন্ন word গুলো queue-তে; parent track করে পথ reconstruct।
```

## ভাবনা ১: DFS
যেকোনো একটা পথ পেলেই চলে; কিন্তু shortest নয়, আর cycle সামলাতে visited লাগে।

## ভাবনা ২: BFS (shortest path)
parent map রেখে শেষে path reconstruct। প্রতিবেশী খোঁজার দুই উপায়: (ক) প্রতিটা word-এর প্রতিটা position-এ a–z বসিয়ে dictionary-তে আছে কিনা; (খ) সব pair compare (slow)।

## Code

```dart
// Dart — BFS
import 'dart:collection';

List<String> transform(String start, String end, Set<String> dict) {
  final queue = Queue<String>()..add(start);
  final parent = <String, String?>{start: null};
  while (queue.isNotEmpty) {
    final word = queue.removeFirst();
    if (word == end) {
      final path = <String>[];
      String? w = end;
      while (w != null) { path.add(w); w = parent[w]; }
      return path.reversed.toList();
    }
    for (int i = 0; i < word.length; i++) {       // প্রতিটা position
      for (int c = 0; c < 26; c++) {              // প্রতিটা অক্ষর
        final ch = String.fromCharCode('a'.codeUnitAt(0) + c);
        if (ch == word[i]) continue;
        final next = word.substring(0, i) + ch + word.substring(i + 1);
        if (dict.contains(next) && !parent.containsKey(next)) {
          parent[next] = word;
          queue.add(next);
        }
      }
    }
  }
  return [];   // পথ নেই
}
```
```python
# Python — BFS
from collections import deque

def transform(start: str, end: str, dictionary: set) -> list:
    queue = deque([start])
    parent = {start: None}
    while queue:
        word = queue.popleft()
        if word == end:
            path = []
            w = end
            while w is not None:
                path.append(w)
                w = parent[w]
            return path[::-1]
        for i in range(len(word)):                 # প্রতিটা position
            for c in 'abcdefghijklmnopqrstuvwxyz':  # প্রতিটা অক্ষর
                if c == word[i]:
                    continue
                nxt = word[:i] + c + word[i+1:]
                if nxt in dictionary and nxt not in parent:
                    parent[nxt] = word
                    queue.append(nxt)
    return []   # পথ নেই
```

## Complexity
**Time: O(W · L · 26)** (W = word সংখ্যা, L = length) · **Space: O(W)**।

## Pattern চিনুন
> **"এক ধাপে এক বদল, valid state-এ থাকতে হবে, shortest path" → BFS on state graph (word ladder)।** প্রতিবেশী = এক অক্ষর বদলে valid word।

## Common mistake
- DFS দিয়ে shortest দাবি করা (DFS shortest দেয় না)।
- visited/parent না রাখা → infinite loop বা পুনরাবৃত্তি।

## Follow-up
- **দুই দিক থেকে BFS (bidirectional)** → অনেক দ্রুত (search space কমে)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-23"></a>
# 17.23 — Max Black Square

> Pattern: **DP (precompute contiguous runs) + border check** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Imagine you have a square matrix, where each cell (pixel) is either black or white. Design an algorithm to find the maximum subsquare such that all four borders are filled with black pixels.

## সমস্যাটা সহজ বাংলায়
একটা square matrix, প্রতিটা ঘর কালো বা সাদা। এমন সবচেয়ে বড় subsquare খুঁজতে হবে যার **চার বাহু (border)** পুরো কালো (ভেতরটা যেকোনো রঙ)।

## মূল insight — প্রতিটা ঘর থেকে ডানে/নিচে কত কালো টানা
naive-এ প্রতিটা square-এর চার border চেক করা ব্যয়বহুল। তাই আগে precompute করি: প্রতিটা ঘর থেকে **ডান দিকে** আর **নিচের দিকে** পরপর কতগুলো কালো।

```
right[i][j] = (i,j) থেকে ডানে টানা কালো সংখ্যা
below[i][j] = (i,j) থেকে নিচে টানা কালো সংখ্যা

একটা size-s square-এর top-left (i,j) হলে border কালো কিনা:
  উপরের বাহু: right[i][j]   >= s
  বাঁ বাহু:   below[i][j]   >= s
  ডান বাহু:   below[i][j+s-1] >= s
  নিচের বাহু: right[i+s-1][j] >= s
```

বড় size থেকে ছোট দিকে দেখি; প্রথম যেটা মেলে সেটাই সর্বোচ্চ।

## ভাবনা ১: Brute Force
প্রতিটা square-এর প্রতিটা border-cell চেক — O(n⁴) বা O(n⁵)।

## ভাবনা ২: Precompute right/below (O(n³))
border চেক O(1)-এ নেমে আসে।

## Code

```dart
// Dart — true = কালো
List<int> maxBlackSquare(List<List<bool>> m) {
  final n = m.length;
  final right = List.generate(n, (_) => List<int>.filled(n, 0));
  final below = List.generate(n, (_) => List<int>.filled(n, 0));
  for (int i = n - 1; i >= 0; i--) {
    for (int j = n - 1; j >= 0; j--) {
      if (m[i][j]) {
        right[i][j] = 1 + (j + 1 < n ? right[i][j + 1] : 0);
        below[i][j] = 1 + (i + 1 < n ? below[i + 1][j] : 0);
      }
    }
  }
  for (int size = n; size >= 1; size--) {              // বড় থেকে ছোট
    for (int i = 0; i + size <= n; i++) {
      for (int j = 0; j + size <= n; j++) {
        if (right[i][j] >= size &&
            below[i][j] >= size &&
            right[i + size - 1][j] >= size &&
            below[i][j + size - 1] >= size) {
          return [i, j, size];                          // top, left, size
        }
      }
    }
  }
  return [];
}
```
```python
# Python — True = কালো
def max_black_square(m: list) -> list:
    n = len(m)
    right = [[0] * n for _ in range(n)]
    below = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if m[i][j]:
                right[i][j] = 1 + (right[i][j + 1] if j + 1 < n else 0)
                below[i][j] = 1 + (below[i + 1][j] if i + 1 < n else 0)
    for size in range(n, 0, -1):                 # বড় থেকে ছোট
        for i in range(n - size + 1):
            for j in range(n - size + 1):
                if (right[i][j] >= size and below[i][j] >= size and
                        right[i + size - 1][j] >= size and
                        below[i][j + size - 1] >= size):
                    return [i, j, size]            # top, left, size
    return []
```

## Complexity
**Time: O(n³)** (precompute O(n²) + size×position scan O(n³)) · **Space: O(n²)**।

## Pattern চিনুন
> **"matrix-এ border condition সহ সর্বোচ্চ square" → precompute directional runs (right/below), তারপর border O(1)-এ চেক।** runs precompute = DP-র সরল রূপ।

## Common mistake
- border চেকে শুধু দুই বাহু (top+left) দেখা, ডান/নিচ বাদ দেওয়া।
- size-loop বড় থেকে ছোট না করা (প্রথম hit-ই largest পেতে)।

## Follow-up
- **পুরো ভরা (filled) square, শুধু border নয়** → 2D prefix sum দিয়ে area চেক।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-24"></a>
# 17.24 — Max Submatrix

> Pattern: **2D → 1D max-subarray (Kadane) row-pair compression** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Given an NxM matrix of positive and negative integers, write code to find the submatrix with the largest possible sum.

## সমস্যাটা সহজ বাংলায়
একটা matrix-এ ধনাত্মক ও ঋণাত্মক সংখ্যা। এমন একটা rectangular submatrix খুঁজতে হবে যার সব element-এর **যোগফল সর্বোচ্চ**।

## মূল insight — দুটো row fix করে 1D Kadane
এক মাত্রায় (1D array) max-sum subarray = **Kadane's algorithm** (O(n))। 2D-তে: প্রতিটা জোড়া row (top, bottom) fix করি, এর মাঝের column গুলো যোগ করে একটা 1D array বানাই — তাতে Kadane চালাই।

```
top, bottom row জোড়া fix:
  colSum[c] = top..bottom row-এর c-th column-এর যোগফল
  → এই 1D colSum-এ Kadane = ওই row-band-এর best submatrix

সব (top,bottom) জোড়ার মধ্যে সর্বোচ্চ = উত্তর
```

```
row জোড়া O(N²), প্রতি জোড়ায় column compress O(M) + Kadane O(M)
→ মোট O(N² · M)
```

## ভাবনা ১: Brute Force
সব সম্ভাব্য submatrix (চারটা সীমা) — O(N²M²) area sum সহ O(N³M³)। ভয়াবহ।

## ভাবনা ২: Row-pair + Kadane (O(N²·M))
উপরের কৌশল। (Kadane = Chapter 16-এর contiguous-sum-এর 2D সম্প্রসারণ।)

## Code

```dart
// Dart
int maxSubmatrixSum(List<List<int>> matrix) {
  final rows = matrix.length, cols = matrix[0].length;
  int best = -1 << 62;
  for (int top = 0; top < rows; top++) {
    final colSum = List<int>.filled(cols, 0);
    for (int bottom = top; bottom < rows; bottom++) {
      for (int c = 0; c < cols; c++) colSum[c] += matrix[bottom][c]; // band যোগ
      best = best > kadane(colSum) ? best : kadane(colSum);          // 1D best
    }
  }
  return best;
}

int kadane(List<int> a) {
  int best = a[0], cur = a[0];
  for (int i = 1; i < a.length; i++) {
    cur = (a[i] > cur + a[i]) ? a[i] : cur + a[i];   // নতুন শুরু বা চালিয়ে যাওয়া
    if (cur > best) best = cur;
  }
  return best;
}
```
```python
# Python
def max_submatrix_sum(matrix: list) -> int:
    rows, cols = len(matrix), len(matrix[0])
    best = float('-inf')
    for top in range(rows):
        col_sum = [0] * cols
        for bottom in range(top, rows):
            for c in range(cols):
                col_sum[c] += matrix[bottom][c]      # band যোগ
            best = max(best, kadane(col_sum))         # 1D best
    return best

def kadane(a: list) -> int:
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)        # নতুন শুরু বা চালিয়ে যাওয়া
        best = max(best, cur)
    return best
```

## Complexity
**Time: O(N²·M)** (row জোড়া × Kadane) · **Space: O(M)** (colSum)।

## Pattern চিনুন
> **"2D max-sum submatrix" → row জোড়া fix করে column compress, তারপর 1D Kadane।** 2D problem-কে 1D-তে নামানো — খুব শক্তিশালী technique।

## Common mistake
- প্রতি (top,bottom)-এ colSum আবার শূন্য থেকে গোনা (top fix রেখে bottom বাড়ালে incrementally যোগ করাই O(M))।
- সব negative হলে Kadane যেন 0 না দেয় (best = a[0] দিয়ে শুরু করা জরুরি)।

## Follow-up
- **submatrix-এর coordinate** চাও → Kadane-এ start/end index track করো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-25"></a>
# 17.25 — Word Rectangle

> Pattern: **Trie + backtracking (build column-by-column)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Given a list of millions of words, design an algorithm to create the largest possible rectangle of letters such that every row forms a word (reading left to right) and every column forms a word (reading top to bottom). The words need not be chosen from the same length group, but each row must be the same length and each column must be the same length.

## সমস্যাটা সহজ বাংলায়
অনেক word দেওয়া। অক্ষর দিয়ে সবচেয়ে বড় rectangle বানাতে হবে যেখানে **প্রতিটা row একটা word** আর **প্রতিটা column-ও একটা word**। সব row সমান length, সব column সমান length (rectangle তো)।

## মূল insight — row যোগ করো, Trie দিয়ে column বৈধতা যাচাই
নির্দিষ্ট প্রস্থ (width W) ও উচ্চতা (height H) ধরে নিই। W-length word একটা একটা করে row হিসেবে যোগ করি। প্রতিবার যোগের পর **প্রতিটা column যেন কোনো word-এর valid prefix থাকে** — এটা H-length word-দের একটা **Trie** দিয়ে চেক করি। কোনো column-এর prefix invalid হলে সেই branch ছেঁটে ফেলি (prune)।

```
words length-অনুযায়ী group করি।
সবচেয়ে বড় area আগে চেষ্টা করি (length descending pair)।

           c0 c1 c2          c0,c1,c2 প্রতিটা column =
row0:  →   d  o  g           H-length word-এর valid prefix?
row1:  →   o  v  e           না হলে এই row বাদ দাও (backtrack)
...
সব column পূর্ণ word হলে → rectangle পাওয়া গেল
```

Trie দিয়ে "এই partial column কি কোনো word-এর prefix" — O(1)-ish চেক, বিশাল search-space ছাঁটে।

## ভাবনা ১: Brute Force
সব W×H অক্ষর-সমাবেশ — astronomically বড়। অসম্ভব।

## ভাবনা ২: Trie + backtracking, area-descending
বড় area আগে; column-prefix Trie দিয়ে prune।

## Code (মূল কাঠামো; পুরো million-word optimize বাদ দিয়ে core)

```dart
// Dart — সরলীকৃত core (এক নির্দিষ্ট width-এ rectangle খোঁজা)
class TrieNode {
  final Map<String, TrieNode> children = {};
  bool isWord = false;
}
TrieNode buildTrie(List<String> words) {
  final root = TrieNode();
  for (final w in words) {
    var n = root;
    for (final ch in w.split('')) {
      n = n.children.putIfAbsent(ch, () => TrieNode());
    }
    n.isWord = true;
  }
  return root;
}
// isPrefix: column-এ এ পর্যন্ত যা আছে তা কোনো word-এর prefix কিনা
bool isPrefix(TrieNode root, String s) {
  var n = root;
  for (final ch in s.split('')) {
    final c = n.children[ch];
    if (c == null) return false;
    n = c;
  }
  return true;
}

List<String>? makeRectangle(
    List<String> rowWords, TrieNode colTrie, int height) {
  final rect = <String>[];
  bool build() {
    if (rect.length == height) {
      // সব column পূর্ণ word হতে হবে
      for (int c = 0; c < rect[0].length; c++) {
        final col = [for (final r in rect) r[c]].join();
        if (!_isWord(colTrie, col)) return false;
      }
      return true;
    }
    for (final w in rowWords) {
      rect.add(w);
      // প্রতিটা column এখনো valid prefix?
      bool ok = true;
      for (int c = 0; c < w.length && ok; c++) {
        final col = [for (final r in rect) r[c]].join();
        if (!isPrefix(colTrie, col)) ok = false;
      }
      if (ok && build()) return true;
      rect.removeLast();   // backtrack
    }
    return false;
  }
  return build() ? List.of(rect) : null;
}
bool _isWord(TrieNode root, String s) {
  var n = root;
  for (final ch in s.split('')) {
    final c = n.children[ch];
    if (c == null) return false;
    n = c;
  }
  return n.isWord;
}
```
```python
# Python — সরলীকৃত core
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

def build_trie(words):
    root = TrieNode()
    for w in words:
        n = root
        for ch in w:
            n = n.children.setdefault(ch, TrieNode())
        n.is_word = True
    return root

def is_prefix(root, s):
    n = root
    for ch in s:
        n = n.children.get(ch)
        if n is None:
            return False
    return True

def is_word(root, s):
    n = root
    for ch in s:
        n = n.children.get(ch)
        if n is None:
            return False
    return n.is_word

def make_rectangle(row_words, col_trie, height):
    rect = []
    def build():
        if len(rect) == height:
            for c in range(len(rect[0])):           # সব column পূর্ণ word?
                col = ''.join(r[c] for r in rect)
                if not is_word(col_trie, col):
                    return False
            return True
        for w in row_words:
            rect.append(w)
            ok = all(is_prefix(col_trie, ''.join(r[c] for r in rect))
                     for c in range(len(w)))        # column prefix valid?
            if ok and build():
                return True
            rect.pop()                              # backtrack
        return False
    return list(rect) if build() else None
```

## Complexity
worst-case exponential, কিন্তু Trie-prune বাস্তবে বিশাল কমায়। বাইরে **area-descending** iteration দিয়ে প্রথম সফল rectangle = largest।

## Pattern চিনুন
> **"row ও column দুটোই word হতে হবে / 2D word constraint" → row একটা একটা যোগ করো, column-prefix Trie দিয়ে prune (backtracking)।**

## Common mistake
- column-prefix চেক না করে শেষ পর্যন্ত যাওয়া (exponential blow-up)।
- partial column-কে পূর্ণ word ধরে চেক করা (prefix vs word গুলিয়ে ফেলা)।

## Follow-up
- **largest area নিশ্চিত করতে** → length জোড়াগুলো area-descending sort করে প্রথম সফলটাতেই থামো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q17-26"></a>
# 17.26 — Sparse Similarity

> Pattern: **Inverted index (only shared elements)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** The similarity of two documents (each with distinct words) is defined to be the size of the intersection divided by the size of the union. For example, if the documents consist of integers, the similarity of {1,5,3} and {1,7,2,3} is 0.4, because the intersection has size 2 and the union has size 5. We have a long list of documents (with distinct values and each with an associated ID) where the similarity is believed to be "sparse" (most pairs have similarity 0). Design an algorithm that returns a list of pairs of document IDs and the associated similarity, printing only the pairs with similarity greater than 0.

## সমস্যাটা সহজ বাংলায়
অনেক document, প্রতিটায় distinct integer-এর set। দুই document-এর similarity = `|intersection| / |union|` (Jaccard)। বেশিরভাগ জোড়ার similarity 0 (sparse)। শুধু **similarity > 0** জোড়াগুলো বের করতে হবে — দক্ষভাবে।

## মূল insight — element → কোন কোন document, inverted index
সব জোড়া তুলনা করলে O(D²)। কিন্তু similarity > 0 মানে অন্তত **একটা common element**। তাই উল্টো ভাবি: প্রতিটা element কোন কোন document-এ আছে (**inverted index**)। একই element-এর document-জোড়াগুলোই কেবল intersection share করে।

```
element → [doc ids]
  1 → [A, B]
  3 → [A, B]
  5 → [A]
  7 → [B]

element 1: A,B জোড়ার intersection +1
element 3: A,B জোড়ার intersection +1
→ intersection(A,B) = 2,  union = |A|+|B|-2,  similarity = 2/union
```

কোনো element একাধিক doc-এ থাকলেই তবে কাজ; sparse হলে এই জোড়ার সংখ্যা ছোট থাকে।

## ভাবনা ১: Brute Force
সব জোড়া (D²) তুলনা, প্রতিটায় set intersection — O(D² · avgSize)। sparse হলে অপচয়।

## ভাবনা ২: Inverted index → শুধু shared element-এর জোড়া
প্রতিটা element-এর document-list থেকে জোড়া বানিয়ে intersection-count জমাই; শেষে union হিসাব করে similarity।

## Code

```dart
// Dart
Map<String, double> sparseSimilarity(Map<int, Set<int>> docs) {
  // element → কোন কোন doc-এ আছে
  final inverted = <int, List<int>>{};
  docs.forEach((docId, words) {
    for (final w in words) {
      inverted.putIfAbsent(w, () => []).add(docId);
    }
  });
  // doc-জোড়া → কতগুলো common element
  final pairCount = <String, int>{};
  for (final docList in inverted.values) {
    for (int i = 0; i < docList.length; i++) {
      for (int j = i + 1; j < docList.length; j++) {
        var a = docList[i], b = docList[j];
        if (a > b) { final t = a; a = b; b = t; }
        final key = '$a,$b';
        pairCount[key] = (pairCount[key] ?? 0) + 1;
      }
    }
  }
  // similarity = intersection / union
  final result = <String, double>{};
  pairCount.forEach((key, inter) {
    final parts = key.split(',');
    final a = int.parse(parts[0]), b = int.parse(parts[1]);
    final union = docs[a]!.length + docs[b]!.length - inter;
    result[key] = inter / union;
  });
  return result;
}
```
```python
# Python
def sparse_similarity(docs: dict) -> dict:
    inverted = {}                                  # element → [doc ids]
    for doc_id, words in docs.items():
        for w in words:
            inverted.setdefault(w, []).append(doc_id)

    pair_count = {}                                # (a,b) → common element সংখ্যা
    for doc_list in inverted.values():
        for i in range(len(doc_list)):
            for j in range(i + 1, len(doc_list)):
                a, b = sorted((doc_list[i], doc_list[j]))
                pair_count[(a, b)] = pair_count.get((a, b), 0) + 1

    result = {}
    for (a, b), inter in pair_count.items():
        union = len(docs[a]) + len(docs[b]) - inter
        result[(a, b)] = inter / union
    return result
```

## Complexity
**Time: O(Σ pairs per shared element)** — sparse হলে D²-এর চেয়ে অনেক কম · **Space: O(সব জোড়া যাদের common আছে)**।

## Pattern চিনুন
> **"sparse intersection / similarity, বেশিরভাগ জোড়া 0" → inverted index (element→docs), শুধু shared element-এর document-জোড়া প্রক্রিয়া করো।** D² জোড়া এড়াও।

## Common mistake
- সব D² জোড়া তুলনা করা (sparsity-র সুবিধা হারানো)।
- union-এ intersection দুবার গোনা (`|A|+|B|−inter` করতে হবে)।

## Follow-up
- **খুব বড় data** → MinHash / LSH দিয়ে আনুমানিক similarity, অথবা distributed (MapReduce) inverted index।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---
---

# Chapter 17 — সারসংক্ষেপ ও Pattern Cheat Sheet

| # | প্রশ্ন | মূল technique | Time | Space |
|---|---|---|---|---|
| 17.1 | Add Without Plus | Bit: XOR sum + AND<<1 carry | O(1) | O(1) |
| 17.2 | Shuffle | Fisher-Yates | O(n) | O(1) |
| 17.3 | Random Set | Reservoir sampling | O(n) | O(m) |
| 17.4 | Missing Number | Bit-by-bit divide | O(n) | O(n) |
| 17.5 | Letters and Numbers | Prefix sum + hash | O(n) | O(n) |
| 17.6 | Count of 2s | Place-value counting | O(log n) | O(1) |
| 17.7 | Baby Names | Union-Find | ~O(N+P) | O(N) |
| 17.8 | Circus Tower | Sort + LIS | O(n²) | O(n) |
| 17.9 | Kth Multiple | Three-pointer merge | O(k) | O(k) |
| 17.10 | Majority Element | Boyer-Moore voting | O(n) | O(1) |
| 17.11 | Word Distance | One-pass / preprocess index | O(n) | O(1)/O(n) |
| 17.12 | BiNode | In-order → DLL | O(n) | O(h) |
| 17.13 | Re-Space | DP + Trie (word break) | O(n²) | O(n) |
| 17.14 | Smallest K | Max-heap / Quickselect | O(n log K)/O(n) | O(K)/O(1) |
| 17.15 | Longest Word | Word break recursion + memo | O(n·L²) | O(n) |
| 17.16 | The Masseuse | House Robber DP | O(n) | O(1) |
| 17.17 | Multi Search | Trie of patterns | O(Σp + b·L) | O(Σp) |
| 17.18 | Shortest Supersequence | Sliding window | O(n) | O(m) |
| 17.19 | Missing Two | Sum + sq-sum / XOR split | O(n) | O(1) |
| 17.20 | Continuous Median | Two heaps | O(log n) ins | O(n) |
| 17.21 | Volume of Histogram | Two pointer (trap water) | O(n) | O(1) |
| 17.22 | Word Transformer | BFS (word ladder) | O(W·L·26) | O(W) |
| 17.23 | Max Black Square | Precompute runs + border | O(n³) | O(n²) |
| 17.24 | Max Submatrix | Row-pair + Kadane | O(N²·M) | O(M) |
| 17.25 | Word Rectangle | Trie + backtracking | exp (pruned) | O(words) |
| 17.26 | Sparse Similarity | Inverted index | O(shared pairs) | O(pairs) |

### "এটা দেখলে → এটা ভাবো" (signal → technique)
```
arithmetic ছাড়া যোগ / carry           →  Bit: XOR + AND<<1
uniform shuffle / random m থেকে n      →  Fisher-Yates / Reservoir sampling
bit-only access, missing               →  bit-by-bit divide
সমান count longest subarray            →  +1/-1 prefix sum + hash
0..n-এ digit গোনা                       →  place-value counting
equivalent / transitive group          →  Union-Find
দুই dimension-এ nesting/বাড়া            →  sort একটা + LIS অন্যটা
prime factor শুধু কয়েকটা / ugly number  →  multi-pointer merge / min-heap
অর্ধেকের বেশি, O(1) space               →  Boyer-Moore voting
বহুবার query একই data-তে                →  preprocess / index
BST → sorted sequence/DLL              →  in-order traversal
string ভেঙে dictionary word            →  word break DP (+Trie)
top/smallest K                          →  size-K heap / quickselect
পাশাপাশি নেওয়া যাবে না, max             →  House Robber DP
অনেক pattern এক text-এ                  →  Trie / Aho-Corasick
সব cover করা সবচেয়ে ছোট window          →  sliding window
k টা missing, O(1) space                →  k equation (sum, sq-sum) / XOR
streaming median                        →  two heaps
trap water / দুই পাশের min wall         →  two pointer
এক বদলে এক ধাপ, shortest                 →  BFS on state graph
matrix border square                    →  precompute right/below runs
2D max-sum submatrix                    →  row-pair compress + Kadane
row+column দুটোই word                   →  Trie + backtracking
sparse similarity, বেশিরভাগ 0           →  inverted index
```

### এই chapter-এর ৫টা সোনার নিয়ম
1. **Hard = চেনা technique-এর combination।** problem দেখে আগে জিজ্ঞেস করুন — "এটা কোন পরিচিত problem-এর ছদ্মবেশ?"
2. **2D-কে 1D-তে নামান।** Circus Tower (LIS), Max Submatrix (Kadane) — dimension কমানো বারবার কাজে লাগে।
3. **Preprocess করুন।** বহু query, repeated lookup, prefix-check — index/Trie/prefix-sum আগে বানিয়ে রাখলে পরে সস্তা।
4. **Heap, Union-Find, Trie, BFS** — এই চারটা structure hard chapter-এর মেরুদণ্ড; চিনতে শিখুন কখন কোনটা।
5. **Bit tricks** (XOR cancel, AND carry, bit-split) ছোট কিন্তু শক্তিশালী — O(1) space-এর দরজা খোলে।

---

## অভিনন্দন — পুরো guide শেষ!

আপনি Cracking the Coding Interview-এর সব ১৮৯টা প্রশ্নের বাংলা গাইড শেষ করেছেন — array/string থেকে শুরু করে এই hard chapter পর্যন্ত। মনে রাখবেন: এই বইয়ের আসল শিক্ষা মুখস্থ solution নয়, বরং **pattern চেনা** — "এই signal দেখলে এই technique"। প্রতিটা chapter-এর শেষের cheat sheet গুলো বারবার চোখ বুলিয়ে নিন; interview-র আগে ওগুলোই দ্রুত revision-এর সবচেয়ে ভালো হাতিয়ার।

**পরের ধাপ:**
- চেনা pattern গুলো নতুন problem-এ নিজে নিজে লাগিয়ে দেখুন (LeetCode/HackerRank)।
- mock interview দিন — Listen → Brute → Optimize → Code → Test ধাপ জোরে জোরে বলে practice করুন।
- দুর্বল লাগে এমন chapter (DP, graph, bit) আলাদা করে গভীরভাবে ঝালিয়ে নিন।

শুভকামনা — আপনার interview দারুণ হোক!

> [মূল Index](README.md)

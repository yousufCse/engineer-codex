# Chapter 1 — Arrays & Strings (প্রশ্ন 1.1 – 1.9)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। Code **Dart + Python** দুটোতেই।
> 👉 এই chapter শুরুর আগে [Chapter 0 — Foundation](chapter00_foundation.md) (Big-O + 7-step) পড়ে নিন।

---

## এই chapter-এ কী শিখব

```
A. আগে background (অবশ্যই পড়ুন): Array, Dynamic Array, String, Hash Table
B. তারপর ৯টা প্রশ্ন:
   1.1  Is Unique          — সব character unique কিনা
   1.2  Check Permutation  — একটা string আরেকটার permutation কিনা
   1.3  URLify             — space কে %20 দিয়ে বদলানো
   1.4  Palindrome Perm.   — palindrome বানানো যায় এমন permutation আছে কিনা
   1.5  One Away           — একটা edit-এ দুটো string সমান কিনা
   1.6  String Compression — aaabb → a3b2
   1.7  Rotate Matrix      — ছবি ৯০° ঘোরানো
   1.8  Zero Matrix        — 0 পেলে পুরো row+column 0
   1.9  String Rotation    — একটা string আরেকটার rotation কিনা
```

প্রতিটা প্রশ্ন এই কাঠামোয়: **সহজ বাংলায় সমস্যা → উদাহরণ → Listen → Brute force → Optimize → Code (Dart+Python) → Complexity → Pattern → Common mistake → Follow-up।**

---
---

# 📚 Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

## ১. Array আসলে কী? (memory-তে কীভাবে থাকে)

Array হলো **একটানা (contiguous) memory**-তে পাশাপাশি বসানো কতগুলো ঘর। প্রতিটা ঘরের একটা **index** (ঠিকানা) আছে, শুরু হয় `0` থেকে।

```
Index :   0     1     2     3     4
        ┌─────┬─────┬─────┬─────┬─────┐
Value : │ 10  │ 20  │ 30  │ 40  │ 50  │
        └─────┴─────┴─────┴─────┴─────┘
          ↑
   memory address: 1000  1004  1008 ... (পরপর, ৪ byte করে int হলে)
```

**কেন `arr[3]`-এ যাওয়া O(1)?**
কম্পিউটার সরাসরি হিসাব করে: `address = শুরুর address + (index × প্রতিটা element-এর size)`। তাই যেকোনো index-এ **এক লাফে** পৌঁছায় — খুঁজতে হয় না। এজন্যই array-তে index access সবচেয়ে দ্রুত (**O(1)**)।

কিন্তু মাঝখানে insert/delete করলে বাকি সবাইকে সরাতে হয় → **O(n)**।

## ২. Static vs Dynamic Array

| | Static array | Dynamic array |
|---|---|---|
| size | শুরুতেই fixed | নিজে নিজে বাড়ে |
| উদাহরণ | C-এর `int[5]` | **Dart `List`**, **Python `list`**, Java `ArrayList` |

Dynamic array ভরে গেলে **double size**-এর নতুন array বানিয়ে সব copy করে (একবার O(n))। কিন্তু গড়ে প্রতিটা add **amortized O(1)** (Chapter 0-এ ব্যাখ্যা করা আছে)।

## ৩. String — আসলে character-এর array

`"hello"` মানে `['h','e','l','l','o']`। বেশিরভাগ ভাষায় (Dart, Python, Java) **string immutable** — মানে একবার বানালে আর বদলানো যায় না।

```dart
String s = "abc";
s = s + "d";   // নতুন string "abcd" বানায়, পুরোনোটা বদলায় না
```

**কেন এটা জরুরি?** loop-এ বারবার string জোড়া দিলে প্রতিবার নতুন string copy হয় → **O(n²)** হয়ে যায়! এর সমাধান StringBuilder ↓

## ৪. StringBuilder / StringBuffer — string জোড়ার সঠিক উপায়

বারবার string জোড়া দিতে হলে একটা পরিবর্তনযোগ্য buffer-এ জমিয়ে শেষে একবার string বানান:

```dart
// Dart — StringBuffer
final sb = StringBuffer();
for (int i = 0; i < 1000; i++) sb.write('x');
String result = sb.toString();   // পুরোটা O(n)
```
```python
# Python — list-এ জমিয়ে join (StringBuilder-এর সমতুল্য)
parts = []
for i in range(1000):
    parts.append('x')
result = ''.join(parts)          # পুরোটা O(n)
```
> 🔑 **নিয়ম:** loop-এ string জোড়া = StringBuilder/`join` ব্যবহার করুন, নইলে O(n²)।

## ৫. Hash Table (Map / Set) — এই chapter-এর সবচেয়ে দরকারি tool

Hash Table এমন একটা structure যেখানে **add, খোঁজা, মুছে ফেলা — গড়ে সব O(1)**। কীভাবে?

```
key "apple"  ──hash()──►  3   ──►  bucket[3]-এ রাখা হলো
              (একটা function key কে একটা index বানায়)

খুঁজতে: "apple" ──hash()──► 3 ──► সরাসরি bucket[3] দেখো  (O(1))
```

দুই রকম:
- **Set** — শুধু "এই জিনিসটা আছে কিনা" রাখে (duplicate রাখে না)। `{1, 2, 3}`
- **Map / Dictionary** — key → value জোড়া রাখে। `{"a": 1, "b": 2}`

```dart
// Dart
final seen = <String>{};        // Set
seen.add("apple");
seen.contains("apple");          // true, O(1)

final count = <String, int>{};  // Map
count["apple"] = 5;
```
```python
# Python
seen = set()
seen.add("apple")
"apple" in seen                  # True, O(1)

count = {}
count["apple"] = 5
```
> 🔑 **Pattern:** "duplicate আছে?", "আগে দেখেছি?", "কতবার আছে?" — এসব দেখলেই **Hash Set/Map** মাথায় আনুন।

---
---

# 1.1 — Is Unique

> Pattern: **Hash Set / Bit Vector** · Difficulty: **Easy** · 🔥 খুব common (warm-up প্রশ্ন)

> **বইয়ের ভাষায়:** Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

## 🔹 সমস্যাটা সহজ বাংলায়
একটা string দেওয়া আছে। বলতে হবে এর **সব character আলাদা (unique)** কিনা — অর্থাৎ কোনো character **দুইবার** আছে কিনা। আর একটা extra চ্যালেঞ্জ: **কোনো extra data structure ব্যবহার না করে** করতে পারবেন?

## 🔹 উদাহরণ

```
"abcde"  →  true    (সব আলাদা)
"hello"  →  false   ('l' দুইবার আছে)
            h e l l o
                ↑ ↑
              এখানে repeat
```

## 🔹 ধাপ ১: Listen (clarifying questions)
Interview-তে কোডের আগে এই প্রশ্নগুলো করুন — এতেই আপনি ভালো candidate মনে হবেন:
- **Character set কী?** শুধু lowercase `a-z`? নাকি পুরো ASCII (১২৮ character)? নাকি Unicode? → এটা solution বদলে দেয়।
- **Case-sensitive?** `'A'` আর `'a'` কি আলাদা ধরব?

ধরে নিচ্ছি: **ASCII (১২৮ character), case-sensitive।**

## 🔹 ভাবনা ১: Brute Force — প্রতিটা character বাকি সবার সাথে মেলাও

প্রতিটা character নিয়ে তার পরের সব character-এর সাথে মিলিয়ে দেখি কোনোটা সমান কিনা।

```
"hello":
  h কে মেলাও → e,l,l,o  (মিল নেই)
  e কে মেলাও → l,l,o    (মিল নেই)
  l কে মেলাও → l,o      → 'l'=='l' পাওয়া গেল! → false
```
- **Time: O(n²)** (প্রতিটা character × বাকি সব) · **Space: O(1)**
- কাজ করে, কিন্তু ধীর। BUD দিয়ে দেখি — এখানে **duplicated work**: একই character বারবার মেলাচ্ছি।

## 🔹 ভাবনা ২: Sort করে পাশাপাশি দেখা

Sort করলে একই character পাশাপাশি চলে আসে। তখন শুধু পরপর দুটো সমান কিনা দেখলেই হয়।

```
"hello" → sort → "ehllo"
                    ↑↑
              পাশাপাশি 'l','l' → false
```
- **Time: O(n log n)** (sort-এর জন্য) · **Space: O(1)** যদি in-place sort
- Brute force-এর চেয়ে ভালো, কিন্তু আরও ভালো করা যায়।

## 🔹 ভাবনা ৩: Hash Set — ✅ optimal time

একটা Set-এ দেখা character জমাই। নতুন character আসলে — আগে দেখেছি কিনা চেক করি। দেখে থাকলে duplicate → `false`।

```
seen = { }
h → seen-এ নেই → যোগ করো → {h}
e → নেই → {h,e}
l → নেই → {h,e,l}
l → আছে! ──────────────► return false
```
- **Time: O(n)** (প্রতিটা character একবার) · **Space: O(n)** (Set-এ জমা)
- "space দিয়ে time কিনলাম" — classic optimization।

## 🔹 ভাবনা ৪: Bit Vector — ✅ O(1) space ("extra data structure ছাড়া")

যদি শুধু lowercase `a-z` হয়, তাহলে Set-এর বদলে একটা **integer-এর bit** দিয়ে কাজ চালানো যায় — ২৬টা bit, প্রতিটা একটা অক্ষরের জন্য। এটাই বইয়ের "extra data structure ছাড়া" অংশের উত্তর।

```
'a'=bit0, 'b'=bit1, ... একটা character দেখলে তার bit 1 করি।
আবার সেই bit আগে থেকে 1 থাকলে → duplicate!

  checker:  0 0 0 1 0 0 1   ('a' আর 'd' দেখা হয়েছে)
                  ↑     ↑
                 'd'   'a'
```
- **Time: O(n)** · **Space: O(1)** (মাত্র একটা int!)

## 🔹 আরেকটা সহজ যুক্তি (early exit)
ASCII ১২৮ character। string-এর length যদি **১২৮-এর বেশি** হয়, তাহলে pigeonhole principle অনুযায়ী অবশ্যই কোনো character repeat — সাথে সাথে `false`! এই check টা শুরুতে রাখা ভালো।

## 🔹 Code — Hash Set (সবচেয়ে practical উত্তর)

```dart
// Dart
bool isUnique(String s) {
  if (s.length > 128) return false;        // ASCII early exit
  final seen = <String>{};
  for (final ch in s.split('')) {
    if (seen.contains(ch)) return false;   // আগে দেখেছি → duplicate
    seen.add(ch);
  }
  return true;
}
```
```python
# Python
def is_unique(s: str) -> bool:
    if len(s) > 128:          # ASCII early exit
        return False
    seen = set()
    for ch in s:
        if ch in seen:        # আগে দেখেছি → duplicate
            return False
        seen.add(ch)
    return True
```

## 🔹 Code — Bit Vector (O(1) space, শুধু a-z)

```dart
// Dart — extra data structure ছাড়া
bool isUniqueBits(String s) {
  int checker = 0;
  for (final ch in s.codeUnits) {
    final bit = 1 << (ch - 'a'.codeUnitAt(0));   // এই অক্ষরের bit
    if ((checker & bit) != 0) return false;       // bit আগেই 1 → duplicate
    checker |= bit;                               // bit 1 করো
  }
  return true;
}
```
```python
# Python
def is_unique_bits(s: str) -> bool:
    checker = 0
    for ch in s:
        bit = 1 << (ord(ch) - ord('a'))    # এই অক্ষরের bit
        if checker & bit:                  # bit আগেই 1 → duplicate
            return False
        checker |= bit                     # bit 1 করো
    return True
```

## 🔹 সব approach-এর তুলনা

| Approach | Time | Space | কখন ব্যবহার |
|---|---|---|---|
| Brute force (সব pair) | O(n²) | O(1) | শুধু শুরুর ধারণা হিসেবে বলবেন |
| Sort + পাশাপাশি | O(n log n) | O(1)* | input বদলানো গেলে |
| **Hash Set** | **O(n)** | O(n) | ✅ সাধারণ/safe উত্তর |
| **Bit Vector** | **O(n)** | **O(1)** | ✅ "no extra DS", শুধু a-z |

`*` in-place sort হলে

## 🔹 Pattern চিনুন
> **"unique / duplicate / আগে দেখেছি কিনা" দেখলেই → Hash Set।** আর character set ছোট ও fixed (যেমন a-z) হলে → **Bit Vector**-এ space O(1) করা যায়।

## 🔹 Common mistake (junior শোনায়)
- ❌ Character set জিজ্ঞেস না করেই code শুরু করা (ASCII না Unicode — এটাই প্রথম প্রশ্ন)।
- ❌ Bit vector solution-কে "no extra data structure" বললেও আসলে int-ও তো memory — তবে এটা O(1), constant space, তাই গ্রহণযোগ্য।
- ❌ length > 128 early-exit মিস করা (ছোট কিন্তু interviewer খুশি হয়)।

## 🔹 Follow-up প্রশ্ন (interviewer এরপর যা জিজ্ঞেস করতে পারে)
- **"extra data structure ছাড়া করো"** → Bit vector, অথবা in-place sort করে পাশাপাশি check (O(n log n), O(1) space)।
- **"Unicode হলে?"** → ১২৮ নয়, অনেক বড় range; Hash Set-ই নিরাপদ, bit vector অবাস্তব।
- **"case-insensitive হলে?"** → আগে `toLowerCase()` করে নিন।

---

# 1.2 — Check Permutation

> Pattern: **Frequency Count / Sort** · Difficulty: **Easy** · 🔥 খুব common

> **বইয়ের ভাষায়:** Given two strings, write a method to decide if one is a permutation of the other.

## 🔹 সমস্যাটা সহজ বাংলায়
দুটো string দেওয়া। বলতে হবে একটা কি আরেকটার **permutation** — অর্থাৎ **একই character গুলো, শুধু সাজানো (order) আলাদা**।

## 🔹 উদাহরণ
```
"abc" & "bca"  →  true    (একই অক্ষর, শুধু order ভিন্ন)
"abc" & "abd"  →  false   ('c' নেই, 'd' আছে)
"abc" & "ab"   →  false   (length-ই আলাদা)
```

## 🔹 ধাপ ১: Listen
- **Case-sensitive?** (`'A'` ≠ `'a'`?)
- **Whitespace গোনা হবে?** ("god " কি "dog"-এর permutation?)
- ধরছি: case-sensitive, whitespace গোনা হবে, ASCII।

## 🔹 মূল insight
Permutation হতে হলে দুটো শর্ত:
1. দুটোর **length সমান** হতে হবে (নাহলে সাথে সাথে `false`)।
2. প্রতিটা character-এর **count সমান** হতে হবে।

## 🔹 ভাবনা ১: Sort করে মেলাও
দুটো string sort করলে permutation হলে তারা **হুবহু সমান** হবে।
```
"bca" → sort → "abc"
"abc" → sort → "abc"   →  সমান  →  true
```
- **Time: O(n log n)** · **Space: O(n)** (sort-এর জন্য)। সহজ, লেখা যায় ১ লাইনে।

## 🔹 ভাবনা ২: Frequency Count — ✅ optimal
একটা Map-এ s1-এর প্রতিটা character গুনি, তারপর s2-এর জন্য কমাই। কোনোটা negative হলে বা শেষে অমিল থাকলে → `false`।
```
a = "abc"  →  count = {a:1, b:1, c:1}
b = "bca"  →  b:1→0, c:1→0, a:1→0  →  সব 0  →  true
```
- **Time: O(n)** · **Space: O(c)** (c = আলাদা character সংখ্যা)।

## 🔹 Code

```dart
// Dart — frequency count
bool isPermutation(String a, String b) {
  if (a.length != b.length) return false;      // ১ম শর্ত
  final counts = <String, int>{};
  for (final ch in a.split('')) {
    counts[ch] = (counts[ch] ?? 0) + 1;        // s1 গুনি
  }
  for (final ch in b.split('')) {
    final c = (counts[ch] ?? 0) - 1;           // s2 দিয়ে কমাই
    if (c < 0) return false;                    // s2-তে বেশি আছে
    counts[ch] = c;
  }
  return true;
}
```
```python
# Python — frequency count
from collections import Counter

def is_permutation(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)   # Counter = ready-made frequency map
```
> 💡 Python-এ `Counter` দিয়ে এক লাইনেই হয়; Dart-এ নিজে Map ব্যবহার করতে হয়।

## 🔹 তুলনা
| Approach | Time | Space |
|---|---|---|
| Sort + compare | O(n log n) | O(n) |
| **Frequency count** | **O(n)** | O(c) |

## 🔹 Pattern চিনুন
> **"permutation / anagram / একই অক্ষর reorder" দেখলেই → Frequency Count (অথবা sort করে মেলাও)।** এটাই anagram-জাতীয় সব problem-এর চাবি।

## 🔹 Common mistake
- ❌ আগে **length compare** না করা (খুব সহজ early-exit মিস)।
- ❌ Whitespace/case নিয়ে clarify না করা।

## 🔹 Follow-up
- **Anagram group বানাও** (Chapter-এ পরে আসবে) → sorted string কে Map-এর key বানান।

---
---

# 1.3 — URLify

> Pattern: **In-place edit (পিছন থেকে), Two Pointer** · Difficulty: **Easy–Medium** · Common

> **বইয়ের ভাষায়:** Write a method to replace all spaces in a string with `'%20'`. You may assume the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
> Example: `"Mr John Smith    "`, 13 → `"Mr%20John%20Smith"`

## 🔹 সমস্যাটা সহজ বাংলায়
String-এর প্রতিটা **space** কে `"%20"` দিয়ে বদলাতে হবে। ধরা আছে — array-র **শেষে যথেষ্ট খালি জায়গা** দেওয়া আছে (কারণ ১টা space=১ অক্ষর, কিন্তু `%20`=৩ অক্ষর, তাই প্রতি space-এ +২ ঘর লাগে), আর আসল লেখার দৈর্ঘ্য (**true length**) আলাদা করে দেওয়া আছে।

## 🔹 কেন এটা একটু tricky?
String **immutable** (Dart/Python দুটোতেই), তাই আমরা একটা **character array (list)** নিয়ে কাজ করি। আর আসল চালাকি: **সামনে থেকে লিখলে** যে অক্ষরগুলো এখনো process করিনি, সেগুলোর ওপর লিখে ফেলব (overwrite)। তাই **পিছন থেকে সামনের দিকে** লিখি।

## 🔹 উদাহরণ (পিছন থেকে ভরা)
```
true length = 13  →  শুধু "Mr John Smith" আসল
buffer:  M r _ J o h n _ S m i t h _ _ _ _    (শেষে ৪টা extra ঘর: ২ space × ২)
index:   0 1 2 3 4 5 6 7 8 9 ...        16

পিছন থেকে লিখি (write-pointer j = 16):
result:  M r % 2 0 J o h n % 2 0 S m i t h
```

## 🔹 ধাপে ধাপে approach
1. true length-এর মধ্যে কতগুলো space আছে গুনি (`spaceCount`)।
2. নতুন শেষ index = `trueLength + 2 × spaceCount − 1`।
3. আসল লেখার শেষ থেকে শুরুর দিকে যাই:
   - space পেলে → পিছন থেকে `0`, `2`, `%` বসাই (write-pointer ৩ কমাই)।
   - সাধারণ অক্ষর হলে → সেটাই বসাই (write-pointer ১ কমাই)।

## 🔹 Code
```dart
// Dart — character list-এ in-place
List<String> urlify(List<String> chars, int trueLength) {
  int spaceCount = 0;
  for (int i = 0; i < trueLength; i++) {
    if (chars[i] == ' ') spaceCount++;
  }
  int j = trueLength + 2 * spaceCount - 1;     // নতুন শেষ index
  for (int i = trueLength - 1; i >= 0; i--) {  // পিছন থেকে সামনে
    if (chars[i] == ' ') {
      chars[j] = '0'; chars[j - 1] = '2'; chars[j - 2] = '%';
      j -= 3;
    } else {
      chars[j] = chars[i];
      j -= 1;
    }
  }
  return chars;
}
```
```python
# Python — list of chars (string immutable বলে)
def urlify(chars: list, true_length: int) -> list:
    space_count = sum(1 for i in range(true_length) if chars[i] == ' ')
    j = true_length + 2 * space_count - 1        # নতুন শেষ index
    for i in range(true_length - 1, -1, -1):     # পিছন থেকে সামনে
        if chars[i] == ' ':
            chars[j], chars[j-1], chars[j-2] = '0', '2', '%'
            j -= 3
        else:
            chars[j] = chars[i]
            j -= 1
    return chars
```

## 🔹 Complexity
**Time: O(n)** (প্রতি অক্ষর একবার) · **Space: O(1)** (একই array-তে, নতুন কিছু বানাইনি)।

## 🔹 Pattern চিনুন
> **In-place array edit যেখানে size বাড়ছে → পিছন থেকে (back-to-front) লিখুন।** এতে unprocessed data overwrite হয় না। এটা অনেক array problem-এ কাজে লাগে।

## 🔹 Common mistake
- ❌ **সামনে থেকে** লেখা → পরের অক্ষরগুলো নষ্ট হয়ে যায়।
- ❌ `trueLength` আর buffer length গুলিয়ে ফেলা।

## 🔹 Follow-up
- **যথেষ্ট জায়গা না থাকলে?** → নতুন array allocate করতে হবে (in-place সম্ভব নয়)।

---
---

# 1.4 — Palindrome Permutation

> Pattern: **Frequency Count / Bit Vector** · Difficulty: **Easy–Medium** · Common

> **বইয়ের ভাষায়:** Given a string, write a function to check if it is a permutation of a palindrome. Example: `"Tact Coa"` → `true` (`"taco cat"`).

## 🔹 সমস্যাটা সহজ বাংলায়
একটা string-এর অক্ষরগুলো **এমনভাবে সাজানো যায় কিনা যাতে palindrome হয়** (সামনে-পিছনে একই)। আসল string palindrome হওয়া লাগবে না — শুধু **সাজিয়ে** palindrome বানানো সম্ভব কিনা।

## 🔹 মূল insight (সবচেয়ে দামি অংশ)
Palindrome-এ অক্ষরগুলো **জোড়ায় জোড়ায়** থাকে (যেমন `racecar`-এ `r,a,c` দুপাশে আয়নার মতো)। মাঝখানে বড়জোর **একটা** অক্ষর একা থাকতে পারে (বিজোড় length হলে)।
> ✅ **নিয়ম:** একটা string কে palindrome-এ সাজানো যায় **যদি ও কেবল যদি — বড়জোর একটা character-এর count বিজোড় (odd) হয়।**

## 🔹 উদাহরণ
```
"tactcoa"  (space বাদ, lowercase):
  t:2  a:2  c:2  o:1
            ↑ মাত্র একটা odd (o)  →  true  ("tacocat")

"aabbc"  →  a:2 b:2 c:1  →  একটা odd  →  true
"aabbcd" →  c:1 d:1      →  দুটো odd   →  false
```

## 🔹 ভাবনা ১: Count করে odd গোনা
প্রতিটা character গুনে দেখি কয়টার count odd। odd-এর সংখ্যা **≤ 1** হলে `true`।
- **Time: O(n)** · **Space: O(c)**।

## 🔹 ভাবনা ২: Bit Vector toggle (চালাক, O(1) space-ish)
Count রাখার বদলে প্রতিটা character দেখলে তার bit **toggle** (XOR) করি। জোড়া হলে bit আবার 0 হয়ে যাবে। শেষে যদি **০ বা মাত্র ১টা bit** 1 থাকে → palindrome সম্ভব।
```
bit আগে 0 → অক্ষর একবার এলে 1 → আবার এলে 0 (জোড়া মিলে গেল)
শেষে কয়টা bit 1 আছে = কয়টা অক্ষরের count odd
```

## 🔹 Code
```dart
// Dart — count approach
bool isPalindromePermutation(String s) {
  s = s.replaceAll(' ', '').toLowerCase();
  final counts = <String, int>{};
  for (final ch in s.split('')) {
    counts[ch] = (counts[ch] ?? 0) + 1;
  }
  int odd = 0;
  for (final c in counts.values) {
    if (c.isOdd) odd++;
  }
  return odd <= 1;
}
```
```python
# Python — count approach
from collections import Counter

def is_palindrome_permutation(s: str) -> bool:
    s = s.replace(' ', '').lower()
    counts = Counter(s)
    odd = sum(1 for c in counts.values() if c % 2 == 1)
    return odd <= 1
```
```python
# Python — bit vector toggle (bonus)
def is_palindrome_permutation_bits(s: str) -> bool:
    bits = 0
    for ch in s.lower():
        if ch == ' ':
            continue
        bits ^= 1 << (ord(ch) - ord('a'))   # toggle
    return (bits & (bits - 1)) == 0          # ০ বা ১টা bit set?
```
> 🧠 `bits & (bits - 1) == 0` কৌশলটা চেক করে "বড়জোর একটা bit 1 আছে কিনা" — খুব common bit trick (Chapter 5-এ বিস্তারিত)।

## 🔹 Complexity
**Time: O(n)** · **Space: O(c)** (count) বা **O(1)** (bit vector, ছোট alphabet)।

## 🔹 Pattern চিনুন
> **"palindrome বানানো যায় কিনা" → অক্ষর count করো, odd-count ≤ 1 কিনা দেখো।** Permutation generate করার দরকার **নেই** — এটাই ফাঁদ।

## 🔹 Common mistake
- ❌ সব permutation বানিয়ে চেক করা (O(n!) — ভয়াবহ ধীর, একদম দরকার নেই)।
- ❌ space/case handle না করা (example-এ `"Tact Coa"` দেখেই বোঝা যায় ignore করতে হবে)।

## 🔹 Follow-up
- **odd-count rule কেন কাজ করে — প্রমাণ করো** → palindrome-এ প্রতিটা অক্ষর mirror জোড়ায়, একমাত্র মাঝেরটা একা থাকতে পারে।

---
---

# 1.5 — One Away

> Pattern: **Two Pointer (এক mismatch allow)** · Difficulty: **Medium** · 🔥 common

> **বইয়ের ভাষায়:** Three edits: insert, remove, or replace a character. Given two strings, check if they are one (or zero) edits away.
> `pale, ple → true` · `pales, pale → true` · `pale, bale → true` · `pale, bake → false`

## 🔹 সমস্যাটা সহজ বাংলায়
তিন রকম edit করা যায়: একটা অক্ষর **যোগ** (insert), একটা **মুছে ফেলা** (remove), একটা **বদলানো** (replace)। বলতে হবে — দুটো string কে **০ বা ১টা edit**-এ সমান করা যায় কিনা।

## 🔹 মূল insight — তিনটা edit আসলে দুটো case
```
length সমান     →  শুধু "replace" সম্ভব  →  বড়জোর ১টা অক্ষর আলাদা?
length ১ ভিন্ন  →  "insert/remove" সম্ভব →  ছোটটা বড়টার মধ্যে ১টা অক্ষর বাদে মেলে?
length ≥২ ভিন্ন →  অসম্ভব               →  false
```
Insert আর remove আসলে **একই জিনিস উল্টো দিক থেকে** — তাই আলাদা করে ভাবার দরকার নেই।

## 🔹 উদাহরণ (pointer চলা)
```
"pale" vs "ple"   (length 4 vs 3 → insert/remove case)
 p a l e
 p l e
 ↑ p==p, এগোও
   a≠l → এখানে 'a' বাদ দিলে মেলে? শুধু বড়টার pointer এগোও
   l==l, e==e  →  ১টা edit  →  true
```

## 🔹 ধাপে ধাপে approach
1. length-এর পার্থক্য > 1 হলে → `false`।
2. ছোট ও বড় string আলাদা করি, দুটো pointer দিয়ে একসাথে হাঁটি।
3. মিল না হলে: একটা "difference" পেলাম —
   - length সমান হলে দুটো pointer-ই এগোই (replace)।
   - নাহলে শুধু বড় string-এর pointer এগোই (insert/remove)।
4. **দ্বিতীয়বার** mismatch হলে → `false`।

## 🔹 Code
```dart
// Dart
bool oneAway(String a, String b) {
  if ((a.length - b.length).abs() > 1) return false;
  final shorter = a.length < b.length ? a : b;
  final longer  = a.length < b.length ? b : a;
  int i = 0, j = 0;
  bool foundDiff = false;
  while (i < shorter.length && j < longer.length) {
    if (shorter[i] != longer[j]) {
      if (foundDiff) return false;             // ২য় বার mismatch
      foundDiff = true;
      if (shorter.length == longer.length) i++; // replace: দুটোই এগোও
    } else {
      i++;
    }
    j++;                                        // বড়টার pointer সবসময় এগোয়
  }
  return true;
}
```
```python
# Python
def one_away(a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
        return False
    shorter, longer = (a, b) if len(a) < len(b) else (b, a)
    i = j = 0
    found_diff = False
    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            if found_diff:
                return False
            found_diff = True
            if len(shorter) == len(longer):   # replace
                i += 1
        else:
            i += 1
        j += 1                                # longer-এর pointer সবসময় এগোয়
    return True
```

## 🔹 Complexity
**Time: O(n)** · **Space: O(1)**।

## 🔹 Pattern চিনুন
> **"এক edit / পার্থক্য বড়জোর ১" → Two Pointer, একটা mismatch পর্যন্ত সহ্য করো।** এটা পুরো "Edit Distance" (Chapter 8 DP) সমস্যার ছোট/সহজ রূপ।

## 🔹 Common mistake
- ❌ insert, remove, replace — তিনটা আলাদা করে জটিল code লেখা (একসাথে handle করাই পরিষ্কার)।
- ❌ length-পার্থক্য > 1 early-exit মিস করা।

## 🔹 Follow-up
- **যেকোনো সংখ্যক edit-এ minimum কত লাগবে?** → Edit Distance / Levenshtein, DP দিয়ে (Chapter 8)।

---
---

# 1.6 — String Compression

> Pattern: **Run-Length Encoding + StringBuilder** · Difficulty: **Easy–Medium** · Common

> **বইয়ের ভাষায়:** Compress using counts of repeated characters: `aabcccccaaa` → `a2b1c5a3`. If the "compressed" string is not smaller than the original, return the original. Assume only `a-z`.

## 🔹 সমস্যাটা সহজ বাংলায়
পরপর একই অক্ষর কতবার আছে গুনে `অক্ষর+সংখ্যা` লিখতে হবে। compressed version যদি original-এর চেয়ে **ছোট না হয়**, তাহলে original-ই ফেরত দাও।

## 🔹 উদাহরণ
```
"aabcccccaaa"  →  a2 b1 c5 a3  →  "a2b1c5a3"   (length 8 < 11  →  ভালো, এটাই দাও)
"abc"          →  a1 b1 c1     →  "a1b1c1"      (length 6 > 3  →  original "abc" দাও)
```

## 🔹 ⚠️ সবচেয়ে গুরুত্বপূর্ণ সতর্কতা — StringBuilder ব্যবহার করুন
Loop-এর ভেতর `result = result + ...` করলে প্রতিবার নতুন string copy হয় → পুরোটা **O(n²)**! তাই **StringBuilder** (Dart `StringBuffer`, Python `list` + `join`) ব্যবহার করুন। (Background section দেখুন।)

## 🔹 ধাপে ধাপে approach
একবার হেঁটে যাই, একটা `count` রাখি। পরের অক্ষর আলাদা হলে (বা string শেষ হলে) → buffer-এ `অক্ষর + count` লিখি, count রিসেট করি। শেষে compressed ছোট হলে সেটা, নাহলে original দাও।

## 🔹 Code
```dart
// Dart
String compress(String s) {
  final sb = StringBuffer();
  int count = 0;
  for (int i = 0; i < s.length; i++) {
    count++;
    // পরের অক্ষর আলাদা, অথবা এটাই শেষ → run শেষ, লিখে ফেলো
    if (i + 1 == s.length || s[i] != s[i + 1]) {
      sb.write(s[i]);
      sb.write(count);
      count = 0;
    }
  }
  final compressed = sb.toString();
  return compressed.length < s.length ? compressed : s;
}
```
```python
# Python
def compress(s: str) -> str:
    parts = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i + 1 == len(s) or s[i] != s[i + 1]:   # run শেষ
            parts.append(s[i])
            parts.append(str(count))
            count = 0
    compressed = ''.join(parts)
    return compressed if len(compressed) < len(s) else s
```

## 🔹 Complexity
**Time: O(n)** · **Space: O(n)** (buffer)। StringBuilder ব্যবহার না করলে time O(n²) হয়ে যেত।

## 🔹 Pattern চিনুন
> **"পরপর একই জিনিস গোনা / run-length encoding" → single pass + counter + StringBuilder।**

## 🔹 Common mistake
- ❌ Loop-এ string concatenation (O(n²))।
- ❌ **শেষ run** লিখতে ভুলে যাওয়া (loop শেষে বাকি count handle করা)।
- ❌ "ছোট না হলে original দাও" শর্ত ভুলে যাওয়া।

## 🔹 Follow-up
- **আগে compressed length হিসাব করে নাও** (O(n)), ছোট হলে তবেই buffer বানাও — অপ্রয়োজনীয় কাজ বাঁচে।

---
---

# 1.7 — Rotate Matrix

> Pattern: **Matrix layer-by-layer in-place rotation** · Difficulty: **Medium** · 🔥 খুব common

> **বইয়ের ভাষায়:** Given an image as an N×N matrix (4 bytes/pixel), rotate it 90 degrees. Can you do it **in place**?

## 🔹 সমস্যাটা সহজ বাংলায়
একটা **N×N matrix** (ছবি) **৯০° ঘোরাতে** হবে। চ্যালেঞ্জ: **extra matrix না বানিয়ে**, একই matrix-এর ভেতরেই (in place)।

## 🔹 উদাহরণ
```
original         90° clockwise ঘোরালে
1 2 3            7 4 1
4 5 6     →      8 5 2
7 8 9            9 6 3

(প্রথম column "1 4 7" উপরের row হয়ে গেল → "7 4 1" উল্টো করে)
```

## 🔹 ভাবনা ১: নতুন matrix (সহজ কিন্তু extra space)
`new[j][N-1-i] = old[i][j]` — O(n²) time, **O(n²) space**। কাজ করে, কিন্তু "in place" শর্ত মানে না।

## 🔹 ভাবনা ২: Layer-by-layer in-place — ✅
Matrix-কে **স্তরে স্তরে (ring/layer)** ভাবি — বাইরের ring, তারপর ভেতরের। প্রতিটা ring-এ ৪টা পাশ আছে; এদের একসাথে **৪-মুখী swap** করি: top→right→bottom→left→top।
```
        top (→)
     ┌───────────┐
left │           │ right
 (↑) │           │ (↓)
     └───────────┘
       bottom (←)

একটা temp-এ top রাখো, তারপর:
 top   ← left
 left  ← bottom
 bottom← right
 right ← temp(top)
```

## 🔹 Code
```dart
// Dart — in-place, O(1) space
void rotate(List<List<int>> matrix) {
  final n = matrix.length;
  for (int layer = 0; layer < n ~/ 2; layer++) {
    final first = layer, last = n - 1 - layer;
    for (int i = first; i < last; i++) {
      final offset = i - first;
      final top = matrix[first][i];                          // top রাখো
      matrix[first][i] = matrix[last - offset][first];        // left → top
      matrix[last - offset][first] = matrix[last][last - offset]; // bottom → left
      matrix[last][last - offset] = matrix[i][last];          // right → bottom
      matrix[i][last] = top;                                  // top → right
    }
  }
}
```
```python
# Python — in-place, O(1) space
def rotate(matrix: list) -> None:
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
```
> 🧠 **সহজ বিকল্প (মনে রাখা সহজ):** **transpose** (সারি↔কলাম অদলবদল) **+ প্রতিটা row reverse** = ৯০° clockwise। interview-তে এটাও বলা যায়।

## 🔹 Complexity
**Time: O(n²)** (প্রতিটা pixel ছুঁতেই হবে) · **Space: O(1)** (in-place)।

## 🔹 Pattern চিনুন
> **"matrix in-place ঘোরাও" → layer-by-layer ৪-মুখী swap; অথবা transpose + reverse।**

## 🔹 Common mistake
- ❌ index-এ off-by-one (`last - offset` গুলিয়ে ফেলা)।
- ❌ swap-এর ক্রম ভুল করা / temp variable ভুলে যাওয়া।

## 🔹 Follow-up
- **৯০° anti-clockwise?** → swap-এর দিক উল্টে দাও, বা transpose + প্রতিটা **column** reverse।

---
---

# 1.8 — Zero Matrix

> Pattern: **Matrix mark-then-apply** · Difficulty: **Medium** · Common

> **বইয়ের ভাষায়:** In an M×N matrix, if an element is 0, set its entire row and column to 0.

## 🔹 সমস্যাটা সহজ বাংলায়
Matrix-এ কোথাও **0** থাকলে, সেই ঘরের **পুরো row আর পুরো column** 0 করে দাও।

## 🔹 ⚠️ প্রধান ফাঁদ
চলতে চলতে 0 বসালে — সেই **নতুন 0** গুলোকেও আসল 0 ভেবে আবার row/column 0 করবে → পুরো matrix 0 হয়ে যাবে! তাই **আগে সব 0-এর অবস্থান খুঁজে রাখো, তারপর** 0 বসাও।

## 🔹 উদাহরণ
```
input:            output:   (row 1 আর col 2 শূন্য, কারণ (1,2)=0)
1 2 3 4           1 2 0 4
5 6 0 8     →     0 0 0 0
9 1 2 3           9 1 0 3
```

## 🔹 ভাবনা ১: কোন row/col শূন্য করতে হবে — Set-এ রাখো (পরিষ্কার)
প্রথম pass-এ সব 0-এর row আর column দুটো Set-এ জমাই। দ্বিতীয় pass-এ যেসব ঘরের row বা col ওই Set-এ আছে, সেগুলো 0 করি।
- **Time: O(M·N)** · **Space: O(M + N)**।

## 🔹 Code
```dart
// Dart
void zeroMatrix(List<List<int>> matrix) {
  if (matrix.isEmpty) return;
  final rows = <int>{}, cols = <int>{};
  final m = matrix.length, n = matrix[0].length;
  for (int i = 0; i < m; i++) {                 // pass 1: 0 খুঁজে রাখো
    for (int j = 0; j < n; j++) {
      if (matrix[i][j] == 0) { rows.add(i); cols.add(j); }
    }
  }
  for (int i = 0; i < m; i++) {                 // pass 2: 0 বসাও
    for (int j = 0; j < n; j++) {
      if (rows.contains(i) || cols.contains(j)) matrix[i][j] = 0;
    }
  }
}
```
```python
# Python
def zero_matrix(matrix: list) -> None:
    if not matrix:
        return
    rows, cols = set(), set()
    m, n = len(matrix), len(matrix[0])
    for i in range(m):                  # pass 1: 0 খুঁজে রাখো
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i); cols.add(j)
    for i in range(m):                  # pass 2: 0 বসাও
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
```

## 🔹 Complexity
**Time: O(M·N)** · **Space: O(M + N)**। 

## 🔹 Pattern চিনুন
> **"condition দেখে matrix পরিবর্তন" → আগে scan করে mark করো, পরে apply করো — চলতে চলতে বদলিয়ো না।**

## 🔹 Common mistake
- ❌ প্রথম pass-এই 0 বসিয়ে দেওয়া (cascade bug — সব 0 হয়ে যায়)।

## 🔹 Follow-up
- **O(1) space-এ করো** → আলাদা Set না রেখে **প্রথম row আর প্রথম column-কেই marker** হিসেবে ব্যবহার করো (একটু tricky — overlap সাবধানে handle করতে হয়)।

---
---

# 1.9 — String Rotation

> Pattern: **String + self (s1+s1) trick** · Difficulty: **Easy–Medium** · Common

> **বইয়ের ভাষায়:** Assume you have `isSubstring`. Given `s1`, `s2`, check if `s2` is a rotation of `s1` using **only one call** to `isSubstring` (e.g., `"waterbottle"` is a rotation of `"erbottlewat"`).

## 🔹 সমস্যাটা সহজ বাংলায়
`isSubstring(big, small)` (একটা string আরেকটার ভেতরে আছে কিনা) — শুধু **এই একটা function একবার** ডেকে বলতে হবে: `s2` কি `s1`-এর **rotation**?

## 🔹 মূল insight (দারুণ একটা trick)
Rotation মানে `s1` কে দুই টুকরো করে `s1 = x + y`, আর `s2 = y + x`। এখন মজা হলো —
> ✅ **`s2` সবসময় `s1 + s1`-এর substring হবে!** কারণ `s1+s1 = (x+y)+(x+y) = x + (y+x) + y` — এর মাঝখানে `y+x` (অর্থাৎ `s2`) আছেই।

## 🔹 উদাহরণ
```
s1 = "waterbottle"          →  x="wat", y="erbottle"
s2 = "erbottlewat"          →  y+x = "erbottle"+"wat"  ✅

s1+s1 = "waterbottlewaterbottle"
              └──erbottlewat──┘   ←  s2 এখানে substring!  →  rotation ✅
```

## 🔹 Code
```dart
// Dart
bool isRotation(String s1, String s2) {
  if (s1.length != s2.length || s1.isEmpty) return false;  // জরুরি check
  return isSubstring(s1 + s1, s2);                          // মাত্র একবার call
}

bool isSubstring(String big, String small) => big.contains(small);
```
```python
# Python
def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2) or not s1:     # জরুরি check
        return False
    return is_substring(s1 + s1, s2)     # মাত্র একবার call

def is_substring(big: str, small: str) -> bool:
    return small in big
```

## 🔹 Complexity
**Time: O(n)** (concat + substring search) · **Space: O(n)** (`s1+s1`-এর জন্য)।

## 🔹 Pattern চিনুন
> **"rotation কিনা" → string টাকে নিজের সাথে জোড়া (`s1+s1`) দিয়ে অন্যটা substring কিনা খোঁজো।** circular array/string problem-এ এই trick বারবার লাগে।

## 🔹 Common mistake
- ❌ length সমান কিনা / খালি কিনা — এই check বাদ দেওয়া (নাহলে ভুল `true`)।
- ❌ `isSubstring` একাধিকবার ডাকা (শর্ত ভাঙা)।

## 🔹 Follow-up
- **`isSubstring` নিজে implement করো** → naive O(n·m), অথবা KMP দিয়ে O(n+m)।

---
---

# ✅ Chapter 1 — সারসংক্ষেপ ও Pattern Cheat Sheet

| # | প্রশ্ন | মূল technique | Time | Space |
|---|---|---|---|---|
| 1.1 | Is Unique | Hash Set / Bit Vector | O(n) | O(1)–O(n) |
| 1.2 | Check Permutation | Frequency Count | O(n) | O(c) |
| 1.3 | URLify | পিছন থেকে in-place edit | O(n) | O(1) |
| 1.4 | Palindrome Permutation | Count + odd ≤ 1 | O(n) | O(c) |
| 1.5 | One Away | Two Pointer (১ mismatch) | O(n) | O(1) |
| 1.6 | String Compression | Run-length + StringBuilder | O(n) | O(n) |
| 1.7 | Rotate Matrix | Layer-by-layer swap | O(n²) | O(1) |
| 1.8 | Zero Matrix | Mark-then-apply | O(M·N) | O(M+N) |
| 1.9 | String Rotation | `s1+s1` substring trick | O(n) | O(n) |

### 🎯 "এটা দেখলে → এটা ভাবো" (signal → technique)
```
duplicate / unique / আগে দেখেছি?     →  Hash Set
permutation / anagram                →  Frequency Count (বা sort)
palindrome বানানো যায়?               →  Count, odd ≤ 1
পার্থক্য বড়জোর ১ / এক edit           →  Two Pointer, এক mismatch allow
পরপর একই জিনিস গোনা                  →  Run-length + StringBuilder
matrix ঘোরানো (in place)             →  Layer swap / transpose+reverse
matrix condition দেখে বদলানো          →  আগে mark, পরে apply
rotation / circular                  →  s1+s1 trick
loop-এ string জোড়া                   →  StringBuilder/join (নাহলে O(n²))
```

### 📝 এই chapter-এর 5টা সোনার নিয়ম
1. **Hash Set/Map** = O(1) lookup — array/string problem-এর সবচেয়ে দরকারি tool।
2. **Frequency count** anagram/permutation/palindrome — সব এক পরিবার।
3. **Two Pointer** (একই দিকে বা উল্টো দিকে) — string compare ও in-place edit-এ বারবার লাগে।
4. **StringBuilder** ছাড়া loop-এ string জোড়া দিলে O(n²) — মনে রাখবেন।
5. **Matrix problem**: in-place চাইলে layer/marker ভাবুন; condition apply-এ আগে mark করুন।

> **পরের ধাপ:** [Chapter 2 — Linked Lists](chapter02_linked_lists.md) (2.1–2.8), যেখানে "runner" (slow/fast pointer) technique শিখব।

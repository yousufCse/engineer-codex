# Chapter 10 — Sorting & Searching (প্রশ্ন 10.1 – 10.11)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। Code **Dart + Python** দুটোতেই।
> এই chapter শুরুর আগে [Chapter 0 — Foundation](chapter00_foundation.md) (Big-O + 7-step) পড়ে নিন।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: System Design](chapter09_system_design_scalability.md) · [পরের: Testing](chapter11_testing.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
A. আগে Background (অবশ্যই পড়ুন):
   - sorting কী, কেন লাগে (merge sort, quick sort, bucket/radix)
   - binary search — sorted data-তে খোঁজার অস্ত্র
   - কোন signal-এ কোন technique

B. তারপর ১১টা প্রশ্ন:
   10.1  Sorted Merge          — দুটো sorted array merge (পিছন থেকে)
   10.2  Group Anagrams        — anagram গুলো একসাথে গোছানো
   10.3  Search in Rotated     — ঘোরানো sorted array-তে খোঁজা
   10.4  Sorted Search,No Size — length না জানা sorted array-তে খোঁজা
   10.5  Sparse Search         — ফাঁকা string সহ array-তে খোঁজা
   10.6  Sort Big File         — RAM-এ ধরে না এমন file sort (external)
   10.7  Missing Int           — ৪ billion int থেকে missing খোঁজা
   10.8  Find Duplicates       — সীমিত RAM-এ duplicate খোঁজা (bit vector)
   10.9  Sorted Matrix Search  — row+col sorted matrix-এ খোঁজা
   10.10 Rank from Stream      — stream থেকে rank বের করা (BST)
   10.11 Peaks and Valleys     — array কে peak/valley-তে সাজানো
```

**প্রশ্নসমূহ:** [10.1 — Sorted Merge](#q10-1) · [10.2 — Group Anagrams](#q10-2) · [10.3 — Search in Rotated Array](#q10-3) · [10.4 — Sorted Search, No Size](#q10-4) · [10.5 — Sparse Search](#q10-5) · [10.6 — Sort Big File](#q10-6) · [10.7 — Missing Int](#q10-7) · [10.8 — Find Duplicates](#q10-8) · [10.9 — Sorted Matrix Search](#q10-9) · [10.10 — Rank from Stream](#q10-10) · [10.11 — Peaks and Valleys](#q10-11)

প্রতিটা প্রশ্ন এই কাঠামোয়: **সহজ বাংলায় সমস্যা → উদাহরণ → Listen → Brute force → Optimize → Code (Dart+Python) → Complexity → Pattern → Common mistake → Follow-up।**

---
---

# Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

এই chapter-এর সবকিছু দুটো মূল ধারণার ওপর দাঁড়িয়ে: **sorting** (সাজানো) আর **searching** (খোঁজা)। একটা data sorted থাকলে খোঁজা অনেক সহজ ও দ্রুত হয়ে যায় — তাই দুটো একসাথে শেখা হয়।

## ১. Sorting কী, কেন দরকার

Sorting মানে কতগুলো জিনিসকে একটা order-এ (ছোট→বড় বা বড়→ছোট) সাজানো। কেন দরকার?

- **খোঁজা দ্রুত হয়:** unsorted array-তে কিছু খুঁজতে সব দেখতে হয় (O(n)); sorted হলে **binary search**-এ O(log n)।
- **duplicate / pair খোঁজা সহজ:** sort করলে একই জিনিস পাশাপাশি চলে আসে।
- **অনেক problem-এর প্রথম ধাপ:** "আগে sort করি, তারপর..." — খুব common শুরু।

> **নিয়ম:** কোনো problem আটকে গেলে নিজেকে জিজ্ঞেস করুন — "data টা **sorted** থাকলে কি সহজ হতো?" হলে, sort করাই হয়তো প্রথম ধাপ।

## ২. দরকারি কয়েকটা sorting algorithm

ভাষার built-in sort (`list.sort()`, `sorted()`) প্রায় সবসময়ই ভালো — কিন্তু interview-তে এগুলো কীভাবে কাজ করে জানতে হয়।

### (ক) Merge Sort — "ভাগ করো, সাজাও, জোড়া দাও"

Array-কে দুই ভাগে ভাগ করো, প্রতি ভাগ আলাদা করে sort করো (recursion), তারপর দুই sorted ভাগ **merge** করো।

```
        [5 2 4 1 3]
        /         \
     [5 2]       [4 1 3]
     /  \         /    \
   [5]  [2]    [4]   [1 3]
     \  /         \    /  \
     [2 5]       [4] [1] [3]
        \           \  /
         \          [1 3]
          \          /
           merge → [1 2 3 4 5]
```

- **Time: O(n log n)** সবসময় (log n স্তর × প্রতি স্তরে O(n) merge)।
- **Space: O(n)** (merge করার সময় extra array লাগে)।
- **stable** (সমান জিনিসের আপেক্ষিক order ঠিক থাকে)।
- **merge** ধাপটাই 10.1-এর মূল।

### (খ) Quick Sort — "একটা pivot বেছে দুই ভাগে ফেলো"

একটা element কে **pivot** ধরো। তার চেয়ে ছোট সব বামে, বড় সব ডানে রাখো (**partition**)। তারপর দুই পাশ আলাদা করে quick sort করো।

```
pivot = 4:   [5 2 4 1 3]
  ছোট(<4): 2 1 3 | pivot 4 | বড়(>4): 5
  → [2 1 3] 4 [5]   তারপর প্রতি পাশ আবার quick sort
```

- **Time: গড়ে O(n log n)**, কিন্তু সবচেয়ে খারাপ ক্ষেত্রে **O(n²)** (pivot খারাপ পড়লে)।
- **Space: O(log n)** (recursion stack), in-place করা যায়।

### (গ) Bucket Sort / Radix Sort — comparison ছাড়াই sort (O(n) সম্ভব)

সাধারণ sort তুলনা (compare) করে — তাই O(n log n)-এর নিচে নামা যায় না। কিন্তু data যদি **integer / সীমিত range**-এর হয়, তাহলে তুলনা না করেও সাজানো যায়:

- **Bucket sort:** value-এর range কে কয়েকটা "bucket"-এ ভাগ করে প্রতিটা জিনিস নিজের bucket-এ ফেলো, তারপর bucket গুলো পরপর জোড়াও।
- **Radix sort:** সংখ্যাগুলোকে অঙ্ক ধরে ধরে (units, tens, hundreds...) বারবার সাজাও।

```
Radix sort [170, 45, 75, 90, 2, 802, 24]:
  units অঙ্ক ধরে:  [170, 90, 2, 802, 24, 45, 75]
  tens অঙ্ক ধরে:   [2, 802, 24, 45, 170, 75, 90]
  hundreds ধরে:    [2, 24, 45, 75, 90, 170, 802]  ← sorted
```

- **Time: O(n·k)** (k = অঙ্কসংখ্যা / pass) — integer হলে কার্যত **O(n)**।
- কখন: বড় সংখ্যক integer, সীমিত range — যেমন 10.7।

## ৩. Binary Search — sorted data-তে খোঁজার অস্ত্র

Sorted array-তে কিছু খুঁজতে প্রতিবার **মাঝখানে** দেখি। target মাঝের চেয়ে ছোট হলে বাম অর্ধেক, বড় হলে ডান অর্ধেক — প্রতি ধাপে অর্ধেক বাদ। তাই **O(log n)**।

```
খুঁজছি 7 in [1 3 5 7 9 11]:
 lo=0, hi=5, mid=2 → arr[2]=5 < 7 → ডানে যাও, lo=mid+1=3
 lo=3, hi=5, mid=4 → arr[4]=9 > 7 → বামে যাও, hi=mid-1=3
 lo=3, hi=3, mid=3 → arr[3]=7 == 7 → পেলাম! index 3
```

```dart
// Dart — classic binary search
int binarySearch(List<int> a, int target) {
  int lo = 0, hi = a.length - 1;
  while (lo <= hi) {
    final mid = lo + (hi - lo) ~/ 2;   // overflow এড়াতে এভাবে
    if (a[mid] == target) return mid;
    if (a[mid] < target) lo = mid + 1; // ডান অর্ধেক
    else hi = mid - 1;                 // বাম অর্ধেক
  }
  return -1;
}
```
```python
# Python — classic binary search
def binary_search(a: list, target: int) -> int:
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:   # ডান অর্ধেক
            lo = mid + 1
        else:                 # বাম অর্ধেক
            hi = mid - 1
    return -1
```

> **নিয়ম:** "sorted" + "খোঁজা" শব্দ দুটো একসাথে দেখলেই **binary search** ভাবুন। এই chapter-এর অর্ধেক প্রশ্ন আসলে binary search-এর একটু-বদলানো রূপ।

## ৪. এই chapter-এর signal → technique (এক নজরে)

```
দুটো sorted array merge          →  পিছন থেকে two-pointer
anagram একসাথে গোছাও             →  sorted-string কে Map-এর key
sorted কিন্তু ঘোরানো (rotated)    →  modified binary search
length জানা নেই                  →  আগে exponential দিয়ে boundary, পরে binary search
মাঝে ফাঁকা ("") আছে              →  mid ফাঁকা হলে কাছের non-empty-তে সরো
RAM-এ ধরে না                     →  external merge sort / bit vector
সীমিত RAM, integer               →  bit vector / bucket
row+col sorted matrix            →  উপর-ডান কোণ থেকে হাঁটো
stream থেকে rank                 →  BST প্রতি node-এ left-subtree size রাখো
peak/valley সাজানো               →  একবার হেঁটে প্রতিবেশীর সাথে swap
```

---
---

<a id="q10-1"></a>
# 10.1 — Sorted Merge

> Pattern: **Two Pointer (পিছন থেকে merge)** · Difficulty: **Easy** · খুব common (warm-up)

> **বইয়ের ভাষায়:** You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

## সমস্যাটা সহজ বাংলায়
দুটো **sorted array** `A` আর `B` দেওয়া। `A`-র শেষে **যথেষ্ট খালি জায়গা (buffer)** আছে যাতে `B`-র সব element ধরে। `B`-কে `A`-র ভেতর এমনভাবে ঢোকাতে হবে যেন পুরো `A` **sorted** থাকে। অর্থাৎ — দুটো sorted array এক জায়গায় (A-তে) sorted করে merge করো।

## উদাহরণ

```
A = [1, 4, 7, _, _, _]   (true length 3, শেষে 3টা খালি ঘর)
B = [2, 5, 8]

merge করার পর:
A = [1, 2, 4, 5, 7, 8]
```

## ধাপ ১: Listen
- **A-তে কি সত্যিই B-এর জন্য জায়গা আছে?** (হ্যাঁ, ধরে নেওয়া আছে)
- **A-র আসল (filled) length কত আলাদা করে জানি?** (হ্যাঁ — buffer বাদে)।
- ধরছি: দুটোই non-decreasing sorted, A-তে B ধরার মতো জায়গা আছে।

## ভাবনা ১: Brute Force — সামনে থেকে merge

স্বাভাবিক মনে হয়: দুটো array-র সামনে থেকে ছোটটা তুলে A-তে বসাই। কিন্তু সমস্যা — A-র **সামনের ঘরগুলোতে তো A-র নিজের data**! সামনে থেকে বসাতে গেলে A-র যেসব element এখনো বসাইনি, তাদের উপর লিখে ফেলব (overwrite)। বাঁচাতে হলে সেগুলো সরাতে হবে → প্রতিবার shift → **O(n²)**।

## ভাবনা ২: Optimize (BUD) — পিছন থেকে merge

মূল চালাকি: **A-র শেষ দিকটা খালি**। তাই সবচেয়ে **বড়** element গুলো পিছন থেকে বসালে কোনো কিছু overwrite হয় না।

তিনটা pointer:
- `i` → A-র আসল data-র শেষ
- `j` → B-র শেষ
- `k` → পুরো merged A-র শেষ ঘর (এখানে লিখব)

প্রতি ধাপে `A[i]` আর `B[j]`-এর মধ্যে **বড়টা** `A[k]`-তে বসাই, তারপর সংশ্লিষ্ট pointer ও `k` এক ধাপ পিছাই।

```
A = [1, 4, 7, _, _, _]   i=2 (value 7)
B = [2, 5, 8]            j=2 (value 8)
                          k=5 (শেষ ঘর)

7 vs 8 → 8 বড়  → A[5]=8, j=2→1, k=5→4   A=[1,4,7,_,_,8]
7 vs 5 → 7 বড়  → A[4]=7, i=2→1, k=4→3   A=[1,4,_,_,7,8]
4 vs 5 → 5 বড়  → A[3]=5, j=1→0, k=3→2   A=[1,4,_,5,7,8]
4 vs 2 → 4 বড়  → A[2]=4, i=1→0, k=2→1   A=[1,_,4,5,7,8]
1 vs 2 → 2 বড়  → A[1]=2, j=0→-1, k=1→0  A=[1,2,4,5,7,8]
B শেষ (j<0) → বাকি A ইতিমধ্যেই জায়গামতো → শেষ
```

## Code
```dart
// Dart — পিছন থেকে merge, O(1) extra space
void mergeSorted(List<int> a, int lenA, List<int> b, int lenB) {
  int i = lenA - 1;        // A-র আসল data-র শেষ
  int j = lenB - 1;        // B-র শেষ
  int k = lenA + lenB - 1; // merged A-র শেষ ঘর
  while (j >= 0) {         // B খালি না হওয়া পর্যন্ত
    if (i >= 0 && a[i] > b[j]) {
      a[k--] = a[i--];     // A-র element বড়
    } else {
      a[k--] = b[j--];     // B-র element বড় (বা A শেষ)
    }
  }
}
```
```python
# Python — পিছন থেকে merge, O(1) extra space
def merge_sorted(a: list, len_a: int, b: list, len_b: int) -> None:
    i = len_a - 1          # A-র আসল data-র শেষ
    j = len_b - 1          # B-র শেষ
    k = len_a + len_b - 1  # merged A-র শেষ ঘর
    while j >= 0:          # B খালি না হওয়া পর্যন্ত
        if i >= 0 and a[i] > b[j]:
            a[k] = a[i]; i -= 1   # A-র element বড়
        else:
            a[k] = b[j]; j -= 1   # B-র element বড় (বা A শেষ)
        k -= 1
```
> খেয়াল করুন loop চলে **`j >= 0`** পর্যন্ত। কারণ B শেষ হয়ে গেলে A-র বাকি element ইতিমধ্যেই সঠিক জায়গায়; কিন্তু A আগে শেষ হলে B-র বাকিগুলো বসাতেই হবে।

## Complexity
**Time: O(A + B)** — প্রতিটা element ঠিক একবার বসে। **Space: O(1)** — A-র নিজের buffer-এ কাজ, নতুন array লাগেনি।

## Pattern চিনুন
> **দুটো sorted জিনিস merge, আর গন্তব্য array-র শেষে খালি জায়গা → পিছন থেকে (back-to-front) লিখুন।** ঠিক 1.3 URLify-এর মতো নীতি: size বাড়ার দিকে in-place edit হলে পেছন থেকে।

## Common mistake
- **সামনে থেকে** merge করা → A-র data overwrite হয় বা shift দরকার হয় (O(n²))।
- loop শেষে B-র বাকি element বসাতে ভুলে যাওয়া (`while j >= 0` দিয়ে এটা handle হয়; A-র বাকি নিয়ে আলাদা কিছু করতে হয় না)।

## Follow-up
- **A-তে জায়গা না থাকলে?** → নতুন একটা array বানিয়ে সামনে থেকে standard merge (O(A+B) time, O(A+B) space)।
- **k-টা sorted array merge?** → min-heap ব্যবহার করো (10.x ধাঁচ; O(N log k))।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-2"></a>
# 10.2 — Group Anagrams

> Pattern: **Sorted-string কে Hash Map-এর key** · Difficulty: **Easy–Medium** · খুব common

> **বইয়ের ভাষায়:** Write a method to sort an array of strings so that all the anagrams are next to each other.

## সমস্যাটা সহজ বাংলায়
একগুচ্ছ string দেওয়া। এমনভাবে সাজাতে হবে যেন **anagram** গুলো (একই অক্ষর, শুধু order ভিন্ন — যেমন `"abc"`, `"bca"`, `"cab"`) **পাশাপাশি** চলে আসে। পুরো array globally sort করা লাগবে না — শুধু anagram দলগুলো একসাথে থাকলেই হলো।

## উদাহরণ

```
input:  ["abc", "bca", "xyz", "cab", "zyx"]

দল:     [abc, bca, cab]   [xyz, zyx]
                ↑ একই অক্ষর    ↑ একই অক্ষর

output: ["abc", "bca", "cab", "xyz", "zyx"]   (anagram পাশাপাশি)
```

## ধাপ ১: Listen
- **case-sensitive?** ("Abc" আর "abc" কি একই দল?) — ধরছি না, case-sensitive।
- পুরো array কি sorted হতে হবে, নাকি শুধু দল একসাথে? — শুধু দল একসাথে।

## ভাবনা ১: Brute Force — প্রতিটা pair মিলিয়ে দেখা

প্রতিটা string-এর সাথে বাকি সবার anagram-check করে দল বানানো। anagram check নিজেই O(s log s) বা O(s); সব pair O(n²) → মোট O(n²·s)। ধীর।

## ভাবনা ২: Optimize — sorted string কে "signature" বানাও

মূল insight: **দুটো string anagram হবে তখনই, যখন তাদের অক্ষর sort করলে একই string পাওয়া যায়।**

```
"bca" → sort → "abc"
"cab" → sort → "abc"   ← একই signature!  →  একই দল
"xyz" → sort → "xyz"
"zyx" → sort → "xyz"   ← একই signature!
```

তাই: প্রতিটা string-এর sorted রূপকে **Hash Map-এর key** বানাই, value হলো ওই signature-এর সব string-এর list। শেষে দল ধরে ধরে বের করি।

```
Map:
  "abc" → [abc, bca, cab]
  "xyz" → [xyz, zyx]
পরপর ছাপলে → anagram পাশাপাশি
```

## Code
```dart
// Dart
List<String> groupAnagrams(List<String> strs) {
  final groups = <String, List<String>>{};
  for (final s in strs) {
    final key = (s.split('')..sort()).join();   // sorted signature
    groups.putIfAbsent(key, () => []).add(s);
  }
  final result = <String>[];
  for (final list in groups.values) {
    result.addAll(list);                         // দল ধরে ধরে যোগ
  }
  return result;
}
```
```python
# Python
from collections import defaultdict

def group_anagrams(strs: list) -> list:
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))   # sorted signature
        groups[key].append(s)
    result = []
    for group in groups.values():  # দল ধরে ধরে যোগ
        result.extend(group)
    return result
```
> **বিকল্প key:** sort না করে প্রতিটা অক্ষরের count (২৬টা সংখ্যার tuple) কেও key বানানো যায় — তখন signature বানানো O(s), sort-এর O(s log s)-এর চেয়ে সামান্য দ্রুত।

## Complexity
ধরি n = string সংখ্যা, s = সবচেয়ে বড় string-এর length।
**Time: O(n · s log s)** — প্রতিটা string sort করতে s log s। **Space: O(n · s)** — Map-এ সব string জমা।

## Pattern চিনুন
> **"anagram একসাথে গোছাও / একই অক্ষরের দল" → প্রতিটা element-এর একটা canonical signature (এখানে sorted string) বানাও, সেটাকে Hash Map-এর key করো।** এই "normalize করে key বানানো" trick অনেক grouping problem-এ লাগে।

## Common mistake
- পুরো array কে comparator দিয়ে globally sort করার চেষ্টা (custom comparator লেখা যায়, কিন্তু Map approach সহজ ও দ্রুত)।
- signature বানানোর সময় mutate করে original string নষ্ট করা (Dart-এ `s.split('')..sort()` নতুন list-এ কাজ করে, safe)।

## Follow-up
- **case/space ignore করতে হলে?** → signature বানানোর আগে `toLowerCase()` ও space বাদ দাও।
- **একই দলের string গুলোও sorted চাই?** → প্রতিটা group list আলাদা করে sort করো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-3"></a>
# 10.3 — Search in Rotated Array

> Pattern: **Modified Binary Search** · Difficulty: **Medium** · খুব common

> **বইয়ের ভাষায়:** Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order. Example: find 5 in `{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}` → index 8.

## সমস্যাটা সহজ বাংলায়
একটা sorted array কে **কয়েকবার ঘোরানো (rotate)** হয়েছে — মানে শুরুর কিছু অংশ তুলে শেষে বসিয়ে দেওয়া হয়েছে। এখন এই rotated array-তে একটা নির্দিষ্ট value কোন index-এ আছে খুঁজতে হবে — **O(log n)**-এ (binary search-এর মতো দ্রুত)।

## উদাহরণ

```
মূল sorted:   [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]
ঘোরানোর পর:   [15,16,19,20,25, 1, 3, 4, 5, 7, 10, 14]
index:          0  1  2  3  4  5  6  7  8  9 10 11
                └── বড় অর্ধেক ──┘  └── ছোট অর্ধেক ──┘

5 খুঁজছি → index 8
```

## ধাপ ১: Listen
- **duplicate থাকতে পারে?** (থাকলে worst case O(n) হয়ে যেতে পারে) — ধরছি প্রথমে distinct।
- target না থাকলে কী ফেরাব? → `-1`।

## ভাবনা ১: Brute Force
পুরো array linear scan → **O(n)**। rotation-এর তথ্য কাজে লাগাইনি, তাই ধীর।

## ভাবনা ২: Optimize — অর্ধেকের একটা সবসময় sorted

মূল insight: rotated array-কে মাঝখানে কাটলে, **দুই অর্ধেকের অন্তত একটা সবসময় ঠিকঠাক sorted** থাকে।

প্রতি ধাপে `mid` দেখি। তারপর:
1. `arr[lo] <= arr[mid]` হলে → **বাম অর্ধেক sorted**।
 - target যদি `arr[lo]` আর `arr[mid]`-এর মধ্যে পড়ে → বামে যাও, নইলে ডানে।
2. নইলে → **ডান অর্ধেক sorted**।
 - target যদি `arr[mid]` আর `arr[hi]`-এর মধ্যে পড়ে → ডানে যাও, নইলে বামে।

এভাবে প্রতি ধাপে অর্ধেক বাদ → **O(log n)**।

```
[15,16,19,20,25,1,3,4,5,7,10,14]  target=5
lo=0 hi=11 mid=5 → arr[mid]=1
 arr[lo]=15 > arr[mid]=1 → ডান অর্ধেক sorted (1..14)
 5 কি (1, 14]-এর মধ্যে? হ্যাঁ → ডানে যাও  lo=6
lo=6 hi=11 mid=8 → arr[mid]=5 == target → পেলাম! index 8
```

## Code
```dart
// Dart — modified binary search
int searchRotated(List<int> a, int target) {
  int lo = 0, hi = a.length - 1;
  while (lo <= hi) {
    final mid = lo + (hi - lo) ~/ 2;
    if (a[mid] == target) return mid;
    if (a[lo] <= a[mid]) {                 // বাম অর্ধেক sorted
      if (a[lo] <= target && target < a[mid]) {
        hi = mid - 1;                      // target বাম অর্ধেকে
      } else {
        lo = mid + 1;
      }
    } else {                               // ডান অর্ধেক sorted
      if (a[mid] < target && target <= a[hi]) {
        lo = mid + 1;                      // target ডান অর্ধেকে
      } else {
        hi = mid - 1;
      }
    }
  }
  return -1;
}
```
```python
# Python — modified binary search
def search_rotated(a: list, target: int) -> int:
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == target:
            return mid
        if a[lo] <= a[mid]:                # বাম অর্ধেক sorted
            if a[lo] <= target < a[mid]:
                hi = mid - 1               # target বাম অর্ধেকে
            else:
                lo = mid + 1
        else:                              # ডান অর্ধেক sorted
            if a[mid] < target <= a[hi]:
                lo = mid + 1               # target ডান অর্ধেকে
            else:
                hi = mid - 1
    return -1
```

## Complexity
**Time: O(log n)** (distinct হলে) — প্রতি ধাপে অর্ধেক বাদ। **Space: O(1)**।
duplicate থাকলে `a[lo] == a[mid] == a[hi]` ক্ষেত্রে কোন পাশ sorted বোঝা যায় না, তখন এক-এক ধাপ এগোতে হয় → worst case **O(n)**।

## Pattern চিনুন
> **"sorted কিন্তু ঘোরানো (rotated) array-তে খোঁজা" → modified binary search: প্রতি ধাপে কোন অর্ধেক sorted বের করো, target সেই sorted range-এ পড়ে কিনা দেখে দিক ঠিক করো।**

## Common mistake
- `<=` আর `<` গুলিয়ে ফেলা (range check-এ boundary ভুল হলে answer মিস)।
- `a[lo] <= a[mid]` শর্ত বাদ দেওয়া — এটাই "কোন পাশ sorted" নির্ণয় করে।
- duplicate-এর case ভুলে যাওয়া (interviewer প্রায়ই জিজ্ঞেস করে)।

## Follow-up
- **duplicate থাকলে?** → `a[lo] == a[mid]` হলে `lo++` করে এগোও; worst case O(n)।
- **rotation point (সবচেয়ে ছোট element) খুঁজে দাও** → একই ধাঁচের binary search।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-4"></a>
# 10.4 — Sorted Search, No Size

> Pattern: **Exponential boundary + Binary Search** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** You are given an array-like data structure `Listy` which lacks a size method. It does, however, have an `elementAt(i)` method that returns the element at index i in O(1) time. If i is beyond the bounds of the data structure, it returns -1. Given a `Listy` which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.

## সমস্যাটা সহজ বাংলায়
একটা sorted array আছে কিন্তু তার **length জানা নেই**। `elementAt(i)` দিয়ে যেকোনো index-এর value পাই (O(1)); index range-এর বাইরে গেলে **-1** ফেরে। এই array-তে একটা value `x` খুঁজতে হবে — দ্রুত (binary search-এর মতো)। সব সংখ্যা positive।

## উদাহরণ

```
Listy: [1, 3, 5, 7, 9, 11, 13]   (length গোপন!)
elementAt(2)  → 5
elementAt(6)  → 13
elementAt(7)  → -1   (সীমার বাইরে)
elementAt(100)→ -1

x = 9 খুঁজছি  →  index 4
```

## ধাপ ১: Listen
- **negative value থাকতে পারে?** না (সব positive — তাই -1 মানেই "সীমার বাইরে", value নয়)।
- multiple occurrence হলে যেকোনো index দিলেই চলবে।

## মূল সমস্যা
Binary search-এর জন্য `hi` (শেষ index) দরকার, কিন্তু length-ই তো জানি না! তাই **আগে একটা boundary খুঁজে বের করতে হবে** যার ভেতরে x নিশ্চিত আছে।

## ভাবনা ১: Brute Force — একটা একটা করে দেখা
index 0, 1, 2... করে আগাই যতক্ষণ না x পাই বা -1 আসে → **O(n)**। length ছোট হলে চলে, কিন্তু binary search-এর সুবিধা হারালাম।

## ভাবনা ২: Optimize — Exponential backoff দিয়ে boundary খোঁজা

index **দ্বিগুণ করে করে** (1, 2, 4, 8, 16, ...) লাফাই, যতক্ষণ না হয় -1 আসে, নয়তো ওই index-এর value `x`-এর চেয়ে বড় হয়। তখন বুঝি `x` (যদি থাকে) আগের আর এই index-এর **মাঝে** আছে। এই range-এ এবার normal binary search চালাই।

```
x = 9:
 index 1 → 3   (< 9, আরও দূরে)  → index 2
 index 2 → 5   (< 9)            → index 4
 index 4 → 9   (== 9 বা >= 9) → boundary পেলাম, range [2..4]-এ binary search
 binary search → index 4-এ 9 → পেলাম
```

দ্বিগুণ করে লাফানোয় boundary খুঁজতে O(log n), তারপর binary search-ও O(log n) → মোট **O(log n)**।

## Code
```dart
// Dart — Listy abstraction ধরে নিচ্ছি: int elementAt(int i)
int searchNoSize(List<int> listy, int x) {
  // ধাপ ১: exponential দিয়ে boundary খোঁজা
  int index = 1;
  while (listy.length > index && listy[index] != -1 && listy[index] < x) {
    index *= 2;   // দ্বিগুণ লাফ
  }
  // এখানে index = এমন জায়গা যেখানে value >= x বা সীমার বাইরে
  return _binarySearch(listy, x, index ~/ 2, index);
}

int _binarySearch(List<int> a, int x, int lo, int hi) {
  while (lo <= hi) {
    final mid = lo + (hi - lo) ~/ 2;
    int val = (mid < a.length) ? a[mid] : -1;   // সীমার বাইরে = -1
    if (val == -1 || val > x) {
      hi = mid - 1;        // বাঁয়ে (বড় বা সীমার বাইরে)
    } else if (val < x) {
      lo = mid + 1;        // ডানে
    } else {
      return mid;          // পেলাম
    }
  }
  return -1;
}
```
```python
# Python — listy.element_at(i): index বাইরে হলে -1
def search_no_size(listy, x: int) -> int:
    # ধাপ ১: exponential দিয়ে boundary খোঁজা
    index = 1
    while listy.element_at(index) != -1 and listy.element_at(index) < x:
        index *= 2          # দ্বিগুণ লাফ
    # ধাপ ২: range [index//2, index]-এ binary search
    lo, hi = index // 2, index
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = listy.element_at(mid)   # সীমার বাইরে = -1
        if val == -1 or val > x:
            hi = mid - 1              # বাঁয়ে
        elif val < x:
            lo = mid + 1              # ডানে
        else:
            return mid                # পেলাম
    return -1
```
> খেয়াল করুন: binary search-এর ভেতরে `elementAt(mid)` যদি **-1** দেয়, সেটাকে "খুব বড়" ধরে বাঁ দিকে সরি — কারণ -1 মানে আমরা সীমার বাইরে চলে গেছি।

## Complexity
**Time: O(log n)** — boundary খোঁজা O(log n) (দ্বিগুণ লাফ), তারপর binary search O(log n)। **Space: O(1)**।

## Pattern চিনুন
> **"sorted কিন্তু size/boundary জানা নেই" → আগে exponential (দ্বিগুণ) লাফ দিয়ে একটা boundary বের করো, তারপর সেই range-এ normal binary search।** unbounded/infinite sorted stream-এ খোঁজার classic কৌশল।

## Common mistake
- boundary খোঁজার সময় -1 (সীমার বাইরে) কে ভুল করে value হিসেবে তুলনা করা।
- binary search-এ `mid`-এর value -1 হলে "বড়" হিসেবে treat না করা।

## Follow-up
- **negative number থাকলে?** → -1 আর আসল value আলাদা করতে আলাদা sentinel বা length-probe লাগবে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-5"></a>
# 10.5 — Sparse Search

> Pattern: **Modified Binary Search (ফাঁকা element skip)** · Difficulty: **Easy–Medium** · common

> **বইয়ের ভাষায়:** Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string. Example: find "ball" in `{"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}` → index 4.

## সমস্যাটা সহজ বাংলায়
একটা **sorted string array** দেওয়া, কিন্তু মাঝে মাঝে **ফাঁকা string `""`** ছড়ানো আছে। একটা নির্দিষ্ট string কোন index-এ আছে খুঁজতে হবে। ফাঁকাগুলো বাদ দিলে বাকিগুলো sorted।

## উদাহরণ

```
["at","","","","ball","","","car","","","dad","",""]
  0   1  2  3   4    5  6   7   8  9  10  11 12

"ball" খুঁজছি  →  index 4
```

## মূল সমস্যা
Binary search-এ `mid` যদি `""` (ফাঁকা)-তে পড়ে, তাহলে তুলনাই করা যায় না — কোন দিকে যাব বোঝা যাবে না। তাই ফাঁকা পেলে কী করব সেটাই মূল।

## ভাবনা ১: Brute Force
পুরো array linear scan, `""` বাদ দিয়ে মিলিয়ে দেখা → **O(n)**। sorted-এর সুবিধা নষ্ট হলো।

## ভাবনা ২: Optimize — mid ফাঁকা হলে কাছের non-empty-তে সরো

Normal binary search-ই করি, কিন্তু `mid` যদি `""` হয়, তাহলে **mid-এর দুই পাশে সবচেয়ে কাছের non-empty index** খুঁজে সেখানে `mid` সরিয়ে নিই। তারপর normal তুলনা।

```
mid = 5 → "" (ফাঁকা)
 বাঁয়ে: index 4 → "ball" (non-empty)   ┐ দুই দিকে একসাথে খুঁজি,
 ডানে: index 6 → "" → 7 → "car"        ┘ যেটা আগে পাই
 কাছেরটা ধরে mid কে সেখানে নিয়ে যাই, তারপর তুলনা
```

## Code
```dart
// Dart
int sparseSearch(List<String> a, String target) {
  if (target.isEmpty) return -1;     // ফাঁকা খোঁজা অর্থহীন
  return _search(a, target, 0, a.length - 1);
}

int _search(List<String> a, String target, int lo, int hi) {
  while (lo <= hi) {
    int mid = lo + (hi - lo) ~/ 2;
    if (a[mid].isEmpty) {                 // mid ফাঁকা → কাছের non-empty খোঁজো
      int left = mid - 1, right = mid + 1;
      while (true) {
        if (left < lo && right > hi) return -1;     // চারপাশ ফাঁকা
        if (right <= hi && a[right].isNotEmpty) { mid = right; break; }
        if (left >= lo && a[left].isNotEmpty)  { mid = left;  break; }
        left--; right++;
      }
    }
    final cmp = a[mid].compareTo(target);
    if (cmp == 0) return mid;
    if (cmp < 0) lo = mid + 1; else hi = mid - 1;
  }
  return -1;
}
```
```python
# Python
def sparse_search(a: list, target: str) -> int:
    if target == "":          # ফাঁকা খোঁজা অর্থহীন
        return -1
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == "":      # mid ফাঁকা → কাছের non-empty খোঁজো
            left, right = mid - 1, mid + 1
            while True:
                if left < lo and right > hi:
                    return -1            # চারপাশ ফাঁকা
                if right <= hi and a[right] != "":
                    mid = right; break
                if left >= lo and a[left] != "":
                    mid = left; break
                left -= 1; right += 1
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## Complexity
**Time: গড়ে O(log n)**, কিন্তু **worst case O(n)** — যদি অনেক `""` থাকে (যেমন পুরো array `""` একটা ছাড়া), তখন কাছের non-empty খুঁজতেই অনেক ঘর পেরোতে হয়। **Space: O(1)**।

## Pattern চিনুন
> **"sorted, কিন্তু মাঝে অর্থহীন/ফাঁকা element" → binary search চালাও, mid খারাপ পড়লে কাছের ভালো element-এ সরে গিয়ে তুলনা করো।**

## Common mistake
- target নিজেই `""` হলে handle না করা (sorted ধরে খোঁজা অর্থহীন → আগে reject)।
- কাছের non-empty খোঁজার সময় `lo`/`hi` boundary পেরিয়ে যাওয়া (index out of range)।

## Follow-up
- **প্রায় পুরোটাই ফাঁকা হলে?** → তখন কোনো algorithm-ই O(n)-এর ভালো করতে পারে না, কারণ ফাঁকার কারণে sorted-structure কাজে লাগে না।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-6"></a>
# 10.6 — Sort Big File

> Pattern: **External Merge Sort** · Difficulty: **Medium (conceptual)** · common (scalability)

> **বইয়ের ভাষায়:** Imagine you have a 20 GB file with one string per line. Explain how you would sort the file.

## সমস্যাটা সহজ বাংলায়
একটা **২০ GB file**, প্রতি লাইনে একটা string। এটা sort করতে হবে। সমস্যা — পুরো ২০ GB একসাথে **RAM-এ ধরবে না** (সাধারণ মেশিনে RAM হয়তো কয়েক GB)। তাই `list.sort()` করে এক চোটে sort করা যাবে না। তাহলে কীভাবে?

## মূল insight
"২০ GB" শব্দটাই signal — মানে এটা **memory-তে আঁটে না**। এমন ক্ষেত্রে আমরা **External Sort** (বাইরের, disk-ভিত্তিক sort) ব্যবহার করি, বিশেষত **External Merge Sort**।

> এটা কোডিং নয়, **system/scalability** ধাঁচের প্রশ্ন — interviewer চান আপনি "data RAM-এ ধরে না" বুঝে সঠিক পদ্ধতি বলতে পারেন কিনা।

## External Merge Sort — দুই ধাপ

```
ধাপ ১ (Split + Sort করা ছোট chunk):
  ২০ GB কে RAM-এ আঁটে এমন ছোট টুকরোয় (ধরি ১ GB করে ২০ chunk) ভাগ করো।
  প্রতিটা chunk RAM-এ এনে normal sort করো, sorted অবস্থায় disk-এ আলাদা file-এ লেখো।

  20 GB ──► [1GB][1GB][1GB] ... 20টা chunk
              │    │    │
            sort sort sort   (প্রতিটা আলাদা, RAM-এ ধরে)
              ▼    ▼    ▼
            run1 run2 ... run20   (প্রতিটা sorted, disk-এ)

ধাপ ২ (k-way Merge):
  ২০টা sorted run একসাথে merge করো। প্রতিটা run থেকে শুরুর কিছু অংশ
  RAM-এ এনে, min-heap দিয়ে সবচেয়ে ছোট element বেছে output-এ লেখো।
  কোনো run-এর buffer খালি হলে disk থেকে পরের অংশ আনো।

  run1: a c f
  run2: b d g     →  k-way merge (min-heap)  →  a b c d e f g ...
  run3: e h i                                    (পুরো sorted output)
```

- প্রতিটা **chunk**-কে বলে **run**।
- ধাপ ২-তে একসাথে সব run থেকে একটু একটু RAM-এ আনি (streaming) — তাই কখনো পুরো file RAM-এ থাকে না।

## ছদ্ম-কোড (concept বোঝাতে)
```dart
// Dart — concept skeleton (আসল file I/O বাদ)
List<String> externalMergeSort(BigFile file, int ramLimit) {
  final runs = <SortedRun>[];
  // ধাপ ১: chunk করে sort
  while (file.hasMore()) {
    final chunk = file.readChunk(ramLimit);  // RAM-এ আঁটে এতটুকু
    chunk.sort();                             // normal in-memory sort
    runs.add(writeToDisk(chunk));             // sorted run disk-এ
  }
  // ধাপ ২: সব run k-way merge
  return kWayMerge(runs);                     // min-heap দিয়ে
}
```
```python
# Python — concept skeleton; heapq.merge ঠিক এই কাজটা করে
import heapq

def external_merge_sort(file, ram_limit):
    runs = []
    # ধাপ ১: chunk করে sort, disk-এ লেখো
    for chunk in file.read_in_chunks(ram_limit):
        chunk.sort()                 # RAM-এ আঁটে এতটুকু
        runs.append(write_to_disk(chunk))
    # ধাপ ২: sorted run গুলো streaming-ভাবে merge
    sorted_streams = [read_stream(r) for r in runs]
    return heapq.merge(*sorted_streams)   # k-way merge, lazy/streaming
```
> Python-এর `heapq.merge` ঠিক ধাপ ২-এর kaaj করে: একাধিক sorted stream নিয়ে একটা sorted stream দেয়, সব RAM-এ না এনে।

## Complexity
ধরি N = মোট record, M = RAM-এ আঁটে এমন record সংখ্যা।
**Time: O(N log N)** (প্রতি record কিছু সংখ্যক pass-এ যায়)। **disk I/O ই আসল cost** — pass সংখ্যা ≈ `log_(M)(N/M)`, তাই RAM যত বড়, তত কম pass, তত দ্রুত।

## Pattern চিনুন
> **"X GB / RAM-এ ধরে না / huge file sort" → External Merge Sort: ছোট chunk-এ ভাগ করে আলাদা sort (run), তারপর min-heap দিয়ে k-way merge।**

## Common mistake
- পুরো file একসাথে RAM-এ আনার চেষ্টা (যা প্রশ্নের পুরো পয়েন্ট মিস করে)।
- merge ধাপে সব run পুরোটা RAM-এ আনা (শুধু buffer-টুকু আনতে হয়, streaming)।

## Follow-up
- **একাধিক মেশিন থাকলে?** → distributed sort (MapReduce-এর মতো): প্রতিটা মেশিন range-ভিত্তিক partition sort করে, পরে merge। (Chapter 9-এর scalability ধারণা।)

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-7"></a>
# 10.7 — Missing Int

> Pattern: **Bit Vector / Bucketed counting** · Difficulty: **Medium–Hard** · common (memory-constrained)

> **বইয়ের ভাষায়:** Given an input file with four billion non-negative integers, provide an algorithm to generate an integer which is not contained in the file. Assume you have 1 GB of memory available for this task. FOLLOW UP: What if you have only 10 MB of memory? Assume that all the values are distinct and there are no more than one billion distinct integers.

## সমস্যাটা সহজ বাংলায়
একটা file-এ **৪ billion** non-negative integer আছে। এমন একটা integer বের করতে হবে যা file-এ **নেই**। দুই version:
- **(ক) ১ GB RAM** আছে।
- **(খ) মাত্র ১০ MB RAM** আছে (follow-up, কঠিন অংশ)।

## জরুরি সংখ্যাতত্ত্ব (এটাই চাবি)
সব non-negative int ধরা হয় ৪-byte (32-bit) → মোট সম্ভাব্য মান `2^32 ≈ 4.29 billion`। কিন্তু file-এ মাত্র ৪ billion আছে → **কিছু মান অবশ্যই নেই** (pigeonhole)। সেটাই খুঁজব।

## ভাগ (ক): ১ GB RAM — Bit Vector

প্রতিটা সম্ভাব্য মানের জন্য **একটা bit** রাখি: bit 1 = "এই সংখ্যা file-এ দেখেছি"।
`2^32` bit = `2^32 / 8` byte = **512 MB** → ১ GB-তে অনায়াসে আঁটে।

```
file পড়তে পড়তে: প্রতিটা সংখ্যা n দেখলে → bit[n] = 1
শেষে: প্রথম যে bit এখনো 0 → সেই index-ই missing integer
```

```dart
// Dart (ক) — bit vector, ১ GB RAM
int findMissing1GB(Iterable<int> numbers) {
  const int n = 1 << 32;            // 2^32 সম্ভাব্য মান (ধারণাগত)
  final bitset = List<int>.filled(n ~/ 32, 0);  // প্রতি int 32 bit
  for (final num in numbers) {
    bitset[num >> 5] |= (1 << (num & 31));       // bit[num] = 1
  }
  for (int i = 0; i < n; i++) {
    if ((bitset[i >> 5] & (1 << (i & 31))) == 0) return i;  // প্রথম 0 bit
  }
  return -1;  // সব আছে (বাস্তবে হবে না)
}
```
```python
# Python (ক) — bytearray দিয়ে bit vector
def find_missing_1gb(numbers) -> int:
    SIZE = 1 << 32
    bitset = bytearray(SIZE // 8)        # 512 MB
    for num in numbers:
        bitset[num >> 3] |= (1 << (num & 7))   # bit[num] = 1
    for i in range(SIZE):
        if not (bitset[i >> 3] & (1 << (i & 7))):
            return i                     # প্রথম 0 bit
    return -1
```

## ভাগ (খ): ১০ MB RAM — দুই pass, bucket গোনা

৫১২ MB bit vector ১০ MB-তে আঁটবে না। তাই **দুই pass**:

```
Pass 1 (range গুনি):
  পুরো মান-পরিসরকে সমান কিছু bucket-এ ভাগ করি (ধরি প্রতিটা range-এ
  ~1000 সংখ্যা, মোট ~4M+ bucket — প্রতি bucket-এ শুধু একটা count রাখি,
  সেটা ১০ MB-তে আঁটে)।
  প্রতিটা সংখ্যা যে range-এ পড়ে, সেই bucket-এর count++।

  একটা range-এ যদি count < (range-এর আকার), তাহলে ওই range-এ
  অন্তত একটা সংখ্যা missing!  ← এই bucket টা বেছে নিই।

Pass 2 (ওই bucket-এর ভেতর bit vector):
  শুধু ওই একটা range-এর সংখ্যাগুলোর জন্য ছোট bit vector বানাই
  (range ছোট, তাই ১০ MB-তে আঁটে)। আবার file পড়ি, শুধু ওই range-এর
  সংখ্যার bit 1 করি। শেষে প্রথম 0-bit-ই missing integer।
```

কেন কাজ করে: pass 1-এ একটা range কম-ভরা পেলেই নিশ্চিত হই সেখানে missing আছে, তারপর শুধু সেই ছোট range-এ মন দিই।

```python
# Python (খ) — দুই pass, ১০ MB
def find_missing_10mb(file_reader) -> int:
    RANGE = 1 << 20                    # প্রতি bucket-এ এতটা মান
    NUM_BUCKETS = (1 << 32) // RANGE   # bucket সংখ্যা
    counts = [0] * NUM_BUCKETS         # ছোট, ১০ MB-তে আঁটে

    for num in file_reader():          # pass 1: range গুনি
        counts[num // RANGE] += 1

    bucket = next(i for i, c in enumerate(counts) if c < RANGE)  # কম-ভরা range
    start = bucket * RANGE

    bitset = bytearray(RANGE // 8)     # শুধু ওই range-এর bit vector
    for num in file_reader():          # pass 2: ওই range-এর bit set
        if start <= num < start + RANGE:
            offset = num - start
            bitset[offset >> 3] |= (1 << (offset & 7))
    for i in range(RANGE):
        if not (bitset[i >> 3] & (1 << (i & 7))):
            return start + i           # প্রথম 0-bit
    return -1
```
```dart
// Dart (খ) — concept (file দুইবার পড়তে হয়)
int findMissing10MB(Iterable<int> Function() readFile) {
  const int range = 1 << 20;
  const int buckets = (1 << 32) ~/ range;
  final counts = List<int>.filled(buckets, 0);
  for (final num in readFile()) counts[num ~/ range]++;     // pass 1
  int b = counts.indexWhere((c) => c < range);              // কম-ভরা range
  final start = b * range;
  final bitset = List<int>.filled(range ~/ 32, 0);
  for (final num in readFile()) {                            // pass 2
    if (num >= start && num < start + range) {
      final off = num - start;
      bitset[off >> 5] |= (1 << (off & 31));
    }
  }
  for (int i = 0; i < range; i++) {
    if ((bitset[i >> 5] & (1 << (i & 31))) == 0) return start + i;
  }
  return -1;
}
```

## Complexity
**(ক):** Time O(n), Space ~512 MB। **(খ):** Time O(n) (দুই pass, তাই 2n), Space ~১০ MB। দুটোই n-এ linear; পার্থক্য শুধু memory ব্যবহারে।

## Pattern চিনুন
> **"বিশাল সংখ্যক integer + সীমিত memory + missing/duplicate খোঁজা" → bit vector; memory আরও কম হলে → আগে bucket-এ গুনে কোন range-এ ঘাটতি বের করো, তারপর সেই range-এ ছোট bit vector।**

## Common mistake
- bit আর byte গুলিয়ে ফেলা — `2^32` bit = ৫১২ MB (৪ GB নয়!)।
- (খ)-তে "কম-ভরা bucket"-এর শর্ত ভুলে যাওয়া (count < range size হলেই missing আছে)।

## Follow-up
- **মান distinct না হলে (duplicate থাকতে পারে)?** → bit vector-এ duplicate এমনিতেই সমস্যা করে না (একই bit আবার 1 হয়); কিন্তু (খ)-তে "কম-ভরা" শর্ত আর সরাসরি খাটে না — তখন distinct-count আলাদা ভাবতে হয়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-8"></a>
# 10.8 — Find Duplicates

> Pattern: **Bit Vector** · Difficulty: **Medium** · common (memory-constrained)

> **বইয়ের ভাষায়:** You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how would you print all duplicate elements in the array?

## সমস্যাটা সহজ বাংলায়
একটা array-তে `1` থেকে `N`-এর মধ্যে সংখ্যা আছে (`N ≤ 32,000`), কিছু সংখ্যা **একাধিকবার** (duplicate) থাকতে পারে। মাত্র **৪ KB memory** দিয়ে সব duplicate ছাপতে হবে।

## জরুরি সংখ্যাতত্ত্ব
৪ KB = `4 × 1024 × 8 = 32,768 bit`। আর সংখ্যা বড়জোর ৩২,০০০ পর্যন্ত। মানে **প্রতিটা সম্ভাব্য সংখ্যার জন্য একটা bit** রাখার মতো জায়গা আমাদের আছে! ৩২,৭৬৮ > ৩২,০০০ — ঠিক আঁটে।

## ভাবনা ১: Brute Force
প্রতিটা সংখ্যার জন্য বাকি সব মিলিয়ে দেখা → O(n²)। অথবা Hash Set → O(n) time কিন্তু O(n) memory — ৪ KB-তে ৩২,০০০ সংখ্যার Set আঁটবে না (প্রতি entry অনেক byte)। তাই memory-ই বাধা।

## ভাবনা ২: Optimize — Bit Vector

একটা ৩২,০০০-bit-এর bit vector নিই। প্রতিটা সংখ্যা `n` পড়ার সময়:
- `bit[n]` যদি **আগে থেকে 1** → এই সংখ্যা আগেও দেখেছি → **duplicate, ছাপো**।
- নইলে `bit[n] = 1` করো (প্রথমবার দেখলাম)।

```
array: [1, 2, 3, 2, 5, 1]
 1 → bit[1]=0 → set 1            bits: ..0010
 2 → bit[2]=0 → set 1
 3 → bit[3]=0 → set 1
 2 → bit[2]=1 → DUPLICATE! ছাপো 2
 5 → bit[5]=0 → set 1
 1 → bit[1]=1 → DUPLICATE! ছাপো 1
```

## Code
```dart
// Dart — int-list দিয়ে bit vector (প্রতি int 32 bit)
void printDuplicates(List<int> numbers) {
  final bitset = List<int>.filled((32000 ~/ 32) + 1, 0);
  for (final n in numbers) {
    final idx = n - 1;                       // 1..N কে 0-base করি
    final wordIdx = idx >> 5;                // কোন int
    final bitMask = 1 << (idx & 31);         // কোন bit
    if ((bitset[wordIdx] & bitMask) != 0) {
      print(n);                              // bit আগেই 1 → duplicate
    } else {
      bitset[wordIdx] |= bitMask;            // প্রথমবার → set
    }
  }
}
```
```python
# Python — bytearray দিয়ে bit vector (~4 KB)
def print_duplicates(numbers: list) -> None:
    bitset = bytearray((32000 // 8) + 1)     # ~4 KB
    for n in numbers:
        idx = n - 1                          # 1..N কে 0-base
        byte_idx = idx >> 3                   # কোন byte
        bit_mask = 1 << (idx & 7)             # কোন bit
        if bitset[byte_idx] & bit_mask:       # আগেই 1 → duplicate
            print(n)
        else:
            bitset[byte_idx] |= bit_mask      # প্রথমবার → set
```
> `n - 1` করছি কারণ সংখ্যা `1..N`, কিন্তু bit index `0..N-1`। এতে এক bit-ও নষ্ট হয় না।

## Complexity
**Time: O(n)** — প্রতিটা সংখ্যা একবার পড়ি, bit-অপারেশন O(1)। **Space: O(N) bit = ~৪ KB** (constant, N-এ bound)।

## Pattern চিনুন
> **"সীমিত range-এর integer + খুব কম memory + duplicate/seen খোঁজা" → Hash Set-এর বদলে Bit Vector।** এক সংখ্যা = এক bit, তাই memory ৩২× কম।

## Common mistake
- Hash Set ব্যবহার করা (memory limit ভাঙে — interviewer ঠিক এটাই পরীক্ষা করছে)।
- `n` সরাসরি index ধরা; `1..N` হলে `n-1` করতে ভুলে যাওয়া।
- bit vs byte হিসাবে গুলিয়ে memory ভুল বলা।

## Follow-up
- **range আরও বড় হলে (memory আঁটে না)?** → 10.7-এর মতো দুই-pass bucket পদ্ধতি।
- **duplicate গুনতেও হবে?** → এক bit নয়, ছোট counter দরকার; তখন memory বেশি লাগে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-9"></a>
# 10.9 — Sorted Matrix Search

> Pattern: **উপর-ডান কোণ থেকে হাঁটা (staircase)** · Difficulty: **Medium** · খুব common

> **বইয়ের ভাষায়:** Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.

## সমস্যাটা সহজ বাংলায়
একটা matrix দেওয়া যেখানে **প্রতিটা row বাঁ→ডান sorted** এবং **প্রতিটা column উপর→নিচ sorted**। একটা নির্দিষ্ট value আছে কিনা (এবং কোথায়) খুঁজতে হবে — দ্রুত।

## উদাহরণ

```
     col0 col1 col2 col3
row0  1    4    7   11
row1  2    5    8   12
row2  3    6    9   16
row3 10   13   14   17

খুঁজছি 5  →  (row1, col1)
```

## ভাবনা ১: Brute Force
প্রতিটা ঘর দেখা → O(M·N)। sorted-এর সুবিধা নিইনি।

## ভাবনা ২: প্রতি row-তে binary search
প্রতিটা row sorted, তাই প্রতি row-তে binary search → O(M log N)। ভালো, কিন্তু column-sorted তথ্য কাজে লাগাইনি, আরও ভালো হয়।

## ভাবনা ৩: Optimize — উপর-ডান কোণ থেকে শুরু করো

মূল insight: **উপর-ডান কোণ** থেকে শুরু করি (অথবা নিচ-বাম)। এই কোণের একটা মজার ধর্ম আছে —
- এটা তার **পুরো row-এর সবচেয়ে বড়**, এবং
- তার **পুরো column-এর সবচেয়ে ছোট**।

তাই current-এর সাথে target তুলনা করে এক ধাপে একটা **পুরো row বা পুরো column বাদ** দিতে পারি:

```
target এর চেয়ে current বড়  →  এই column বাদ (col--, বাঁয়ে সরো)
target এর চেয়ে current ছোট  →  এই row বাদ (row++, নিচে নামো)
সমান                        →  পেলাম!
```

```
target = 5, শুরু উপর-ডান (row0,col3)=11
 11 > 5 → col-- → (row0,col2)=7
 7  > 5 → col-- → (row0,col1)=4
 4  < 5 → row++ → (row1,col1)=5
 5  == 5 → পেলাম! (1,1)
```

প্রতি ধাপে এক row বা এক column বাদ → বড়জোর M+N ধাপ → **O(M + N)**।

## Code
```dart
// Dart — উপর-ডান কোণ থেকে staircase
List<int>? searchMatrix(List<List<int>> m, int target) {
  if (m.isEmpty || m[0].isEmpty) return null;
  int row = 0, col = m[0].length - 1;        // উপর-ডান কোণ
  while (row < m.length && col >= 0) {
    final val = m[row][col];
    if (val == target) return [row, col];     // পেলাম
    if (val > target) col--;                  // column বাদ, বাঁয়ে
    else row++;                               // row বাদ, নিচে
  }
  return null;                                // নেই
}
```
```python
# Python — উপর-ডান কোণ থেকে staircase
def search_matrix(m: list, target: int):
    if not m or not m[0]:
        return None
    row, col = 0, len(m[0]) - 1               # উপর-ডান কোণ
    while row < len(m) and col >= 0:
        val = m[row][col]
        if val == target:
            return (row, col)                 # পেলাম
        if val > target:
            col -= 1                           # column বাদ, বাঁয়ে
        else:
            row += 1                           # row বাদ, নিচে
    return None                                # নেই
```

## Complexity
**Time: O(M + N)** — প্রতি ধাপে অন্তত একটা row বা column চিরতরে বাদ। **Space: O(1)**।

## Pattern চিনুন
> **"row ও column দুটোই sorted matrix-এ খোঁজা" → উপর-ডান (বা নিচ-বাম) কোণ থেকে শুরু করে staircase-এর মতো হাঁটো; প্রতি ধাপে একটা পুরো row বা column বাদ।**

## Common mistake
- উপর-**বাম** কোণ থেকে শুরু করা — সেখান থেকে দুই দিকেই বড়, তাই row নাকি column বাদ দেব ঠিক করা যায় না (decision তৈরি হয় না)।
- প্রতি row binary search-কেই optimal ভেবে থেমে যাওয়া (O(M log N), staircase O(M+N) ভালো ও সহজ)।

## Follow-up
- **আরও দ্রুত (sub-linear)?** → matrix কে quadrant-এ ভাগ করে recursive binary-partition (CTCI-এর full solution); তবে staircase সাধারণত যথেষ্ট ও পরিষ্কার।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-10"></a>
# 10.10 — Rank from Stream

> Pattern: **Augmented BST (left-subtree size রাখা)** · Difficulty: **Medium–Hard** · common

> **বইয়ের ভাষায়:** Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x, not including x itself). Implement the data structures and algorithms to support these operations. That is, implement the method `track(int x)`, which is called when each number is generated, and the method `getRankOfNumber(int x)`, which returns the number of values less than or equal to x (not including x itself).

## সমস্যাটা সহজ বাংলায়
সংখ্যা একটার পর একটা **stream**-এ আসছে। যেকোনো সময় জিজ্ঞেস করলে বলতে হবে — "এ পর্যন্ত যত সংখ্যা এসেছে তার মধ্যে কতগুলো `x`-এর চেয়ে **ছোট বা সমান** (নিজে বাদে)?" এটাই `x`-এর **rank**। দুটো method: `track(x)` (নতুন সংখ্যা যোগ) আর `getRankOfNumber(x)` (rank জিজ্ঞেস)।

## উদাহরণ

```
stream এসেছে: 5, 1, 4, 4, 5, 9, 7, 13, 3
getRankOfNumber(1)  → 0   (1-এর চেয়ে ছোট/সমান, নিজে বাদে → কিছু নেই)
getRankOfNumber(3)  → 1   (শুধু 1)
getRankOfNumber(4)  → 3   (1, 3, এবং একটা 4)
```

## ভাবনা ১: Brute Force — array রাখো, প্রতিবার গোনো
সব সংখ্যা একটা list-এ রাখি। `getRankOfNumber(x)` চাইলে পুরো list ঘেঁটে x-এর চেয়ে ছোট গুনি → প্রতি query **O(n)**। sorted রাখলে binary search-এ rank O(log n), কিন্তু `track` (insert) sorted রাখতে O(n)। কোনো-না-কোনো operation ধীর।

## ভাবনা ২: Optimize — Augmented BST

একটা **Binary Search Tree** বানাই, প্রতিটা node-এ একটা extra তথ্য রাখি: **leftSize** = এই node-এর বাঁ-subtree-তে কতগুলো node আছে (অর্থাৎ এই node-এর চেয়ে ছোট কতগুলো এই subtree-তে)।

```
insert করা: 5,1,4,4,5,9,7,13,3

              5(leftSize=3)
             /            \
        1(ls=0)          9(ls=1)
            \           /     \
          4(ls=1)    7(ls=0) 13(ls=0)
          /
       3(ls=0)        (duplicate 4,5 কে ≤ ধরে ডানে রাখা যায়)
```

**`getRankOfNumber(x)`:** root থেকে নামি —
- `x == node.value` → rank += node.leftSize (এই node-এর বাঁয়ের সব ছোট); return।
- `x < node.value` → বাঁয়ে যাও (এই node ও তার ডান কিছুই গোনায় আসে না)।
- `x > node.value` → এই node + তার বাঁ-subtree সব x-এর চেয়ে ছোট → `rank += node.leftSize + 1`, তারপর ডানে যাও।

**`track(x)`:** standard BST insert; পথে যতবার বাঁয়ে নামি না, কিন্তু x যে যে node-এর বাঁ-subtree-তে ঢোকে, সেই node-এর `leftSize++`।

## Code
```dart
// Dart — augmented BST
class RankNode {
  int value;
  int leftSize = 0;          // বাঁ-subtree-তে কতগুলো node
  RankNode? left, right;
  RankNode(this.value);
}

class StreamRank {
  RankNode? root;

  void track(int x) { root = _insert(root, x); }

  RankNode _insert(RankNode? node, int x) {
    if (node == null) return RankNode(x);
    if (x <= node.value) {
      node.leftSize++;                       // x বাঁয়ে গেল
      node.left = _insert(node.left, x);
    } else {
      node.right = _insert(node.right, x);
    }
    return node;
  }

  int getRankOfNumber(int x) => _rank(root, x);

  int _rank(RankNode? node, int x) {
    if (node == null) return -1;             // x stream-এ নেই
    if (x == node.value) return node.leftSize;
    if (x < node.value) return _rank(node.left, x);
    // x > node.value → এই node + বাঁ-subtree সব ছোট
    final right = _rank(node.right, x);
    return right == -1 ? -1 : node.leftSize + 1 + right;
  }
}
```
```python
# Python — augmented BST
class RankNode:
    def __init__(self, value):
        self.value = value
        self.left_size = 0          # বাঁ-subtree-তে কতগুলো node
        self.left = None
        self.right = None

class StreamRank:
    def __init__(self):
        self.root = None

    def track(self, x: int) -> None:
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if node is None:
            return RankNode(x)
        if x <= node.value:
            node.left_size += 1                 # x বাঁয়ে গেল
            node.left = self._insert(node.left, x)
        else:
            node.right = self._insert(node.right, x)
        return node

    def get_rank_of_number(self, x: int) -> int:
        return self._rank(self.root, x)

    def _rank(self, node, x):
        if node is None:
            return -1                           # x stream-এ নেই
        if x == node.value:
            return node.left_size
        if x < node.value:
            return self._rank(node.left, x)
        right = self._rank(node.right, x)       # x বড় → বাঁ-subtree+এই node গোনো
        return -1 if right == -1 else node.left_size + 1 + right
```

## Complexity
**balanced** হলে `track` ও `getRankOfNumber` দুটোই **O(log n)**। **worst case (skewed tree)** → **O(n)**। **Space: O(n)** (সব সংখ্যা node-এ)। balanced BST (যেমন AVL/Red-Black) ব্যবহার করলে worst case-ও O(log n)।

## Pattern চিনুন
> **"stream-এ rank / কতগুলো ছোট / order statistic" → প্রতিটা node-এ left-subtree size রাখা augmented BST।** "এর চেয়ে ছোট কতগুলো" টাইপ query-র classic উত্তর।

## Common mistake
- duplicate (`x <= node.value`) কোন দিকে যাবে ঠিক না করা — না করলে leftSize-এর হিসাব ভুল হয়।
- `x > node.value` ক্ষেত্রে **`node.leftSize + 1`** (current node নিজেও ছোট) যোগ করতে ভুলে যাওয়া।

## Follow-up
- **worst case O(log n) চাই?** → self-balancing BST (AVL/Red-Black) ব্যবহার করো।
- **delete-ও লাগবে?** → delete-এ পথের সব node-এর leftSize ঠিক করতে হবে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q10-11"></a>
# 10.11 — Peaks and Valleys

> Pattern: **এক-pass প্রতিবেশীর সাথে swap** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** In an array of integers, a "peak" is an element which is greater than or equal to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. For example, in the array `{5, 8, 6, 2, 3, 4, 6}`, `{8, 6}` are peaks and `{5, 2}` are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

## সমস্যাটা সহজ বাংলায়
একটা integer array কে এমনভাবে সাজাতে হবে যেন সংখ্যাগুলো **পিক-উপত্যকা-পিক-উপত্যকা** (peak-valley-peak-valley...) ভাবে আঁকাবাঁকা হয়। peak = দুই প্রতিবেশীর চেয়ে বড়-বা-সমান, valley = দুই প্রতিবেশীর চেয়ে ছোট-বা-সমান।

## উদাহরণ

```
input:  [5, 3, 1, 2, 3]
চাই:    valley peak valley peak valley  (index 0,2,4 valley; 1,3 peak)

output (একটা সম্ভাব্য): [1, 5, 2, 3, 3]
                          ↓  ↑  ↓  ↑  ↓
                        valley peak ...   প্রতিবেশীর সাথে শর্ত মানে
```

## ভাবনা ১: Brute Force — আগে sort, তারপর জোড়া swap
পুরো array sort করি, তারপর প্রতি জোড়া element swap করি → আঁকাবাঁকা হয়।
- **Time: O(n log n)** (sort-এর জন্য)। কাজ করে, কিন্তু sort না করেও হয়।

## ভাবনা ২: Optimize — এক pass, শুধু প্রতিবেশীর সাথে swap

মূল insight: **প্রতিটা জোড়া (neighbor) ঠিক থাকলেই পুরো array ঠিক।** তাই sort লাগে না — শুধু একবার হাঁটি এবং local fix করি।

প্রতি **peak position** (index 1, 3, 5, ...)-এ দাঁড়িয়ে নিশ্চিত করি এটা তার বাঁ ও ডান প্রতিবেশীর চেয়ে বড়। কোনো প্রতিবেশী বড় হলে তার সাথে **swap** করি।

```
[5, 3, 1, 2, 3]
i=1 (peak হওয়া উচিত): প্রতিবেশী 5(বাঁ),1(ডান)
   বড় প্রতিবেশী 5 (index 0) → swap(1,0)  → [3, 5, 1, 2, 3]
i=3 (peak): প্রতিবেশী 1(বাঁ),3(ডান)
   বড় প্রতিবেশী 3 (index 4) → swap(3,4)  → [3, 5, 1, 3, 2]
ফল: 3<5>1<3>2  →  valley-peak-valley-peak-valley  (ঠিক)
```

কেন আগের element নষ্ট হয় না? index `i`-তে peak বানাতে আমরা বড়জোর বাঁয়ের (index i-1, যা valley) সাথে swap করি — তাতে valley **আরও ছোট** হয়, তার আগের peak-শর্ত ভাঙে না। তাই এক pass-ই যথেষ্ট।

## Code
```dart
// Dart — এক pass, O(n)
void sortPeaksAndValleys(List<int> a) {
  for (int i = 1; i < a.length; i += 2) {       // শুধু peak position
    int biggest = i;
    if (a[i - 1] > a[biggest]) biggest = i - 1; // বাঁ প্রতিবেশী বড়?
    if (i + 1 < a.length && a[i + 1] > a[biggest]) biggest = i + 1; // ডান?
    if (biggest != i) {                          // swap করে peak বানাও
      final tmp = a[i]; a[i] = a[biggest]; a[biggest] = tmp;
    }
  }
}
```
```python
# Python — এক pass, O(n)
def sort_peaks_and_valleys(a: list) -> None:
    for i in range(1, len(a), 2):           # শুধু peak position
        biggest = i
        if a[i - 1] > a[biggest]:            # বাঁ প্রতিবেশী বড়?
            biggest = i - 1
        if i + 1 < len(a) and a[i + 1] > a[biggest]:   # ডান?
            biggest = i + 1
        if biggest != i:                      # swap করে peak বানাও
            a[i], a[biggest] = a[biggest], a[i]
```

## Complexity
**Time: O(n)** — একবার হাঁটা, প্রতি ধাপে O(1) কাজ (sort লাগে না!)। **Space: O(1)** — in-place swap।

## Pattern চিনুন
> **"alternating / আঁকাবাঁকা / peak-valley সাজানো" → পুরো sort না করে, এক pass-এ প্রতি peak position-এ বড় প্রতিবেশীর সাথে swap করে local condition ঠিক করো।** "local ঠিক → global ঠিক" নীতির সুন্দর উদাহরণ।

## Common mistake
- সবসময় আগে sort করা (O(n log n)) — O(n)-এ হয় বুঝতে না পারা।
- `i + 1` boundary check ভুলে যাওয়া (শেষ peak position-এ ডান প্রতিবেশী নাও থাকতে পারে)।
- valley position-এও আলাদা করে কাজ করা — শুধু peak ঠিক করলেই যথেষ্ট।

## Follow-up
- **strictly peak/valley (সমান চলবে না)?** → duplicate থাকলে অসম্ভব হতে পারে; clarify করতে হবে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---
---

# Chapter 10 — সারসংক্ষেপ ও Pattern Cheat Sheet

| # | প্রশ্ন | মূল technique | Time | Space |
|---|---|---|---|---|
| 10.1 | Sorted Merge | পিছন থেকে two-pointer merge | O(A+B) | O(1) |
| 10.2 | Group Anagrams | sorted-string কে Map key | O(n·s log s) | O(n·s) |
| 10.3 | Search in Rotated Array | modified binary search | O(log n) | O(1) |
| 10.4 | Sorted Search, No Size | exponential boundary + binary search | O(log n) | O(1) |
| 10.5 | Sparse Search | binary search + empty skip | O(log n)\* | O(1) |
| 10.6 | Sort Big File | external merge sort | O(n log n) | O(RAM) |
| 10.7 | Missing Int | bit vector / bucket দুই-pass | O(n) | 512 MB / 10 MB |
| 10.8 | Find Duplicates | bit vector | O(n) | ~4 KB |
| 10.9 | Sorted Matrix Search | উপর-ডান কোণ staircase | O(M+N) | O(1) |
| 10.10 | Rank from Stream | augmented BST (leftSize) | O(log n)\*\* | O(n) |
| 10.11 | Peaks and Valleys | এক-pass প্রতিবেশী swap | O(n) | O(1) |

`*` worst case O(n) (অনেক empty) · `**` balanced হলে; skewed হলে O(n)

### "এটা দেখলে → এটা ভাবো" (signal → technique)
```
দুটো sorted array merge, শেষে জায়গা    →  পিছন থেকে two-pointer
anagram একসাথে গোছাও                   →  sorted-string = Map key
sorted কিন্তু rotated                  →  modified binary search (কোন অর্ধেক sorted?)
size/length জানা নেই                   →  exponential দিয়ে boundary, পরে binary search
sorted-এ মাঝে empty / অর্থহীন element   →  binary search, mid খারাপ হলে কাছেরটায় সরো
GB-scale / RAM-এ ধরে না                →  external merge sort
বিশাল integer + সীমিত memory + missing  →  bit vector (কম হলে bucket দুই-pass)
সীমিত range integer + duplicate         →  bit vector (Hash Set নয়)
row+col sorted matrix                  →  উপর-ডান কোণ থেকে staircase walk
stream-এ rank / কতগুলো ছোট             →  augmented BST (left-subtree size)
alternating / peak-valley সাজানো        →  এক pass, peak-এ বড় প্রতিবেশীর সাথে swap
```

### এই chapter-এর ৫টা সোনার নিয়ম
1. **"sorted" + "খোঁজা" = binary search।** rotated/no-size/sparse — সবই binary search-এর বদলানো রূপ।
2. **পিছন থেকে লেখা** (10.1) — গন্তব্যে খালি জায়গা থাকলে overwrite এড়ানোর চাবি।
3. **Bit Vector** (10.7, 10.8) — সীমিত-range integer-এ Hash Set-এর জায়গায় ৩২× কম memory।
4. **"RAM-এ ধরে না"** শুনলেই external merge sort / streaming / bucket — পুরোটা একসাথে আনার চেষ্টা নয়।
5. **Augmented data structure** (10.10) — সাধারণ structure-এ extra তথ্য (leftSize) রেখে নতুন query দ্রুত করা।

> **পরের ধাপ:** [Chapter 11 — Testing](chapter11_testing.md) (11.1–11.6), যেখানে code কম, কিন্তু "ভালো test case কীভাবে ভাবি" — normal/edge/stress — সেটা শিখব।

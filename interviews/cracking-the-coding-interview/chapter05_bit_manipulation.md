# Chapter 5 — Bit Manipulation (প্রশ্ন 5.1 – 5.8)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। Code **Dart + Python** দুটোতেই।
> Bit manipulation প্রথম দেখলে ভয় লাগে — কিন্তু মাত্র কয়েকটা নিয়ম আয়ত্ত করলে এই chapter-এর সব সমাধান নিজেই বের করা যায়।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: Trees & Graphs](chapter04_trees_graphs.md) · [পরের: Math & Logic Puzzles](chapter06_math_logic_puzzles.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
Background — binary, two's complement, operators, essential bit tricks (অবশ্যই আগে পড়ুন)

5.1  Insertion           — একটা number অন্য number-এর নির্দিষ্ট bit range-এ ঢোকানো
5.2  Binary to String    — 0 থেকে 1-এর মধ্যে decimal কে binary string-এ রূপান্তর
5.3  Flip Bit to Win     — একটা bit উল্টে পাওয়া সবচেয়ে লম্বা 1-এর series
5.4  Next Number         — একই সংখ্যক 1-bit সহ পরের বড় ও পরের ছোট number
5.5  Debugger            — ((n & (n-1)) == 0) কী করে?
5.6  Conversion          — দুটো number-এর মধ্যে কতগুলো bit আলাদা
5.7  Pairwise Swap       — জোড়/বিজোড় bit-এর অবস্থান একে অপরের সাথে বদলানো
5.8  Draw Line           — একটা ছবিতে horizontal line আঁকা
```

- [5.1 — Insertion](#q5-1)
- [5.2 — Binary to String](#q5-2)
- [5.3 — Flip Bit to Win](#q5-3)
- [5.4 — Next Number](#q5-4)
- [5.5 — Debugger](#q5-5)
- [5.6 — Conversion](#q5-6)
- [5.7 — Pairwise Swap](#q5-7)
- [5.8 — Draw Line](#q5-8)

প্রতিটা প্রশ্ন এই কাঠামোয়: **সহজ বাংলায় সমস্যা → উদাহরণ (ASCII binary diagram) → Listen → Brute force → Optimize (BUD) → Code (Dart+Python) → Complexity → Pattern → Common mistake → Follow-up।**

---
---

# Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

## ১. Binary Representation — number কীভাবে bit-এ থাকে

Computer সব number **binary (base-2)** তে রাখে। প্রতিটা ঘরকে বলে **bit** — মান হয় `0` বা `1`।

```
Decimal 13 কে binary-তে লিখি:
  13 = 8 + 4 + 1
     = 2³ + 2² + 2⁰

  bit position:   7   6   5   4   3   2   1   0
                ┌───┬───┬───┬───┬───┬───┬───┬───┐
  value (8-bit): │ 0 │ 0 │ 0 │ 0 │ 1 │ 1 │ 0 │ 1 │
                └───┴───┴───┴───┴───┴───┴───┴───┘
                                  ↑   ↑       ↑
                                 8   4        1   = 13

  পড়ার নিয়ম: ডান থেকে বাম — bit 0 (সবচেয়ে ডানে) = সবচেয়ে ছোট (LSB),
              bit 7 (সবচেয়ে বামে) = সবচেয়ে বড় (MSB)।
```

**Decimal → Binary রূপান্তর (হাতে):** বারবার 2 দিয়ে ভাগ করুন, ভাগশেষ নিন। নিচ থেকে উপরে পড়ুন।

```
13 ÷ 2 = 6 ভাগশেষ 1   ←  bit 0
 6 ÷ 2 = 3 ভাগশেষ 0   ←  bit 1
 3 ÷ 2 = 1 ভাগশেষ 1   ←  bit 2
 1 ÷ 2 = 0 ভাগশেষ 1   ←  bit 3
                          উপরে পড়ো: 1101  
```

## ২. Two's Complement — negative number-এর binary

Computer negative number রাখে **two's complement** পদ্ধতিতে। 32-bit int-এ সবচেয়ে বাম bit হলো **sign bit**: 0 মানে positive, 1 মানে negative।

**-N বের করার নিয়ম:**
1. N-এর সব bit উল্টে দাও (NOT করো)।
2. তাতে 1 যোগ করো।

```
উদাহরণ: -5 বের করব (8-bit এ)

ধাপ 1: 5 = 0000 0101
ধাপ 2: সব bit উল্টাও → 1111 1010
ধাপ 3: 1 যোগ করো    → 1111 1011   ← এটাই -5

যাচাই: 5 + (-5) = 0
  0000 0101
+ 1111 1011
-----------
  0000 0000  (carry উপচে পড়ে যায়, result = 0) 
```

**গুরুত্বপূর্ণ:** 8-bit-এ -1 হলো `1111 1111`, -128 হলো `1000 0000`, 127 হলো `0111 1111`।

## ৩. Bit Operators — ৬টা operator জানতে হবে

### AND ( & ) — দুটো bit-ই 1 হলে 1, নইলে 0
```
  1 1 0 1 0 1 1 0   (= 214)
& 1 0 1 1 0 0 1 1   (= 179)
─────────────────
  1 0 0 1 0 0 1 0   (= 146)

Truth table:
  0 & 0 = 0
  0 & 1 = 0
  1 & 0 = 0
  1 & 1 = 1   ← দুটোই 1 তবেই 1
```

### OR ( | ) — যেকোনো একটা 1 হলে 1
```
  1 1 0 1 0 1 1 0   (= 214)
| 1 0 1 1 0 0 1 1   (= 179)
─────────────────
  1 1 1 1 0 1 1 1   (= 247)

Truth table:
  0 | 0 = 0
  0 | 1 = 1
  1 | 0 = 1
  1 | 1 = 1   ← অন্তত একটা 1 হলেই 1
```

### XOR ( ^ ) — দুটো আলাদা হলে 1, সমান হলে 0
```
  1 1 0 1 0 1 1 0   (= 214)
^ 1 0 1 1 0 0 1 1   (= 179)
─────────────────
  0 1 1 0 0 1 0 1   (= 101)

Truth table:
  0 ^ 0 = 0
  0 ^ 1 = 1
  1 ^ 0 = 1
  1 ^ 1 = 0   ← সমান হলে 0 (toggle!)
```

XOR-এর গুরুত্বপূর্ণ বৈশিষ্ট্য:
- `a ^ a = 0` (নিজের সাথে XOR = 0)
- `a ^ 0 = a` (0-এর সাথে XOR = নিজেই)
- `a ^ b ^ a = b` (একই জিনিস দুবার XOR করলে বাদ যায়)

### NOT ( ~ ) — প্রতিটা bit উল্টে দাও
```
~  0 0 0 0 1 1 0 1   (= 13)
─────────────────
   1 1 1 1 0 0 1 0   (= -14, two's complement-এ)

নিয়ম: ~n = -(n+1)   সবসময়
       ~13 = -14 
```

### Left Shift ( << ) — সব bit বামে সরাও, ডানে 0 ঢোকে
```
  0 0 0 0 1 1 0 1   (= 13)
<< 2 (দুই ঘর বামে)
─────────────────
  0 0 1 1 0 1 0 0   (= 52)

প্রতিবার 1 ঘর বামে সরানো = 2 দিয়ে গুণ করা।
n << k = n × 2^k
```

### Right Shift ( >> , >>> ) — সব bit ডানে সরাও
```
Arithmetic right shift (>> , sign-bit রক্ষা করে):
  1 1 1 1 0 1 0 0   (= -12, signed)
>> 2
─────────────────
  1 1 1 1 1 1 0 1   (= -3)   ← বামে sign bit (1) ঢোকে

Logical right shift (>>> , সবসময় 0 ঢোকে):
  1 1 1 1 0 1 0 0   (= -12 / 244 unsigned)
>>> 2
─────────────────
  0 0 1 1 1 1 0 1   (= 61)   ← বামে 0 ঢোকে

Dart-এ >>> আছে (logical); Python-এ >> সবসময় arithmetic।
n >> k = n ÷ 2^k (integer division, positive n-এর জন্য)
```

## ৪. Essential Bit Tricks — এগুলো মুখস্থ করুন

### Get bit — i-তম bit কী? (0 বা 1)
```
mask = 1 << i   (i-তম স্থানে শুধু 1)
result = (n & mask) != 0

উদাহরণ: n = 1101, bit 2 টা কী?
mask = 0100
n & mask = 0100 → != 0 → bit 2 = 1  
```

### Set bit — i-তম bit কে 1 করো
```
n = n | (1 << i)

উদাহরণ: n = 1001, bit 1 set করব
1 << 1 = 0010
n | 0010 = 1011  
```

### Clear bit — i-তম bit কে 0 করো
```
n = n & ~(1 << i)

উদাহরণ: n = 1101, bit 2 clear করব
1 << 2    = 0100
~(1 << 2) = 1011
n & 1011  = 1001  
```

### Update bit — i-তম bit কে v (0 বা 1) বানাও
```
n = (n & ~(1 << i)) | (v << i)
   ──── bit clear ────  + ── bit set ──
```

### x & (x-1) — সবচেয়ে ডানের 1-bit মুছে ফেলে
```
x     = 1 0 1 1 0 0   (44)
x - 1 = 1 0 1 0 1 1   (43)
─────────────────────
x & (x-1) = 1 0 1 0 0 0   (40)
                   ↑
             এই 1-bit টা গেছে!

কাজে লাগে: 1-bit গোনা, power-of-2 চেক।
```

### x & (-x) — সবচেয়ে ডানের 1-bit শুধু রাখে (বাকি সব 0)
```
x    = 1 0 1 1 0 1 0 0   (180)
-x   = 0 1 0 0 1 1 0 0   (two's complement)
────────────────────────
x&-x = 0 0 0 0 0 1 0 0   ← শুধু সবচেয়ে ডানের 1-bit
```

### n == 0 হলে (n & (n-1)) == 0 মানে n হলো 2-এর ঘাত
```
n = 8  = 1000
n-1 = 7 = 0111
n & (n-1) = 0000 → true, 8 = 2³ 

n = 6  = 0110
n-1 = 5 = 0101
n & (n-1) = 0100 → != 0 → false, 6 ≠ 2^k 
```

---
---

<a id="q5-1"></a>
# 5.1 — Insertion

> Pattern: **Bit masking (clear + set)** · Difficulty: **Medium** · মাঝে মাঝে আসে

> **বইয়ের ভাষায়:** You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough room to fit all of M.
> Example: N = 10000000000, M = 10011, i = 2, j = 6 → N = 10001001100

## সমস্যাটা সহজ বাংলায়

দুটো number দেওয়া: N (বড়) আর M (ছোট)। N-এর bit i থেকে bit j পর্যন্ত অংশটা মুছে দিয়ে সেখানে M বসাতে হবে। বাকি bit গুলো অপরিবর্তিত থাকবে।

ভাবুন N একটা পুরনো ছবি, আর M একটা নতুন ছোট টুকরা — নির্দিষ্ট জায়গায় আটকে দিতে হবে।

## উদাহরণ (ASCII binary diagram)

```
N = 1 0 0 0 0 0 0 0 0 0 0   (11-bit এ দেখাচ্ছি)
    bit: 10 9 8 7 6 5 4 3 2 1 0

M = 1 0 0 1 1   (5-bit)
    i=2, j=6

কাজ: N-এর bit 2 থেকে bit 6 (মোট 5 bit) পরিষ্কার করো, তারপর M বসাও।

আগে:  1 0 0 0 0 [0 0 0 0 0] 0  ← [ ] ঘরগুলো বদলাবে
                 ↑         ↑
                j=6       i=2

পরে:  1 0 0 0 0 [1 0 0 1 1] 0 0  →  1 0 0 0 1 0 0 1 1 0 0
```

## ধাপ ১: Listen
- i এবং j দেওয়া, এবং j >= i সবসময়।
- M যথেষ্ট ছোট যাতে (j - i + 1) bit-এ আঁটে।
- 32-bit signed integer ধরা হবে।

## ভাবনা: Brute Force থেকে শুরু
সরাসরি bit-by-bit করা যায়: M-এর প্রতিটা bit পড়ে N-এ set করা।
- **Time: O(j - i)** · **Space: O(1)**
- কিন্তু masking দিয়ে আরও পরিষ্কার করা যায়।

## Optimize — তিনটা ধাপ

```
ধাপ 1: N-এর bit i থেকে j পরিষ্কার করো (clear)
        mask বানাই যাতে bit i..j = 0, বাকি = 1:

        all ones:   1 1 1 1 1 1 1 1   (0xFFFFFFFF)
        left part:  1 1 1 1 1 0 0 0   (শুধু j-এর উপরে, -1 << (j+1))
        right part: 0 0 0 0 0 0 1 1   (শুধু i-এর নিচে, (1 << i) - 1)
        mask:       1 1 1 1 1 0 0 0
                  | 0 0 0 0 0 0 1 1
                  = 1 1 1 1 1 0 0 1 1   ← bit i..j = 0, বাকি = 1
        N_cleared = N & mask

ধাপ 2: M কে সঠিক জায়গায় shift করো
        M_shifted = M << i

ধাপ 3: দুটো OR করো
        result = N_cleared | M_shifted
```

বিস্তারিত diagram:

```
N        = 1 0 0 0 0 0 0 0 0 0 0   (bit 10..0)
mask     = 1 1 1 1 1 0 0 0 0 0 1 1  (উপরে আর নিচে 1, মাঝে 0)
N & mask = 1 0 0 0 0 0 0 0 0 0 0   (bit 6..2 পরিষ্কার)

M        =         1 0 0 1 1        (decimal 19)
M << 2   = 0 0 0 0 1 0 0 1 1 0 0   (i=2 ঘর বামে)

OR:
N&mask   = 1 0 0 0 0 0 0 0 0 0 0
M<<2     = 0 0 0 0 1 0 0 1 1 0 0
─────────────────────────────────
result   = 1 0 0 0 1 0 0 1 1 0 0   
```

## Code

```dart
// Dart
int insertion(int n, int m, int i, int j) {
  // ধাপ 1: bit i থেকে j পরিষ্কার করার mask বানাই
  // left part: bit j-এর উপরে সব 1  →  -1 << (j + 1)
  // right part: bit i-এর নিচে সব 1  →  (1 << i) - 1
  // Dart-এ signed int ব্যবহার হয়; -1 = 0xFFFFFFFF...
  final allOnes = ~0;                       // সব bit 1
  final left = allOnes << (j + 1);          // bit j+1 থেকে উপরে সব 1
  final right = (1 << i) - 1;              // bit 0 থেকে i-1 পর্যন্ত সব 1
  final mask = left | right;               // bit i..j = 0, বাকি = 1

  // ধাপ 2 ও 3
  final nCleared = n & mask;               // bit i..j পরিষ্কার
  final mShifted = m << i;                 // M কে সঠিক জায়গায়
  return nCleared | mShifted;             // জোড়া লাগাও
}

void main() {
  // N = 1024 (10000000000), M = 19 (10011), i=2, j=6
  print(insertion(1024, 19, 2, 6).toRadixString(2)); // 10001001100
}
```

```python
# Python
def insertion(n: int, m: int, i: int, j: int) -> int:
    # ধাপ 1: mask বানাই
    all_ones = ~0                         # Python-এ arbitrary precision int
    left = all_ones << (j + 1)           # bit j+1 থেকে উপরে সব 1
    right = (1 << i) - 1                 # bit 0 থেকে i-1 সব 1
    mask = left | right                  # bit i..j = 0, বাকি = 1

    # ধাপ 2 ও 3
    n_cleared = n & mask                 # bit i..j পরিষ্কার
    m_shifted = m << i                   # M কে সঠিক জায়গায়
    return n_cleared | m_shifted        # জোড়া লাগাও

# যাচাই
result = insertion(0b10000000000, 0b10011, 2, 6)
print(bin(result))   # 0b10001001100  
```

## Complexity
**Time: O(1)** (fixed 32-bit — constant number of operations) · **Space: O(1)**।

## Pattern চিনুন
> **"নির্দিষ্ট bit range বদলাও" → তিন ধাপ: clear mask বানাও → M shift করো → OR দিয়ে জোড়া লাগাও।**
> Mask বানানোর ফর্মুলা: left = `-1 << (j+1)`, right = `(1 << i) - 1`, mask = `left | right`।

## Common mistake
- mask-এ শুধু left অথবা শুধু right করা — দুটো মিলিয়ে বানাতে হবে।
- M shift করতে ভুলে যাওয়া।
- Dart-এ `~0` negative — Python-এ `~0 = -1` কিন্তু arbitrary precision, তাই masking একটু ভিন্ন আচরণ করতে পারে। 32-bit-এ আটকাতে চাইলে `& 0xFFFFFFFF` করুন।

## Follow-up
- **i এবং j সঠিক কিনা validate করতে হবে** (j >= i, M (j-i+1)-bit-এ আঁটে) — production code-এ এই check যোগ করুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q5-2"></a>
# 5.2 — Binary to String

> Pattern: **Bit extraction (fraction)** · Difficulty: **Easy–Medium** · মাঝে মাঝে আসে

> **বইয়ের ভাষায়:** Given a real number between 0 and 1 (e.g., 0.72) passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".

## সমস্যাটা সহজ বাংলায়

`0.0` থেকে `1.0`-এর মধ্যে একটা decimal fraction দেওয়া। এটাকে **binary fraction** হিসেবে লিখতে হবে — যেমন `0.5` → `"0.1"`, `0.625` → `"0.101"`। ৩২ character-এর বেশি লাগলে "ERROR" দাও।

## উদাহরণ (ASCII diagram)

```
Binary fraction কীভাবে কাজ করে:

0.101 (binary) = 1×2^(-1) + 0×2^(-2) + 1×2^(-3)
               = 0.5 + 0 + 0.125
               = 0.625 (decimal)

প্রতিটা bit নির্ধারণ করি ×2 করে:
  num = 0.625

  num × 2 = 1.25  → integer part = 1  → bit "1"  → num = 0.25
  num × 2 = 0.5   → integer part = 0  → bit "0"  → num = 0.5
  num × 2 = 1.0   → integer part = 1  → bit "1"  → num = 0.0
  num = 0, শেষ!

  result: "0.101"  
```

**কেন ×2?** Binary-তে `.` এর পরে প্রতিটা bit 2^(-k)। গুণ করলে সেই bit integer part-এ চলে আসে।

## ধাপ ১: Listen
- Input সবসময় 0 এবং 1-এর মধ্যে।
- 32 character limit (দশমিক বিন্দু `"0."` সহ বা ছাড়া? — বইয়ে bit সংখ্যা 32)।
- Floating-point precision নিয়ে সতর্ক থাকতে হবে।

## Brute Force ও Optimal একই — bit by bit বের করা

```
algorithm:
  result = "0."
  loop যতক্ষণ num != 0:
    যদি result.length > 34 (যেমন "0." + 32 bit) → "ERROR"
    num = num * 2
    যদি num >= 1:
      result += "1"
      num -= 1
    নইলে:
      result += "0"
```

## Code

```dart
// Dart
String binaryToString(double num) {
  if (num <= 0 || num >= 1) return 'ERROR';  // boundary check
  final sb = StringBuffer('0.');
  while (num > 0) {
    if (sb.length >= 34) return 'ERROR';     // "0." + 32 bit = 34 character
    num *= 2;
    if (num >= 1) {
      sb.write('1');
      num -= 1;
    } else {
      sb.write('0');
    }
  }
  return sb.toString();
}

void main() {
  print(binaryToString(0.625));   // "0.101"
  print(binaryToString(0.1));     // "ERROR" (0.1 binary-তে repeating)
  print(binaryToString(0.5));     // "0.1"
}
```

```python
# Python
def binary_to_string(num: float) -> str:
    if num <= 0 or num >= 1:
        return 'ERROR'
    result = ['0', '.']
    while num > 0:
        if len(result) >= 34:           # "0." + 32 bit = 34 character
            return 'ERROR'
        num *= 2
        if num >= 1:
            result.append('1')
            num -= 1
        else:
            result.append('0')
    return ''.join(result)

print(binary_to_string(0.625))   # "0.101"
print(binary_to_string(0.1))     # "ERROR"
print(binary_to_string(0.5))     # "0.1"
```

## Complexity
**Time: O(1)** (loop সর্বোচ্চ 32 বার চলে, fixed) · **Space: O(1)**।

## Pattern চিনুন
> **"Fraction কে binary-তে রূপান্তর" → বারবার 2 গুণ করো, integer part-ই পরের bit।** এটা integer কে binary-তে রূপান্তরের (বারবার 2 ভাগ করা, ভাগশেষ bit) mirror/উল্টো।

## Common mistake
- `num == 0` check না করলে infinite loop।
- 32 character limit-এর গণনায় `"0."` prefix ভুলে যাওয়া।
- `0.1` binary-তে exact representation নেই — floating-point precision error-এ ৩২-এর বেশি bit লাগতে পারে → "ERROR"।

## Follow-up
- **Integer অংশ থাকলে?** (যেমন `3.625`) → Integer অংশ আলাদা করো (regular binary), decimal অংশ এই method-এ।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q5-3"></a>
# 5.3 — Flip Bit to Win

> Pattern: **Sliding window (longest sequence)** · Difficulty: **Medium** · মোটামুটি common

> **বইয়ের ভাষায়:** You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.
> Example: 1775 (11011101111) → 8

## সমস্যাটা সহজ বাংলায়

একটা integer দেওয়া। ঠিক **একটা 0-bit কে 1 করে দিতে পারবেন** (flip)। এতে পাওয়া **সবচেয়ে লম্বা পরপর 1-এর দল** কত?

## উদাহরণ (ASCII diagram)

```
n = 1775  →  binary: 1 1 0 1 1 1 0 1 1 1 1
                     ↑↑   ↑↑↑↑   ↑↑↑↑↑
             bit: 10 9 8 7 6 5 4 3 2 1 0

এই 0-গুলো একটা করে flip করে দেখি কোনটায় সবচেয়ে লম্বা 1-এর run পাই:

bit 8 flip → 1 1 1 1 1 1 0 1 1 1 1 → run: [6 টা 1] + [4 টা 1] → consecutive = 7
bit 4 flip → 1 1 0 1 1 1 1 1 1 1 1 → run: [2 টা 1] + [7 টা 1] → consecutive = 8 ← সেরা!

উত্তর: 8
```

## ধাপ ১: Listen
- Integer 32-bit (signed)।
- সবগুলো bit 1 থাকলে? → উত্তর 32।
- Negative number সামলানো দরকার (sign bit সহ সব 32 bit)।

## ভাবনা ১: Brute Force
প্রতিটা 0-bit flip করে দেখি সবচেয়ে লম্বা consecutive 1-run কত — তারপর সর্বোচ্চ নিই।
- **Time: O(b²)** (b = bit সংখ্যা = 32, তাই আসলে O(1) কিন্তু ধারণাটা দরকারী) · **Space: O(1)**।

## ভাবনা ২: Optimal — Sliding Window / two run tracking

একটা 0 flip করলে সে দুটো 1-run-কে যোগ করে দেয়। তাই আমি শুধু ট্র্যাক করব: **এখনকার run** আর **আগের run** (তার আগে ছিল 0)।

```
Bit by bit বাম থেকে ডানে (অথবা ডান থেকে বাম) হাঁটি।
currentLen = এখন যতগুলো পরপর 1 দেখছি
prevLen    = সবশেষ 0-এর আগে ছিল কতগুলো 1

প্রতিটা bit:
  1 → currentLen++
  0 → পরের bit যদি 1: prevLen = currentLen, currentLen = 0
       পরের bit যদি 0: prevLen = 0, currentLen = 0
       (কারণ দুটো 0 মানে এই flip একটামাত্র 0 সেতু দিতে পারবে না)

answer = max(answer, prevLen + 1 + currentLen)
         ↑ আগের run + flip করা 0 + এখনকার run
```

বিস্তারিত trace:

```
n = 1775 = 1 1 0 1 1 1 0 1 1 1 1
           bit 10→0 এ যাচ্ছি ডান থেকে:

bit 0: 1 → cur=1, prev=0, max=prev+1+cur=2
bit 1: 1 → cur=2, prev=0, max=3
bit 2: 1 → cur=3, prev=0, max=4
bit 3: 1 → cur=4, prev=0, max=5
bit 4: 0 → পরের bit (bit 5) = 1, তাই prev=4, cur=0
bit 5: 1 → cur=1, max=prev+1+cur=4+1+1=6
bit 6: 1 → cur=2, max=4+1+2=7
bit 7: 1 → cur=3, max=4+1+3=8
bit 8: 0 → পরের bit (bit 9) = 1, তাই prev=3, cur=0
bit 9: 1 → cur=1, max=3+1+1=5 (আগের 8 > 5, রইলো 8)
bit 10:1 → cur=2, max=3+1+2=6 (আগের 8 এখনো বড়)

উত্তর: 8 
```

## Code

```dart
// Dart
int flipBitToWin(int n) {
  // সব bit 1 → 32
  if (~n == 0) return 32;   // ~n == 0 মানে n = 0xFFFFFFFF (সব 1)

  int currentLen = 0;   // এখনকার 1-run
  int prevLen = 0;      // আগের 1-run (একটা 0 পার হয়ে এসেছে)
  int maxLen = 1;       // অন্তত 1 (যেকোনো bit flip করলে ১টা 1 তো পাবোই)

  while (n != 0) {
    if ((n & 1) == 1) {
      // bit = 1
      currentLen++;
    } else {
      // bit = 0
      // পরের bit (n >>> 1 & 1) = 0 হলে আগের run ব্যবহার করা যাবে না
      prevLen = ((n & 2) == 0) ? 0 : currentLen;
      currentLen = 0;
    }
    maxLen = maxLen > prevLen + 1 + currentLen
        ? maxLen
        : prevLen + 1 + currentLen;
    n >>>= 1;   // logical right shift (Dart >>>)
  }
  return maxLen;
}

void main() {
  print(flipBitToWin(1775));   // 8
  print(flipBitToWin(-1));     // 32 (সব 1)
  print(flipBitToWin(0));      // 1 (একটা 0 flip করলে 1 পাবো)
}
```

```python
# Python — 32-bit unsigned-এর মতো treat করতে masking করি
def flip_bit_to_win(n: int) -> int:
    # Python arbitrary int — 32-bit এ সীমাবদ্ধ করি
    if n < 0:
        n = n & 0xFFFFFFFF   # 32-bit unsigned representation

    if n == 0xFFFFFFFF:
        return 32

    current_len = 0
    prev_len = 0
    max_len = 1

    while n != 0:
        if n & 1:                        # bit = 1
            current_len += 1
        else:                            # bit = 0
            prev_len = 0 if (n & 2) == 0 else current_len
            current_len = 0
        max_len = max(max_len, prev_len + 1 + current_len)
        n >>= 1
    return max_len

print(flip_bit_to_win(1775))    # 8
print(flip_bit_to_win(-1))      # 32
print(flip_bit_to_win(0))       # 1
```

## Complexity
**Time: O(b)** যেখানে b = bit সংখ্যা (32) → effective **O(1)** · **Space: O(1)**।

## Pattern চিনুন
> **"একটা জিনিস বদলে সবচেয়ে লম্বা run/sequence" → Sliding window বা two-pointer।** এখানে window হলো: "আগের run + এই 0 + এখনকার run" — আগের 0 পার হওয়ামাত্র window পিছিয়ে যায়।

## Common mistake
- দুটো 0 পরপর আসলে `prevLen` কে 0 করতে ভুলে যাওয়া।
- Negative number বা all-1s edge case মিস করা।
- Dart-এ `>>` arithmetic (sign bit রক্ষা করে) — negative-এ চিরতরে loop চলতে পারে! `>>>` (logical shift) ব্যবহার করুন।

## Follow-up
- **যেকোনো সংখ্যক bit flip করা যাবে?** → Sliding window with k zeros allowed (classic pattern)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q5-4"></a>
# 5.4 — Next Number

> Pattern: **Bit counting + manipulation** · Difficulty: **Hard** · কম common কিন্তু চালাকি শেখায়

> **বইয়ের ভাষায়:** Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.

## সমস্যাটা সহজ বাংলায়

একটা positive integer দেওয়া। বলতে হবে:
1. এর চেয়ে **বড়** কিন্তু **একই সংখ্যক 1-bit** আছে এমন পরবর্তী number।
2. এর চেয়ে **ছোট** কিন্তু **একই সংখ্যক 1-bit** আছে এমন পরবর্তী number।

## উদাহরণ

```
n = 13948  →  binary: 1 1 0 1 1 0 0 1 1 1 1 1 0 0
                      bit: 13 12 11 10 9 8 7 6 5 4 3 2 1 0
1-bit count: 9

পরের বড়  (next largest):  14004  =  1 1 0 1 1 0 1 1 0 0 1 1 1 1 0 0
পরের ছোট (next smallest): 13946  =  1 1 0 1 1 0 0 1 1 1 1 0 1 1

দুটোতেই 1-bit = 9 
```

## ধাপ ১: Listen
- Positive integer শুধু।
- n = 0 বা সব bit 1 হলে → next largest বা next smallest নেই (overflow/underflow)।

## ভাবনা: Brute Force
n+1 থেকে উপরে যাই যতক্ষণ না একই 1-bit count পাই (largest), একইভাবে n-1 থেকে নিচে (smallest)।
- Worst case: **O(n)** — যেমন n = 0b0111...1 হলে অনেক দূর যেতে হয়। Bit manipulation দিয়ে O(1)-এ করা যায়।

## Optimize — Bit Pattern Analysis

### পরের বড় number (getNext)

**মূল idea:** সবচেয়ে ডানে এমন একটা `01` pattern খুঁজি যেটাকে `10` করা যায় (এতে number বাড়বে), তারপর বাকি 1-bit গুলো যতটা সম্ভব ডানে গুছিয়ে রাখি (number ছোট রাখতে)।

```
ধাপ-by-ধাপ (n = 13948 = ...11011001111100):

ডান থেকে গুনি:
  c0 = ডানদিকের 0-এর সংখ্যা (trailing zeros)
  c1 = তার পরের 1-এর সংখ্যা (1-run আগে পরের 0)

উদাহরণ: 1 1 0 1 1 0 0 1 1 1 1 1 0 0
  trailing 0: c0 = 2
  তারপর 1-run: c1 = 5

p = c0 + c1 = 7  ← এই position-এ একটা 0→1 flip করব

ধাপ 1: bit p কে 1 করো (যেখানে 0→1 flip হবে)
  n |= 1 << p

ধাপ 2: bit p-এর ডানে সব bit 0 করো
  n &= ~((1 << p) - 1)

ধাপ 3: ডানদিকে (c1-1)টা 1-bit বসাও (সর্বোচ্চ ডানে)
  n |= (1 << (c1 - 1)) - 1

ব্যাখ্যা: bit p-এ 0→1 flip করে 1-bit বাড়ল 1, কিন্তু
  আগের (c1+1)টা bit-এর জায়গায় এখন আছে 1টা (bit p) + (c1-1)টা (ডানে)।
  মোট 1-bit = c1 + আগের বাকি 1-bit 
```

### পরের ছোট number (getPrev)

**মূল idea:** সবচেয়ে ডানে `10` pattern খুঁজি, সেটাকে `01` করি (number কমবে), তারপর 1-bit গুলো ওই 10-এর ঠিক বামে গুছাই (number বড় রাখতে, কিন্তু minimum পার্থক্যে)।

```
ডান থেকে গুনি:
  c0 = trailing 1-এর সংখ্যা
  c1 = তার পরের 0-এর সংখ্যা (0-run)

p = c0 + c1  ← এখানে 1→0 flip করব

ধাপ 1: bit p কে 0 করো  →  n &= ~(1 << p)
ধাপ 2: bit p-এর ডানে সব 0 করো  →  n &= ~((1 << p) - 1)
ধাপ 3: bit (p-1) থেকে শুরু করে (c1+1)টা 1 বসাও
  n |= ((1 << (c1 + 1)) - 1) << (c0 - 1)
```

## Code

```dart
// Dart
int getNext(int n) {
  int temp = n;
  int c0 = 0, c1 = 0;

  // ডান থেকে 0 গুনি
  while (temp != 0 && (temp & 1) == 0) { c0++; temp >>= 1; }
  // তারপর 1 গুনি
  while (temp != 0 && (temp & 1) == 1) { c1++; temp >>= 1; }

  // Edge: 0b0...01...10...0 বা সব 0/1 → next largest নেই
  if (c0 + c1 == 31 || c0 + c1 == 0) return -1;

  final p = c0 + c1;   // flip করার position

  n |= (1 << p);                   // bit p → 1
  n &= ~((1 << p) - 1);            // bit p-এর ডানে সব 0
  n |= (1 << (c1 - 1)) - 1;       // ডানদিকে (c1-1)টা 1
  return n;
}

int getPrev(int n) {
  int temp = n;
  int c0 = 0, c1 = 0;

  // ডান থেকে 1 গুনি
  while (temp != 0 && (temp & 1) == 1) { c0++; temp >>= 1; }
  // তারপর 0 গুনি
  while (temp != 0 && (temp & 1) == 0) { c1++; temp >>= 1; }

  // Edge: 0 বা সব 1-এর পরে 0 নেই
  if (temp == 0) return -1;

  final p = c0 + c1;   // flip করার position

  n &= ~(1 << p);                            // bit p → 0
  n &= ~((1 << p) - 1);                     // bit p-এর ডানে সব 0
  n |= ((1 << (c1 + 1)) - 1) << (c0 - 1);  // 1-bit গুলো সঠিক জায়গায়
  return n;
}

void main() {
  print(getNext(13948).toRadixString(2));   // 11011011001111 (=14004 approx)
  print(getPrev(13948).toRadixString(2));   // নির্ভুল ছোট number
}
```

```python
# Python
def get_next(n: int) -> int:
    temp, c0, c1 = n, 0, 0

    while temp and not (temp & 1):   # trailing 0 গুনি
        c0 += 1
        temp >>= 1
    while temp and (temp & 1):       # তারপর 1 গুনি
        c1 += 1
        temp >>= 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1
    return n

def get_prev(n: int) -> int:
    temp, c0, c1 = n, 0, 0

    while temp and (temp & 1):       # trailing 1 গুনি
        c0 += 1
        temp >>= 1
    while temp and not (temp & 1):   # তারপর 0 গুনি
        c1 += 1
        temp >>= 1

    if temp == 0:
        return -1

    p = c0 + c1
    n &= ~(1 << p)
    n &= ~((1 << p) - 1)
    n |= ((1 << (c1 + 1)) - 1) << (c0 - 1)
    return n

print(bin(get_next(13948)))
print(bin(get_prev(13948)))
```

## Complexity
**Time: O(b)** → effective **O(1)** (b ≤ 32) · **Space: O(1)**।

## Pattern চিনুন
> **"Same number of 1s, পরের/আগের number" → ডান থেকে বামে 0/1 run গুনো, সঠিক position-এ flip করো, বাকি bit পুনর্বিন্যাস করো।**

## Common mistake
- `c0` এবং `c1` গণনার ক্রম গুলিয়ে ফেলা (getNext-এ আগে 0, getPrev-এ আগে 1)।
- Edge case: n-এর সব bit 0 বা সব bit 1।

## Follow-up
- **Brute force-ও আলোচনা করুন** (উপর-নিচ যাওয়া), তারপর bit trick explain করুন — interview-তে ধাপে ধাপে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q5-5"></a>
# 5.5 — Debugger

> Pattern: **Bit trick analysis** · Difficulty: **Easy** · খুব common (conceptual)

> **বইয়ের ভাষায়:** Explain what the following code does: `((n & (n-1)) == 0)`.

## সমস্যাটা সহজ বাংলায়

শুধু একটা expression বুঝতে হবে: `((n & (n-1)) == 0)` — এটা কী check করে?

## গভীরে বুঝুন — ধাপে ধাপে

### প্রথমে `n - 1` কী করে?

`n - 1` করলে **n-এর সবচেয়ে ডানের 1-bit টা 0 হয়ে যায়**, আর তার ডানে যত 0 ছিল সব 1 হয়ে যায়।

```
n     = 1 0 1 1 0 0 0 0   (= 176)
n - 1 = 1 0 1 0 1 1 1 1   (= 175)
              ↑
        এই 1 টা 0 হলো, ডানের 0 গুলো 1 হলো

n     = 1 0 0 0 0 0 0 0   (= 128 = 2^7)
n - 1 = 0 1 1 1 1 1 1 1   (= 127)
        ↑
        একমাত্র 1 টা গেল, সব ডানে 1 হলো
```

### তাহলে `n & (n-1)` কী করে?

`n` আর `n-1` কে AND করলে — ঠিক n-এর সবচেয়ে ডানের 1-bit টা মুছে যায়, বাকি সব অপরিবর্তিত।

```
n       = 1 0 1 1 0 0 0 0
n-1     = 1 0 1 0 1 1 1 1
──────────────────────────
n&(n-1) = 1 0 1 0 0 0 0 0   ← একটা 1-bit কমে গেল
```

### তাহলে `(n & (n-1)) == 0` মানে কী?

n-এর সবচেয়ে ডানের 1-bit মুছে ফেলার পর result 0 হওয়া মানে — n-তে **মাত্র একটাই 1-bit ছিল**।

**মাত্র একটা 1-bit থাকা মানে n হলো 2-এর ঘাত** (2^k = `1000...0` binary-তে)।

```
Power of 2 দের binary:
  1  = 0001   (2^0)
  2  = 0010   (2^1)
  4  = 0100   (2^2)
  8  = 1000   (2^3)
 16  = 0001 0000   (2^4)

সবগুলোতে ঠিক একটা 1-bit আছে।

যাচাই — n = 8:
  n     = 1 0 0 0
  n-1   = 0 1 1 1
  n&n-1 = 0 0 0 0  = 0  →  true, 8 = 2^3 

যাচাই — n = 6:
  n     = 0 1 1 0
  n-1   = 0 1 0 1
  n&n-1 = 0 1 0 0  ≠ 0  →  false, 6 ≠ 2^k 

যাচাই — n = 1:
  n     = 0 0 0 1
  n-1   = 0 0 0 0
  n&n-1 = 0 0 0 0  = 0  →  true, 1 = 2^0 
```

### সম্পূর্ণ উত্তর

> `((n & (n-1)) == 0)` expression টা check করে: **n কি 0 অথবা 2-এর ঘাত?**
>
> - n = 0 হলে → `(0 & -1) == 0` → `0 == 0` → true (edge case)
> - n > 0 এবং n = 2^k হলে → true
> - অন্য যেকোনো n > 0 হলে → false

n-এর শূন্য হওয়ার edge case বাদ দিলে: **"n কি 2-এর exact ঘাত?"**

Interview-তে সম্পূর্ণ উত্তর: "এই code টা check করে n শূন্য না হলে এটা 2-এর ঘাত কিনা, কারণ 2-এর ঘাত-এর binary-তে ঠিক একটা 1-bit থাকে, আর `n & (n-1)` সেই একটা bit মুছে দেয়।"

## Code — সম্পূর্ণ function

```dart
// Dart
bool isPowerOfTwo(int n) {
  return n > 0 && (n & (n - 1)) == 0;
}

void main() {
  print(isPowerOfTwo(1));    // true  (2^0)
  print(isPowerOfTwo(8));    // true  (2^3)
  print(isPowerOfTwo(6));    // false
  print(isPowerOfTwo(0));    // false (edge)
  print(isPowerOfTwo(-8));   // false (negative)
}
```

```python
# Python
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(1))    # True
print(is_power_of_two(8))    # True
print(is_power_of_two(6))    # False
print(is_power_of_two(0))    # False
print(is_power_of_two(-8))   # False
```

## Complexity
**Time: O(1)** · **Space: O(1)**।

## Pattern চিনুন
> **`x & (x-1)` সবচেয়ে ডানের 1-bit মুছে দেয়।** এটা একটা fundamental bit trick। ব্যবহার:
> - Power of 2 check: `n > 0 && (n & (n-1)) == 0`
> - 1-bit গোনা (Brian Kernighan's algorithm): `while(n != 0) { count++; n &= (n-1); }`
> - "1-bit আছে কিনা" — এই trick ছাড়াও `Integer.bitCount()` / `bin(n).count('1')` আছে।

## Common mistake
- `n == 0` এর ক্ষেত্রে `(0 & -1) == 0` → true হয় — কিন্তু 0 কে সাধারণত 2-এর ঘাত ধরা হয় না। তাই `n > 0` শর্ত জরুরি।
- Negative number-এও false হওয়া উচিত।

## Follow-up
- **1-bit count করো (Hamming Weight/popcount)** → while loop-এ `n &= (n-1)` করো, গুনো।
- **"n কি 4-এর ঘাত?"** → `n > 0 && (n & (n-1)) == 0 && (n & 0xAAAAAAAA) == 0` (bit position even কিনা)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q5-6"></a>
# 5.6 — Conversion

> Pattern: **XOR + popcount** · Difficulty: **Easy** · common

> **বইয়ের ভাষায়:** Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
> Example: 29 (11101), 15 (01111) → 2

## সমস্যাটা সহজ বাংলায়

দুটো integer A এবং B দেওয়া। A কে B-তে রূপান্তর করতে **কতগুলো bit flip করতে হবে** তা বলো।

## উদাহরণ (ASCII diagram)

```
A = 29 = 1 1 1 0 1
B = 15 = 0 1 1 1 1

কোন bit গুলো আলাদা?
  A: 1 1 1 0 1
  B: 0 1 1 1 1
     ↑       ↑
  bit 4 আলাদা  bit 0 আলাদা

উত্তর: 2 টা bit flip করতে হবে।
```

## মূল insight — XOR দিয়ে সহজেই

XOR করলে **শুধু আলাদা bit গুলোতে 1 আসে**। তারপর সেই 1 গুলো গুনলেই উত্তর।

```
A XOR B:
  A = 1 1 1 0 1
  B = 0 1 1 1 1
  ─────────────
XOR = 1 0 0 1 0   ← 1 আছে ঠিক যেখানে আলাদা
           ↑ ↑
     bit 1 আর bit 4 আলাদা → count = 2 
```

## ভাবনা ১: Brute Force — bit by bit compare
প্রতিটা bit-এ A এবং B মিলিয়ে দেখি।
- **Time: O(b)** · **Space: O(1)**

## ভাবনা ২: Optimal — XOR + `x & (x-1)` দিয়ে count
XOR করে c = A ^ B পাই। তারপর c-এর 1-bit গুনি। `x & (x-1)` trick দিয়ে লুপ চালাই।

```
c = A ^ B = 10010  (= 18)

step 1: c & (c-1) = 10010 & 10001 = 10000  (ডানের 1 মুছলো), count=1
step 2: c & (c-1) = 10000 & 01111 = 00000  (আবার 1 মুছলো), count=2
step 3: c = 0, stop

উত্তর: 2 
```

## Code

```dart
// Dart
int bitsToFlip(int a, int b) {
  int c = a ^ b;    // আলাদা bit গুলো 1
  int count = 0;
  while (c != 0) {
    c &= c - 1;     // সবচেয়ে ডানের 1-bit মুছো
    count++;
  }
  return count;
}

void main() {
  print(bitsToFlip(29, 15));   // 2
  print(bitsToFlip(0, 0));     // 0
  print(bitsToFlip(0, -1));    // 32 (সব bit আলাদা)
}
```

```python
# Python
def bits_to_flip(a: int, b: int) -> int:
    c = a ^ b           # আলাদা bit গুলো 1
    count = 0
    # Python-এ arbitrary precision — শুধু set bit গুনি
    while c:
        c &= c - 1      # সবচেয়ে ডানের 1-bit মুছো
        count += 1
    return count

# Python shortcut — built-in
def bits_to_flip_short(a: int, b: int) -> int:
    return bin(a ^ b).count('1')

print(bits_to_flip(29, 15))          # 2
print(bits_to_flip_short(29, 15))    # 2
```

## Complexity
**Time: O(b)** যেখানে b = set bit-এর সংখ্যা ≤ 32 → effective **O(1)** · **Space: O(1)**।

## Pattern চিনুন
> **"কতটা আলাদা / কতটা পরিবর্তন লাগবে" → XOR করো (আলাদা জায়গায় 1 আসে) → 1-bit গুনো।**
> এটা **Hamming Distance** — information theory-তে ব্যাপক ব্যবহার।

## Common mistake
- XOR না করে bit-by-bit compare করা (কাজ করে, কিন্তু XOR বেশি elegant)।
- Negative number-এ Python-এ `bin(n).count('1')` সরাসরি কাজ করে না (`bin(-5)` = `'-0b101'`), XOR এবং তারপর count ঠিক থাকে।

## Follow-up
- **Hamming Distance কী?** → দুটো string বা number-এর মধ্যে আলাদা position-এর সংখ্যা।
- **Minimum number of flips to make all bits same?** → min(count of 0s, count of 1s)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q5-7"></a>
# 5.7 — Pairwise Swap

> Pattern: **Fixed bit mask + shift** · Difficulty: **Easy–Medium** · মাঝে মাঝে আসে

> **বইয়ের ভাষায়:** Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

## সমস্যাটা সহজ বাংলায়

একটা integer-এর **জোড় (even) position bit** আর **বিজোড় (odd) position bit** একে অপরের সাথে বদলাতে হবে — জোড়ায় জোড়ায়। যত কম instruction-এ সম্ভব।

```
position:  7  6  5  4  3  2  1  0
           ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑
           odd even odd even odd even odd even

বিজোড় (1,3,5,7) আর জোড় (0,2,4,6) swap হবে।
```

## উদাহরণ (ASCII diagram)

```
n = 0b10110010  (= 178)
    bit:  7 6 5 4 3 2 1 0
    val:  1 0 1 1 0 0 1 0

swap করার পর (pair-wise):
    pair (7,6): 1,0 → 0,1
    pair (5,4): 1,1 → 1,1   (একই তাই বদলায় না)
    pair (3,2): 0,0 → 0,0   (একই)
    pair (1,0): 1,0 → 0,1

    bit:  7 6 5 4 3 2 1 0
    val:  0 1 1 1 0 0 0 1   = 0b01110001 = 113
```

## মূল insight — Mask দিয়ে আলাদা করো, তারপর shift করো

**দুটো mask দরকার:**
- `0xAAAAAAAA` = `1010 1010 1010 1010 1010 1010 1010 1010` (odd position bit গুলো)
- `0x55555555` = `0101 0101 0101 0101 0101 0101 0101 0101` (even position bit গুলো)

```
ধাপ 1: odd bit গুলো বের করো → n & 0xAAAAAAAA
ধাপ 2: এদের একঘর ডানে shift করো (>>> 1) → এরা এখন even position-এ

ধাপ 3: even bit গুলো বের করো → n & 0x55555555
ধাপ 4: এদের একঘর বামে shift করো (<< 1) → এরা এখন odd position-এ

ধাপ 5: দুটো OR করো → swap সম্পন্ন!
```

বিস্তারিত trace:

```
n = 1 0 1 1 0 0 1 0   (= 178)

odd bits (mask 0xAA... = 10101010):
  n & 10101010 = 1 0 1 0 0 0 1 0   (শুধু odd position 7,5,3,1 থাকল)
  >>> 1        = 0 1 0 1 0 0 0 1   (একঘর ডানে → এখন even position 6,4,2,0-এ)

even bits (mask 0x55... = 01010101):
  n & 01010101 = 0 0 0 1 0 0 0 0   (শুধু even position 6,4,2,0 থাকল)
  << 1         = 0 0 1 0 0 0 0 0   (একঘর বামে → এখন odd position 7,5,3,1-এ)

OR:
  0 1 0 1 0 0 0 1
| 0 0 1 0 0 0 0 0
─────────────────
  0 1 1 1 0 0 0 1   = 113 
```

## Code

```dart
// Dart
int pairwiseSwap(int n) {
  // odd bit গুলো (1,3,5,...) একঘর ডানে, even bit গুলো (0,2,4,...) একঘর বামে
  return ((n & 0xAAAAAAAA) >>> 1) | ((n & 0x55555555) << 1);
  //       ─── odd bits ───         ──── even bits ────
  //                       ডানে              বামে
}

void main() {
  print(pairwiseSwap(178).toRadixString(2).padLeft(8, '0'));  // 01110001 = 113
  print(pairwiseSwap(0xAB));   // bits swap হয়ে যাবে
}
```

```python
# Python — 32-bit এ সীমাবদ্ধ করতে masking
def pairwise_swap(n: int) -> int:
    # Python arbitrary int, তাই 32-bit mask দরকার
    odd_bits  = (n & 0xAAAAAAAA) >> 1    # odd bits এক ঘর ডানে
    even_bits = (n & 0x55555555) << 1   # even bits এক ঘর বামে
    result = (odd_bits | even_bits) & 0xFFFFFFFF   # 32-bit তে সীমাবদ্ধ
    return result

print(bin(pairwise_swap(178)))     # 0b1110001 = 113
print(bin(pairwise_swap(0xAB)))
```

## Complexity
**Time: O(1)** (fixed bit operations) · **Space: O(1)**।

## Pattern চিনুন
> **"Alternate bit manipulation / জোড়ায় কাজ" → even/odd bit mask (`0xAAAAAAAA` / `0x55555555`) দিয়ে আলাদা করো, shift করো, OR দিয়ে জোড়া লাগাও।**

## Common mistake
- Dart-এ `>>` arithmetic shift ব্যবহার — negative number-এ sign bit replicate হয়, ভুল ফলাফল আসে। `>>>` (logical shift) ব্যবহার করুন।
- Python-এ 32-bit bound না দিলে অদ্ভুত বড় result আসতে পারে।
- mask গুলো ভুল হওয়া: `0xAAAAAAAA` = odd positions (bit 1,3,5...), `0x55555555` = even positions (bit 0,2,4...)।

## Follow-up
- **4-bit group-এ rotate করো** (প্রতি nibble-এ pair swap) → mask পরিবর্তন করুন।
- **General k-bit group swap?** → loop বা recursive doubling।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q5-8"></a>
# 5.8 — Draw Line

> Pattern: **Byte-level bit manipulation + boundary handling** · Difficulty: **Hard** · কম common

> **বইয়ের ভাষায়:** A monochrome screen is stored as a single array of bytes, allowing eight pixels per byte. The screen has width `w`, where `w` is divisible by 8 (that is, no byte will be split across rows). Draw a horizontal line from (r, x1) to (r, x2).
> The method signature should be:
> `drawLine(byte[] screen, int width, int x1, int x2, int r)`

## সমস্যাটা সহজ বাংলায়

একটা মনোক্রোম (কালো-সাদা) screen আছে — প্রতিটা **byte-এ ৮টা pixel** থাকে। Screen-টা একটা byte array হিসেবে আছে। `r` নম্বর row-তে `x1` pixel থেকে `x2` pixel পর্যন্ত একটা **horizontal line (সব pixel কালো = 1)** আঁকতে হবে।

## উদাহরণ (ASCII diagram)

```
ধরি width = 32 pixel = 4 byte per row
r = 1, x1 = 5, x2 = 23

byte index: 0        1        2        3        ← row 0
            4        5        6        7        ← row 1 (r=1)
            8        9        10       11       ← row 2

row 1-এর byte positions:
pixel:      0-7      8-15     16-23    24-31
byte index:  4        5        6        7

x1=5 → byte 5, byte-এর ভেতরে bit 5 (0-indexed from left)
x2=23→ byte 6, byte-এর ভেতরে bit 7 (শেষ bit)

byte 4 (pixel 0-7):   আংশিক, শুধু bit 5,6,7 কালো
  0 0 0 0 0 1 1 1   = 0x07

byte 5 (pixel 8-15):  পুরোটাই কালো
  1 1 1 1 1 1 1 1   = 0xFF

byte 6 (pixel 16-23): পুরোটাই কালো
  1 1 1 1 1 1 1 1   = 0xFF

লক্ষ্য করুন: "left bit" মানে high bit।
pixel x → byte x/8, সেই byte-এর ভেতরে bit (7 - x%8)।
```

## ধাপ ১: Listen
- `width` সবসময় 8-এর গুণিতক।
- Pixel 0 হলো সবচেয়ে বাম।
- x1 ≤ x2 ধরা।
- `r` valid row।

## ভাবনা: তিন অংশ ভাগ করো

```
x1=5, x2=23, width=32 (row 1):

  byte 4      byte 5      byte 6      byte 7
[0 0 0 0 0 1 1 1][1 1 1 1 1 1 1 1][1 1 1 1 1 1 1 1][0 0 0 0 0 0 0 0]
 ↑                ↑                ↑                ↑
start byte       full bytes         end byte        untouched
(আংশিক)         (পুরো 0xFF)       (আংশিক)

১. Start byte: x1-এর ডানে সব bit 1
   mask = 0xFF >> (x1 % 8)   (বাম থেকে x1%8 টা 0, বাকি 1)

২. End byte: x2-এর বাঁয়ে সব bit 1
   mask = ~(0xFF >> (x2 % 8 + 1)) & 0xFF
   অথবা: (0xFF << (7 - x2 % 8)) & 0xFF

৩. মাঝের full byte গুলো: সবই 0xFF

Start আর End একই byte-এ থাকলে: দুটো mask AND করো।
```

## বিস্তারিত mask বোঝা

```
x1 = 5  →  byte-এর ভেতরে bit position 5 (left = bit 7, right = bit 0)
           pixel 5 মানে byte-এর বাম থেকে 5 নম্বর bit
           bit position (0=rightmost) = 7 - 5 = 2

start mask: 0xFF >> (x1 % 8)
  x1 % 8 = 5
  0xFF = 1111 1111
  >> 5  = 0000 0111   ← বাম থেকে 5 টা 0, ডানে 3 টা 1

end mask: ~(0xFF >> (x2 % 8 + 1)) & 0xFF
  x2 = 23, x2 % 8 = 7
  0xFF >> 8 = 0x00
  ~0x00 = 0xFF
  & 0xFF = 1111 1111  ← পুরো byte কালো (x2 শেষ bit)

আরেক উদাহরণ: x2 = 21, x2 % 8 = 5
  0xFF >> 6 = 0000 0011
  ~ = 1111 1100  ← বাম 6 bit কালো, ডান 2 bit সাদা
```

## Code

```dart
// Dart
void drawLine(List<int> screen, int width, int x1, int x2, int r) {
  final bytesPerRow = width ~/ 8;
  final startByte = r * bytesPerRow + x1 ~/ 8;
  final endByte   = r * bytesPerRow + x2 ~/ 8;

  // পুরো মাঝের byte গুলো 0xFF
  for (int i = startByte + 1; i < endByte; i++) {
    screen[i] = 0xFF;
  }

  // Start byte mask: x1-এর ডানে সব 1
  final startMask = (0xFF >> (x1 % 8)) & 0xFF;
  // End byte mask: x2-এর বাঁয়ে সব 1
  final endMask = (~(0xFF >> (x2 % 8 + 1))) & 0xFF;

  if (startByte == endByte) {
    // একই byte-এ শুরু ও শেষ
    screen[startByte] |= (startMask & endMask) & 0xFF;
  } else {
    screen[startByte] |= startMask;
    screen[endByte]   |= endMask;
  }
}

void main() {
  // width=32, 2 row → 8 bytes
  final screen = List<int>.filled(8, 0);
  drawLine(screen, 32, 5, 23, 1);   // row 1, pixel 5 to 23
  print(screen.map((b) => b.toRadixString(2).padLeft(8, '0')).toList());
  // [00000000, 00000000, 00000000, 00000000, 00000111, 11111111, 11111111, 00000000]
}
```

```python
# Python
def draw_line(screen: list, width: int, x1: int, x2: int, r: int) -> None:
    bytes_per_row = width // 8
    start_byte = r * bytes_per_row + x1 // 8
    end_byte   = r * bytes_per_row + x2 // 8

    # মাঝের পুরো byte গুলো
    for i in range(start_byte + 1, end_byte):
        screen[i] = 0xFF

    # Start mask: x1-এর ডানে সব 1
    start_mask = (0xFF >> (x1 % 8)) & 0xFF
    # End mask: x2-এর বাঁয়ে সব 1
    end_mask = (~(0xFF >> (x2 % 8 + 1))) & 0xFF

    if start_byte == end_byte:
        screen[start_byte] |= (start_mask & end_mask) & 0xFF
    else:
        screen[start_byte] |= start_mask
        screen[end_byte]   |= end_mask

# যাচাই
screen = [0] * 8   # width=32, 2 rows
draw_line(screen, 32, 5, 23, 1)
for b in screen:
    print(format(b, '08b'), end=' ')
# 00000000 00000000 00000000 00000000 00000111 11111111 11111111 00000000
```

## Complexity
**Time: O(w/8)** (row-এর byte সংখ্যা, worst case সব byte fill) · **Space: O(1)** (in-place)।

## Pattern চিনুন
> **"Pixel/bit level manipulation" → byte boundary সাবধানে handle করো: start partial byte, full middle bytes, end partial byte — তিনটা আলাদা।** এই "boundary + middle" pattern অনেক low-level problem-এ লাগে।

## Common mistake
- start আর end একই byte-এ থাকলে আলাদাভাবে handle না করা (দুটো mask AND করতে হবে, আলাদা আলাদা OR করলে ভুল হবে)।
- Dart-এ `~` দিলে negative হয় — `& 0xFF` দিয়ে 8-bit-এ সীমাবদ্ধ করতে ভুল করা।
- x2 % 8 == 7 হলে end mask = 0xFF — এটা edge case হিসেবে আলাদা না ধরলে formula ভুল আসতে পারে।

## Follow-up
- **Vertical line?** → প্রতি row-তে ঠিক একটা bit set করুন।
- **Color screen (multiple bits per pixel)?** → byte-per-pixel গুণ করে adjust করুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

## Chapter সারসংক্ষেপ

| # | প্রশ্ন | মূল technique | Time | Space |
|---|---|---|---|---|
| 5.1 | Insertion | Clear mask + shift + OR | O(1) | O(1) |
| 5.2 | Binary to String | Repeated × 2, integer part নেওয়া | O(1) | O(1) |
| 5.3 | Flip Bit to Win | Sliding window (prev/cur run) | O(1) | O(1) |
| 5.4 | Next Number | c0/c1 গুনে flip + rearrange | O(1) | O(1) |
| 5.5 | Debugger | `n & (n-1)` — ডানের 1 মুছে | O(1) | O(1) |
| 5.6 | Conversion | XOR + popcount | O(1) | O(1) |
| 5.7 | Pairwise Swap | Even/odd mask + shift | O(1) | O(1) |
| 5.8 | Draw Line | Byte boundary partial+full mask | O(w/8) | O(1) |

### Essential Bit Tricks — Cheat Sheet

```
Get bit i:     (n >> i) & 1
Set bit i:     n | (1 << i)
Clear bit i:   n & ~(1 << i)
Update bit i:  (n & ~(1 << i)) | (v << i)

x & (x-1)     → সবচেয়ে ডানের 1-bit মুছে দেয়
x & (-x)       → শুধু সবচেয়ে ডানের 1-bit রাখে
~x = -(x+1)   → NOT, two's complement
n > 0 && (n & (n-1)) == 0  → n কি 2-এর ঘাত?

XOR tricks:
  a ^ a = 0         (নিজের সাথে = 0)
  a ^ 0 = a         (0 এর সাথে = নিজেই)
  a ^ b ^ a = b     (দুবার XOR = বাদ)
  A^B → আলাদা bit-এ 1  (Hamming distance)

Masks:
  0xAAAAAAAA = 1010...10  (odd positions)
  0x55555555 = 0101...01  (even positions)
  0xFF = একটা byte সব 1
  (1 << k) - 1 = নিচের k-bit সব 1
  ~0 = সব bit 1 (= -1, signed)

Shift rules:
  n << k  = n × 2^k
  n >> k  = n ÷ 2^k  (arithmetic, sign রাখে)
  n >>> k = n ÷ 2^k  (logical, sign রাখে না — Dart)
```

### "এটা দেখলে → এটা ভাবো"

```
নির্দিষ্ট bit range বসানো          →  clear mask + shift + OR
decimal fraction → binary           →  বারবার ×2, integer part নাও
একটা bit flip, লম্বা 1-run         →  prev/cur run track (sliding window)
same 1-bit count, পরের/আগের number →  c0/c1 গুনে flip, rearrange
n & (n-1) == 0                      →  n = 0 বা 2-এর ঘাত
দুটো number কতটা আলাদা             →  XOR → popcount
জোড়/বিজোড় bit swap               →  even/odd mask (0x55.../0xAA...) + shift
pixel/bit range screen-এ           →  byte boundary: partial + full + partial
```

### এই chapter-এর ৫টা সোনার নিয়ম

1. **`n & (n-1)`** সবচেয়ে ডানের 1-bit মুছে — power-of-2 check ও popcount-এ ব্যাপক কাজে লাগে।
2. **XOR** আলাদা bit-এ 1 দেয় — bit difference, toggle, duplicate খোঁজা সব কাজে লাগে।
3. **Mask = left | right** — নির্দিষ্ট range clear করতে দুটো mask OR করুন।
4. **Dart-এ `>>` arithmetic** (sign replicate করে) — logical shift-এ **`>>>`** ব্যবহার করুন।
5. **Byte boundary problem-এ** সবসময় তিনটা ভাগ: partial start + full middle + partial end।

> **পরের ধাপ:** [Chapter 6 — Math & Logic Puzzles](chapter06_math_logic_puzzles.md), যেখানে prime sieve, probability, আর logic puzzle pattern শিখব।

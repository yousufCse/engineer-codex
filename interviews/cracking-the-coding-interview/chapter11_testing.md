# Chapter 11 — Testing (প্রশ্ন 11.1 – 11.6)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। এটা একটা **conceptual chapter** — কোড কম, যুক্তি ও approach বেশি।
> এই chapter-এ শিখব: কীভাবে যেকোনো জিনিস (software হোক বা একটা পেন) **পদ্ধতিগতভাবে test** করতে হয়।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: Sorting & Searching](chapter10_sorting_searching.md) · [পরের: C & C++](chapter12_c_cpp.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
A. আগে Background (অবশ্যই পড়ুন):
   - কেন test করি, কী কী ধরনের test (unit / integration / system)
   - manual vs automated
   - real-world জিনিস test করার 5-step framework
   - test case-এর তিন ভাগ: normal / edge / stress
B. তারপর ৬টা প্রশ্ন:
   11.1  Mistake        — কোডে কী ভুল আছে খুঁজে বের করা
   11.2  Random Crashes — অনিয়মিতভাবে crash করা app debug করা
   11.3  Chess Test     — একটা method (isValidMove) test করা
   11.4  No Test Tools  — কোনো tool ছাড়া webpage test করা
   11.5  Test a Pen     — একটা physical পেন test করা
   11.6  Test an ATM    — একটা ATM system test করা
```

**প্রশ্নসমূহ:** [11.1 — Mistake](#q11-1) · [11.2 — Random Crashes](#q11-2) · [11.3 — Chess Test](#q11-3) · [11.4 — No Test Tools](#q11-4) · [11.5 — Test a Pen](#q11-5) · [11.6 — Test an ATM](#q11-6)

এই chapter-এর প্রশ্নগুলো algorithm প্রশ্নের মতো নয় — এখানে **একটাই "সঠিক উত্তর" নেই**। interviewer দেখতে চায় আপনি **গুছিয়ে, পদ্ধতিগতভাবে চিন্তা করতে পারেন কিনা** — সব case ধরতে পারেন কিনা, প্রশ্ন করতে পারেন কিনা।

---
---

# Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

## ১. কেন test করি? (intuition আগে)

ভাবুন আপনি একটা সেতু বানালেন। গাড়ি ছাড়ার আগে নিশ্চিত হবেন না — সেতু ভার নিতে পারবে কিনা? Software-ও তেমন। Test হলো **"জিনিসটা ঠিকঠাক কাজ করে কিনা" তা প্রমাণ করার পদ্ধতি** — শুধু "সাধারণ অবস্থায়" নয়, **খারাপ/অপ্রত্যাশিত অবস্থায়ও**।

> মূল কথা: একজন ভালো tester ভাবে — **"এটা কীভাবে ভাঙতে পারে?"** শুধু "এটা কীভাবে কাজ করে?" নয়।

Test দুটো ভিন্ন উদ্দেশ্যে হতে পারে — interview-তে কোনটা জিজ্ঞেস করা হচ্ছে সেটা প্রথমেই বুঝে নিন:

| উদ্দেশ্য | মানে | উদাহরণ প্রশ্ন |
|---|---|---|
| **Software test** | একটা প্রোগ্রাম/feature ঠিক কাজ করে কিনা যাচাই | 11.3, 11.4 |
| **Real-world object test** | একটা বাস্তব জিনিস/system যাচাই | 11.5 (পেন), 11.6 (ATM) |
| **Debug / fault-find** | ভুল বা crash-এর কারণ খুঁজে বের করা | 11.1, 11.2 |

## ২. Test-এর ধরন (type অনুযায়ী)

```
            ┌──────────────────────────────────────────┐
   System   │  পুরো app একসাথে — user যেভাবে ব্যবহার করে │   (সবচেয়ে বড় scope)
            ├──────────────────────────────────────────┤
Integration │  দুই/বেশি module একসাথে ঠিকঠাক কথা বলে কিনা│
            ├──────────────────────────────────────────┤
   Unit     │  একটা ছোট function/class আলাদা করে যাচাই  │   (সবচেয়ে ছোট scope)
            └──────────────────────────────────────────┘
```

- **Unit test** — সবচেয়ে ছোট অংশ (একটা function) আলাদা করে test করা। দ্রুত, নির্ভুল, ভুল কোথায় তা চট করে বলে দেয়। (11.3-এ এটাই করব)
- **Integration test** — কয়েকটা অংশ একসাথে ঠিকঠাক কাজ করে কিনা (যেমন: ATM + bank server)।
- **System test** — পুরো app, শুরু থেকে শেষ (end-to-end), যেমন user করবে।

আরেকটা ভাগ — **কে চালায়**:

| | Manual test | Automated test |
|---|---|---|
| কে চালায় | মানুষ, হাতে | কোড নিজে নিজে |
| ভালো দিক | নতুন/দেখতে কেমন (UI/UX) ধরা পড়ে | দ্রুত, বারবার, ভুল করে না |
| খারাপ দিক | ধীর, ক্লান্তিকর, ভুল হয় | প্রথমে লিখতে সময় লাগে |
| কখন | exploratory, UI feel | regression (বারবার চালাতে হবে এমন) |

> **Regression test** = নতুন কোড যোগ করার পর পুরোনো feature ভাঙেনি তা নিশ্চিত করা। automated test এখানে সোনার মতো।

## ৩. Real-world জিনিস test করার 5-step framework (সবচেয়ে দামি অংশ)

11.5 (পেন) আর 11.6 (ATM)-এর মতো "এই জিনিসটা test করো" প্রশ্নে **এই ৫ ধাপ মুখস্থ রাখুন** — এটাই interview-তে আপনাকে গোছানো দেখাবে:

```
ধাপ 1: কে ব্যবহার করবে? (Who)
        → user-রা কারা? শিশু? বয়স্ক? দৃষ্টিহীন? — তাদের চাহিদা আলাদা।

ধাপ 2: কীভাবে ব্যবহার করবে? (Use cases — What)
        → স্বাভাবিক ব্যবহারগুলো তালিকা করুন (পেন: লেখা; ATM: টাকা তোলা, balance দেখা)।

ধাপ 3: কোন কোন সীমা/চাপ? (Edge cases + Stress)
        → চরম অবস্থা: খালি, খুব বড়, খুব বেশিবার, ভুল input, একসাথে অনেকে।

ধাপ 4: কী কী test করব? (What to test)
        → কাজ ঠিকঠাক হয় কিনা (functional) + কত দ্রুত/নিরাপদ (non-functional)।

ধাপ 5: কীভাবে চালাব? (How to perform)
        → manual না automated? কোন pass/fail criteria? কোন tools?
```

## ৪. Test case-এর তিন ভাগ (এই chapter জুড়ে বারবার লাগবে)

প্রতিটা test প্রশ্নে test case গুলো তিন ভাগে ভাবুন:

| ভাগ | মানে | পেন উদাহরণ |
|---|---|---|
| **Normal** | স্বাভাবিক, প্রত্যাশিত ব্যবহার | কাগজে লেখা |
| **Edge** | সীমানার ব্যতিক্রম, কম-ঘটা case | উল্টো করে লেখা, ভেজা কাগজে |
| **Stress** | চাপ/extreme — অনেক, বড়, দ্রুত | একটানা ১০ ঘণ্টা লেখা |

> এই তিনটা মাথায় রাখলে আপনি প্রায় কখনো গুরুত্বপূর্ণ case মিস করবেন না।

---
---

<a id="q11-1"></a>
# 11.1 — Mistake

> Pattern: **Code review / Find the bug** · Difficulty: **Easy** · warm-up, খুব common

> **বইয়ের ভাষায়:** Find the mistake(s) in the following code:
> ```c
> unsigned int i;
> for (i = 100; i >= 0; --i)
> printf("%d\n", i);
> ```

## সমস্যাটা সহজ বাংলায়
উপরের C কোডটায় **কী কী ভুল আছে** খুঁজে বের করতে হবে। দেখতে নিরীহ — `100` থেকে `0` পর্যন্ত গুনে নামার একটা loop। কিন্তু এর মধ্যে **দুটো** সমস্যা লুকিয়ে আছে।

## কীভাবে approach করব (এই ধরনের প্রশ্নের সাধারণ পদ্ধতি)
"কোডে ভুল খোঁজো" প্রশ্নে শুধু চোখ বুলিয়ে যাবেন না। **একটা checklist মেনে** পড়ুন:

```
1. Type ঠিক আছে? (signed/unsigned, int/float, overflow হয় কিনা)
2. Loop-এর সীমা ঠিক? (off-by-one, কখনো শেষ হয় কিনা — infinite loop?)
3. Boundary value-তে কী হয়? (0, সর্বোচ্চ, সর্বনিম্ন)
4. Format/print/return ঠিক?
5. Null / খালি / negative input-এ কী হয়?
```

## কী কী test case
এই প্রশ্নে নিজে কোড চালালেই ধরা পড়ে — তবু চিন্তায় boundary গুলো দেখুন:

```
+-----------------+-----------------------------------------------+
| input/অবস্থা    | আশা vs বাস্তব                                  |
+-----------------+-----------------------------------------------+
| i = 100..1      | ঠিকঠাক print হয়                               |
| i = 0           | print হওয়ার পর --i করলে কী হয়? ← এখানেই বাগ    |
| unsigned i < 0  | অসম্ভব! unsigned কখনো negative হয় না          |
+-----------------+-----------------------------------------------+
```

## ধাপে ধাপে (এই নির্দিষ্ট সমস্যার সমাধান)

**ভুল ১ — Infinite loop (`unsigned` দিয়ে `>= 0`):**
`i` একটা `unsigned int` — মানে এটা **কখনো negative হতে পারে না**। তাই শর্ত `i >= 0` **সবসময় সত্য**। যখন `i = 0` হয়ে `--i` হবে, তখন এটা negative না হয়ে **wrap around** করে সবচেয়ে বড় সংখ্যা (যেমন 4294967295) হয়ে যাবে। loop **কখনো থামবে না** → infinite loop।

```
... 2  1  0   --i করলে →  4294967295  (negative না হয়ে ঘুরে এলো!)
                          ↑ loop থামল না
```

**সমাধান:** শর্তটা `i > 0` করুন (তাহলে 0-তে থামবে), অথবা `i` কে **signed int** করুন।

**ভুল ২ — `printf` format specifier:**
`i` হলো `unsigned int`, কিন্তু `%d` দিয়ে **signed** হিসেবে print করা হচ্ছে। সঠিক হলো `%u` (unsigned-এর জন্য)। ছোট ভুল, কিন্তু interviewer এটা ধরলে খুশি হয়।

**ঠিক করা কোড:**
```c
unsigned int i;
for (i = 100; i > 0; --i)   // i > 0  →  0-তে থামবে
    printf("%u\n", i);      // %u  →  unsigned-এর জন্য
```
> খেয়াল করুন: এখন `0` print হবে না। যদি `0`-ও দরকার হয়, তাহলে signed int + `i >= 0` ব্যবহার করুন।

## Common mistake
- শুধু একটা ভুল (infinite loop) ধরে থেমে যাওয়া — `%d` vs `%u`-টাও বলুন।
- "off-by-one" বলে ফেলা, অসল সমস্যা type (unsigned)-এ।
- ভুলটা **কেন** হয় ব্যাখ্যা না করা (wrap-around-এর ধারণাটা বলুন)।

## Follow-up
- **"Signed int হলে কী হতো?"** → তখন `i >= 0` ঠিকঠাক 0-তে থামত, কিন্তু `0` print হওয়ার পর `--i` করে `-1` হতো এবং loop শেষ হতো। তবে `%d`-ও তখন সঠিক।
- **"এই বাগ কীভাবে আগে ধরা পড়ত?"** → unit test/compiler warning (`-Wall`), অথবা একটা সহজ run।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q11-2"></a>
# 11.2 — Random Crashes

> Pattern: **Debugging / fault isolation** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** You are given the source to an application which crashes when it is run. After running it ten times in a debugger, you find it never crashes in the same place. The application is single threaded, and uses only the C standard library. What programming errors could be causing this crash? How would you test each one?

## সমস্যাটা সহজ বাংলায়
একটা app আছে যেটা **মাঝে মাঝে crash করে**, কিন্তু **প্রতিবার আলাদা জায়গায়** — কোনো নির্দিষ্ট ধাপে নয়। app **single-threaded** (তাই thread/race condition নয়) এবং শুধু **C standard library** ব্যবহার করে। প্রশ্ন: **কী কী কারণ** এমন অনিয়মিত crash ঘটাতে পারে, আর প্রতিটা কীভাবে test করব?

## কীভাবে debug করব (এই ধরনের প্রশ্নের সাধারণ পদ্ধতি)
"এলোমেলো crash" = এমন কিছু যা **প্রতিবার একই থাকে না**। তাই আগে ভাবুন — **কী কী জিনিস run-to-run বদলায়?**

```
run-to-run কী বদলায়?
  → memory-র অবস্থা (uninitialized মান, heap layout)
  → বাইরের জিনিস (user input, file, network, OS-এর দেওয়া resource)
  → সময়/ঘড়ি, random সংখ্যা
  → কত memory ফাঁকা আছে
এগুলোই সন্দেহের তালিকা।
```

## কী কী কারণ হতে পারে (এবং প্রতিটা কীভাবে test করব)

```
+----------------------------------+--------------------------------------------+
| সম্ভাব্য কারণ                     | কীভাবে test/ধরব                            |
+----------------------------------+--------------------------------------------+
| 1. বাইরের নির্ভরতা              | crash-এর আগে কী input/file/network ছিল     |
|    (file/network/random সময়)    | log করুন; একই input দিয়ে বারবার চালান      |
+----------------------------------+--------------------------------------------+
| 2. Uninitialized variable        | uninitialized মান প্রতিবার আলাদা; debugger |
|    (garbage মান প্রতিবার ভিন্ন)  | warning, Valgrind/MemorySanitizer চালান    |
+----------------------------------+--------------------------------------------+
| 3. Memory leak / heap শেষ        | অনেকক্ষণ চালালে memory ভরে crash; memory   |
|                                  | usage monitor করুন, leak detector চালান    |
+----------------------------------+--------------------------------------------+
| 4. Dangling pointer / use-after- | freed memory ব্যবহার; Valgrind/AddressSan. |
|    free / buffer overflow        | দিয়ে চালান — সঠিক লাইন দেখাবে              |
+----------------------------------+--------------------------------------------+
| 5. অন্য process/OS-এর প্রভাব     | অন্য program বন্ধ করে চালান; resource     |
|    (shared resource, low memory) | (memory/disk) ভরা অবস্থায় test করুন        |
+----------------------------------+--------------------------------------------+
```

## ধাপে ধাপে (গুছিয়ে কীভাবে এগোব)
1. **তথ্য জোগাড়:** crash-এর আগের অবস্থা log করুন (কী input, কত memory, কোন file)। দুই category-তে ভাগ করুন: (ক) component নিজে, (খ) বাইরের জিনিস/পরিবেশ।
2. **পরিবেশ আলাদা করুন:** একই input/file দিয়ে বারবার চালিয়ে দেখুন crash হয় কিনা — হলে input নির্ভর; না হলে memory/random কারণ।
3. **Tool লাগান:** memory-জনিত bug-এর জন্য **Valgrind / AddressSanitizer / MemorySanitizer** — এরা ঠিক লাইন বলে দেয় কোথায় invalid memory ছোঁয়া হয়েছে।
4. **চাপ দিন:** অনেকক্ষণ/অনেকবার চালান (leak ধরতে), কম memory-তে চালান (allocation failure ধরতে)।
5. **সংকুচিত করুন:** কোডের অংশ একে একে বন্ধ/বিচ্ছিন্ন করে খুঁজুন কোন অংশ থাকলে crash হয়।

> মূল intuition: **crash যদি র্যান্ডম জায়গায় হয়, তাহলে কারণটাও সম্ভবত র্যান্ডম কিছুর সাথে জড়িত** — uninitialized memory, allocation, বা বাইরের input।

## Common mistake
- শুধু একটা কারণ (যেমন memory leak) বলে থেমে যাওয়া — কয়েকটা সম্ভাবনা দিন।
- "কারণ" বলে test করার উপায় না বলা — প্রশ্ন দুটোই চায়: কারণ **আর** কীভাবে যাচাই।
- single-threaded বলা সত্ত্বেও race condition-এর কথা বলা (ওটা বাদ — প্রশ্নে clarify করা আছে)।

## Follow-up
- **"কোন tool সবচেয়ে কাজের?"** → memory bug-এ Valgrind/AddressSanitizer; uninitialized-এ MemorySanitizer; leak-এ leak detector।
- **"একই জায়গায় crash করলে?"** → তখন deterministic bug, debugger-এ stack trace দেখেই দ্রুত ধরা যায়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q11-3"></a>
# 11.3 — Chess Test

> Pattern: **Unit testing একটা method** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** We have the following method used in a chess game: `boolean canMoveTo(int x, int y)`. This method is part of the `Piece` class and returns whether or not the piece can move to position `(x, y)`. Explain how you would test this method.

## সমস্যাটা সহজ বাংলায়
দাবার একটা `Piece` (গুটি) class-এ একটা method আছে: `canMoveTo(int x, int y)` — এটা বলে গুটিটা `(x, y)` ঘরে যেতে পারবে কিনা। এই **একটা method** কীভাবে test করব তা ব্যাখ্যা করতে হবে। এটা একটা software unit test প্রশ্ন।

## কীভাবে approach করব (এই ধরনের প্রশ্নের সাধারণ পদ্ধতি)
একটা নির্দিষ্ট method test করতে দুই ধরনের জিনিস ভাবুন:

```
A. Extreme / invalid input  →  function যেন crash না করে, ঠিকভাবে handle করে
   (board-এর বাইরের ঘর, negative, একই ঘর, খুব বড় সংখ্যা)

B. General / স্বাভাবিক case   →  function যেন সঠিক উত্তর দেয়
   (প্রতিটা গুটির নিয়ম: ঘোড়া L-আকারে, বোড়ে সোজা, ইত্যাদি)
```

## কী কী test case (normal / edge / stress)

```
+----------+-------------------------------------------------------------+
| ভাগ      | test case                                                    |
+----------+-------------------------------------------------------------+
| Normal   | প্রতিটা গুটির বৈধ move:                                       |
|          |  - ঘোড়া (Knight): L-আকারে যাওয়া valid                        |
|          |  - বোড়ে (Pawn): সোজা ১ ঘর / শুরুতে ২ ঘর, কোনাকুনি খেলে      |
|          |  - রাজা/রানি/নৌকা/হাতি: নিজ নিজ নিয়ম                          |
+----------+-------------------------------------------------------------+
| Edge     | - (x, y) board-এর বাইরে (x<0, x>7, y<0, y>7)                  |
|          | - একই ঘরে যাওয়া (current position = target)                  |
|          | - গন্তব্যে নিজের গুটি আছে (যাওয়া যাবে না)                     |
|          | - মাঝপথে অন্য গুটি (blocked path)                             |
+----------+-------------------------------------------------------------+
| Stress   | - সব valid এবং invalid move একসাথে (প্রতিটা গুটি × প্রতিটা ঘর)|
|          | - বহুবার call করে দ্রুততা/স্থিতিশীলতা যাচাই                  |
+----------+-------------------------------------------------------------+
```

## ধাপে ধাপে (এই নির্দিষ্ট সমস্যার সমাধান)
1. **আগে clarify করুন:** এটা কি শুধু গুটির move pattern চেক করে, নাকি পুরো game-এর বৈধতা (check/checkmate, path blocked)? — scope বুঝে নিন।
2. **প্রতিটা গুটির জন্য আলাদা valid/invalid move set বানান।** প্রতিটার জন্য কয়েকটা সঠিক move (true আশা করি) আর কয়েকটা ভুল move (false আশা করি)।
3. **Edge case যোগ করুন** (board-এর বাইরে, একই ঘর, blocked)।
4. **Automated unit test লিখুন** — প্রতিটা case-এ আশা vs বাস্তব মিলিয়ে দেখুন (assert)। নিচে একটা ছোট pseudo-code:

```python
# pseudo unit test (অল্প কোড — মূলত structure বোঝার জন্য)
def test_knight_moves():
    knight = Piece("knight", x=4, y=4)
    assert knight.canMoveTo(6, 5) == True    # valid L-move
    assert knight.canMoveTo(5, 5) == False   # invalid (L নয়)
    assert knight.canMoveTo(-1, 0) == False  # board-এর বাইরে
    assert knight.canMoveTo(4, 4) == False   # একই ঘর
```
5. **Regression-এর জন্য automated রাখুন** — নিয়ম বদলালে test আবার চালিয়ে নিশ্চিত হবেন পুরোনো কিছু ভাঙেনি।

> মূল intuition: একটা method test = **(সব invalid input ধরে কিনা) + (সব valid input-এ সঠিক উত্তর দেয় কিনা)**।

## Common mistake
- শুধু valid move test করা, invalid/edge (board-এর বাইরে, একই ঘর) ভুলে যাওয়া।
- scope clarify না করা (শুধু গুটির নিয়ম, নাকি পুরো game state)।
- manual test বলা — এটা পুরোপুরি automated unit test-এর উপযুক্ত।

## Follow-up
- **"পুরো game test করতে বললে?"** → integration/system test দরকার: চাল-পাল্টা সিকোয়েন্স, check/checkmate, illegal move প্রত্যাখ্যান।
- **"path blocked check কোথায়?"** → যদি `canMoveTo` শুধু geometry দেখে, তাহলে blocked-path আলাদা method/test-এ যায়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q11-4"></a>
# 11.4 — No Test Tools

> Pattern: **Manual web testing, কোনো tool ছাড়া** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** How would you load test a webpage without using any test tools?

## সমস্যাটা সহজ বাংলায়
একটা webpage-এর **load test** করতে হবে — মানে দেখতে হবে অনেক চাপ (অনেক user, অনেক request) পড়লে এটা কেমন আচরণ করে — কিন্তু **কোনো load-testing tool ব্যবহার করা যাবে না**। নিজেদের বানানো সহজ উপায়ে করতে হবে।

## কীভাবে approach করব (এই ধরনের প্রশ্নের সাধারণ পদ্ধতি)
আগে বুঝে নিন **load test কী মাপে** — তিনটা প্রধান জিনিস:

```
1. Response time   →  request পাঠালে কত সময়ে উত্তর আসে?
2. Throughput      →  প্রতি সেকেন্ডে কতগুলো request সামলাতে পারে?
3. Resource usage  →  CPU / memory / network কতটা ব্যবহার হয়?
```

আর জানতে হবে — **কোন অবস্থায় performance খারাপ হতে শুরু করে** (maximum load, breaking point)।

## কী কী test case (normal / edge / stress)

```
+----------+-------------------------------------------------------------+
| ভাগ      | কী মাপব                                                      |
+----------+-------------------------------------------------------------+
| Normal   | অল্প user — response time ঠিকঠাক (baseline)                  |
| Edge     | প্রত্যাশিত সর্বোচ্চ user সংখ্যা — তখনও কাজ করে কিনা          |
| Stress   | প্রত্যাশার চেয়ে অনেক বেশি user — কখন/কোথায় ভাঙে              |
+----------+-------------------------------------------------------------+
```

## ধাপে ধাপে (এই নির্দিষ্ট সমস্যার সমাধান)
"কোনো tool নেই" — তাই **নিজেরাই tool বানাই**। মূল ধারণা: **অনেকগুলো virtual user একসাথে নকল করা**।

1. **মাপার জিনিস ঠিক করুন:** key metrics = response time, throughput, resource usage; আর pass/fail criteria (যেমন "১০০০ user-এ response < ২ সেকেন্ড")।
2. **নিজে script লিখুন:** একটা ছোট program/script বানান যেটা বারবার ওই page-এ request পাঠায় (যেকোনো programming language-এর HTTP client দিয়ে — এটা "load test tool" নয়, নিজের লেখা code)।
3. **Concurrency নকল করুন:** অনেকগুলো **thread/process** একসাথে চালান, প্রত্যেকটা একজন user-এর মতো request পাঠাবে। এভাবে শত-হাজার একসাথে user-এর চাপ নকল করা যায়।
4. **ধীরে ধীরে চাপ বাড়ান:** ১০ → ১০০ → ১০০০ user — প্রতিবার response time/throughput মাপুন। কোন সংখ্যায় ধীর হয় বা fail করে তা লক্ষ্য করুন।
5. **ফলাফল log + analyze করুন:** প্রতিটা request-এর সময় রেকর্ড করে গড়/সর্বোচ্চ বের করুন; কোন load-এ performance ভাঙে (breaking point) তা চিহ্নিত করুন।

```
নিজের লেখা load generator-এর কাঠামো:
  ┌────────────────────────────────────────┐
  │  N টা thread একসাথে চালু               │
  │   thread 1 →  বারবার GET /page  (সময় মাপো)│
  │   thread 2 →  বারবার GET /page  (সময় মাপো)│
  │   ...                                    │
  │   thread N →  ...                        │
  └────────────────────────────────────────┘
            ↓  সব thread-এর সময় জমিয়ে গড়/max বের করো
```

> মূল intuition: load test tool আসলে এটাই করে — **একসাথে অনেক fake user বানিয়ে চাপ দেয় ও সময় মাপে**। আমরা শুধু সেটা নিজের ছোট কোডে করছি।

## Common mistake
- একসাথে (concurrent) নয়, একটার পর একটা request পাঠানো — তাহলে "load" নকল হয় না।
- শুধু response time মাপা, throughput/resource ভুলে যাওয়া।
- breaking point খোঁজার চেষ্টা না করা (শুধু "কাজ করছে" বলা)।

## Follow-up
- **"একটা মেশিন থেকে যথেষ্ট load দিতে না পারলে?"** → কয়েকটা মেশিন থেকে একসাথে চালান (distributed)।
- **"কোন tool থাকলে কী ব্যবহার করতেন?"** → JMeter, Locust, k6 — এরা এই concurrent-request কাজটাই করে দেয়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q11-5"></a>
# 11.5 — Test a Pen

> Pattern: **Real-world object — 5-step framework** · Difficulty: **Medium** · খুব common (classic)

> **বইয়ের ভাষায়:** How would you test a pen?

## সমস্যাটা সহজ বাংলায়
একটা **পেন** কীভাবে test করবেন? প্রশ্নটা ইচ্ছাকৃতভাবে অস্পষ্ট (open-ended) — interviewer দেখতে চায় আপনি **প্রশ্ন করে scope ঠিক করতে পারেন কিনা** এবং তারপর গুছিয়ে সব দিক ভাবতে পারেন কিনা। এখানে Background-এর **5-step framework** সরাসরি প্রয়োগ করব।

## কীভাবে approach করব (এই ধরনের প্রশ্নের সাধারণ পদ্ধতি)
সবচেয়ে বড় ভুল হলো সাথে সাথে "কাগজে লিখে দেখব" বলা। আগে **প্রশ্ন করে scope ছোট করুন** — তারপর 5 ধাপে এগোন।

```
Listen (scope ঠিক করুন — interviewer-কে জিজ্ঞেস করুন):
  - কী ধরনের পেন? (ballpoint / fountain / শিশুদের marker?)
  - কে ব্যবহার করবে? (শিশু / অফিস / শিল্পী?)
  - কীসে লিখবে? (শুধু কাগজ / কাপড় / যেকোনো surface?)
  - মূল উদ্দেশ্য কী? (লেখা / আঁকা / খেলনা?)
```

## কী কী test case (normal / edge / stress)
ধরা যাক: এটা একটা **শিশুদের জন্য ballpoint পেন, কাগজে লেখার জন্য**।

```
+----------+-------------------------------------------------------------+
| ভাগ      | test case                                                    |
+----------+-------------------------------------------------------------+
| Normal   | - সাধারণ কাগজে স্বাভাবিকভাবে লেখা যায়                         |
|          | - কালি একসমান, পরিষ্কার দাগ পড়ে                              |
|          | - ঢাকনা ঠিকমতো লাগে/খোলে                                      |
+----------+-------------------------------------------------------------+
| Edge     | - উল্টো করে (উপরের দিকে মুখ) লিখলে?                            |
|          | - ভেজা / মসৃণ / খসখসে কাগজে?                                  |
|          | - খুব আস্তে বা খুব জোরে চাপ দিলে?                             |
|          | - কালি প্রায় শেষ হলে?                                        |
+----------+-------------------------------------------------------------+
| Stress   | - একটানা অনেকক্ষণ লেখা (কালি কতক্ষণ চলে)                      |
|          | - মাটিতে ফেলা / ভাঙার পরীক্ষা (durability)                    |
|          | - গরম/ঠান্ডায় রেখে দেওয়া (কালি গলে/জমে কিনা)                 |
+----------+-------------------------------------------------------------+
```

## ধাপে ধাপে (5-step framework প্রয়োগ)

```
ধাপ 1 — কে ব্যবহার করবে (Who):
   শিশু। তাই → নিরাপদ কিনা? (বিষাক্ত নয় তো? ধারালো নয় তো? গিলে ফেলার ঝুঁকি?)

ধাপ 2 — use case (What):
   মূল কাজ: কাগজে লেখা/আঁকা। তালিকা করুন সব স্বাভাবিক ব্যবহার।

ধাপ 3 — edge/stress (সীমা ও চাপ):
   উপরের table-এর edge ও stress case গুলো।

ধাপ 4 — কী কী test করব (functional + non-functional):
   - Functional: লেখে কিনা, কালি বের হয় কিনা, ঢাকনা কাজ করে কিনা।
   - Non-functional: কতদিন টেকে, নিরাপদ কিনা, দেখতে/ধরতে আরামদায়ক কিনা।

ধাপ 5 — কীভাবে চালাব (How):
   বেশিরভাগ manual; durability/কালি-আয়ু-র জন্য বারবার চালানো machine test।
   pass/fail criteria ঠিক করুন (যেমন "কমপক্ষে X মিটার লেখা যাবে")।
```

> মূল intuition: "পেন" বলতে interviewer একটা **সীমিত পরিসর** চায় — আপনি প্রশ্ন করে সেটা ঠিক করবেন, তারপর Who → use case → edge/stress → কী test → কীভাবে — এই ৫ ধাপে গুছিয়ে বলবেন।

## Common mistake
- scope clarify না করে সরাসরি test শুরু করা (সবচেয়ে বড় ভুল)।
- শুধু "লেখে কিনা" দেখা — durability, safety, edge surface ভুলে যাওয়া।
- শিশুদের পেন বলেও safety (বিষাক্ত/ধারালো) test বাদ দেওয়া।

## Follow-up
- **"শিশুদের জন্য না, মহাকাশচারীর জন্য হলে?"** → শূন্য মাধ্যাকর্ষণে, প্রচণ্ড গরম/ঠান্ডায় লেখে কিনা — use case ও edge পুরো বদলে যায়।
- **"একটাই পেন না, লক্ষ লক্ষ উৎপাদন হলে?"** → consistency/quality-control test যোগ হবে (প্রতিটা batch একই মানের কিনা)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q11-6"></a>
# 11.6 — Test an ATM

> Pattern: **Real-world system — 5-step framework + test type** · Difficulty: **Medium–Hard** · খুব common (classic)

> **বইয়ের ভাষায়:** How would you test an ATM in a distributed banking system?

## সমস্যাটা সহজ বাংলায়
একটা **ATM** (টাকা তোলার মেশিন) কীভাবে test করবেন — যেটা একটা বড় **distributed banking system**-এর অংশ (অনেক ATM, একটা central bank server)। এখানে শুধু একটা জিনিস নয়, একটা **system** test করছি — তাই নিরাপত্তা ও নির্ভুলতা (টাকার হিসাব) সবচেয়ে গুরুত্বপূর্ণ।

## কীভাবে approach করব (এই ধরনের প্রশ্নের সাধারণ পদ্ধতি)
আবারও আগে **clarify** করুন, তারপর test-গুলোকে **স্তরে স্তরে (unit → integration → system)** ভাগ করুন।

```
Listen (scope ঠিক করুন):
  - কোন অংশ test করছি? শুধু ATM hardware? software? বা পুরো system?
  - কী কী কাজ করতে পারে? (টাকা তোলা, জমা, balance, transfer, PIN বদল?)
  - "distributed" — মানে ATM ব্যাংকের server-এর সাথে কথা বলে; network থাকতে/না থাকতে পারে।
```

## কী কী test case (normal / edge / stress)

```
+----------+-------------------------------------------------------------+
| ভাগ      | test case                                                    |
+----------+-------------------------------------------------------------+
| Normal   | - সঠিক PIN দিয়ে login, ব্যালেন্স আছে এমন পরিমাণ তোলা         |
|          | - balance দেখা, টাকা জমা, সঠিক receipt                        |
+----------+-------------------------------------------------------------+
| Edge     | - ভুল PIN (৩ বার ভুল → card block?)                           |
|          | - balance-এর চেয়ে বেশি তোলার চেষ্টা                          |
|          | - মেশিনে cash কম/শেষ                                          |
|          | - মাঝপথে card টেনে নেওয়া / current চলে যাওয়া                  |
|          | - $0 বা negative পরিমাণ                                       |
+----------+-------------------------------------------------------------+
| Stress   | - একই account থেকে দুই ATM-এ একসাথে টাকা তোলা (concurrency)   |
|          | - হাজারো transaction একসাথে (load)                           |
|          | - server-এর সাথে connection হারিয়ে গেলে                       |
+----------+-------------------------------------------------------------+
```

## ধাপে ধাপে (এই নির্দিষ্ট সমস্যার সমাধান)
টাকার ব্যাপার — তাই সবচেয়ে বড় ঝুঁকি দুটো: **(ক) ভুল হিসাব** আর **(খ) নিরাপত্তা**। তিন স্তরে test সাজাই:

1. **Unit test (আলাদা function):** প্রতিটা ছোট অংশ আলাদা করে — PIN যাচাই, টাকার হিসাব, note গোনা। সবচেয়ে দ্রুত ও নিশ্চিত।
2. **Integration test (অংশগুলো একসাথে):** ATM ↔ bank server ঠিকমতো কথা বলে কিনা — balance ঠিক আসে, withdrawal-এর পর server-এ balance ঠিক কমে।
3. **System test (পুরো flow, user যেভাবে করে):** card ঢোকানো → PIN → টাকা তোলা → receipt → card ফেরত — পুরোটা end-to-end।
4. **বিশেষ গুরুত্ব — দুটো জিনিস আলাদা করে test করুন:**
 - **Correctness (টাকার হিসাব নিখুঁত):** কোনো অবস্থাতেই balance ভুল হওয়া যাবে না। বিশেষ করে concurrency — একই account, দুই ATM, একসাথে তোলা → double-withdrawal হওয়া যাবে না (race condition test)।
 - **Security:** ভুল PIN, card চুরি, network মাঝপথে কাটা — এসব অবস্থায় টাকা/তথ্য ফাঁস না হওয়া।
5. **Failure/recovery test:** transaction-এর মাঝপথে current/network গেলে — টাকা বেরোলো কিন্তু account থেকে কাটল না, বা উল্টোটা — এমন যেন না হয় (transaction atomic হতে হবে)।

```
Unit       →  PIN check, টাকার হিসাব  (আলাদা, দ্রুত)
Integration→  ATM ↔ bank server       (balance sync ঠিক?)
System     →  পুরো withdraw flow      (user যেভাবে করে)
      +  Correctness (race condition, double-withdraw না)
      +  Security (ভুল PIN, card চুরি)
      +  Recovery (মাঝপথে fail হলে টাকা/হিসাব ঠিক থাকে)
```

> মূল intuition: ATM = টাকা + অনেক user একসাথে + network। তাই সাধারণ functional test-এর পাশাপাশি **concurrency, security, আর failure-recovery** — এই তিনটায় বিশেষ জোর দিন। এটাই উত্তরকে junior থেকে আলাদা করে।

## Common mistake
- শুধু "টাকা তোলা যায় কিনা" (happy path) test করা — concurrency/security/recovery বাদ।
- "distributed" দিকটা উপেক্ষা করা (network কাটা, দুই ATM একসাথে — এগুলোই এই প্রশ্নের আসল কঠিন অংশ)।
- transaction atomicity না ভাবা (মাঝপথে fail হলে টাকা ও হিসাব মেলে না — ব্যাংকে ভয়াবহ)।

## Follow-up
- **"একই account-এ একসাথে দুই withdrawal এলে কীভাবে নিশ্চিত হবেন double হয়নি?"** → locking/transaction; test-এ ইচ্ছাকৃতভাবে concurrent request পাঠিয়ে balance যাচাই।
- **"server down থাকলে ATM-এর কী করা উচিত?"** → হয় transaction প্রত্যাখ্যান, নয় নিরাপদভাবে queue — কখনোই টাকা দিয়ে account update মিস করা যাবে না।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---
---

# Chapter 11 — সারসংক্ষেপ ও Cheat Sheet

| # | প্রশ্ন | ধরন | মূল approach |
|---|---|---|---|
| 11.1 | Mistake | Find the bug | unsigned `>=0` → infinite loop; `%d`→`%u` |
| 11.2 | Random Crashes | Debug | run-to-run কী বদলায় ভাবো: uninit memory, leak, dangling pointer, বাইরের input |
| 11.3 | Chess Test | Unit test (method) | extreme/invalid input + প্রতিটা গুটির valid/invalid move, automated assert |
| 11.4 | No Test Tools | Manual load test | নিজে script লিখে অনেক concurrent thread দিয়ে request পাঠাও, সময় মাপো |
| 11.5 | Test a Pen | Real-world object | 5-step: Who → use case → edge/stress → কী test → কীভাবে |
| 11.6 | Test an ATM | Real-world system | unit/integration/system + concurrency + security + recovery |

### "এই ধরনের প্রশ্ন → এই framework" (signal → approach)

```
"কোডে কী ভুল?" (find the bug)
    →  checklist: type / loop সীমা / boundary / format / null-খালি-negative

"মাঝে মাঝে crash, এলোমেলো জায়গায়" (debug)
    →  "run-to-run কী বদলায়?" ভাবো: uninit memory, leak, dangling pointer,
       বাইরের input — প্রতিটার test/tool (Valgrind, AddressSanitizer) বলো

"এই method/function কীভাবে test করবে?" (unit test)
    →  (১) সব invalid/extreme input ধরে কিনা + (২) সব valid input-এ সঠিক উত্তর কিনা
       →  automated unit test (assert)

"tool ছাড়া load/test করো" (manual)
    →  tool যা করে তা নিজে কোডে করো (concurrent threads দিয়ে চাপ + সময় মাপা)

"এই জিনিসটা test করো" (পেন/গাড়ি/টোস্টার — real-world object)
    →  5-step framework:
         1. কে ব্যবহার করবে?  2. কীভাবে (use cases)?
         3. edge ও stress?    4. কী test করব (functional + non-functional)?
         5. কীভাবে চালাব (manual/automated, pass-fail)?

"এই system test করো" (ATM/website — অনেক অংশ + user)
    →  5-step + test type স্তর (unit → integration → system)
       + concurrency + security + failure/recovery
```

### এই chapter-এর ৫টা সোনার নিয়ম
1. **আগে clarify করুন (Listen)।** "পেন test করো"-র মতো প্রশ্নে সরাসরি শুরু করবেন না — scope ছোট করুন। এটাই junior থেকে senior-এর পার্থক্য।
2. **প্রতিটা test case তিন ভাগে ভাবুন: normal / edge / stress।** তাহলে গুরুত্বপূর্ণ case মিস হবে না।
3. **real-world জিনিস = 5-step framework** (Who → use cases → edge/stress → কী → কীভাবে)।
4. **"কীভাবে ভাঙতে পারে?" ভাবুন** — শুধু happy path নয়। edge, failure, security-ই আসল test।
5. **Debug প্রশ্নে "কারণ + কীভাবে যাচাই" দুটোই দিন;** একটা মাত্র সম্ভাবনায় থেমে যাবেন না।

> **পরের ধাপ:** [Chapter 12 — C & C++](chapter12_c_cpp.md), যেখানে pointer, memory, virtual function-এর মতো C/C++-এর নিজস্ব ধারণাগুলো শিখব।

<a id="toc"></a>
# Cracking the Coding Interview — সম্পূর্ণ বাংলা গাইড

> ১৮৯টা প্রশ্নের পূর্ণাঙ্গ ব্যাখ্যা — বাংলায়। Technical term ইংরেজিতে, code **Dart + Python** দুটোতেই, প্রচুর ASCII diagram + mermaid।
> এটাই **মূল Index** — এখান থেকে যেকোনো chapter-এ যান; প্রতিটা প্রশ্ন থেকে আবার এখানে ফিরে আসতে পারবেন।

---

## কীভাবে ব্যবহার করবেন

- প্রতিটা **chapter একটা আলাদা `.md` ফাইল**। chapter-এর শুরুতে একটা **সূচি (Table of Contents)** আছে — সেখান থেকে যেকোনো প্রশ্নে লাফ দিন।
- প্রতিটা প্রশ্নের শেষে **"↑ Chapter সূচি"** আর **"মূল Index"** link আছে — এক ক্লিকে ফিরে আসুন।
- পড়ার নিয়ম: আগে নিজে ১৫ মিনিট চেষ্টা করুন → তারপর solution → তারপর কোড বন্ধ করে নিজে আবার লিখুন।

---

## পড়ার রোডম্যাপ (অল্প সময়ে interview-ready)

```
ধাপ ০:  Foundation (Big-O + 7-Step Approach)   <- সবার আগে, এটাই ভিত্তি
ধাপ ১:  Core (সবচেয়ে বেশি জিজ্ঞেস করে):  Ch 1, 2, 3, 4, 8, 10
ধাপ ২:  Design round:                      Ch 7 (OOD), Ch 9 (System Design)
ধাপ ৩:  বাকিগুলো:                          Ch 5, 6, 14, 16, 17
ধাপ ৪:  ভাষা-নির্ভর (দরকার হলে):           Ch 11, 12, 13, 15
```

**7-Step Approach (প্রতিটা problem-এ):** Listen → Draw Example → Brute Force → Optimize (BUD) → Walk Through → Implement → Test.

---

## সব Chapter (Index)

| # | Chapter | প্রশ্ন | সংখ্যা | অগ্রাধিকার |
|---|---|---|---|---|
| 0 | [Foundation — Big-O + 7-Step](chapter00_foundation.md) | — | — | অবশ্যই আগে |
| 1 | [Arrays & Strings](chapter01_arrays_strings.md) | 1.1–1.9 | 9 | উচ্চ |
| 2 | [Linked Lists](chapter02_linked_lists.md) | 2.1–2.8 | 8 | উচ্চ |
| 3 | [Stacks & Queues](chapter03_stacks_queues.md) | 3.1–3.6 | 6 | মাঝারি |
| 4 | [Trees & Graphs](chapter04_trees_graphs.md) | 4.1–4.12 | 12 | উচ্চ (সবচেয়ে common) |
| 5 | [Bit Manipulation](chapter05_bit_manipulation.md) | 5.1–5.8 | 8 | নিম্ন |
| 6 | [Math & Logic Puzzles](chapter06_math_logic_puzzles.md) | 6.1–6.10 | 10 | কম |
| 7 | [Object-Oriented Design](chapter07_object_oriented_design.md) | 7.1–7.12 | 12 | মাঝারি |
| 8 | [Recursion & Dynamic Programming](chapter08_recursion_dp.md) | 8.1–8.14 | 14 | উচ্চ |
| 9 | [System Design & Scalability](chapter09_system_design_scalability.md) | 9.1–9.8 | 8 | মাঝারি |
| 10 | [Sorting & Searching](chapter10_sorting_searching.md) | 10.1–10.11 | 11 | উচ্চ |
| 11 | [Testing](chapter11_testing.md) | 11.1–11.6 | 6 | কম |
| 12 | [C & C++](chapter12_c_cpp.md) | 12.1–12.11 | 11 | optional |
| 13 | [Java](chapter13_java.md) | 13.1–13.8 | 8 | নিম্ন (Android-এ) |
| 14 | [Databases](chapter14_databases.md) | 14.1–14.7 | 7 | মাঝারি |
| 15 | [Threads & Locks](chapter15_threads_locks.md) | 15.1–15.7 | 7 | কম |
| 16 | [Moderate](chapter16_moderate.md) | 16.1–16.26 | 26 | মাঝারি (practice) |
| 17 | [Hard](chapter17_hard.md) | 17.1–17.26 | 26 | মাঝারি (practice) |

**মোট: ১৮৯টা প্রশ্ন।**

---

## প্রতিটা প্রশ্নের কাঠামো

1. সমস্যাটা সহজ বাংলায় — আসলে কী চাওয়া হচ্ছে
2. উদাহরণ (ASCII diagram)
3. Listen — interview-তে কী clarify করবেন
4. Brute force → Optimize (BUD) — খারাপ থেকে ভালো সমাধান
5. Code — Dart + Python
6. Complexity — Time/Space, কেন সহ
7. Pattern চিনুন — "X দেখলে → Y technique"
8. Common mistake + Follow-up প্রশ্ন

---

## অগ্রগতি

```
[done] Foundation
[done] Chapter 1 — Arrays & Strings
[..  ] Chapter 2–17  (তৈরি হচ্ছে)
```

> টিপ: কোনো প্রশ্ন আরও সহজ করে বা আরও গভীরে বুঝতে চাইলে বলুন — যেকোনো একটা problem নিয়ে আলাদা বসা যায় (mock interview, hint mode, বা line-by-line code walkthrough)।

# Section 17 — Git & Version Control

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন। Command-গুলো ঠিক যেভাবে টাইপ করবেন সেভাবেই দেখানো।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-17-git.md](../software-engineer-flutter/section-17-git.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব command সহ ধাপে ধাপে ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে ট্যাগ দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** Git-এর ক্ষেত্রে ব্যাখ্যা করুন *command আপনার history-র (commit graph) সাথে কী করে*, শুধু syntax নয়। `rebase` *কেন* history rewrite করে — এটা জানাই senior signal।

---


## <a id="toc"></a>সূচিপত্র

**A. প্রতিদিনের command**
1. [মূল command (init/clone/status/add/commit/push/pull)](#q1) · *Very common*
2. [Branching (তৈরি/switch/delete)](#q2) · *Very common*
3. [`fetch` vs `pull`](#q3) · *Common*

**B. কাজ একসাথে করা**
4. [`merge` vs `rebase`](#q4) · *Very common*
5. [Merge conflict সমাধান করা](#q5) · *Very common*
6. [`cherry-pick`](#q6) · *Common*

**C. Undo আর ঠিক করা**
7. [`reset` — soft / mixed / hard](#q7) · *Very common*
8. [`revert` vs `reset`](#q8) · *Common*
9. [শেষ commit undo করা (পরিবর্তন রেখে)](#q9) · *Common*
10. [`stash`](#q10) · *Common*

**D. History আর debugging**
11. [`log` আর `blame`](#q11) · *Common*
12. [`bisect` — খারাপ commit খুঁজে বের করা](#q12) · *Deeper*
13. [Detached HEAD](#q13) · *Deeper*

**E. Workflow আর team**
14. [`.gitignore` (Flutter-এর entry)](#q14) · *Common*
15. [Git Flow vs GitHub Flow vs Trunk-Based](#q15) · *Common*
16. [Conventional Commits](#q16) · *Common*
17. [Commit squash করা](#q17) · *Common*
18. [Pull Request আর code review](#q18) · *Very common*
19. [Production-এ hotfix](#q19) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

**পর্যায় ১ — প্রতিদিনের বেসিক (এখান থেকে শুরু করুন)।**
→ [Q1 মূল command](#q1) · [Q2 Branching](#q2) · [Q3 fetch vs pull](#q3)

**পর্যায় ২ — কাজ একসাথে করা আর ঠিক করা।**
→ [Q4 merge vs rebase](#q4) · [Q5 Conflict](#q5) · [Q7 reset](#q7) · [Q9 শেষ commit undo](#q9)

**পর্যায় ৩ — Undo করার tool আর history।**
→ [Q8 revert vs reset](#q8) · [Q10 stash](#q10) · [Q11 log আর blame](#q11)

**পর্যায় ৪ — Team workflow।**
→ [Q15 Branching strategy](#q15) · [Q16 Conventional commit](#q16) · [Q18 PR আর review](#q18) · [Q19 Hotfix](#q19)

**পর্যায় ৫ — গভীর tool-গুলো।**
→ [Q6 cherry-pick](#q6) · [Q12 bisect](#q12) · [Q13 Detached HEAD](#q13) · [Q17 squash](#q17)

**সময় কম?** দেখে নিন [Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q5](#q5) · [Q7](#q7) · [Q9](#q9), তারপর [Cheat Sheet](#cheatsheet)।

---

# A. প্রতিদিনের command

---

## <a id="q1"></a>1. `git init`, `clone`, `status`, `add`, `commit`, `push`, আর `pull` কী কাজ করে?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"এগুলো প্রতিদিনের command। `init` একটা repo শুরু করে, `clone` একটা remote repo কপি করে। `status` দেখায় কী কী বদলেছে, `add` পরিবর্তনগুলো stage করে, `commit` সেগুলো history-তে সেভ করে। `push` commit-গুলো remote-এ পাঠায়, `pull` remote-এর commit নামিয়ে আনে। ধারাটা হলো: edit → add → commit → push।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — মনের ছবি: তিনটা জায়গা।**
- **Working directory** — আপনার file, যেগুলো আপনি edit করছেন।
- **Staging area (index)** — যে পরিবর্তনগুলো পরের commit-এ রাখবেন বলে চিহ্নিত করেছেন (`add`)।
- **Repository** — commit-এর সেভ করা history (`commit`)।

**ধাপ ২ — একটা repo শুরু করা।**

```bash
git init               # বর্তমান folder-কে নতুন Git repo বানায়
git clone <url>        # আগে থেকে থাকা remote repo কপি করে (history সহ)
```

**ধাপ ৩ — প্রতিদিনের চক্র।**

```bash
git status             # কী বদলেছে / কী stage হয়ে আছে
git add file.dart      # একটা file stage করে  (git add . = সব stage করা)
git commit -m "feat: add login"   # stage করা পরিবর্তন history-তে সেভ করে
git push               # commit-গুলো remote-এ পাঠায় (যেমন GitHub)
git pull               # remote commit নামায় + আপনার branch-এ merge করে
```

**ধাপ ৪ — একটা commit হলো একটা save point।**
Commit-কে ভাবুন video game-এর নাম দেওয়া save point হিসেবে — যেকোনো সময় সেখানে ফিরে যেতে পারবেন। প্রতিটা commit রাখে *কী* বদলেছে, *কে* বদলেছে, আর *কখন* বদলেছে।

**Interviewer কেন জিজ্ঞেস করে:** এটা একেবারে ভিত্তি; তাঁরা নিশ্চিত হতে চান আপনি staging → commit → push ধারাটা বোঝেন।

**সাধারণ ভুল:** `add` (stage) আর `commit` (সেভ) গুলিয়ে ফেলা। `add` শুধু পরিবর্তন চিহ্নিত করে; `commit` সেগুলো রেকর্ড করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"add vs commit?"* → `add` stage করে; `commit` stage করা পরিবর্তন সেভ করে।
- *"একটা commit কী কী রাখে?"* → একটা snapshot, একজন author, একটা message, আর তার parent commit-এর link।

**সম্পর্কিত:** [Q2 — branching](#q2) · [Q3 — fetch vs pull](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. একটা branch কীভাবে তৈরি করবেন, switch করবেন, আর delete করবেন?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Branch হলো কাজের একটা আলাদা লাইন, যাতে main code না ছুঁয়েই feature বানানো যায়। `git switch -c name` দিয়ে তৈরি করে switch করি, `git switch` দিয়ে branch-এর মধ্যে ঘোরাঘুরি করি, আর merge হয়ে যাওয়া branch `git branch -d` দিয়ে delete করি। আধুনিক command হলো `switch` আর `restore`; পুরোনো tutorial-এ `checkout` ব্যবহার হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব ছবি: একটা পাশাপাশি কাজের জায়গা।**
Branch হলো project-এর একটা কপির মতো, যেখানে আপনি স্বাধীনভাবে পরীক্ষা করতে পারেন। কাজ করলে সেটা merge করে দেন; না করলে delete করে দেন — main নিরাপদ থাকে।

**ধাপ ২ — Command-গুলো।**

```bash
git branch                 # branch-এর তালিকা দেখায়
git switch -c feature/login   # নতুন branch তৈরি করে এবং সেখানে switch করে
git switch main            # main-এ ফিরে যায়
git branch -d feature/login   # merge হওয়া branch delete করে (জোর করতে -D)
git push -u origin feature/login  # নতুন branch remote-এ push করে
```

(`git checkout -b feature/login` হলো `switch -c`-এর পুরোনো সমতুল্য রূপ।)

**ধাপ ৩ — Branch কেন গুরুত্বপূর্ণ।**
এতে অনেক মানুষ একসাথে কাজ করতে পারেন একে অন্যের গায়ে না পড়ে, আর `main` সবসময় release-যোগ্য থাকে। শেষ হওয়া branch আপনি Pull Request দিয়ে merge করেন ([Q18](#q18))।

**Interviewer কেন জিজ্ঞেস করে:** Branching হলো team workflow-এর মূল ভিত্তি; তাঁরা নিশ্চিত হতে চান আপনি branch-এ কাজ করেন, সরাসরি main-এ নয়।

**সাধারণ ভুল:** সরাসরি `main`-এ commit করা। বাস্তব team `main`-কে protect করে আর review হওয়া branch দিয়ে merge করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"switch vs checkout?"* → `switch`/`restore` নতুন এবং বেশি পরিষ্কার command; `checkout` দুটো কাজই করে (আরও বেশি করে), যেটা বিভ্রান্তিকর।

**সম্পর্কিত:** [Q15 — branching strategy](#q15) · [Q18 — pull request](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. `git fetch` আর `git pull`-এর মধ্যে পার্থক্য কী?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`fetch` remote থেকে সর্বশেষ commit নামায়, কিন্তু আপনার working branch বদলায় না — এটা শুধু remote সম্পর্কে আপনার জানাটা update করে। `pull` একটা `fetch` করে, তারপর সাথে সাথে সেই পরিবর্তনগুলো আপনার বর্তমান branch-এ merge করে। তাই `pull = fetch + merge`।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `fetch` — দেখুন, ছোঁবেন না।**

```bash
git fetch          # remote commit নামায়; আপনার file অপরিবর্তিত থাকে
git log origin/main   # merge করার আগে নতুন কী আছে দেখে নিতে পারেন
```

`fetch` নিরাপদ — এটা কখনোই আপনার working file বদলায় না। এটা শুধু remote-tracking branch (`origin/main`) update করে।

**ধাপ ২ — `pull` — এক ধাপে fetch আর merge।**

```bash
git pull           # = git fetch + git merge origin/<branch>
```

এটা আপনার বর্তমান branch সাথে সাথে update করে। সুবিধাজনক, কিন্তু হঠাৎ একটা merge বা conflict তৈরি করতে পারে।

**ধাপ ৩ — কখন কোনটা ব্যবহার করবেন।**
- **`fetch`** — যখন remote-এর পরিবর্তন আগে দেখে নিতে চান (বেশি নিরাপদ)।
- **`pull`** — যখন শুধু দ্রুত update হতে চান।
- `git pull --rebase` আপনার local commit-গুলো remote commit-এর উপরে বসায়, ফলে history সরলরেখায় থাকে ([rebase](#q4) দেখুন)।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি বোঝেন কি না যে `pull` চুপচাপ merge করে ফেলে, আর সেটা আপনাকে চমকে দিতে পারে।

**সাধারণ ভুল:** ভাবা যে `fetch` আপনার file update করে (করে না), অথবা uncommitted পরিবর্তনের উপর `pull` করে এলোমেলো conflict বাধিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`origin` কী?"* → যে remote থেকে clone করেছেন, তার default নাম।

**সম্পর্কিত:** [Q1 — মূল command](#q1) · [Q4 — merge vs rebase](#q4)

[↑ উপরে ফিরুন](#toc)

---

# B. কাজ একসাথে মেলানো

---

## <a id="q4"></a>4. `git merge` আর `git rebase`-এর পার্থক্য কী? কোনটা কখন ব্যবহার করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"দুটোই দুই branch-এর কাজ একসাথে করে, কিন্তু আলাদা ভাবে। `merge` একটা নতুন merge commit দিয়ে দুটোকে জোড়া লাগায়, আর আসল history রেখে দেয় (branch গুলো যে মিলেছে সেটা দেখা যায়)। `rebase` আপনার commit গুলোকে অন্য branch-এর উপরে আবার বসায়, ফলে history পরিষ্কার আর সোজা হয় — কিন্তু এটা আপনার commit গুলো নতুন করে লেখে। মূল নিয়ম: যে commit আপনি ইতিমধ্যে share/push করেছেন, সেগুলো কখনোই rebase করবেন না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `merge` — জোড়া লাগায়, history রেখে দেয়।**

```bash
git switch main
git merge feature   # একটা merge commit বানায় যা দুই history জোড়া দেয়
```

History দেখায় branch আলাদা হয়েছিল আর আবার ফিরে এসেছে — সৎ, কিন্তু দেখতে এলোমেলো লাগতে পারে।

**ধাপ ২ — `rebase` — আবার চালায়, সোজা লাইন বানায়।**

```bash
git switch feature
git rebase main     # feature-এর commit গুলোকে সর্বশেষ main-এর উপরে সরায়
```

দেখে মনে হয় আপনি কাজটা শুরু করেছেন সর্বশেষ main-এর *পরে* — একটা পরিষ্কার সোজা লাইন। কিন্তু commit গুলো *নতুন করে লেখা* হয় (নতুন ID)।

**ধাপ ৩ — ছবিটা।**

```
merge:                 rebase:
  A---B---C main         A---B---C main
       \   \                      \
        D---E feature              D'--E' feature (replayed on top)
```

**ধাপ ৪ — মূল নিয়ম।**
**অন্যদের কাছে ইতিমধ্যে আছে এমন commit কখনোই rebase করবেন না** (যেমন কোনো shared branch-এ push করা)। Rebase history নতুন করে লেখে। ফলে বাকি সবার copy ভেঙে যাবে। *Local, push না করা* কাজ rebase করুন; shared branch merge করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা Git-এর ক্লাসিক judgment প্রশ্ন — পরিষ্কার history বনাম নিরাপত্তা।

**সাধারণ ভুল:** কোনো shared/push করা branch rebase করে force-push করা, ফলে সহকর্মীদের history ভেঙে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"rebase কেন commit ID বদলে দেয়?"* → এটা একই changes নিয়ে নতুন commit বানায়, কিন্তু parent আলাদা হয়। তাই hash আলাদা হয়।
- *"pull --rebase?"* → আগে fetch করে, তারপর আপনার local commit গুলো উপরে rebase করে — history সোজা থাকে।

**সম্পর্কিত:** [Q5 — conflict](#q5) · [Q3 — fetch বনাম pull](#q3) · [Q17 — squash](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Merge conflict কেন হয়, আর ধাপে ধাপে কীভাবে সমাধান করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Conflict হয় যখন দুটো branch একই file-এর *একই line* আলাদা ভাবে বদলায়। তখন Git ঠিক করতে পারে না কোনটা রাখবে। সমাধান করতে হয় marker দেওয়া file খুলে, সঠিক final code বেছে নিয়ে, conflict marker গুলো মুছে, তারপর stage আর commit করে। সমাধানের পরে test চালানো খুব জরুরি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের একটা ছবি।**
দুজন মানুষ একটা shared document-এ একই বাক্য edit করছেন। System জানে না কোন version সঠিক। তাই এটা একজন মানুষকে (আপনাকে) সিদ্ধান্ত নিতে বলে।

**ধাপ ২ — Conflict দেখতে কেমন।**

```
<<<<<<< HEAD
final color = Colors.blue;     // আপনার version
=======
final color = Colors.green;    // তাদের version
>>>>>>> feature
```

**ধাপ ৩ — ধাপে ধাপে সমাধান।**

```bash
# 1. Git বলে দেয় কোন file গুলোতে conflict
git status

# 2. প্রতিটা file খুলুন, সঠিক final code বেছে নিন, আর
#    <<<<<<<, =======, >>>>>>> marker line গুলো মুছে দিন।

# 3. resolve করা file stage করুন
git add lib/theme.dart

# 4. merge শেষ করুন
git commit          # (অথবা: rebase করলে git rebase --continue)

# 5. app/test চালিয়ে দেখুন কিছু ভাঙেনি
```

**ধাপ ৪ — Conflict কম করার উপায়।**
ঘনঘন pull/rebase করুন (ছোট ছোট, বারবার merge)। Branch বেশি দিন বাঁচিয়ে রাখবেন না। Function ছোট রাখুন, তাহলে দুজনের একই line ছোঁয়ার সম্ভাবনা কমে।

**Interviewer কেন জিজ্ঞেস করে:** Conflict সবারই হয়। তাঁরা দেখতে চান আপনি ঠান্ডা মাথায় ঠিকভাবে সমাধান করেন, নাকি ভয় পেয়ে `--force` মারেন।

**সাধারণ ভুল:** File-এ একটা `<<<<<<<` marker রেখে দেওয়া (এতে build ভেঙে যায়)। অথবা logic না দেখে চোখ বন্ধ করে এক দিক মেনে নেওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কীভাবে বাতিল করবেন?"* → `git merge --abort` (বা `git rebase --abort`) শুরুর আগের অবস্থায় ফিরিয়ে নেয়।

**সম্পর্কিত:** [Q4 — merge বনাম rebase](#q4) · [Q10 — stash](#q10)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. `git cherry-pick` কী, আর কখন এটা ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`cherry-pick` অন্য branch থেকে একটা নির্দিষ্ট commit কপি করে আপনার বর্তমান branch-এ আনে, পুরো branch merge না করেই। একটামাত্র fix নিতে এটা ব্যবহার করা হয় — যেমন, main থেকে বাকি সব কিছু না এনে শুধু একটা bug fix release branch-এ বসানো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা চেরি তোলা।**
পুরো গাছ না নিয়ে (মানে full merge), আপনি ঠিক যে একটা চেরি (একটা commit) চান সেটাই তুলে নিলেন।

**ধাপ ২ — কীভাবে ব্যবহার করবেন।**

```bash
git switch release/1.2
git cherry-pick a1b2c3d   # ওই একটা commit-এর changes এই branch-এ কপি করে
```

এটা আপনার branch-এ একই changes নিয়ে একটা *নতুন* commit বানায় (নতুন ID)।

**ধাপ ৩ — সবচেয়ে সাধারণ ব্যবহার: fix backport করা।**
একটা জরুরি bug fix `main`-এ merge হয়েছে। কিন্তু এটা আপনার পুরোনো `release` branch-এও দরকার, যেটা main-এর সব কিছু নেওয়ার জন্য তৈরি নয়। তখন শুধু ওই fix commit-টা release branch-এ cherry-pick করুন।

**ধাপ ৪ — সাবধান থাকুন।**
একই change এমন branch গুলোতে cherry-pick করলে, যেগুলো পরে merge হবে, duplicate commit বা conflict হতে পারে। ভেবেচিন্তে ব্যবহার করুন, আলাদা আলাদা fix-এর জন্য।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি একটা মাত্র change ঠিকঠাক সরাতে পারেন কি না — release management-এর একটা বাস্তব দরকার।

**সাধারণ ভুল:** merge না করে অনেকগুলো commit cherry-pick করা — এতে ভুল হওয়ার ঝুঁকি বেশি; অনেক commit-এর জন্য merge/rebase ভালো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Cherry-pick বনাম merge?"* → Cherry-pick একটা commit নেয়; merge পুরো branch নিয়ে আসে।

**সম্পর্কিত:** [Q19 — hotfix](#q19) · [Q4 — merge বনাম rebase](#q4)

[↑ উপরে ফিরুন](#toc)

---

# C. Undo করা ও ঠিক করা

---

## <a id="q7"></a>7. `git reset --soft`, `--mixed`, আর `--hard`-এর পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"তিনটাই branch pointer-কে আগের একটা commit-এ ফিরিয়ে নেয়; পার্থক্য হলো আপনার changes-এর সাথে কী করে। `--soft` changes staged রেখে দেয়, `--mixed` (default) সেগুলো unstaged করে রাখে, আর `--hard` changes একদম ফেলে দেয়। `--hard` হলো বিপজ্জনকটা — এটা কাজ মুছে ফেলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটাই history পিছিয়ে দেয়; পার্থক্য আপনার file-এ।**

| Mode | Branch পিছিয়ে যায়? | Staging area | Working file |
|---|---|---|---|
| `--soft` | হ্যাঁ | changes **staged** থাকে | থাকে |
| `--mixed` (default) | হ্যাঁ | changes **unstaged** হয়ে যায় | থাকে |
| `--hard` | হ্যাঁ | খালি হয়ে যায় | **মুছে যায় (নেই)** |

**ধাপ ২ — উদাহরণ।**

```bash
git reset --soft HEAD~1    # শেষ commit undo, changes staged থাকে (সহজে re-commit)
git reset --mixed HEAD~1   # শেষ commit undo, changes আবার unstaged
git reset --hard HEAD~1    # শেষ commit undo আর changes মুছে ফেলা — সাবধান!
```

**ধাপ ৩ — নিরাপদ mental model।**
- `--soft` / `--mixed` → "commit undo করো, আমার কাজ রেখে দাও।"
- `--hard` → "commit undo করো আর আমার কাজ মুছে দাও।" নিশ্চিত হলে তবেই ব্যবহার করুন।

**ধাপ ৪ — Reset history নতুন করে লেখে।**
Rebase-এর মতোই `reset` history বদলে দেয় — shared branch-এ push করা commit reset করবেন না। Shared branch-এর জন্য `revert` ব্যবহার করুন ([Q8](#q8))।

**Interviewer কেন জিজ্ঞেস করে:** এটা undo সম্পর্কে খুঁটিনাটি জ্ঞান দেখে, আর আপনি জানেন কি না যে `--hard` কাজ নষ্ট করে দেয়।

**সাধারণ ভুল:** `git reset --hard` চালিয়ে commit না করা কাজ হারিয়ে ফেলা। (কখনো কখনো `git reflog` দিয়ে ফেরত পাওয়া যায়, কিন্তু এর উপর ভরসা করবেন না।)

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"খারাপ reset-এর পরে কীভাবে ফেরত পাবেন?"* → `git reflog` দেখায় HEAD কোথায় কোথায় ছিল; সেখান থেকে হারানো commit-এ reset করে ফিরতে পারবেন।

**সম্পর্কিত:** [Q8 — revert বনাম reset](#q8) · [Q9 — শেষ commit undo](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. `git revert` কী, আর `git reset`-এর সাথে এর পার্থক্য কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`revert` একটা *নতুন* commit বানায়, যেটা আগের একটা commit-এর পরিবর্তন বাতিল করে। history অক্ষত থাকে। `reset` branch pointer-কে পেছনে সরিয়ে দেয় আর history rewrite করে। তাই shared/public branch-এর জন্য `revert` নিরাপদ পছন্দ। আর push করার আগে local cleanup-এর জন্য `reset`।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `revert` — নতুন commit যোগ করে undo করা।**

```bash
git revert a1b2c3d   # নতুন একটা commit বানায় যা a1b2c3d-এর পরিবর্তন উল্টে দেয়
```

History-তে মূল commit আর revert — দুটোই থাকে। এটা সৎ, আর shared branch-এর জন্য নিরাপদ।

**ধাপ ২ — `reset` — history পেছনে নিয়ে undo করা।**

```bash
git reset --hard a1b2c3d   # branch পেছনে সরে যায়; পরের commit-গুলো history থেকে উধাও
```

এটা history rewrite করে। তাই অন্যদের কাছে সেই commit চলে গেলে এটা অনিরাপদ।

**ধাপ ৩ — নিয়মটা।**

| | `revert` | `reset` |
|---|---|---|
| History | অক্ষত থাকে (একটা commit যোগ করে) | rewrite হয় (pointer সরে যায়) |
| Shared branch-এ নিরাপদ? | **হ্যাঁ** | না |
| কীসের জন্য | push করা/public commit undo করতে | push করার আগে local cleanup |

**ধাপ ৪ — একটা ছবি।**
`revert` বলে — "আমি নতুন একটা ধাপ যোগ করব, যেটা পুরোনো ধাপটা বাতিল করবে।" `reset` বলে — "চলো ধরে নিই পুরোনো ধাপটা কখনো ঘটেইনি।" Team branch-এ আপনার দরকার সৎ আর যোগ করার ধরনের `revert`।

**Interviewer কেন জিজ্ঞেস করে:** এটা পরীক্ষা করে আপনি shared history-র জন্য নিরাপদ undo বেছে নেন কি না।

**সাধারণ ভুল:** push করা branch-এ `reset --hard` করে force-push দেওয়া। এতে teammate-দের কাজ ভেঙে যায়। সেখানে `revert` ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Merge commit revert করবেন কীভাবে?"* → `git revert -m 1 <merge>` দিয়ে কোন parent রাখবেন সেটা বলে দিন।

**সম্পর্কিত:** [Q7 — reset mode](#q7) · [Q19 — hotfix](#q19)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. পরিবর্তন না হারিয়ে শেষ commit undo করবেন কীভাবে?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`git reset --soft HEAD~1` ব্যবহার করি। এটা শেষ commit সরিয়ে দেয়, কিন্তু সব পরিবর্তন staged থাকে। ফলে message ঠিক করে বা আরও কিছু যোগ করে আবার commit করা যায়। শুধু message ঠিক করতে বা ভুলে যাওয়া file যোগ করতে চাইলে `git commit --amend` আরও সহজ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — commit undo করুন, কাজ রেখে দিন।**

```bash
git reset --soft HEAD~1   # শেষ commit undo হলো; পরিবর্তন staged-ই থাকে
# আরও কিছু edit/add করুন, তারপর:
git commit -m "feat: better message"
```

`HEAD~1` মানে "বর্তমান commit-এর ঠিক আগের commit।"

**ধাপ ২ — শুধু শেষ commit ঠিক করছেন? `--amend` ব্যবহার করুন।**

```bash
git commit --amend -m "fix: correct typo in message"   # শেষ commit-টা rewrite করে
git add forgotten.dart && git commit --amend --no-edit  # ভুলে যাওয়া file যোগ করে
```

**ধাপ ৩ — সাবধানতা।**
দুটোই history rewrite করে। commit আগেই push করে ফেললে amend/reset করার মানে force-push লাগবে। এটা শুধু নিজের branch-এ করুন, shared branch-এ কখনোই না ([Q8](#q8))।

**Interviewer কেন জিজ্ঞেস করে:** এটা প্রতিদিনের কাজ। তাঁরা দেখেন আপনি নিরাপদ, পরিবর্তন-রক্ষাকারী উপায়টা জানেন কি না।

**সাধারণ ভুল:** পরিবর্তন রাখতে চেয়েও `git reset --hard HEAD~1` ব্যবহার করা (এটা পরিবর্তন মুছে দেয়) — `--soft` ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Amend না reset?"* → Amend শেষ commit-টাকে জায়গাতেই edit করে; reset সেটা সরিয়ে কাজটা আবার stage করে।

**সম্পর্কিত:** [Q7 — reset mode](#q7) · [Q17 — squash](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. `git stash` কী করে, আর stash করা পরিবর্তন কীভাবে ফিরিয়ে আনবেন?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`stash` আপনার uncommitted পরিবর্তন সাময়িকভাবে সরিয়ে রাখে, ফলে working directory পরিষ্কার হয়ে যায় — অর্ধেক করা কাজ commit না করেই দ্রুত branch বদলাতে হলে এটা কাজে লাগে। `stash pop` দিয়ে পরিবর্তনগুলো ফিরিয়ে আনা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: অসমাপ্ত কাজের জন্য একটা ড্রয়ার।**
আপনি feature-এর মাঝপথে আছেন, এমন সময় একটা জরুরি bug এলো। অর্ধেক করা code commit করা যায় না। তাই সেটা ড্রয়ারে (stash) রেখে দিন, bug ঠিক করুন, তারপর আবার বের করে আনুন।

**ধাপ ২ — command-গুলো।**

```bash
git stash             # এখনকার পরিবর্তন সরিয়ে রাখে; working dir এখন পরিষ্কার
git switch main       # কিছু একটা ঠিক করতে যান
git switch feature
git stash pop         # পরিবর্তন ফিরিয়ে আনে এবং stash থেকে সরিয়েও দেয়
```

**ধাপ ৩ — কাজের variant-গুলো।**

```bash
git stash list        # সব stash দেখুন
git stash apply       # পরিবর্তন ফিরিয়ে আনে কিন্তু stash-এ রেখেও দেয়
git stash -u          # untracked (নতুন) file-ও stash করে
git stash drop        # একটা stash মুছে দেয়
```

**ধাপ ৪ — কখন ব্যবহার করবেন।**
ছোট বিরতির জন্য। লম্বা বিরতির জন্য একটা branch-এ দ্রুত commit (এমনকি WIP হলেও) ভুলে যাওয়া stash-এর চেয়ে নিরাপদ।

**Interviewer কেন জিজ্ঞেস করে:** এটা প্রতিদিনের একটা সাধারণ tool। তাঁরা দেখেন আপনি পরিষ্কারভাবে context-switch করতে পারেন কি না।

**সাধারণ ভুল:** stash করা কাজের কথা ভুলে যাওয়া (`git stash list` সেটা দেখিয়ে দেয়), অথবা branch-এর মাঝে stash করে কোথায় apply হবে তা নিয়ে গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"pop না apply?"* → `pop` apply করে এবং stash সরিয়ে দেয়; `apply` সেটা stash list-এ রেখে দেয়।

**সম্পর্কিত:** [Q5 — conflict](#q5) · [Q2 — branching](#q2)

[↑ উপরে ফিরুন](#toc)

---

# D. History ও debugging

---

## <a id="q11"></a>11. `git log` আর `git blame` কীভাবে ব্যবহার করেন?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`git log` commit history দেখায় — কে কী বদলেছে আর কখন। `git blame` line ধরে ধরে দেখায়, কোন commit শেষবার file-এর প্রতিটা line বদলেছে। দুটো মিলে history বুঝতে সাহায্য করে, আর একটা line কখন ও কেন এসেছে তা খুঁজে দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — `git log` — history।**

```bash
git log --oneline --graph --all   # সব branch-এর সংক্ষিপ্ত, ছবির মতো history
git log -p file.dart              # একটা file-এর history আসল diff সহ
git log --author="srana"          # একজন ব্যক্তির commit
```

`--oneline --graph` প্রতিদিনের কাজে সবচেয়ে দরকারি view।

**ধাপ ২ — `git blame` — প্রতিটা line শেষবার কে ছুঁয়েছে।**

```bash
git blame lib/login.dart          # প্রতিটা line-এ শেষ commit + author লেখা থাকে
```

এটা *বোঝার* জন্য, মানুষকে দোষ দেওয়ার জন্য নয় — যে commit line-টা এনেছে সেটা খুঁজে বের করে তার message আর context পড়ার জন্য এটা ব্যবহার করেন।

**ধাপ ৩ — একটা সাধারণ workflow।**
একটা গোলমেলে line দেখলেন → `git blame` দিয়ে তার commit খুঁজুন → `git show <commit>` দিয়ে পড়ুন কেন এটা যোগ হয়েছিল (message আর পুরো পরিবর্তন)।

**Interviewer কেন জিজ্ঞেস করে:** History পড়া debugging আর onboarding-এর একটা মূল দক্ষতা।

**সাধারণ ভুল:** `blame`-কে দোষ চাপানোর জিনিস মনে করা। এটা *context* খোঁজার tool, আঙুল তোলার নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা bug কখন এসেছে কীভাবে খুঁজবেন?"* → `git bisect` ([Q12](#q12))।

**সম্পর্কিত:** [Q12 — bisect](#q12) · [Q1 — মূল command](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. `git bisect` দিয়ে কোন commit একটা bug এনেছে তা কীভাবে খুঁজবেন?

> Deeper · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`git bisect` আপনার history-তে binary search চালিয়ে সেই commit খুঁজে বের করে, যেটা bug এনেছে। আপনি একটা known-good commit আর একটা known-bad commit চিহ্নিত করেন। Git মাঝের commit-টা checkout করে দেয়, আপনি সেটা test করেন। এভাবে বারবার range অর্ধেক হতে হতে ঠিক খারাপ commit-টা বেরিয়ে আসে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ধারণাটা: commit-এর উপর binary search।**
শেষ 100টা commit-এর কোথাও bug এসে থাকলে bisect সেটা প্রায় 7 ধাপে খুঁজে দেয় (log₂ 100), 100 ধাপে নয় — প্রতিবার অর্ধেক করে ([binary search](section-11-data-structure-bn.md#q11))।

**ধাপ ২ — Workflow।**

```bash
git bisect start
git bisect bad                # এখনকার commit ভাঙা
git bisect good v1.0          # এই পুরোনো commit/tag কাজ করত

# Git মাঝের একটা commit checkout করে। সেটা test করুন, তারপর Git-কে বলুন:
git bisect good   # এই commit কাজ করলে
git bisect bad    # ভাঙা থাকলে

# আবার করুন। Git ছোট করতে করতে প্রথম খারাপ commit-এর নাম বলে দেবে।
git bisect reset  # শেষ হলে নিজের branch-এ ফিরে আসুন
```

**ধাপ ৩ — এটাকে automate করুন।**
আপনার একটা test script থাকলে `git bisect run ./test.sh` প্রতি ধাপে সেটা নিজে চালায় — কোনো হাতে করা test ছাড়াই Git খারাপ commit খুঁজে দেয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা উন্নত debugging পরীক্ষা করে — আর আপনি বাস্তব সমস্যায় binary search কাজে লাগাতে পারেন কি না।

**সাধারণ ভুল:** এক এক commit ধরে হাতে খোঁজা, যেখানে bisect অল্প কয়েক ধাপেই খুঁজে দিত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা দ্রুত কেন?"* → প্রতি ধাপে search range অর্ধেক করে — O(log n)।

**সম্পর্কিত:** [Q11 — log ও blame](#q11) · [Q11 (DSA) — binary search](section-11-data-structure-bn.md#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. Detached HEAD state কী? এটা কীভাবে হয়, আর কীভাবে recover করবেন?

> Deeper · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"সাধারণত HEAD একটা branch-কে point করে। 'detached HEAD' মানে HEAD কোনো branch নয়, সরাসরি একটা নির্দিষ্ট commit-কে point করছে — সাধারণত একটা commit hash বা tag checkout করার কারণে। ওখানে যে commit করবেন সেগুলো কোনো branch-এ থাকে না, আর হারিয়ে যেতে পারে। Recover করতে হলে অন্য জায়গায় যাওয়ার আগেই এখানেই একটা branch বানিয়ে নিন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — 'detached HEAD' মানে কী।**
HEAD মানে "আপনি এখন কোথায় আছেন।" সাধারণত এটা একটা branch-কে follow করে (`main`)। আপনি যদি সরাসরি একটা commit checkout করেন, HEAD ঠিক ওই commit-কে point করে — নতুন commit রাখার মতো কোনো branch থাকে না।

```bash
git checkout a1b2c3d   # এখন detached HEAD-এ — HEAD commit-কে point করছে, branch-কে নয়
```

**ধাপ ২ — কেন এটা ঝুঁকির কাজ।**
এখানে commit করে তারপর অন্য branch-এ `switch` করলে, ওই commit-গুলো কোনো কিছুর সাথে যুক্ত থাকে না। ফলে খুঁজে পাওয়া কঠিন হয়ে যায় (cleanup-এর জন্য যোগ্য হয়ে যায়)।

**ধাপ ৩ — কীভাবে recover করবেন / নিরাপদে ব্যবহার করবেন।**

```bash
# রাখতে চান এমন commit করে ফেললে, ঠিক এখানেই একটা branch বানান:
git switch -c my-fix
# এখন আপনার commit-গুলো 'my-fix' branch-এ নিরাপদে আছে।
```

কোনো commit না করে থাকলে শুধু `git switch main` দিয়ে নিরাপদে বেরিয়ে যান।

**ধাপ ৪ — কখন এটা ইচ্ছাকৃত।**
পুরোনো একটা commit বা tag *দেখার* জন্য এটা ঠিক আছে (read-only)। শুধু আগে branch না বানিয়ে ওখানে গুরুত্বপূর্ণ কাজ করবেন না।

**Interviewer কেন জিজ্ঞেস করে:** এটা HEAD, branch, আর commit কীভাবে "হারায়" — এসবের গভীর বোঝাপড়া যাচাই করে।

**সাধারণ ভুল:** detached HEAD-এ commit করা, তারপর অন্য জায়গায় switch করে সেগুলো হারিয়ে ফেলা। সবসময় আগে branch বানান।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা commit হারিয়ে গেছে — ফেরত আনতে পারবেন?"* → `git reflog` সাম্প্রতিক HEAD position দেখায়; হারানো commit থেকে branch বানাতে পারবেন।

**সম্পর্কিত:** [Q2 — branching](#q2) · [Q7 — reset (reflog recovery)](#q7)

[↑ উপরে ফিরুন](#toc)

---

# E. Workflow আর team

---

## <a id="q14"></a>14. `.gitignore` কী, আর Flutter-এ সাধারণ entry কোনগুলো?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`.gitignore`-এ সেই file আর folder-এর তালিকা থাকে যেগুলো Git track করবে না — build output, secret, আর মেশিন-নির্দিষ্ট file। Flutter-এ `build/`, `.dart_tool/`, IDE file, আর `.env` বা signing key-এর মতো secret আছে এমন সব কিছু ignore করা হয়। উদ্দেশ্য হলো repo পরিষ্কার রাখা, আর generated বা sensitive file কখনোই commit না করা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কেন file ignore করবেন।**
- **Generated** file (build output) শুধু repo ভারী করে আর conflict তৈরি করে।
- **Secret** (API key, keystore) কখনোই commit করা যাবে না।
- **মেশিন-নির্দিষ্ট** file (IDE config) প্রতি developer-এর জন্য আলাদা হয়।

**ধাপ ২ — একটা সাধারণ Flutter `.gitignore`।**

```gitignore
# Dart/Flutter
build/
.dart_tool/
.packages
.flutter-plugins
.flutter-plugins-dependencies
pubspec.lock        # (app সাধারণত এটা commit করে; package প্রায়ই করে না)

# IDE
.idea/
*.iml
.vscode/

# Secret — এগুলো কখনোই commit করবেন না
.env
*.keystore
*.jks
ios/Runner/GoogleService-Info.plist  # যদি এতে secret থাকে
android/key.properties
```

**ধাপ ৩ — আগেই যদি একটা secret commit করে ফেলে থাকেন।**
`.gitignore`-এ যোগ করলে সেটা history থেকে মুছে যায় না। আপনাকে history থেকে সরাতে হবে (যেমন `git filter-repo`) **এবং** ফাঁস হওয়া key rotate করতে হবে, কারণ এটা এখনো পুরোনো commit-এ আছে।

**Interviewer কেন জিজ্ঞেস করে:** এটা basic repo hygiene আর নিরাপত্তা-সচেতনতা যাচাই করে (secret commit না করা)।

**সাধারণ ভুল:** `build/` বা secret commit করে ফেলা, তারপর ভাবা যে `.gitignore` সেগুলো সরিয়ে দেবে — এটা শুধু *untracked* file-কেই সামনের দিকে ignore করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আগে থেকেই track করা file ignore করবেন কীভাবে?"* → `git rm --cached file` দিয়ে untrack করুন, তারপর এটা `.gitignore` মানবে।

**সম্পর্কিত:** [Q20 (Security) — secrets](section-20-mobile-security-bn.md#q1) · [Q1 — মূল command](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. Git Flow, GitHub Flow, আর Trunk-Based Development-এর তুলনা করুন।

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"এগুলো branching strategy, প্রতিটার structure-এর পরিমাণ আলাদা। Git Flow-তে অনেকগুলো দীর্ঘস্থায়ী branch থাকে (main, develop, feature, release, hotfix) — শক্তিশালী কিন্তু ভারী। GitHub Flow সহজ: main থেকে branch, PR, merge, deploy। Trunk-Based-এ সবাই feature flag-এর আড়ালে main-এ commit করে, খুব ছোট স্বল্পস্থায়ী branch নিয়ে — continuous delivery-র জন্য সবচেয়ে ভালো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Git Flow — সুগঠিত, অনেক branch।**
- Branch: `main` (release), `develop` (integration), সাথে `feature/`, `release/`, `hotfix/`।
- নির্ধারিত সময়ের release আর versioned software-এর জন্য ভালো।
- অসুবিধা: জটিল, অনেক merge করতে হয়, ধীর।

**ধাপ ২ — GitHub Flow — সহজ, PR-ভিত্তিক।**
- একটাই main branch; একটা ছোট feature branch বানান, Pull Request খুলুন, review, merge, deploy।
- Web app আর continuous deployment-এর জন্য ভালো।
- সহজ আর দ্রুত; দলে সবচেয়ে বেশি ব্যবহার করা flow।

**ধাপ ৩ — Trunk-Based — সবাই main-এ।**
- খুব স্বল্পস্থায়ী branch (কয়েক ঘণ্টা), অনবরত `main`-এ merge হয়; অসম্পূর্ণ কাজ **feature flag**-এর আড়ালে লুকানো থাকে।
- সত্যিকারের continuous integration/delivery সম্ভব করে।
- শক্ত automated test আর feature-flag শৃঙ্খলা দরকার।

**ধাপ ৪ — কীভাবে বেছে নেবেন।**

| Strategy | কার জন্য সবচেয়ে ভালো | জটিলতা |
|---|---|---|
| Git Flow | versioned/নির্ধারিত সময়ের release | high |
| GitHub Flow | বেশিরভাগ app, continuous deploy | low |
| Trunk-Based | দ্রুত CI/CD, পরিণত দল | medium |

**Interviewer কেন জিজ্ঞেস করে:** এটা senior পদের জন্য দল ও process নিয়ে সচেতনতা যাচাই করে।

**সাধারণ ভুল:** ছোট একটা দল যারা অনবরত ship করে, তাদের জন্যও default হিসেবে ভারী Git Flow নেওয়া, যেখানে GitHub Flow সহজ ও ভালো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Trunk-based কী দিয়ে সম্ভব হয়?"* → Feature flag + শক্ত automated test, যাতে অসম্পূর্ণ code নিরাপদে main-এ থাকতে পারে।

**সম্পর্কিত:** [Q2 — branching](#q2) · [Q18 — pull requests](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. Conventional Commits কী, আর দলগুলো কেন এটা নেয়?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Conventional Commits হলো commit message লেখার একটা মান করা format: একটা type, একটা optional scope, আর একটা description — যেমন `feat(auth): add Google login`। দলগুলো এটা নেয় কারণ একই রকম format history পড়তে সহজ করে, আর tool দিয়ে changelog ও version number নিজে থেকে তৈরি করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Format।**

```
<type>(<optional scope>): <description>

feat(auth): add Google sign-in
fix(cart): correct total when quantity is zero
docs(readme): update setup steps
refactor(home): extract header widget
```

**ধাপ ২ — সাধারণ type-গুলো।**
- `feat` — একটা নতুন feature।
- `fix` — একটা bug fix।
- `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`।

**ধাপ ৩ — দলগুলো কেন এটা নেয়।**
- **পড়ার উপযোগী history** — প্রতিটা commit কী করেছে তা চোখ বুলিয়েই বোঝা যায়।
- **Automated versioning** — tool version বাড়িয়ে দেয়: `fix` → patch, `feat` → minor, একটা `BREAKING CHANGE` → major (semantic versioning)।
- **Auto changelog** — commit type থেকে তৈরি হয়।

**ধাপ ৪ — Message অর্থবহ রাখুন।**
Description-এ imperative ভঙ্গিতে বলা উচিত *কী বদলেছে আর কেন* ("add", "fix"), "stuff" বা "wip" নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা বোঝায় আপনি পরিষ্কার, tool-বান্ধব history নিয়ে ভাবেন — দলের পরিপক্বতার একটা লক্ষণ।

**সাধারণ ভুল:** অস্পষ্ট message ("update", "fix bug", "asdf") যা পরের পাঠককে কিছুই বলে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা versioning-এর সাথে কীভাবে যুক্ত?"* → Tool `feat`/`fix`/`BREAKING CHANGE`-কে minor/patch/major version bump-এর সাথে মেলায়।

**সম্পর্কিত:** [Q18 — pull requests](#q18) · [Q1 — commits](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q17"></a>17. Commit "squash" করা মানে কী, আর কখন এটা করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Squash করা মানে কয়েকটা commit-কে এক করে ফেলা। Merge করার আগে এলোমেলো work-in-progress history (`wip`, `fix typo`, `try again`) থেকে একটা পরিষ্কার, অর্থবহ commit বানাতে এটা করা হয়। অনেক দল Pull Request-এ 'Squash and merge' করে, যাতে প্রতিটা feature main-এ একটা পরিপাটি commit হয়ে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কেন squash করবেন।**
Develop করার সময় আপনি অনেক ছোট ও এলোমেলো commit করেন। দলের বাকিদের এই শব্দদূষণ দরকার নেই — তাঁরা একটা পরিষ্কার commit চান, যেটা বলে feature-টা কী করেছে।

**ধাপ ২ — কীভাবে (interactive rebase)।**

```bash
git rebase -i HEAD~3   # শেষ ৩টা commit edit করুন
# Editor-এ প্রথমটা 'pick' রাখুন, বাকিগুলো 'squash' (বা 's') চিহ্নিত করুন
# Save → একটা সম্মিলিত commit message লিখুন।
```

**ধাপ ৩ — সহজ উপায়: Squash and merge।**
GitHub/GitLab-এ PR-এর "Squash and merge" button merge করার সময় branch-এর সব commit-কে একটায় মিলিয়ে দেয় — হাতে rebase করার দরকার নেই। এটাই সবচেয়ে প্রচলিত উপায়।

**ধাপ ৪ — সতর্কতা।**
Squash করা history rewrite করে। এটা নিজের feature branch-এ করুন, merge হওয়ার *আগে* — shared history-তে নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি `main`-এর history পরিষ্কার রাখেন কি না, আর interactive rebase বোঝেন কি না।

**সাধারণ ভুল:** আগেই shared হয়ে যাওয়া commit squash করা, অথবা দরকারি আলাদা ভাগ squash করে মুছে ফেলা (কখনো কখনো কয়েকটা যৌক্তিক commit একটা বিশাল commit-এর চেয়ে ভালো)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Squash vs merge commit?"* → Squash = প্রতি feature-এ একটা পরিপাটি commit; merge commit = branch-এর পুরো history রক্ষা পায়।

**সম্পর্কিত:** [Q4 — rebase](#q4) · [Q18 — pull requests](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. Pull Request আর code review-এর best practice কী কী (author হিসেবে আর reviewer হিসেবে)?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Author হিসেবে: PR ছোট আর একটা বিষয়ে সীমিত রাখি, কী বদলেছে আর কেন বদলেছে তার পরিষ্কার description লিখি, আর test pass করা নিশ্চিত করি। Reviewer হিসেবে: সময়মতো, ভদ্রভাবে আর নির্দিষ্ট করে review করি — হুকুম না দিয়ে প্রশ্ন করি, style-এর চেয়ে correctness আর design-এ বেশি মন দিই (style formatter সামলাক), আর যথেষ্ট ভালো হলেই approve করি, নিখুঁত হওয়ার অপেক্ষা করি না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Author হিসেবে।**
- **ছোট আর একটা বিষয়ে সীমিত** — এক PR-এ একটাই concern; বড় PR-এ review হয় ভাসা ভাসা।
- **পরিষ্কার description** — কী বদলেছে, কেন বদলেছে, আর কীভাবে test করতে হবে।
- **সব check সবুজ** — review চাওয়ার আগে test, lint আর format pass করা চাই।
- **আগে নিজে review করুন** — নিজের diff পড়ুন; স্পষ্ট সমস্যাগুলো নিজেই ধরুন।

**ধাপ ২ — Reviewer হিসেবে।**
- **সময়মতো করুন** — আটকে থাকা teammate ভারী; দ্রুত review করুন।
- **ভদ্র আর নির্দিষ্ট হোন** — "list খালি হলে কী হবে?" — এটা "এটা ভুল"-এর চেয়ে অনেক ভালো।
- **অগ্রাধিকার ঠিক করুন** — আগে correctness আর design; linter যে style সামলায় তা নিয়ে খুঁতখুঁত করবেন না।
- **যথেষ্ট ভালো হলেই approve করুন** — নিখুঁত হলে নয়; ছোট জিনিসগুলোর জন্য follow-up-এর পরামর্শ দিন।

**ধাপ ৩ — ছোট PR কেন গুরুত্বপূর্ণ।**
50 line-এর PR মন দিয়ে review হয়; 2,000 line-এর PR-এ শুধু "LGTM" সিল পড়ে। ছোট PR বেশি bug ধরে আর দ্রুত merge হয়।

**ধাপ ৪ — সুর-ই সব।**
Review হয় code নিয়ে, মানুষ নিয়ে নয়। প্রশ্ন আর পরামর্শ কাজটাকে সহযোগিতামূলক রাখে; হুকুম আর "আপনি কেন এটা করলেন…" আক্রমণের মতো লাগে।

**Interviewer কেন জিজ্ঞেস করে:** Code review একজন senior-এর দৈনন্দিন দায়িত্ব; তাঁরা আপনার সহযোগিতা আর বুদ্ধি যাচাই করেন।

**সাধারণ ভুল:** বিশাল PR (review করাই যায় না), অথবা এমন review যেখানে formatting নিয়ে খুঁত ধরা হয় কিন্তু আসল design/correctness সমস্যা চোখ এড়িয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা PR কত বড় হওয়া উচিত?"* → এক বসাতেই মন দিয়ে review করা যায় — এতটুকু ছোট; সাধারণত কয়েকশো line বা তার কম।

**সম্পর্কিত:** [Q16 — conventional commits](#q16) · [Q14 (Clean Code) — enforcing](section-16-clean-code-bn.md#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q19"></a>19. Feature branch-এর কাজ চলার মাঝে production-এ hotfix কীভাবে সামলান?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-17-git.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি hotfix branch সরাসরি production branch (বা সর্বশেষ release tag) থেকে কাটি, চলতে থাকা feature কাজ থেকে নয়। ফলে fix-এ শুধু fix-টুকুই থাকে। আমি fix করি, test করি, deploy করি, তারপর সেটা আবার main-এ merge করি যাতে fix হারিয়ে না যায় — বা যেখানে দরকার সেখানে cherry-pick করি। পরে feature branch-গুলো main pull করে fix-টা নিয়ে নেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Production থেকে branch কাটুন, আপনার feature থেকে নয়।**
Production code আপনার অর্ধেক করা feature থেকে আলাদা হতে পারে। যা আসলে live আছে, সেখান থেকেই পরিষ্কারভাবে শুরু করুন।

```bash
git switch main          # অথবা production-এ থাকা release branch/tag
git switch -c hotfix/login-crash
# fix করুন, commit করুন, test করুন
```

**ধাপ ২ — Fix দ্রুত deploy করুন, তারপর সেটা ফিরিয়ে merge করুন।**
Hotfix ship করুন, তারপর নিশ্চিত করুন এটা `main`-এ পৌঁছেছে যাতে পরের release-গুলোতেও থাকে:

```bash
git switch main
git merge hotfix/login-crash   # main-এ এখন fix আছে
git push
```

পুরোনো কোনো release branch-এও দরকার হলে, সেখানে fix commit-টা **cherry-pick** করুন ([Q6](#q6))।

**ধাপ ৩ — Feature branch-গুলো ধরে ফেলে।**
চলতে থাকা feature branch-গুলো তখন `merge main` করে (বা rebase করে) hotfix-টা তুলে নেয়। ফলে তারা bug-টা আবার ফিরিয়ে আনে না।

**ধাপ ৪ — Hotfix আলাদা রাখা কেন দরকার।**
Hotfix হতে হবে ছোট আর কম ঝুঁকির। অসমাপ্ত feature-এর সাথে মেশালে সেটা ঝুঁকির হয় আর deploy করতে দেরি হয় — incident-এর সময়ে ঠিক এটাই আপনি সামলাতে পারবেন না।

**Interviewer কেন জিজ্ঞেস করে:** এটা চাপের মুখে বাস্তব release management যাচাই করে — যা একজন senior-এর দায়িত্ব।

**সাধারণ ভুল:** অসমাপ্ত কাজে ভরা feature branch-এ bug fix করা, ফলে fix-টা একা deploy করা যায় না। অথবা hotfix আবার main-এ merge করতে ভুলে যাওয়া (পরের release-এ bug ফিরে আসে)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Git Flow এটা কীভাবে সামলায়?"* → এতে `main` থেকে কাটা আলাদা `hotfix/` branch থাকে, যা `main` আর `develop` — দুটোতেই merge করা হয়।

**সম্পর্কিত:** [Q6 — cherry-pick](#q6) · [Q15 — branching strategies](#q15)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। আগে table, তারপর এক line-এর মনে করিয়ে দেওয়া কথাগুলো।

## দৈনন্দিন command

| Command | যা করে |
|---|---|
| `git add` / `commit` | stage করা / history-তে জমিয়ে রাখা |
| `git push` / `pull` | upload / download+merge |
| `git switch -c name` | branch তৈরি + switch |
| `git stash` / `stash pop` | পরিবর্তন সরিয়ে রাখা / ফিরিয়ে আনা |

## Undo করার tool

| যা করতে চান... | যা ব্যবহার করবেন |
|---|---|
| শেষ commit undo করা, পরিবর্তন রেখে | `git reset --soft HEAD~1` |
| Push করা commit নিরাপদে undo করা | `git revert <commit>` |
| সব local পরিবর্তন ফেলে দেওয়া | `git reset --hard` (সাবধান) |
| শেষ commit ঠিক করা | `git commit --amend` |

## merge vs rebase vs reset vs revert

| | History রাখে? | Shared branch-এ নিরাপদ? |
|---|---|---|
| merge | হ্যাঁ (merge commit) | হ্যাঁ |
| rebase | না (rewrite করে) | না |
| reset | না (rewrite করে) | না |
| revert | হ্যাঁ (নতুন commit) | হ্যাঁ |

## এক line-এর মনে করিয়ে দেওয়া কথা

- ধারা: edit → `add` → `commit` → `push`। ([Q1](#q1))
- **`pull` = `fetch` + `merge`**; `fetch` নিরাপদ (file বদলায় না)। ([Q3](#q3))
- **merge** history রাখে; **rebase** history সরলরেখা করে কিন্তু rewrite করে — shared commit কখনোই rebase করবেন না। ([Q4](#q4))
- **Conflict** = একই line দুইভাবে বদলানো; resolve করুন, marker মুছুন, `add` করুন, commit করুন। ([Q5](#q5))
- **`reset --hard` কাজ মুছে ফেলে**; `--soft`/`--mixed` কাজ রেখে দেয়। ([Q7](#q7))
- **`revert`** হলো push করা commit-এর নিরাপদ undo (নতুন commit যোগ করে)। ([Q8](#q8))
- **শেষ commit undo করুন, কাজ রেখে** → `git reset --soft HEAD~1`। ([Q9](#q9))
- **`cherry-pick`** একটা commit copy করে (একটা fix backport করা)। ([Q6](#q6))
- **`bisect`** = খারাপ commit খোঁজার binary search। ([Q12](#q12))
- **Detached HEAD** = একটা commit-এ আছেন, branch-এ নয় — কাজ বাঁচাতে `git switch -c`। ([Q13](#q13))
- **GitHub Flow** (branch→PR→merge) বেশিরভাগ team-এর জন্য মানানসই; Git Flow ভারী। ([Q15](#q15))
- **Conventional Commits** (`feat:`, `fix:`) → পড়ার মতো history + automatic versioning। ([Q16](#q16))
- **ছোট PR + ভদ্র, নির্দিষ্ট review** বেশি bug ধরে। ([Q18](#q18))
- **Hotfix** production থেকে কাটুন, main-এ merge করে ফেরান। ([Q19](#q19))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: interviewer কীভাবে আরও গভীরে যান

Interviewer শুধু syntax নয়, বুদ্ধি যাচাই করেন। জোরে বলে অনুশীলন করুন:

1. *"এখানে merge না rebase?"* → local পরিষ্কার করতে rebase; shared branch-এ merge; push করা commit কখনোই rebase নয়।
2. *"আপনি একটা secret commit করে ফেলেছেন — এখন কী?"* → history থেকে সরান আর key rotate করুন; শুধু .gitignore যথেষ্ট নয়।
3. *"Production down আর আপনার feature অর্ধেক শেষ — ঠিক করুন।"* → production থেকে hotfix branch কাটুন, deploy করুন, main-এ merge করে ফেরান।
4. *"কোন commit এটা ভেঙেছে বের করুন।"* → `git bisect` (binary search), `bisect run` দিয়ে automatic করুন।
5. *"আপনার PR 1,500 line — review করতে স্বচ্ছন্দ?"* → না; ছোট, নির্দিষ্ট PR-এ ভাগ করুন।

*প্রতিটা command history-তে কী করে* আর *shared branch-এ কোনটা নিরাপদ* — এটা ব্যাখ্যা করতে পারাই senior signal, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

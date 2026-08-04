# Section 18 — Agile, Scrum ও Methodology

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **Bangladesh (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরোপুরি ব্যাখ্যা করা**, আর **link করা** — যাতে আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারেন। এটা একটা process-এর বিষয় — উদাহরণগুলো বাস্তব scenario, code নয়।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-18-agile-scrum-bn.md](../software-engineer-flutter/section-18-agile-scrum.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমেই বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ সহ ধাপে ধাপে ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সংশ্লিষ্ট প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে আসুন।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর তার কঠিনতা (**Easy / Medium / Hard**)।

> **Interview Tip:** Agile-এর ক্ষেত্রে interviewer-রা *বাস্তব অভিজ্ঞতা* শুনতে চান, বইয়ের সংজ্ঞা নয়। প্রতিটা উত্তরকে "আমাদের team-এ আমরা X করতাম" — এর সাথে জুড়ে দিন। manifesto মুখস্থ বলার চেয়ে এটা অনেক বেশি বিশ্বাসযোগ্য।

---

<a id="toc"></a>

## সূচিপত্র

**A. Agile-এর ভিত্তি**
1. [The Agile Manifesto](#q1) · *Very common*
2. [Waterfall vs Agile](#q2) · *Very common*

**B. Scrum-এর role আর artifact**
3. [Scrum framework (overview)](#q3) · *Very common*
4. [Scrum-এর ৩টি role](#q4) · *Very common*
5. [Scrum artifact](#q5) · *Common*

**C. Sprint আর ceremony**
6. [Sprint কী?](#q6) · *Very common*
7. [Sprint Planning](#q7) · *Common*
8. [Daily Standup](#q8) · *Very common*
9. [Sprint Review vs Retrospective](#q9) · *Common*
10. [Backlog refinement](#q10) · *Common*

**D. Estimation আর tracking**
11. [User story (format, AC, DoD)](#q11) · *Very common*
12. [Story point আর planning poker](#q12) · *Very common*
13. [Velocity](#q13) · *Common*
14. [Burndown chart](#q14) · *Common*

**E. চর্চা আর tool**
15. [Kanban vs Scrum (WIP limit)](#q15) · *Common*
16. [Sprint-এর মাঝে requirement বদলালে কী করবেন](#q16) · *Common*
17. [Sprint team-এ technical debt](#q17) · *Common*
18. [Jira (epic, story, task)](#q18) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---

<a id="study-plan"></a>

## ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

**পর্যায় ১ — ভিত্তি (এখান থেকে শুরু করুন)।**
→ [Q1 Agile Manifesto](#q1) · [Q2 Waterfall vs Agile](#q2) · [Q3 Scrum overview](#q3)

**পর্যায় ২ — Scrum-এর যন্ত্রপাতি।**
→ [Q4 Role](#q4) · [Q5 Artifact](#q5) · [Q6 Sprint](#q6)

**পর্যায় ৩ — Ceremony-গুলো।**
→ [Q7 Planning](#q7) · [Q8 Standup](#q8) · [Q9 Review vs Retro](#q9) · [Q10 Refinement](#q10)

**পর্যায় ৪ — Estimation আর tracking।**
→ [Q11 User story](#q11) · [Q12 Story point](#q12) · [Q13 Velocity](#q13) · [Q14 Burndown](#q14)

**পর্যায় ৫ — বাস্তব চর্চা।**
→ [Q15 Kanban](#q15) · [Q16 Requirement বদলানো](#q16) · [Q17 Tech debt](#q17) · [Q18 Jira](#q18)

**সময় কম?** পড়ুন [Q1](#q1) · [Q2](#q2) · [Q3](#q3) · [Q8](#q8) · [Q11](#q11) · [Q12](#q12), তারপর [Cheat Sheet](#cheatsheet)।

---

# A. Agile-এর ভিত্তি

---

<a id="q1"></a>
## 1. Agile Manifesto কী?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Agile Manifesto (2001) হলো কিছু value-র তালিকা, যা নমনীয় আর customer-কেন্দ্রিক উপায়ে software বানাতে বলে। এর মূল হলো চারটা value statement — যেমন 'individuals and interactions over processes and tools' আর 'responding to change over following a plan'। এটা বলে না যে ডান পাশের জিনিসগুলো মূল্যহীন; এটা বলে বাম পাশেরগুলোর গুরুত্ব বেশি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের একটা ছবি: স্বাদ দেখে রান্না।**
কড়া recipe (Waterfall) হুবহু মেনে চলা হয়, খাবারের স্বাদ খারাপ হলেও। Agile মানে রান্নার সময় স্বাদ দেখে ঠিক করে নেওয়া — আপনি চোখ বন্ধ করে plan মানেন না, feedback অনুযায়ী বদলান।

**ধাপ ২ — ৪টি value (প্রতিটাই "X over Y")।**

| আমরা মূল্য দিই... | ...-এর চেয়ে বেশি |
|---|---|
| Individuals and interactions | processes and tools |
| Working software | comprehensive documentation |
| Customer collaboration | contract negotiation |
| Responding to change | following a plan |

মূল বাক্যটা: "while there is value in the items on the right, we value the items on the left more."

**ধাপ ৩ — ১২টি principle (সারকথা)।**
এগুলো value-গুলোকে বিস্তারিত করে: ঘন ঘন working software deliver করা, requirement বদলানোকে স্বাগত জানানো, business-এর সাথে ঘনিষ্ঠভাবে কাজ করা, উৎসাহী মানুষদের ঘিরে দল গড়া, নিয়মিত নিজেদের কাজ পর্যালোচনা করে উন্নত হওয়া, আর টেকসই গতিতে কাজ করা।

**ধাপ ৪ — Agile যা নয়।**
Agile মানে "plan নেই" বা "documentation নেই" — এমন নয়। এর মানে *শুরুতে কম কড়াকড়ি* আর *বেশি ঘন ঘন feedback ও সমন্বয়*।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখেন আপনি Agile-এর *মূল ভাব* (feedback আর নমনীয়তা) বোঝেন কি না, শুধু buzzword নয়।

**সাধারণ ভুল:** বলা যে Agile মানে "documentation নেই" বা "plan নেই"। এর মানে হলো working software আর মানিয়ে নেওয়ার ক্ষমতাকে *বেশি* মূল্য দেওয়া, বাকিগুলো ছুঁড়ে ফেলা নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Agile vs Scrum?"* → Agile হলো mindset (value); Scrum হলো একটা নির্দিষ্ট framework যা সেটা বাস্তবায়ন করে ([Q3](#q3))।

**সম্পর্কিত:** [Q2 — Waterfall vs Agile](#q2) · [Q3 — Scrum](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q2"></a>
## 2. Waterfall আর Agile-এর পার্থক্য কী? কোনটা কখন উপযুক্ত?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Waterfall ধারাবাহিক — আগে সব requirement শেষ, তারপর design, তারপর build, তারপর test — নির্দিষ্ট ধাপে ধাপে। Agile পুনরাবৃত্তিমূলক — আপনি ছোট ছোট cycle-এ বানান আর release করেন, আর সবসময় feedback পান। যেসব project-এ requirement নির্দিষ্ট ও ভালোভাবে জানা (যেমন regulated বা hardware project), সেখানে Waterfall মানানসই; আর যেখানে requirement বদলায়, সেখানে Agile মানানসই — যা বেশিরভাগ software-এর ক্ষেত্রেই সত্যি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Waterfall — একটা বড় ধারাবাহিক লাইন।**

```
Requirements → Design → Build → Test → Release
   (each phase finishes before the next starts; change is expensive)
```

**ধাপ ২ — Agile — ছোট ছোট পুনরাবৃত্ত cycle।**

```
[plan → build → test → release → feedback] → repeat every 1–4 weeks
   (you adjust each cycle based on real feedback)
```

**ধাপ ৩ — Trade-off গুলো।**

| | Waterfall | Agile |
|---|---|---|
| Requirement | শুরুতেই নির্দিষ্ট | সময়ের সাথে বদলায় |
| Feedback | দেরিতে (release-এর পরে) | ক্রমাগত |
| পরিবর্তন | ব্যয়বহুল, নিরুৎসাহিত | প্রত্যাশিত, স্বাগত |
| ঝুঁকি | দেরিতে ধরা পড়ে | আগে ধরা পড়ে |

**ধাপ ৪ — কোনটা কখন ব্যবহার করবেন।**
- **Waterfall** — requirement নির্দিষ্ট ও পরিষ্কার, আর পরিবর্তন ব্যয়বহুল (medical device, construction, fixed-scope contract)।
- **Agile** — requirement বদলাবে আর আপনি আগেভাগে feedback চান (বেশিরভাগ app আর product)।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখেন আপনি project অনুযায়ী process বেছে নিতে পারেন কি না, নাকি গোঁড়ামি করে একটাই চাপিয়ে দেন।

**সাধারণ ভুল:** দাবি করা যে Agile সবসময় ভালো। সত্যিই fixed-scope আর safety-critical project-এ Waterfall-এর শুরুর কড়া নিয়মই সঠিক পছন্দ হতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"দুটো কি মেশানো যায়?"* → হ্যাঁ — "hybrid" পদ্ধতিতে নির্দিষ্ট অংশের জন্য শুরুতেই planning হয়, আর বদলাতে থাকা অংশের জন্য Agile cycle চলে।

**সম্পর্কিত:** [Q1 — Agile Manifesto](#q1) · [Q19 (SDLC) — model](section-19-sdlc-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

# B. Scrum-এর role আর artifact

---

<a id="q3"></a>
## 3. Scrum framework ব্যাখ্যা করুন (overview)।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Scrum হলো সবচেয়ে জনপ্রিয় Agile framework। কাজ হয় নির্দিষ্ট দৈর্ঘ্যের Sprint-এ (সাধারণত 1–4 সপ্তাহ)। এতে তিনটা role আছে (Product Owner, Scrum Master, Developers), তিনটা artifact আছে (Product Backlog, Sprint Backlog, Increment), আর কিছু event আছে (Sprint Planning, Daily Standup, Sprint Review, Retrospective)। লক্ষ্য হলো প্রতি Sprint-এ একটা working increment deliver করা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বড় ছবিটা।**

```
Product Backlog → [Sprint Planning] → Sprint Backlog
   → daily work + [Daily Standup] (1–4 weeks)
   → working Increment → [Sprint Review] + [Retrospective] → repeat
```

**ধাপ ২ — তিনটা অংশ।**
- **Role** — Product Owner ("কী" ঠিক করেন), Scrum Master (process-এর coach), Developers ("কীভাবে" ঠিক করেন)। দেখুন [Q4](#q4)।
- **Artifact** — Product Backlog, Sprint Backlog, Increment। দেখুন [Q5](#q5)।
- **Event** — Planning, Daily Standup, Review, Retrospective (আর Sprint নিজেও)। দেখুন [Q7](#q7)–[Q9](#q9)।

**ধাপ ৩ — ছন্দটা।**
প্রতিটা Sprint একটা পূর্ণ mini-cycle: plan করুন, বানান, দেখান (Review), কাজের ধরন উন্নত করুন (Retrospective), আবার শুরু করুন। প্রতিটা Sprint শেষ হওয়া উচিত এমন কিছু দিয়ে যা ship করা সম্ভব।

**Interviewer কেন জিজ্ঞেস করে:** এটা Scrum-এর মৌলিক প্রশ্ন; তাঁরা নিশ্চিত হতে চান আপনি জানেন role, artifact আর event কীভাবে একসাথে কাজ করে।

**সাধারণ ভুল:** Scrum Master-কে "boss" বা "project manager" বলা। Scrum Master একজন facilitator/coach, manager নন ([Q4](#q4))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা Sprint কতদিনের?"* → সাধারণত 1–4 সপ্তাহ, সবচেয়ে বেশি চলে 2 সপ্তাহ ([Q6](#q6))।

**সম্পর্কিত:** [Q4 — role](#q4) · [Q5 — artifact](#q5) · [Q6 — sprint](#q6)

[↑ উপরে ফিরুন](#toc)

---

<a id="q4"></a>
## 4. Scrum-এর তিনটি role কী কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"তিনটি role আছে: Product Owner-এর হাতে থাকে 'কী' — backlog আর priority, তিনি customer-এর প্রতিনিধি। Scrum Master-এর হাতে থাকে 'আমরা কীভাবে কাজ করি' — team-কে coach করা আর বাধা সরানো, মানুষকে হুকুম দেওয়া নয়। Developer-দের হাতে থাকে 'কীভাবে' — তাঁরা increment বানান আর ঠিক করেন কতটুকু কাজ নিতে পারবেন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Product Owner (PO) — customer-এর কণ্ঠস্বর।**
- **Product Backlog**-এর মালিক, আর তিনিই priority ঠিক করেন।
- *কী* বানানো হবে আর কোন order-এ হবে, সেটা তিনি ঠিক করেন (সবচেয়ে বেশি value আনার জন্য)।
- Scope-এ হ্যাঁ/না বলেন; priority-র ব্যাপারে একমাত্র সিদ্ধান্তদাতা।

**ধাপ ২ — Scrum Master (SM) — coach।**
- Event-গুলো চালান আর team-এর process রক্ষা করেন।
- **Blocker সরান** (impediment), যাতে developer-রা কাজ করতে পারেন।
- Team-কে Scrum শেখান; team-কে সেবা দেন, task assign করেন **না**, মানুষ manage করেন না।

**ধাপ ৩ — Developer-রা — যাঁরা বানান।**
- আসল কাজটা করেন (design, code, test)।
- **Self-organizing**: কাজটা কীভাবে হবে আর প্রতি Sprint-এ কতটুকু নেবেন, তাঁরাই ঠিক করেন।
- Cross-functional: সবাই মিলে deliver করার জন্য দরকারি সব skill তাঁদের আছে।

**ধাপ ৪ — স্পষ্ট সীমারেখা।**
PO = *কী* আর *কেন*। Developer-রা = *কীভাবে* আর *কতটুকু*। SM = *process কাজ করতে সাহায্য করেন*। এগুলো মিশিয়ে ফেললে (যেমন SM task ঠিক করে দিচ্ছেন, বা PO team-কে ছাড়াই client-কে date-এর কথা দিচ্ছেন) Scrum ভেঙে যায়।

**Interviewer কেন জিজ্ঞেস করে:** Role গুলিয়ে ফেলা (বিশেষ করে SM-কে manager ভাবা) সবচেয়ে সাধারণ Scrum ভুল; তাঁরা দেখেন আপনি সীমারেখাটা বোঝেন কি না।

**সাধারণ ভুল:** Scrum Master-কে সাধারণ project manager মনে করা, যিনি কাজ ভাগ করে দেন। SM সাহায্য করেন আর blocker সরান; team নিজে নিজেকে সংগঠিত করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Sprint scope কে ঠিক করে?"* → PO priority-র order ঠিক করেন; **Developer-রা** ঠিক করেন কতটুকু নিতে পারবেন।

**সম্পর্কিত:** [Q3 — Scrum overview](#q3) · [Q5 — artifacts](#q5)

[↑ উপরে ফিরুন](#toc)

---

<a id="q5"></a>
## 5. Scrum artifact গুলো কী কী?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"তিনটি আছে: Product Backlog হলো product-এর যা যা লাগতে পারে তার পূর্ণ, priority অনুযায়ী সাজানো তালিকা। Sprint Backlog হলো তার একটা অংশ, যেটা team চলতি Sprint-এর জন্য নেয়, সাথে সেটা করার পরিকল্পনা। Increment হলো Sprint শেষে পাওয়া কাজ করা, ship করার মতো ফলাফল।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Product Backlog — প্রধান to-do তালিকা।**
- এর মালিক Product Owner।
- যা যা বানানো *হতে পারে* সবকিছু, priority/value অনুযায়ী সাজানো।
- এটা জীবন্ত — item যোগ হয়, বাদ যায়, আর order বদলায় সবসময়।

**ধাপ ২ — Sprint Backlog — এই Sprint-এর পরিকল্পনা।**
- Product Backlog থেকে *এই* Sprint-এর জন্য নেওয়া item গুলো, সাথে Sprint Goal।
- এর মালিক Developer-রা; তাঁরাই ঠিক করেন কতটুকু বাস্তবসম্মত।
- Sprint-এর মাঝে খুব একটা বদলায় না (goal সুরক্ষিত থাকে — দেখুন [Q16](#q16))।

**ধাপ ৩ — Increment — কাজ করা ফলাফল।**
- এই Sprint-এ শেষ হওয়া সব কাজের যোগফল, যা **Definition of Done** ([Q11](#q11)) মেনে চলে।
- অবশ্যই *ship করার মতো* হতে হবে — সত্যিই কাজ করে এমন, অর্ধেক করা নয়।

**ধাপ ৪ — প্রবাহটা।**

```
Product Backlog (everything) → Sprint Backlog (this sprint) → Increment (done & working)
```

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি বোঝেন কি না team কীসের দায়িত্ব নেয়, আর প্রতি Sprint-এ "done" মানে কী।

**সাধারণ ভুল:** Product Backlog (সবকিছু, PO-র মালিকানায়) আর Sprint Backlog (এই Sprint, team-এর মালিকানায়) গুলিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কোনটার মালিক কে?"* → Product Backlog = PO; Sprint Backlog = Developer-রা।

**সম্পর্কিত:** [Q4 — roles](#q4) · [Q10 — refinement](#q10) · [Q11 — Definition of Done](#q11)

[↑ উপরে ফিরুন](#toc)

---

# C. Sprint ও ceremony

---

<a id="q6"></a>
## 6. Sprint কী, কতদিনের হয়, আর goal পূরণ না হলে কী হয়?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Sprint হলো একটা নির্দিষ্ট time-box, সাধারণত ২ সপ্তাহ, যার মধ্যে team একটা Sprint Goal-এর দিকে কাজ করা increment বানায়। দৈর্ঘ্যটা নির্দিষ্ট, বাড়ানো হয় না। Goal পূরণ না হলে Sprint বাড়ানো হয় না — অসমাপ্ত কাজ backlog-এ ফিরে যায় আর নতুন করে plan করা হয়, আর Retrospective-এ কারণটা দেখা হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা নির্দিষ্ট time-box।**
Sprint-এর একটা নির্দিষ্ট দৈর্ঘ্য থাকে (সাধারণত ২ সপ্তাহ; ১–৪ স্বাভাবিক)। দৈর্ঘ্যটা এক রকম থাকে, যাতে team-এর একটা স্থির ছন্দ আর অনুমানযোগ্য velocity তৈরি হয়।

**ধাপ ২ — মূল নিয়ম।**
- এমন কোনো পরিবর্তন নয় যা **Sprint Goal**-কে বিপদে ফেলে।
- Scope আরও স্পষ্ট করা যায়, কিন্তু goal সুরক্ষিত থাকে।
- নির্ধারিত তারিখেই শেষ হয় — কখনোই বাড়ানো হয় না।

**ধাপ ৩ — Goal পূরণ না হলে কী?**
- Sprint তবুও **সময়মতো শেষ হয়** — এটা বাড়ানো হয় না।
- অসমাপ্ত item **Product Backlog-এ ফিরে যায়**, নতুন করে estimate আর priority করার জন্য।
- **Retrospective** ([Q9](#q9)) দেখে *কেন* হলো (বেশি কাজ নেওয়া? blocker? অস্পষ্ট story?) আর team নিজেকে ঠিক করে নেয়।

**ধাপ ৪ — নির্দিষ্ট দৈর্ঘ্য কেন গুরুত্বপূর্ণ।**
এক রকম Sprint দৈর্ঘ্য velocity-কে অর্থবহ করে ([Q13](#q13)) আর একটা নির্ভরযোগ্য delivery ছন্দ তৈরি করে। Sprint বাড়ালে সমস্যা সামনে না এসে লুকিয়ে যায়।

**Interviewer কেন জিজ্ঞেস করে:** এটা Scrum-এর মূল শৃঙ্খলা যাচাই করে — নির্দিষ্ট time-box আর অসমাপ্ত কাজ সৎভাবে সামলানো।

**সাধারণ ভুল:** বলা যে "শেষ করার জন্য আমরা Sprint কয়েক দিন বাড়াই।" এতে time-box ভেঙে যায়; বদলে নতুন করে plan করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Sprint কি বাতিল করা যায়?"* → শুধু PO পারেন, আর তখনই যখন Sprint Goal অপ্রয়োজনীয় হয়ে যায় — এটা বিরল।

**সম্পর্কিত:** [Q3 — Scrum overview](#q3) · [Q13 — velocity](#q13) · [Q16 — changing requirements](#q16)

[↑ উপরে ফিরুন](#toc)

---

<a id="q7"></a>
## 7. Sprint Planning-এ কী হয়?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Sprint Planning দিয়ে Sprint শুরু হয়। পুরো team একটা Sprint Goal-এ একমত হয়, Product Owner সবচেয়ে বেশি priority-র backlog item গুলো তুলে ধরেন, আর Developer-রা তাঁদের velocity দেখে যতটুকু বাস্তবে শেষ করতে পারবেন ততটুকু নেন। ফলাফল হলো Sprint Backlog আর একটা যৌথ পরিকল্পনা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা যে দুটো প্রশ্নের উত্তর দেয়।**
1. এই Sprint-এ আমরা **কী** deliver করতে পারি? (Sprint Goal + বেছে নেওয়া item)
2. আমরা এটা **কীভাবে** করব? (item গুলোকে task-এ ভাগ করা)

**ধাপ ২ — কে কী করেন।**
- **PO** — সবচেয়ে বেশি priority-র, refine করা item গুলো তুলে ধরেন আর স্পষ্ট করেন।
- **Developer-রা** — estimate করেন, কতটুকু নিতে পারবেন ঠিক করেন, আর item গুলোকে task-এ ভাগ করেন।
- **SM** — meeting চালান আর সময়ের ভেতরে রাখেন।

**ধাপ ৩ — বাস্তবসম্মত থাকতে velocity ব্যবহার করুন।**
Team তার গড় velocity ([Q13](#q13)) দেখে, যাতে বেশি কাজ না নিয়ে ফেলে। গড় ২৫ হলে ৪০ point নেওয়া মানে Sprint-কে ব্যর্থ হওয়ার পথে ঠেলে দেওয়া।

**ধাপ ৪ — ফলাফল।**
একটা স্পষ্ট **Sprint Goal** আর একটা **Sprint Backlog**, যেটা সবাই মানেন যে করা সম্ভব।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি বাস্তবসম্মতভাবে plan করেন কি না, আর scope কে ঠিক করে সেটা বোঝেন কি না (team, PO-র priority অনুযায়ী)।

**সাধারণ ভুল:** PO বা কোনো manager team-এর velocity-র চেয়ে বেশি কাজ *চাপিয়ে* দেন। কতটুকু নেওয়া হবে সেটা team-এর সিদ্ধান্ত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Planning কতক্ষণ চলে?"* → Time-box করা, Sprint-এর প্রতি সপ্তাহে মোটামুটি ২ ঘণ্টা (তাই ২ সপ্তাহের Sprint-এ ~৪ ঘণ্টা)।

**সম্পর্কিত:** [Q6 — sprint](#q6) · [Q12 — story points](#q12) · [Q13 — velocity](#q13)

[↑ উপরে ফিরুন](#toc)

---

<a id="q8"></a>
## 8. Daily Standup কী, আর সেখানে আপনি কী বলেন?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Daily Standup (Daily Scrum) হলো ১৫ মিনিটের একটা ছোট meeting, যেখানে team Sprint Goal-এর দিকে অগ্রগতি নিয়ে sync করে। চিরাচরিতভাবে প্রত্যেকে তিনটা জিনিস বলেন: গতকাল কী করেছি, আজ কী করব, আর কোনো blocker আছে কি না। এটা সমন্বয়ের জন্য, manager-কে status report দেওয়ার জন্য নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটা প্রশ্ন।**
1. গতকাল আমি কী করেছি (goal-এর দিকে)?
2. আজ আমি কী করব?
3. আমাকে কী আটকে রেখেছে?

**ধাপ ২ — ছোট আর নির্দিষ্ট রাখুন।**
- **১৫ মিনিট**-এ time-box করা।
- এটা *developer*-দের মধ্যে sync, boss-কে দেওয়া report নয়।
- বিস্তারিত আলোচনা standup-এর পরে "offline"-এ নেওয়া হয়, শুধু সংশ্লিষ্ট মানুষদের নিয়ে।

**ধাপ ৩ — যে সাধারণ anti-pattern গুলো এড়াবেন।**
- এটাকে Scrum Master বা manager-এর *কাছে* status report বানিয়ে ফেলা।
- Meeting-এ দীর্ঘ সমস্যা সমাধান করা (offline-এ নিন)।
- মানুষ goal-এর দিকে না শুনে শুধু নিজের পালার জন্য অপেক্ষা করা।

**ধাপ ৪ — আসল উদ্দেশ্য।**
এটা blocker আগেভাগে সামনে আনে আর সবাইকে Sprint Goal-এ এক রাখে। Format-এর চেয়ে ফলাফল বেশি গুরুত্বপূর্ণ: একটা সমন্বিত team, যার blocker সবার চোখে পড়ে।

**Interviewer কেন জিজ্ঞেস করে:** Standup প্রতিদিনের ব্যাপার; তাঁরা দেখেন আপনি এটাকে team সমন্বয় হিসেবে নেন, না কি micro-management-এর status meeting হিসেবে।

**সাধারণ ভুল:** এটাকে *manager-এর জন্য* status meeting মনে করা, বা গভীর technical তর্কে meeting লম্বা হতে দেওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Remote standup-এর tip?"* → সময়মতো রাখুন, camera চালু রাখুন, আর time zone না মিললে লেখা update async-এ post করুন।

**সম্পর্কিত:** [Q3 — Scrum overview](#q3) · [Q14 — burndown](#q14)

[↑ উপরে ফিরুন](#toc)

---

<a id="q9"></a>
## 9. Sprint Review আর Sprint Retrospective-এর মধ্যে পার্থক্য কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Sprint Review হলো *product* নিয়ে — team stakeholder-দের কাছে working increment demo করে, আর পরে কী বানাতে হবে তার feedback নেয়। Retrospective হলো *process* নিয়ে — team নিজেদের মধ্যে ভাবে তারা কীভাবে কাজ করেছে, আর কিছু উন্নতি বেছে নেয়। Review = কী; Retrospective = কীভাবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Sprint Review — কাজ দেখান, feedback নিন।**
- Sprint-এর শেষে হয়।
- Team PO আর stakeholder-দের কাছে **increment demo করে**।
- লক্ষ্য: feedback নেওয়া আর Product Backlog ঠিক করা। এটা *product* নিয়ে।

**ধাপ ২ — Sprint Retrospective — আমরা কীভাবে কাজ করি তা উন্নত করা।**
- Review-এর পরে হয়, **শুধু team** (একটা নিরাপদ জায়গা)।
- Team ভেবে দেখে: কী ভালো হয়েছে, কী হয়নি, কী উন্নত করা দরকার।
- লক্ষ্য: পরের Sprint-এর জন্য ১–২টা নির্দিষ্ট উন্নতি বেছে নেওয়া। এটা *process* নিয়ে।

**ধাপ ৩ — মনে রাখার সহজ উপায়।**

| | Sprint Review | Retrospective |
|---|---|---|
| মূল বিষয় | product (আমরা যা বানিয়েছি) | process (আমরা যেভাবে কাজ করেছি) |
| কারা থাকেন | team + stakeholders | শুধু team |
| ফলাফল | feedback, backlog update | process-এর উন্নতি |

**ধাপ ৪ — Retro কেন গোপন।**
সৎভাবে ভাবতে হলে psychological safety লাগে। Stakeholder সামনে থাকলে মানুষ সমস্যা লুকিয়ে ফেলেন। শুধু team থাকলে কথা খোলাখুলি থাকে।

**Interviewer কেন জিজ্ঞেস করে:** মানুষ প্রায়ই দুটো গুলিয়ে ফেলেন; product/process-এর ভাগটা ব্যাখ্যা করলে আসল Scrum বোঝা যায়।

**সাধারণ ভুল:** দুটো মিশিয়ে ফেলা — Retro-তে demo করা, বা stakeholder-দের সামনে process-এর উন্নতি নিয়ে কথা বলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আপনি কোন retro format ব্যবহার করেছেন?"* → "Start / Stop / Continue", বা "কী ভালো হয়েছে / কী হয়নি / action।"

**সম্পর্কিত:** [Q8 — standup](#q8) · [Q17 — tech debt](#q17)

[↑ উপরে ফিরুন](#toc)

---

<a id="q10"></a>
## 10. Backlog Refinement (grooming) কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Backlog refinement হলো একটা চলমান কাজ — ভবিষ্যতের Sprint-এর জন্য backlog item গুলোকে তৈরি করা। মানে item পরিষ্কার করা, বড় গুলো ভাগ করা, acceptance criteria যোগ করা, আর estimate করা। PO আর Developer-রা একসাথে এটা করেন, সাধারণত সপ্তাহে অল্প কিছু সময়। ফলে Sprint Planning দ্রুত হয় আর item গুলো 'ready' থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — লক্ষ্য: একটা 'ready' backlog।**
Refinement backlog-এর উপরের অংশটা পরিষ্কার, যথেষ্ট ছোট আর estimate করা রাখে। ফলে Planning-এর সময় team লম্বা আলোচনা ছাড়াই item তুলে নিতে পারে।

**ধাপ ২ — এর ভেতরে কী হয়।**
- অস্পষ্ট item **পরিষ্কার করা** (PO প্রশ্নের উত্তর দেন)।
- বড় item (epic/বড় story) ছোট ছোট ভাগে **ভাগ করা**।
- **Acceptance criteria যোগ করা** ("done" মানে কী)।
- Story point দিয়ে **estimate করা** ([Q12](#q12))।

**ধাপ ৩ — কে করে আর কত ঘনঘন।**
- **PO** আর **Developer-রা** একসাথে (SM সাহায্য করেন)।
- চলমান — প্রায়ই সপ্তাহে ~১টা ছোট session, team-এর সময়ের প্রায় 10%-এর মধ্যে রাখা হয়।

**ধাপ ৪ — Definition of Ready।**
একটা "ready" item পরিষ্কার, ছোট, estimate করা, আর তার acceptance criteria আছে। তাই এটা নিরাপদে Sprint-এ টেনে নেওয়া যায়। Refinement এই ready item গুলোই বানায়।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি backlog-কে সুস্থ রাখেন কি না। এতেই Sprint অনুমান করা যায়।

**সাধারণ ভুল:** Refinement বাদ দেওয়া। ফলে Sprint Planning একটা লম্বা, এলোমেলো meeting হয়ে যায়, যেখানে item গুলো আধা-বোঝা থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Definition of Ready vs Done?"* → Ready = item শুরু করার মতো যথেষ্ট ভালো; Done = কাজ শেষ আর ship করার মতো ([Q11](#q11))।

**সম্পর্কিত:** [Q5 — backlog](#q5) · [Q11 — acceptance criteria](#q11) · [Q12 — estimation](#q12)

[↑ উপরে ফিরুন](#toc)

---

# D. Estimation ও tracking

---

<a id="q11"></a>
## 11. User story কী? Format, acceptance criteria আর Definition of Done ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"User story একটা feature-কে user-এর চোখে বর্ণনা করে, এই format-এ — 'As a [user], I want [goal], so that [benefit].' Acceptance criteria হলো নির্দিষ্ট শর্ত, যেগুলো পূরণ হলে এটা সঠিক। Definition of Done হলো পুরো team-এর checklist (tested, reviewed, documented), যেটা *প্রতিটা* story-র উপর খাটে, complete গোনার আগে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — User story-র format।**

```
As a [type of user], I want [some goal], so that [some benefit].

Example:
As a shopper, I want to save items to a wishlist,
so that I can buy them later.
```

এটা *কে* আর *কেন*-এর উপর জোর দেয়, technical *কীভাবে*-এর উপর নয়।

**ধাপ ২ — Acceptance Criteria (AC) — এই story কখন সঠিক?**
এই একটা story-র জন্য নির্দিষ্ট, testable শর্ত। একটা সাধারণ format হলো Given/When/Then:

```
Given I am logged in,
When I tap the heart icon on a product,
Then the product appears in my wishlist.
```

**ধাপ ৩ — Definition of Done (DoD) — প্রতিটা story-র উপর খাটে।**
Team মিলে ঠিক করা একটা যৌথ checklist, যেমন:
- Code লেখা আর peer-review করা হয়েছে।
- Test লেখা হয়েছে আর pass করছে।
- Acceptance criteria পূরণ করে।
- Merge করা আর deploy করার মতো।

**ধাপ ৪ — AC vs DoD (মূল পার্থক্য)।**
- **Acceptance Criteria** = *একটা* story-র জন্য নির্দিষ্ট (এই feature কীসে সঠিক হয়)।
- **Definition of Done** = সবার জন্য, *সব* story-তে খাটে (মানের সীমা)।

**Interviewer কেন জিজ্ঞেস করে:** Story, AC আর DoD হলো Agile team-এর দৈনন্দিন ভাষা; তাঁরা দেখেন আপনি পরিষ্কার আর testable work item লেখেন কি না।

**সাধারণ ভুল:** AC (প্রতি story) আর DoD (পুরো team) গুলিয়ে ফেলা। অথবা এমন story লেখা যা user value-র বদলে technical task বর্ণনা করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ভালো story-র বৈশিষ্ট্য কী?"* → INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable।

**সম্পর্কিত:** [Q10 — refinement](#q10) · [Q12 — story points](#q12) · [Q5 — increment ও DoD](#q5)

[↑ উপরে ফিরুন](#toc)

---

<a id="q12"></a>
## 12. Story point কী, ঘণ্টার বদলে কেন এটা ব্যবহার করা হয়, আর planning poker কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Story point কাজের *আপেক্ষিক আকার* estimate করে — এর effort, জটিলতা আর অনিশ্চয়তা — সঠিক ঘণ্টার বদলে। Team এটা পছন্দ করে কারণ মানুষ ঘণ্টা estimate করতে খারাপ, কিন্তু আকার তুলনা করতে মোটামুটি ভালো। আর point নিজেকে নিখুঁত প্রতিশ্রুতি বলে দাবি করে না। Planning poker হলো সেই পদ্ধতি, যেখানে team একসাথে estimate করে আর ভিন্ন ভিন্ন মত সামনে আসে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Point হলো আপেক্ষিক আকার, সময় নয়।**
T-shirt size (S, M, L) বা Fibonacci scale (1, 2, 3, 5, 8, 13)-এর মতো। ২ point-এর একটা story ১ point-এর story-র "প্রায় দ্বিগুণ আকার" — "২ ঘণ্টা" নয়।

**ধাপ ২ — ঘণ্টার বদলে point কেন।**
- মানুষ পরম ঘণ্টার চেয়ে *আপেক্ষিক* আকার ভালো estimate করে।
- Point-এ effort + জটিলতা + অনিশ্চয়তা সবই ধরা পড়ে, শুধু টাইপ করার সময় নয়।
- ঘণ্টা শুনতে নিখুঁত প্রতিশ্রুতির মতো লাগে (আর ভুল হলে দোষারোপ শুরু হয়); point অনিশ্চয়তা নিয়ে সৎ থাকে।
- Team-এর velocity ([Q13](#q13)) সময়ের সাথে point-কে অনুমানযোগ্য planning-এ বদলে দেয়।

**ধাপ ৩ — Planning Poker।**
1. PO একটা story পড়ে শোনান।
2. প্রতিটা developer গোপনে একটা card বেছে নেন (1, 2, 3, 5, 8...)।
3. সবাই একসাথে card দেখান।
4. Estimate অনেক আলাদা হলে সবচেয়ে বেশি আর সবচেয়ে কম যাঁরা দিয়েছেন তাঁরা কারণ বলেন, তারপর আবার vote হয়।

আলোচনাটাই আসল লাভ — এতে লুকানো জটিলতা বেরিয়ে আসে আর সবার বোঝা এক হয়।

**ধাপ ৪ — আগে লুকিয়ে, পরে দেখানো কেন।**
আগে গোপনে vote করলে সবচেয়ে জোরে কথা বলা বা সবচেয়ে senior মানুষটি সবাইকে প্রভাবিত করতে পারেন না। পার্থক্য থেকেই দরকারি আলোচনা শুরু হয়।

**Interviewer কেন জিজ্ঞেস করে:** Estimation সবসময়ই একটা কষ্টের জায়গা; তাঁরা দেখেন আপনি আপেক্ষিক estimation আর team-ভিত্তিক estimate করা বোঝেন কি না।

**সাধারণ ভুল:** Point-কে সরাসরি ঘণ্টায় বদলে ফেলা ("১ point = ৪ ঘণ্টা")। এতে পুরো সুবিধাটাই নষ্ট হয় আর ভুয়া নিখুঁততা ফিরে আসে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Fibonacci সংখ্যা কেন?"* → ফাঁকগুলো বড় হতে থাকে, কারণ বড় item অনেক বেশি অনিশ্চিত — "21 vs 22" বলার কোনো মানে হয় না।

**সম্পর্কিত:** [Q11 — user stories](#q11) · [Q13 — velocity](#q13) · [Q7 — planning](#q7)

[↑ উপরে ফিরুন](#toc)

---

<a id="q13"></a>
## 13. Sprint velocity কী, আর planning-এ এটা কীভাবে ব্যবহার হয়?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Velocity হলো একটা team প্রতি Sprint-এ গড়ে কত story point শেষ করে তার হিসাব। এটা দিয়ে বাস্তবসম্মত planning করা হয় — team-এর গড় ২৫ point হলে তারা ৪০ point-এর কথা দেবে না। এটা team-এর জন্য একটা planning tool, team তুলনা করার বা মানুষের উপর চাপ দেওয়ার productivity score নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কীভাবে মাপা হয়।**
প্রতি Sprint-এ *শেষ হওয়া* সব story-র point যোগ করুন। শেষ কয়েকটা Sprint-এর গড় নিলেই velocity পাওয়া যায়।

```
Sprint 1: 22 done   Sprint 2: 26 done   Sprint 3: 24 done
Velocity ≈ 24 points per sprint
```

**ধাপ ২ — কীভাবে ব্যবহার হয়।**
Planning-এ team মোটামুটি তার velocity-র সমান কাজ তুলে নেয় — এর বেশি নয়। কয়েকটা Sprint পরে velocity দিয়ে আন্দাজও করা যায়, N point-এর একটা backlog কখন শেষ হবে।

**ধাপ ৩ — গুরুত্বপূর্ণ সতর্কতা।**
- Velocity **প্রতিটা team-এর নিজস্ব** — কখনোই দুই team-এর velocity তুলনা করবেন না (তাঁদের point-এর মানে আলাদা)।
- এটা একটা **planning-এর সাহায্য**, target নয়। "আরও বেশি velocity" চাপ দিলে team estimate ফুলিয়ে দেয়, আর এতে এর মূল্যই নষ্ট হয়।
- একটা স্থির team নিয়ে কয়েকটা Sprint যাওয়ার পরেই এটা থিতু হয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা বাস্তবসম্মত planning যাচাই করে, আর দেখে আপনি velocity-কে performance metric হিসেবে ভুলভাবে ব্যবহার করবেন কি না (একটা পরিচিত anti-pattern)।

**সাধারণ ভুল:** Velocity দিয়ে team তুলনা করা, বা team-এর উপর চাপ দিতে KPI হিসেবে ব্যবহার করা — দুটোই estimate আর metric দুটোকেই নষ্ট করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কোন কারণে velocity অন্যায্যভাবে কমে যায়?"* → ছুটি, team-এ পরিবর্তন, অনেক unplanned bug-এর কাজ — প্রসঙ্গটা গুরুত্বপূর্ণ।

**সম্পর্কিত:** [Q12 — story points](#q12) · [Q7 — planning](#q7) · [Q14 — burndown](#q14)

[↑ উপরে ফিরুন](#toc)

---

<a id="q14"></a>
## 14. Burndown chart কী?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Burndown chart দেখায় সময়ের সাথে কত কাজ বাকি আছে — Sprint এগোনোর সাথে বাকি কাজ 'burn down' হয়ে শূন্যের দিকে নামে। এটা দ্রুত একটা চিত্র দেয় যে team Sprint শেষ করার পথে আছে কি না। আর সমস্যা আগেভাগে ধরতে সাহায্য করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কী দেখায়।**
- X-axis: Sprint-এর দিনগুলো।
- Y-axis: বাকি কাজ (story point বা task)।
- একটা line, যেটা শেষ দিনে নেমে শূন্যে পৌঁছানোর কথা।

```
points
 25 | \
 20 |  \___        actual line above the ideal = behind schedule
 15 |      \  .    (the dotted line is the "ideal" steady burn)
 10 |       \ .
  5 |        \.
  0 |_________\_____ days
    1  2  3  4  5
```

**ধাপ ২ — কীভাবে পড়বেন।**
- ideal line-এর **উপরে** → schedule-এর পিছনে (কাজ যথেষ্ট দ্রুত শেষ হচ্ছে না)।
- **নিচে** → এগিয়ে আছেন।
- **সমতল** line → কাজ আটকে আছে (কোনো blocker, বা কিছুই শেষ হচ্ছে না)।

**ধাপ ৩ — এটা কেন কাজে লাগে।**
এটা সমস্যাটা আগেভাগে সামনে আনে — সমতল বা উপরে ওঠা line team-কে বলে এখনই খোঁজ নিতে, শেষ দিনে নয়। এটা standup-এ কথা শুরু করার একটা উপায়, বিচার করার হাতিয়ার নয়।

**ধাপ ৪ — Burndown বনাম burnup।**
**Burnup** chart দেখায় *শেষ হওয়া* কাজ মোটের দিকে উঠছে। এটা scope-এর পরিবর্তনও দেখাতে পারে (মোট line-টা সরে যায়) — scope বদলালে এটা কাজে লাগে।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি অগ্রগতি track করেন কি না, আর আগাম সতর্কতা দেখে কাজ করেন কি না।

**সাধারণ ভুল:** নিখুঁত burndown-কে লক্ষ্য মনে করা। Chart হলো কথা শুরু করার সংকেত, খেলে জেতার target নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Burndown বনাম burnup?"* → Burndown দেখায় বাকি কাজ; burnup দেখায় শেষ হওয়া কাজ আর মোট scope (scope creep ধরা পড়ে)।

**সম্পর্কিত:** [Q13 — velocity](#q13) · [Q8 — standup](#q8)

[↑ উপরে ফিরুন](#toc)

---

# E. চর্চা আর tool

---

<a id="q15"></a>
## 15. Kanban কী, Scrum থেকে এটা কীভাবে আলাদা, আর WIP limit কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Kanban হলো flow-ভিত্তিক একটা Agile পদ্ধতি: কাজের item একটা board-এর উপর দিয়ে চলতে থাকে (To Do → In Progress → Done), কোনো নির্দিষ্ট Sprint নেই। WIP (Work In Progress) limit ঠিক করে দেয় প্রতিটি column-এ একসাথে কতগুলো item থাকতে পারবে। এটা team-কে বাধ্য করে নতুন কাজ শুরুর আগে চলতি কাজ শেষ করতে। Kanban মানায় support-এর মতো চলমান, অনিশ্চিত কাজে; Scrum মানায় পরিকল্পিত feature delivery-তে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Kanban = চলমান flow।**
এখানে কোনো Sprint নেই। যখন capacity খালি হয়, item board-এর উপর দিয়ে এগোয়। কিছু শেষ হলেই release করবেন, Sprint-এর সীমানায় নয়।

**ধাপ ২ — WIP limit — মূল ধারণা।**
প্রতিটি column-এর একটা সর্বোচ্চ সংখ্যা থাকে (যেমন "In Progress: max 3")। ভরে গেলে নতুন কাজ শুরু করা যাবে না — আগে কিছু শেষ করতে হবে বা unblock করতে হবে।

```
To Do        In Progress (max 3)     Done
[a][b][c]    [d][e][f]   ← full!     [g][h]
             (can't pull a new item until one moves to Done)
```

এতে সবাই সব কাজ শুরু করে কিছুই শেষ না করার অভ্যাস বন্ধ হয়। আর bottleneck সামনে চলে আসে।

**ধাপ ৩ — Kanban বনাম Scrum।**

| | Scrum | Kanban |
|---|---|---|
| Cadence | নির্দিষ্ট Sprint | চলমান flow |
| Roles | PO, SM, Developers | কোনো বাধ্যতামূলক role নেই |
| Change | Sprint-এর মাঝে নয় | যেকোনো সময় |
| Best for | পরিকল্পিত feature-এর কাজ | support, ops, নিয়মিত ধারা |

**ধাপ ৪ — কখন Kanban ব্যবহার করবেন।**
যে কাজে বারবার বাধা আসে বা কাজ চলমান (bug fixing, support, ops), সেখানে নির্দিষ্ট Sprint-এর প্রতিশ্রুতি মানায় না। কিছু team দুটো মিলিয়ে ব্যবহার করে ("Scrumban")।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি কাজের ধরন বুঝে সঠিক Agile ধরনটা বাছতে পারেন কি না। আর WIP সীমিত রাখার শক্তিশালী ধারণাটা বোঝেন কি না।

**সাধারণ ভুল:** Kanban মানে "কোনো process নেই" — এটা ভাবা। এতে কড়া শৃঙ্খলা আছে — বিশেষ করে WIP limit আর flow মাপা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"WIP সীমিত করব কেন?"* → বেশি সমান্তরাল কাজ সবকিছু ধীর করে দেয় (context switching) আর bottleneck ঢেকে রাখে; সীমিত করলে delivery দ্রুত হয়।

**সম্পর্কিত:** [Q3 — Scrum overview](#q3) · [Q6 — sprint](#q6)

[↑ উপরে ফিরুন](#toc)

---

<a id="q16"></a>
## 16. Sprint-এর মাঝপথে requirement বদলে গেলে আপনি কী করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Agile পরিবর্তনকে স্বাগত জানায়, কিন্তু Sprint-এর মাঝে Sprint Goal সুরক্ষিত থাকে। ছোট ও জরুরি পরিবর্তন হলে আমি PO আর team-এর সাথে আলোচনা করব — কিছু ঢোকাতে হলে সাধারণত সমান আকারের কিছু বের করে দিতে হয়। জরুরি নয় এমন সব কিছু পরের Sprint-এর জন্য backlog-এ যায়। মূল কথা হলো মনোযোগ রক্ষা করা, পরিবর্তন প্রত্যাখ্যান করা নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — নীতি বনাম বাস্তব চর্চা।**
Agile বদলে যাওয়া requirement-কে *স্বাগত জানায়* — কিন্তু Scrum *Sprint Goal রক্ষা করে*, যাতে team মনোযোগ ধরে রাখতে পারে। এই দুটো পরস্পরবিরোধী নয়: backlog পর্যায়ে পরিবর্তনকে স্বাগত জানান, কিন্তু চলতি Sprint-কে এলোমেলো করবেন না।

**ধাপ ২ — বাস্তব বিকল্পগুলো।**
- **জরুরি নয় এমন পরিবর্তন** → Product Backlog-এ যোগ করুন; ভবিষ্যতের কোনো Sprint-এর জন্য priority ঠিক করুন।
- **ছোট জরুরি পরিবর্তন** → PO আর team রাজি হয়ে এটা ঢোকায়, আর সমান আকারের কাজ বের করে দেয় (এটা বদল, যোগ নয়)।
- **সংকট/জরুরি অবস্থা** (production বন্ধ, security) → PO Sprint বাতিল করতে বা নতুন করে পরিকল্পনা করতে পারেন; বিরল, কিন্তু হয়।

**ধাপ ৩ — কে সিদ্ধান্ত নেয়।**
**Product Owner** priority ঠিক করেন, কিন্তু **team**-কে মানতে হবে যে goal না ভেঙে পরিবর্তনটা করা সম্ভব। এটা আলোচনা, আদেশ নয়।

**ধাপ ৪ — Sprint কেন রক্ষা করবেন।**
Sprint-এর মাঝে বারবার পরিবর্তন মানে কিছুই কখনো শেষ হয় না (সব কিছু 80% হয়ে পড়ে থাকে)। Sprint ছোট হওয়ায় এমনিতেই কোনো পরিবর্তনকে বেশিদিন অপেক্ষা করতে হয় না — সাধারণত কয়েক দিন।

**Interviewer কেন জিজ্ঞেস করে:** এটা নমনীয়তা আর মনোযোগের ভারসাম্য যাচাই করে — প্রতিটি team-ই এই টানাপোড়েনে পড়ে।

**সাধারণ ভুল:** হয় কঠোরভাবে সব পরিবর্তন মানা না করা ("এই Sprint-এ হবে না, ব্যস"), নয়তো প্রতিটি বাধা মেনে নেওয়া (ফলে team এলোমেলো হয় আর কিছুই শেষ হয় না)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"পরিবর্তনের কারণে Sprint Goal অর্থহীন হয়ে গেলে কী হবে?"* → PO Sprint বাতিল করে নতুন পরিকল্পনা করতে পারেন; পুরো দিক বদলানোর এটাই একমাত্র পরিষ্কার উপায়।

**সম্পর্কিত:** [Q6 — sprint goal](#q6) · [Q4 — PO role](#q4) · [Q1 — পরিবর্তনকে স্বাগত জানানো](#q1)

[↑ উপরে ফিরুন](#toc)

---

<a id="q17"></a>
## 17. Technical debt কী, আর sprint-ভিত্তিক team-এ আপনি এটা কীভাবে সামলান?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Technical debt হলো শর্টকাটের খরচ — দ্রুত লেখা code, যা পরে আপনাকে ধীর করে দেবে। এটা এখন সময় ধার নেওয়া, আর ভবিষ্যতে bug আর ধীর পরিবর্তনের মাধ্যমে সুদ দেওয়ার মতো। এটা সামলাতে হয় দৃশ্যমান করে (track করে), আর প্রতিটি Sprint-এর একটা অংশ (ধরুন 10–20%) রেখে ধীরে ধীরে শোধ করে। পাশাপাশি review আর শক্ত Definition of Done দিয়ে নতুন debt ঠেকাতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের একটা ছবি: টাকা ধার নেওয়া।**
শর্টকাট আজকে দ্রুত delivery দেয় (ধার নেওয়া), কিন্তু পরে সুদ দিতে হয় — ওই এলোমেলো জায়গায় প্রতিটি ভবিষ্যৎ পরিবর্তনে বেশি সময় লাগে আর bug-এর ঝুঁকি থাকে। অল্প debt একটা বুদ্ধিমান বদল হতে পারে; বেশি হলে team পঙ্গু হয়ে যায়।

**ধাপ ২ — Flutter project-এ সাধারণ উৎস।**
- Deadline ধরতে test বাদ দেওয়া।
- পুনঃব্যবহারযোগ্য widget/logic-এর বদলে copy-paste করা widget/logic।
- পুরোনো package, কোনো architecture নেই, widget-এর ভেতরে business logic।

**ধাপ ৩ — Sprint-এ এটা কীভাবে সামলাবেন।**
- **দৃশ্যমান করুন** — debt-এর item backlog-এ track করুন, মাথার ভেতরে রাখবেন না।
- **এর জন্য বাজেট রাখুন** — প্রতিটি Sprint-এর ~10–20% debt শোধের জন্য রাখুন, যাতে এটা জমে না যায়।
- **চলতে চলতে শোধ করুন** — boy scout rule: আপনি যে code-এ কাজ করছেন তার আশেপাশের অংশ একটু ভালো করুন ([Q12 Clean Code](section-16-clean-code-bn.md#q12))।
- **নতুন debt ঠেকান** — code review আর শক্ত Definition of Done।

**ধাপ ৪ — ব্যবসার ভাষায় বলুন।**
"আমরা পরিষ্কার code চাই" — এটা বলবেন না। বলুন "এই এলোমেলো module থেকেই আমাদের বেশিরভাগ bug আসে আর নতুন feature ধীর হয়; এটা ঠিক করলে delivery দ্রুত হবে।" Debt-কে ব্যবসার খরচের সাথে জুড়ে দিন।

**Interviewer কেন জিজ্ঞেস করে:** Senior engineer গতি আর টেকসই হওয়ার মধ্যে ভারসাম্য রাখেন; তাঁরা দেখতে চান আপনি ভেবেচিন্তে debt সামলান, উপেক্ষাও করেন না, আবার এটা নিয়ে বাড়াবাড়িও করেন না।

**সাধারণ ভুল:** হয় debt উপেক্ষা করা যতক্ষণ না codebase-এ কাজ করাই অসম্ভব হয়, নয়তো একটা বড় "সব থামাও আর refactor করো" sprint দাবি করা (ঝুঁকিপূর্ণ আর সাধারণত নাকচ হয়)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"PO-কে সময় বরাদ্দ করতে কীভাবে রাজি করাবেন?"* → bug-এর হার আর ধীর delivery দিয়ে খরচটা দেখান; ছোট, নিয়মিত একটা বাজেটের প্রস্তাব দিন ([Q3 Refactoring](section-15-code-smells-bn.md#q3))।

**সম্পর্কিত:** [Q3 (Refactoring) — team-কে রাজি করানো](section-15-code-smells-bn.md#q3) · [Q12 (Clean Code) — boy scout rule](section-16-clean-code-bn.md#q12)

[↑ উপরে ফিরুন](#toc)

---

<a id="q18"></a>
## 18. আপনি Jira কীভাবে ব্যবহার করেন? Epic, story, task আর board ব্যাখ্যা করুন।

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-18-agile-scrum.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Agile-এর কাজ track করার সবচেয়ে সাধারণ tool হলো Jira। কাজ একটা স্তরবিন্যাসে সাজানো হয়: Epic হলো বড় একটা কাজের অংশ, যেটা ভাঙা হয় Story-তে (user যা দেখে এমন feature), আর Story ভাঙা যায় Task/Subtask-এ। Board-এ item গুলো column ধরে এগোতে দেখা যায় (To Do → In Progress → Done), তাই পুরো team অবস্থাটা দেখতে পায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — স্তরবিন্যাস।**

```
Epic         "User authentication"          (large, spans many sprints)
 └─ Story    "As a user, I can log in"       (one feature, fits in a sprint)
     └─ Task        "Build the login form"   (a piece of work)
         └─ Subtask "Add email validation"   (a small step)
```

**ধাপ ২ — Issue type গুলো।**
- **Epic** — একটা বড় বিষয়, অনেক Sprint ধরে delivery হয়।
- **Story** — user যা দেখে এমন feature, সাথে acceptance criteria থাকে ([Q11](#q11))।
- **Task** — কারিগরি একটা কাজ (সবসময় user-এর চোখে পড়ে না)।
- **Bug** — নষ্ট হয়ে যাওয়া কিছু, যা ঠিক করতে হবে।

**ধাপ ৩ — Board।**
Scrum/Kanban board, যাতে column থাকে (To Do, In Progress, In Review, Done)। প্রতিটি card একটা issue; কাজ এগোনোর সাথে আপনি এটা টেনে পরের column-এ নেন। Standup-এর সময় team এক নজরেই অবস্থা বুঝে নেয়।

**ধাপ ৪ — এটাকে কাজের রাখুন, আমলাতান্ত্রিক নয়।**
Tool team-এর সেবা করে, উল্টোটা নয়। Ticket সৎভাবে update করুন, কিন্তু process-এ ডুবে যাবেন না — লক্ষ্য হলো দৃশ্যমানতা, কাগজপত্র নয়।

**Interviewer কেন জিজ্ঞেস করে:** বেশিরভাগ team Jira (বা একই রকম কিছু) ব্যবহার করে; তাঁরা নিশ্চিত হতে চান আপনি একটা track করা Agile workflow-তে কাজ করতে পারেন।

**সাধারণ ভুল:** Jira-কেই লক্ষ্য মনে করা — অতিরিক্ত বিস্তারিত ticket আর লোক দেখানো status — সহজ একটা দৃশ্যমানতার tool হিসেবে না দেখে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Epic বনাম Story?"* → Epic = বড়, অনেক Sprint; Story = একটা feature যা এক Sprint-এ ধরে যায়।

**সম্পর্কিত:** [Q11 — user stories](#q11) · [Q5 — backlog](#q5) · [Q15 — boards](#q15)

[↑ উপরে ফিরুন](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। আগে table, তারপর এক লাইনের reminder।

## Scrum এক নজরে

| Roles | Artifacts | Events |
|---|---|---|
| Product Owner (কী) | Product Backlog | Sprint Planning |
| Scrum Master (process) | Sprint Backlog | Daily Standup |
| Developers (কীভাবে) | Increment | Review + Retrospective |

## যে জোড়াগুলো গুলিয়ে যায়

| | A | B |
|---|---|---|
| Review vs Retro | product (demo) | process (উন্নতি) |
| Acceptance Criteria vs DoD | প্রতি story-তে | পুরো team-এ |
| Product vs Sprint Backlog | সবকিছু (PO) | এই sprint (team) |
| Scrum vs Kanban | নির্দিষ্ট sprint | continuous flow |
| Burndown vs Burnup | বাকি কাজ | শেষ হওয়া কাজ + scope |

## এক লাইনের reminder

- **Agile** = working software + পরিবর্তনে সাড়া দেওয়া; "docs/plan থাকবে না" মানে নয়। ([Q1](#q1))
- **Waterfall** = ধাপে ধাপে, scope নির্দিষ্ট; **Agile** = iterative, feedback-নির্ভর। ([Q2](#q2))
- **Scrum Master = coach/facilitator**, manager নন। ([Q4](#q4))
- **PO priority ঠিক করেন; team ঠিক করে কতটুকু** কাজ নেবে। ([Q4](#q4), [Q7](#q7))
- **Sprint-এর দৈর্ঘ্য নির্দিষ্ট** — বাড়াবেন না; অসমাপ্ত কাজ আবার plan করুন। ([Q6](#q6))
- **Standup** = 15 মিনিটের team sync (৩টি প্রশ্ন), boss-কে দেওয়া status report নয়। ([Q8](#q8))
- **Review = product-এর demo; Retro = process-এর উন্নতি** (শুধু team)। ([Q9](#q9))
- **Story point = আপেক্ষিক আকার, ঘণ্টা নয়**; planning poker দিয়ে estimate করুন। ([Q12](#q12))
- **Velocity** = গড় point/sprint; এটা planning-এর সাহায্য, কখনোই cross-team KPI নয়। ([Q13](#q13))
- **WIP limit** শুরু করার আগে শেষ করতে বাধ্য করে — এটাই Kanban-এর মূল কথা। ([Q15](#q15))
- Sprint-এর মাঝখানে **Sprint Goal রক্ষা করুন**; বদলে নিন, উপরে চাপাবেন না। ([Q16](#q16))
- **Technical debt** = এটাকে দৃশ্যমান করুন, প্রতি sprint-এ ~10–20% বরাদ্দ রাখুন। ([Q17](#q17))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যান

Agile interview-এ আসল অভিজ্ঞতা যাচাই করা হয়। জোরে বলে অনুশীলন করুন:

1. *"আপনি চালিয়েছেন এমন একটা Sprint-এর গল্প বলুন।"* → planning → goal → daily standup → review/retro, একটা বাস্তব উদাহরণসহ।
2. *"৩ নম্বর দিনে একজন stakeholder পরিবর্তন চাইছেন — আপনি কী করবেন?"* → goal রক্ষা করুন; জরুরি হলে PO-র সাথে swap করুন, নাহলে backlog-এ রাখুন।
3. *"আপনার velocity কমে গেছে — team কি ফাঁকি দিচ্ছে?"* → না; ছুটি, blocker, scope দেখুন; velocity কোনো performance score নয়।
4. *"Tech debt জমতে থাকা কীভাবে আটকান?"* → দৃশ্যমান করুন, প্রতি sprint-এ একটু অংশ বরাদ্দ রাখুন, শক্ত DoD রাখুন।
5. *"Support team-এর জন্য Scrum না Kanban?"* → Kanban — WIP limit সহ continuous flow বারবার বাধা আসা কাজের সাথে মানায়।

উত্তরের সাথে "আমাদের team-এ আমরা X করেছি" জুড়ে দিন। আসল ও নির্দিষ্ট অভিজ্ঞতা প্রতিবারই বইয়ের সংজ্ঞাকে হারিয়ে দেয়। এটা remote আর BD — দুই ধরনের interview-তেই খাটে।

[↑ উপরে ফিরুন](#toc)

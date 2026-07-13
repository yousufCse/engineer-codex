# Full-Stack Web Deployment — সম্পূর্ণ গাইড (সহজ বাংলা)

> একটা **সম্পূর্ণ (complete) সেলফ-স্টাডি রেফারেন্স** — লক্ষ্য: এই **এক ডকেই** full-stack web app deployment শেখা যাবে। PaaS থেকে VPS, Docker, CI/CD আর cloud — সব রাস্তা এক জায়গায়।
> প্রথমবার **~১.৫ ঘণ্টায় মূল ধারণা** নিয়ে নিন (পর্ব ১ + পর্ব ২)। বাকিটা reference — দরকার মতো ফিরে আসবেন।
> বিষয়: **নিজের কম্পিউটারে বানানো একটা full-stack app (frontend + backend + database) কীভাবে ইন্টারনেটে সবার জন্য live করবেন — চারটা আলাদা উপায়ে, সহজ থেকে production-grade পর্যন্ত।**

---

### এই ডক কীভাবে পড়বেন

- ভাষা: **সহজ বাংলা**। ছোট ছোট বাক্য। technical শব্দ ইংরেজিতেই রাখা হয়েছে (যেমন *server, port, deploy, build*), কারণ industry-তে এগুলো ইংরেজিতেই বলা হয়।
- প্রতিটি বড় অংশের শেষে `↑ সূচিপত্রে ফিরুন` লিংক আছে — ওটাতে ক্লিক করলে উপরে **সূচিপত্রে (TOC)** ফিরবেন।
- ছবি দুই ধরনের: **Mermaid diagram** (GitHub/VS Code-এ রেন্ডার হয়) আর **ASCII diagram** (সব জায়গায় দেখা যায়)।
- সব command **আসল, চালানোর মতো**। কপি করে চালাতে পারবেন — শুধু নিজের নাম/ডোমেইন বসিয়ে নেবেন।
- 🟢 = করুন (do), 🔴 = করবেন না (don't) — checklist সহজ করতে।
- পড়ার পথ (তিন গতি):
  - **দ্রুত (~১.৫ ঘণ্টা):** পর্ব ১ + পর্ব ২ (PaaS)। এতেই আপনার app প্রথমবার live হয়ে যাবে।
  - **মাঝারি:** পর্ব ৩ (VPS) + পর্ব ৪ (Docker) — নিজের হাতে সার্ভার চালানো শিখবেন।
  - **পূর্ণ (reference):** পর্ব ৫ (CI/CD + cloud) + পর্ব ৬ (production জরুরি বিষয়) — কাজ করার সময় ফিরে আসবেন।

### একটা কথা আগে বুঝে নিন

Deployment শেখার সবচেয়ে বড় ভুল = "সব একসাথে শেখা"। তা করবেন না। **এক app** নিন (ছোট হলেও), সেটাকে **আগে PaaS-এ live করুন** (পর্ব ২)। তারপর **সেই একই app** VPS-এ (পর্ব ৩), তারপর Docker-এ (পর্ব ৪), তারপর CI/CD দিয়ে (পর্ব ৫) — একই app বারবার deploy করলে চারটা রাস্তার পার্থক্য নিজে থেকেই পরিষ্কার হয়ে যাবে। এটাই এই ডকের শেখানোর পথ।

---

## সূচিপত্র (Table of Contents) <a id="toc"></a>

**পর্ব ১ — ভিত্তি (Foundations)**
1. [১ মিনিটে সারাংশ (TL;DR)](#s1)
2. [Deployment আসলে কী — dev থেকে production-এর যাত্রা](#s2)
3. [Full-stack app-এর অংশগুলো — কোনটা কোথায় যায়](#s3)
4. [যে ১০টা মূল ধারণা সব জায়গায় লাগবে](#s4)
5. [Deploy করার ৪টা রাস্তা — তুলনা ও কখন কোনটা](#s5)

**পর্ব ২ — সবচেয়ে সহজ শুরু: PaaS**

6. [PaaS কী, কীভাবে কাজ করে](#s6)
7. [Frontend deploy — Vercel / Netlify](#s7)
8. [Backend deploy — Render / Railway](#s8)
9. [Database — managed Postgres (Supabase / Neon)](#s9)
10. [Env vars, custom domain, HTTPS — PaaS-এ](#s10)

**পর্ব ৩ — নিজের সার্ভার: VPS (গভীরে)**

11. [VPS কী, কেন শিখবেন](#s11)
12. [Server প্রথম setup — SSH, user, firewall](#s12)
13. [Runtime + database install](#s13)
14. [App কে চালু রাখা — systemd / PM2](#s14)
15. [Nginx reverse proxy](#s15)
16. [Domain + free SSL (Let's Encrypt)](#s16)
17. [পুরো VPS deploy — এক জায়গায় (frontend+backend+db)](#s17)

★ [**Capstone — React + Node + Postgres: সম্পূর্ণ deploy (শুরু → শেষ)**](#capstone)

**পর্ব ৪ — Docker + Containers**

18. [Container কী, কেন ("আমার মেশিনে তো চলছিল" সমস্যা)](#s18)
19. [Dockerfile — frontend ও backend](#s19)
20. [docker-compose — পুরো stack এক ফাইলে](#s20)
21. [Image registry (Docker Hub / GHCR)](#s21)
22. [VPS-এ Docker দিয়ে deploy](#s22)

**পর্ব ৫ — CI/CD + Cloud (production-grade)**

23. [CI/CD কী — pipeline-এর গঠন](#s23)
24. [GitHub Actions — build → test → deploy](#s24)
25. [Cloud providers (AWS/GCP) — কোন service কী কাজ](#s25)
26. [AWS-এ deploy — কয়েকটা রাস্তা](#s26)
27. [Kubernetes — কখন লাগে, basics (সৎভাবে)](#s27)

**পর্ব ৬ — Production-এ যা না জানলেই নয়**

28. [Secrets ও environment management](#s28)
29. [Domain, DNS, CDN](#s29)
30. [Monitoring, logs, health check](#s30)
31. [Database migration ও backup](#s31)
32. [Zero-downtime deploy ও rollback](#s32)
33. [Scaling — বড় হলে কী করবেন](#s33)
34. [Security checklist](#s34)

**পর্ব ৭ — গুছিয়ে রাখা (Reference)**

35. [কোন scenario কখন — সিদ্ধান্তের গাইড](#s35)
36. [শেখার পথ — ধাপে ধাপে, project সহ](#s36)
37. [সাধারণ ভুল (এড়িয়ে চলুন)](#s37)
38. [শব্দকোষ (Glossary)](#s38)
39. [রেফারেন্স / আরও শেখার জায়গা](#s39)
40. [বাংলা ভিডিও রিসোর্স (YouTube)](#s40)

---

# পর্ব ১ — ভিত্তি (Foundations)

## ১. ১ মিনিটে সারাংশ (TL;DR) <a id="s1"></a>

- **Deploy** = আপনার কম্পিউটারে (localhost) চলা app-টাকে একটা **সবসময় চালু থাকা কম্পিউটারে (server)** তুলে দেওয়া, যাতে ইন্টারনেট থেকে যে কেউ URL দিয়ে ঢুকতে পারে।
- Full-stack app-এর **৩টা অংশ** আলাদা করে ভাবুন: **frontend** (browser-এ যা দেখা যায়), **backend/API** (logic + auth), **database** (data জমা থাকে)। Deploy মানে এই তিনটাকে জায়গামতো বসানো + তাদের একে অপরের সাথে কথা বলিয়ে দেওয়া।
- **৪টা রাস্তা**, সহজ থেকে কঠিন:
  1. **PaaS** (Vercel, Netlify, Render, Railway) — click করলেই হয়। শেখা সবচেয়ে সহজ, শুরু এখান থেকেই।
  2. **VPS** (DigitalOcean, EC2) — নিজের একটা Linux সার্ভার। Nginx, SSH, systemd, SSL নিজে বসান। সবচেয়ে বেশি **শেখা হয়** এখানে।
  3. **Docker** — app-কে একটা "box"-এ প্যাক করে যেকোনো জায়গায় একইভাবে চালানো।
  4. **CI/CD + Cloud** — git push করলেই নিজে নিজে test + build + deploy। Production-এ এটাই আসল।
- সব রাস্তায় **একই কয়েকটা ধারণা** ঘুরেফিরে আসে: server, port, domain/DNS, **HTTPS/SSL**, **environment variable (secret)**, **build vs run**, **reverse proxy**, **process manager**। এগুলো একবার বুঝলে সব রাস্তা সহজ (পর্ব [৪ নং](#s4))।
- **শেখার নিয়ম:** এক app বারবার — আগে PaaS, তারপর VPS, তারপর Docker, তারপর CI/CD। তাহলে পার্থক্যগুলো হাতে-কলমে বুঝবেন।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২. Deployment আসলে কী — dev থেকে production-এর যাত্রা <a id="s2"></a>

আপনি কোড লিখে `npm run dev` দিলেন, browser-এ `localhost:3000` খুললেন — app চলছে। কিন্তু এটা **শুধু আপনার কম্পিউটারে**। আপনি ল্যাপটপ বন্ধ করলেই app শেষ। বন্ধুকে link পাঠালে সে খুলতে পারবে না।

**Deployment** মানে এই ফাঁকটা পার করা:

```
আপনার ল্যাপটপ (localhost)          →          Server (ইন্টারনেটে, সবসময় চালু)
─────────────────────────                    ──────────────────────────────
শুধু আপনি দেখেন                                পৃথিবীর যে কেউ URL দিয়ে দেখে
বন্ধ করলে app শেষ                             ২৪/৭ চালু
localhost:3000                                https://myapp.com
```

### তিনটা environment আলাদা করে চিনুন

বাস্তবে একটা app-এর সাধারণত তিনটা "environment" থাকে:

| Environment | কী | কারা ব্যবহার করে |
|---|---|---|
| **development (dev)** | আপনার নিজের মেশিন, `localhost` | শুধু আপনি, কোড লেখার সময় |
| **staging** | production-এর মতো একটা কপি, কিন্তু আসল না | team, testing-এর জন্য |
| **production (prod)** | আসল live site, আসল user, আসল data | পৃথিবীর সবাই |

শুরুতে শুধু dev আর prod থাকলেই চলে। বড় হলে মাঝখানে staging যোগ করবেন।

### Deploy করলে ভেতরে আসলে কী হয়

মোটামুটি সব রাস্তায় একই চারটা ধাপ:

```mermaid
flowchart LR
  A[কোড লেখা<br/>local] --> B[Build<br/>কোডকে চালানোর মতো রূপে আনা]
  B --> C[Ship<br/>server-এ পাঠানো]
  C --> D[Run<br/>server-এ চালু রাখা]
  D --> E[Serve<br/>domain + HTTPS দিয়ে user-কে দেওয়া]
```

1. **Build** — source code-কে চালানোর উপযোগী রূপে আনা (React → static HTML/JS; TypeScript → JavaScript; ইত্যাদি)।
2. **Ship** — সেই build-টা server-এ পাঠানো (git, scp, docker image — যেভাবেই হোক)।
3. **Run** — server-এ app চালু করা এবং **চালু রাখা** (crash করলে আবার চালু)।
4. **Serve** — একটা domain আর HTTPS দিয়ে user-এর browser পর্যন্ত পৌঁছে দেওয়া।

চারটা রাস্তার পার্থক্য শুধু: **এই ধাপগুলো কে করে — আপনি হাতে, নাকি tool নিজে থেকে।** PaaS-এ প্রায় সব tool করে; VPS-এ প্রায় সব আপনি করেন; CI/CD-তে একটা pipeline করে।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩. Full-stack app-এর অংশগুলো — কোনটা কোথায় যায় <a id="s3"></a>

Deploy শুরুর আগে এটা পরিষ্কার হওয়া সবচেয়ে জরুরি। Full-stack app আসলে **আলাদা আলাদা কয়েকটা জিনিস**, একটা না। প্রত্যেকটার deploy করার নিয়ম আলাদা।

```mermaid
flowchart TB
  U[User-এর browser]
  subgraph Frontend["Frontend (client)"]
    F[React / Next / Vue<br/>HTML + CSS + JS]
  end
  subgraph Backend["Backend (server)"]
    A[Node/Express, Django,<br/>.NET, Laravel — API]
  end
  subgraph Data["Database + Storage"]
    DB[(Postgres / MySQL)]
    ST[File storage<br/>images, video]
  end
  U --> F
  F -->|HTTP request /api| A
  A -->|SQL query| DB
  A --> ST
```

| অংশ | কী করে | উদাহরণ | Deploy কোথায় (সহজ পছন্দ) |
|---|---|---|---|
| **Frontend** | Browser-এ যা দেখা যায় — UI | React, Next.js, Vue, Angular | Static host / CDN (Vercel, Netlify) |
| **Backend / API** | Logic, auth, database-এর সাথে কথা | Express, Django, .NET, Laravel | App server (Render, VPS, container) |
| **Database** | Data স্থায়ীভাবে জমা রাখে | Postgres, MySQL, MongoDB | Managed DB (Supabase, Neon, RDS) |
| **File/Object storage** | ছবি, ভিডিও, বড় ফাইল | S3, Supabase Storage, R2 | Object storage + CDN |
| **Background jobs** | ইমেইল পাঠানো, রিপোর্ট বানানো | queue + worker | আলাদা worker process |

### দুই ধরনের frontend — পার্থক্যটা deploy বদলে দেয়

এটা না বুঝলে বহু মানুষ আটকায়:

- **Static frontend (SPA / SSG)** — build করলে শুধু কতগুলো **HTML/CSS/JS ফাইল** বের হয়। এগুলো "চলে" না, শুধু browser-এ পাঠাতে হয়। তাই একে **CDN / static host**-এ রাখলেই হয় (সবচেয়ে সস্তা, সবচেয়ে দ্রুত)। উদাহরণ: plain React (Vite build), Vue, পুরনো Create-React-App।
- **Server-rendered frontend (SSR)** — প্রতিটা request-এ server-এ কোড চলে HTML বানায়। এর জন্য একটা **চালু Node process** লাগে, শুধু ফাইল রাখলে হয় না। উদাহরণ: Next.js (SSR mode), Nuxt, Remix।

> মনে রাখার সহজ নিয়ম: **build করে শুধু ফাইল পেলে → static host। build করেও একটা "চালু process" লাগলে → app server।**

এই ডকে full-stack বলতে ধরছি: **একটা frontend + একটা backend API + একটা Postgres database** — বাস্তবে সবচেয়ে common combination। বাকি অংশ (storage, jobs) দরকার মতো যোগ হবে।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৪. যে ১০টা মূল ধারণা সব জায়গায় লাগবে <a id="s4"></a>

এই ১০টা একবার বুঝলে, চারটা রাস্তার ৮০% জানা হয়ে গেল। প্রতিটার সাথে একটা রোজকার উদাহরণ দিলাম।

**১) Server (সার্ভার)** — একটা কম্পিউটার যেটা কখনো বন্ধ হয় না, ইন্টারনেটে লাগানো। আপনার ল্যাপটপের মতোই, শুধু data-center-এ বসে সবসময় চালু। *উদাহরণ: একটা দোকান যেটা ২৪ ঘণ্টা খোলা।*

**২) Port (পোর্ট)** — এক সার্ভারে অনেক app চলতে পারে; প্রত্যেকে একটা নম্বরে "শোনে"। Web সাধারণত **80** (http) আর **443** (https)। আপনার app হয়তো ভেতরে **3000** বা **8000**-এ চলে। *উদাহরণ: এক বড় বিল্ডিং (server), অনেক ফ্ল্যাট (port); নম্বর ছাড়া চিঠি পৌঁছাবে না।*

**৩) Domain + DNS** — `myapp.com` একটা নাম; DNS হলো সেই নামকে সার্ভারের **IP address**-এ (যেমন `142.93.1.5`) বদলে দেয়। *উদাহরণ: ফোনবুক — নাম দিলে নম্বর বের করে দেয়।*

**৪) HTTPS / SSL (TLS)** — data-কে encrypt করে, যাতে মাঝপথে কেউ পড়তে না পারে। browser-এ 🔒 তালা। আজকাল **বাধ্যতামূলক** (Let's Encrypt দিয়ে ফ্রি)। *উদাহরণ: সিল করা খাম, খোলা পোস্টকার্ড নয়।*

**৫) Environment variable (env var)** — কোডের বাইরে রাখা setting/secret: database password, API key, ইত্যাদি। **কখনো কোডে/GitHub-এ লিখবেন না।** *উদাহরণ: ঘরের চাবি — দেয়ালে লিখে রাখেন না, আলাদা রাখেন।* (বিস্তারিত [২৮ নং](#s28))

**৬) Build vs Runtime** — **build** = deploy-এর আগে একবার কোড তৈরি করা (compile, bundle)। **runtime** = user request দিলে যেটা চলে। কিছু ভুল build-এ ধরা পড়ে, কিছু runtime-এ। *উদাহরণ: রান্না করা (build) বনাম পরিবেশন করা (runtime)।*

**৭) Process manager** — আপনার app crash করলে বা server reboot হলে কে আবার চালু করবে? একটা process manager (**systemd**, **PM2**, বা container orchestrator)। এটা ছাড়া app একবার পড়ে গেলে পড়েই থাকে। *উদাহরণ: জেনারেটর — কারেন্ট গেলে নিজে চালু হয়।*

**৮) Reverse proxy** — user-এর সব request প্রথমে একটা "gatekeeper"-এ আসে (**Nginx** / **Caddy**), সে HTTPS সামলায়, তারপর ভেতরের ঠিক app-এ পাঠায়। *উদাহরণ: অফিসের রিসেপশন — সবাই আগে ওখানে আসে, তারপর সঠিক রুমে যায়।* (বিস্তারিত [১৫ নং](#s15))

**৯) Container (Docker)** — app + তার সব dependency একসাথে একটা "box"-এ প্যাক করা, যাতে যেকোনো মেশিনে **হুবহু একইভাবে** চলে। *উদাহরণ: রেডি টিফিন বক্স — যেখানেই নিন, ভেতরের খাবার একই।* (বিস্তারিত [১৮ নং](#s18))

**১০) CI/CD** — **CI** (Continuous Integration): git push করলে নিজে নিজে test + build চলে। **CD** (Continuous Deployment): সেটা পাস করলে নিজে নিজে deploy হয়। মানুষ হাতে কিছু করে না। *উদাহরণ: কারখানার conveyor belt — একদিকে কাঁচামাল, অন্যদিকে রেডি পণ্য।* (বিস্তারিত [২৩ নং](#s23))

> এই ১০টা মুখস্থ নয়, **বুঝুন**। বাকি পুরো ডক এগুলোরই হাতে-কলমে প্রয়োগ।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৫. Deploy করার ৪টা রাস্তা — তুলনা ও কখন কোনটা <a id="s5"></a>

```mermaid
flowchart LR
  subgraph সহজ["সহজ · কম নিয়ন্ত্রণ"]
    P[PaaS<br/>Vercel/Render]
  end
  subgraph মাঝারি[" "]
    V[VPS<br/>DigitalOcean/EC2]
    D[Docker<br/>container]
  end
  subgraph কঠিন["কঠিন · পূর্ণ নিয়ন্ত্রণ"]
    C[CI/CD + Cloud<br/>Actions + AWS/k8s]
  end
  P --> V --> D --> C
```

| | **PaaS** | **VPS** | **Docker** | **CI/CD + Cloud** |
|---|---|---|---|---|
| **কী** | সব-অটো platform | খালি Linux server | app প্যাকেজিং | pipeline + cloud service |
| **আপনি কতটা করেন** | খুব কম | প্রায় সব | মাঝামাঝি | সেটআপ কঠিন, পরে অটো |
| **শেখার সময়** | ঘণ্টাখানেক | কয়েক দিন | কয়েক দিন | ১–২ সপ্তাহ |
| **নিয়ন্ত্রণ** | কম | পূর্ণ | পূর্ণ | পূর্ণ |
| **খরচ** | ফ্রি tier ভালো, বড় হলে দামি | সস্তা ($5–10/মাস) | VPS-এর সমান | পরিবর্তনশীল, বড় হলে দামি |
| **শেখা হয় কতটা** | কম | **সবচেয়ে বেশি** | অনেক | অনেক (production skill) |
| **কখন** | দ্রুত launch, ছোট team, MVP | control চাই, খরচ কমাতে, শিখতে | একই app বহু জায়গায়, team | বড় team, ঘনঘন deploy, production |

### সহজ সিদ্ধান্ত

- **প্রথমবার / দ্রুত দেখাতে চাই / MVP** → **PaaS** (পর্ব ২)। ১ ঘণ্টায় live।
- **শিখতে চাই কীভাবে ভেতরে কাজ করে / খরচ কমাতে চাই** → **VPS** (পর্ব ৩)। এখানে আসল শেখা।
- **"আমার মেশিনে চলছিল" সমস্যা দূর করতে / team-এ একই environment** → **Docker** (পর্ব ৪)।
- **প্রতিদিন deploy / বড় team / production-grade** → **CI/CD + Cloud** (পর্ব ৫)।

এগুলো **প্রতিদ্বন্দ্বী নয়, স্তর**। বাস্তব production প্রায়ই = **Docker + CI/CD + Cloud** একসাথে। কিন্তু শেখার সময় **এক ধাপ এক ধাপ** — নিচ থেকে উপরে।

### বাস্তব জীবনের তুলনা — বাসা ভাড়ার মতো

চারটা রাস্তা মনে রাখার সহজ উপায় — থাকার জায়গার সাথে মেলান:

| রাস্তা | বাসার তুলনা | মানে |
|---|---|---|
| **PaaS** | সার্ভিস অ্যাপার্টমেন্ট / হোটেল | সব রেডি — রান্না, পরিষ্কার, নিরাপত্তা ওরা করে। আপনি শুধু থাকেন (কোড দেন)। আরাম বেশি, নিয়ন্ত্রণ কম, ভাড়া বেশি। |
| **VPS** | খালি ফ্ল্যাট ভাড়া | চার দেয়াল পেলেন; আসবাব, রান্নাঘর, তালা সব **নিজে** বসান। খাটুনি বেশি, কিন্তু সব আপনার মতো + সস্তা। |
| **Docker** | রেডিমেড মডুলার ঘর (কন্টেইনার হাউস) | পুরো ঘর একটা বাক্সে প্যাক — যেখানেই বসান, ভেতরটা **হুবহু এক**। এক শহর থেকে আরেক শহরে তুলে নিলেও একই। |
| **CI/CD + Cloud** | স্মার্ট হোম + অটো ডেলিভারি | নতুন জিনিস এলেই নিজে নিজে সাজানো, পুরনোটা সরানো — সব অটো। বসানো কঠিন, পরে হাত লাগে না। |

[↑ সূচিপত্রে ফিরুন](#toc)

---

# পর্ব ২ — সবচেয়ে সহজ শুরু: PaaS

> লক্ষ্য: এই পর্ব শেষে আপনার full-stack app **প্রথমবার ইন্টারনেটে live** হবে — সার্ভার, Nginx, SSL কিছুই হাতে করা লাগবে না। platform সব করবে।

## ৬. PaaS কী, কীভাবে কাজ করে <a id="s6"></a>

**PaaS = Platform as a Service.** আপনি শুধু কোড দেন (সাধারণত GitHub repo যুক্ত করে), platform বাকি সব করে: build, server, HTTPS, scaling, restart — সব। আপনি server-এর মুখই দেখেন না।

> **বাস্তব উদাহরণ:** এটা যেন একটা **রেস্টুরেন্ট** — আপনি শুধু অর্ডার (কোড) দেন। রান্নাঘর কে চালায়, বাসন কে ধোয়, গ্যাস কে দেয় — কিচ্ছু ভাবতে হয় না; খাবার (live app) টেবিলে চলে আসে। বদলে দাম একটু বেশি, আর রেসিপির নিয়ন্ত্রণ আপনার হাতে থাকে না।

```mermaid
flowchart LR
  G[GitHub repo] -->|git push| P[PaaS platform]
  P --> B[অটো build]
  B --> R[অটো run + restart]
  R --> H[অটো HTTPS + domain]
  H --> U[User]
```

**যেভাবে কাজ করে (সাধারণ ধাপ):**
1. GitHub-এ আপনার repo।
2. PaaS-এ account খুলে repo যুক্ত করেন।
3. বলে দেন: কোন folder, কোন build command (`npm run build`), কোন start command (`npm start`)।
4. env vars (secret) dashboard-এ বসিয়ে দেন।
5. **Deploy।** এরপর প্রতিবার `git push` করলেই নিজে নিজে নতুন version live।

**জনপ্রিয় PaaS:**

| Platform | সবচেয়ে ভালো যার জন্য |
|---|---|
| **Vercel** | Next.js ও যেকোনো frontend (এরাই Next বানায়) |
| **Netlify** | Static site, JAMstack frontend |
| **Render** | Backend API, full-stack, cron, managed Postgres — সব একসাথে |
| **Railway** | Full-stack + database, খুব সহজ UI |
| **Fly.io** | container চালানো, user-এর কাছাকাছি region-এ |
| **Cloudflare Pages/Workers** | static + edge function |

🟢 শুরুর জন্য সহজ combo: **Frontend → Vercel, Backend + Database → Render (বা Railway)।** পুরোটা ফ্রি tier-এ শেখা যায়।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৭. Frontend deploy — Vercel / Netlify <a id="s7"></a>

ধরা যাক frontend একটা **React (Vite)** বা **Next.js** app।

### Vercel দিয়ে (সবচেয়ে সহজ)

1. কোড GitHub-এ push করুন।
2. [vercel.com](https://vercel.com) → GitHub দিয়ে login → **Add New → Project** → repo select।
3. Vercel নিজেই framework ধরে ফেলে (React/Next)। Build command আর output folder auto-fill হয়:
   - Vite React: build = `npm run build`, output = `dist`
   - Next.js: সব auto।
4. **Environment Variables** সেকশনে frontend-এর env বসান — যেমন backend API-র URL:
   ```
   VITE_API_URL = https://myapi.onrender.com
   ```
   (Next.js হলে browser-এ লাগলে নাম `NEXT_PUBLIC_` দিয়ে শুরু করতে হয়, যেমন `NEXT_PUBLIC_API_URL`।)
5. **Deploy।** ১–২ মিনিটে একটা URL পাবেন: `https://myapp.vercel.app`।

এরপর প্রতিবার `git push` → Vercel নিজে নিজে নতুন build দেয়। Pull request দিলে আলাদা **preview URL**-ও দেয় (খুব কাজের)।

### Netlify দিয়ে (static-এর জন্য)

প্রায় একই: repo যুক্ত করুন → build command (`npm run build`) + publish directory (`dist`) দিন → deploy। SPA হলে একটা `_redirects` ফাইল লাগে যাতে refresh করলে 404 না দেয়:

```
# public/_redirects  (build output-এ যাবে)
/*    /index.html   200
```

> **মূল কথা:** static frontend deploy করা সবচেয়ে সহজ অংশ — কারণ এটা "চলে" না, শুধু কতগুলো ফাইল। platform সেগুলো CDN-এ রেখে দেয়, HTTPS ফ্রি।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৮. Backend deploy — Render / Railway <a id="s8"></a>

Backend (Express/Django/.NET) একটা **চালু process** — তাই static host-এ যায় না, **app server** লাগে। Render বা Railway সহজ পছন্দ।

### Render দিয়ে (Node/Express উদাহরণ)

1. কোড GitHub-এ।
2. [render.com](https://render.com) → **New → Web Service** → repo select।
3. Settings:
   - **Build Command:** `npm install && npm run build` (build না থাকলে শুধু `npm install`)
   - **Start Command:** `npm start` (আপনার server চালু করার command)
   - **Instance Type:** Free (শেখার জন্য)।
4. **গুরুত্বপূর্ণ — port:** platform একটা port দেয় `PORT` env var-এ (Render-এ default প্রায়ই **10000**)। আপনার কোডকে সেই মান পড়ে ঐ port-এ bind করতে হবে:
   ```js
   const port = process.env.PORT || 3000;
   app.listen(port, () => console.log(`listening on ${port}`));
   ```
   🔴 port hardcode না করে সবসময় `process.env.PORT` পড়ুন — নাহলে PaaS/cloud platform অন্য port আশা করলে deploy fail হতে পারে।
5. **Environment Variables:** database URL, JWT secret, ইত্যাদি dashboard-এ বসান (কোডে নয়):
   ```
   DATABASE_URL = postgres://...
   JWT_SECRET   = <লম্বা random string>
   NODE_ENV     = production
   ```
6. Deploy → একটা URL পাবেন: `https://myapi.onrender.com`। এই URL-টাই frontend-এর `VITE_API_URL`-এ বসান।

### CORS — frontend আর backend আলাদা domain-এ

Frontend `myapp.vercel.app`, backend `myapi.onrender.com` — আলাদা origin। Browser নিরাপত্তার জন্য cross-origin request আটকায়। Backend-এ **CORS** allow করতে হবে:

```js
import cors from 'cors';
app.use(cors({ origin: 'https://myapp.vercel.app', credentials: true }));
```

🔴 `origin: '*'` production-এ, বিশেষত cookie/auth থাকলে — নিরাপদ নয়। নির্দিষ্ট origin দিন।

### Railway দিয়ে

আরও সহজ UI: repo যুক্ত করুন → Railway auto-detect করে → env vars বসান → deploy। একই project-এ **Postgres**-ও এক ক্লিকে যোগ করা যায়, আর `DATABASE_URL` নিজে থেকে inject হয়।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৯. Database — managed Postgres (Supabase / Neon) <a id="s9"></a>

Database **নিজে চালাবেন না** শুরুতে — একটা **managed** service নিন। তারা backup, patch, availability সামলায়। আপনি শুধু একটা **connection string** পান।

**জনপ্রিয় managed Postgres:**

| Service | ভালো দিক |
|---|---|
| **Supabase** | Postgres + Auth + Storage + Realtime, ভালো ফ্রি tier |
| **Neon** | Serverless Postgres, branching, ফ্রি tier উদার |
| **Railway / Render Postgres** | একই platform-এ backend + db |
| **AWS RDS** | production-grade, cloud-এর অংশ (পর্ব ৫) |

**ব্যবহার (যেকোনোটা):**
1. Service-এ একটা Postgres database বানান।
2. একটা **connection string** পাবেন:
   ```
   postgres://user:password@host:5432/dbname
   ```
3. সেটা backend-এর env var-এ বসান: `DATABASE_URL = postgres://...`
4. Backend থেকে ORM/driver (Prisma, Drizzle, `pg`, SQLAlchemy) দিয়ে connect করুন।
5. **Migration চালান** — টেবিল বানানোর script (Prisma হলে `npx prisma migrate deploy`)। (বিস্তারিত [৩১ নং](#s31))

🟢 connection string-এ `?sslmode=require` দরকার হতে পারে managed DB-তে — না দিলে connect fail করে। docs দেখুন।
🔴 Database password কখনো কোডে/GitHub-এ নয়। শুধু env var।

> এই পর্যায়ে আপনার তিন অংশ তিন জায়গায়: **frontend (Vercel) → backend (Render) → database (Supabase/Neon)।** তিনটা env var দিয়ে জোড়া লাগানো। এটাই একটা পূর্ণ PaaS full-stack deploy।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১০. Env vars, custom domain, HTTPS — PaaS-এ <a id="s10"></a>

### Environment variables — কোথায় কী

| env var | কোথায় বসে | উদাহরণ |
|---|---|---|
| `VITE_API_URL` / `NEXT_PUBLIC_API_URL` | frontend (Vercel) | backend-এর URL |
| `DATABASE_URL` | backend (Render) | Postgres connection string |
| `JWT_SECRET` | backend | লম্বা random string |
| `NODE_ENV=production` | backend | production mode চালু |

🟢 প্রতি environment-এ আলাদা মান (dev-এ localhost, prod-এ আসল URL)।
🔴 একই secret dev আর prod-এ শেয়ার করবেন না।

### Custom domain যোগ করা (নিজের `.com`)

1. একটা domain কিনুন (Namecheap, GoDaddy, Cloudflare)।
2. PaaS dashboard → **Domains → Add** → `myapp.com` লিখুন।
3. Platform বলে দেবে কোন **DNS record** বসাতে হবে। সাধারণত:
   - root domain (`myapp.com`) → একটা **A record** (IP-তে) বা **ALIAS**
   - `www` বা subdomain → একটা **CNAME** (platform-এর দেওয়া host-এ)
4. domain provider-এর DNS setting-এ সেই record বসান।
5. কিছুক্ষণ (মিনিট থেকে ঘণ্টা) পর propagate হবে।

### HTTPS

PaaS-এ HTTPS **নিজে থেকেই** হয় — Let's Encrypt দিয়ে ফ্রি certificate, auto-renew। আপনার কিছু করা লাগে না। (VPS-এ এটাই হাতে করতে হয় — [১৬ নং](#s16), তাই VPS-এ আসল শেখা।)

**পর্ব ২ শেষ — এখন আপনার app live। কিন্তু ভেতরে কী ঘটছে বুঝতে হলে, নিজের হাতে একবার সার্ভার চালাতে হবে। সেটাই পর্ব ৩।**

[↑ সূচিপত্রে ফিরুন](#toc)

---

# পর্ব ৩ — নিজের সার্ভার: VPS (গভীরে)

> লক্ষ্য: একটা খালি Linux সার্ভার নিয়ে **শূন্য থেকে** full-stack app live করা — SSH, firewall, runtime, database, systemd, Nginx, SSL সব নিজের হাতে। **এই পর্বেই deployment-এর আসল ছবি পরিষ্কার হয়।**

## ১১. VPS কী, কেন শিখবেন <a id="s11"></a>

**VPS = Virtual Private Server.** একটা data-center-এ ভাড়া নেওয়া একটা Linux কম্পিউটার, যেটা শুধু আপনার। SSH দিয়ে ভেতরে ঢুকে আপনি যা খুশি করতে পারেন — ঠিক নিজের একটা Linux মেশিনের মতো, কিন্তু সবসময় চালু ও ইন্টারনেটে।

> **বাস্তব উদাহরণ:** VPS যেন **নিজে রান্না করা** — বাজার, কাটাকুটি, রান্না, বাসন ধোয়া সব নিজে হাতে ([১২](#s12)–[১৬](#s16))। PaaS ছিল রেস্টুরেন্ট; VPS নিজের রান্নাঘর। খাটুনি বেশি, কিন্তু এতেই **রান্নাটা শেখা হয়** আর খরচও কম — তাই deployment শিখতে VPS-ই সেরা।

**কেন শিখবেন (PaaS থাকতেও):**
- PaaS আপনার থেকে সব **লুকিয়ে রাখে**। VPS-এ আপনি নিজে হাতে করেন — তাই **আসলে কী ঘটছে বোঝেন**। server, port, process, proxy, SSL — সব চোখের সামনে।
- **সস্তা** — $5–10/মাসে একটা ছোট VPS-এ full-stack app চলে (PaaS-এ বড় হলে অনেক দামি)।
- **পূর্ণ নিয়ন্ত্রণ** — যেকোনো software বসাতে পারেন।
- চাকরির জন্য **DevOps/backend skill** — এটা জানা মানুষ কম।

**জনপ্রিয় VPS:** DigitalOcean (সবচেয়ে সহজ, ভালো docs), Linode/Akamai, Hetzner (সস্তা), Vultr, AWS **EC2** / GCP **Compute Engine** (cloud-এর অংশ)।

🟢 শেখার জন্য: DigitalOcean-এ একটা **$6/মাস Ubuntu droplet** নিন। এই পুরো পর্ব ওটাতেই করা যাবে।

**ধরে নিচ্ছি:** একটা Ubuntu (22.04/24.04) VPS আছে, তার একটা IP আছে (`142.93.1.5` ধরা যাক), আর root বা sudo access আছে।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১২. Server প্রথম setup — SSH, user, firewall <a id="s12"></a>

নতুন সার্ভার পেলে প্রথমে এই কাজগুলো — **নিরাপত্তার ভিত্তি**।

### ধাপ ১: SSH দিয়ে ঢোকা

আপনার নিজের ল্যাপটপ থেকে:
```bash
ssh root@142.93.1.5
```
প্রথমবার password (provider ইমেইলে দেয়) বা SSH key দিয়ে ঢুকবেন।

### ধাপ ২: SSH key setup (password-এর চেয়ে নিরাপদ)

নিজের ল্যাপটপে key না থাকলে বানান:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
তারপর public key সার্ভারে পাঠান:
```bash
ssh-copy-id root@142.93.1.5
```
এবার password ছাড়াই ঢুকতে পারবেন। 🟢 পরে password login বন্ধ করে দেওয়া ভালো (নিচে)।

### ধাপ ৩: root-এর বদলে normal user বানান

Root দিয়ে সব করা বিপজ্জনক। একটা user বানিয়ে তাকে sudo দিন:
```bash
adduser deploy
usermod -aG sudo deploy
# নতুন user-এও SSH key কপি করুন
rsync --archive --chown=deploy:deploy ~/.ssh /home/deploy/
```
এবার `ssh deploy@142.93.1.5` দিয়ে ঢুকবেন, দরকারে `sudo` দেবেন।

### ধাপ ৪: system update

```bash
sudo apt update && sudo apt upgrade -y
```

### ধাপ ৫: Firewall (ufw) — শুধু দরকারি port খোলা রাখুন

```bash
sudo ufw allow OpenSSH      # port 22 — না দিলে নিজেই লক-আউট হবেন!
sudo ufw allow 80/tcp       # http
sudo ufw allow 443/tcp      # https
sudo ufw enable
sudo ufw status
```
🔴 **`ufw enable` দেওয়ার আগে অবশ্যই `allow OpenSSH` দিন** — নাহলে নিজের সার্ভার থেকে চিরতরে লক-আউট হয়ে যাবেন।

### ধাপ ৬ (ঐচ্ছিক, ভালো অভ্যাস): SSH আরও শক্ত করা

`/etc/ssh/sshd_config`-এ:
```
PermitRootLogin no
PasswordAuthentication no
```
তারপর `sudo systemctl restart ssh`। (আগে নিশ্চিত হোন key দিয়ে ঢুকতে পারছেন!) Bonus: **fail2ban** বসান (`sudo apt install fail2ban`) — বারবার ভুল login করলে IP block করে।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১৩. Runtime + database install <a id="s13"></a>

এবার app চালানোর জিনিসপত্র বসান। উদাহরণে: **Node.js backend + Postgres**।

### Node.js (nvm দিয়ে — version control ভালো)

```bash
# nvm-এর latest version দেখে নিন: github.com/nvm-sh/nvm/releases (এখন v0.40.5)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh | bash
source ~/.bashrc
nvm install 22        # current LTS নিন (Node 20 এখন EOL — নতুন security update পায় না)
node -v               # যাচাই
```
(Python হলে: `sudo apt install python3 python3-venv python3-pip`. .NET হলে Microsoft-এর apt repo যোগ করে `dotnet-sdk`।)

### Git দিয়ে কোড আনা

```bash
sudo apt install git -y
cd /home/deploy
git clone https://github.com/you/myapp.git
cd myapp/backend
npm install
npm run build      # থাকলে
```

### Postgres install

```bash
sudo apt install postgresql postgresql-contrib -y
sudo systemctl status postgresql     # চালু আছে কিনা
```
একটা database + user বানান:
```bash
sudo -u postgres psql
```
```sql
CREATE DATABASE myapp;
CREATE USER myapp_user WITH ENCRYPTED PASSWORD 'strong_password_here';
GRANT ALL PRIVILEGES ON DATABASE myapp TO myapp_user;
-- ⚠️ Postgres 15+ এ এটুকু যথেষ্ট নয়: নতুন user public schema-তে table বানাতে পারবে না।
-- DB-তে ঢুকে schema-র permission-ও দিতে হবে:
\c myapp
GRANT ALL ON SCHEMA public TO myapp_user;   -- বিকল্প: ALTER DATABASE myapp OWNER TO myapp_user;
\q
```
এখন connection string:
```
postgres://myapp_user:strong_password_here@localhost:5432/myapp
```
🟢 database একই সার্ভারে থাকলে host = `localhost` — বাইরে থেকে DB port (5432) খুলবেন না, নিরাপদ থাকে।

### App-এর env var

`.env` ফাইল বানান app folder-এ (🔴 এটা **git-এ commit করবেন না** — `.gitignore`-এ রাখুন):
```bash
# /home/deploy/myapp/backend/.env
DATABASE_URL=postgres://myapp_user:strong_password_here@localhost:5432/myapp
JWT_SECRET=<লম্বা random string>
NODE_ENV=production
PORT=3000
```

এবার হাতে চালিয়ে দেখুন কাজ করে কিনা: `node dist/server.js` → `http://142.93.1.5:3000`-এ (firewall-এ 3000 সাময়িক খুলে) সাড়া দেয় কিনা। কাজ করলে বন্ধ করুন — এবার একে **স্থায়ীভাবে চালু** রাখতে হবে।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১৪. App কে চালু রাখা — systemd / PM2 <a id="s14"></a>

আপনি `node server.js` দিয়ে চালালেন, কিন্তু SSH বন্ধ করলে বা server reboot হলে app বন্ধ। দরকার একটা **process manager** যে app-কে **সবসময় চালু রাখবে**, crash করলে **নিজে থেকে আবার চালু করবে**।

### উপায় ১: systemd (Linux-এর নিজস্ব, কিছু install লাগে না) — 🟢 সুপারিশ

একটা service ফাইল বানান:
```bash
sudo nano /etc/systemd/system/myapp.service
```
```ini
[Unit]
Description=MyApp backend
After=network.target postgresql.service

[Service]
Type=simple
User=deploy
WorkingDirectory=/home/deploy/myapp/backend
EnvironmentFile=/home/deploy/myapp/backend/.env
ExecStart=/home/deploy/.nvm/versions/node/v22.11.0/bin/node dist/server.js
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
(`ExecStart`-এ node-এর পুরো path দিন — `which node` দিয়ে বের করুন।)

চালু করুন:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp     # reboot-এও চালু হবে
sudo systemctl start myapp
sudo systemctl status myapp     # চলছে কিনা
journalctl -u myapp -f          # live log দেখা
```
এখন app crash করলে systemd ৫ সেকেন্ডে আবার চালু করবে; server reboot হলেও নিজে চালু হবে।

### উপায় ২: PM2 (Node-এর জনপ্রিয় tool)

```bash
npm install -g pm2
pm2 start dist/server.js --name myapp
pm2 startup      # reboot-এ auto-start সেট করে (যে command দেয়, চালান)
pm2 save
pm2 logs myapp   # log
pm2 restart myapp
```
PM2 সহজ ও Node-বান্ধব (cluster mode-এ multiple instance-ও চালায়)। systemd বেশি universal (যেকোনো ভাষার app)। **যেকোনো একটা** বেছে নিন।

> **এটাই সেই "process manager" ধারণা** ([৪ নং](#s4), point 7) — বাস্তবে এখানে। PaaS এটা লুকিয়ে করত; এখন আপনি নিজে করলেন।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১৫. Nginx reverse proxy <a id="s15"></a>

এখন app চলছে port 3000-এ। কিন্তু user তো `142.93.1.5:3000` টাইপ করবে না — সে চায় `https://myapp.com` (port 443)। আর frontend-ও serve করতে হবে। এই কাজটা করে **Nginx** — একটা **reverse proxy**।

```mermaid
flowchart LR
  U[User<br/>myapp.com:443] --> N[Nginx<br/>port 80/443]
  N -->|/ | S[Static frontend<br/>ফাইল]
  N -->|/api| B[Backend<br/>localhost:3000]
```

Nginx যা করে:
- port **80/443**-এ সব request নেয়।
- **HTTPS** সামলায় ([১৬ নং](#s16))।
- `/api/...` request → ভেতরের backend (`localhost:3000`)-এ পাঠায়।
- বাকি (`/`, `/about`) → frontend-এর static ফাইল serve করে।
- একটা IP-তে **অনেক site** চালাতে পারে (server block দিয়ে)।

### Install ও config

```bash
sudo apt install nginx -y
```

Frontend build সার্ভারে আনুন (local-এ `npm run build`, তারপর `dist/` folder সার্ভারে; বা সার্ভারেই build)। ধরা যাক ফাইল `/home/deploy/myapp/frontend/dist`-এ।

Config বানান:
```bash
sudo nano /etc/nginx/sites-available/myapp
```
```nginx
server {
    listen 80;
    server_name myapp.com www.myapp.com;

    # Frontend — static ফাইল
    root /home/deploy/myapp/frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;   # SPA — refresh-এ 404 এড়ায়
    }

    # Backend API — proxy to Node
    location /api/ {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        # app-এ WebSocket (Socket.IO, live chat) থাকলে এই দুটোও দিন:
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

Enable + test + reload:
```bash
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t          # config ঠিক আছে কিনা — সবসময় আগে test করুন
sudo systemctl reload nginx
```
এখন `http://myapp.com` খুললে frontend দেখাবে, `myapp.com/api/...` backend-এ যাবে। শুধু **HTTPS** বাকি।

🟢 `sudo nginx -t` — reload-এর আগে **সবসময়** চালান। ভুল config দিয়ে reload করলে site পড়ে যাবে।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১৬. Domain + free SSL (Let's Encrypt) <a id="s16"></a>

### ধাপ ১: domain-কে সার্ভারে point করা (DNS)

Domain provider-এর DNS setting-এ:
```
A record:   myapp.com       →  142.93.1.5   (আপনার VPS IP)
A record:   www.myapp.com   →  142.93.1.5
```
কয়েক মিনিট থেকে ঘণ্টাখানেকে propagate হবে। যাচাই: `dig myapp.com +short` — IP দেখাবে।

### ধাপ ২: ফ্রি HTTPS — Certbot (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d myapp.com -d www.myapp.com
```
> 🟢 **নোট:** EFF এখন certbot **snap** দিয়ে বসাতে বলে — `sudo snap install --classic certbot` — সবচেয়ে নতুন version পাওয়ার জন্য। উপরের apt package-ও কাজ করে, শুধু একটু পুরনো হতে পারে।

Certbot নিজে থেকে:
- Let's Encrypt থেকে ফ্রি certificate আনে,
- আপনার Nginx config **নিজে edit করে** HTTPS (443) যোগ করে,
- http (80) → https redirect বসিয়ে দেয়।

এবার `https://myapp.com` — 🔒 তালা এসে গেল।

### ধাপ ৩: auto-renew (certificate ৯০ দিনে শেষ হয়)

Certbot একটা timer বসিয়ে দেয় যা নিজে থেকে renew করে। যাচাই:
```bash
sudo certbot renew --dry-run
```

> **এটাই সেই HTTPS/SSL ধারণা** ([৪ নং](#s4), point 4)। PaaS এটা নিজে করত; VPS-এ Certbot দিয়ে আপনি করলেন — একবার করলেই ধারণাটা পাকা।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১৭. পুরো VPS deploy — এক জায়গায় (frontend+backend+db) <a id="s17"></a>

উপরের সব একসাথে করলে full-stack app VPS-এ live করার **পূর্ণ recipe**:

```mermaid
flowchart TB
  Dev[লোকাল কোড] -->|git push| GH[GitHub]
  GH -->|git pull| VPS
  subgraph VPS["VPS (Ubuntu, 142.93.1.5)"]
    NG[Nginx :80/:443<br/>+ SSL] --> FE[frontend/dist<br/>static ফাইল]
    NG --> BE[Node backend<br/>:3000 · systemd]
    BE --> PG[(Postgres<br/>localhost:5432)]
  end
  User --> NG
```

**পূর্ণ চেকলিস্ট (প্রথমবার):**
1. 🟢 VPS নিন, SSH-এ ঢুকুন, user + firewall setup ([১২](#s12))।
2. 🟢 Node/runtime + Postgres install, DB বানান ([১৩](#s13))।
3. 🟢 `git clone` → `npm install` → `npm run build` (backend ও frontend দুটোই)।
4. 🟢 `.env` বসান (DB URL, secret)। migration চালান।
5. 🟢 systemd service দিয়ে backend চালু রাখুন ([১৪](#s14))।
6. 🟢 Nginx দিয়ে frontend serve + `/api` proxy ([১৫](#s15))।
7. 🟢 DNS point করুন, Certbot দিয়ে HTTPS ([১৬](#s16))।

**পরের বার deploy (update) — সহজ:**
```bash
cd /home/deploy/myapp
git pull
cd backend && npm install && npm run build && sudo systemctl restart myapp
cd ../frontend && npm install && npm run build   # Nginx নতুন ফাইল serve করবে
```
এই কয়েকটা command রোজ চালানো ঝামেলা — তাই মানুষ এটাকে **script** বানায়, তারপর **CI/CD** দিয়ে অটো করে ফেলে (পর্ব ৫)। একটা সহজ deploy script:
```bash
#!/usr/bin/env bash
# deploy.sh — VPS-এ চালাবেন
set -e
cd /home/deploy/myapp
git pull
cd backend && npm ci && npm run build && sudo systemctl restart myapp
cd ../frontend && npm ci && npm run build
echo "Deployed ✓"
```

> এখন আপনি deployment-এর **পুরো নাড়িভুঁড়ি** জানেন। PaaS-এ ফিরে গেলে বুঝবেন platform ঠিক এই কাজগুলোই আপনার হয়ে করছিল। এই বোঝাপড়াটাই আসল অর্জন।

**পরের সমস্যা:** "আমার মেশিনে Node 20, সার্ভারে 18 — কোড ভাঙল।" এই "environment মেলে না" সমস্যা সমাধান করে **Docker** — পর্ব ৪।

[↑ সূচিপত্রে ফিরুন](#toc)

---

# ★ Capstone — React + Node + Postgres: সম্পূর্ণ deploy (শুরু → শেষ) <a id="capstone"></a>

তোমার হাতে তিনটা জিনিস: একটা **React** app (frontend), একটা **Node/Express** API (backend), আর একটা **Postgres** database। এই section-এ ঐ তিনটাকে **এক VPS-এ, শুরু থেকে শেষ পর্যন্ত** live করি — উপরের §১১–§১৭ এর সব একটা টানা recipe-তে সাজানো, কিছু বাদ নেই। copy-paste করে এগোতে পারবে।

> এটা **raw route** (VPS, নিজে হাতে)। একই app PaaS/Docker/CI-CD-তে কীভাবে যায় — শেষে [ছোট table](#capstone-other) আছে।

### কী কোথায় বসবে (এক ডোমেইন → CORS লাগে না)

```mermaid
flowchart TB
  U["User — https://myapp.com"] --> NG[Nginx :443<br/>+ SSL]
  NG -->|/ page| FE[React build<br/>frontend/dist]
  NG -->|/api| BE[Node/Express<br/>127.0.0.1:3000]
  BE --> PG[(Postgres<br/>localhost:5432)]
```

মূল চাল: **সব এক ডোমেইনে** (`myapp.com`)। Nginx `/` দিলে React দেয়, `/api` দিলে Node-এ পাঠায়। যেহেতু frontend আর backend **একই origin**, browser-এ **CORS সমস্যা হয় না** — React থেকে সরাসরি `/api/...` (relative path) ডাকতে পারো। (PaaS-এ frontend আর backend আলাদা ডোমেইনে বসে বলে ওখানে CORS লাগত — [§8](#s8)।)

---

### ধাপ ০ — ধরে নিচ্ছি

- একটা Ubuntu VPS আছে, [§১২](#s12) এর মতো user (`deploy`) + firewall + SSH রেডি।
- তিনটা জিনিস git-এ আছে (এক repo-তে `frontend/` + `backend/`, বা আলাদা দুই repo)।
- backend-এ Postgres schema বানানোর একটা migration আছে (raw `.sql` ফাইল, বা Prisma/Knex migration)।

### ধাপ ১ — কোড সার্ভারে আনা

```bash
ssh deploy@142.93.1.5
cd /home/deploy
git clone https://github.com/you/myapp.git
cd myapp
```

### ধাপ ২ — Postgres: database + user + schema + migration

```bash
sudo apt install postgresql postgresql-contrib -y
sudo -u postgres psql
```
```sql
CREATE DATABASE myapp;
CREATE USER myapp_user WITH ENCRYPTED PASSWORD 'strong_password';
GRANT ALL PRIVILEGES ON DATABASE myapp TO myapp_user;
\c myapp
GRANT ALL ON SCHEMA public TO myapp_user;   -- Postgres 15+ এ জরুরি (নাহলে table বানাতে পারবে না)
\q
```
এবার তোমার schema/migration চালাও (তুমি যেটা use করো):
```bash
# (a) raw SQL ফাইল হলে:
psql "postgres://myapp_user:strong_password@localhost:5432/myapp" -f backend/migrations/001_init.sql

# (b) Prisma হলে:
cd backend && DATABASE_URL="postgres://myapp_user:strong_password@localhost:5432/myapp" npx prisma migrate deploy

# (c) Knex হলে:
cd backend && npx knex migrate:latest
```

### ধাপ ৩ — Backend (Node/Express) চালু

```bash
cd /home/deploy/myapp/backend
npm ci
npm run build          # TypeScript হলে; plain JS হলে বাদ দাও
```
`.env` বানাও (🔴 git-এ নয় — `.gitignore`-এ রাখো):
```bash
# /home/deploy/myapp/backend/.env
DATABASE_URL=postgres://myapp_user:strong_password@localhost:5432/myapp
JWT_SECRET=<লম্বা random string>
NODE_ENV=production
PORT=3000
```
🟢 Express কোডে port অবশ্যই env থেকে পড়ো: `app.listen(process.env.PORT || 3000)` — [§8](#s8)।

systemd দিয়ে সবসময় চালু রাখো ([§১৪](#s14)):
```bash
sudo nano /etc/systemd/system/myapp.service
```
```ini
[Unit]
Description=MyApp API
After=network.target postgresql.service

[Service]
Type=simple
User=deploy
WorkingDirectory=/home/deploy/myapp/backend
EnvironmentFile=/home/deploy/myapp/backend/.env
ExecStart=/home/deploy/.nvm/versions/node/v22.11.0/bin/node dist/server.js
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now myapp
curl localhost:3000/health      # {"status":"ok"} আসছে কিনা দেখো
```

### ধাপ ৪ — Frontend (React) build

**সবচেয়ে জরুরি কথা:** React-এর env var **build-এর সময়** কোডে বসে যায় (runtime-এ না)। যেহেতু এক ডোমেইনে proxy করছি, API base রাখো **relative** — শুধু `/api`:
```bash
cd /home/deploy/myapp/frontend
echo 'VITE_API_URL=/api' > .env.production    # Vite; CRA হলে REACT_APP_API_URL
npm ci
npm run build          # dist/ বানায়
```
React কোডে fetch: `` fetch(`${import.meta.env.VITE_API_URL}/notes`) `` → `/api/notes` হবে → Nginx সেটা Node-এ পাঠাবে। **CORS লাগবে না।**

### ধাপ ৫ — Nginx: React serve + /api proxy

```bash
sudo apt install nginx -y
sudo nano /etc/nginx/sites-available/myapp
```
```nginx
server {
    listen 80;
    server_name myapp.com www.myapp.com;

    root /home/deploy/myapp/frontend/dist;
    index index.html;

    # React (SPA) — refresh-এ 404 এড়ায়
    location / {
        try_files $uri $uri/ /index.html;
    }

    # /api → Node backend
    location /api/ {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
🟢 **path মেলানো জরুরি:** তোমার Express route যদি `/api/...` দিয়ে শুরু হয় (যেমন `app.use('/api/notes', ...)`) — তাহলে উপরেরটা ঠিক আছে। যদি backend route শুধু `/notes` হয়, তাহলে `proxy_pass http://localhost:3000/;` (শেষে `/`) দাও — Nginx তখন `/api` অংশ কেটে Node-এ পাঠাবে।
```bash
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

### ধাপ ৬ — Domain + HTTPS

DNS-এ `myapp.com` ও `www` → VPS IP (A record, [§১৬](#s16))। তারপর:
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d myapp.com -d www.myapp.com
```
এখন `https://myapp.com` — 🔒 live।

### ধাপ ৭ — শেষ যাচাই (end-to-end)

```bash
curl https://myapp.com/api/health        # backend ঠিক আছে?
curl -I https://myapp.com                 # 200 + React index আসছে?
```
Browser-এ `https://myapp.com` খোলো → React app দেখাচ্ছে → login/data কাজ করছে → DevTools → Network-এ `/api/...` call **200** আসছে কিনা দেখো।

### পরের বার update (এক command)

VPS-এ একটা `deploy.sh`:
```bash
#!/usr/bin/env bash
set -e
cd /home/deploy/myapp
git pull
cd backend && npm ci && npm run build && npx prisma migrate deploy && sudo systemctl restart myapp
cd ../frontend && npm ci && npm run build
echo "Deployed ✓"
```
(migration line তোমার tool অনুযায়ী বদলাও; migration না থাকলে ঐ অংশ বাদ দাও।) এই script-টাই পরে **CI/CD** দিয়ে অটো হয় — [§২৪](#s24)।

### এই stack-এর সব env var (এক নজরে)

| env var | কোথায় | মান |
|---|---|---|
| `VITE_API_URL` | frontend build | `/api` (same-domain) |
| `DATABASE_URL` | backend `.env` | `postgres://...@localhost:5432/myapp` |
| `JWT_SECRET` | backend `.env` | লম্বা random string |
| `PORT` | backend `.env` | `3000` |
| `NODE_ENV` | backend `.env` | `production` |

### React + Node + Postgres-এ যে ভুলগুলো সবচেয়ে বেশি হয়

- 🔴 React-এ API URL **runtime-এ বদলাতে চাওয়া** — হয় না; build-এর সময় fix হয়ে যায়। আলাদা environment হলে আলাদা build লাগে।
- 🔴 `VITE_` (বা CRA-তে `REACT_APP_`) prefix ভুলে যাওয়া — তাহলে var browser-এ পৌঁছায় না।
- 🔴 Postgres 15+ এ schema grant না দেওয়া → `permission denied for schema public`।
- 🔴 Express-এর `/api` prefix আর Nginx `location /api/` না মেলা → 404।
- 🔴 systemd ছাড়া `node server.js` → reboot/crash-এ app মরে থাকে।
- 🔴 `.env` git-এ push → secret ফাঁস ([§২৮](#s28))।

<a id="capstone-other"></a>
### একই app — অন্য রাস্তায় (all deployment process এক টেবিলে)

| রাস্তা | Frontend (React) | Backend (Node) | Postgres | বিস্তারিত |
|---|---|---|---|---|
| **PaaS** | Vercel / Netlify | Render / Railway | Neon / Supabase | [পর্ব ২](#s6) |
| **VPS (এই capstone)** | Nginx + dist | systemd + Node | সার্ভারে নিজে | পর্ব ৩ |
| **Docker** | nginx container | node container | postgres container | [পর্ব ৪](#s18) |
| **CI/CD** | push → auto build + deploy | push → image → deploy | managed / RDS | [পর্ব ৫](#s24) |

তিনটা অংশ (React / Node / Postgres) সব রাস্তায় **একই থাকে** — শুধু **কে host করে আর কে deploy চালায়** বদলায়। raw-তে সব তুমি করো; উপরের দিকে যত যাবে, tool তত বেশি করে দেয়।

[↑ সূচিপত্রে ফিরুন](#toc)

---

# পর্ব ৪ — Docker + Containers

> লক্ষ্য: app-কে একটা "box"-এ প্যাক করা যাতে আপনার ল্যাপটপ, বন্ধুর ল্যাপটপ, আর সার্ভার — সবখানে **হুবহু একইভাবে** চলে। "আমার মেশিনে তো চলছিল" সমস্যার শেষ।

## ১৮. Container কী, কেন <a id="s18"></a>

আপনার মেশিনে Node 20, সার্ভারে Node 18; আপনার মেশিনে একটা library আছে, সার্ভারে নেই — কোড ভাঙে। কারণ **environment আলাদা**। **Container** এই সমস্যা মেটায়: app + তার Node version + সব library + config — সব একসাথে একটা image-এ প্যাক করে। সেই image যেখানেই চালান, ভেতরটা **একদম এক**।

```
VM (ভারী)                          Container (হালকা)
┌───────────────┐                  ┌───────────────┐
│ App           │                  │ App           │
│ Libraries     │                  │ Libraries     │
│ পুরো OS       │   ← ভারী, ধীর     │ (OS শেয়ার করে)│  ← হালকা, দ্রুত
│ Hypervisor    │                  │ Docker engine │
└───────────────┘                  └───────────────┘
```

**দুটো শব্দ আলাদা করুন:**
- **Image** = রেসিপি + জমানো সব উপকরণ (একটা স্থির প্যাকেজ)।
- **Container** = সেই image চালু করা একটা চলমান কপি। এক image থেকে অনেক container।

*উদাহরণ: image = রান্নার রেসিপি বইয়ের ছবি; container = সেই রেসিপি দিয়ে বানানো আসল খাবারের প্লেট।*

**কেন শিখবেন:**
- environment সব জায়গায় এক — dev, staging, prod।
- team-এর সবাই এক জিনিস চালায়।
- CI/CD আর cloud (ECS, Kubernetes) container-ভিত্তিক — production-এ প্রায় অবশ্যম্ভাবী।

**Install:** নিজের মেশিনে **Docker Desktop** (Mac/Windows) বা সার্ভারে Docker Engine:
```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER   # sudo ছাড়া docker চালাতে; পুনরায় login
docker run hello-world          # যাচাই
```
> 🟢 **নোট:** `get.docker.com` script official ও দ্রুত, কিন্তু Docker docs বলে **production-এ সরাসরি pipe না করে** আগে download করে দেখে নেওয়া ভালো: `curl -fsSL https://get.docker.com -o get-docker.sh` → (ফাইলটা দেখুন) → `sudo sh get-docker.sh`।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ১৯. Dockerfile — frontend ও backend <a id="s19"></a>

**Dockerfile** = একটা text ফাইল, যেখানে ধাপে ধাপে লেখা কীভাবে app-এর image বানাতে হবে।

### Backend Dockerfile (Node/Express) — multi-stage, ছোট image

```dockerfile
# ---- build stage ----
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# ---- run stage ----  (শুধু দরকারিটুকু, image ছোট থাকে)
FROM node:22-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=build /app/dist ./dist
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

**গুরুত্বপূর্ণ লাইনগুলো:**
- `FROM node:22-alpine` — ভিত্তি image (alpine = ছোট Linux)।
- **multi-stage** — build-এর ভারী জিনিস বাদ দিয়ে শুধু run-এর অংশ রাখে; image ছোট ও নিরাপদ।
- `COPY package*.json` **আগে**, `npm ci` তারপর `COPY . .` — এই ক্রমে দিলে কোড বদলালেও dependency layer cache থাকে, build দ্রুত হয়।
- `EXPOSE 3000` — container কোন port-এ শোনে।
- `CMD` — container চালু হলে কোন command চলবে।

একটা `.dockerignore`ও দিন (image হালকা রাখে):
```
node_modules
.git
.env
dist
```

### Frontend Dockerfile (React build → Nginx দিয়ে serve)

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build          # dist/ বানায়

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
# SPA routing-এর জন্য নিজের nginx.conf দিতে পারেন
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Build + run হাতে

```bash
docker build -t myapp-backend ./backend
docker run -p 3000:3000 --env-file backend/.env myapp-backend
# -p 3000:3000 = হোস্টের 3000 → container-এর 3000
```
`http://localhost:3000` — container-এ চলছে। যেকোনো মেশিনে এই image চালালে **একই** ফল।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২০. docker-compose — পুরো stack এক ফাইলে <a id="s20"></a>

Full-stack-এ তিন container: frontend, backend, database। হাতে তিনটা `docker run` + network জোড়া দেওয়া ঝামেলা। **docker-compose** এক YAML ফাইলে সব বর্ণনা করে, এক command-এ সব চালায়।

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: myapp_user
      POSTGRES_PASSWORD: strong_password_here
      POSTGRES_DB: myapp
    volumes:
      - dbdata:/var/lib/postgresql/data     # data টিকে থাকে
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myapp_user"]
      interval: 5s
      retries: 5

  backend:
    build: ./backend
    environment:
      DATABASE_URL: postgres://myapp_user:strong_password_here@db:5432/myapp
      JWT_SECRET: ${JWT_SECRET}
      NODE_ENV: production
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "3000:3000"

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  dbdata:
```

**খেয়াল করুন:**
- backend-এর `DATABASE_URL`-এ host = **`db`** (localhost নয়!) — compose-এ প্রতিটা service অন্যকে তার **নাম দিয়ে** খুঁজে পায়, একই private network-এ থাকে।
- **`volumes: dbdata`** — এটা ছাড়া container মুছলে database-এর সব data চলে যাবে। volume data-কে বাঁচিয়ে রাখে।
- **`depends_on` + `healthcheck`** — db পুরো তৈরি হওয়ার আগে backend চালু হবে না।
- `${JWT_SECRET}` — আসল secret একই folder-এর `.env` ফাইল থেকে আসে (git-এ নয়)।

**চালানো:**
```bash
docker compose up -d --build     # সব build + চালু, background-এ
docker compose logs -f backend   # log
docker compose ps                # কী চলছে
docker compose down              # সব বন্ধ (down -v দিলে volume-ও মুছবে — সাবধান)
```

এক command-এ পুরো full-stack app চালু। এই একই `docker-compose.yml` নিজের মেশিনে আর সার্ভারে — **হুবহু এক**।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২১. Image registry (Docker Hub / GHCR) <a id="s21"></a>

Image সার্ভারে নেওয়ার দুই উপায়: (ক) সার্ভারে কোড নিয়ে ওখানে build, (খ) 🟢 নিজের মেশিন/CI-তে build করে একটা **registry**-তে push, সার্ভারে শুধু **pull** — এটাই ভালো ও দ্রুত।

**Registry** = image রাখার জায়গা (GitHub-এর মতো, কিন্তু কোডের বদলে image)। জনপ্রিয়: **Docker Hub**, **GHCR** (GitHub Container Registry), **AWS ECR**।

```bash
# tag + login + push (GHCR উদাহরণ)
docker build -t ghcr.io/you/myapp-backend:1.0 ./backend
echo $GITHUB_TOKEN | docker login ghcr.io -u you --password-stdin
docker push ghcr.io/you/myapp-backend:1.0

# সার্ভারে:
docker pull ghcr.io/you/myapp-backend:1.0
docker run -d -p 3000:3000 --env-file .env ghcr.io/you/myapp-backend:1.0
```

🟢 **tag-এ version দিন** (`:1.0`, বা git commit hash) — `:latest` ছাড়া। তাহলে কোন version চলছে জানবেন, আর দরকারে আগের version-এ **rollback** করতে পারবেন ([৩২ নং](#s32))।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২২. VPS-এ Docker দিয়ে deploy <a id="s22"></a>

পর্ব ৩-এর VPS + পর্ব ৪-এর Docker মিলিয়ে — সবচেয়ে বাস্তব "নিজে চালানো" setup:

1. VPS-এ Docker + docker-compose install ([১৮](#s18))।
2. সার্ভারে `docker-compose.yml` + `.env` রাখুন (কোড clone করা লাগে না যদি registry থেকে image টানেন)।
3. `docker compose pull && docker compose up -d` — নতুন version live।
4. **HTTPS** — দুই উপায়:
   - compose-এ **Caddy** যোগ করুন — Caddy নিজে থেকে Let's Encrypt SSL করে (Nginx + Certbot-এর সহজ বিকল্প), অথবা
   - host-এ Nginx + Certbot রেখে container-এ proxy করুন ([১৫](#s15)–[১৬](#s16))।

Caddy দিয়ে auto-HTTPS reverse proxy (compose-এ যোগ):
```yaml
  caddy:
    image: caddy:alpine
    ports: ["80:80", "443:443"]
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddydata:/data
    depends_on: [backend, frontend]
```
`Caddyfile`:
```
myapp.com {
    handle /api/* {
        reverse_proxy backend:3000
    }
    handle {
        reverse_proxy frontend:80
    }
}
```
ব্যস — Caddy `myapp.com`-এর জন্য নিজে থেকে ফ্রি SSL এনে HTTPS চালু করে দেবে।

> এখন update মানে শুধু: নতুন image push → সার্ভারে `docker compose pull && up -d`। পরের ধাপ: এই কাজটাও **হাতে না করে** git push-এ অটো করা — CI/CD, পর্ব ৫।

[↑ সূচিপত্রে ফিরুন](#toc)

---

# পর্ব ৫ — CI/CD + Cloud (production-grade)

> লক্ষ্য: `git push` করলেই নিজে নিজে test → build → deploy। হাতে কিছু করা লাগবে না। আর cloud (AWS/GCP)-এর মূল service-গুলো চেনা।

## ২৩. CI/CD কী — pipeline-এর গঠন <a id="s23"></a>

এতক্ষণ deploy করতে হাতে command চালাচ্ছিলেন। ভুল হওয়ার ঝুঁকি, সময় নষ্ট, ভুলে যাওয়ার ভয়। **CI/CD** এই পুরোটা **অটোমেট** করে — একটা **pipeline** যেটা প্রতিবার code push-এ নিজে চলে।

- **CI (Continuous Integration):** push করলেই নিজে নিজে — dependency install → **test চালানো** → **build**। কোড ভাঙলে সাথে সাথে জানায়, merge-এর আগেই।
- **CD (Continuous Delivery/Deployment):** CI পাস করলে নিজে নিজে server/cloud-এ **deploy**।

```mermaid
flowchart LR
  A[git push] --> B[Checkout কোড]
  B --> C[Install deps]
  C --> D[Lint + Test]
  D -->|fail| X[থামো · জানাও]
  D -->|pass| E[Build<br/>docker image]
  E --> F[Push to registry]
  F --> G[Deploy<br/>server/cloud]
  G --> H[Health check]
```

**জনপ্রিয় CI/CD tool:** **GitHub Actions** (repo-র সাথেই, সবচেয়ে সহজ শুরু), GitLab CI, CircleCI, Jenkins (self-hosted, পুরনো/বড় org)।

🟢 শেখা শুরু করুন **GitHub Actions** দিয়ে — কোড GitHub-এ থাকলে আলাদা কিছু লাগে না।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২৪. GitHub Actions — build → test → deploy <a id="s24"></a>

Repo-তে `.github/workflows/` folder-এ একটা YAML ফাইল দিলেই pipeline তৈরি।

### সহজ CI (test + build চালায়, প্রতি push-এ)

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run lint --if-present
      - run: npm test --if-present
      - run: npm run build
```
এখন প্রতিটা push/PR-এ GitHub নিজে নিজে test + build চালাবে; fail করলে লাল ক্রস দেখাবে।

### CD — build image → push → VPS-এ deploy

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:            # GHCR-এ push করতে বাধ্যতামূলক
      contents: read
      packages: write       # না দিলে push-এ 403 — নতুন repo-তে GITHUB_TOKEN default read-only
    steps:
      - uses: actions/checkout@v4

      # 1) Docker image build + GHCR-এ push
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          context: ./backend
          push: true
          tags: ghcr.io/${{ github.repository }}/backend:${{ github.sha }}

      # 2) VPS-এ SSH দিয়ে নতুন image টেনে চালু
      - name: Deploy to VPS
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USER }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd /home/deploy/myapp
            docker compose pull
            docker compose up -d
            docker image prune -f
```

**Secrets:** `secrets.VPS_HOST`, `VPS_SSH_KEY`, ইত্যাদি — GitHub repo-র **Settings → Secrets and variables → Actions**-এ বসান। 🔴 কখনো YAML-এ সরাসরি password/key লিখবেন না — সবসময় `secrets.`।

> **Action version নিয়ে:** উপরের `@v4`/`@v3`/`@v6`/`@v1` tag-গুলো এখনো কাজ করে, কিন্তু মাঝে মাঝে নতুন major বের হয় (২০২৬-এর মাঝামাঝি live: checkout `v5+`, setup-node `v6`, login-action `v4`, build-push `v7`)। `@v4` লিখলে ঐ major-এর latest patch নিজে আসে; সবচেয়ে নতুন major জানতে [GitHub Marketplace](https://github.com/marketplace?type=actions) দেখুন — tutorial-এর number-এ আটকে থাকবেন না।

এবার `git push origin main` → GitHub নিজে নিজে test → image build → registry-তে push → VPS-এ SSH দিয়ে নতুন version চালু। **আপনি শুধু কোড লিখলেন।** এটাই CI/CD-র আসল শক্তি।

> খেয়াল করুন — CD আসলে পর্ব ৩/৪-এ হাতে করা কাজগুলোই (pull, up) অটো করছে। CI/CD জাদু নয়, **আপনার হাতের কাজের স্ক্রিপ্ট**। তাই আগে হাতে শেখা জরুরি ছিল।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২৫. Cloud providers (AWS/GCP) — কোন service কী কাজ <a id="s25"></a>

VPS একটা খালি সার্ভার। **Cloud** (AWS, GCP, Azure) দেয় শত শত **আলাদা service** — সার্ভার, database, storage, network, monitoring — সব managed, চাহিদামতো বড়/ছোট। প্রথমে ভয় লাগে কারণ নাম অনেক; কিন্তু full-stack-এর জন্য গুটিকয়েক জানলেই চলে।

| দরকার | AWS | GCP | কাজ |
|---|---|---|---|
| খালি সার্ভার (VPS-এর মতো) | **EC2** | Compute Engine | নিজে সব বসান |
| container চালানো (managed) | **ECS** / Fargate | Cloud Run / GKE | Docker image চালায়, সার্ভার সামলাতে হয় না |
| Managed Postgres | **RDS** | Cloud SQL | database, auto-backup |
| File/object storage | **S3** | Cloud Storage | ছবি, ফাইল, static site |
| CDN (দ্রুত global delivery) | **CloudFront** | Cloud CDN | static + cache |
| Serverless function | **Lambda** | Cloud Functions | কোড চালান, সার্ভার নেই |
| DNS | **Route 53** | Cloud DNS | domain |
| Secrets | Secrets Manager | Secret Manager | নিরাপদ env |
| Load balancer | **ELB/ALB** | Cloud Load Balancing | ট্রাফিক ভাগ করা |

**দুটো মন-মডেল:**
- **"আমি সার্ভার চালাই"** (IaaS): EC2 — VPS-এর মতো, কিন্তু cloud-এর সব service হাতের কাছে। পর্ব ৩-এর সব জ্ঞান এখানে খাটে।
- **"আমি শুধু container/কোড দিই"** (managed): **Cloud Run** (GCP) বা **ECS Fargate** (AWS) — Docker image দিন, তারা চালায়, scale করে; সার্ভার আপনি দেখেনও না। PaaS-এর মতো, কিন্তু cloud-এর ভেতরে।

🟢 শেখার সহজ cloud entry: **GCP Cloud Run** — Docker image দিলেই URL + HTTPS + auto-scale, EC2/ECS/k8s-এর জটিলতা ছাড়াই। (AWS-এর **App Runner** একই কাজ করত, কিন্তু এটা এখন **নতুন customer নিচ্ছে না** — তাই AWS-এ থাকলে **ECS Fargate** ধরুন।)

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২৬. AWS-এ deploy — কয়েকটা রাস্তা <a id="s26"></a>

একই full-stack app AWS-এ কয়েকভাবে বসানো যায় — সহজ থেকে জটিল:

**রাস্তা A — সহজ, container:**
```
Frontend  → S3 + CloudFront   (static ফাইল, global CDN, সস্তা)
Backend   → ECS Fargate  (Docker image → auto scale; App Runner এখন নতুন customer নিচ্ছে না)
Database  → RDS Postgres
Secrets   → Secrets Manager / SSM Parameter Store
```
🟢 শেখার জন্য ও অধিকাংশ প্রোডাক্টের জন্য এই combo যথেষ্ট।

**রাস্তা B — EC2 (VPS-এর মতো, পূর্ণ নিয়ন্ত্রণ):**
পর্ব ৩ হুবহু, শুধু VPS-এর জায়গায় EC2। Docker + compose (পর্ব ৪) EC2-তে চালান, RDS আলাদা database হিসেবে। CI/CD (পর্ব ৫) দিয়ে auto-deploy।

**রাস্তা C — ECS/Kubernetes (বড় স্কেল):**
অনেক container, auto-scaling, rolling update, service discovery — ECS বা EKS (managed k8s)। জটিল; দরকার না হলে এড়িয়ে চলুন ([২৭](#s27))।

### Frontend-কে S3 + CloudFront-এ (খুব common)

```bash
aws s3 sync ./dist s3://my-frontend-bucket --delete
aws cloudfront create-invalidation --distribution-id ABC123 --paths "/*"
```
CloudFront ফাইলগুলো global edge-এ cache করে — user যেখানেই থাক, কাছের জায়গা থেকে দ্রুত পায়। HTTPS free (ACM certificate)।

> **সৎ পরামর্শ:** শেখার শুরুতে পুরো AWS-এ ঝাঁপ দেবেন না। আগে PaaS/VPS-এ app live করুন, তারপর AWS-এর **এক-দুইটা service** (S3, RDS) দিয়ে শুরু করুন। AWS-এর ব্যাপ্তি বিশাল — একদিনে হবে না, দরকারও নেই।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২৭. Kubernetes — কখন লাগে, basics (সৎভাবে) <a id="s27"></a>

**Kubernetes (k8s)** = অনেকগুলো container চালানো, scale করা, crash হলে replace করা, update rolling ভাবে দেওয়া — সব **অটো** সামলানোর একটা system। শক্তিশালী, কিন্তু **জটিল**।

**মূল ধারণা (এক লাইনে):**
- **Pod** — এক বা কয়েকটা container একসাথে (ক্ষুদ্রতম একক)।
- **Deployment** — "আমি এই image-এর ৩টা কপি চাই" — k8s বজায় রাখে।
- **Service** — pod-গুলোর সামনে একটা স্থির address + load balance।
- **Ingress** — বাইরের HTTP/HTTPS ট্রাফিক ভেতরের service-এ পাঠায় (Nginx proxy-র k8s সংস্করণ)।
- **ConfigMap / Secret** — config ও গোপন মান।

```mermaid
flowchart TB
  I[Ingress<br/>HTTPS] --> S[Service]
  S --> P1[Pod: backend]
  S --> P2[Pod: backend]
  S --> P3[Pod: backend]
  P1 & P2 & P3 --> DB[(managed DB<br/>k8s-এর বাইরে)]
```

**কখন k8s লাগে:** অনেক microservice, বড় team, বিশাল/অসম traffic, multi-region, ঘনঘন rolling deploy।

🔴 **কখন লাগে না (বেশিরভাগ ক্ষেত্রে):** ছোট/মাঝারি app, একটা backend + একটা frontend, ছোট team। k8s তখন **অতিরিক্ত জটিলতা** — App Runner / Cloud Run / ECS Fargate / এমনকি একটা ভালো VPS-ই যথেষ্ট।

> **সৎ কথা:** k8s আছে বলেই আপনার লাগবে — এটা ভুল ধারণা। আগে পর্ব ২–৫ শক্ত করুন। k8s **সবার শেষে**, যখন সত্যিই scale-এর সমস্যা আসবে। CV-তে ভালো দেখায় বলে শুরুতেই এতে সময় ঢালবেন না।

[↑ সূচিপত্রে ফিরুন](#toc)

---

# পর্ব ৬ — Production-এ যা না জানলেই নয়

> রাস্তা যেটাই হোক (PaaS/VPS/Docker/cloud), এই বিষয়গুলো সব জায়গায় লাগে। এগুলো না জানলে app "চলে" কিন্তু "টেকে না"।

## ২৮. Secrets ও environment management <a id="s28"></a>

**Secret** = database password, API key, JWT secret — যা ফাঁস হলে বিপদ।

🟢 **করুন:**
- সব secret **environment variable**-এ, কোডের বাইরে।
- প্রতি environment-এ আলাদা মান (dev/staging/prod)।
- production secret **platform-এর secret manager**-এ (PaaS dashboard, GitHub Secrets, AWS Secrets Manager, `.env` file সার্ভারে `chmod 600`)।
- একটা `.env.example` রাখুন (নাম আছে, মান নেই) — team জানবে কী কী লাগে।
- secret বদলানোর (rotate) একটা পথ রাখুন।

🔴 **করবেন না:**
- secret কোডে hardcode।
- `.env` **git-এ commit** (সবচেয়ে common ভুল — `.gitignore`-এ রাখুন)। ভুলে commit হলে key **এখনই বদলান**, history থেকে মুছেও পুরনো key মৃত ধরুন।
- একই secret সব environment-এ শেয়ার।

ভুলে GitHub-এ key push হলে ধরার tool: **git-secrets**, **gitleaks**, GitHub-এর নিজের **secret scanning**।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ২৯. Domain, DNS, CDN <a id="s29"></a>

**DNS record** যেগুলো বারবার লাগবে:

| Record | কাজ | উদাহরণ |
|---|---|---|
| **A** | নাম → IPv4 | `myapp.com → 142.93.1.5` |
| **AAAA** | নাম → IPv6 | `myapp.com → 2001:db8::1` |
| **CNAME** | নাম → আরেক নাম | `www → myapp.com` |
| **MX** | ইমেইল সার্ভার | ইমেইলের জন্য |
| **TXT** | যাচাই/নিরাপত্তা | domain verify, SPF |

- **TTL** — record কতক্ষণ cache থাকে। বদলানোর আগে TTL কমিয়ে দিলে দ্রুত propagate হয়।
- **propagation** — DNS বদল সব জায়গায় ছড়াতে কয়েক মিনিট–কয়েক ঘণ্টা। যাচাই: `dig myapp.com +short`।

**CDN (Content Delivery Network)** — আপনার static ফাইল (JS, CSS, ছবি) পৃথিবীর নানা জায়গায় cache করে রাখে; user কাছের জায়গা থেকে দ্রুত পায়। উদাহরণ: **Cloudflare**, CloudFront। 🟢 frontend-এর সামনে একটা CDN রাখলে গতি অনেক বাড়ে, সার্ভারের চাপ কমে। Cloudflare-এর ফ্রি plan-এ CDN + DDoS সুরক্ষা + DNS একসাথে পাওয়া যায়।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩০. Monitoring, logs, health check <a id="s30"></a>

Deploy শেষ ≠ কাজ শেষ। app **এখন চলছে কিনা, ঠিকঠাক চলছে কিনা** — জানতে হবে।

**১) Health check endpoint** — backend-এ একটা সহজ route:
```js
app.get('/health', (req, res) => res.json({ status: 'ok' }));
```
Load balancer / uptime monitor এটা বারবার হিট করে দেখে app বেঁচে আছে কিনা। ব্যর্থ হলে alert / restart।

**২) Uptime monitoring** — বাইরে থেকে কেউ (UptimeRobot, Better Stack — ফ্রি tier আছে) প্রতি মিনিটে site চেক করে; down হলে ইমেইল/SMS পাঠায়।

**৩) Logs** — কী ঘটছে দেখার জানালা:
- VPS: `journalctl -u myapp -f` (systemd), `pm2 logs`, `docker compose logs -f`।
- PaaS/cloud: dashboard-এ log পাতা।
- 🟢 structured log (JSON) + একটা log service (Better Stack, Grafana Loci, Datadog) — খোঁজা সহজ হয়।

**৪) Error tracking** — **Sentry** (ফ্রি tier) বসান — production-এ কোনো user-এর কাছে error হলে stack trace সহ আপনাকে জানায়। খুব কাজের।

**৫) Metrics** — CPU, memory, request/সেকেন্ড, response time। Prometheus + Grafana (self-host) বা cloud-এর built-in (CloudWatch)।

🟢 minimum production setup: **health check + uptime monitor + Sentry**। এটুকু থাকলেই app মরে গেলে আপনি user-এর আগে জানবেন।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩১. Database migration ও backup <a id="s31"></a>

### Migration — schema বদলানো নিরাপদে

Code বদলালে প্রায়ই database-এর গঠনও বদলায় (নতুন টেবিল/কলাম)। এটা হাতে SQL চালিয়ে নয়, **migration** দিয়ে — version-controlled, repeatable script।

```bash
# Prisma উদাহরণ
npx prisma migrate dev --name add_orders_table   # dev-এ বানান
npx prisma migrate deploy                         # prod-এ চালান (deploy-এর সময়)
```
(অন্য tool: Drizzle, Knex, TypeORM, Alembic (Python), EF Core (.NET), Flyway/Liquibase।)

🟢 migration কে **deploy pipeline-এর অংশ** করুন — deploy করার সময় নিজে চলবে।
🔴 production database-এ হাতে `ALTER TABLE` চালিয়ে schema বদলাবেন না — track থাকবে না, team-এ মিলবে না।
🟢 migration হতে হবে **backward-compatible** যাতে zero-downtime deploy-এ পুরনো+নতুন কোড দুটোই চলে (আগে কলাম যোগ করুন, পরে পুরনো কলাম বাদ দিন — এক ধাপে নয়)।

### Backup — সবচেয়ে অবহেলিত, সবচেয়ে জরুরি

Data হারালে ব্যবসা শেষ। **Backup ছাড়া production চালাবেন না।**

- 🟢 managed DB (RDS, Supabase, Neon) — **auto-backup** থাকে, শুধু চালু আছে নিশ্চিত করুন + retention সেট করুন।
- self-host Postgres হলে নিজে নিন:
  ```bash
  pg_dump -U myapp_user myapp | gzip > backup_$(date +%F).sql.gz
  ```
  একটা cron-এ রোজ চালিয়ে অন্য জায়গায় (S3) রাখুন।
- 🟢 **restore টেস্ট করুন** — backup আছে কিন্তু restore হয় না, এমন হলে backup অর্থহীন। মাঝেমধ্যে একটা restore চালিয়ে দেখুন।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩২. Zero-downtime deploy ও rollback <a id="s32"></a>

**সমস্যা:** নতুন version deploy করার সময় app কয়েক সেকেন্ড বন্ধ থাকলে user error দেখে। **Zero-downtime deploy** এটা এড়ায়।

**মূল কৌশল — নতুন চালু করার পর পুরনো বন্ধ করা (কখনো উল্টো নয়):**

```mermaid
flowchart LR
  LB[Load balancer / proxy] --> Old[পুরনো v1<br/>চলছে]
  LB -.নতুন চালু.-> New[নতুন v2]
  New -->|health OK| Switch[traffic v2-তে সরাও]
  Switch --> Kill[তবেই v1 বন্ধ]
```

দুটো common প্যাটার্ন:
- **Rolling update** — একটা একটা করে instance নতুন version-এ বদলানো (k8s/ECS নিজে করে)।
- **Blue-green** — পুরো নতুন version (green) আলাদা চালু, health OK হলে traffic এক ঝটকায় সরানো; সমস্যা হলে সাথে সাথে পুরনো (blue)-তে ফেরত।

**সহজ VPS-এ:** systemd/PM2-তে graceful reload; বা Docker-এ নতুন container চালু → health OK → proxy সরাও → পুরনো বন্ধ।

### Rollback — পিছিয়ে যাওয়ার পথ সবসময় রাখুন

নতুন deploy ভাঙলে দ্রুত আগের ভালো version-এ ফেরা:
- 🟢 image-এ **version tag** থাকলে (`:1.4`) — আগের tag চালালেই rollback।
- 🟢 PaaS-এ সাধারণত এক ক্লিকে "rollback to previous deploy"।
- 🟢 database migration যেন rollback-safe হয় ([৩১](#s31)) — নাহলে কোড পেছালেও DB আটকে থাকে।

🔴 rollback-এর পথ না রেখে deploy করবেন না। "কীভাবে পেছাব" — deploy-এর **আগে** ভাবুন।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩৩. Scaling — বড় হলে কী করবেন <a id="s33"></a>

User বাড়ল, সার্ভার হাঁপাচ্ছে — এখন?

**দুই ধরনের scaling:**
- **Vertical (উপরে)** — সার্ভারকে বড় করা (বেশি CPU/RAM)। সহজ, কিন্তু একটা সীমা আছে, আর single point of failure।
- **Horizontal (পাশে)** — 🟢 আরও কয়েকটা সার্ভার/instance যোগ করে সামনে একটা **load balancer** বসানো, যে traffic ভাগ করে দেয়। এটাই আসল scale।

```mermaid
flowchart TB
  U[Users] --> LB[Load Balancer]
  LB --> A1[app instance 1]
  LB --> A2[app instance 2]
  LB --> A3[app instance 3]
  A1 & A2 & A3 --> DB[(Database)]
```

**Horizontal scale করতে হলে app-কে হতে হবে "stateless":**
- 🔴 session/data সার্ভারের memory-তে রাখবেন না (এক instance-এ রাখলে অন্যটা জানে না)।
- 🟢 session → Redis/DB-তে; file → object storage (S3)-এ। তাহলে যেকোনো instance যেকোনো request সামলাতে পারে।

**আরও scale-এর হাতিয়ার:**
- **Caching** — বারবার একই জিনিস? Redis-এ cache করুন; DB-র চাপ কমে।
- **CDN** — static সব CDN-এ ([২৯](#s29))।
- **DB read replica** — পড়ার চাপ আলাদা কপিতে।
- **Queue + worker** — ভারী/ধীর কাজ (ইমেইল, রিপোর্ট) background-এ, request দ্রুত ছাড়ুন।
- **Auto-scaling** — cloud/k8s traffic বুঝে instance বাড়ায়/কমায়।

🟢 তবে **আগে মাপুন, পরে scale করুন**। বেশিরভাগ ছোট app-এর scaling লাগেই না — একটা ঠিকঠাক VPS বহুদূর নিয়ে যায়। আসল bottleneck না জেনে scale করা = টাকা ও সময় নষ্ট।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩৪. Security checklist <a id="s34"></a>

Deploy করলেন মানেই আপনি এখন ইন্টারনেটের সবার নাগালে — bot ২৪/৭ দুর্বলতা খোঁজে। ন্যূনতম সুরক্ষা:

🟢 **সার্ভার:**
- firewall — শুধু 22, 80, 443 খোলা ([১২](#s12))।
- SSH key-only, root login বন্ধ, fail2ban।
- নিয়মিত `apt upgrade` (security patch)।

🟢 **App:**
- **HTTPS everywhere** — http → https redirect।
- সব secret env-এ, কোডে নয় ([২৮](#s28))।
- input validation + parameterized query (**SQL injection** ঠেকাতে — কখনো string জোড়া দিয়ে query নয়)।
- password **hash** (bcrypt/argon2), plain-text কখনো নয়।
- CORS নির্দিষ্ট origin-এ ([৮](#s8)), `*` নয়।
- **rate limiting** — এক IP থেকে অতিরিক্ত request আটকান (brute-force, abuse)।
- dependency আপডেট রাখুন (`npm audit`, Dependabot)।
- security header (Helmet middleware): HSTS, CSP, X-Frame-Options।

🟢 **Data:**
- least privilege — DB user-কে শুধু যতটা দরকার ততটা permission।
- backup + restore টেস্ট ([৩১](#s31))।
- ব্যক্তিগত data encrypt (at-rest ও in-transit)।

🔴 **কখনো নয়:** default password, খোলা database port ইন্টারনেটে, debug mode production-এ, error-এ ভেতরের stack trace user-কে দেখানো।

[↑ সূচিপত্রে ফিরুন](#toc)

---

# পর্ব ৭ — গুছিয়ে রাখা (Reference)

## ৩৫. কোন scenario কখন — সিদ্ধান্তের গাইড <a id="s35"></a>

```mermaid
flowchart TD
  Q1{দ্রুত live করা<br/>দরকার? MVP?} -->|হ্যাঁ| PaaS[PaaS<br/>Vercel + Render]
  Q1 -->|না| Q2{ভেতরে কী হয়<br/>শিখতে চান? খরচ<br/>কমাতে চান?}
  Q2 -->|হ্যাঁ| VPS[VPS<br/>নিজে সব setup]
  Q2 -->|না| Q3{team-এ environment<br/>মিলছে না? বহু<br/>জায়গায় চালাবেন?}
  Q3 -->|হ্যাঁ| Docker[Docker +<br/>compose]
  Q3 -->|না| Q4{ঘনঘন deploy?<br/>বড় team?<br/>production?}
  Q4 -->|হ্যাঁ| CICD[CI/CD +<br/>Cloud]
  Q4 -->|বিশাল scale<br/>বহু service| K8s[Kubernetes]
```

**সংক্ষেপে:**
- **শুরু / MVP / solo** → PaaS। এক ঘণ্টায় live।
- **শিখতে / খরচ কমাতে** → VPS। সবচেয়ে বেশি শেখা।
- **environment consistency / team** → Docker।
- **production / ঘনঘন release** → CI/CD + cloud (Docker সহ)।
- **বিশাল scale, বহু microservice** → Kubernetes (তার আগে নয়)।

বাস্তব production-এ এগুলো মেশানো: **কোড GitHub → Actions (CI/CD) → Docker image → cloud (ECS/Cloud Run) → managed DB (RDS) + CDN + monitoring।** কিন্তু ওখানে পৌঁছানোর পথ হলো নিচ থেকে উপরে — এক ধাপ এক ধাপ।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩৬. শেখার পথ — ধাপে ধাপে, project সহ <a id="s36"></a>

**সোনালি নিয়ম: এক app, বারবার deploy — চারটা রাস্তায়।** একটা ছোট full-stack app নিন (একটা todo/notes app — React frontend + Express/Django backend + Postgres)। এবার:

### সপ্তাহ ১ — ভিত্তি + PaaS (app প্রথমবার live)
- 🟢 পর্ব ১ পড়ুন — ১০টা ধারণা বুঝুন ([৪](#s4))।
- 🟢 frontend → Vercel, backend → Render, DB → Supabase/Neon।
- 🟢 env var দিয়ে তিনটা জোড়া লাগান, CORS ঠিক করুন, custom domain যোগ করুন।
- **অর্জন:** আপনার app ইন্টারনেটে live, নিজের domain-এ।

### সপ্তাহ ২ — VPS (আসল বোঝাপড়া)
- 🟢 একটা $6 DigitalOcean droplet নিন।
- 🟢 SSH → user → firewall → Node → Postgres install ([১২](#s12)–[১৩](#s13))।
- 🟢 systemd দিয়ে backend চালু, Nginx দিয়ে frontend + `/api` proxy।
- 🟢 domain point + Certbot দিয়ে HTTPS।
- **অর্জন:** PaaS যা লুকিয়ে করত, সব নিজে করলেন। এবার "deploy" শব্দটা আর রহস্য নয়।

### সপ্তাহ ৩ — Docker
- 🟢 backend ও frontend-এর Dockerfile লিখুন।
- 🟢 `docker-compose.yml`-এ তিন service (web + api + db) — নিজের মেশিনে `docker compose up`।
- 🟢 সেই compose সার্ভারে চালান; Caddy দিয়ে auto-HTTPS।
- **অর্জন:** "আমার মেশিনে চলছিল" সমস্যা শেষ; environment সব জায়গায় এক।

### সপ্তাহ ৪ — CI/CD + এক টুকরো cloud
- 🟢 GitHub Actions: push-এ test + build + image push।
- 🟢 CD: push-এ VPS-এ auto-deploy (SSH action)।
- 🟢 cloud-এর স্বাদ: frontend → S3+CloudFront অথবা backend → Cloud Run (GCP) / ECS Fargate (AWS)।
- 🟢 monitoring: health check + UptimeRobot + Sentry বসান।
- **অর্জন:** git push = live। production-এর মূল অভ্যাস তৈরি।

### এরপর (দরকার হলে)
- Blue-green/rolling deploy, DB backup automation, rate limiting, caching (Redis)।
- সত্যিই scale-এর সমস্যা এলে তবেই k8s।

🟢 প্রতি সপ্তাহে **নিজে হাতে করুন**, শুধু পড়বেন না। ভাঙবে — ভাঙাটাই শেখা। error message পড়ুন, log দেখুন, খুঁজুন। এভাবেই deployment শেখা হয়, video দেখে নয়।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩৭. সাধারণ ভুল (এড়িয়ে চলুন) <a id="s37"></a>

| ভুল | কী হয় | ঠিক পথ |
|---|---|---|
| `.env` git-এ commit | secret ফাঁস | `.gitignore` + platform secret ([২৮](#s28)) |
| port hardcode (`3000`) | PaaS/cloud-এ fail | `process.env.PORT` পড়ুন ([৮](#s8)) |
| `ufw enable` আগে SSH allow না করা | নিজেই লক-আউট | আগে `allow OpenSSH` ([১২](#s12)) |
| process manager ছাড়া `node server.js` | reboot/crash-এ app মরে থাকে | systemd/PM2 ([১৪](#s14)) |
| CORS `origin: '*'` | নিরাপত্তা ফাঁক | নির্দিষ্ট origin ([৮](#s8)) |
| DB backup না রাখা | data হারালে সব শেষ | auto-backup + restore টেস্ট ([৩১](#s31)) |
| `nginx -t` ছাড়া reload | ভুল config → site down | সবসময় আগে test ([১৫](#s15)) |
| HTTPS ছাড়া live | browser warning, অনিরাপদ | Certbot/Caddy/PaaS ([১৬](#s16)) |
| rollback-এর পথ না রাখা | ভাঙা deploy আটকে থাকে | version tag + rollback plan ([৩২](#s32)) |
| শুরুতেই k8s/AWS-এর সব | সময় নষ্ট, হতাশা | নিচ থেকে উপরে, এক ধাপ ([৩৬](#s36)) |
| monitoring ছাড়া deploy | app মরলে user-এর কাছে শোনেন | health + uptime + Sentry ([৩০](#s30)) |
| migration হাতে SQL | team-এ মেলে না, track নেই | migration tool ([৩১](#s31)) |

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩৮. শব্দকোষ (Glossary) <a id="s38"></a>

| শব্দ | মানে |
|---|---|
| **Deploy** | local app-কে server-এ তুলে live করা |
| **Server** | সবসময় চালু, ইন্টারনেটে লাগানো কম্পিউটার |
| **Port** | এক সার্ভারে অনেক app-কে আলাদা করা নম্বর (80/443/3000) |
| **Domain / DNS** | নাম (myapp.com) ↔ IP-তে অনুবাদ |
| **A record / CNAME** | DNS entry — নাম→IP / নাম→নাম |
| **HTTPS / SSL / TLS** | encrypted connection, 🔒 |
| **Let's Encrypt / Certbot** | ফ্রি SSL certificate ও auto-renew tool |
| **Env var** | কোডের বাইরে রাখা setting/secret |
| **Build** | source code → চালানোর মতো রূপ |
| **Runtime** | app আসলে যখন চলছে |
| **Process manager** | app চালু রাখে/crash-এ restart (systemd, PM2) |
| **Reverse proxy** | সামনের gatekeeper (Nginx/Caddy) — HTTPS + routing |
| **VPS** | ভাড়া করা একটা Linux সার্ভার |
| **SSH** | দূরের সার্ভারে নিরাপদে ঢোকা |
| **Firewall (ufw)** | কোন port খোলা/বন্ধ নিয়ন্ত্রণ |
| **Container / Docker** | app+dependency এক "box"-এ, সব জায়গায় এক |
| **Image / Registry** | প্যাকেজ / image রাখার জায়গা (Docker Hub, GHCR) |
| **docker-compose** | বহু container এক ফাইলে চালানো |
| **CI/CD** | push-এ auto test/build/deploy |
| **PaaS** | সব-অটো platform (Vercel, Render) |
| **Load balancer** | traffic কয়েক সার্ভারে ভাগ করে |
| **Stateless** | app memory-তে state রাখে না — scale-এর শর্ত |
| **CDN** | static ফাইল global cache, দ্রুত delivery |
| **Migration** | database schema বদলের version-controlled script |
| **Health check** | app বেঁচে আছে কিনা দেখার endpoint |
| **Rollback** | আগের ভালো version-এ ফেরা |
| **Zero-downtime** | deploy-এর সময় site বন্ধ না হওয়া |
| **Kubernetes (k8s)** | বহু container auto-চালানো/scale করা system |

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৩৯. রেফারেন্স / আরও শেখার জায়গা <a id="s39"></a>

**Official docs (সবচেয়ে নির্ভরযোগ্য):**
- Vercel — https://vercel.com/docs
- Render — https://render.com/docs
- DigitalOcean Tutorials (VPS-এর সোনার খনি) — https://www.digitalocean.com/community/tutorials
- Docker — https://docs.docker.com
- Nginx — https://nginx.org/en/docs/
- Let's Encrypt / Certbot — https://certbot.eff.org
- GitHub Actions — https://docs.github.com/actions
- AWS — https://docs.aws.amazon.com · GCP — https://cloud.google.com/docs
- Kubernetes — https://kubernetes.io/docs/home/

**হাতে-কলমে শেখার জন্য:**
- The Twelve-Factor App (deploy-বান্ধব app বানানোর নীতি) — https://12factor.net
- Roadmap.sh — DevOps ও Backend roadmap — https://roadmap.sh/devops
- DigitalOcean-এর "How To Deploy" সিরিজ — নির্দিষ্ট stack ধরে ধরে।

**অভ্যাস করার পথ:** এই ডকের [৩৬ নং](#s36)-এর ৪-সপ্তাহ প্ল্যান — এক app, চার রাস্তা। পড়ার চেয়ে **করা** ১০ গুণ বেশি শেখায়।

[↑ সূচিপত্রে ফিরুন](#toc)

---

## ৪০. বাংলা ভিডিও রিসোর্স (YouTube) <a id="s40"></a>

লেখা পড়ে না বুঝলে ভিডিও দেখুন। নিচের ক্রম মেনে এগোলে ফাঁক থাকবে না।

### ধাপ ১ — Frontend (React)

| রিসোর্স | কেন |
|---|---|
| [React.js Full Course in Bangla — Anisul Islam](https://www.youtube.com/playlist?list=PLgH5QX0i9K3rGtitufynBKMy5gAFpa1y8) | সবচেয়ে বিস্তারিত, ধীরে ব্যাখ্যা। একেবারে নতুনদের জন্য সেরা। |
| [React js Tutorial Bangla Course for Beginners](https://www.youtube.com/playlist?list=PLerpoOYRrjUzBYHMq7TVTKcl6w3MQaCcZ) | বিকল্প — অন্য শেখানোর ধরন পছন্দ হলে। |
| [React JS Bangla Tutorial](https://www.youtube.com/playlist?list=PLNMnAEqLBwmqvuLEb5fVyGfcdMMlrEsHL) | আরেকটা বিকল্প। |

JavaScript-এ ভিত দুর্বল লাগলে React-এর আগে: [JavaScript FULL COURSE in 30 Days — Learn with Sumit](https://www.youtube.com/watch?v=bc61fVxUHzU)।

### ধাপ ২ — Backend (Node + Express)

- [Node.js + Express.js Tutorial Bangla Series](https://www.youtube.com/playlist?list=PLHiZ4m8vCp9PHnOIT7gd30PCBoYCpGoQM) — বাংলায় সবচেয়ে পূর্ণাঙ্গ backend সিরিজ।

### ধাপ ৩ — Database (PostgreSQL)

> সৎ কথা: বাংলায় একটামাত্র পূর্ণাঙ্গ Postgres প্লেলিস্ট নেই। নিচের ভিডিওগুলো ছড়ানো, কিন্তু একসাথে দেখলে কাজ চলে যায়।

| রিসোর্স | কেন |
|---|---|
| [postgresql bangla tutorial 1 — Installation](https://www.youtube.com/watch?v=XH96C8Hz2Og) | শুরুর পয়েন্ট। ওই চ্যানেলের পরের ভিডিওগুলো ধরে এগোন। |
| [postgresql bangla tutorial 6 — WHERE Query](https://www.youtube.com/watch?v=fbAn-OZLR0M) | একই সিরিজ, SQL query। |
| [PERN Stack Bangla — Postgres টেবিলে data insert](https://www.youtube.com/watch?v=qBNnupZA4Qo) | React + Node + Postgres **একসাথে জোড়া লাগানো** — এই ডকের [৩ নং](#s3)-এর হাতে-কলমে রূপ। |
| [Prisma ORM Crash Course in Bangla](https://www.youtube.com/watch?v=QgREoATKO9s) | raw SQL না লিখে ORM দিয়ে DB। [৩১ নং](#s31)-এর migration এখানেই। |
| [Supabase Complete Crash Course in Bangla](https://www.youtube.com/watch?v=PJBHfF-BWlQ) | **Managed Postgres** — DB আলাদা service হিসেবে নেওয়ার সবচেয়ে সহজ রাস্তা। |

বাংলায় গভীরে না পেলে ইংরেজি fallback: [PERN Stack Course — freeCodeCamp](https://www.youtube.com/watch?v=ldYcgPKEZC8)।

### ধাপ ৪ — Deployment (এই ডকের মূল বিষয়)

| রিসোর্স | ডকের কোন অংশ |
|---|---|
| [Nginx Tutorial in Bangla — কেন production-এ লাগে](https://www.youtube.com/watch?v=mEAcyo2qdm8) | পর্ব ৩ (VPS) — reverse proxy কেন দরকার |
| [What is Docker, Virtualization & Containers (বাংলা)](https://www.youtube.com/watch?v=6A4VZlyAfe0) | পর্ব ৪ — container-এর ধারণা |
| [Docker Zero To Hero Bangla — Day 1](https://www.youtube.com/watch?v=eHVkgI_bDas) | পর্ব ৪ — Docker হাতে-কলমে |
| [(Bangla) Docker: microservice system from scratch](https://www.youtube.com/playlist?list=PLEYpvDF6qy8Yo9SpzhniLCjgRIxCpo2ku) | পর্ব ৪ — Compose দিয়ে **DB + API একসাথে** চালানো |

### চ্যানেল (bookmark করে রাখুন)

- [Anisul Islam](https://www.youtube.com/@anisul-islam) — সবচেয়ে বড় বাংলা programming চ্যানেল। প্রায় সব topic আছে।
- [Learn with Sumit (LWS)](https://www.youtube.com/@LearnwithSumit) — industry-level, আধুনিক। JS/React গভীরে।

### সতর্কতা

🔴 ভিডিও গিলে ফেলবেন না। প্রতি ধাপ শেষে **একটা ছোট project** বানান — নাহলে কিছুই থাকবে না।
🟢 তাড়াহুড়ো থাকলে শুধু দুটো: **Supabase crash course** (managed DB) + **Docker microservice playlist** (নিজে চালানো)। এই দুইয়েই "database কি আলাদা service?" প্রশ্নের উত্তর পরিষ্কার হয়ে যাবে।

[↑ সূচিপত্রে ফিরুন](#toc)

---

> **শেষ কথা:** Deployment ভীতিকর লাগে কারণ একসাথে অনেক নতুন শব্দ আসে। কিন্তু ভেতরে সবই ঘুরেফিরে সেই [১০টা ধারণা](#s4)। এক app নিন, আজই PaaS-এ live করুন, তারপর ধাপে ধাপে গভীরে যান। ছয় মাস পরে পেছনে তাকিয়ে অবাক হবেন — যেটা রহস্য ছিল, সেটা এখন রুটিন।

[↑ সূচিপত্রে ফিরুন](#toc)

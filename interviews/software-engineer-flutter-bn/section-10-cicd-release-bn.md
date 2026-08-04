# Section 10 — CI/CD, Flavors ও App Release

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** এবং **Bangladesh (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যা** সহ, আর **link** করা — যাতে আপনি এদিক-ওদিক ঘুরে ধাপে ধাপে প্রস্তুতি নিতে পারেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-10-cicd-release-bn.md](../software-engineer-flutter/section-10-cicd-release.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ লাইনের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code সহ ধাপে ধাপে বিস্তারিত ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সংযুক্ত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে ট্যাগ দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তর** দিন (২–৩ লাইন), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন "আরও গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলাটাই একটা senior skill — remote আর BD দুই ধরনের কোম্পানিতেই এটা একইভাবে কাজ করে।

---


## <a id="toc"></a>সূচিপত্র

**A. Build mode আর CI/CD-র মূল কথা**
1. [Build mode — debug, profile, release](#q1) · *Very common*
2. [GitHub Actions দিয়ে মৌলিক CI pipeline](#q2) · *Very common*
3. [CI secrets, caching আর build দ্রুত করা](#q3) · *Common*
4. [App versioning — `1.0.0+1` আর auto-increment](#q4) · *Very common*

**B. Flavors ও environments**
5. [Flavor — dev / staging / prod (Android আর iOS)](#q5) · *Very common*
6. [`--dart-define` আর build-time variable](#q6) · *Very common*
7. [প্রতি environment-এ API URL, key আর config সামলানো](#q7) · *Common*

**C. Code signing ও obfuscation**
8. [Code signing — Android keystore আর iOS profile](#q8) · *Very common*
9. [Fastlane — `match` (iOS) আর `supply` (Android)](#q9) · *Common*
10. [App obfuscation আর crash symbolize করা](#q10) · *Common*

**D. Store release ও distribution**
11. [APK vs AAB — আর Play কেন AAB পছন্দ করে](#q11) · *Very common*
12. [Test build-এর জন্য Firebase App Distribution](#q12) · *Common*
13. [Google Play release — internal / alpha / beta / production](#q13) · *Very common*
14. [Apple App Store আর TestFlight-এর flow](#q14) · *Very common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

১৪টা প্রশ্ন একসাথে পড়ার দরকার নেই। এই পর্যায়গুলো ক্রম অনুযায়ী অনুসরণ করুন — প্রতিটা আগেরটার উপর দাঁড়ানো। একটা পর্যায় তখনই টিক দিন, যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন।

**পর্যায় ১ — ভিত্তি (এখান থেকে শুরু করুন)।** এগুলো ছাড়া release নিয়ে কথা বলা যায় না।
→ [Q1 Build mode](#q1) · [Q4 Versioning](#q4) · [Q5 Flavor](#q5) · [Q6 dart-define](#q6)

**পর্যায় ২ — একটা build বের করে আনুন।** প্রতিদিনের CI-র কাজ।
→ [Q2 GitHub Actions CI](#q2) · [Q3 Secrets আর caching](#q3) · [Q7 Env config](#q7)

**পর্যায় ৩ — Signing (এই অংশটাই সবচেয়ে বেশি ভাঙে)।**
→ [Q8 Code signing](#q8) · [Q9 Fastlane](#q9) · [Q10 Obfuscation](#q10)

**পর্যায় ৪ — User-এর কাছে পাঠান।** Store-release-এর pipeline।
→ [Q11 APK vs AAB](#q11) · [Q12 Firebase App Distribution](#q12) · [Q13 Google Play track](#q13) · [Q14 App Store আর TestFlight](#q14)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই ছয়টা দেখে নিন:
[Q1](#q1) · [Q4](#q4) · [Q5](#q5) · [Q6](#q6) · [Q8](#q8) · [Q11](#q11), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Build mode আর CI/CD-র মূল কথা

---

## <a id="q1"></a>1. Flutter-এর build mode কী কী? Debug, profile আর release ব্যাখ্যা করুন।

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flutter-এ তিনটা build mode আছে। Debug প্রতিদিনের code লেখার জন্য — এতে hot reload আর অনেক check থাকে, কিন্তু এটা ধীর। Profile হলো performance মাপার জন্য — এটা release-এর মতো চলে, কিন্তু profiling tool চালু রাখে। Release হলো যেটা আসল user পায় — এটা native code-এ compile হয়, ছোট আর দ্রুত। বড় নিয়ম: debug build দেখে কখনোই গতি বিচার করবেন না।"

**এবার পুরোটা বুঝি:**

এই তিনটা mode-কে গাড়ি বানানোর তিনটা পর্যায়ের মতো ভাবুন। **গ্যারেজের prototype** (debug) নাড়াচাড়া করা সহজ, কিন্তু রাস্তায় নামানোর মতো নয়। **Test track-এর গাড়ি** (profile) হলো আসল গাড়ি, তবে মাপার জন্য sensor লাগানো। **Showroom-এর গাড়ি** (release) পরিষ্কার, দ্রুত আর ক্রেতাকে বিক্রি করা হয়।

**ধাপ ১ — Debug mode (code লেখার জন্য)।**
Run চাপলে এটাই default থাকে। এটা JIT compilation ব্যবহার করে, আর এ কারণেই **hot reload** কাজ করে। এটা `assert` আর বাড়তি check-ও চালু রাখে, যা bug আগেভাগে ধরে। বিনিময়ে: এটা অনেক ধীর আর app-টা অনেক বড় হয়।

```bash
flutter run                 # debug-ই default
flutter run --debug         # একই জিনিস, স্পষ্ট করে লেখা
```

**ধাপ ২ — Profile mode (গতি মাপার জন্য)।**
Profile mode release-এর মতোই native code-এ (AOT) compile করে, তাই গতিটা বাস্তবসম্মত। কিন্তু কিছু tooling চালু থাকে, যাতে DevTools দিয়ে ধীর frame (jank) খুঁজে পান। Profile mode-এ hot reload করা যায় না।

```bash
flutter run --profile       # বাস্তব গতি + profiling tool
```

কেউ যখন বলে "app-টা কেমন যেন আটকে যাচ্ছে", তখন এটা ব্যবহার করুন — অনুমান না করে profile করে আসল কারণ বের করুন।

**ধাপ ৩ — Release mode (user-এর জন্য)।**
এটাই আপনি ship করেন। এটা AOT ব্যবহার করে (চালু হওয়ার আগেই native machine code-এ compile করা), `assert` আর debug info বাদ দেয়, আর অব্যবহৃত code tree-shake করে। ফল হলো একটা ছোট আর দ্রুত app। এখানে hot reload নেই, debugging tool-ও নেই।

```bash
flutter run --release       # user যা পায়
flutter build apk --release
flutter build appbundle --release
flutter build ipa --release
```

**ধাপ ৪ — দ্রুত একটা তুলনা।**

| | Debug | Profile | Release |
|---|---|---|---|
| Compilation | JIT | AOT (native) | AOT (native) |
| Hot reload | হ্যাঁ | না | না |
| Assert / check | চালু | বন্ধ | বন্ধ |
| গতি | ধীর | বাস্তবসম্মত | দ্রুত |
| কীসের জন্য | code লেখা | performance মাপা | user-এর কাছে পাঠানো |

**Interviewer কেন জিজ্ঞেস করে:** Junior-দের খুব সাধারণ একটা ভুল হলো debug build-এ lag নিয়ে অভিযোগ করা। তিনটা mode জানা — আর মাপার জন্য profile-ই সঠিক, এটা জানা — স্পষ্ট senior signal।

**সাধারণ ভুল:** Debug mode-এ performance মেপে এমন জিনিস "optimize" করার চেষ্টা করা, যেগুলো শুধু debug check-এর কারণেই ধীর। অনেক "performance bug" release বা profile mode-এ এমনিতেই উধাও হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Debug কেন ধীর?"* → JIT চলার সময়ে compile করে। তার উপর সব assert আর check বাড়তি খরচ যোগ করে।
- *"Release-এর বদলে profile কখন ব্যবহার করেন?"* → যখন গতি মাপা দরকার, কিন্তু DevTools যুক্ত রাখতে চান। Release-এ tool-গুলো বাদ দেওয়া থাকে।

**সম্পর্কিত:** [Q11 — APK vs AAB output](#q11) · [Q10 — release obfuscation](#q10)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. GitHub Actions ব্যবহার করে Flutter-এর জন্য মৌলিক CI pipeline কীভাবে সেট করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"CI মানে: আমি যতবার code push করি, একটা server স্বয়ংক্রিয়ভাবে সেটা check করে। Flutter-এর জন্য আমি `.github/workflows/`-এ একটা YAML file লিখি। Pipeline সাধারণত চারটা ধাপ করে — code আনা, Flutter install করা, analyze আর test চালানো, তারপর app build করা। Android build চলে Linux machine-এ; iOS build-এর জন্য macOS machine লাগে।"

**এবার পুরোটা বুঝি:**

CI/CD-কে একটা **কারখানার conveyor belt** হিসেবে ভাবুন। আপনি এক প্রান্তে code ফেলেন (একটা push), আর সেটা একের পর এক station পেরিয়ে যায় — check, test, packing — হাতে কিছু না ছুঁয়েই। শেষে একটা তৈরি, tested build বেরিয়ে আসে। মূল কথা হলো সমস্যা স্বয়ংক্রিয়ভাবে ধরা, আর প্রতিবার একই নিয়মে।

**ধাপ ১ — File কোথায় থাকে।**
GitHub Actions আপনার repo-র `.github/workflows/` folder থেকে YAML file পড়ে। প্রতিটা file একটা pipeline (যাকে "workflow" বলে)।

**ধাপ ২ — কখন চলে (trigger)।**
কোন event belt চালু করবে, সেটা আপনি বলে দেন — সাধারণত `main`-এ push আর প্রতিটা pull request।

```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
```

**ধাপ ৩ — Station-গুলো (একটা পূর্ণ কাজ করা উদাহরণ)।**

```yaml
# .github/workflows/flutter_ci.yml
name: Flutter CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest          # Android-এর জন্য Linux-ই যথেষ্ট
    steps:
      - uses: actions/checkout@v4    # 1. code আনা

      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.24.0'  # একই ফল পেতে version pin করুন
          channel: 'stable'
          cache: true                # run-এর মাঝে SDK cache করুন

      - name: Install dependencies
        run: flutter pub get

      - name: Analyze code
        run: flutter analyze --fatal-infos   # warning হলেও fail করবে

      - name: Run tests
        run: flutter test --coverage

      - name: Build APK
        run: flutter build apk --release --build-number=${{ github.run_number }}

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: release-apk
          path: build/app/outputs/flutter-apk/app-release.apk
```

**ধাপ ৪ — iOS কেন আলাদা।**
Linux-এ iOS app build করা যায় না, কারণ এর জন্য Xcode লাগে, আর Xcode শুধু macOS-এ চলে। তাই iOS job-টাকে macOS machine ব্যবহার করতে হবে, আর আগে code signing সেট করতে হবে।

```yaml
jobs:
  ios-build:
    runs-on: macos-latest            # iOS-এর জন্য macOS বাধ্যতামূলক
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.24.0'
          channel: 'stable'
      - run: flutter pub get
      # ... এখানে certificate আর provisioning profile install করুন (দেখুন Q8/Q9) ...
      - run: flutter build ipa --release
```

**ধাপ ৫ — ফলাফল সংরক্ষণ করুন (artifact)।**
Run শেষ হলে build machine-টা মুছে ফেলা হয়। তাই আপনাকে অবশ্যই **APK/IPA-কে artifact হিসেবে upload করতে** হবে (উপরের শেষ ধাপ), না হলে আপনার build হারিয়ে যাবে।

```
  Push / PR to main
        |
        v
   Checkout + Setup Flutter
        |
        v
   flutter analyze  ->  flutter test
        |
   +----+-----------------+
   |                       |
   v                       v
 Build APK (Linux)   Build IPA (macOS)
   |                       |
   v                       v
 Upload artifact     Upload artifact
```

**Interviewer কেন জিজ্ঞেস করে:** যেকোনো পেশাদার Flutter team-এ CI থাকাটা প্রত্যাশিত। তাঁরা দেখতে চান আপনি শুধু feature লেখেন না, check আর build স্বয়ংক্রিয়ও করতে পারেন। YAML-এর গঠন, caching আর artifact জানা production-এর জন্য প্রস্তুতির লক্ষণ।

**সাধারণ ভুল:** Linux runner-এ iOS build করার চেষ্টা করা — এটা fail করবে, কারণ সেখানে Xcode নেই। আরেকটা ভুল, artifact upload করতে ভুলে যাওয়া — তাতে machine মুছে গেলে build হারিয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"CI আর CD-র পার্থক্য কী?"* → CI = স্বয়ংক্রিয়ভাবে build আর test করা। CD = সেই build স্বয়ংক্রিয়ভাবে পৌঁছে দেওয়া/deploy করা (tester বা store-এ)।
- *"GitHub Actions vs Codemagic vs Bitrise?"* → GitHub Actions সাধারণ কাজের জন্য, আর অনেক repo-তে বিনামূল্যে। Codemagic আর Bitrise mobile-কেন্দ্রিক। এগুলো Mac machine আর signing শুরু থেকেই আরও সহজে সামলায়।

**সম্পর্কিত:** [Q3 — secrets আর caching](#q3) · [Q9 — store upload-এর জন্য Fastlane](#q9) · [Q4 — CI-তে build number](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. CI-তে secrets কীভাবে handle করেন, আর Flutter build কীভাবে দ্রুত করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Secrets — যেমন keystore, API key আর store credentials — কখনোই Git-এ commit করা যাবে না। আমি এগুলো CI secrets হিসেবে রাখি এবং build-এর সময়ে inject করি, প্রায়ই base64-encoded file হিসেবে। Build দ্রুত করতে আমি Flutter SDK আর pub package cache করি, Flutter version pin করি, আর কাজটা আলাদা parallel job-এ ভাগ করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সোনালি নিয়ম: secrets কখনো repo-তে থাকবে না।**
Git-এ কোনো password বা key থাকলে, যে কেউ code পড়তে পারে সে সেটা চিরকালের জন্য পেয়ে যায় — আপনি মুছে ফেললেও (history-তে থেকে যায়)। তাই secrets যায় CI provider-এর secret store-এ। Build-এর সময়ে environment variable হিসেবে সেগুলো পড়া হয়।

**ধাপ ২ — GitHub Actions-এ secrets পড়া।**
আপনি সেগুলো repo-র Settings → Secrets-এ যোগ করেন, তারপর `${{ secrets.NAME }}` দিয়ে পড়েন।

```yaml
- name: Build signed APK
  env:
    KEY_PASSWORD: ${{ secrets.ANDROID_KEY_PASSWORD }}
    STORE_PASSWORD: ${{ secrets.ANDROID_STORE_PASSWORD }}
  run: flutter build appbundle --release
```

**ধাপ ৩ — File-কে secret বানানো (base64 কৌশল)।**
Keystore বা Google Play JSON key একটা file, কিন্তু secret store শুধু text রাখে। তাই file-টাকে base64 string-এ encode করুন, সেই string-টা secret হিসেবে save করুন, আর machine-এ আবার file-এ decode করুন।

```bash
# আপনার computer-এ file-টাকে এক line text বানান:
base64 -i my-release-key.jks | pbcopy      # তারপর CI secret-এ paste করুন
```

```yaml
- name: Restore keystore from secret
  run: echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 --decode > android/app/release.jks
```

**ধাপ ৪ — গতি: যা বদলায় না তা cache করুন।**
CI run-এর বেশিরভাগ সময় যায় একই file বারবার download করতে। ওগুলো cache করুন।

```yaml
- uses: subosito/flutter-action@v2
  with:
    flutter-version: '3.24.0'
    cache: true                 # Flutter SDK cache করে

- name: Cache pub packages
  uses: actions/cache@v4
  with:
    path: ~/.pub-cache
    key: pub-${{ hashFiles('pubspec.lock') }}
```

**ধাপ ৫ — গতি বাড়ানোর আরও উপায়।**
- **Flutter version pin করুন** (`3.24.0`, `stable` নয়) যাতে build বারবার একই হয় আর cache hit করে।
- **Job গুলো parallel-এ চালান** — analyze, test আর build আলাদা machine-এ একসাথে চলতে পারে।
- **যা বদলেছে শুধু তা build করুন** — যেমন, iOS file বদলালেই কেবল iOS job চালান।
- **`pub get`-এর পরের step-গুলোতে `--no-pub` ব্যবহার করুন** যাতে package আবার resolve না হয়।

**Interviewer কেন জিজ্ঞেস করে:** Keystore বা store key ফাঁস হওয়া একটা গুরুতর, বাস্তব ঘটনা। তাঁরা দেখতে চান আপনি secrets সাবধানে handle করেন কি না। Caching দেখায় আপনি পুরো team-এর দ্রুত feedback নিয়ে ভাবেন।

**সাধারণ ভুল:** `key.properties`, keystore বা Google Play JSON key repo-তে commit করে ফেলা। আরেকটা ভুল — কিছুই cache না করা, ফলে প্রতিটা CI run ধীর হয় আর টাকা নষ্ট হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"base64 file কোথায় decode করেন?"* → Job চলার সময়ে runner-এ, তারপর কাজ শেষে মুছে ফেলি। এটা কখনো Git-এ যায় না।
- *"Log-এ secrets না আসা কীভাবে নিশ্চিত করেন?"* → CI provider log-এ secret value স্বয়ংক্রিয়ভাবে mask করে; নিজে কখনো secret `echo` করবেন না।

**সম্পর্কিত:** [Q2 — CI pipeline](#q2) · [Q8 — keystore কী](#q8) · [Q9 — Fastlane match secrets](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. Flutter-এ versioning কীভাবে কাজ করে? `1.0.0+1` format আর CI-তে build number স্বয়ংক্রিয়ভাবে বাড়ানো ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`pubspec.yaml`-এ version দেখতে এমন — `1.2.3+45`। `+`-এর আগের অংশটা version name, যেটা user store-এ দেখে। `+`-এর পরের অংশটা build number — একটা internal integer, প্রতিটা upload-এ যেটা সবসময় বাড়তে হবে। CI-তে আমি সাধারণত হাতে file edit না করে build number স্বয়ংক্রিয়ভাবে set করি।"

**এবার পুরোটা বুঝি:**

এটাকে বইয়ের edition-এর মতো ভাবুন। **Version name** (`1.2.3`) হলো মলাটে ছাপা edition, যেটা পাঠক চেনে। **Build number** (`45`) হলো ছাপাখানার ভেতরের serial number — পাঠক এটা কখনো দেখে না, কিন্তু এটা বাড়তেই থাকতে হবে যাতে গুদাম বুঝতে পারে কোন কপিটা নতুন।

**ধাপ ১ — Format।**

```yaml
# pubspec.yaml
version: 1.2.3+45
#        ^^^^^  ^^
#        |      |
#        |      +-- Build number  (versionCode on Android,
#        |                         CFBundleVersion on iOS)
#        +--------- Version name  (versionName on Android,
#                                  CFBundleShortVersionString on iOS)
```

**ধাপ ২ — যে নিয়ম ভাঙলে build আটকে যায়: number বাড়তেই হবে।**
- **Android**-এ, Play-তে প্রতিটা upload-এর জন্য build number (`versionCode`) কঠোরভাবে বাড়তে থাকা integer হতে হবে। `45` upload করলে, পরের upload হতে হবে `46` বা তার বেশি।
- **iOS**-এ, একই version name-এর ভেতরে প্রতিটা upload-এর জন্য build number (`CFBundleVersion`) বাড়তে হবে।
- **Version name** হলো যা user দেখে। এটা semantic versioning (`MAJOR.MINOR.PATCH`) মেনে চলা উচিত।

একই build number আবার upload করলে store সেটা reject করে। Release-এর সবচেয়ে সাধারণ মাথাব্যথা এটাই।

**ধাপ ৩ — Build-এর সময়ে override করুন (file edit করবেন না)।**
Flutter flag দিয়ে version override করতে দেয়। ফলে CI নিজে number হিসাব করে নিতে পারে।

```bash
# CI run number-কেই build number হিসেবে ব্যবহার করুন:
flutter build appbundle --release \
  --build-name=1.2.3 \
  --build-number=$GITHUB_RUN_NUMBER

# অথবা git commit count থেকে নিন (সবসময় বাড়ে):
BUILD_NUM=$(git rev-list --count HEAD)
flutter build appbundle --release \
  --build-name=1.2.3 \
  --build-number=$BUILD_NUM
```

**ধাপ ৪ — GitHub Actions workflow-এ।**

```yaml
- name: Build app bundle
  run: |
    flutter build appbundle --release \
      --build-name=1.2.3 \
      --build-number=${{ github.run_number }}
```

প্রতিটা workflow run-এ `github.run_number` এক করে বাড়ে। তাই এটা একটা নিরাপদ, সবসময় বাড়তে থাকা build number।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান আপনি বোঝেন *কেন* build number সবসময় বাড়তে হবে, আর আপনি এটা automate করতে পারেন কি না। প্রতিটা release-এ হাতে `pubspec.yaml` edit করা ভুলে ভরা কাজ আর এটা automation আটকে দেয়।

**সাধারণ ভুল:** `build-name` (দেখানোর version, যেমন `1.2.3`) আর `build-number` (ভেতরের integer, যেমন `45`) গুলিয়ে ফেলা। আরেকটা ক্লাসিক ভুল: upload fail হওয়ার পরে একই build number আবার ব্যবহার করা, তারপর অবাক হওয়া যে store কেন reject করছে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Build number দিতে ভুলে গেলে কী হয়?"* → Flutter `pubspec.yaml`-এর টা ব্যবহার করে। Flag শুধু ওটাকে override করে।
- *"দুই platform কি একই build number ব্যবহার করতে পারে?"* → হ্যাঁ, সমস্যা নেই — প্রতিটা store শুধু *নিজের* ধারাবাহিকতা বাড়ছে কি না তা দেখে।

**সম্পর্কিত:** [Q2 — CI-তে এটার ব্যবহার](#q2) · [Q13 — Play না-বাড়া build reject করে](#q13)

[↑ উপরে ফিরুন](#toc)

---

# B. Flavors ও environments

---

## <a id="q5"></a>5. Flutter flavors কী? Android আর iOS-এ dev / staging / prod কীভাবে setup করেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flavors দিয়ে আমি এক codebase থেকে একই app-এর কয়েকটা version build করতে পারি — সাধারণত dev, staging আর prod। প্রতিটা flavor-এর নিজস্ব app ID, নাম, icon আর config থাকতে পারে। Android-এ আমি `build.gradle`-এ `productFlavors` define করি; iOS-এ Xcode scheme আর build configuration বানাই। তারপর `--flavor` দিয়ে run করি।"

**এবার পুরোটা বুঝি:**

Flavors-কে ভাবুন **একই recipe, শুধু label আলাদা**। কেক একই, কিন্তু একটা বাক্সে লেখা "Dev" (রান্নাঘরের team-এর স্বাদ নেওয়ার জন্য), একটায় "Staging" (manager-এর অনুমোদনের জন্য), আর একটায় "Prod" (গ্রাহকের জন্য)। App একই, শুধু নাম, icon আর কোন server-এর সাথে কথা বলে সেটা আলাদা — তাই তিনটাই এক phone-এ পাশাপাশি install রাখা যায়।

**ধাপ ১ — Flavors কেন দরকার।**
Flavors ছাড়া dev আর prod একই app ID নিয়ে কাড়াকাড়ি করে, তাই দুটো একসাথে install করা যায় না। আর প্রতিটা build-এর আগে হাতে API URL বদলাতে হতো — ধীর আর বিপজ্জনক। Flavors এই পার্থক্যটা স্বয়ংক্রিয় আর নিরাপদ করে দেয়।

**ধাপ ২ — Android setup (`build.gradle`)।**
আপনি একটা dimension আর flavor গুলো declare করেন। প্রতিটা flavor আলাদা `applicationIdSuffix` পায় (যাতে app ID আলাদা হয়) আর একটা display নাম পায়।

```groovy
// android/app/build.gradle
android {
    flavorDimensions "environment"     // লাগবেই, নাহলে Gradle error দেয়

    productFlavors {
        dev {
            dimension "environment"
            applicationIdSuffix ".dev"          // com.example.app.dev
            resValue "string", "app_name", "MyApp Dev"
        }
        staging {
            dimension "environment"
            applicationIdSuffix ".staging"      // com.example.app.staging
            resValue "string", "app_name", "MyApp Staging"
        }
        prod {
            dimension "environment"
            resValue "string", "app_name", "MyApp"   // suffix নেই = আসল ID
        }
    }
}
```

**ধাপ ৩ — iOS setup (Xcode scheme + configuration)।**
iOS-এ "flavors" বলে কিছু নেই। বদলে আপনি এটা করেন:
1. প্রতিটা flavor-এর জন্য Debug আর Release **configuration** duplicate করুন (যেমন `Debug-dev`, `Release-dev`, `Debug-prod`, `Release-prod`)।
2. প্রতিটা flavor-এর জন্য একটা **scheme** বানান, যেটা তার মিলে যাওয়া configuration-গুলো দেখায়।
3. প্রতিটা configuration-এর build settings-এ আলাদা `PRODUCT_BUNDLE_IDENTIFIER` আর `PRODUCT_NAME` দিন।

এতে iOS-এ ঠিক সেই "প্রতি environment-এ আলাদা ID + নাম" ফলটাই পাওয়া যায়, যেটা Android-এ `productFlavors` দেয়।

**ধাপ ৪ — প্রতি flavor-এর জন্য আলাদা entry point (সাধারণ pattern)।**
প্রতিটা flavor-এর সাধারণত নিজের `main` file থাকে, যাতে সে ঠিক config বেছে নিতে পারে।

```dart
// lib/main_dev.dart
void main() => bootstrap(Environment.dev);

// lib/main_prod.dart
void main() => bootstrap(Environment.prod);
```

**ধাপ ৫ — Flavor দিয়ে run আর build করা।**

```bash
# dev চালান:
flutter run --flavor dev -t lib/main_dev.dart

# prod release build করুন:
flutter build appbundle --release --flavor prod -t lib/main_prod.dart
flutter build ipa --release --flavor prod -t lib/main_prod.dart
```

```
        Flutter codebase
               |
      +--------+--------+
      |        |        |
    [dev]  [staging]  [prod]
      |        |        |
   .dev ID  .stg ID   real ID
   Dev icon Stg icon  Prod icon
   Dev API  Stg API   Prod API
```

**ধাপ ৬ — Flavor বনাম `--dart-define` (সাধারণ follow-up)।**
Flavor একটা **native** ধারণা — এটা platform level-এ app ID, নাম, icon আর native resource বদলায়। `--dart-define` শুধু **compile-time value গুলো Dart code-এ পাঠায়**। সাধারণত আপনি দুটোই ব্যবহার করেন: native পার্থক্যের জন্য flavors, আর API URL-এর মতো Dart-level config-এর জন্য dart-define (দেখুন [Q6](#q6))।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা নিশ্চিত হতে চান আপনি code copy-paste বা হাতে config edit না করে একাধিক environment সামলাতে পারেন। QA আর CI pipeline আছে এমন যেকোনো team-এর জন্য এটা মৌলিক।

**সাধারণ ভুল:** Flavors আর dart-define গুলিয়ে ফেলে বলা "আমি সব কিছুর জন্য dart-define ব্যবহার করি" — dart-define app ID, icon বা native resource বদলাতে পারে না। আরেকটা ভুল হলো Android-এ `flavorDimensions` দিতে ভুলে যাওয়া, ফলে Gradle একটা বিভ্রান্তিকর error দিয়ে fail করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আলাদা app ID কেন চান?"* → যাতে dev, staging আর prod একসাথে এক phone-এ install থাকতে পারে, একটা আরেকটাকে মুছে না দিয়ে।
- *"প্রতিটা flavor-কে আলাদা icon/Firebase file কীভাবে দেন?"* → Icon আর `google-services.json` / `GoogleService-Info.plist` প্রতি flavor-এর আলাদা folder-এ রাখুন, build সেগুলো তুলে নেবে।

**সম্পর্কিত:** [Q6 — dart-define](#q6) · [Q7 — env config](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. `--dart-define` কীভাবে কাজ করে? Build-এর সময় variable কীভাবে pass করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`--dart-define` key-value জোড়া Dart-এ পাঠায় compile-time constant হিসেবে। Build করার সময় এগুলো binary-র ভেতরে বসে যায় — এগুলো runtime value নয়। আমি এগুলো পড়ি `String.fromEnvironment` আর তার সঙ্গীদের দিয়ে। এগুলো `const` বলে Dart এমনকি এদের উপর নির্ভরশীল code tree-shake করে ফেলতে পারে।"

**এবার পুরোটা বুঝি:**

`--dart-define`-কে ভাবুন **কারখানায় বাক্সের গায়ে একটা মান ছাপিয়ে দেওয়ার মতো**। বাক্স একবার সিল হয়ে গেলে (build হয়ে গেলে) ওই মান স্থায়ী — নতুন বাক্স না বানিয়ে পরে আর বদলানো যায় না। এটা এমন কোনো setting নয় যা app চলার সময় user বদলাতে পারে।

**ধাপ ১ — command line-এ মান pass করা।**

```bash
# একটা variable:
flutter run --dart-define=API_URL=https://dev.api.com

# কয়েকটা variable:
flutter build apk --release \
  --dart-define=API_URL=https://dev.api.com \
  --dart-define=API_KEY=abc123 \
  --dart-define=ENABLE_LOGS=true
```

**ধাপ ২ — Dart-এ এগুলো পড়া।**
`fromEnvironment` constructor দিয়ে এগুলো `const` field-এ পড়তে হবে। আর সবসময় একটা `defaultValue` দিন।

```dart
class EnvConfig {
  static const String apiUrl = String.fromEnvironment(
    'API_URL',
    defaultValue: 'https://localhost',
  );

  static const String apiKey = String.fromEnvironment(
    'API_KEY',
    defaultValue: '',
  );

  static const bool enableLogs = bool.fromEnvironment(
    'ENABLE_LOGS',
    defaultValue: false,
  );
}
```

**ধাপ ৩ — এগুলো কেন `const` হতেই হবে।**
মানটা compile time-এ ঠিক হয়ে যায় বলে Dart একে constant ধরে। মানে Dart অব্যবহৃত (dead) branch গুলো সরিয়ে ফেলতে পারে। যেমন, `enableLogs` যদি `false` হয়, তাহলে release-এ logging code tree-shake হয়ে বাদ যাবে — app ছোট হবে, আর logging path পুরোপুরি লুকিয়ে যাবে।

**ধাপ ৪ — আরও পরিষ্কার উপায়: একটা JSON file (Flutter 3.7+)।**
দশটা flag pass করা এলোমেলো লাগে, আর সেগুলো shell history-তে ফাঁস হয়ে যায়। এর বদলে এগুলো একটা JSON file-এ রাখুন, আর সেই file-এর দিকে ইশারা করুন।

```json
// env/dev.json
{
  "API_URL": "https://dev.api.com",
  "API_KEY": "abc123",
  "ENABLE_LOGS": "true"
}
```

```bash
flutter run --dart-define-from-file=env/dev.json
flutter build appbundle --release --dart-define-from-file=env/prod.json
```

CI-এর জন্য এটা অনেক পরিষ্কার: প্রতি environment-এর জন্য একটা করে file রাখুন। আর CI build করার ঠিক আগে secret থেকে file-টা লিখে দিতে পারে।

**ধাপ ৫ — Compile-time বনাম runtime (মূল পার্থক্য)।**
`--dart-define` হলো **compile-time**। এটা operating system-এর runtime environment variable-এর মতো নয়। তাই `Platform.environment` দিয়ে আপনি dart-define পড়তে পারবেন না — ওটা device-এর OS env var পড়ে, যা সম্পূর্ণ আলাদা জিনিস।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি compile-time বনাম runtime configuration বোঝেন কি না। আর CI দিয়ে inject করে secret কীভাবে source code-এর বাইরে রাখতে হয়, সেটা জানেন কি না।

**সাধারণ ভুল:** `Platform.environment` দিয়ে dart-define পড়ার চেষ্টা করা (ভুল — ওটা runtime OS variable-এর জন্য)। আরেকটা ভুল হলো `env/prod.json` file commit করা, যেখানে আসল production secret থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"dart-define কি আসল secret নিরাপদে রাখতে পারে?"* → আসলে না। এটা binary-র ভেতরে বসে যায়, তাই নাছোড় attacker এটা বের করে আনতে পারে। URL-এর মতো config-এর জন্য ব্যবহার করুন; আসল secret server-এ রাখুন।
- *"int বা bool কীভাবে পড়বেন?"* → `int.fromEnvironment('PORT')` আর `bool.fromEnvironment('FLAG')`, প্রতিটাতে একটা করে `defaultValue` দিয়ে।

**সম্পর্কিত:** [Q5 — flavors বনাম dart-define](#q5) · [Q7 — config class বানানো](#q7) · [Q3 — CI-তে secret](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. প্রতি environment-এর জন্য আলাদা API URL, key আর config কীভাবে সামলান?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি সব environment value একটা config class-এ কেন্দ্রীভূত করি, code-এর নানা জায়গায় URL ছড়িয়ে রাখি না। মানগুলো আসে হয় প্রতি flavor-এর আলাদা `main` entry point থেকে, নয়তো `--dart-define` থেকে। নিয়মটা হলো: config বদলানোর জায়গা একটাই, আর কোনো service class-এর ভেতরে URL কখনোই hardcode নয়।"

**এবার পুরোটা বুঝি:**

একটা বাড়ির **fuse box**-এর কথা ভাবুন। দেয়ালজুড়ে তার এলোমেলো টানার বদলে প্রতিটা circuit একটা লেবেল করা panel-এর ভেতর দিয়ে যায়। কিছু বদলাতে হলে একটাই জায়গায় যেতে হয়। Config class হলো আপনার app-এর setting-এর সেই fuse box।

**ধাপ ১ — উপায় A: entry point দিয়ে সেট করা config class।**
প্রতিটা flavor-এর `main` file config-কে বলে দেয় কোন environment এটা। আর config সঠিক মানগুলো ধরে রাখে।

```dart
enum Environment { dev, staging, prod }

class AppConfig {
  static late Environment env;
  static late String apiUrl;
  static late String apiKey;
  static late bool enableLogging;

  static void init(Environment e) {
    env = e;
    switch (e) {
      case Environment.dev:
        apiUrl = 'https://dev.api.example.com';
        apiKey = 'dev_key_xxx';
        enableLogging = true;
      case Environment.staging:
        apiUrl = 'https://staging.api.example.com';
        apiKey = 'staging_key_xxx';
        enableLogging = true;
      case Environment.prod:
        apiUrl = 'https://api.example.com';
        apiKey = const String.fromEnvironment('PROD_API_KEY'); // CI inject করে
        enableLogging = false;
    }
  }
}
```

```dart
// lib/main_dev.dart
void main() {
  AppConfig.init(Environment.dev);
  runApp(const MyApp());
}
```

খেয়াল করুন, prod key **hardcode করা নেই** — এটা আসে `--dart-define` থেকে, CI inject করে দেয়।

**ধাপ ২ — উপায় B: সবকিছু dart-define থেকে পড়া (একটাই `main`)।**
এই উপায়ে আপনি একটাই `main.dart` রাখেন, আর build-এর সময় সব মান ভেতরে দেন।

```dart
void main() {
  final config = AppConfig(
    apiUrl: const String.fromEnvironment('API_URL'),
    apiKey: const String.fromEnvironment('API_KEY'),
    enableLogs: const bool.fromEnvironment('ENABLE_LOGS'),
  );
  runApp(MyApp(config: config));
}
```

```bash
flutter build appbundle --release --dart-define-from-file=env/dev.json
flutter build appbundle --release --dart-define-from-file=env/staging.json
flutter build appbundle --release --dart-define-from-file=env/prod.json
```

**ধাপ ৩ — CI-তে সবকিছু কীভাবে মেলে।**

```
   CI pipeline
       |
       v
   env/prod.json  --->  --dart-define-from-file
       |                        |
       v                        v
   --flavor prod         Dart const values baked in
       |                        |
       v                        v
   Native: app ID,       Dart: API_URL, API_KEY,
   icon, name            feature flags
```

**ধাপ ৪ — কোন উপায়টা বেছে নেবেন।**
- **উপায় A** ভালো লাগে যখন প্রতিটা environment অনেক দিক থেকে আলাদা, আর আপনি স্পষ্ট entry point রাখতে পছন্দ করেন।
- **উপায় B** CI-এর জন্য ভালো, কারণ সবকিছু একটা file-এর ভেতরে data — code না বদলেই প্রতি environment-এ সহজে অদলবদল করা যায়।

দুটোই একই নীতি মানে: **একটা কেন্দ্রীভূত config**, আর **secret inject করা হবে, commit করা হবে না**।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা যাচাই করেন আপনি পরিষ্কার environment separation design করতে পারেন কি না। Codebase-জুড়ে ছড়ানো hardcoded URL একটা বিপদ সংকেত; কেন্দ্রীভূত ও maintainable config-ই তাঁরা দেখতে চান।

**সাধারণ ভুল:** service class-এর ভেতরে সরাসরি API URL hardcode করা, আর `if/else` দিয়ে সেগুলো বদলানো। আরেকটা গুরুতর ভুল হলো repository-তে production API key রাখা — production secret CI inject করবে, কখনোই commit হবে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"তাহলে prod API key কোথা থেকে আসে?"* → একটা CI secret থেকে, `--dart-define` দিয়ে pass করা হয়। এটা কখনোই source-এ থাকে না।
- *"প্রতি environment-এ আলাদা Firebase project কীভাবে সামলাবেন?"* → প্রতি flavor-এর জন্য আলাদা `google-services.json` / `GoogleService-Info.plist` ব্যবহার করুন। অথবা FlutterFire-এর `flutterfire configure` flavor support সহ ব্যবহার করুন।

**সম্পর্কিত:** [Q5 — flavors](#q5) · [Q6 — dart-define](#q6) · [Q3 — CI secret](#q3)

[↑ উপরে ফিরুন](#toc)

---

# C. Code signing ও obfuscation

---

## <a id="q8"></a>8. Code signing ব্যাখ্যা করুন। Android keystore আর iOS certificate ও provisioning profile কী?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Code signing প্রমাণ করে app-টা আমিই বানিয়েছি, আর কেউ এটা বদলায়নি। এটা public-key cryptography ব্যবহার করে — আমি আমার private key দিয়ে sign করি, আর OS বা store public key দিয়ে verify করে। Android-এ private key থাকে একটা keystore file-এ। iOS-এ লাগে দুটোই — একটা signing certificate, আর একটা provisioning profile যেটা certificate, app ID আর device গুলোকে একসাথে বাঁধে।"

**এবার পুরোটা বুঝি:**

Code signing-কে ভাবুন ওষুধের বোতলের **tamper-proof seal** হিসেবে। Seal দুটো জিনিস প্রমাণ করে: কে বানিয়েছে, আর factory-র পরে কেউ খোলেনি। Seal ভাঙা বা নকল হলে আপনি ওই বোতল বিশ্বাস করবেন না। Phone আর store app-এর ক্ষেত্রে ঠিক এটাই করে — valid seal নেই মানে install নেই।

**ধাপ ১ — ধারণা: private দিয়ে sign, public দিয়ে verify।**
আপনার কাছে একটা private key থাকে (গোপন)। আপনি সেটা দিয়ে app sign করেন। Device বা store-এর কাছে আপনার public key থাকে আর সেটা signature check করে। মিলে গেলে app আসল আর অপরিবর্তিত।

**ধাপ ২ — Android: keystore।**
Keystore (`.jks` বা `.keystore`) হলো একটা file, যেখানে এক বা একাধিক private key থাকে। প্রতিটা key একটা password দিয়ে সুরক্ষিত। আপনি release build করলে Gradle এই keystore-এর একটা key দিয়ে app sign করে। একই app-এর **প্রতিটা update-এ একই keystore ব্যবহার করতেই হবে** — হারিয়ে ফেললে আপনি আর app update করতে পারবেন না (যদি না Play App Signing-এ enroll করা থাকে)।

```bash
# একটা keystore বানান:
keytool -genkey -v \
  -keystore my-release-key.jks \
  -keyalg RSA -keysize 2048 \
  -validity 10000 \
  -alias my-key-alias
```

```properties
# android/key.properties  (কখনোই git-এ commit করবেন না)
storePassword=myStorePass
keyPassword=myKeyPass
keyAlias=my-key-alias
storeFile=../my-release-key.jks
```

```groovy
// android/app/build.gradle — load করে ব্যবহার করুন
def keystoreProperties = new Properties()
keystoreProperties.load(new FileInputStream(rootProject.file("key.properties")))

android {
    signingConfigs {
        release {
            keyAlias keystoreProperties['keyAlias']
            keyPassword keystoreProperties['keyPassword']
            storeFile file(keystoreProperties['storeFile'])
            storePassword keystoreProperties['storePassword']
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
        }
    }
}
```

**ধাপ ৩ — iOS: দুটো অংশ একসাথে কাজ করে।**
iOS signing-এ দুটোই লাগে:
- একটা **signing certificate** (`.p12`) — এতে আপনার private key আর পরিচয় থাকে। এটা প্রমাণ করে *কে* app বানিয়েছে।
- একটা **provisioning profile** — এটা certificate, app ID (bundle ID), অনুমোদিত device গুলো (dev/ad-hoc-এর জন্য) আর app-এর entitlement একসাথে জোড়ে। এটা iOS-কে বলে app *কোথায়* চলতে পারবে আর *কোন* certificate দিয়ে sign করা হয়েছে।

```
  Signing Certificate (.p12)        Provisioning Profile
  +----------------------+          +---------------------------+
  | - Private key        |          | links together:           |
  | - Public key         |  <-----  | - the certificate          |
  | - Your identity      |          | - the App ID (bundle ID)   |
  +----------------------+          | - allowed device UUIDs     |
                                     | - entitlements             |
                                     +---------------------------+

  Profile types:
   - Development -> run on registered test devices
   - Ad Hoc      -> distribute to specific listed devices
   - App Store   -> submit to App Store / TestFlight
   - Enterprise  -> internal company-wide distribution
```

**ধাপ ৪ — Keystore বনাম provisioning profile (এই তুলনাটাই তাঁরা চান)।**

| | Android keystore | iOS provisioning profile |
|---|---|---|
| এটা কী | আপনার private key রাখা একটা file | cert + app ID + device জোড়া লাগানো একটা file |
| পরিচয় প্রমাণ করে? | হ্যাঁ (key app sign করে) | certificate করে; profile সেটাকে অনুমোদন দেয় |
| Device তালিকা থাকে? | না | হ্যাঁ, development / ad-hoc-এর জন্য |
| হারিয়ে ফেললে? | app update করা যাবে না (Play App Signing ছাড়া) | account থেকে আবার তৈরি করে নিন |

**Interviewer কেন জিজ্ঞেস করে:** Junior থেকে mid developer-দের জন্য signing error সবচেয়ে সাধারণ বাধাগুলোর একটা। তাঁরা জানতে চান আপনি এর কাজের নিয়ম বোঝেন কি না, error গুলো সমাধান করতে পারেন কি না, আর team-এর মধ্যে key নিরাপদে সামলাতে পারেন কি না।

**সাধারণ ভুল:** Keystore বা `key.properties` Git-এ commit করা। Play App Signing-এ enroll না করে Android keystore হারিয়ে ফেলা। iOS-এ হাতে হাতে একাধিক distribution certificate বানানো, যেটা সতীর্থদের certificate বাতিল করে দেয় — ঠিক এই ঝামেলাটাই Fastlane match সমাধান করে (দেখুন [Q9](#q9))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Play App Signing কী?"* → আসল signing key Google আপনার হয়ে রাখে। আপনি একটা upload key দিয়ে upload করেন, আর Google আবার sign করে। Upload key হারিয়ে গেলে Google সেটা reset করে দিতে পারে — তাই app স্থায়ীভাবে হারান না।
- *"iOS কেন device UUID-র তালিকা রাখে?"* → Development আর ad-hoc build-এর জন্য profile ঠিক করে বলে দেয় কোন কোন আসল device-এ app চলতে পারবে। App Store build-এ এটা লাগে না, কারণ store সবার কাছে বিতরণ করে।

**সম্পর্কিত:** [Q9 — Fastlane match/supply](#q9) · [Q3 — CI secret হিসেবে keystore](#q3) · [Q14 — iOS distribution cert](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. Fastlane কী? iOS signing-এর জন্য `match` কীভাবে কাজ করে, আর Android deployment-এর জন্য `supply`?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Fastlane এমন একটা tool যেটা mobile app build আর release করা automate করে। আপনি Fastfile নামের একটা Ruby file-এ 'lane' লিখে রাখেন। `match` iOS signing-এর সমস্যা সমাধান করে — এটা একটা private Git repo-তে একটাই shared certificate আর profile-এর set রাখে, তাই প্রতিটা machine একইভাবে sign করে। `supply` আপনার Android app সরাসরি Play Store-এ upload করে।"

**এবার পুরোটা বুঝি:**

Fastlane-কে ভাবুন release-এর জন্য **রেকর্ড করা macro-র একটা সেট** হিসেবে। প্রতিবার হাতে হাতে Xcode আর Play Console-এ click করার বদলে আপনি একটা button চাপেন (`fastlane beta`)। এটা পুরো ধাপগুলো প্রতিবার একইভাবে চালায়।

**ধাপ ১ — Fastfile-এ lane।**
Lane হলো ধাপের একটা নাম দেওয়া ক্রম। আপনি এটা চালান `fastlane <lane>` দিয়ে।

```ruby
# Fastfile
lane :beta do
  match(type: "appstore")       # shared signing asset গুলো নিয়ে আসে
  build_app(scheme: "prod", export_method: "app-store")
  upload_to_testflight
end
```

**ধাপ ২ — iOS signing-এর যে কষ্ট `match` দূর করে।**
Team-এ সবাই নিজের নিজের iOS certificate বানালে সেটা বিশৃঙ্খলা — নতুন distribution certificate বানালে অন্য কারও certificate বাতিল হয়ে যেতে পারে, আর তাঁর build ভেঙে যায়। `match` এটা ঠিক করে **একটাই** certificate আর profile-এর set একটা private, encrypted Git repo-তে রেখে। প্রতিটা developer আর CI machine *একই* asset নিয়ে আসে।

```bash
fastlane match init           # একবারের setup
fastlane match development    # dev profile তৈরি/নিয়ে আসে
fastlane match appstore       # distribution profile তৈরি/নিয়ে আসে
```

```
   Private Git repo (encrypted)
   +-----------------------------+
   | - Certificates (.cer, .p12) |
   | - Provisioning profiles     |
   +--------------+--------------+
                  |
     +------------+------------+
     |            |            |
   Dev A        Dev B       CI Server
   (match)      (match)      (match)
     |            |            |
  same certs   same certs   same certs
```

**ধাপ ৩ — Android upload-এর জন্য `supply`।**
`supply` আপনার APK বা AAB সরাসরি Play-তে upload করে, একটা নির্দিষ্ট track-এ (internal, alpha, beta, production)। এটা store listing, screenshot আর metadata-ও update করতে পারে। এটা একটা **service account JSON key** দিয়ে authenticate করে।

```ruby
lane :deploy_android do
  supply(
    track: "internal",
    aab: "../build/app/outputs/bundle/prodRelease/app-prod-release.aab",
    json_key: "play-store-key.json",   # service account key (একটা CI secret)
    package_name: "com.example.myapp",
  )
end
```

**ধাপ ৪ — `supply` দিয়ে track থেকে track-এ promote করা।**
আপনি আগের একটা build আবার upload না করেই উপরের track-এ তুলতে পারেন।

```ruby
lane :promote do
  supply(
    track: "internal",
    track_promote_to: "production",
    json_key: "play-store-key.json",
    package_name: "com.example.myapp",
  )
end
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা আসল release-automation অভিজ্ঞতা খোঁজেন। হাতে হাতে store upload আর signing করা — team বড় হলে এটা আর টেকে না। Fastlane জানা মানে আপনি পেশাদার setup-এ production app ship করেছেন।

**সাধারণ ভুল:** `match`-কে পুরোনো tool `cert` আর `sigh`-এর সাথে গুলিয়ে ফেলা। ওগুলো প্রতিবার নতুন certificate বানায় আর ঠিক সেই বাতিল হওয়ার ঝামেলা তৈরি করে, যেটা এড়াতেই `match` বানানো হয়েছে। আরেকটা ভুল — Play service-account JSON key CI secret হিসেবে না দিয়ে commit করে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"CI কীভাবে match repo পায়?"* → এটা একটা private Git repo; CI একটা deploy key দিয়ে clone করে, আর match password (একটা secret) দিয়ে asset গুলো decrypt হয়।
- *"Fastlane ব্যবহার করা কি বাধ্যতামূলক?"* → না। Codemagic আর Bitrise-ও signing আর upload করতে পারে, আর store-এর জন্য GitHub Actions আছে। Fastlane শুধু সবচেয়ে প্রচলিত cross-tool সমাধান।

**সম্পর্কিত:** [Q8 — এটা কী sign করছে](#q8) · [Q13 — Play track](#q13) · [Q14 — upload_to_testflight](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. App obfuscation কী? কেন করবেন, আর Flutter-এ কীভাবে enable করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Obfuscation compiled app-এ আপনার class আর method-এর নাম বদলে অর্থহীন নাম বসায়, যেমন `aa`, `b0`। এতে কারও পক্ষে app decompile করে আপনার logic পড়া অনেক কঠিন হয়ে যায়। Flutter-এ এটা enable করবেন `--obfuscate` আর `--split-debug-info` দিয়ে। আর জমানো symbol গুলো রেখে দিতেই হবে, যাতে পরে আসল crash report পড়তে পারেন।"

**এবার পুরোটা বুঝি:**

Obfuscation-কে ভাবুন এভাবে — একটা machine পাঠানোর আগে **সব তারের label ছিঁড়ে ফেলা**। Machine ঠিকঠাক কাজ করে, কিন্তু যে খুলবে সে সহজে বুঝবে না কোন তার কী করে। Wiring diagram (debug symbol) আপনি নিজের কাছে নিরাপদে রাখেন, যাতে *আপনি* এটা মেরামত করতে পারেন।

**ধাপ ১ — এটা কী করে।**
Release binary-তে পড়ার মতো নামগুলোকে ছোট অর্থহীন নাম দিয়ে বদলে দেয়।

```
  Before obfuscation:          After obfuscation:

  class PaymentService {       class a0 {
    void processCard(            void b(
      CardInfo info                c d
    ) {                          ) {
      validateCVV(info);           e(d);
      chargeAmount(info);          f(d);
    }                            }
  }                            }
```

Decompiler এখনো app খুলতে পারবে, কিন্তু code পড়তে অর্থহীন লাগবে — বোঝা অনেক কঠিন।

**ধাপ ২ — কীভাবে enable করবেন।**
`--obfuscate` আর `--split-debug-info` একসাথে দিন। দুটোই লাগবে।

```bash
flutter build apk --release \
  --obfuscate \
  --split-debug-info=build/debug-info/

flutter build appbundle --release \
  --obfuscate \
  --split-debug-info=build/debug-info/

flutter build ipa --release \
  --obfuscate \
  --split-debug-info=build/debug-info/
```

**ধাপ ৩ — `--split-debug-info` কেন লাগে।**
ওই flag debug symbol গুলোকে আলাদা একটা folder-এ বের করে আনে। এই symbol গুলোই হলো অর্থহীন নাম থেকে আসল নামে ফেরার **map**। Crash report পড়তে এই map লাগবে — না হলে crash report শুধু `a0.b()` দেখাবে আর কিছুই বলবে না।

**ধাপ ৪ — আসল crash decode করা।**
Obfuscated নাম সহ crash এলে আপনি জমানো map দিয়ে সেটা "symbolize" করেন।

```bash
flutter symbolize \
  -i crash_stack_trace.txt \
  -d build/debug-info/
# আসল class/method নাম সহ পড়ার মতো stack trace print করে
```

**ধাপ ৫ — Obfuscation যা করে না।**
এটা string **encrypt করে না**। `const apiKey = 'secret123'`-এর মতো literal binary-তে এখনো পড়া যায়। তাই আসল secret কখনোই hardcode করবেন না — সেগুলো server-এ রাখুন। Obfuscation শুধু reverse engineering-এর কষ্ট বাড়ায়; এটা পুরো সুরক্ষা নয়।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা আপনার security সচেতনতা যাচাই করেন। Obfuscation ছাড়া ship করা একটা ঝুঁকি, বিশেষ করে fintech, health বা enterprise app-এর জন্য। Symbol গুলো archive করার কথা জানা মানে আপনি শুধু build নয়, production-এ app সামলানোর কথাও ভাবেন।

**সাধারণ ভুল:** `--split-debug-info` ছাড়া `--obfuscate` ব্যবহার করা (build fail করে — দুটোই লাগে)। আরেকটা ভুল — build-এর পরে `debug-info` folder ফেলে দেওয়া। এটা ছাড়া আপনি production crash কখনোই symbolize করতে পারবেন না — তাই CI-তে build artifact-এর পাশে সবসময় এটা archive করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Obfuscation কি আমার API key লুকায়?"* → না। String literal পড়া যায়ই। আসল secret server-side রাখুন।
- *"Symbol গুলো কোথায় রাখেন?"* → CI artifact হিসেবে upload করুন, আর আপনার crash tool-এ (যেমন Crashlytics/Sentry) দিন, যাতে সেটা নিজে থেকেই de-obfuscate করতে পারে।

**সম্পর্কিত:** [Q1 — release build](#q1) · [Q3 — CI-তে symbol archive করা](#q3)

[↑ উপরে ফিরুন](#toc)

---

# D. Store release ও distribution

---

## <a id="q11"></a>11. Build artifact কী? APK আর AAB-এর পার্থক্য ব্যাখ্যা করুন, আর কেন Google Play AAB পছন্দ করে।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Build artifact মানে build যা কিছু তৈরি করে — APK, AAB, IPA, symbol, test report। Android-এর জন্য বড় দুটো হলো APK আর AAB। APK একটা single installable file, যাতে সব device-এর জন্য সবকিছু থাকে। AAB একটা upload format — এটা আমি Google Play-কে দিই, আর Play প্রতিটা user-এর device-এর জন্য ছোট, optimized APK তৈরি করে।"

**এবার পুরোটা বুঝি:**

ব্যাপারটা **আসবাব পাঠানোর** মতো ভাবুন। APK হলো সব কাপড় আর সব সাইজে বানানো একটা পুরো sofa, সব এক বিশাল বাক্সে ভরা — customer শুধু একটা দরকার হলেও পুরোটা টেনে বাড়ি নেয়। AAB হলো flat-pack: আপনি যন্ত্রাংশ গুদামে (Google Play) পাঠান, আর সেটা ঠিক ওই একটা sofa জোড়া দেয় যেটা প্রতিটা customer-এর ঘরে ফিট করে। ডেলিভারি ছোট, ফল একই।

**ধাপ ১ — APK: একটা file, ভেতরে সবকিছু।**
একটা APK-তে থাকে প্রতিটা CPU architecture-এর compiled code, প্রতিটা screen density-র resource, আর প্রতিটা ভাষা। User পুরোটাই download করে, এমনকি যে অংশ কখনোই কাজে লাগবে না সেটাও। APK সরাসরি device-এ install করা যায় (sideload)।

**ধাপ ২ — AAB: একটা publishing format, সরাসরি install হয় না।**
আপনি AAB-টা Play-তে upload করেন। Play তারপর প্রতিটা device-এর জন্য optimized "split" APK তৈরি করে। একজন Pixel 7 user শুধু arm64 code, শুধু তাঁর screen density, শুধু তাঁর ভাষা download করেন — download অনেক ছোট।

```
  APK (one big file):
  +----------------------------------+
  | code: arm, arm64, x86, x86_64    |
  | resources: mdpi..xxxhdpi         |
  | strings: en, es, fr, de, ja ...  |
  | total ~25 MB                     |
  +----------------------------------+
        user downloads ALL of it

  AAB (Google splits it for each device):
  +----------------------------------+
  |  upload AAB to Play Store        |
  +---------------+------------------+
                  |  Play generates splits
   +-----------+  +-----------+  +-------------+
   | Pixel 7   |  | Galaxy S23|  | budget phone|
   | arm64     |  | arm64     |  | arm         |
   | xxhdpi    |  | xxxhdpi   |  | hdpi        |
   | en only   |  | ko only   |  | es only     |
   | ~10 MB    |  | ~11 MB    |  | ~8 MB       |
   +-----------+  +-----------+  +-------------+
```

**ধাপ ৩ — Build command গুলো।**

```bash
# APK (সরাসরি install, QA, sideloading-এর জন্য):
flutter build apk --release
# output: build/app/outputs/flutter-apk/app-release.apk

# AAB (Play Store-এর জন্য):
flutter build appbundle --release
# output: build/app/outputs/bundle/release/app-release.aab
```

**ধাপ ৪ — নতুন app-এর জন্য Play কেন AAB বাধ্যতামূলক করে।**
২০২১ সালের August থেকে Play সব নতুন app-এর জন্য AAB চায়। মূল কারণ হলো **ছোট download** — ছোট download মানে বেশি মানুষ install শেষ করেন আর কম storage লাগে। Google-এর হিসাবে গড়ে প্রায় 15% size কমে। AAB on-demand feature delivery আর বড় asset delivery-ও সম্ভব করে।

**ধাপ ৫ — কখন এখনো APK দরকার হয়।**
- Firebase App Distribution আর সরাসরি QA testing (দেখুন [Q12](#q12))।
- Enterprise sideloading।
- যেসব app store AAB support করে না।
- Development-এর সময় local device testing।

**Interviewer কেন জিজ্ঞেস করে:** এটা Android-এর ভিত্তি জ্ঞান। তাঁরা আশা করেন আপনি জানবেন AAB কেন আছে, আর কখন APK বনাম AAB ব্যবহার করবেন। এটা app-size optimization-এর সাথেও যুক্ত, যা install conversion-এ প্রভাব ফেলে।

**সাধারণ ভুল:** APK আর AAB-কে একে অপরের বদলে ব্যবহারযোগ্য ভাবা। AAB device-এ sideload করার চেষ্টা করা (পারবেন না — এটা installable নয়)। নতুন app-এর জন্য Play-তে APK upload করা (reject হবে)। আরেকটা ভুল — বুঝতে না পারা যে AAB-এর জন্য Play App Signing দিয়ে Google-কে আপনার app sign করতে হয়, যা নিয়ে কিছু team দ্বিধায় থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একজন user AAB থেকে আসলে কী পান, সেটা আমি কীভাবে test করব?"* → `bundletool` দিয়ে আপনার AAB থেকে device-specific APK তৈরি করুন, অথবা Play-র internal testing track ব্যবহার করুন।
- *"আমি কি এখনো একটা single universal APK পেতে পারি?"* → হ্যাঁ, `bundletool` test করার জন্য AAB থেকে একটা universal APK বানাতে পারে।

**সম্পর্কিত:** [Q1 — release build](#q1) · [Q12 — tester-দের জন্য APK](#q12) · [Q13 — AAB upload করা](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. Test build বিলি করার জন্য Firebase App Distribution কীভাবে কাজ করে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Firebase App Distribution pre-release build — APK, AAB বা IPA — সরাসরি tester-দের কাছে পাঠায়, app store বাদ দিয়ে। Tester-রা একটা email বা in-app prompt পান, link-এ tap করেন, আর install করেন। QA-র কাছে দ্রুত build পৌঁছাতে এটা দারুণ। iOS-এর ঝামেলাটা হলো: tester-দের device UDID ad-hoc provisioning profile-এ থাকতে হবে।"

**এবার পুরোটা বুঝি:**

এটাকে ভাবুন **দোকানের তাকে পণ্য না রেখে দরজায় দাঁড়িয়ে ফ্রি sample বিলি করার** মতো। কে sample পাবে সেটা আপনি ঠিক করেন (tester group), সাথে একটা নোট দেন ("নতুন login টা দেখুন"), আর তাঁরা সাথে সাথেই পেয়ে যান — store approval-এর জন্য অপেক্ষা নেই।

**ধাপ ১ — পুরো flow।**

```
  Developer / CI
       |
       v
   Build APK / IPA
       |
       v
   Upload to Firebase App Distribution
   (CLI, Fastlane plugin, or console)
       |
       v
   Firebase emails the tester groups
       |
       v
   Testers:
    - Android: tap link -> install APK
    - iOS: device UDID must be in the ad-hoc profile -> install IPA
```

**ধাপ ২ — Firebase CLI দিয়ে upload।**

```bash
npm install -g firebase-tools

firebase appdistribution:distribute \
  build/app/outputs/flutter-apk/app-release.apk \
  --app YOUR_FIREBASE_APP_ID \
  --groups "qa-team,designers" \
  --release-notes "Fixed login bug, added dark mode"
```

**ধাপ ৩ — Fastlane দিয়ে upload (CI-তে সুবিধাজনক)।**

```ruby
lane :distribute do
  firebase_app_distribution(
    app: "1:1234567890:android:abc123",
    groups: "qa-team",
    release_notes: "Build from CI ##{ENV['BUILD_NUMBER']}",
    apk_path: "../build/app/outputs/flutter-apk/app-release.apk",
  )
end
```

**ধাপ ৪ — iOS-এর ফাঁদটা (খুব গুরুত্বপূর্ণ)।**
iOS-এ আপনাকে একটা **ad-hoc** build বিলি করতে হবে, যার provisioning profile-এ প্রতিটা tester-এর device UDID তালিকাভুক্ত থাকে। Firebase তার onboarding flow দিয়ে UDID সংগ্রহ করতে পারে। তবু নতুন tester যোগ হলেই আপনাকে profile আবার তৈরি করে rebuild করতে হবে। UDID সামলানো এড়াতে চাইলে বরং **TestFlight** ব্যবহার করুন (দেখুন [Q14](#q14)) — সেখানে device registration লাগে না।

**Interviewer কেন জিজ্ঞেস করে:** QA-র কাছে দ্রুত build পৌঁছানো দ্রুত iteration-এর জন্য খুব জরুরি। তাঁরা দেখতে চান আপনি এর একটা পরিষ্কার উপায় জানেন কি না — চারদিকে APK file email করা নয়।

**সাধারণ ভুল:** iOS-এ ভুলে যাওয়া যে ad-hoc distribution-এর জন্য profile-এ device UDID লাগে। আরেকটা ভুল — **App Store** profile দিয়ে sign করা IPA Firebase-এ upload করা। ওটা device-এ install হবে না, কারণ App Store profile শুধু TestFlight আর App Store দিয়েই কাজ করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Firebase App Distribution বনাম TestFlight?"* → Firebase Android আর iOS দুটোতেই কাজ করে এবং দ্রুত, কিন্তু iOS-এ ad-hoc-এর জন্য UDID লাগে। TestFlight শুধু iOS-এর জন্য, UDID লাগে না, কিন্তু external testing-এর জন্য Beta App Review লাগে।
- *"Tester invite কি automate করা যায়?"* → হ্যাঁ — tester group আর CI-তে CLI/Fastlane step থাকলে প্রতিটা build-এ invite নিজে থেকেই চলে যায়।

**সম্পর্কিত:** [Q11 — tester-দের জন্য APK](#q11) · [Q14 — TestFlight](#q14) · [Q8 — ad-hoc profile](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. Google Play Store-এ app কীভাবে submit করবেন? Track গুলো ব্যাখ্যা করুন: internal, alpha, beta, production।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Play release-গুলোকে track-এ সাজায় — internal, closed (alpha), open (beta), আর production — প্রতিটাই rollout-এর এক একটা পর্যায়। আপনি একটা track-এ AAB upload করেন, আর শুধু ওই track-এর user-রাই সেটা পান। Production-এ staged rollout আছে, তাই আমি আগে অল্প শতাংশ user-কে release দিতে পারি আর কিছু ভাঙলে থামিয়ে দিতে পারি।"

**এবার পুরোটা বুঝি:**

Track গুলোকে ভাবুন **রান্নাঘর থেকে ধাপে ধাপে খাবার বের করার** মতো। প্রথমে বাবুর্চি নিজে চেখে দেখেন (internal), তারপর কয়েকজন বিশ্বস্ত নিয়মিত খদ্দের (alpha), তারপর আগ্রহী যে কারো জন্য soft launch (beta), আর শেষে সেটা সবার জন্য মূল menu-তে ওঠে (production)। প্রতিটা পর্যায় আরও বেশি মানুষ ক্ষতিগ্রস্ত হওয়ার আগেই সমস্যা ধরে ফেলে।

**ধাপ ১ — চারটা track।**

```
  Track          Testers           Review      Use case
  -----          -------           ------      --------
  Internal       up to 100 emails  none        quick smoke tests by the team
  Closed/Alpha   unlimited*        none        wider internal / external QA
  Open/Beta      unlimited         none        public beta, anyone opts in
  Production     all users         review**    full public release

  *  via invite link or tester lists
  ** first submission needs a full review; updates can be faster
```

**ধাপ ২ — Submission-এর ধাপগুলো।**
1. একটা signed AAB build করুন: `flutter build appbundle --release`।
2. Play Console-এ আপনার পছন্দের track-এ একটা নতুন release তৈরি করুন।
3. AAB upload করুন। Play সেটা process করে প্রতিটা device-এর জন্য optimized APK প্রস্তুত করে।
4. Release notes যোগ করুন।
5. Review করে roll out করুন। Production-এর ক্ষেত্রে প্রথম release-এ পুরো review লাগে (listing, content rating, privacy policy, ইত্যাদি)।

**ধাপ ৩ — Staged rollout (production-এর একটা মূল feature)।**
Production release-এ staged rollout আছে। আপনি 5% user-কে release দিতে পারেন, crash rate আর ANR দেখতে পারেন, তারপর ধীরে ধীরে সেটা 100% পর্যন্ত বাড়াতে পারেন। কিছু ভুল থাকলে rollout থামিয়ে দিন, তাহলে বাকি user-রা খারাপ build-টা কখনোই পাবেন না।

**ধাপ ৪ — Track-এর মধ্যে promote করা।**

```
  Internal --> Closed/Alpha --> Open/Beta --> Production
     |              |              |             |
  100 testers    QA team      public beta    all users
  no review      no review    no review      full review
```

```ruby
# Fastlane supply দিয়ে promote (আবার upload লাগে না):
supply(
  track: "internal",
  track_promote_to: "beta",
  json_key: "play-store-key.json",
)
```

**Interviewer কেন জিজ্ঞেস করে:** Play release pipeline জানা মানে আপনি পেশাদারভাবে app ship করেছেন। তাঁরা প্রায়ই staged rollout নিয়ে জিজ্ঞেস করেন, আর খারাপ release কীভাবে সামলাবেন সেটাও। Rollout থামাতে পারা operational সচেতনতা দেখায়।

**সাধারণ ভুল:** AAB-এর বদলে APK upload করা (নতুন app-এর জন্য Play AAB চায়)। বুঝতে না পারা যে internal track-এ সর্বোচ্চ 100 tester, তাই বড় QA team-এর জন্য এটা মানানসই নয় — তার জন্য closed testing ব্যবহার করুন। আর upload করার আগে `versionCode` বাড়াতে ভুলে যাওয়া, যাতে upload reject হয়ে যায় (দেখুন [Q4](#q4))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Internal আর closed testing-এর পার্থক্য কী?"* → Internal-এ email দিয়ে সর্বোচ্চ 100 tester, আর সাথে সাথেই পাওয়া যায়। Closed (alpha)-তে অনেক বেশি tester রাখা যায় এবং এটা বৃহত্তর QA-র জন্য, তবু কোনো public review ছাড়াই।
- *"খারাপ release কীভাবে roll back করবেন?"* → আসলে কোনো release মুছে ফেলা যায় না, কিন্তু staged rollout থামিয়ে দিয়ে fix সহ নতুন, বেশি version-এর একটা build push করা যায়।

**সম্পর্কিত:** [Q11 — AAB upload](#q11) · [Q4 — versionCode বাড়াতেই হবে](#q4) · [Q9 — supply automation](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. Apple App Store-এ app কীভাবে submit করবেন? TestFlight-এর flow বর্ণনা করুন।

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-10-cicd-release.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"সবকিছু App Store Connect-এর ভেতর দিয়ে যায়। প্রথমে আমি একটা signed IPA upload করি। Pre-release testing সামলায় TestFlight — internal tester-রা সাথে সাথেই পায়, external tester-দের জন্য একটা ছোট Beta App Review লাগে। তারপর public release-এর জন্য store listing পূরণ করে App Review-তে submit করি, যেটাতে সাধারণত এক-দুই দিন লাগে।"

**এবার পুরোটা বুঝি:**

Apple-এর process-কে Google-এর চেয়ে **আরও কড়া customs office** ভাবুন। আপনার beta tester-রাও (external) package পাওয়ার আগে একটা ছোট পরীক্ষা পার হয়। আর শেষ public release সবসময় একটা পূর্ণ পরীক্ষার ভেতর দিয়ে যায়। ঝামেলা বেশি, কিন্তু ধাপগুলো একবার জেনে গেলে সেগুলো অনুমান করা যায়।

**ধাপ ১ — Signed IPA build করুন আর upload করুন।**
আপনি **distribution** certificate আর App Store provisioning profile দিয়ে build করেন। সাধারণত একটা `ExportOptions.plist` দিতে হয়, যাতে archive সঠিকভাবে sign হয়।

```bash
# IPA build করুন:
flutter build ipa --release \
  --export-options-plist=ios/ExportOptions.plist

# এটা upload করুন (CLI):
xcrun altool --upload-app \
  -f build/ios/ipa/MyApp.ipa \
  -t ios \
  --apiKey YOUR_KEY_ID \
  --apiIssuer YOUR_ISSUER_ID

# অথবা Fastlane দিয়ে:
upload_to_testflight
```

**ধাপ ২ — TestFlight-এর flow।**

```
  Build IPA (signed with App Store cert)
       |
       v
  Upload to App Store Connect
       |
       v
  Apple processes the build (5-30 min)
       |
       +--> Internal testing
       |     - up to 100 of your Apple Developer team
       |     - NO Apple review
       |     - available right after processing
       |
       +--> External testing
             - up to 10,000 testers (email or link)
             - needs Beta App Review (usually < 24 hrs)
             - testers install via the TestFlight app
             - each build expires after 90 days
```

**ধাপ ৩ — Public App Store-এ submit করা।**
Testing শেষ হলে:
1. App Store Connect-এ build-টি select করুন।
2. Metadata পূরণ করুন — description, screenshot, keyword, privacy policy URL, category।
3. App Review-তে submit করুন (সাধারণত 24–48 ঘণ্টা)।
4. Approve হলে সাথে সাথে release করুন, বা নির্দিষ্ট দিনে, বা হাতে হাতে।

**ধাপ ৪ — Google Play-র সাথে মূল পার্থক্য।**
- Apple **external** TestFlight build-এর জন্যও review চায়; Google-এর track test build review করে না।
- Google-এর review-ছাড়া internal track-এর মতো কিছু Apple-এ নেই, শুধু আপনার নিজের developer account-এর সদস্যরা ছাড়া।
- সব iOS test build **90 দিন পরে expire** হয়।
- শতাংশভিত্তিক staged rollout নেই; iOS-এ এর বদলে production-এর জন্য 7 দিনের **phased release** আছে।

**Interviewer কেন জিজ্ঞেস করে:** iOS submission-এ Android-এর চেয়ে বেশি ঝামেলা, আর এটা অনেক developer-কে বিভ্রান্ত করে। তাঁরা দেখতে চান আপনি পুরো cycle পার করেছেন কি না — build, sign, upload, TestFlight, review, release। এটা আসল shipping অভিজ্ঞতার শক্ত সংকেত।

**সাধারণ ভুল:** ভুলে যাওয়া যে external TestFlight-এর জন্য Beta App Review লাগে। **distribution**-এর বদলে **development** certificate দিয়ে sign করা — upload সফল হয়, কিন্তু processing fail করে। `ExportOptions.plist` না দেওয়া, যার ফলে `flutter build ipa` ভুলভাবে signed archive বানায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Internal vs external TestFlight?"* → Internal = আপনার team-এর সর্বোচ্চ 100 জন, review নেই, সাথে সাথে। External = সর্বোচ্চ 10,000 tester, কিন্তু Beta App Review লাগে।
- *"Phased release কী?"* → Production update ধীরে ধীরে 7 দিনে ছাড়ার Apple-এর উপায়, মাঝপথে থামানোর সুযোগসহ — Google-এর staged rollout-এর সবচেয়ে কাছের জিনিস।

**সম্পর্কিত:** [Q8 — distribution cert ও profile](#q8) · [Q9 — upload_to_testflight](#q9) · [Q12 — Firebase vs TestFlight](#q12)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার টেবিল, তারপর এক লাইনের মনে করিয়ে দেওয়া কথাগুলো।

## দ্রুত তুলনার টেবিল

**Build mode: debug vs profile vs release**

| | Debug | Profile | Release |
|---|---|---|---|
| Compilation | JIT | AOT (native) | AOT (native) |
| Hot reload | হ্যাঁ | না | না |
| গতি | ধীর | বাস্তবসম্মত | দ্রুত |
| কীসের জন্য | code লেখা | গতি মাপা | ship করা |

**Flavor: dev vs staging vs prod**

| | dev | staging | prod |
|---|---|---|---|
| App ID | `.dev` suffix | `.staging` suffix | আসল ID |
| API | dev server | staging server | live server |
| Logs | চালু | চালু | বন্ধ |
| কে ব্যবহার করে | developer-রা | QA / manager | আসল user-রা |

**Android keystore vs iOS provisioning profile**

| | Android keystore | iOS provisioning profile |
|---|---|---|
| কী জিনিস | আপনার private key আছে এমন file | cert + app ID + device যুক্ত করে |
| Device-এর তালিকা রাখে? | না | হ্যাঁ (dev / ad-hoc) |
| হারিয়ে গেলে | update করা যাবে না (Play App Signing না থাকলে) | আবার generate করলেই হয় |
| Git-এ রাখবেন? | কখনোই না | কখনোই না |

**Firebase App Distribution vs TestFlight**

| | Firebase App Distribution | TestFlight |
|---|---|---|
| Platform | Android + iOS | শুধু iOS |
| iOS device UDID | লাগে (ad-hoc) | লাগে না |
| Apple review | না | external tester-দের লাগে |
| Build expiry | নেই | 90 দিন |

## এক লাইনের মনে করিয়ে দেওয়া কথা

- **Build mode**: debug = code লেখা, profile = গতি মাপা, release = ship করা। Debug-এ কখনোই গতি বিচার করবেন না। ([Q1](#q1))
- **CI**: `.github/workflows/`-এ YAML; Android চলে Linux-এ, iOS চলে macOS-এ; artifact সবসময় upload করুন। ([Q2](#q2))
- **Secret** কখনোই Git-এ যায় না — CI secret হিসেবে রাখুন, file base64 থেকে decode করুন, SDK আর pub cache করুন। ([Q3](#q3))
- **Version `1.2.3+45`**: `+`-এর আগের অংশ name (user এটা দেখে), `+`-এর পরের build number সবসময় বাড়তে হবে। ([Q4](#q4))
- **Flavor** = native পার্থক্য (app ID, icon, name)। **dart-define** = Dart-এ compile-time মান। দুটোই ব্যবহার করুন। ([Q5](#q5), [Q6](#q6))
- **একটাই config class**; prod secret dart-define দিয়ে inject করুন; service-এ URL কখনোই hardcode করবেন না। ([Q7](#q7))
- **Code signing** = tamper-proof সিল। Android = keystore; iOS = certificate + provisioning profile। ([Q8](#q8))
- **Fastlane match** = private repo-তে iOS cert-এর একটাই শেয়ার করা set। **supply** = Play-তে AAB upload করা। ([Q9](#q9))
- **Obfuscate** করুন `--obfuscate --split-debug-info` দিয়ে; crash `flutter symbolize` করার জন্য symbol রেখে দিন। ([Q10](#q10))
- **APK** = একটা install করার মতো file। **AAB** = upload-এর format; Play প্রতি device-এর জন্য ছোট download বানায়। ([Q11](#q11))
- **Firebase App Distribution**: দ্রুত test build; iOS-এ ad-hoc profile-এ UDID লাগে। ([Q12](#q12))
- **Play track**: internal → alpha → beta → production; production-এ staged rollout আছে (খারাপ build থামানো যায়)। ([Q13](#q13))
- **App Store**: IPA upload → TestFlight (external-এর জন্য Beta Review লাগে) → App Review → release; build 90 দিনে expire হয়। ([Q14](#q14))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যান

Interviewer-রা এক প্রশ্নে থামেন না। আপনার গভীরতা মাপতে তাঁরা খুঁড়তেই থাকেন। এই চেইনটা মুখে বলে অনুশীলন করুন — শান্তভাবে, ধাপে ধাপে:

1. *"dev, staging আর prod কীভাবে সেট করেন?"* → native পার্থক্যের জন্য flavor (app ID, icon), Dart config-এর জন্য dart-define (API URL)।
2. *"সবকিছুর জন্য শুধু dart-define কেন নয়?"* → dart-define app ID, icon বা native resource বদলাতে পারে না — শুধু flavor পারে।
3. *"Prod API key নিরাপদ থাকে কীভাবে?"* → এটা একটা CI secret, dart-define দিয়ে inject হয়, কখনোই Git-এ commit হয় না।
4. *"সেই key CI build-এ পৌঁছায় কীভাবে?"* → CI secret হিসেবে রাখা থাকে, build-এর সময় পড়া হয়; keystore-এর মতো file runner-এ base64 থেকে decode হয়।
5. *"Prod build user-দের কাছে কীভাবে পাঠাবেন?"* → signed AAB build করব, Play-র internal track-এ upload করব, তারপর staged rollout দিয়ে production পর্যন্ত promote করব।

এভাবে শান্তভাবে ধাপে ধাপে যেতে পারা — অনুমান না করে — এটাই আপনাকে **senior** শোনায়, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)

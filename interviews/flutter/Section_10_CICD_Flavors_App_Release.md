# Section 10 — CI/CD, Flavors & App Release

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a detailed, step-by-step explanation with real-life examples and code.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** Always give the **short answer first** (2–3 sentences), then stop. Let the interviewer ask "can you go deeper?" Speaking simply and clearly is itself a senior skill — and it works the same for both remote and BD companies.

---

<a id="toc"></a>

## Table of Contents

**A. Build modes & CI/CD basics**
1. [Build modes — debug, profile, release](#q1) · *Very common*
2. [Basic CI pipeline with GitHub Actions](#q2) · *Very common*
3. [CI secrets, caching & speeding up builds](#q3) · *Common*
4. [App versioning — `1.0.0+1` and auto-increment](#q4) · *Very common*

**B. Flavors & environments**
5. [Flavors — dev / staging / prod (Android & iOS)](#q5) · *Very common*
6. [`--dart-define` and build-time variables](#q6) · *Very common*
7. [Managing API URLs, keys & configs per environment](#q7) · *Common*

**C. Code signing & obfuscation**
8. [Code signing — Android keystore & iOS profiles](#q8) · *Very common*
9. [Fastlane — `match` (iOS) and `supply` (Android)](#q9) · *Common*
10. [App obfuscation & symbolizing crashes](#q10) · *Common*

**D. Store release & distribution**
11. [APK vs AAB — and why Play prefers AAB](#q11) · *Very common*
12. [Firebase App Distribution for test builds](#q12) · *Common*
13. [Google Play release — internal / alpha / beta / production](#q13) · *Very common*
14. [Apple App Store & the TestFlight flow](#q14) · *Very common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 14 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — The foundation (start here).** You can't talk about release without these.
→ [Q1 Build modes](#q1) · [Q4 Versioning](#q4) · [Q5 Flavors](#q5) · [Q6 dart-define](#q6)

**Stage 2 — Get a build out the door.** The everyday CI work.
→ [Q2 GitHub Actions CI](#q2) · [Q3 Secrets & caching](#q3) · [Q7 Env config](#q7)

**Stage 3 — Signing (the part that breaks the most).**
→ [Q8 Code signing](#q8) · [Q9 Fastlane](#q9) · [Q10 Obfuscation](#q10)

**Stage 4 — Ship to users.** The store-release pipeline.
→ [Q11 APK vs AAB](#q11) · [Q12 Firebase App Distribution](#q12) · [Q13 Google Play tracks](#q13) · [Q14 App Store & TestFlight](#q14)

**Short on time (1 hour before the interview)?** Just review these six:
[Q1](#q1) · [Q4](#q4) · [Q5](#q5) · [Q6](#q6) · [Q8](#q8) · [Q11](#q11), then read the [Cheat Sheet](#cheatsheet).

---

# A. Build modes & CI/CD basics

---

<a id="q1"></a>
## 1. What are Flutter's build modes? Explain debug, profile, and release.

> Very common · Easy–Medium

**Short answer (say this):**
"Flutter has three build modes. Debug is for daily coding — it has hot reload and lots of checks, but it's slow. Profile is for measuring performance — it runs like release but keeps the profiling tools on. Release is what real users get — it's compiled to native code, small and fast. The big rule: never judge speed from a debug build."

**Let's understand it fully:**

Think of these three modes like the three stages of building a car. The **garage prototype** (debug) is easy to tinker with but not road-ready. The **test track car** (profile) is the real car with sensors attached to measure it. The **showroom car** (release) is clean, fast, and sold to customers.

**Step 1 — Debug mode (for coding).**
This is the default when you press Run. It uses JIT compilation, which is what makes **hot reload** work. It also turns on `assert`s and extra checks that catch bugs early. The trade-off: it is much slower and the app is much bigger.

```bash
flutter run                 # debug is the default
flutter run --debug         # same thing, explicit
```

**Step 2 — Profile mode (for measuring speed).**
Profile mode compiles to native code (AOT) like release, so the speed is realistic. But it keeps some tooling on so you can use DevTools to find slow frames (jank). You cannot hot reload in profile mode.

```bash
flutter run --profile       # realistic speed + profiling tools
```

You use this when someone says "the app feels laggy" — you profile it to find the real cause, instead of guessing.

**Step 3 — Release mode (for users).**
This is what you ship. It uses AOT (compiled to native machine code before running), strips out `assert`s and debug info, and tree-shakes unused code. The result is a small, fast app. There is no hot reload and no debugging tools.

```bash
flutter run --release       # what users experience
flutter build apk --release
flutter build appbundle --release
flutter build ipa --release
```

**Step 4 — A quick comparison.**

| | Debug | Profile | Release |
|---|---|---|---|
| Compilation | JIT | AOT (native) | AOT (native) |
| Hot reload | yes | no | no |
| Asserts / checks | on | off | off |
| Speed | slow | realistic | fast |
| Use for | coding | measuring performance | shipping to users |

**Why interviewers ask:** A very common junior mistake is complaining about lag in a debug build. Knowing the three modes — and that profile is the right one for measuring — is a clear senior signal.

**Common mistake:** Measuring performance in debug mode and trying to "optimize" things that are only slow because of debug checks. Many "performance bugs" simply disappear in release or profile mode.

**Follow-ups they may ask:**
- *"Why is debug slower?"* → JIT compiles while running, plus all the asserts and checks add overhead.
- *"When do you use profile over release?"* → When you need to measure speed but still want DevTools attached. Release has the tools stripped out.

**Related:** [Q11 — APK vs AAB output](#q11) · [Q10 — release obfuscation](#q10)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. How do you set up a basic CI pipeline for Flutter using GitHub Actions?

> Very common · Medium

**Short answer (say this):**
"CI means: every time I push code, a server automatically checks it. For Flutter I write a YAML file in `.github/workflows/`. The pipeline usually does four steps — get the code, install Flutter, run analyze and tests, then build the app. Android builds run on a Linux machine; iOS builds need a macOS machine."

**Let's understand it fully:**

Think of CI/CD as a **factory conveyor belt**. You drop your code on one end (a push), and it moves through stations — checking, testing, packing — without anyone touching it by hand. At the end, a finished, tested build comes out. The whole point is to catch problems automatically and the same way every time.

**Step 1 — Where the file lives.**
GitHub Actions reads YAML files from the `.github/workflows/` folder in your repo. Each file is one pipeline (called a "workflow").

**Step 2 — When it runs (the trigger).**
You say what events start the belt — usually a push to `main` and every pull request.

```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
```

**Step 3 — The stations (a full working example).**

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
    runs-on: ubuntu-latest          # Linux is fine for Android
    steps:
      - uses: actions/checkout@v4    # 1. get the code

      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.24.0'  # pin a version for repeatable builds
          channel: 'stable'
          cache: true                # cache the SDK between runs

      - name: Install dependencies
        run: flutter pub get

      - name: Analyze code
        run: flutter analyze --fatal-infos   # fail on warnings too

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

**Step 4 — Why iOS is different.**
You cannot build an iOS app on Linux, because it needs Xcode, which only runs on macOS. So the iOS job must use a macOS machine and set up code signing first.

```yaml
jobs:
  ios-build:
    runs-on: macos-latest            # iOS REQUIRES macOS
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.24.0'
          channel: 'stable'
      - run: flutter pub get
      # ... install certificates & provisioning profiles here (see Q8/Q9) ...
      - run: flutter build ipa --release
```

**Step 5 — Save the result (artifacts).**
When the run finishes, the build machine is destroyed. So you must **upload the APK/IPA as an artifact** (last step above), or your build is gone.

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

**Why interviewers ask:** CI is expected in any professional Flutter team. They want to see you can automate checks and builds, not just write features. Knowing the YAML shape, caching, and artifacts shows production readiness.

**Common mistake:** Trying to build iOS on a Linux runner — it will fail because there is no Xcode. Also, forgetting to upload the artifact, so the build is lost when the machine is destroyed.

**Follow-ups they may ask:**
- *"What is the difference between CI and CD?"* → CI = automatically build and test. CD = automatically deliver/deploy that build (to testers or the store).
- *"GitHub Actions vs Codemagic vs Bitrise?"* → GitHub Actions is general-purpose and free for many repos. Codemagic and Bitrise are mobile-focused and handle Mac machines and signing more easily out of the box.

**Related:** [Q3 — secrets & caching](#q3) · [Q9 — Fastlane for store upload](#q9) · [Q4 — build number in CI](#q4)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. How do you handle secrets in CI, and how do you speed up Flutter builds?

> Common · Medium

**Short answer (say this):**
"Secrets — like keystores, API keys, and store credentials — must never be committed to Git. I store them as CI secrets and inject them at build time, often as base64-encoded files. To speed builds up, I cache the Flutter SDK and pub packages, pin the Flutter version, and split work into parallel jobs."

**Let's understand it fully:**

**Step 1 — The golden rule: secrets never live in the repo.**
If a password or key is in Git, anyone who reads the code has it forever — even after you delete it (it stays in history). So secrets go into the CI provider's secret store and are read as environment variables at build time.

**Step 2 — Reading secrets in GitHub Actions.**
You add them in the repo's Settings → Secrets, then read them with `${{ secrets.NAME }}`.

```yaml
- name: Build signed APK
  env:
    KEY_PASSWORD: ${{ secrets.ANDROID_KEY_PASSWORD }}
    STORE_PASSWORD: ${{ secrets.ANDROID_STORE_PASSWORD }}
  run: flutter build appbundle --release
```

**Step 3 — Files as secrets (base64 trick).**
A keystore or a Google Play JSON key is a file, but secret stores hold text. So you encode the file to a base64 string, save that string as a secret, and decode it back to a file on the machine.

```bash
# On your computer, turn the file into one line of text:
base64 -i my-release-key.jks | pbcopy      # then paste into a CI secret
```

```yaml
- name: Restore keystore from secret
  run: echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 --decode > android/app/release.jks
```

**Step 4 — Speed: cache things that don't change.**
Most of a CI run is re-downloading the same files. Cache them.

```yaml
- uses: subosito/flutter-action@v2
  with:
    flutter-version: '3.24.0'
    cache: true                 # caches the Flutter SDK

- name: Cache pub packages
  uses: actions/cache@v4
  with:
    path: ~/.pub-cache
    key: pub-${{ hashFiles('pubspec.lock') }}
```

**Step 5 — Other speed wins.**
- **Pin the Flutter version** (`3.24.0`, not `stable`) so builds are repeatable and the cache hits.
- **Run jobs in parallel** — analyze, test, and build can run at the same time on separate machines.
- **Only build what changed** — for example, run the iOS job only when iOS files change.
- **Use `--no-pub` after `pub get`** on later steps so it doesn't re-resolve packages.

**Why interviewers ask:** Leaking a keystore or a store key is a serious, real incident. They want to see you treat secrets carefully. Caching shows you care about fast feedback for the whole team.

**Common mistake:** Committing `key.properties`, the keystore, or the Google Play JSON key to the repo. Another mistake is not caching anything, so every CI run is slow and wastes money.

**Follow-ups they may ask:**
- *"Where do you decode the base64 file?"* → On the runner during the job, then delete it after. It never touches Git.
- *"How do you keep secrets out of logs?"* → CI providers mask secret values in logs automatically; never `echo` a secret yourself.

**Related:** [Q2 — the CI pipeline](#q2) · [Q8 — what the keystore is](#q8) · [Q9 — Fastlane match secrets](#q9)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. How does Flutter versioning work? Explain the `1.0.0+1` format and auto-incrementing the build number in CI.

> Very common · Medium

**Short answer (say this):**
"In `pubspec.yaml` the version looks like `1.2.3+45`. The part before the `+` is the version name that users see in the store. The part after the `+` is the build number — an internal integer that must always go up with each upload. In CI, I usually set the build number automatically instead of editing the file by hand."

**Let's understand it fully:**

Think of it like editions of a book. The **version name** (`1.2.3`) is the edition printed on the cover that readers recognize. The **build number** (`45`) is the printer's internal serial number — readers never see it, but it must keep increasing so the warehouse knows which copy is newer.

**Step 1 — The format.**

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

**Step 2 — The rule that breaks builds: the number must increase.**
- On **Android**, the build number (`versionCode`) must be a strictly increasing integer for every upload to Play. Upload `45`, and the next upload must be `46` or higher.
- On **iOS**, the build number (`CFBundleVersion`) must increase for each upload within the same version name.
- The **version name** is what users see and should follow semantic versioning (`MAJOR.MINOR.PATCH`).

If you re-upload the same build number, the store rejects it. This is the most common release headache.

**Step 3 — Override it at build time (don't edit the file).**
Flutter lets you override the version with flags, so CI can compute the number automatically.

```bash
# Use the CI run number as the build number:
flutter build appbundle --release \
  --build-name=1.2.3 \
  --build-number=$GITHUB_RUN_NUMBER

# Or derive it from the git commit count (always increases):
BUILD_NUM=$(git rev-list --count HEAD)
flutter build appbundle --release \
  --build-name=1.2.3 \
  --build-number=$BUILD_NUM
```

**Step 4 — In a GitHub Actions workflow.**

```yaml
- name: Build app bundle
  run: |
    flutter build appbundle --release \
      --build-name=1.2.3 \
      --build-number=${{ github.run_number }}
```

`github.run_number` increases by one on every workflow run, so it is a safe, always-increasing build number.

**Why interviewers ask:** They want to know you understand *why* the build number must always increase, and that you can automate it. Editing `pubspec.yaml` by hand for every release is error-prone and blocks automation.

**Common mistake:** Confusing `build-name` (the display version, like `1.2.3`) with `build-number` (the internal integer, like `45`). Another classic: re-using the same build number after a failed upload, then wondering why the store rejects it.

**Follow-ups they may ask:**
- *"What if you forget the build number?"* → Flutter uses the one in `pubspec.yaml`. The flags just override it.
- *"Can two platforms share the same build number?"* → Yes, that's fine — each store only cares that *its own* sequence increases.

**Related:** [Q2 — using it in CI](#q2) · [Q13 — Play rejects non-increasing builds](#q13)

[↑ Back to top](#toc)

---

# B. Flavors & environments

---

<a id="q5"></a>
## 5. What are Flutter flavors? How do you set up dev / staging / prod on Android and iOS?

> Very common · Medium

**Short answer (say this):**
"Flavors let me build several versions of the same app from one codebase — usually dev, staging, and prod. Each flavor can have its own app ID, name, icon, and config. On Android I define `productFlavors` in `build.gradle`; on iOS I create Xcode schemes and build configurations. Then I run with `--flavor`."

**Let's understand it fully:**

Think of flavors as the **same recipe with different labels**. The cake is the same, but one box is labelled "Dev" (for the kitchen team to taste-test), one "Staging" (for the manager to approve), and one "Prod" (for customers). Same app, different name, icon, and which server it talks to — so you can have all three installed side by side on one phone.

**Step 1 — Why flavors exist.**
Without flavors, dev and prod fight over the same app ID, so you can't install both. And you'd be hand-editing the API URL before every build — slow and dangerous. Flavors make the difference automatic and safe.

**Step 2 — Android setup (`build.gradle`).**
You declare a dimension and the flavors. Each flavor gets a unique `applicationIdSuffix` (so the app IDs differ) and a display name.

```groovy
// android/app/build.gradle
android {
    flavorDimensions "environment"     // required, or Gradle errors

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
            resValue "string", "app_name", "MyApp"   // no suffix = real ID
        }
    }
}
```

**Step 3 — iOS setup (Xcode schemes + configurations).**
iOS does not have "flavors." Instead you:
1. Duplicate the Debug and Release **configurations** for each flavor (e.g. `Debug-dev`, `Release-dev`, `Debug-prod`, `Release-prod`).
2. Create a **scheme** for each flavor that points to its matching configurations.
3. In each configuration's build settings, set a different `PRODUCT_BUNDLE_IDENTIFIER` and `PRODUCT_NAME`.

This gives iOS the same "different ID + name per environment" result that `productFlavors` gives on Android.

**Step 4 — A separate entry point per flavor (common pattern).**
Each flavor usually has its own `main` file so it can pick the right config.

```dart
// lib/main_dev.dart
void main() => bootstrap(Environment.dev);

// lib/main_prod.dart
void main() => bootstrap(Environment.prod);
```

**Step 5 — Running and building with a flavor.**

```bash
# Run dev:
flutter run --flavor dev -t lib/main_dev.dart

# Build a prod release:
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

**Step 6 — Flavor vs `--dart-define` (a common follow-up).**
A flavor is a **native** concept — it changes the app ID, name, icon, and native resources at the platform level. `--dart-define` only passes **compile-time values into Dart code**. You normally use both: flavors for native differences, dart-define for Dart-level config like the API URL (see [Q6](#q6)).

**Why interviewers ask:** They want to confirm you can manage multiple environments without copy-pasting code or hand-editing config. This is fundamental for any team with QA and a CI pipeline.

**Common mistake:** Confusing flavors with dart-define and saying "I just use dart-define for everything" — dart-define cannot change the app ID, icon, or native resources. Another mistake is forgetting `flavorDimensions` on Android, which makes Gradle fail with a confusing error.

**Follow-ups they may ask:**
- *"Why do you want different app IDs?"* → So dev, staging, and prod can all be installed on one phone at the same time without overwriting each other.
- *"How do you give each flavor a different icon/Firebase file?"* → Put the icon and `google-services.json` / `GoogleService-Info.plist` in per-flavor folders that the build picks up.

**Related:** [Q6 — dart-define](#q6) · [Q7 — env config](#q7)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. How does `--dart-define` work? How do you pass variables at build time?

> Very common · Medium

**Short answer (say this):**
"`--dart-define` passes key-value pairs into Dart as compile-time constants. They get baked into the binary when I build — they are not runtime values. I read them with `String.fromEnvironment` and friends. Because they're `const`, Dart can even tree-shake away code that depends on them."

**Let's understand it fully:**

Think of `--dart-define` like **printing a value onto the box at the factory**. Once the box is sealed (built), that value is permanent — you can't change it later without making a new box. This is different from a setting the user can change while the app runs.

**Step 1 — Passing values on the command line.**

```bash
# One variable:
flutter run --dart-define=API_URL=https://dev.api.com

# Several variables:
flutter build apk --release \
  --dart-define=API_URL=https://dev.api.com \
  --dart-define=API_KEY=abc123 \
  --dart-define=ENABLE_LOGS=true
```

**Step 2 — Reading them in Dart.**
You must read them into `const` fields using the `fromEnvironment` constructors, and always give a `defaultValue`.

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

**Step 3 — Why they must be `const`.**
Because the value is fixed at compile time, Dart treats it as a constant. That means Dart can remove dead branches. For example, if `enableLogs` is `false`, the logging code can be tree-shaken away in release — making the app smaller and hiding the logging path entirely.

**Step 4 — The cleaner way: a JSON file (Flutter 3.7+).**
Passing ten flags is messy and leaks into your shell history. Put them in a JSON file and point to it instead.

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

This is much cleaner for CI: you keep one file per environment, and CI can write the file from secrets just before building.

**Step 5 — Compile-time vs runtime (the key distinction).**
`--dart-define` is **compile-time**. It is NOT the same as the operating system's runtime environment variables. So you cannot read a dart-define with `Platform.environment` — that reads OS env vars on the device, which is a totally different thing.

**Why interviewers ask:** This tests whether you understand compile-time vs runtime configuration, and whether you know how to keep secrets out of source code by injecting them through CI.

**Common mistake:** Trying to read a dart-define with `Platform.environment` (wrong — that's for runtime OS variables). Another mistake is committing an `env/prod.json` file that contains real production secrets.

**Follow-ups they may ask:**
- *"Can dart-define hold a real secret safely?"* → Not really. It's baked into the binary, so a determined attacker can extract it. Use it for config like URLs; keep true secrets on the server.
- *"How do you read an int or bool?"* → `int.fromEnvironment('PORT')` and `bool.fromEnvironment('FLAG')`, each with a `defaultValue`.

**Related:** [Q5 — flavors vs dart-define](#q5) · [Q7 — building the config class](#q7) · [Q3 — secrets in CI](#q3)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. How do you manage different API URLs, keys, and configs per environment?

> Common · Medium

**Short answer (say this):**
"I centralize all environment values in one config class instead of scattering URLs around the code. The values come either from separate `main` entry points per flavor, or from `--dart-define`. The rule: one place to change config, and never hardcode a URL inside a service class."

**Let's understand it fully:**

Imagine a **fuse box** in a house. Instead of running wires loose all over the walls, every circuit goes through one labelled panel. If something needs changing, you go to one place. A config class is that fuse box for your app's settings.

**Step 1 — Approach A: a config class set by the entry point.**
Each flavor's `main` file tells the config which environment it is, and the config holds the right values.

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
        apiKey = const String.fromEnvironment('PROD_API_KEY'); // injected by CI
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

Notice the prod key is **not hardcoded** — it comes from `--dart-define`, injected by CI.

**Step 2 — Approach B: read everything from dart-define (one `main`).**
With this approach you keep a single `main.dart` and feed all values in at build time.

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

**Step 3 — How it fits together in CI.**

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

**Step 4 — Which approach to pick.**
- **Approach A** is nice when each environment differs in many ways and you like having explicit entry points.
- **Approach B** is nice for CI because everything is data in a file — easy to swap per environment with no code change.

Both share the same principle: **one centralized config**, and **secrets injected, not committed**.

**Why interviewers ask:** They evaluate whether you can architect clean environment separation. Hardcoded URLs scattered through the codebase are a red flag; a centralized, maintainable config is what they want to see.

**Common mistake:** Hardcoding API URLs directly inside service classes and using `if/else` to switch them. Another serious mistake is storing production API keys in the repository — production secrets should be injected by CI and never committed.

**Follow-ups they may ask:**
- *"Where does the prod API key come from then?"* → From a CI secret, passed in with `--dart-define`. It never lives in the source.
- *"How do you handle a different Firebase project per environment?"* → Use per-flavor `google-services.json` / `GoogleService-Info.plist`, or FlutterFire's `flutterfire configure` with flavor support.

**Related:** [Q5 — flavors](#q5) · [Q6 — dart-define](#q6) · [Q3 — CI secrets](#q3)

[↑ Back to top](#toc)

---

# C. Code signing & obfuscation

---

<a id="q8"></a>
## 8. Explain code signing. What are an Android keystore and iOS certificates & provisioning profiles?

> Very common · Medium–Hard

**Short answer (say this):**
"Code signing proves an app was built by me and hasn't been tampered with. It uses public-key cryptography — I sign with my private key, and the OS or store verifies with the public key. On Android the private key lives in a keystore file. On iOS you need both a signing certificate and a provisioning profile that ties the certificate, app ID, and devices together."

**Let's understand it fully:**

Think of code signing as a **tamper-proof seal** on a medicine bottle. The seal proves two things: who made it, and that nobody opened it after the factory. If the seal is broken or fake, you don't trust the bottle. Phones and stores do the same with apps — no valid seal, no install.

**Step 1 — The idea: sign with private, verify with public.**
You hold a private key (secret). You sign the app with it. The device or store has your public key and checks the signature. If it matches, the app is genuine and unchanged.

**Step 2 — Android: the keystore.**
A keystore (`.jks` or `.keystore`) is a file holding one or more private keys, each protected by a password. When you build a release, Gradle signs the app with a key from this keystore. The **same keystore must be used for every update** to the same app — if you lose it, you can't update your app (unless you enrolled in Play App Signing).

```bash
# Create a keystore:
keytool -genkey -v \
  -keystore my-release-key.jks \
  -keyalg RSA -keysize 2048 \
  -validity 10000 \
  -alias my-key-alias
```

```properties
# android/key.properties  (NEVER committed to git)
storePassword=myStorePass
keyPassword=myKeyPass
keyAlias=my-key-alias
storeFile=../my-release-key.jks
```

```groovy
// android/app/build.gradle — load and use it
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

**Step 3 — iOS: two pieces working together.**
iOS signing needs both:
- A **signing certificate** (`.p12`) — contains your private key and identity. It proves *who* built the app.
- A **provisioning profile** — links the certificate, the app ID (bundle ID), the allowed devices (for dev/ad-hoc), and the app's entitlements. It tells iOS *where* the app may run and *which* certificate signed it.

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

**Step 4 — Keystore vs provisioning profile (the comparison they want).**

| | Android keystore | iOS provisioning profile |
|---|---|---|
| What it is | a file holding your private key | a file linking cert + app ID + devices |
| Proves identity? | yes (the key signs the app) | the certificate does; profile authorizes it |
| Devices listed? | no | yes, for development / ad-hoc |
| Lose it? | can't update app (unless Play App Signing) | just regenerate it from your account |

**Why interviewers ask:** Signing errors are one of the most common blockers for junior-to-mid developers. They want to know you understand the mechanics, can troubleshoot the errors, and can manage keys safely across a team.

**Common mistake:** Committing the keystore or `key.properties` to Git. Losing the Android keystore without having enrolled in Play App Signing. On iOS, manually creating multiple distribution certificates, which revokes teammates' certificates — the exact mess Fastlane match solves (see [Q9](#q9)).

**Follow-ups they may ask:**
- *"What is Play App Signing?"* → Google holds the real signing key for you. You upload with an upload key, and Google re-signs. If you lose your upload key, Google can reset it — so you don't permanently lose the app.
- *"Why does iOS list device UUIDs?"* → For development and ad-hoc builds, the profile says exactly which physical devices may run the app. App Store builds skip this because the store distributes to everyone.

**Related:** [Q9 — Fastlane match/supply](#q9) · [Q3 — keystore as a CI secret](#q3) · [Q14 — iOS distribution cert](#q14)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What is Fastlane? How does `match` work for iOS signing, and `supply` for Android deployment?

> Common · Medium

**Short answer (say this):**
"Fastlane is a tool that automates building and releasing mobile apps. You define 'lanes' in a Ruby file called the Fastfile. `match` solves iOS signing by storing one shared set of certificates and profiles in a private Git repo, so every machine signs the same way. `supply` uploads your Android app straight to the Play Store."

**Let's understand it fully:**

Think of Fastlane as a **set of recorded macros** for release. Instead of clicking through Xcode and the Play Console by hand every time, you press one button (`fastlane beta`) and it runs the whole sequence the same way, every time.

**Step 1 — Lanes in a Fastfile.**
A lane is a named sequence of steps. You run it with `fastlane <lane>`.

```ruby
# Fastfile
lane :beta do
  match(type: "appstore")       # fetch the shared signing assets
  build_app(scheme: "prod", export_method: "app-store")
  upload_to_testflight
end
```

**Step 2 — The iOS signing pain that `match` solves.**
On a team, everyone making their own iOS certificates is chaos — making a new distribution certificate can revoke someone else's, breaking their builds. `match` fixes this by storing **one** set of certificates and profiles in a private, encrypted Git repo. Every developer and CI machine fetches the *same* assets.

```bash
fastlane match init           # one-time setup
fastlane match development    # create/fetch dev profiles
fastlane match appstore       # create/fetch distribution profiles
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

**Step 3 — `supply` for Android upload.**
`supply` uploads your APK or AAB straight to Play, targeting a track (internal, alpha, beta, production). It can also update the store listing, screenshots, and metadata. It authenticates with a **service account JSON key**.

```ruby
lane :deploy_android do
  supply(
    track: "internal",
    aab: "../build/app/outputs/bundle/prodRelease/app-prod-release.aab",
    json_key: "play-store-key.json",   # service account key (a CI secret)
    package_name: "com.example.myapp",
  )
end
```

**Step 4 — Promoting between tracks with `supply`.**
You can move an existing build up a track without re-uploading.

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

**Why interviewers ask:** They look for real release-automation experience. Manual store uploads and signing don't scale for teams. Knowing Fastlane signals you've shipped production apps in a professional setup.

**Common mistake:** Confusing `match` with the older tools `cert` and `sigh`, which create new certificates each time and cause exactly the revocation mess `match` was built to avoid. Another mistake is committing the Play service-account JSON key instead of injecting it as a CI secret.

**Follow-ups they may ask:**
- *"How does CI get the match repo?"* → It's a private Git repo; CI clones it with a deploy key, and the match password (a secret) decrypts the assets.
- *"Do you have to use Fastlane?"* → No. Codemagic and Bitrise can do signing and upload too, and there are GitHub Actions for the stores. Fastlane is just the most common cross-tool option.

**Related:** [Q8 — what it's signing](#q8) · [Q13 — Play tracks](#q13) · [Q14 — upload_to_testflight](#q14)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What is app obfuscation? Why do it, and how do you enable it in Flutter?

> Common · Medium

**Short answer (say this):**
"Obfuscation renames your classes and methods to meaningless names like `aa`, `b0` in the compiled app. This makes it much harder for someone to decompile your app and read your logic. In Flutter you enable it with `--obfuscate` plus `--split-debug-info`, and you must keep the saved symbols so you can decode real crash reports later."

**Let's understand it fully:**

Think of obfuscation like **shredding the labels off all the wires** in a machine before shipping it. The machine still works perfectly, but anyone who opens it up can't easily tell what each wire does. You keep the wiring diagram (the debug symbols) in a safe so *you* can still repair it.

**Step 1 — What it does.**
It replaces readable names with short meaningless ones in the release binary.

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

A decompiler can still open the app, but the code reads like gibberish — much harder to understand.

**Step 2 — How to enable it.**
Add `--obfuscate` and `--split-debug-info` together. Both are required.

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

**Step 3 — Why `--split-debug-info` is required.**
That flag pulls the debug symbols out into a separate folder. Those symbols are the **map** from the meaningless names back to the real ones. You need that map to read crash reports — otherwise a crash report is just `a0.b()` and tells you nothing.

**Step 4 — Decoding a real crash.**
When a crash comes in with obfuscated names, you "symbolize" it using the saved map.

```bash
flutter symbolize \
  -i crash_stack_trace.txt \
  -d build/debug-info/
# prints the human-readable stack trace with real class/method names
```

**Step 5 — What obfuscation does NOT do.**
It does **not** encrypt strings. A literal like `const apiKey = 'secret123'` is still readable in the binary. So never hardcode true secrets — keep them on the server. Obfuscation only raises the difficulty of reverse engineering; it is not full protection.

**Why interviewers ask:** They check your security awareness. Shipping without obfuscation is a liability, especially for fintech, health, or enterprise apps. Knowing to archive the symbols shows you think about supporting the app in production, not just building it.

**Common mistake:** Using `--obfuscate` without `--split-debug-info` (the build fails — both are required). Another mistake is throwing away the `debug-info` folder after building. Without it, you can never symbolize production crashes — so always archive it in CI next to the build artifact.

**Follow-ups they may ask:**
- *"Does obfuscation hide my API key?"* → No. String literals stay readable. Keep real secrets server-side.
- *"Where do you store the symbols?"* → Upload them as a CI artifact, and to your crash tool (e.g. Crashlytics/Sentry) so it can de-obfuscate automatically.

**Related:** [Q1 — release builds](#q1) · [Q3 — archiving symbols in CI](#q3)

[↑ Back to top](#toc)

---

# D. Store release & distribution

---

<a id="q11"></a>
## 11. What is a build artifact? Explain the difference between APK and AAB, and why Google Play prefers AAB.

> Very common · Medium

**Short answer (say this):**
"A build artifact is anything the build produces — APKs, AABs, IPAs, symbols, test reports. For Android the two big ones are APK and AAB. An APK is a single installable file containing everything for every device. An AAB is an upload format — you give it to Google Play, and Play generates a small, optimized APK for each user's device."

**Let's understand it fully:**

Think of it like **shipping furniture**. An APK is a fully-built sofa in every fabric and size, all packed into one giant box — the customer hauls home the whole thing even though they only need one. An AAB is the flat-pack: you send the parts to the warehouse (Google Play), and it assembles exactly the one sofa that fits each customer's room. Smaller delivery, same result.

**Step 1 — APK: one file, everything inside.**
An APK includes compiled code for every CPU architecture, resources for every screen density, and every language. The user downloads all of it, even the parts they'll never use. An APK can be installed directly on a device (sideloaded).

**Step 2 — AAB: a publishing format, not directly installable.**
You upload the AAB to Play. Play then generates optimized "split" APKs per device. A Pixel 7 user downloads only arm64 code, only their screen density, only their language — a much smaller download.

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

**Step 3 — The build commands.**

```bash
# APK (for direct install, QA, sideloading):
flutter build apk --release
# output: build/app/outputs/flutter-apk/app-release.apk

# AAB (for the Play Store):
flutter build appbundle --release
# output: build/app/outputs/bundle/release/app-release.aab
```

**Step 4 — Why Play requires AAB for new apps.**
Since August 2021, Play requires AAB for all new apps. The main reason is **smaller downloads** — smaller downloads mean more people finish installing and less storage used. Google reports about a 15% average size reduction. AAB also enables on-demand feature delivery and large-asset delivery.

**Step 5 — When you still need an APK.**
- Firebase App Distribution and direct QA testing (see [Q12](#q12)).
- Enterprise sideloading.
- App stores that don't support AAB.
- Local device testing during development.

**Why interviewers ask:** This is foundational Android knowledge. They expect you to know why AAB exists and when to use APK vs AAB. It also connects to app-size optimization, which affects install conversion.

**Common mistake:** Thinking APK and AAB are interchangeable. Trying to sideload an AAB onto a device (you can't — it's not installable). Uploading an APK to Play for a new app (rejected). Also, not realizing AAB requires Google to sign your app via Play App Signing, which some teams hesitate over.

**Follow-ups they may ask:**
- *"How do I test what a user actually gets from an AAB?"* → Use the `bundletool` to generate device-specific APKs from your AAB, or use Play's internal testing track.
- *"Can I still get a single universal APK?"* → Yes, `bundletool` can build a universal APK from an AAB for testing.

**Related:** [Q1 — release builds](#q1) · [Q12 — APK for testers](#q12) · [Q13 — uploading the AAB](#q13)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. How does Firebase App Distribution work for distributing test builds?

> Common · Medium

**Short answer (say this):**
"Firebase App Distribution sends pre-release builds — APK, AAB, or IPA — straight to testers, skipping the app stores. Testers get an email or in-app prompt, tap a link, and install. It's great for getting builds to QA fast. The iOS catch: testers' device UDIDs must be in an ad-hoc provisioning profile."

**Let's understand it fully:**

Think of it as **handing out free samples at the door** instead of putting the product on store shelves. You pick who gets a sample (tester groups), attach a note ("try the new login"), and they get it immediately — no waiting for store approval.

**Step 1 — The flow.**

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

**Step 2 — Upload via the Firebase CLI.**

```bash
npm install -g firebase-tools

firebase appdistribution:distribute \
  build/app/outputs/flutter-apk/app-release.apk \
  --app YOUR_FIREBASE_APP_ID \
  --groups "qa-team,designers" \
  --release-notes "Fixed login bug, added dark mode"
```

**Step 3 — Upload via Fastlane (handy in CI).**

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

**Step 4 — The iOS gotcha (very important).**
On iOS you must distribute an **ad-hoc** build whose provisioning profile lists each tester's device UDID. Firebase can collect UDIDs through its onboarding flow, but you still have to regenerate the profile and rebuild whenever a new tester is added. If you'd rather avoid managing UDIDs, use **TestFlight** instead (see [Q14](#q14)) — it doesn't need device registration.

**Why interviewers ask:** Getting builds to QA quickly is critical for fast iteration. They want to see you know a clean way to do this — not emailing APK files around.

**Common mistake:** On iOS, forgetting that ad-hoc distribution needs device UDIDs in the profile. Also, uploading an IPA signed with an **App Store** profile to Firebase — it won't install on devices, because App Store profiles only work through TestFlight and the App Store.

**Follow-ups they may ask:**
- *"Firebase App Distribution vs TestFlight?"* → Firebase works for both Android and iOS and is fast, but iOS needs UDIDs for ad-hoc. TestFlight is iOS-only, needs no UDIDs, but external testing requires a Beta App Review.
- *"Can you automate the tester invite?"* → Yes — tester groups plus the CLI/Fastlane step in CI sends invites automatically on each build.

**Related:** [Q11 — APK for testers](#q11) · [Q14 — TestFlight](#q14) · [Q8 — ad-hoc profile](#q8)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. How do you submit an app to the Google Play Store? Explain the tracks: internal, alpha, beta, production.

> Very common · Medium

**Short answer (say this):**
"Play organizes releases into tracks — internal, closed (alpha), open (beta), and production — each a stage in the rollout. You upload an AAB to a track, and only users on that track get it. Production supports staged rollout, so I can release to a small percentage first and halt if something breaks."

**Let's understand it fully:**

Think of the tracks as **bringing a dish out of the kitchen in stages**. First the chef tastes it (internal), then a few trusted regulars (alpha), then a soft launch to anyone curious (beta), and finally it goes on the main menu for everyone (production). Each stage catches problems before more people are affected.

**Step 1 — The four tracks.**

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

**Step 2 — The submission steps.**
1. Build a signed AAB: `flutter build appbundle --release`.
2. In Play Console, create a new release in your chosen track.
3. Upload the AAB. Play processes it and prepares optimized APKs per device.
4. Add release notes.
5. Review and roll out. For production, the first release needs a full review (listing, content rating, privacy policy, etc.).

**Step 3 — Staged rollout (a key production feature).**
Production releases support staged rollout. You can release to 5% of users, watch crash rates and ANRs, then gradually raise it to 100%. If something is wrong, you halt the rollout so the rest of your users never get the bad build.

**Step 4 — Promoting between tracks.**

```
  Internal --> Closed/Alpha --> Open/Beta --> Production
     |              |              |             |
  100 testers    QA team      public beta    all users
  no review      no review    no review      full review
```

```ruby
# Promote via Fastlane supply (no re-upload needed):
supply(
  track: "internal",
  track_promote_to: "beta",
  json_key: "play-store-key.json",
)
```

**Why interviewers ask:** Knowing the Play release pipeline shows you've shipped professionally. They often ask about staged rollouts and how to handle a bad release — being able to halt a rollout shows operational awareness.

**Common mistake:** Uploading an APK instead of an AAB (Play requires AAB for new apps). Not realizing the internal track caps at 100 testers and isn't suited for big QA teams — use closed testing for that. And forgetting to increment the `versionCode` before uploading, which gets the upload rejected (see [Q4](#q4)).

**Follow-ups they may ask:**
- *"What's the difference between internal and closed testing?"* → Internal is up to 100 testers by email with instant availability. Closed (alpha) can have many more testers and is for broader QA, still without a public review.
- *"How do you roll back a bad release?"* → You can't truly delete a release, but you can halt a staged rollout and push a new, higher-versioned build with the fix.

**Related:** [Q11 — AAB upload](#q11) · [Q4 — versionCode must increase](#q4) · [Q9 — supply automation](#q9)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. How do you submit an app to the Apple App Store? Describe the TestFlight flow.

> Very common · Medium–Hard

**Short answer (say this):**
"Everything goes through App Store Connect. First you upload a signed IPA. TestFlight handles pre-release testing — internal testers get it instantly, external testers need a quick Beta App Review. Then for the public release you fill in the store listing and submit for App Review, which usually takes a day or two."

**Let's understand it fully:**

Think of Apple's process as a **stricter customs office** than Google's. Even your beta testers (external) pass a quick inspection before they can receive the package, and the final public release always goes through a full inspection. It's more friction, but the steps are predictable once you know them.

**Step 1 — Build and upload a signed IPA.**
You build with a **distribution** certificate and an App Store provisioning profile, usually supplying an `ExportOptions.plist` so the archive is signed correctly.

```bash
# Build the IPA:
flutter build ipa --release \
  --export-options-plist=ios/ExportOptions.plist

# Upload it (CLI):
xcrun altool --upload-app \
  -f build/ios/ipa/MyApp.ipa \
  -t ios \
  --apiKey YOUR_KEY_ID \
  --apiIssuer YOUR_ISSUER_ID

# Or with Fastlane:
upload_to_testflight
```

**Step 2 — The TestFlight flow.**

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

**Step 3 — Submitting for the public App Store.**
Once testing is done:
1. Select the build in App Store Connect.
2. Fill in metadata — description, screenshots, keywords, privacy policy URL, category.
3. Submit for App Review (typically 24–48 hours).
4. If approved, release immediately, on a scheduled date, or manually.

**Step 4 — Key differences from Google Play.**
- Apple requires review even for **external** TestFlight builds; Google's tracks don't review test builds.
- There's no Apple equivalent to Google's review-free internal track beyond your own developer-account members.
- All iOS test builds **expire after 90 days**.
- There's no percentage-based staged rollout; iOS has a 7-day **phased release** for production instead.

**Why interviewers ask:** iOS submission has more friction than Android and confuses many developers. They want to see you've navigated the full cycle — build, sign, upload, TestFlight, review, release. It's a strong signal of real shipping experience.

**Common mistake:** Forgetting that external TestFlight needs a Beta App Review. Signing with a **development** certificate instead of a **distribution** one — the upload succeeds but processing fails. Not providing an `ExportOptions.plist`, which makes `flutter build ipa` produce an incorrectly signed archive.

**Follow-ups they may ask:**
- *"Internal vs external TestFlight?"* → Internal = up to 100 of your team, no review, instant. External = up to 10,000 testers but needs Beta App Review.
- *"What's phased release?"* → Apple's way to roll a production update out gradually over 7 days, with the option to pause — the closest thing to Google's staged rollout.

**Related:** [Q8 — distribution cert & profile](#q8) · [Q9 — upload_to_testflight](#q9) · [Q12 — Firebase vs TestFlight](#q12)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**Build modes: debug vs profile vs release**

| | Debug | Profile | Release |
|---|---|---|---|
| Compilation | JIT | AOT (native) | AOT (native) |
| Hot reload | yes | no | no |
| Speed | slow | realistic | fast |
| Use for | coding | measuring speed | shipping |

**Flavors: dev vs staging vs prod**

| | dev | staging | prod |
|---|---|---|---|
| App ID | `.dev` suffix | `.staging` suffix | real ID |
| API | dev server | staging server | live server |
| Logs | on | on | off |
| Who uses it | developers | QA / manager | real users |

**Android keystore vs iOS provisioning profile**

| | Android keystore | iOS provisioning profile |
|---|---|---|
| What | file with your private key | links cert + app ID + devices |
| Lists devices? | no | yes (dev / ad-hoc) |
| If lost | can't update (unless Play App Signing) | just regenerate it |
| Keep in Git? | never | never |

**Firebase App Distribution vs TestFlight**

| | Firebase App Distribution | TestFlight |
|---|---|---|
| Platforms | Android + iOS | iOS only |
| iOS device UDIDs | needed (ad-hoc) | not needed |
| Apple review | no | external testers need one |
| Build expiry | none | 90 days |

## One-line reminders

- **Build modes**: debug = coding, profile = measure speed, release = ship. Never judge speed in debug. ([Q1](#q1))
- **CI**: YAML in `.github/workflows/`; Android on Linux, iOS on macOS; always upload the artifact. ([Q2](#q2))
- **Secrets** never go in Git — store as CI secrets, decode files from base64, cache the SDK and pub. ([Q3](#q3))
- **Version `1.2.3+45`**: name before `+` (users see it), build number after `+` must always increase. ([Q4](#q4))
- **Flavors** = native difference (app ID, icon, name). **dart-define** = compile-time values in Dart. Use both. ([Q5](#q5), [Q6](#q6))
- **One config class**; inject prod secrets via dart-define; never hardcode URLs in services. ([Q7](#q7))
- **Code signing** = tamper-proof seal. Android = keystore; iOS = certificate + provisioning profile. ([Q8](#q8))
- **Fastlane match** = one shared set of iOS certs in a private repo. **supply** = upload AAB to Play. ([Q9](#q9))
- **Obfuscate** with `--obfuscate --split-debug-info`; keep the symbols to `flutter symbolize` crashes. ([Q10](#q10))
- **APK** = one installable file. **AAB** = upload format; Play splits a smaller download per device. ([Q11](#q11))
- **Firebase App Distribution**: fast test builds; iOS needs UDIDs in an ad-hoc profile. ([Q12](#q12))
- **Play tracks**: internal → alpha → beta → production; production supports staged rollout (halt a bad build). ([Q13](#q13))
- **App Store**: upload IPA → TestFlight (external needs Beta Review) → App Review → release; builds expire in 90 days. ([Q14](#q14))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers rarely stop at one question. They keep digging to test your depth. Practice answering this chain out loud — calmly, step by step:

1. *"How do you set up dev, staging, and prod?"* → flavors for native differences (app ID, icon), dart-define for Dart config (API URL).
2. *"Why not just use dart-define for everything?"* → dart-define can't change the app ID, icon, or native resources — only flavors can.
3. *"How does the prod API key stay safe?"* → it's a CI secret injected via dart-define, never committed to Git.
4. *"How does that key reach the CI build?"* → stored as a CI secret, read at build time; files like keystores are decoded from base64 on the runner.
5. *"How would you ship the prod build to users?"* → build a signed AAB, upload to Play's internal track, then promote up to production with a staged rollout.

Being able to calmly go step by step like this — without guessing — is exactly what makes you sound **senior**, in both remote and BD interviews.

[↑ Back to top](#toc)

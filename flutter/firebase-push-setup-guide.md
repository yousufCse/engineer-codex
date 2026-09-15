# Firebase Push Notification — Setup Guide

**Flutter · Android + iOS · Firebase project খোলা থেকে প্রথম push পাওয়া পর্যন্ত**

> **ভাষা নীতি:** ব্যাখ্যা বাংলায়, Technical Term English-এ অপরিবর্তিত।

**এই গাইডের সীমা**

| বিষয় | কোথায় |
|---|---|
| Setup — Console, config file, native config, প্রথম push | এই গাইড |
| Concept, Background Task, Foreground Service, বড় file upload | [notification_background_guide.md](./notification_background_guide.md) |
| Notification tap করে সঠিক screen-এ যাওয়া | [deep-link-guide.md](./deep-link-guide.md) |

---

## Quick Path

```bash
# ১. CLI ইনস্টল ও login
npm install -g firebase-tools
dart pub global activate flutterfire_cli
firebase login

# ২. Project root-এ গিয়ে config বানাও
cd my_app
flutterfire configure

# ৩. Package যোগ করো
flutter pub add firebase_core firebase_messaging flutter_local_notifications
```

তারপর:

```
৪. Android  → Gradle-এ google-services plugin + Manifest permission
৫. iOS      → Apple Developer-এ .p8 key → Firebase-এ upload
৬. Xcode    → Push Notifications + Background Modes capability
৭. Test     → Firebase Console → Messaging → Send test message
```

---

## Table of Contents

**Part 0 — শুরুর আগে**
- [0.1 কী কী লাগবে](#01-কী-কী-লাগবে)
- [0.2 পুরো Setup একনজরে](#02-পুরো-setup-একনজরে)

**Part 1 — Firebase Project**
- [1.1 Console-এ Project বানাও](#11-console-এ-project-বানাও)
- [1.2 FlutterFire CLI দিয়ে App যুক্ত করো](#12-flutterfire-cli-দিয়ে-app-যুক্ত-করো)

**Part 2 — Android**
- [2.1 App রেজিস্টার ও google-services.json](#21-app-রেজিস্টার-ও-google-servicesjson)
- [2.2 Gradle Configuration](#22-gradle-configuration)
- [2.3 AndroidManifest.xml](#23-androidmanifestxml)
- [2.4 Notification Icon ও Channel](#24-notification-icon-ও-channel)
- [2.5 Runtime Permission — Android 13+](#25-runtime-permission--android-13)
- [2.6 Release Build-এর সতর্কতা](#26-release-build-এর-সতর্কতা)

**Part 3 — iOS**
- [3.1 App রেজিস্টার ও GoogleService-Info.plist](#31-app-রেজিস্টার-ও-googleservice-infoplist)
- [3.2 App ID-তে Push চালু করো](#32-app-id-তে-push-চালু-করো)
- [3.3 APNs Auth Key (.p8) বানাও](#33-apns-auth-key-p8-বানাও)
- [3.4 Firebase-এ .p8 Upload করো](#34-firebase-এ-p8-upload-করো)
- [3.5 Xcode Capabilities](#35-xcode-capabilities)
- [3.6 AppDelegate.swift ও Info.plist](#36-appdelegateswift-ও-infoplist)
- [3.7 Device না Simulator](#37-device-না-simulator)

**Part 4 — Flutter Code**
- [4.1 Package](#41-package)
- [4.2 main.dart](#42-maindart)
- [4.3 NotificationService](#43-notificationservice)
- [4.4 Token Backend-এ পাঠানো](#44-token-backend-এ-পাঠানো)

**Part 5 — Push পাঠানো**
- [5.1 Firebase Console থেকে](#51-firebase-console-থেকে)
- [5.2 FCM HTTP v1 API](#52-fcm-http-v1-api)
- [5.3 Legacy Server Key বন্ধ](#53-legacy-server-key-বন্ধ)
- [5.4 Test Matrix](#54-test-matrix)

**Part 6 — সমস্যা ও সমাধান**
- [6.1 Error Table](#61-error-table)
- [6.2 বিস্তারিত সমাধান](#62-বিস্তারিত-সমাধান)

**Part 7 — Production**
- [7.1 Release Checklist](#71-release-checklist)
- [7.2 Security — কোন File গোপন](#72-security--কোন-file-গোপন)

---

# Part 0 — শুরুর আগে

## 0.1 কী কী লাগবে

**Android**

| জিনিস | নোট |
|---|---|
| Google Account | Firebase Console-এ ঢুকতে |
| Device বা Emulator | Emulator-এ push কাজ করে, তবে Google Play সহ system image লাগবে |
| Package name ঠিক করা | যেমন `com.company.myapp`। পরে বদলালে Firebase app আবার বানাতে হয় |
| খরচ | নেই |

**iOS**

| জিনিস | নোট |
|---|---|
| Apple Developer Program | বছরে $99। **এটা ছাড়া push সম্ভব নয়** |
| Mac + Xcode | Capability চালু করতে |
| Real iPhone/iPad | নিচের [3.7](#37-device-না-simulator) দেখো |
| Bundle ID | Android package name-এর সাথে একই রাখলে সুবিধা |

> **সতর্কতা:** Apple Developer Program ছাড়া iOS push-এর কোনো workaround নেই। Free provisioning-এ app চলবে, কিন্তু Push Notifications capability যোগ করা যাবে না। কাজ শুরুর আগেই account নিশ্চিত করো, নাহলে মাঝপথে আটকে যাবে।

---

## 0.2 পুরো Setup একনজরে

```
ধাপ ১ — Firebase Console
        Project → Android app যোগ → iOS app যোগ
                    │
                    ▼
ধাপ ২ — Config File
        google-services.json        → android/app/
        GoogleService-Info.plist    → Xcode Runner target
        firebase_options.dart       → lib/
                    │
                    ▼
ধাপ ৩ — Native Config
        Android : Gradle plugin + Manifest permission
        iOS     : .p8 key + Xcode capability + AppDelegate
                    │
                    ▼
ধাপ ৪ — Flutter Code
        Firebase.initializeApp() → permission → token
        → ৩টা handler (foreground / background / terminated)
                    │
                    ▼
ধাপ ৫ — Test
        Console থেকে test push → ৬টা কেস মিলিয়ে দেখো
```

**মনে রাখার কথা:** Firebase নিজে push পাঠায় না। Android-এ Google-এর FCM সার্ভার পাঠায়, iOS-এ Apple-এর APNs সার্ভার পাঠায়। Firebase মাঝের স্তর। তাই iOS-এ Apple-এর key (`.p8`) Firebase-কে দিতে হয় — নাহলে Apple Firebase-কে অনুরোধ করার অধিকার দেয় না।

---

# Part 1 — Firebase Project

## 1.1 Console-এ Project বানাও

1. যাও → https://console.firebase.google.com
2. **Create a project** চাপো।
3. নাম দাও (যেমন `MyApp Production`)। নিচে যে Project ID দেখাবে (`myapp-production-4f2a1`) সেটা **পরে বদলানো যায় না** — দেখে নাও।
4. Google Analytics — push-এর জন্য লাগে না। চালু রাখলে Console-এ notification-এর open rate দেখতে পাবে।
5. **Create project** চাপো।

**Dev আর Prod আলাদা project রাখো:**

```
myapp-dev   →  ডেভেলপারের ফোন, test push
myapp-prod  →  আসল ইউজার
```

এক project রাখলে test push ভুল করে আসল ইউজারের কাছে যেতে পারে। Push পাঠিয়ে দিলে ফেরত আনার উপায় নেই।

---

## 1.2 FlutterFire CLI দিয়ে App যুক্ত করো

CLI দুই platform-এর app রেজিস্টার করে, config file ঠিক জায়গায় রাখে, আর `firebase_options.dart` বানায়।

**১. Firebase CLI:**

```bash
npm install -g firebase-tools
firebase --version
firebase login
```

Node না থাকলে: `curl -sL https://firebase.tools | bash`

**২. FlutterFire CLI:**

```bash
dart pub global activate flutterfire_cli
```

`flutterfire: command not found` হলে PATH-এ যোগ করো:

```bash
echo 'export PATH="$PATH":"$HOME/.pub-cache/bin"' >> ~/.zshrc
source ~/.zshrc
```

**৩. Configure:**

```bash
cd /path/to/my_app
flutterfire configure
```

CLI জিজ্ঞেস করবে কোন Firebase project, কোন platform (android + ios), আর package name / bundle id।

**৪. তিনটা ফাইল তৈরি হয়েছে কিনা দেখো:**

```bash
ls -la lib/firebase_options.dart \
       android/app/google-services.json \
       ios/Runner/GoogleService-Info.plist
```

> **সতর্কতা:** `flutterfire configure` iOS-এর plist ডিস্কে রাখে, কিন্তু সবসময় **Xcode project-এ যোগ করে না**। যোগ না হলে app চালু হতেই crash করে। [3.1](#31-app-রেজিস্টার-ও-googleservice-infoplist)-এ যোগ করার নিয়ম আছে।

**Flavor ব্যবহার করলে:**

```bash
flutterfire configure \
  --project=myapp-dev \
  --out=lib/firebase_options_dev.dart \
  --android-package-name=com.company.myapp.dev \
  --ios-bundle-id=com.company.myapp.dev
```

Flavor-এর পুরো গাইড → [flavor-setup-guide.md](./flavor-setup-guide.md)

**CLI ছাড়া manual setup:** Part 2 ও Part 3-এর ধাপ হাতে করা যায়। তখন `firebase_options.dart` থাকবে না, তাই কোডে `await Firebase.initializeApp()` (argument ছাড়া) লিখতে হবে — native config file থেকে value নেবে। Android ও iOS-এ চলে, web-এ চলে না।

---

# Part 2 — Android

## 2.1 App রেজিস্টার ও google-services.json

FlutterFire CLI চালিয়ে থাকলে এই ধাপ হয়ে গেছে — ফাইলের জায়গা দেখে [2.2](#22-gradle-configuration)-এ যাও।

**১. Package name বের করো:**

```bash
grep applicationId android/app/build.gradle
# Kotlin DSL হলে
grep applicationId android/app/build.gradle.kts
```

**২.** Firebase Console → Project Overview → Android আইকন।

| Field | কী দেবে |
|---|---|
| Android package name | উপরের `applicationId`-র সাথে হুবহু এক |
| App nickname | Console-এ চেনার জন্য যেকোনো নাম |
| Debug signing certificate SHA-1 | Push-এর জন্য লাগে না। Google Sign-In বা App Links-এর জন্য লাগে |

> Package name একটা অক্ষর ভুল হলে push কখনো আসবে না, আর কোনো error message-ও পাবে না — app চুপচাপ token নেবে, কিন্তু সেই token কাজ করবে না। হাতে টাইপ না করে copy-paste করো।

**৩.** `google-services.json` নামিয়ে রাখো:

```
android/app/google-services.json      সঠিক
android/google-services.json           ভুল
```

**Flavor থাকলে** প্রতিটার জন্য আলাদা Firebase app বানিয়ে আলাদা ফাইল:

```
android/app/src/dev/google-services.json
android/app/src/prod/google-services.json
```

---

## 2.2 Gradle Configuration

`google-services` Gradle plugin ফাইলটা পড়ে build-এর সময় Firebase config app-এ ঢোকায়। Plugin ছাড়া ফাইল থাকলেও কাজে আসে না।

`android/settings.gradle`-এ `plugins { }` block আছে কিনা দেখে পদ্ধতি বেছে নাও।

### পদ্ধতি A — Plugins DSL (Flutter 3.16+ template)

`android/settings.gradle` — বিদ্যমান লাইনগুলো হাত দিও না, শুধু শেষ লাইনটা যোগ করো:

```groovy
plugins {
    id "dev.flutter.flutter-plugin-loader" version "1.0.0"
    id "com.android.application" version "8.7.0" apply false
    id "org.jetbrains.kotlin.android" version "2.1.0" apply false
    id "com.google.gms.google-services" version "4.4.2" apply false   // যোগ করো
}
```

`android/app/build.gradle`:

```groovy
plugins {
    id "com.android.application"
    id "kotlin-android"
    id "com.google.gms.google-services"        // যোগ করো
    id "dev.flutter.flutter-gradle-plugin"     // এটা সবার শেষে থাকতে হবে
}
```

### পদ্ধতি B — buildscript (পুরনো template)

`android/build.gradle`:

```groovy
buildscript {
    repositories { google(); mavenCentral() }
    dependencies {
        classpath 'com.google.gms:google-services:4.4.2'
    }
}
```

`android/app/build.gradle` — ফাইলের একদম নিচে:

```groovy
apply plugin: 'com.google.gms.google-services'
```

### minSdk

```groovy
android {
    defaultConfig {
        minSdk = flutter.minSdkVersion   // Flutter-এর default
    }
}
```

Firebase-এর নতুন version আরও বেশি minSdk চাইলে build fail করবে এবং **error-এই নাম্বারটা বলে দেবে**:

```
uses-sdk:minSdkVersion 21 cannot be smaller than version 23
declared in library [com.google.firebase:firebase-messaging]
```

তখন `minSdk = 23` (error যা বলে) বসাও।

> **Breaking change:** minSdk বাড়ালে তার নিচের Android version-এ তোমার app আর ইনস্টল হবে না। যেমন 23 করলে Android 5.0 ও 5.1 বাদ যাবে। Play Console → Statistics-এ কত ইউজার ঐ version-এ আছে দেখে নাও।

### Build করে দেখো

```bash
flutter clean && flutter pub get && flutter build apk --debug
```

---

## 2.3 AndroidManifest.xml

`android/app/src/main/AndroidManifest.xml`:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- Android 13+ — notification দেখানোর permission -->
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
    <uses-permission android:name="android.permission.INTERNET"/>

    <application android:label="My App" android:icon="@mipmap/ic_launcher">

        <!-- Flutter template-এর <activity> ব্লক অপরিবর্তিত থাকবে।
             launchMode="singleTop" default-ই আছে — বদলিও না। -->

        <!-- ছোট সাদা status bar icon -->
        <meta-data
            android:name="com.google.firebase.messaging.default_notification_icon"
            android:resource="@drawable/ic_notification"/>

        <meta-data
            android:name="com.google.firebase.messaging.default_notification_color"
            android:resource="@color/notification_color"/>

        <!-- App বন্ধ থাকলে FCM এই channel-এ notification দেখায় -->
        <meta-data
            android:name="com.google.firebase.messaging.default_notification_channel_id"
            android:value="high_importance_channel"/>

    </application>
</manifest>
```

`android/app/src/main/res/values/colors.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="notification_color">#2196F3</color>
</resources>
```

> **সতর্কতা:** `default_notification_channel_id`-তে যে নাম দিলে, Dart কোডে **ঠিক সেই নামেই** channel বানাতে হবে ([4.3](#43-notificationservice))। নাম না মিললে Android 8+ এ app terminated অবস্থায় notification চুপচাপ হারিয়ে যাবে — কোনো error দেখাবে না।

---

## 2.4 Notification Icon ও Channel

### Icon

Status bar icon **শুধু সাদা আর transparent** হতে পারে। রঙিন PNG দিলে ধূসর চারকোনা বাক্স দেখাবে।

```
android/app/src/main/res/drawable-mdpi/ic_notification.png      24 × 24
                        drawable-hdpi/                          36 × 36
                        drawable-xhdpi/                         48 × 48
                        drawable-xxhdpi/                        72 × 72
                        drawable-xxxhdpi/                       96 × 96
```

সহজ উপায়: Android Studio → `res` folder-এ right click → **New → Image Asset** → Icon Type: **Notification Icons**।

### Channel

Android 8 (Oreo) থেকে প্রতিটা notification একটা Channel-এর ভেতরে যায়। Channel-এ ঠিক হয় — শব্দ, ভাইব্রেশন, স্ক্রিনে ভেসে ওঠা।

> **সতর্কতা:** Channel-এর setting একবার তৈরি হয়ে গেলে কোড দিয়ে বদলানো যায় না। ইউজার app আনইনস্টল না করা পর্যন্ত পুরনো setting-ই থাকে। Setting বদলাতে হলে **নতুন id দিয়ে নতুন channel** বানাতে হয়।

বিস্তারিত → [notification_background_guide.md — 2.2](./notification_background_guide.md#22-notification-channel--বিস্তারিত)

---

## 2.5 Runtime Permission — Android 13+

```
Android 12 বা নিচে  →  install করলেই notification আসে
Android 13 বা উপরে  →  ইউজার "Allow" না চাপলে কিছুই আসবে না
```

কোড [4.3](#43-notificationservice)-এ আছে।

**কখন permission চাইবে:**

```
খারাপ  — app খোলার প্রথম সেকেন্ডে dialog দেখানো
ভালো   — আগে এক লাইনে কারণ বলো ("Appointment-এর reminder পেতে চাও?"),
         ইউজার রাজি হলে তারপর system dialog দেখাও
```

কারণ: ইউজার একবার Deny চাপলে dialog আর দেখানো যায় না। তখন হাতে Settings-এ গিয়ে চালু করতে হয় — বেশিরভাগ ইউজার করে না।

---

## 2.6 Release Build-এর সতর্কতা

Debug-এ চলে কিন্তু release APK-তে notification আসে না — খুব সাধারণ সমস্যা।

**১. ProGuard/R8** — `android/app/proguard-rules.pro`:

```proguard
-keep class com.google.firebase.** { *; }
-keep class com.google.android.gms.** { *; }
-dontwarn com.google.firebase.**
```

**২. Battery optimization** — Xiaomi, Oppo, Vivo, Realme-র ফোনে app বন্ধ থাকলে system নিজে FCM আটকায়। এটা Android-এর নিয়ম নয়, ওদের নিজস্ব। ইউজারকে Settings → Battery → App → "No restriction" করতে বলতে হয়।

বিস্তারিত → [notification_background_guide.md — 2.8](./notification_background_guide.md#28-android-battery-optimization--doze-mode)

---

# Part 3 — iOS

iOS-এর ধাপ বেশি, কারণ Apple নিজের সার্ভার (APNs) দিয়ে push পাঠায় এবং Firebase-কে সেখানে ঢোকার অনুমতি আলাদা করে দিতে হয়।

```
তোমার Server → Firebase (FCM) → Apple (APNs) → iPhone
                     │
                     └── এখানে .p8 key লাগে
```

## 3.1 App রেজিস্টার ও GoogleService-Info.plist

**১. Bundle ID বের করো:**

```bash
grep -r "PRODUCT_BUNDLE_IDENTIFIER" ios/Runner.xcodeproj/project.pbxproj | head -3
```

**২.** Firebase Console → Project Overview → iOS আইকন → Bundle ID দাও (উপরের মানের সাথে হুবহু এক)।

**৩.** `GoogleService-Info.plist` নামাও।

**৪. Xcode দিয়ে যোগ করো** (Finder দিয়ে টেনে আনলে হবে না):

```
১. open ios/Runner.xcworkspace     (.xcodeproj নয়)
২. Project Navigator-এ "Runner" folder-এ right click
৩. "Add Files to Runner..."
৪. GoogleService-Info.plist বেছে নাও
৫. অপশন:
      Copy items if needed          — টিক
      Create groups                 — টিক
      Add to targets: Runner        — টিক (এটা বাদ গেলে কাজ হবে না)
৬. Add
```

**যাচাই:** Xcode → Runner target → Build Phases → **Copy Bundle Resources** — এই তালিকায় `GoogleService-Info.plist` থাকতে হবে।

> **সতর্কতা:** এই ধাপ বাদ গেলে app চালু হওয়ার সাথে সাথে crash করবে — `Could not locate configuration file: 'GoogleService-Info.plist'`। ফাইলটা Finder-এ ঠিক জায়গায় থাকা যথেষ্ট নয়, Xcode target-এ যোগ করতেই হবে।

---

## 3.2 App ID-তে Push চালু করো

1. যাও → https://developer.apple.com/account
2. **Certificates, Identifiers & Profiles** → **Identifiers**
3. তোমার Bundle ID খুঁজে বের করো।

নেই? বানাও:

```
(+) → App IDs → Continue
Type: App → Continue
Description: My App
Bundle ID: Explicit → com.company.myapp
Capabilities তালিকায় "Push Notifications" টিক দাও
Continue → Register
```

আগে থেকে থাকলে ভেতরে ঢুকে **Push Notifications**-এ টিক আছে কিনা দেখো, না থাকলে টিক দিয়ে **Save**।

> **সতর্কতা:** App ID-তে Push চালু করার পর Provisioning Profile পুরনো হয়ে যায়। Xcode-এ Automatic signing থাকলে Xcode নিজে নতুন profile নামায়। Manual signing হলে portal থেকে profile আবার generate করে নামাতে হবে — নাহলে build হবে কিন্তু push আসবে না।

---

## 3.3 APNs Auth Key (.p8) বানাও

| | APNs Auth Key (.p8) | APNs Certificate (.p12) |
|---|---|---|
| মেয়াদ | শেষ হয় না | ১ বছর |
| কয়টা app | account-এর সব app | একটা app |
| Dev + Prod | একটাই key | আলাদা লাগে |
| কোনটা নেবে | **এটা** | পুরনো পদ্ধতি |

```
১. developer.apple.com/account
২. Certificates, Identifiers & Profiles → Keys
৩. (+) চাপো
৪. Key Name দাও — যেমন "MyApp APNs Key"
৫. "Apple Push Notifications service (APNs)" টিক দাও
৬. Continue → Register
৭. Download → AuthKey_ABC123XYZ.p8 নামবে
৮. একই পেজের Key ID (যেমন ABC123XYZ) কপি করে রাখো
```

> **গুরুত্বপূর্ণ সতর্কতা — মন দিয়ে পড়ো**
>
> `.p8` ফাইল **মাত্র একবার ডাউনলোড করা যায়**। পেজ ছেড়ে চলে গেলে Apple আর কখনো এই ফাইল দেবে না। হারালে key revoke করে নতুন বানানো ছাড়া উপায় নেই।
>
> এখনই করো:
> 1. ফাইলটা password manager বা secret vault-এ রাখো (1Password, Bitwarden, AWS Secrets Manager)।
> 2. **কখনো git-এ commit করবে না।** এই key দিয়ে যে কেউ তোমার Apple account-এর **সব app**-এর যেকোনো ইউজারকে push পাঠাতে পারে। Public repo-তে গেলে ধরে নাও key নষ্ট — revoke করে নতুন বানাতে হবে।
> 3. `.gitignore`-এ যোগ করো: `*.p8` এবং `*.p12`

**Team ID:** developer.apple.com/account → উপরে ডানে **Membership details** → Team ID (১০ অক্ষর, যেমন `9ABCD8EFGH`)।

হাতে রাখতে হবে তিনটা জিনিস: `.p8` ফাইল, Key ID, Team ID।

---

## 3.4 Firebase-এ .p8 Upload করো

```
১. Firebase Console → gear আইকন → Project settings
২. "Cloud Messaging" ট্যাব
৩. নিচে "Apple app configuration" অংশে যাও
৪. তোমার iOS app বেছে নাও
৫. "APNs Authentication Key" ঘরে Upload
৬. তিনটা জিনিস দাও: .p8 ফাইল, Key ID, Team ID
৭. Upload
```

সফল হলে Status **Active** দেখাবে।

একটাই key sandbox আর production দুটোতেই কাজ করে। Xcode থেকে চালানো build sandbox APNs ব্যবহার করে, App Store / TestFlight build production ব্যবহার করে — Firebase নিজে বুঝে নেয়।

---

## 3.5 Xcode Capabilities

```bash
open ios/Runner.xcworkspace
```

```
১. বাঁ পাশে Runner (নীল আইকন) → TARGETS → Runner
২. "Signing & Capabilities" ট্যাব
৩. "+ Capability" → Push Notifications
৪. "+ Capability" → Background Modes
      Background fetch        — টিক
      Remote notifications    — টিক
```

শেষে দেখতে হবে:

```
Signing & Capabilities
├── Signing (Automatically manage signing, Team: ...)
├── Push Notifications
└── Background Modes
    ├── Background fetch
    └── Remote notifications
```

**যাচাই করো:**

```bash
cat ios/Runner/Runner.entitlements
```

থাকতে হবে:

```xml
<key>aps-environment</key>
<string>development</string>
```

> **সতর্কতা:** `aps-environment` না থাকলে iOS-এ APNs token আসবে না। Dart-এ `getToken()` কোনো error ছাড়াই `null` দেবে। Capability যোগ করার পর একবার build করে ফাইলটা আবার দেখো।

**Deployment target:** Xcode-এর Minimum Deployments আর `ios/Podfile`-এর `platform :ios, '...'` এক রাখো। FlutterFire-এর current minimum তার [docs](https://firebase.google.com/docs/flutter/setup)-এ দেখে নাও; কম থাকলে `pod install` error দেবে।

---

## 3.6 AppDelegate.swift ও Info.plist

`ios/Runner/AppDelegate.swift`:

```swift
import UIKit
import Flutter
import FirebaseCore

@main
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {

    FirebaseApp.configure()          // GeneratedPluginRegistrant-এর আগে

    if #available(iOS 10.0, *) {
      UNUserNotificationCenter.current().delegate = self as? UNUserNotificationCenterDelegate
    }
    application.registerForRemoteNotifications()

    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}
```

`registerForRemoteNotifications()` না ডাকলে APNs token আসবে না। APNs token কে Firebase-এ পাঠানোর কাজ `firebase_messaging` plugin নিজেই করে (method swizzling) — তোমাকে callback লিখতে হবে না।

`ios/Runner/Info.plist` — Xcode-এ Background Modes capability দিলে এই key নিজেই যোগ হয়। না হলে হাতে দাও:

```xml
<key>UIBackgroundModes</key>
<array>
    <string>fetch</string>
    <string>remote-notification</string>
</array>
```

> `FirebaseAppDelegateProxyEnabled`-এর default মান **true** — অর্থাৎ Firebase নিজেই notification callback গুলো ধরে। তাই এই key যোগ করার দরকার নেই। শুধু যদি সব callback হাতে লিখতে চাও, তখন `false` দিয়ে বন্ধ করবে।

---

## 3.7 Device না Simulator

```
Real iPhone/iPad                                      কাজ করে
Apple Silicon Mac + macOS 13+ + iOS 16+ Simulator     সাধারণত কাজ করে
Intel Mac বা পুরনো Simulator                          APNs token আসে না
```

Xcode 14 থেকে Apple Silicon Mac-এ iOS 16+ Simulator remote notification register করতে পারে। তবু **release-এর আগে real device-এ test করা বাধ্যতামূলক** — Simulator-এর behaviour আর আসল device-এর behaviour এক নয়, বিশেষ করে terminated অবস্থায়।

**UI দেখার দ্রুত উপায় (যেকোনো Xcode 14+ Simulator):** একটা `.apns` ফাইল বানিয়ে Simulator window-তে drag করে ছাড়ো।

```json
{
  "Simulator Target Bundle": "com.company.myapp",
  "aps": {
    "alert": { "title": "Test", "body": "This is a test" },
    "badge": 1,
    "sound": "default"
  },
  "type": "appointment",
  "id": "123"
}
```

এটা শুধু notification-এর চেহারা দেখায়। FCM, token বা APNs — কোনো কিছুই এই পথে পরীক্ষা হয় না।

---

# Part 4 — Flutter Code

## 4.1 Package

```bash
flutter pub add firebase_core firebase_messaging flutter_local_notifications
```

`firebase_core` আর `firebase_messaging` একই FlutterFire release থেকে আসে, তাই দুটো একসাথে যোগ ও একসাথে upgrade করো।

**`flutter_local_notifications` কেন লাগে**

```
App background / terminated  →  FCM নিজে notification দেখায়
App foreground               →  কিছুই দেখায় না, তোমাকে দেখাতে হবে
```

---

## 4.2 main.dart

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'firebase_options.dart';
import 'services/notification_service.dart';

// top-level function হতে হবে — class-এর ভেতরে বা lambda নয়।
@pragma('vm:entry-point')
Future<void> firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  debugPrint('Background message: ${message.messageId}');
  // ভারী কাজ এখানে নয় — শুধু data সেভ বা notification দেখানো।
}

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  FirebaseMessaging.onBackgroundMessage(firebaseMessagingBackgroundHandler);

  await NotificationService.instance.init();
  runApp(const MyApp());
}
```

**তিনটা নিয়ম, ভাঙলে কাজ করবে না:**

1. Background handler **top-level** function।
2. `@pragma('vm:entry-point')` লাগবে। না দিলে release build-এ tree-shaking function-টা মুছে ফেলে — **debug-এ চলবে, release-এ চুপচাপ fail করবে**।
3. Handler-এর ভেতরে আবার `Firebase.initializeApp()` ডাকতে হবে। এটা আলাদা isolate — main isolate-এর কিছুই এখানে নেই।

---

## 4.3 NotificationService

`lib/services/notification_service.dart`:

```dart
import 'dart:convert';
import 'dart:io';

import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

class NotificationService {
  NotificationService._();
  static final NotificationService instance = NotificationService._();

  final FirebaseMessaging _fcm = FirebaseMessaging.instance;
  final FlutterLocalNotificationsPlugin _local = FlutterLocalNotificationsPlugin();

  // এই id AndroidManifest-এর default_notification_channel_id-এর সাথে হুবহু এক।
  static const AndroidNotificationChannel _channel = AndroidNotificationChannel(
    'high_importance_channel',
    'Important Notifications',
    description: 'Appointment, call এবং জরুরি বার্তা',
    importance: Importance.high,
  );

  Future<void> init() async {
    await _setupLocalNotifications();
    await _requestPermission();
    await _setupHandlers();
    await _logToken();
  }

  Future<void> _setupLocalNotifications() async {
    const androidInit = AndroidInitializationSettings('ic_notification');
    const iosInit = DarwinInitializationSettings(
      requestAlertPermission: false,   // permission নিজে চাইব
      requestBadgePermission: false,
      requestSoundPermission: false,
    );

    await _local.initialize(
      const InitializationSettings(android: androidInit, iOS: iosInit),
      onDidReceiveNotificationResponse: (response) {
        final payload = response.payload;
        if (payload != null) {
          _handleTap(jsonDecode(payload) as Map<String, dynamic>);
        }
      },
    );

    await _local
        .resolvePlatformSpecificImplementation<AndroidFlutterLocalNotificationsPlugin>()
        ?.createNotificationChannel(_channel);
  }

  Future<bool> _requestPermission() async {
    final settings = await _fcm.requestPermission(
      alert: true,
      badge: true,
      sound: true,
    );
    final status = settings.authorizationStatus;
    debugPrint('Notification permission: $status');
    return status == AuthorizationStatus.authorized ||
           status == AuthorizationStatus.provisional;
  }

  Future<void> _setupHandlers() async {
    // iOS-এ foreground-এ FCM যেন নিজে alert না দেখায় —
    // আমরা flutter_local_notifications দিয়ে দেখাব।
    await _fcm.setForegroundNotificationPresentationOptions(
      alert: false, badge: true, sound: false,
    );

    // A. App খোলা অবস্থায়
    FirebaseMessaging.onMessage.listen(_showLocal);

    // B. Background-এ ছিল, tap করে ফিরল
    FirebaseMessaging.onMessageOpenedApp.listen((m) => _handleTap(m.data));

    // C. App বন্ধ ছিল, tap করে খুলল
    final initial = await _fcm.getInitialMessage();
    if (initial != null) _handleTap(initial.data);
  }

  Future<void> _showLocal(RemoteMessage message) async {
    final notification = message.notification;
    if (notification == null) return;

    await _local.show(
      notification.hashCode,
      notification.title,
      notification.body,
      NotificationDetails(
        android: AndroidNotificationDetails(
          _channel.id,
          _channel.name,
          channelDescription: _channel.description,
          importance: Importance.high,
          priority: Priority.high,
          icon: 'ic_notification',
        ),
        iOS: const DarwinNotificationDetails(
          presentAlert: true, presentBadge: true, presentSound: true,
        ),
      ),
      payload: jsonEncode(message.data),
    );
  }

  void _handleTap(Map<String, dynamic> data) {
    debugPrint('Tap → type=${data['type']} id=${data['id']}');
    // navigation এখানে — যেমন router.go('/appointment/${data['id']}')
    // বিস্তারিত → deep-link-guide.md
  }

  Future<void> _logToken() async {
    // iOS-এ FCM token পাওয়ার আগে APNs token আসতে হয়।
    if (Platform.isIOS) {
      final apns = await _fcm.getAPNSToken();
      if (apns == null) {
        debugPrint('APNs token null — capability বা .p8 setup দেখো');
        return;
      }
    }

    debugPrint('FCM token: ${await _fcm.getToken()}');

    _fcm.onTokenRefresh.listen((newToken) {
      debugPrint('Token refreshed');
      // sendTokenToServer(newToken);
    });
  }

  Future<String?> getToken() => _fcm.getToken();
}
```

> **iOS-এর race condition:** app চালু হওয়ার সাথে সাথে `getToken()` ডাকলে `null` আসতে পারে, কারণ APNs token তখনো আসেনি। তাই উপরে আগে `getAPNSToken()` দেখা হয়েছে। এটা বাদ দিলে iOS-এ token কখনো আসবে কখনো আসবে না — এই bug ধরা কঠিন।

---

## 4.4 Token Backend-এ পাঠানো

```dart
Future<void> sendTokenToServer(String token) async {
  await dio.post('/api/devices', data: {
    'fcm_token': token,
    'platform': Platform.isIOS ? 'ios' : 'android',
    'app_version': packageInfo.version,
  });
}
```

| কখন | কেন |
|---|---|
| Login-এর পরপর | ইউজারের সাথে token যুক্ত করতে |
| `onTokenRefresh` এলে | Firebase নিজে token বদলাতে পারে |
| App খোলার সময় (দিনে একবার) | Server-এর পুরনো token ঠিক হয়ে যাবে |
| Logout-এ — **মুছে ফেলো** | নিচের সতর্কতা দেখো |

> **Logout-এ token না মুছলে data leak হয়।** একই ফোনে ইউজার A logout করে ইউজার B login করলে, server-এ পুরনো mapping থেকে গেলে A-র ব্যক্তিগত notification (যেমন "আপনার test report এসেছে") B-র ফোনে চলে যাবে। এটা privacy breach।

```dart
Future<void> onLogout() async {
  await dio.delete('/api/devices/$currentToken');
  await FirebaseMessaging.instance.deleteToken();
}
```

---

# Part 5 — Push পাঠানো

## 5.1 Firebase Console থেকে

1. App চালাও, log থেকে FCM token কপি করো।
2. Firebase Console → **Engage → Messaging** → **Create your first campaign** → **Firebase Notification messages**।
3. Title আর text লেখো।
4. **Send test message** চাপো → token পেস্ট করো → (+) → **Test**।

কয়েক সেকেন্ডে ফোনে notification আসা উচিত।

Custom data লাগলে campaign-এর **Additional options** অংশে key-value জোড়া দেওয়া যায় — deep link test করার জন্য এটাই ব্যবহার করো।

---

## 5.2 FCM HTTP v1 API

Server থেকে যেভাবে পাঠাবে, হাতে করে সেটাই।

**১. Service account key:**

```
Firebase Console → Project settings → "Service accounts" ট্যাব
→ Generate new private key → JSON ফাইল নামবে
```

> **এই JSON একটা server secret।** ভেতরে private key আছে। যার কাছে থাকবে সে তোমার সব ইউজারকে push পাঠাতে পারবে এবং project-এর অন্য অংশেও হাত দিতে পারবে।
> - **কখনো Flutter app-এর ভেতরে রাখবে না** — APK খুলে যে কেউ পড়ে নিতে পারে।
> - **কখনো git-এ commit করবে না।** `.gitignore`-এ `*-firebase-adminsdk-*.json` যোগ করো।
> - শুধু server-এর environment variable বা secret manager-এ রাখো।

**২. Access token:**

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/secure/path/service-account.json"
gcloud auth application-default print-access-token
```

**৩. পাঠাও:**

```bash
PROJECT_ID="myapp-dev-4f2a1"
ACCESS_TOKEN="ya29...."
DEVICE_TOKEN="dxK7..."

curl -X POST \
  "https://fcm.googleapis.com/v1/projects/$PROJECT_ID/messages:send" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "token": "'"$DEVICE_TOKEN"'",
      "notification": {
        "title": "Appointment Confirmed",
        "body": "ডাক্তার আপনার appointment নিশ্চিত করেছেন"
      },
      "data": { "type": "appointment", "id": "42" },
      "android": {
        "priority": "high",
        "notification": { "channel_id": "high_importance_channel", "sound": "default" }
      },
      "apns": {
        "headers": { "apns-priority": "10" },
        "payload": { "aps": { "sound": "default", "badge": 1 } }
      }
    }
  }'
```

সফল হলে: `{ "name": "projects/myapp-dev-4f2a1/messages/0:1731..." }`

**`data` বনাম `notification`**

| | শুধু `notification` | শুধু `data` | দুটো একসাথে |
|---|---|---|---|
| Foreground | তোমার কোড চলে | তোমার কোড চলে | তোমার কোড চলে |
| Background | System দেখায় | Handler চলে, তুমি দেখাও | System দেখায় + tap-এ data পাবে |
| Terminated (Android) | System দেখায় | Handler চলে | System দেখায় |
| Terminated (iOS) | System দেখায় | প্রায়ই চলে না | System দেখায় |

**নিয়ম:** ইউজারকে কিছু দেখাতে চাইলে `notification` + `data` দুটোই পাঠাও। `data` দিয়ে বলো tap-এর পরে কোন screen খুলবে।

বিস্তারিত → [notification_background_guide.md — 1.3](./notification_background_guide.md#13-fcm-firebase-cloud-messaging--deep-dive)

---

## 5.3 Legacy Server Key বন্ধ

পুরনো tutorial-এ এটা দেখতে পাবে:

```bash
# আর কাজ করে না
curl -X POST https://fcm.googleapis.com/fcm/send \
  -H "Authorization: key=AAAA..."
```

> **Legacy FCM API (`/fcm/send` এবং `Authorization: key=`) Google ২০২৪ সালের জুনে বন্ধ করে দিয়েছে।** পুরনো কোডে এটা থাকলে push যাবে না — 401 বা 404 আসবে।
>
> পার্থক্য:
> - URL: `/fcm/send` → `/v1/projects/{project-id}/messages:send`
> - Auth: স্থায়ী server key → service account থেকে বানানো OAuth2 token (১ ঘণ্টা পর মেয়াদ শেষ, server-এ auto refresh লাগবে)
> - Payload-এর গঠনও আলাদা — সবকিছু `"message"` object-এর ভেতরে

Backend-এ Firebase Admin SDK (Node, Python, PHP, Java) ব্যবহার করলে token refresh নিজেই হয়। হাতে না করাই ভালো।

---

## 5.4 Test Matrix

ছয়টা অবস্থা ছয়টা আলাদা code path — একটা test করে "কাজ করছে" বলা যাবে না।

| # | অবস্থা | কী হওয়া উচিত | Android | iOS |
|---|---|---|---|---|
| 1 | Foreground | `onMessage` চলবে, তুমি notification দেখাবে | ☐ | ☐ |
| 2 | Background | System notification দেখাবে | ☐ | ☐ |
| 3 | Terminated | System notification দেখাবে | ☐ | ☐ |
| 4 | Background থেকে tap | `onMessageOpenedApp` → সঠিক screen | ☐ | ☐ |
| 5 | Terminated থেকে tap | `getInitialMessage()` → সঠিক screen | ☐ | ☐ |
| 6 | Release build | উপরের পাঁচটাই আবার | ☐ | ☐ |

```
Foreground   → app স্ক্রিনে খোলা
Background   → Home button (app বন্ধ নয়)
Terminated   → recent apps থেকে swipe করে মুছে দাও
```

> **কেস ৬ বাদ দিও না।** ProGuard, tree-shaking আর signing-এর কারণে debug-এ চলা কোড release-এ ভাঙতে পারে। বিশেষ করে `@pragma('vm:entry-point')` ছাড়া background handler debug-এ ঠিক চলে, release-এ চুপচাপ বন্ধ থাকে।

```bash
flutter build apk --release && flutter install --release
flutter build ipa      # iOS — real device লাগবে
```

---

# Part 6 — সমস্যা ও সমাধান

## 6.1 Error Table

| লক্ষণ | সম্ভাব্য কারণ | কোথায় |
|---|---|---|
| iOS-এ token `null` | Capability নেই / `.p8` upload হয়নি / Simulator | [6.2 A](#a-ios-এ-token-null) |
| Build fail: `minSdkVersion cannot be smaller` | minSdk কম | [2.2](#22-gradle-configuration) |
| iOS crash: `Could not locate GoogleService-Info.plist` | Xcode target-এ যোগ হয়নি | [3.1](#31-app-রেজিস্টার-ও-googleservice-infoplist) |
| Token আছে, push আসে না | Package name / Bundle ID মিলছে না | [6.2 B](#b-token-আছে-কিন্তু-push-আসে-না) |
| Debug-এ আসে, release-এ না | `vm:entry-point` নেই / ProGuard | [6.2 C](#c-debug-এ-আসে-release-এ-আসে-না) |
| Foreground-এ কিছু দেখায় না | স্বাভাবিক — তোমাকে দেখাতে হবে | [4.1](#41-package) |
| Terminated-এ Android-এ আসে না | Channel id মিলছে না / battery | [6.2 D](#d-terminated-অবস্থায়-আসে-না) |
| Icon ধূসর বাক্স | Icon রঙিন, সাদা+transparent লাগবে | [2.4](#24-notification-icon-ও-channel) |
| `SenderId mismatch` | ভুল Firebase project-এর token | [6.2 E](#e-senderid-mismatch) |
| `Unregistered` | App uninstall / token পুরনো | [6.2 F](#f-unregistered) |
| API 401 / 404 | Legacy server key | [5.3](#53-legacy-server-key-বন্ধ) |

---

## 6.2 বিস্তারিত সমাধান

### A. iOS-এ token null

উপর থেকে নিচে ক্রম মেনে দেখো:

```bash
# ১. Real device কিনা? (পুরনো Simulator হলে এখানেই থামো)

# ২. entitlements ঠিক আছে?
cat ios/Runner/Runner.entitlements
#    aps-environment key থাকতে হবে

# ৩. plist bundle-এ যাচ্ছে?
#    Xcode → Runner target → Build Phases → Copy Bundle Resources

# ৪. Firebase-এ .p8 upload হয়েছে? Status Active?
#    Console → Project settings → Cloud Messaging → Apple app configuration

# ৫. Bundle ID তিন জায়গায় মিলছে?
grep -r "PRODUCT_BUNDLE_IDENTIFIER" ios/Runner.xcodeproj/project.pbxproj | head -3
grep -A1 "BUNDLE_ID" ios/Runner/GoogleService-Info.plist
#    + Apple Developer portal-এর App ID

# ৬. কোডে getToken()-এর আগে getAPNSToken() ডাকছো? (4.3)
```

সব ঠিক থাকলে শেষ চেষ্টা:

```bash
flutter clean
rm -rf ios/Pods ios/Podfile.lock
cd ios && pod install --repo-update && cd ..
flutter run
```

### B. Token আছে কিন্তু push আসে না

Firebase চুপচাপ ফেল করে। সাধারণত identifier মিলছে না।

```bash
grep applicationId android/app/build.gradle
grep package_name android/app/google-services.json
# + Firebase Console-এ Android app-এর package name
```

তিনটা হুবহু এক না হলে push আসবে না।

আরও দেখো:
- Token কি ঐ Firebase project-এরই? Dev project-এর token দিয়ে prod থেকে পাঠালে হবে না।
- App reinstall করলে token বদলায় — নতুন করে log থেকে নাও।
- Console-এর **Send test message** কাজ করে? করলে সমস্যা তোমার server-এ, app-এ নয়।

### C. Debug-এ আসে, release-এ আসে না

1. **`@pragma('vm:entry-point')` নেই** — সবচেয়ে সাধারণ কারণ। Release build-এ compiler background handler-কে অব্যবহৃত ধরে মুছে ফেলে।
2. **ProGuard rule নেই** — [2.6](#26-release-build-এর-সতর্কতা)।
3. **iOS APNs environment** — TestFlight/App Store build production APNs ব্যবহার করে, Xcode থেকে চালানো build sandbox। `.p8` key দুটোতেই চলে, তাই সমস্যা হয় না। পুরনো `.p12` certificate ব্যবহার করলে dev ও prod-এর জন্য আলাদা certificate লাগে।

### D. Terminated অবস্থায় আসে না

**Android**

1. Channel id মিলছে? Manifest-এর `default_notification_channel_id` == Dart-এর channel id। না মিললে Android 8+ এ চুপচাপ drop হয়।
2. Payload-এ শুধু `data` আছে, `notification` নেই? তাহলে system কিছু দেখাবে না — এটাই নিয়ম।
3. `priority: high` আছে? না থাকলে Doze mode-এ আটকে থাকতে পারে।
4. Xiaomi / Oppo / Vivo / Realme? Settings → Battery → App → "No restriction"। ইউজারকে বলা ছাড়া উপায় নেই।

**iOS**

1. শুধু `data` message terminated অবস্থায় প্রায়ই চলে না — `notification` block পাঠাও।
2. `apns-priority: 10` দাও।
3. Low Power Mode-এ background কাজ বন্ধ থাকে।

### E. SenderId mismatch

Token এক Firebase project-এর, push যাচ্ছে আরেক project থেকে।

1. App-এ কোন `google-services.json` / `GoogleService-Info.plist` আছে দেখো।
2. তার `project_id` আর server-এর project id মেলাও।
3. Flavor থাকলে — dev build-এ prod config ঢুকে যায়নি তো?

### F. Unregistered

ইউজার app uninstall করেছে, বা token পুরনো। **Server-এ এই token database থেকে মুছে ফেলো।** না মুছলে মরা token জমতে থাকবে, push পাঠানোর সময় ও খরচ দুটোই বাড়বে।

---

# Part 7 — Production

## 7.1 Release Checklist

**Firebase**
- [ ] Dev আর prod আলাদা project
- [ ] Production project-এ `.p8` upload করা, Status Active
- [ ] Analytics চালু (open rate দেখতে)

**Android**
- [ ] Release flavor-এর `google-services.json` ঠিক আছে
- [ ] minSdk build pass করছে
- [ ] ProGuard rule যোগ করা
- [ ] Icon সাদা + transparent, সব density-তে আছে
- [ ] `POST_NOTIFICATIONS` permission আছে
- [ ] Channel id manifest ও Dart কোডে এক
- [ ] Release APK-তে ৬টা test case পাস

**iOS**
- [ ] App ID-তে Push Notifications চালু
- [ ] Push Notifications + Background Modes capability আছে
- [ ] `Runner.entitlements`-এ `aps-environment` আছে
- [ ] `GoogleService-Info.plist` Copy Bundle Resources-এ আছে
- [ ] Real device-এ test হয়েছে
- [ ] TestFlight build-এ test হয়েছে (production APNs যাচাই)

**Code**
- [ ] Background handler top-level + `@pragma('vm:entry-point')`
- [ ] iOS-এ `getToken()`-এর আগে `getAPNSToken()` চেক
- [ ] `onTokenRefresh` শোনা ও server-এ পাঠানো হচ্ছে
- [ ] Logout-এ token মুছে ফেলা হচ্ছে
- [ ] Notification tap-এ সঠিক screen খুলছে
- [ ] Permission denied হলে app crash করছে না

**Server**
- [ ] HTTP v1 API (legacy key নয়)
- [ ] Service account JSON secret manager-এ, git-এ নেই
- [ ] `Unregistered` পেলে token মুছে ফেলা হচ্ছে
- [ ] Retry ও rate limit আছে

---

## 7.2 Security — কোন File গোপন

| File | গোপনীয়তা | কেন |
|---|---|---|
| `AuthKey_XXX.p8` | **সর্বোচ্চ** | Apple account-এর সব app-এ push পাঠানো যায়। Leak হলে revoke ছাড়া উপায় নেই |
| `service-account.json` | **সর্বোচ্চ** | Firebase project-এর admin access — Firestore, Storage সবকিছু |
| `*.p12` certificate | উচ্চ | পুরনো APNs পদ্ধতি, একই ঝুঁকি |
| Legacy server key | উচ্চ | এখন বন্ধ, তবু পুরনো কোড থেকে মুছে ফেলো |
| `google-services.json` | মাঝারি | App-এর ভেতরেই যায়, তাই গোপন নয়। তবু public repo-তে না রাখা ভালো; ভেতরের API key Google Cloud Console-এ restrict করে রাখো |
| `GoogleService-Info.plist` | মাঝারি | একই কথা |
| `firebase_options.dart` | মাঝারি | একই তথ্য, Dart-এ |

`.gitignore`:

```gitignore
# Apple push key ও certificate
*.p8
*.p12
*.mobileprovision

# Firebase server credential
*-firebase-adminsdk-*.json
service-account*.json

# Client config — public repo হলে এগুলোও ignore করো
# android/app/google-services.json
# ios/Runner/GoogleService-Info.plist
# lib/firebase_options.dart
```

> **ভুল করে `.p8` বা service account JSON commit করে ফেললে**
>
> নতুন commit-এ ফাইল মুছে দিলে যথেষ্ট নয় — git history-তে ফাইলটা থেকে যায় এবং পুরনো commit থেকে যে কেউ পড়তে পারে। Repo একবার push হয়ে থাকলে ধরে নাও key নষ্ট।
>
> এই ক্রমে করো:
> 1. **আগে key revoke করো** — Apple Developer → Keys → Revoke। Firebase-এর জন্য Google Cloud Console → IAM → Service Accounts → key delete।
> 2. নতুন key বানিয়ে যথাস্থানে বসাও।
> 3. তারপর history পরিষ্কার করো (`git filter-repo` বা BFG)।
>
> ক্রম উল্টে দিও না। History পরিষ্কার করতে সময় লাগে — ততক্ষণ পুরনো key কাজ করতেই থাকবে।

---

## আরও পড়ো

**এই repo-তে**
- [notification_background_guide.md](./notification_background_guide.md) — Notification ও Background Task-এর গভীর গাইড
- [deep-link-guide.md](./deep-link-guide.md) — Notification tap করে সঠিক screen-এ নেওয়া
- [flavor-setup-guide.md](./flavor-setup-guide.md) — Dev/Prod আলাদা Firebase project

**Official**
- [FlutterFire — Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/flutter/client)
- [FCM HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)
- [Apple — Setting up a remote notification server](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server)
- [Android — Notification channels](https://developer.android.com/develop/ui/views/notifications/channels)

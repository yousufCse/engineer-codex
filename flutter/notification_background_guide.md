# 📱 Notification & Background Task — সম্পূর্ণ গাইড
### Flutter Telemedicine Developer-দের জন্য — Production-Grade In-Depth Reference

> **ভাষা নীতি:** সমস্ত ব্যাখ্যা বাংলায়, Technical Term সমূহ English-এ অপরিবর্তিত।

---

## 📋 Table of Contents

### Part 1 — Abstract / Generic Concepts
- [1.1 Notification কী এবং কেন দরকার?](#11-notification-কী-এবং-কেন-দরকার)
- [1.2 Push Notification-এর সম্পূর্ণ Architecture](#12-push-notification-এর-সম্পূর্ণ-architecture)
- [1.3 FCM (Firebase Cloud Messaging) — Deep Dive](#13-fcm-firebase-cloud-messaging--deep-dive)
- [1.4 Notification-এর জীবনচক্র (Lifecycle)](#14-notification-এর-জীবনচক্র-lifecycle)
- [1.5 Background Task কী?](#15-background-task-কী)
- [1.6 Background Task-এর ৫টি Core Challenge](#16-background-task-এর-৫টি-core-challenge)
- [1.7 Task Scheduling-এর Abstract Model](#17-task-scheduling-এর-abstract-model)
- [1.8 Large File Upload-এর Conceptual Flow](#18-large-file-upload-এর-conceptual-flow)

### Part 2 — Android System
- [2.1 Android Notification System — Architecture](#21-android-notification-system--architecture)
- [2.2 Notification Channel — বিস্তারিত](#22-notification-channel--বিস্তারিত)
- [2.3 Android Notification Importance Levels](#23-android-notification-importance-levels)
- [2.4 Android Background Task — সব Mechanism](#24-android-background-task--সব-mechanism)
- [2.5 WorkManager — Production Guide](#25-workmanager--production-guide)
- [2.6 Foreground Service — File Upload-এর জন্য](#26-foreground-service--file-upload-এর-জন্য)
- [2.7 Android Battery Optimization & Doze Mode](#27-android-battery-optimization--doze-mode)
- [2.8 FCM on Android — Token, Data, Notification Message](#28-fcm-on-android--token-data-notification-message)

### Part 3 — iOS System
- [3.1 iOS Notification System — Architecture](#31-ios-notification-system--architecture)
- [3.2 APNs (Apple Push Notification Service) — Deep Dive](#32-apns-apple-push-notification-service--deep-dive)
- [3.3 iOS Notification Authorization & Categories](#33-ios-notification-authorization--categories)
- [3.4 iOS Background Modes — সব Option](#34-ios-background-modes--সব-option)
- [3.5 BGTaskScheduler — iOS 13+](#35-bgtaskscheduler--ios-13)
- [3.6 Background URLSession — Large File Upload](#36-background-urlsession--large-file-upload)
- [3.7 iOS-এর Background Execution Limits](#37-ios-এর-background-execution-limits)
- [3.8 FCM on iOS — APNs Bridge](#38-fcm-on-ios--apns-bridge)

### Part 4 — Flutter Context
- [4.1 Flutter Notification Stack Overview](#41-flutter-notification-stack-overview)
- [4.2 firebase_messaging Package — Complete Guide](#42-firebase_messaging-package--complete-guide)
- [4.3 flutter_local_notifications — Deep Dive](#43-flutter_local_notifications--deep-dive)
- [4.4 Flutter Isolate — Background কাজের ভিত্তি](#44-flutter-isolate--background-কাজের-ভিত্তি)
- [4.5 flutter_background_service — Persistent Background](#45-flutter_background_service--persistent-background)
- [4.6 workmanager Package — Scheduled Tasks](#46-workmanager-package--scheduled-tasks)
- [4.7 Large Document Upload — Production Implementation](#47-large-document-upload--production-implementation)
- [4.8 Telemedicine Use Case — Appointment Notification Flow](#48-telemedicine-use-case--appointment-notification-flow)
- [4.9 Production Checklist](#49-production-checklist)

---

## [↑ TOC](#-table-of-contents)

# Part 1 — Abstract / Generic Concepts

---

## 1.1 Notification কী এবং কেন দরকার?

**Notification** হলো একটি system-generated বা server-generated বার্তা যা user-কে কোনো event সম্পর্কে জানায় — app foreground-এ থাকুক বা না থাকুক।

### Notification-এর ৩টি মূল ধরন

```
┌─────────────────────────────────────────────────────────────┐
│                    NOTIFICATION TYPES                       │
├───────────────────┬──────────────────┬──────────────────────┤
│  LOCAL            │  PUSH            │  SILENT / DATA       │
│  NOTIFICATION     │  NOTIFICATION    │  NOTIFICATION        │
├───────────────────┼──────────────────┼──────────────────────┤
│ Device নিজেই      │ Server থেকে      │ Server থেকে আসে,    │
│ তৈরি করে         │ আসে              │ UI দেখায় না         │
│                   │                  │                      │
│ Example:          │ Example:         │ Example:             │
│ Appointment       │ Doctor Accept    │ Background data      │
│ Reminder          │ করলে notification│ sync, token refresh  │
│ (scheduled)       │                  │                      │
└───────────────────┴──────────────────┴──────────────────────┘
```

### Telemedicine-এ Notification কেন Critical?

| Use Case | Type | Priority |
|---|---|---|
| Appointment Confirmation | Push | High |
| Doctor Accept/Reject | Push | High |
| Video Call Incoming | Push (VoIP) | Critical |
| Document Upload Complete | Local | Normal |
| Prescription Ready | Push | High |
| Appointment Reminder (1 hr before) | Local Scheduled | High |
| Payment Confirmation | Push | Normal |

---

## [↑ TOC](#-table-of-contents)

## 1.2 Push Notification-এর সম্পূর্ণ Architecture

Push Notification-এ সবসময় **৩টি party** থাকে:

```
┌──────────────┐     ┌──────────────────┐     ┌─────────────┐
│   YOUR APP   │     │  PUSH SERVICE    │     │   DEVICE    │
│   SERVER     │     │  (FCM / APNs)    │     │   (User)    │
│  (Laravel /  │────▶│                  │────▶│             │
│   Node.js)   │     │  Google / Apple  │     │  Flutter    │
│              │     │  infrastructure  │     │  App        │
└──────────────┘     └──────────────────┘     └─────────────┘
     Step 1               Step 2                  Step 3
  Server sends         FCM/APNs routes          Device receives
  to FCM/APNs          to correct device        & shows notification
```

### বিস্তারিত Flow:

```mermaid
sequenceDiagram
    participant App as Flutter App
    participant FCM as FCM Server
    participant YourServer as Your Backend (Laravel)
    participant DB as Database

    Note over App,FCM: Registration Phase
    App->>FCM: getToken() request
    FCM-->>App: FCM Token (unique per device)
    App->>YourServer: Save token (with user_id)
    YourServer->>DB: Store fcm_token

    Note over YourServer,FCM: Send Notification Phase
    YourServer->>DB: Get patient's fcm_token
    YourServer->>FCM: POST /fcm/send {token, title, body, data}
    FCM->>App: Deliver notification
    App-->>App: Show notification OR handle silently
```

### Token কী এবং কেন গুরুত্বপূর্ণ?

**FCM Token** হলো একটি unique string যা প্রতিটি device+app combination-কে identify করে।

```
FCM Token Example:
dXNlcjEyMzQ1Njc4OTAxMjM0NTY3OD....(এরকম ~163 character)

এটি change হয় যখন:
├── App re-install হয়
├── User app data clear করে
├── Token expire হয় (FCM নিজেই refresh করে)
├── Device factory reset হয়
└── App নতুন device-এ restore হয়
```

**Production Rule:** Token সবসময় server-এ update করতে হবে। `onTokenRefresh` callback handle করতেই হবে।

---

## [↑ TOC](#-table-of-contents)

## 1.3 FCM (Firebase Cloud Messaging) — Deep Dive

FCM হলো Google-এর free push notification service। এটি Android এবং iOS উভয়ের জন্য কাজ করে।

### FCM Message-এর দুটি অংশ

```
┌─────────────────────────────────────────────┐
│              FCM MESSAGE                    │
├────────────────────┬────────────────────────┤
│  notification {}   │      data {}           │
├────────────────────┼────────────────────────┤
│ System handles     │ App handles            │
│ automatically      │ manually               │
│                    │                        │
│ title: "..."       │ appointment_id: "123"  │
│ body: "..."        │ doctor_id: "456"       │
│ icon: "..."        │ action: "confirm"      │
│                    │ deep_link: "/apt/123"  │
└────────────────────┴────────────────────────┘
       ▼                        ▼
  OS নিজে দেখায়          App-এর code
  (App dead থাকলেও)       handle করে
```

### FCM Message Types — গুরুত্বপূর্ণ পার্থক্য

| Message Type | `notification` field | `data` field | App State |
|---|---|---|---|
| **Notification Message** | ✅ আছে | ❌ নেই | App dead-এও দেখায় |
| **Data Message** | ❌ নেই | ✅ আছে | App running থাকলে handle করে |
| **Combined Message** | ✅ আছে | ✅ আছে | Background-এ OS দেখায়, Foreground-এ App handle করে |

### FCM Priority

```
priority: "high"    ──▶  Doze mode ভেঙে deliver হয় (তাৎক্ষণিক)
priority: "normal"  ──▶  Device active থাকলে deliver হয়
```

> ⚠️ **Android 13+ caveat:** যদি app বারবার high-priority message পাঠায় কিন্তু notification না দেখায়, Android OS সেই app-এর high-priority FCM messages downgrade করতে পারে। তাই high-priority শুধু সত্যিকারের urgent notification-এ ব্যবহার করুন।

**Telemedicine-এ সবসময় `priority: "high"` ব্যবহার করুন।**

---

## [↑ TOC](#-table-of-contents)

## 1.4 Notification-এর জীবনচক্র (Lifecycle)

App-এর তিনটি state-এ notification আলাদাভাবে আসে:

```
┌─────────────────────────────────────────────────────────┐
│                  APP STATES                             │
├──────────────┬──────────────────┬───────────────────────┤
│  FOREGROUND  │    BACKGROUND    │     TERMINATED        │
│  (App খোলা) │  (App minimize)  │  (App সম্পূর্ণ বন্ধ)  │
├──────────────┼──────────────────┼───────────────────────┤
│ Notification │ OS notification  │ OS notification       │
│ আসে কিন্তু  │ bar-এ দেখায়    │ bar-এ দেখায়          │
│ OS দেখায় না │                  │                       │
│              │ Tap করলে app    │ Tap করলে app          │
│ App নিজে    │ খোলে,           │ launch হয়,           │
│ handle করে  │ data পায়       │ data পায়             │
└──────────────┴──────────────────┴───────────────────────┘
```

### Flutter-এ তিনটি Handler

```
onMessage           ──▶  Foreground-এ notification আসলে
onMessageOpenedApp  ──▶  Background notification tap করলে
getInitialMessage   ──▶  Terminated থেকে tap করে app খুললে
```

---

## [↑ TOC](#-table-of-contents)

## 1.5 Background Task কী?

**Background Task** হলো এমন কাজ যা app user-এর সামনে (foreground) না থাকলেও চলতে থাকে।

### কেন Background Task দরকার? — Telemedicine Context

```
Problem:
User একটি 50MB MRI report upload করতে শুরু করল।
Upload হতে 2 মিনিট লাগবে।
User upload চলাকালীন অন্য app-এ গেল।

❌ Background Task ছাড়া:
   App background-এ গেলেই upload cancel হয়ে যাবে!

✅ Background Task দিয়ে:
   Upload চলতে থাকবে, complete হলে notification দেবে।
```

### Background Task-এর প্রকারভেদ

```
┌──────────────────────────────────────────────────────────────┐
│                   BACKGROUND TASK TYPES                      │
├──────────────────┬───────────────────┬───────────────────────┤
│  IMMEDIATE       │  DEFERRED         │  PERIODIC             │
│  (এখনই, কিন্তু  │  (পরে, শর্ত      │  (নির্দিষ্ট সময়      │
│  UI ছাড়া)       │  পূরণ হলে)        │  পর পর)               │
├──────────────────┼───────────────────┼───────────────────────┤
│ File Upload      │ Log sync          │ Token refresh         │
│ API call         │ Analytics send    │ Health check          │
│ Database write   │ Cache cleanup     │ Prescription reminder │
└──────────────────┴───────────────────┴───────────────────────┘
```

---

## [↑ TOC](#-table-of-contents)

## 1.6 Background Task-এর ৫টি Core Challenge

```
┌─────────────────────────────────────────────────────────────┐
│              BACKGROUND TASK CHALLENGES                     │
├─────┬───────────────────┬─────────────────────────────────  │
│ #   │ Challenge         │ কারণ                              │
├─────┼───────────────────┼────────────────────────────────── │
│ 1   │ Battery Drain     │ Background task CPU/network use   │
│     │                   │ করে, battery শেষ হয়              │
├─────┼───────────────────┼────────────────────────────────── │
│ 2   │ OS Killing        │ Android/iOS memory pressure-এ     │
│     │                   │ background app kill করে           │
├─────┼───────────────────┼────────────────────────────────── │
│ 3   │ Network           │ Background-এ network নাও পাওয়া   │
│     │                   │ যেতে পারে (Doze mode)             │
├─────┼───────────────────┼────────────────────────────────── │
│ 4   │ Execution Time    │ iOS background task-কে সর্বোচ্চ  │
│     │                   │ 30 second দেয়                     │
├─────┼───────────────────┼────────────────────────────────── │
│ 5   │ Resumability      │ Task interrupt হলে কোথা থেকে     │
│     │                   │ resume করবে?                      │
└─────┴───────────────────┴────────────────────────────────── │
```

---

## [↑ TOC](#-table-of-contents)

## 1.7 Task Scheduling-এর Abstract Model

```mermaid
flowchart TD
    A[Task Submit] --> B{Constraints Check}
    B -->|Network Available?| C{Battery OK?}
    B -->|No Network| W[Wait for Network]
    W --> B
    C -->|Yes| D[Task Queue]
    C -->|Low Battery| WB[Wait / Defer]
    WB --> C
    D --> E[Task Executor]
    E --> F{Task Success?}
    F -->|Yes| G[Mark Complete\nSend Notification]
    F -->|No - Retryable| H[Backoff & Retry]
    H --> E
    F -->|No - Fatal| I[Mark Failed\nNotify User]
```

### Retry Strategy — Exponential Backoff

```
Attempt 1:  Wait 10s
Attempt 2:  Wait 20s
Attempt 3:  Wait 40s
Attempt 4:  Wait 80s
...
Max Attempts: 3-5 (production-এ)
```

---

## [↑ TOC](#-table-of-contents)

## 1.8 Large File Upload-এর Conceptual Flow

```
┌─────────────────────────────────────────────────────────────┐
│              LARGE FILE UPLOAD - CHUNKED STRATEGY           │
└─────────────────────────────────────────────────────────────┘

File: MRI_Report.pdf (50 MB)
                    │
                    ▼
        ┌─────────────────────┐
        │   CHUNK SPLITTING   │
        │  50MB ÷ 5MB = 10    │
        │  chunks             │
        └─────────────────────┘
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Chunk 1   Chunk 2 ... Chunk 10
       (5MB)     (5MB)       (5MB)
          │         │         │
          ▼         ▼         ▼
       Upload    Upload    Upload
       Server    Server    Server
          │         │         │
          └─────────┼─────────┘
                    ▼
        ┌─────────────────────┐
        │  SERVER REASSEMBLE  │
        │  10 chunks → 1 file │
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │ NOTIFICATION SENT   │
        │ "Upload Complete!"  │
        └─────────────────────┘

Benefit: যেকোনো chunk fail হলে শুধু সেটি retry করো।
         পুরো file আবার upload করতে হবে না।
```

---

# Part 2 — Android System

---

## [↑ TOC](#-table-of-contents)

## 2.1 Android Notification System — Architecture

Android-এ notification system OS-level-এ built-in। এটি **NotificationManager** service দ্বারা পরিচালিত হয়।

```
┌────────────────────────────────────────────────────────────┐
│                   ANDROID OS                               │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              SystemUI Process                        │  │
│  │   ┌─────────────────────────────────────────────┐   │  │
│  │   │         Notification Shade                  │   │  │
│  │   │  (Status bar থেকে নামানো notification list) │   │  │
│  │   └─────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ▲                                  │
│                          │                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         NotificationManagerService                   │  │
│  │         (System Server-এ চলে)                        │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ▲                                  │
│                          │  notify()                        │
│  ┌───────────────────┐   │                                  │
│  │   Your Flutter    │───┘                                  │
│  │   App Process     │                                      │
│  └───────────────────┘                                      │
└────────────────────────────────────────────────────────────┘
```

### Notification Build করার উপাদান

```
NotificationCompat.Builder
├── setSmallIcon()          ─── Status bar-এর ছোট icon (mandatory)
├── setContentTitle()       ─── বড় শিরোনাম
├── setContentText()        ─── সংক্ষিপ্ত বার্তা
├── setStyle()              ─── BigText / BigPicture / Inbox
├── setPriority()           ─── PRIORITY_HIGH, DEFAULT, LOW
├── setAutoCancel()         ─── Tap করলে dismiss হবে কিনা
├── setContentIntent()      ─── Tap করলে কী হবে (PendingIntent)
├── addAction()             ─── Action button (Accept / Reject)
├── setProgress()           ─── Upload progress bar
├── setOngoing()            ─── Dismiss করা যাবে না (foreground service)
└── setChannelId()          ─── Android 8+ এ mandatory
```

---

## [↑ TOC](#-table-of-contents)

## 2.2 Notification Channel — বিস্তারিত

**Android 8.0 (API 26) থেকে Notification Channel mandatory।** Channel হলো notification-এর category, যা user নিজে customize করতে পারে।

### Channel কেন দরকার?

```
আগে (Android 7 এবং নিচে):
  App সব notification send করত, user শুধু সব বন্ধ করতে পারত।

এখন (Android 8+):
  App channel তৈরি করে।
  User প্রতিটি channel আলাদাভাবে control করতে পারে।

Example:
  ✅ "Appointment" channel — চালু রাখা
  ✅ "Video Call" channel — চালু রাখা
  ❌ "Promotions" channel — বন্ধ করা
```

### Telemedicine App-এর Channels

```kotlin
// Android Native (Kotlin) — Flutter plugin এটি internally করে
val channels = listOf(
    // Channel 1: Video Call (সর্বোচ্চ গুরুত্ব)
    NotificationChannel(
        "video_call",
        "Video Consultation",
        NotificationManager.IMPORTANCE_HIGH
    ).apply {
        description = "Incoming video consultation calls"
        enableVibration(true)
        setSound(callRingtone, audioAttributes)
        lockscreenVisibility = Notification.VISIBILITY_PUBLIC
    },

    // Channel 2: Appointment
    NotificationChannel(
        "appointment",
        "Appointment Updates",
        NotificationManager.IMPORTANCE_HIGH
    ).apply {
        description = "Appointment confirmations and reminders"
        enableVibration(true)
    },

    // Channel 3: Document Upload
    NotificationChannel(
        "document_upload",
        "Document Upload",
        NotificationManager.IMPORTANCE_LOW
    ).apply {
        description = "Document upload progress and completion"
        setSound(null, null)  // Upload-এ sound নেই
    },

    // Channel 4: Prescription
    NotificationChannel(
        "prescription",
        "Prescriptions",
        NotificationManager.IMPORTANCE_DEFAULT
    )
)
```

### Channel Importance Levels

```
IMPORTANCE_NONE     ──▶ Notification দেখায় না
IMPORTANCE_MIN      ──▶ Status bar-এ শুধু icon
IMPORTANCE_LOW      ──▶ Sound/vibration নেই, list-এ দেখায়
IMPORTANCE_DEFAULT  ──▶ Sound আছে, heads-up নেই
IMPORTANCE_HIGH     ──▶ Sound + Heads-up popup ✅ (Vibration: channel-এ enableVibration(true) না দিলে গ্যারান্টি নেই)
IMPORTANCE_MAX      ──▶ (Deprecated, HIGH ব্যবহার করুন)
```

---

## [↑ TOC](#-table-of-contents)

## 2.3 Android Notification Importance Levels

```
┌──────────────────────────────────────────────────────────────┐
│  IMPORTANCE_HIGH — Heads-up Notification                     │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  📞 Dr. Rahman wants to start your consultation     │   │
│  │     Telemedicine App           Accept  Decline      │   │
│  └──────────────────────────────────────────────────────┘   │
│  (Screen-এর উপরে popup হয়, interrupt করে)                  │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  IMPORTANCE_DEFAULT — Standard Notification                  │
│                                                              │
│  Status bar-এ icon, sound আছে, heads-up নেই                 │
│  Notification shade-এ দেখায়                                 │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  IMPORTANCE_LOW — Silent Notification                        │
│                                                              │
│  Document upload progress-এর জন্য ভালো।                    │
│  Sound/vibration নেই। Shade-এ দেখায়।                       │
└──────────────────────────────────────────────────────────────┘
```

---

## [↑ TOC](#-table-of-contents)

## 2.4 Android Background Task — সব Mechanism

Android-এ background task-এর জন্য বিভিন্ন mechanism আছে, যেগুলো বিভিন্ন use case-এ ব্যবহার হয়।

```
┌─────────────────────────────────────────────────────────────┐
│           ANDROID BACKGROUND EXECUTION OPTIONS              │
├──────────────────────┬──────────────────────────────────────┤
│  MECHANISM           │  USE CASE                           │
├──────────────────────┼──────────────────────────────────────┤
│  WorkManager         │  Guaranteed, deferrable tasks        │
│  (Recommended ✅)    │  Log sync, token refresh             │
├──────────────────────┼──────────────────────────────────────┤
│  Foreground Service  │  Long-running, user-visible tasks   │
│  (File Upload ✅)    │  File upload, music playback         │
├──────────────────────┼──────────────────────────────────────┤
│  JobScheduler        │  System-condition-based tasks        │
│  (WorkManager        │  (WorkManager এটি internally ব্যবহার│
│  internally uses it) │  করে, সরাসরি কম ব্যবহার করুন)      │
├──────────────────────┼──────────────────────────────────────┤
│  AlarmManager        │  Exact time-based tasks              │
│                      │  Appointment reminder                │
├──────────────────────┼──────────────────────────────────────┤
│  Thread / Coroutine  │  App চলাকালীন async কাজ             │
│                      │  (Background task নয়)               │
└──────────────────────┴──────────────────────────────────────┘
```

---

## [↑ TOC](#-table-of-contents)

## 2.5 WorkManager — Production Guide

**WorkManager** হলো Android Jetpack-এর সবচেয়ে গুরুত্বপূর্ণ background task library। এটি **guaranteed execution** দেয় — device restart হলেও task হারায় না।

### WorkManager কীভাবে কাজ করে?

```mermaid
flowchart LR
    A[App: enqueueWork] --> B[WorkManager]
    B --> C{API Level?}
    C -->|API 23+| D[JobScheduler]
    C -->|API 14-22| E[AlarmManager +\nBroadcastReceiver]
    D --> F[Execute Worker]
    E --> F
    F --> G{Success?}
    G -->|Yes| H[Done ✅]
    G -->|No| I[Retry with\nBackoff]
    I --> F
```

### WorkManager-এর Key Concepts

**Constraints (শর্ত):**
```
Constraints.Builder()
  .setRequiredNetworkType(NetworkType.CONNECTED)  // Network লাগবে
  .setRequiresBatteryNotLow(true)                 // Battery low হলে না
  .setRequiresCharging(false)                     // Charge দরকার নেই
  .setRequiresStorageNotLow(true)                 // Storage কম হলে না
  .build()
```

**Work Types:**
```
OneTimeWorkRequest  ──▶  একবার চলবে (Token sync, Log send)
PeriodicWorkRequest ──▶  বারবার চলবে (minimum 15 min interval)
```

**Work Chain (Chaining):**
```kotlin
// কাজগুলো পরপর করা
WorkManager.getInstance(context)
    .beginWith(compressDocumentWork)    // প্রথমে compress
    .then(uploadDocumentWork)           // তারপর upload
    .then(notifyServerWork)             // তারপর server-কে জানাও
    .enqueue()
```

### WorkManager vs Foreground Service

```
┌─────────────────────────────────────────────────────────────┐
│  কখন WorkManager, কখন Foreground Service?                   │
├──────────────────────────┬──────────────────────────────────┤
│  WorkManager             │  Foreground Service              │
├──────────────────────────┼──────────────────────────────────┤
│ Deferrable/short tasks   │ Long-running, user-visible tasks │
│ Deferrable               │ Immediate                        │
│ System decides timing    │ App controls timing              │
│ No UI required           │ Persistent notification required │
│ Log sync, Token refresh  │ File upload, Music, Location     │
└──────────────────────────┴──────────────────────────────────┘
```

---

## [↑ TOC](#-table-of-contents)

## 2.6 Foreground Service — File Upload-এর জন্য

**Foreground Service** হলো এমন একটি service যা:
1. User-কে notification দিয়ে জানায় "আমি background-এ কাজ করছি"
2. OS এটিকে সহজে kill করে না
3. দীর্ঘ সময় চলতে পারে

### কেন File Upload-এ Foreground Service?

```
WorkManager দিয়ে 50MB upload:
  Problem: WorkManager regular Worker-এ progress notification update করা কঠিন,
           এবং app standby bucket quota দীর্ঘ upload-এর জন্য উপযুক্ত নয়।
           setForeground() দিয়ে long-running WorkManager worker সম্ভব,
           কিন্তু তখন সেটি internally Foreground Service-ই হয়ে যায়।

Foreground Service দিয়ে:
  No execution time cap ✅
  OS kill করে না ✅
  Progress notification দেখায় ✅
  User সবসময় জানে কী হচ্ছে ✅
```

### Foreground Service-এর Notification (Mandatory)

```
┌─────────────────────────────────────────────────┐
│  📤  Uploading MRI Report                       │
│      Telemedicine                    [Cancel]   │
│  ████████████░░░░░░░░  65% (32.5 MB / 50 MB)   │
└─────────────────────────────────────────────────┘

এই notification ছাড়া Foreground Service চলে না।
User জানে কী হচ্ছে — এটি UX-এর জন্যও ভালো।
```

### Android 14+ Foreground Service Type

Android 14 (API 34) থেকে foreground service type declare করতে হয়:

```xml
<!-- AndroidManifest.xml -->
<service
    android:name=".UploadService"
    android:foregroundServiceType="dataSync"
    android:exported="false" />

<!-- Possible types: -->
<!-- camera, connectedDevice, dataSync, health,      -->
<!-- location, mediaPlayback, mediaProjection,       -->
<!-- microphone, phoneCall, remoteMessaging,         -->
<!-- shortService, specialUse, systemExempted        -->
```

---

## [↑ TOC](#-table-of-contents)

## 2.7 Android Battery Optimization & Doze Mode

Android device idle থাকলে battery বাঁচাতে **Doze Mode** এবং **App Standby** চালু হয়।

### Doze Mode কী?

```
┌─────────────────────────────────────────────────────────────┐
│                    DOZE MODE TIMELINE                       │
│                                                             │
│  Device screen off + unplugged + stationary                 │
│                                                             │
│  0 min ─────────────────────────────────────────▶          │
│         │                                                   │
│    ~কিছুক্ষণ পর: Light Doze শুরু (সময় device-ভেদে ভিন্ন) │
│         │  Network: ✅ (কম)  Alarm: ✅ (restricted)        │
│         │                                                   │
│    আরও পরে: Deep Doze শুরু (সময় officially documented নয়) │
│         │  Network: ❌        Alarm: ❌                      │
│         │  FCM High Priority: ✅ (একমাত্র exception)        │
│         │                                                   │
│    Maintenance Window (মাঝেমধ্যে):                          │
│         │  Network: ✅ (কিছুক্ষণ)  Tasks run               │
│         │                                                   │
│    User touches device: Doze exit                           │
└─────────────────────────────────────────────────────────────┘
```

### FCM High Priority — Doze Exception

```
FCM message-এ priority: "high" দিলে:
  ✅ Doze mode-এও device wake up করে
  ✅ Network briefly available হয়
  ✅ Notification deliver হয়

এজন্য appointment confirmation-এ সবসময় high priority দিন।
```

### Battery Optimization Exemption

Production app-এ user-কে battery optimization থেকে exempt করতে বলা যায়:

```dart
// flutter_background_service package ব্যবহার করলে
// Settings খুলে user-কে manually exempt করতে গাইড করুন

// Android: Settings > Apps > YourApp > Battery > Unrestricted
```

---

## [↑ TOC](#-table-of-contents)

## 2.8 FCM on Android — Token, Data, Notification Message

### Android-এ FCM কীভাবে কাজ করে?

```
┌─────────────────────────────────────────────────────────────┐
│                     ANDROID DEVICE                          │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │               Google Play Services                  │   │
│  │  (FCM connection এখানেই manage হয়)                 │   │
│  │                                                     │   │
│  │  ┌──────────────────────────────────────────────┐  │   │
│  │  │         FCM Persistent Connection            │  │   │
│  │  │   Google servers-এর সাথে সবসময় connected   │  │   │
│  │  └──────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│              Message আসলে │                                 │
│                           ▼                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  App Background/Killed:                             │   │
│  │    notification{} → OS নিজেই দেখায়                 │   │
│  │    data{} → App launch হলে পাবে                     │   │
│  │                                                     │   │
│  │  App Foreground:                                    │   │
│  │    সব message → App-এর onMessage() callback        │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Android-এ Required Permissions (AndroidManifest.xml)

```xml
<!-- FCM-এর জন্য -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />

<!-- Android 13+ (API 33) — Runtime permission দরকার -->
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

<!-- Foreground Service (File Upload) -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />

<!-- WorkManager (Automatic — তবে explicit-এ ভালো) -->
<uses-permission android:name="android.permission.WAKE_LOCK" />

<!-- Exact Alarm (Appointment Reminder) -->
<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
<!-- Android 12+ এ user permission লাগে -->
<uses-permission android:name="android.permission.USE_EXACT_ALARM" />
```

---

# Part 3 — iOS System

---

## [↑ TOC](#-table-of-contents)

## 3.1 iOS Notification System — Architecture

iOS-এর notification system Android-এর চেয়ে বেশি restrictive কিন্তু বেশি consistent।

```
┌─────────────────────────────────────────────────────────────┐
│                         iOS                                 │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Notification Center (OS)               │   │
│  │   User সব notification এখান থেকে manage করে       │   │
│  └─────────────────────────────────────────────────────┘   │
│                           ▲                                 │
│                           │                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         UNUserNotificationCenter                    │   │
│  │  (App notification-এর সাথে interact করার API)      │   │
│  └─────────────────────────────────────────────────────┘   │
│              ▲                        ▲                     │
│              │                        │                     │
│  ┌───────────────────┐    ┌──────────────────────────┐     │
│  │  Remote (Push)    │    │  Local Notification      │     │
│  │  APNs → FCM →     │    │  App নিজেই schedule করে │     │
│  │  Your App         │    │  (Appointment Reminder)  │     │
│  └───────────────────┘    └──────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## [↑ TOC](#-table-of-contents)

## 3.2 APNs (Apple Push Notification Service) — Deep Dive

**APNs** হলো Apple-এর push notification infrastructure। FCM iOS-এ push notification পাঠাতে APNs ব্যবহার করে।

### FCM → APNs → Device Flow

```mermaid
sequenceDiagram
    participant YS as Your Server
    participant FCM as FCM Server
    participant APNs as Apple APNs
    participant Device as iOS Device

    YS->>FCM: Send notification\n(FCM Token দিয়ে)
    FCM->>APNs: Forward via APNs\n(APNs Token দিয়ে)
    APNs->>Device: Deliver to device\n(secure connection)
    Device-->>Device: Show notification
```

### APNs-এর Key Points

```
1. FCM internally APNs ব্যবহার করে iOS-এ।
   তোমাকে সরাসরি APNs handle করতে হবে না।

2. APNs Authentication:
   Firebase Console-এ APNs key (.p8 file) upload করতে হয়।
   এটি না করলে iOS-এ push কাজ করবে না।

3. APNs Environment:
   Development: sandbox APNs
   Production: production APNs
   Firebase automatically সঠিকটি ব্যবহার করে।
```

### Firebase Console-এ APNs Setup

```
Firebase Console
  └── Project Settings
      └── Cloud Messaging
          └── Apple app configuration
              ├── APNs Authentication Key (.p8) ──▶ Recommended
              └── APNs Certificates (.p12) ──▶ Older method
```

---

## [↑ TOC](#-table-of-contents)

## 3.3 iOS Notification Authorization & Categories

iOS-এ notification দেখাতে **user permission** নিতেই হবে। এটি mandatory।

### Permission Request Flow

```mermaid
flowchart TD
    A[App First Launch] --> B[Request Permission]
    B --> C{iOS System Dialog}
    C -->|Allow| D[Authorized ✅\nAll notifications work]
    C -->|Don't Allow| E[Denied ❌\nNo notifications]
    E --> F[User goes to\nSettings > App > Notifications]
    F --> G[Manually enable]
    G --> D
    D --> H[Provisional Authorization\niOS 12+: provisional দিয়ে\nQuiet delivery শুরু করা যায়]
```

### Permission Types

```swift
// iOS Native (Swift) — Flutter plugin internally করে
UNUserNotificationCenter.current().requestAuthorization(
    options: [
        .alert,   // Screen-এ notification দেখানো
        .sound,   // Sound বাজানো
        .badge,   // App icon-এ badge number
        .criticalAlert,  // DND ভেঙে sound (medical apps)
        .provisional     // Quietly deliver করা (user confirm লাগে না)
    ]
)
```

### Critical Alert — Telemedicine-এর জন্য Special

```
Critical Alert:
  ✅ Do Not Disturb (DND) mode ভেঙে sound বাজায়
  ✅ মধ্যরাতেও notification যায়
  ❌ Apple-এর special permission দরকার (entitlement)
  ✅ Medical/Healthcare apps পায় (application করতে হয়)

Telemedicine app-এ incoming video call-এর জন্য এটি কাজে আসে।
```

### Notification Categories (Action Buttons)

```
iOS notification-এ iOS style Action button যোগ করা যায়:

┌──────────────────────────────────────────────────────┐
│  📅  Dr. Rahman has confirmed your appointment       │
│      Tomorrow, 10:00 AM                              │
│  ┌──────────────────┐  ┌──────────────────────────┐ │
│  │   View Details   │  │      Reschedule           │ │
│  └──────────────────┘  └──────────────────────────┘ │
└──────────────────────────────────────────────────────┘

// Category define করতে হয়:
let viewAction = UNNotificationAction(identifier: "VIEW", title: "View Details")
let rescheduleAction = UNNotificationAction(identifier: "RESCHEDULE", title: "Reschedule")
let category = UNNotificationCategory(identifier: "APPOINTMENT", actions: [...])
```

---

## [↑ TOC](#-table-of-contents)

## 3.4 iOS Background Modes — সব Option

iOS background execution-এর জন্য **Info.plist**-এ Background Modes declare করতে হয়।

```
iOS Background Modes (UIBackgroundModes):
├── fetch                    ─── Background App Refresh
├── remote-notification      ─── Silent Push Notification handle
├── processing               ─── BGTaskScheduler (iOS 13+)
├── background-url-session   ─── Background URLSession (File Upload)
├── voip                     ─── VoIP (Video Call)
├── audio                    ─── Background Audio
├── location                 ─── Background Location
└── bluetooth-central        ─── Bluetooth
```

### Telemedicine App-এর Required Background Modes

```xml
<!-- Info.plist -->
<key>UIBackgroundModes</key>
<array>
    <string>remote-notification</string>  <!-- FCM silent push -->
    <string>fetch</string>                <!-- Background refresh -->
    <string>processing</string>           <!-- BGTaskScheduler -->
    <string>background-url-session</string> <!-- File upload -->
    <string>voip</string>                 <!-- Video call -->
</array>
```

---

## [↑ TOC](#-table-of-contents)

## 3.5 BGTaskScheduler — iOS 13+

**BGTaskScheduler** হলো iOS 13+ এর modern background task API। এটি দুই ধরনের task support করে।

```
┌──────────────────────────────────────────────────────────────┐
│                   BGTaskScheduler                            │
├────────────────────────────┬─────────────────────────────────┤
│  BGAppRefreshTask          │  BGProcessingTask               │
├────────────────────────────┼─────────────────────────────────┤
│ Short tasks (Apple officially │ Long tasks (minutes)           │
│ কোনো exact limit document  │ Database migration, ML training │
│ করেনি; ~30s community      │                                 │
│ estimate)                  │                                 │
│ App refresh, data sync     │                                 │
│ Network: Maybe not         │ Network: Yes                    │
│ Frequency: System decides  │ Requires: Charging (optional)   │
└────────────────────────────┴─────────────────────────────────┘
```

### BGTaskScheduler Registration

```swift
// AppDelegate.swift
BGTaskScheduler.shared.register(
    forTaskWithIdentifier: "com.yourapp.appointment.sync",
    using: nil
) { task in
    self.handleAppRefresh(task: task as! BGAppRefreshTask)
}

BGTaskScheduler.shared.register(
    forTaskWithIdentifier: "com.yourapp.document.cleanup",
    using: nil
) { task in
    self.handleProcessing(task: task as! BGProcessingTask)
}
```

### iOS Background Execution — Important Limits

```
┌─────────────────────────────────────────────────────────────┐
│                  iOS EXECUTION LIMITS                       │
├──────────────────────────┬──────────────────────────────────┤
│  Background URLSession   │  No time limit ✅                │
│  (File Upload)           │  iOS manages the transfer        │
├──────────────────────────┼──────────────────────────────────┤
│  BGAppRefreshTask        │  ~30 seconds ⚠️                  │
├──────────────────────────┼──────────────────────────────────┤
│  BGProcessingTask        │  Few minutes (variable) ⚠️       │
├──────────────────────────┼──────────────────────────────────┤
│  Background fetch        │  ~30 seconds ⚠️                  │
│  (legacy)                │                                  │
├──────────────────────────┼──────────────────────────────────┤
│  VoIP push handler       │  ~30 seconds ⚠️                  │
└──────────────────────────┴──────────────────────────────────┘
```

---

## [↑ TOC](#-table-of-contents)

## 3.6 Background URLSession — Large File Upload

iOS-এ large file upload-এর **একমাত্র সঠিক উপায়** হলো **Background URLSession**।

### কীভাবে কাজ করে?

```
Normal URLSession:
  App → Network → Server
  App kill হলে upload cancel ❌

Background URLSession:
  App → NSURLSession Daemon (OS process) → Network → Server
  App kill হলেও OS upload চালিয়ে যায় ✅
  Upload complete হলে App wake up করে ✅
```

```
┌──────────────────────────────────────────────────────────────┐
│                         iOS                                  │
│                                                              │
│  ┌──────────────┐    ┌─────────────────────────────────┐    │
│  │  Your App    │    │  NSURLSession Background Daemon │    │
│  │              │───▶│  (Separate OS process)          │    │
│  │  Upload file │    │                                 │    │
│  │  (then kill) │    │  ┌─────────────────────────┐   │    │
│  └──────────────┘    │  │  Upload continues...    │   │    │
│                       │  │  Even when app is dead  │   │    │
│                       │  └─────────────────────────┘   │    │
│                       └──────────────┬──────────────────┘    │
│                                      │ Upload Complete        │
│                                      ▼                       │
│  ┌──────────────┐    ┌──────────────────────────────────┐   │
│  │  Your App    │◀───│  OS wakes app (background)       │   │
│  │  (woken up)  │    │  handleEventsForBackgroundURLSes  │   │
│  └──────────────┘    └──────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

### iOS AppDelegate-এ Required Handler

```swift
// AppDelegate.swift
func application(
    _ application: UIApplication,
    handleEventsForBackgroundURLSession identifier: String,
    completionHandler: @escaping () -> Void
) {
    // iOS এই method call করে যখন background upload complete হয়
    // completionHandler() call করতে হবে
    backgroundCompletionHandler = completionHandler
}
```

---

## [↑ TOC](#-table-of-contents)

## 3.7 iOS-এর Background Execution Limits

### iOS কখন Background Task Kill করে?

```
Kill করার কারণ:
├── Memory pressure (RAM কম থাকলে)
├── Time limit exceed (task-specific)
├── User force-close করলে
└── Low Power Mode (iOS 9+)

Kill না করার guarantee:
├── Background URLSession upload
│   (OS process, app-এর বাইরে)
└── VoIP connection (CallKit ব্যবহার করলে)
```

### Low Power Mode-এ কী হয়?

```
Low Power Mode চালু হলে:
  ❌ Background App Refresh বন্ধ হয়
  ❌ Push notification delay হতে পারে
  ❌ Background fetch কম frequent হয়
  ✅ FCM High Priority push আসে (APNs delivers)
  ✅ Background URLSession চলতে থাকে
```

---

## [↑ TOC](#-table-of-contents)

## 3.8 FCM on iOS — APNs Bridge

FCM iOS-এ কাজ করে APNs-এর মাধ্যমে। এটি বোঝা গুরুত্বপূর্ণ।

```
┌─────────────────────────────────────────────────────────────┐
│              FCM ON iOS — MESSAGE FLOW                      │
│                                                             │
│  Your Server                                                │
│      │                                                      │
│      │ FCM Token দিয়ে message send                         │
│      ▼                                                      │
│  FCM Servers (Google)                                       │
│      │                                                      │
│      │ FCM internally APNs Token খোঁজে                    │
│      ▼                                                      │
│  Apple APNs Servers                                         │
│      │                                                      │
│      │ APNs Token দিয়ে iOS device-কে push                  │
│      ▼                                                      │
│  iOS Device                                                 │
│      │                                                      │
│      ├─ App Background/Killed:                              │
│      │    notification{} → OS দেখায়                        │
│      │    data{} → App launch হলে পাবে                      │
│      │                                                      │
│      └─ App Foreground:                                     │
│           App-এর didReceiveRemoteNotification callback      │
└─────────────────────────────────────────────────────────────┘
```

### iOS-এ FCM Token vs APNs Token

```
FCM Token:
  তোমার server → FCM-এর সাথে কথা বলার identifier
  Flutter Firebase SDK এটি দেয়
  Format: দীর্ঘ alphanumeric string

APNs Token:
  FCM → APNs-এর সাথে কথা বলার identifier
  iOS OS এটি দেয়
  Flutter Firebase SDK internally APNs token নিয়ে
  FCM-এ register করে
  তোমাকে APNs token সরাসরি handle করতে হয় না
```

---

# Part 4 — Flutter Context

---

## [↑ TOC](#-table-of-contents)

## 4.1 Flutter Notification Stack Overview

Flutter-এ notification এর জন্য একাধিক package আছে। এদের সম্পর্ক বোঝা জরুরি।

```
┌─────────────────────────────────────────────────────────────┐
│              FLUTTER NOTIFICATION STACK                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │          firebase_messaging                         │   │
│  │  FCM integration — remote push notification        │   │
│  │  Android + iOS উভয়েই কাজ করে                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                           +                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │        flutter_local_notifications                  │   │
│  │  Local + Scheduled notification                    │   │
│  │  Foreground-এ push notification display করতে      │   │
│  │  Appointment reminder schedule করতে               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Background Task:                                           │
│  ┌──────────────────┐   ┌──────────────────────────────┐   │
│  │  workmanager     │   │  flutter_background_service  │   │
│  │  Scheduled,      │   │  Persistent background       │   │
│  │  deferred tasks  │   │  service (like Android       │   │
│  │  Android only    │   │  Foreground Service)         │   │
│  └──────────────────┘   └──────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## [↑ TOC](#-table-of-contents)

## 4.2 firebase_messaging Package — Complete Guide

### Setup

```yaml
# pubspec.yaml
dependencies:
  firebase_messaging: ^14.9.0
  firebase_core: ^2.27.0
```

### Initialization

```dart
// main.dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  // Background message handler — TOP LEVEL FUNCTION (class-এর বাইরে!)
  // এটি isolate-এ চলে, তাই top-level হতে হবে।
  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

  runApp(MyApp());
}

// ⚠️ IMPORTANT: এটি অবশ্যই top-level function হতে হবে
// class method বা lambda হলে কাজ করবে না
@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  // Background-এ message handle করো
  print('Background message: ${message.messageId}');

  // Local notification দেখাও (firebase_messaging background-এ UI দেখায় না)
  await _showLocalNotification(message);
}
```

### Permission Request

```dart
class NotificationService {
  final FirebaseMessaging _messaging = FirebaseMessaging.instance;

  Future<void> requestPermission() async {
    // iOS-এ dialog দেখায়, Android 13+ এও দেখায়
    NotificationSettings settings = await _messaging.requestPermission(
      alert: true,
      announcement: false,
      badge: true,
      carPlay: false,
      criticalAlert: false,  // Apple approval লাগে
      provisional: false,    // iOS-এ quiet delivery
      sound: true,
    );

    if (settings.authorizationStatus == AuthorizationStatus.authorized) {
      print('User granted permission');
    } else if (settings.authorizationStatus == AuthorizationStatus.provisional) {
      print('User granted provisional permission');
    } else {
      print('User denied permission');
      // User-কে settings-এ যেতে বলো
    }
  }
}
```

### Token Management

```dart
class TokenService {
  final FirebaseMessaging _messaging = FirebaseMessaging.instance;

  Future<void> initToken() async {
    // Current token নাও
    String? token = await _messaging.getToken();
    if (token != null) {
      await _saveTokenToServer(token);
    }

    // Token refresh হলে update করো (CRITICAL!)
    _messaging.onTokenRefresh.listen((newToken) async {
      await _saveTokenToServer(newToken);
    });
  }

  Future<void> _saveTokenToServer(String token) async {
    // তোমার Laravel/Node.js API-তে save করো
    await ApiService.updateFCMToken(
      userId: AuthService.currentUserId,
      token: token,
      platform: Platform.isAndroid ? 'android' : 'ios',
    );
  }
}
```

### Three Handlers — সবচেয়ে গুরুত্বপূর্ণ অংশ

```dart
class FCMHandlerService {
  void initHandlers() {
    // Handler 1: App FOREGROUND-এ থাকলে
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      print('Foreground message received');
      // FCM background-এ notification দেখায় না
      // আমাদের নিজে local notification দেখাতে হবে
      _showLocalNotification(message);
      // অথবা in-app dialog/banner দেখাও
    });

    // Handler 2: App BACKGROUND-এ, notification tap করলে
    FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
      print('Background notification tapped');
      // Deep link handle করো
      _handleNavigation(message.data);
    });

    // Handler 3: App TERMINATED থেকে notification tap করে খুললে
    _checkInitialMessage();
  }

  Future<void> _checkInitialMessage() async {
    RemoteMessage? initialMessage =
        await FirebaseMessaging.instance.getInitialMessage();
    if (initialMessage != null) {
      print('App opened from terminated via notification');
      _handleNavigation(initialMessage.data);
    }
  }

  void _handleNavigation(Map<String, dynamic> data) {
    // data থেকে deep link বের করো
    final action = data['action'];
    final appointmentId = data['appointment_id'];

    switch (action) {
      case 'view_appointment':
        NavigationService.navigateTo('/appointment/$appointmentId');
        break;
      case 'start_video_call':
        NavigationService.navigateTo('/video-call/$appointmentId');
        break;
      case 'view_prescription':
        NavigationService.navigateTo('/prescription/${data['prescription_id']}');
        break;
    }
  }
}
```

---

## [↑ TOC](#-table-of-contents)

## 4.3 flutter_local_notifications — Deep Dive

এই package দিয়ে:
1. Foreground-এ push notification দেখানো যায়
2. Appointment reminder schedule করা যায়
3. Upload progress notification দেখানো যায়

### Setup

```yaml
dependencies:
  flutter_local_notifications: ^17.2.2
  timezone: ^0.9.4  # Scheduled notification-এর জন্য
```

### Complete Initialization

```dart
class LocalNotificationService {
  static final FlutterLocalNotificationsPlugin _plugin =
      FlutterLocalNotificationsPlugin();

  static Future<void> init() async {
    // Timezone initialize করো
    tz.initializeTimeZones();
    tz.setLocalLocation(tz.getLocation('Asia/Dhaka'));

    // Android settings
    const AndroidInitializationSettings androidSettings =
        AndroidInitializationSettings('@mipmap/ic_launcher');

    // iOS settings
    const DarwinInitializationSettings iosSettings =
        DarwinInitializationSettings(
      requestAlertPermission: true,
      requestBadgePermission: true,
      requestSoundPermission: true,
      // Notification tap callback (foreground)
      onDidReceiveLocalNotification: _onDidReceiveLocalNotification,
    );

    const InitializationSettings initSettings = InitializationSettings(
      android: androidSettings,
      iOS: iosSettings,
    );

    await _plugin.initialize(
      initSettings,
      onDidReceiveNotificationResponse: _onNotificationTapped,
      onDidReceiveBackgroundNotificationResponse: _onBackgroundNotificationTapped,
    );

    // Android Notification Channels তৈরি করো
    await _createAndroidChannels();
  }

  static Future<void> _createAndroidChannels() async {
    final android = _plugin
        .resolvePlatformSpecificImplementation<
            AndroidFlutterLocalNotificationsPlugin>();

    // Video Call Channel
    await android?.createNotificationChannel(
      const AndroidNotificationChannel(
        'video_call',
        'Video Consultation',
        description: 'Incoming video consultation calls',
        importance: Importance.max,
        playSound: true,
        enableVibration: true,
      ),
    );

    // Appointment Channel
    await android?.createNotificationChannel(
      const AndroidNotificationChannel(
        'appointment',
        'Appointment Updates',
        description: 'Appointment confirmations and reminders',
        importance: Importance.high,
        playSound: true,
      ),
    );

    // Upload Progress Channel
    await android?.createNotificationChannel(
      const AndroidNotificationChannel(
        'document_upload',
        'Document Upload',
        description: 'Document upload progress',
        importance: Importance.low,
        playSound: false,
        enableVibration: false,
      ),
    );
  }
}
```

### Appointment Confirmation Notification

```dart
// Push notification আসলে foreground-এ এটি দিয়ে দেখাও
static Future<void> showAppointmentNotification({
  required int id,
  required String title,
  required String body,
  required Map<String, dynamic> payload,
}) async {
  await _plugin.show(
    id,
    title,
    body,
    NotificationDetails(
      android: AndroidNotificationDetails(
        'appointment',
        'Appointment Updates',
        channelDescription: 'Appointment confirmations',
        importance: Importance.high,
        priority: Priority.high,
        icon: '@drawable/ic_notification',
        color: const Color(0xFF2196F3),
        // Action buttons
        actions: [
          AndroidNotificationAction(
            'view',
            'View Details',
            showsUserInterface: true,
          ),
          AndroidNotificationAction(
            'dismiss',
            'Dismiss',
            cancelNotification: true,
          ),
        ],
      ),
      iOS: DarwinNotificationDetails(
        categoryIdentifier: 'APPOINTMENT',
        threadIdentifier: 'appointments',
      ),
    ),
    payload: jsonEncode(payload),
  );
}
```

### Appointment Reminder — Scheduled Notification

```dart
// Doctor/Patient উভয়ের জন্য reminder set করা
static Future<void> scheduleAppointmentReminder({
  required int notificationId,
  required String doctorName,
  required DateTime appointmentTime,
}) async {
  // Appointment-এর 1 ঘণ্টা আগে reminder
  final reminderTime = appointmentTime.subtract(const Duration(hours: 1));

  // এখনকার পরে হলেই schedule করো
  if (reminderTime.isAfter(DateTime.now())) {
    await _plugin.zonedSchedule(
      notificationId,
      'Appointment Reminder',
      'Your consultation with $doctorName starts in 1 hour',
      tz.TZDateTime.from(reminderTime, tz.local),
      NotificationDetails(
        android: AndroidNotificationDetails(
          'appointment',
          'Appointment Updates',
          importance: Importance.high,
          priority: Priority.high,
        ),
        iOS: const DarwinNotificationDetails(
          categoryIdentifier: 'APPOINTMENT_REMINDER',
        ),
      ),
      androidScheduleMode: AndroidScheduleMode.exactAllowWhileIdle,
      uiLocalNotificationDateInterpretation:
          UILocalNotificationDateInterpretation.absoluteTime,
      payload: jsonEncode({
        'action': 'view_appointment',
        'doctor_name': doctorName,
        'appointment_time': appointmentTime.toIso8601String(),
      }),
    );
  }
}
```

### Upload Progress Notification

```dart
static Future<void> showUploadProgress({
  required int notificationId,
  required String fileName,
  required int progressPercent,
  required int uploadedBytes,
  required int totalBytes,
}) async {
  await _plugin.show(
    notificationId,
    'Uploading $fileName',
    '${_formatBytes(uploadedBytes)} / ${_formatBytes(totalBytes)}',
    NotificationDetails(
      android: AndroidNotificationDetails(
        'document_upload',
        'Document Upload',
        channelDescription: 'Upload progress',
        importance: Importance.low,
        priority: Priority.low,
        ongoing: true,          // Swipe করে dismiss করা যাবে না
        showProgress: true,
        maxProgress: 100,
        progress: progressPercent,
        onlyAlertOnce: true,    // Sound শুধু প্রথমবার
      ),
    ),
  );
}

static String _formatBytes(int bytes) {
  if (bytes < 1024) return '$bytes B';
  if (bytes < 1024 * 1024) return '${(bytes / 1024).toStringAsFixed(1)} KB';
  return '${(bytes / (1024 * 1024)).toStringAsFixed(1)} MB';
}

static Future<void> showUploadComplete({
  required int notificationId,
  required String fileName,
}) async {
  await _plugin.show(
    notificationId,
    'Upload Complete ✅',
    '$fileName has been uploaded successfully',
    NotificationDetails(
      android: AndroidNotificationDetails(
        'document_upload',
        'Document Upload',
        importance: Importance.default_,
        ongoing: false,    // এখন dismiss করা যাবে
      ),
    ),
  );
}
```

---

## [↑ TOC](#-table-of-contents)

## 4.4 Flutter Isolate — Background কাজের ভিত্তি

Flutter-এ background task বোঝতে হলে **Isolate** বুঝতে হবে।

### Isolate কী?

```
প্রতিটি Dart Isolate নিজেই single-threaded (একটি event loop)।
কিন্তু একসাথে একাধিক Isolate চলতে পারে — shared memory নেই।

প্রতিটি Isolate:
  ✅ নিজের memory আছে
  ✅ নিজের event loop আছে
  ❌ অন্য isolate-এর memory সরাসরি access করতে পারে না
  ✅ Message passing (SendPort/ReceivePort) দিয়ে communicate করে

Main Isolate:
  UI render করে
  User interaction handle করে
  এখানে heavy কাজ করলে UI freeze হয়

Background Isolate:
  Heavy computation / file processing
  Network calls
  UI access করতে পারে না
```

### Isolate Communication

```
Main Isolate                    Background Isolate
     │                               │
     │──── SendPort দাও ────────────▶│
     │                               │ কাজ করো
     │◀─── Result পাঠাও ─────────────│
     │                               │
```

### Flutter Background-এ Isolate

```dart
// FCM Background Handler একটি আলাদা Isolate-এ চলে
@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  // ⚠️ এটি Main Isolate নয়!
  // ⚠️ এখানে Flutter widget/UI access করা যাবে না
  // ✅ Firebase initialize করতে হবে আবার
  // ✅ SharedPreferences/local DB access করা যাবে
  // ✅ HTTP request করা যাবে

  await Firebase.initializeApp(...);

  // Database-এ save করো
  await LocalDatabase.saveNotification(message);

  // Local notification দেখাও
  await LocalNotificationService.showFromRemoteMessage(message);
}
```

---

## [↑ TOC](#-table-of-contents)

## 4.5 flutter_background_service — Persistent Background

এই package Android Foreground Service এবং iOS Background Task দিয়ে একটি **persistent background service** তৈরি করে।

### কখন ব্যবহার করবে?

```
Use Case:
  ✅ Real-time appointment status check
  ✅ Video call state monitor
  ✅ Large file upload with progress
  ✅ WebSocket/long-polling connection maintain

কখন করবে না:
  ❌ Simple one-time task → WorkManager/BGTaskScheduler ভালো
  ❌ Scheduled reminder → flutter_local_notifications ভালো
```

### Setup

```yaml
dependencies:
  flutter_background_service: ^5.0.10
  flutter_background_service_android: ^6.2.3
```

### Initialization

```dart
Future<void> initBackgroundService() async {
  final service = FlutterBackgroundService();

  await service.configure(
    androidConfiguration: AndroidConfiguration(
      onStart: onServiceStart,           // Background-এ চলার function
      autoStart: true,                   // App open হলে auto start
      isForegroundMode: true,            // Foreground Service হিসেবে চলবে
      notificationChannelId: 'document_upload',
      initialNotificationTitle: 'Telemedicine',
      initialNotificationContent: 'Service running',
      foregroundServiceNotificationId: 888,
    ),
    iosConfiguration: IosConfiguration(
      autoStart: true,
      onForeground: onServiceStart,
      onBackground: onIosBackground,
    ),
  );
}

// Top-level function (Isolate-এ চলে)
@pragma('vm:entry-point')
void onServiceStart(ServiceInstance service) async {
  DartPluginRegistrant.ensureInitialized();

  // Android-এ foreground notification update করো
  if (service is AndroidServiceInstance) {
    service.on('setForeground').listen((event) {
      service.setForegroundNotificationInfo(
        title: 'Uploading Documents',
        content: 'Upload in progress...',
      );
    });
  }

  // Main app থেকে message শোনো
  service.on('startUpload').listen((event) async {
    final filePath = event!['filePath'] as String;
    await _performFileUpload(filePath, service);
  });

  service.on('stopService').listen((event) {
    service.stopSelf();
  });
}

@pragma('vm:entry-point')
Future<bool> onIosBackground(ServiceInstance service) async {
  WidgetsFlutterBinding.ensureInitialized();
  DartPluginRegistrant.ensureInitialized();
  return true;
}
```

---

## [↑ TOC](#-table-of-contents)

## 4.6 workmanager Package — Scheduled Tasks

**workmanager** package Android WorkManager এবং iOS BGTaskScheduler wrap করে।

### Setup

```yaml
dependencies:
  workmanager: ^0.5.2
```

### Initialization

```dart
// main.dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Workmanager initialize করো
  await Workmanager().initialize(
    callbackDispatcher,   // Top-level function
    isInDebugMode: false, // Production-এ false
  );

  runApp(MyApp());
}

// ⚠️ Top-level function — class-এর বাইরে
@pragma('vm:entry-point')
void callbackDispatcher() {
  Workmanager().executeTask((taskName, inputData) async {
    switch (taskName) {
      case 'syncAppointments':
        await _syncAppointments(inputData);
        break;
      case 'uploadDocument':
        await _uploadDocument(inputData);
        break;
      case 'refreshToken':
        await _refreshFCMToken();
        break;
    }
    return Future.value(true); // Success
    // return Future.value(false); // Retry
  });
}
```

### Task Register করা

```dart
class BackgroundTaskService {

  // One-time task: Token sync
  static Future<void> scheduleTokenSync() async {
    await Workmanager().registerOneOffTask(
      'tokenSync_${DateTime.now().millisecondsSinceEpoch}',
      'syncFCMToken',
      constraints: Constraints(
        networkType: NetworkType.connected,
        requiresBatteryNotLow: false,
      ),
      backoffPolicy: BackoffPolicy.exponential,
      backoffPolicyDelay: const Duration(seconds: 10),
    );
  }

  // Periodic task: Appointment sync (minimum 15 minutes)
  static Future<void> schedulePeriodicSync() async {
    await Workmanager().registerPeriodicTask(
      'appointmentSync',
      'syncAppointments',
      frequency: const Duration(hours: 1),
      constraints: Constraints(
        networkType: NetworkType.connected,
        requiresBatteryNotLow: true,
      ),
      existingWorkPolicy: ExistingWorkPolicy.replace,
    );
  }

  // Document upload
  static Future<void> scheduleDocumentUpload({
    required String filePath,
    required String documentType,
    required String patientId,
  }) async {
    await Workmanager().registerOneOffTask(
      'documentUpload_${DateTime.now().millisecondsSinceEpoch}',
      'uploadDocument',
      inputData: {
        'filePath': filePath,
        'documentType': documentType,
        'patientId': patientId,
      },
      constraints: Constraints(
        networkType: NetworkType.connected,
        requiresStorageNotLow: true,
      ),
      backoffPolicy: BackoffPolicy.exponential,
      backoffPolicyDelay: const Duration(seconds: 30),
    );
  }
}
```

---

## [↑ TOC](#-table-of-contents)

## 4.7 Large Document Upload — Production Implementation

এটি সবচেয়ে complex part। Telemedicine-এ patient MRI, X-Ray, Lab Report upload করে — এগুলো বড় file।

### Architecture Overview

```mermaid
flowchart TD
    A[User selects file] --> B[File size check]
    B -->|< 5MB| C[Direct Upload]
    B -->|>= 5MB| D[Chunked Upload]

    C --> E[Upload Service]
    D --> F[Split into chunks\n5MB each]
    F --> G[Get upload session\nfrom server]
    G --> H[Upload chunk 1]
    H --> I{Success?}
    I -->|Yes| J[Upload chunk 2...]
    I -->|No| K[Retry chunk 1\nmax 3 times]
    K --> H
    J --> L[All chunks done?]
    L -->|Yes| M[Complete upload\nserver reassemble]
    L -->|No| J
    M --> N[Send notification\nUpload Complete]
    E --> N
```

### Complete Upload Implementation

```dart
class DocumentUploadService {
  static const int _chunkSize = 5 * 1024 * 1024; // 5MB
  static const int _maxRetries = 3;

  // Main upload function
  Future<void> uploadDocument({
    required String filePath,
    required String documentType,
    required String patientId,
    required Function(double progress) onProgress,
    required Function() onComplete,
    required Function(String error) onError,
  }) async {
    final file = File(filePath);
    final fileName = path.basename(filePath);
    final fileSize = await file.length();

    // Progress notification ID (file-specific)
    final notificationId = fileName.hashCode;

    try {
      if (fileSize <= _chunkSize) {
        // Direct upload
        await _directUpload(
          file: file,
          fileName: fileName,
          documentType: documentType,
          patientId: patientId,
          notificationId: notificationId,
          onProgress: onProgress,
        );
      } else {
        // Chunked upload
        await _chunkedUpload(
          file: file,
          fileName: fileName,
          fileSize: fileSize,
          documentType: documentType,
          patientId: patientId,
          notificationId: notificationId,
          onProgress: onProgress,
        );
      }

      // Success
      await LocalNotificationService.showUploadComplete(
        notificationId: notificationId,
        fileName: fileName,
      );
      onComplete();
    } catch (e) {
      await LocalNotificationService.showUploadFailed(
        notificationId: notificationId,
        fileName: fileName,
        error: e.toString(),
      );
      onError(e.toString());
    }
  }

  // Chunked Upload
  Future<void> _chunkedUpload({
    required File file,
    required String fileName,
    required int fileSize,
    required String documentType,
    required String patientId,
    required int notificationId,
    required Function(double) onProgress,
  }) async {
    // Step 1: Server-এ upload session তৈরি করো
    final sessionId = await _initUploadSession(
      fileName: fileName,
      fileSize: fileSize,
      documentType: documentType,
      patientId: patientId,
    );

    // Step 2: Chunks calculate করো
    final totalChunks = (fileSize / _chunkSize).ceil();
    int uploadedBytes = 0;

    // Step 3: প্রতিটি chunk upload করো
    for (int chunkIndex = 0; chunkIndex < totalChunks; chunkIndex++) {
      final start = chunkIndex * _chunkSize;
      final end = (start + _chunkSize > fileSize) ? fileSize : start + _chunkSize;
      final chunkBytes = await _readFileChunk(file, start, end);

      // Retry logic
      bool chunkUploaded = false;
      int attempts = 0;

      while (!chunkUploaded && attempts < _maxRetries) {
        try {
          await _uploadChunk(
            sessionId: sessionId,
            chunkIndex: chunkIndex,
            totalChunks: totalChunks,
            chunkData: chunkBytes,
          );
          chunkUploaded = true;
        } catch (e) {
          attempts++;
          if (attempts >= _maxRetries) rethrow;

          // Exponential backoff
          await Future.delayed(
            Duration(seconds: (10 * attempts)),
          );
        }
      }

      uploadedBytes += chunkBytes.length;
      final progress = uploadedBytes / fileSize;

      // Progress update
      onProgress(progress);

      // Notification update
      await LocalNotificationService.showUploadProgress(
        notificationId: notificationId,
        fileName: fileName,
        progressPercent: (progress * 100).round(),
        uploadedBytes: uploadedBytes,
        totalBytes: fileSize,
      );
    }

    // Step 4: Server-কে complete করতে বলো
    await _completeUploadSession(sessionId);
  }

  Future<Uint8List> _readFileChunk(File file, int start, int end) async {
    final randomAccess = await file.open();
    await randomAccess.setPosition(start);
    final bytes = await randomAccess.read(end - start);
    await randomAccess.close();
    return bytes;
  }

  Future<String> _initUploadSession({
    required String fileName,
    required int fileSize,
    required String documentType,
    required String patientId,
  }) async {
    final response = await ApiService.post('/documents/upload/init', {
      'file_name': fileName,
      'file_size': fileSize,
      'document_type': documentType,
      'patient_id': patientId,
    });
    return response['session_id'];
  }

  Future<void> _uploadChunk({
    required String sessionId,
    required int chunkIndex,
    required int totalChunks,
    required Uint8List chunkData,
  }) async {
    await ApiService.uploadChunk(
      sessionId: sessionId,
      chunkIndex: chunkIndex,
      totalChunks: totalChunks,
      data: chunkData,
    );
  }

  Future<void> _completeUploadSession(String sessionId) async {
    await ApiService.post('/documents/upload/complete', {
      'session_id': sessionId,
    });
  }
}
```

### Background Upload — WorkManager Integration

```dart
// Background-এ upload করার জন্য WorkManager ব্যবহার
@pragma('vm:entry-point')
void callbackDispatcher() {
  Workmanager().executeTask((taskName, inputData) async {
    if (taskName == 'uploadDocument') {
      final filePath = inputData!['filePath'] as String;
      final documentType = inputData['documentType'] as String;
      final patientId = inputData['patientId'] as String;

      // Firebase initialize (background isolate-এ)
      await Firebase.initializeApp(
        options: DefaultFirebaseOptions.currentPlatform,
      );

      final uploadService = DocumentUploadService();
      bool success = false;

      await uploadService.uploadDocument(
        filePath: filePath,
        documentType: documentType,
        patientId: patientId,
        onProgress: (progress) {
          // Background-এ progress notification update
        },
        onComplete: () { success = true; },
        onError: (error) { success = false; },
      );

      return Future.value(success); // false হলে WorkManager retry করবে
    }
    return Future.value(true);
  });
}
```

---

## [↑ TOC](#-table-of-contents)

## 4.8 Telemedicine Use Case — Appointment Notification Flow

### Complete Flow Diagram

```mermaid
sequenceDiagram
    participant Patient as Patient App
    participant PatientFCM as Patient FCM Token
    participant Server as Laravel Backend
    participant DoctorFCM as Doctor FCM Token
    participant Doctor as Doctor App
    participant FCMServer as FCM Server

    Note over Patient,Doctor: Patient Books Appointment

    Patient->>Server: POST /appointments\n{doctor_id, time, type}
    Server->>Server: Create appointment\nstatus: pending

    Server->>FCMServer: Send to Doctor\n{title: "New Appointment Request"}
    FCMServer->>DoctorFCM: Deliver
    Doctor-->>Doctor: Show notification\n"New appointment request"

    Note over Patient,Doctor: Doctor Confirms Appointment

    Doctor->>Server: PUT /appointments/{id}/confirm
    Server->>Server: Update status: confirmed

    Server->>FCMServer: Send to Patient\n{title: "Appointment Confirmed!"}
    FCMServer->>PatientFCM: Deliver
    Patient-->>Patient: Show notification\n"Dr. Rahman confirmed"

    Note over Patient,Doctor: 1 Hour Before Appointment

    Patient-->>Patient: Local notification fires\n(Scheduled reminder)\n"Your appointment in 1 hour"
    Doctor-->>Doctor: Local notification fires\n"Consultation in 1 hour"

    Note over Patient,Doctor: Doctor Starts Video Call

    Doctor->>Server: PUT /appointments/{id}/start-call
    Server->>FCMServer: Send high-priority to Patient\n{action: "start_video_call"}
    FCMServer->>PatientFCM: High Priority Deliver
    Patient-->>Patient: Incoming call notification\n[Join] [Decline]
```

### Server-side Notification Payload (Laravel)

```php
// Laravel — AppointmentController.php
public function confirm(Request $request, Appointment $appointment)
{
    $appointment->update(['status' => 'confirmed']);

    // Patient-কে notification পাঠাও
    $patientToken = $appointment->patient->fcm_token;

    $this->fcmService->send(
        token: $patientToken,
        title: 'Appointment Confirmed! ✅',
        body: "Dr. {$appointment->doctor->name} confirmed your appointment",
        data: [
            'action'         => 'view_appointment',
            'appointment_id' => (string) $appointment->id,
            'doctor_name'    => $appointment->doctor->name,
            'appointment_time' => $appointment->scheduled_at->toISOString(),
            'type'           => 'appointment_confirmation',
        ],
        priority: 'high',
        channelId: 'appointment',
    );

    return response()->json(['message' => 'Confirmed']);
}
```

### Flutter-এ Notification Tap Handling

```dart
// Notification tap করলে সঠিক screen-এ নিয়ে যাওয়া
class NotificationNavigator {
  static void handleNotificationData(Map<String, dynamic> data) {
    final action = data['action'] as String?;

    switch (action) {
      case 'view_appointment':
        final id = data['appointment_id'];
        Get.toNamed('/appointment/detail', arguments: {'id': id});
        break;

      case 'start_video_call':
        final id = data['appointment_id'];
        Get.toNamed('/video-call', arguments: {'appointment_id': id});
        break;

      case 'view_prescription':
        final id = data['prescription_id'];
        Get.toNamed('/prescription', arguments: {'id': id});
        break;

      case 'document_upload_complete':
        Get.toNamed('/documents');
        break;

      default:
        Get.toNamed('/home');
    }
  }
}
```

---

## [↑ TOC](#-table-of-contents)

## 4.9 Production Checklist

### ✅ Notification Production Checklist

```
ANDROID:
  □ Notification channels তৈরি করা (Android 8+)
  □ POST_NOTIFICATIONS permission request (Android 13+)
  □ FCM high priority সব critical notification-এ
  □ onTokenRefresh handle করা (token সবসময় fresh রাখা)
  □ Notification icon (সাদা, transparent background)
  □ Foreground handler → local notification দেখানো
  □ Background handler (top-level function)
  □ Terminated state handler (getInitialMessage)
  □ Deep link navigation সব notification-এ

iOS:
  □ APNs key Firebase Console-এ upload
  □ Info.plist-এ UIBackgroundModes
  □ Permission request with all options
  □ Notification categories (action buttons)
  □ APN/FCM token উভয় handle করা
  □ AppDelegate background URL session handler
```

### ✅ Background Task Production Checklist

```
FILE UPLOAD:
  □ Chunked upload (5MB chunks)
  □ Retry with exponential backoff (max 3)
  □ Progress notification (ongoing, non-dismissible)
  □ Resume capability (server-side session)
  □ Network change detection (pause/resume)
  □ Android: Foreground Service for large files
  □ iOS: Background URLSession

WORKMANAGER (Android):
  □ Network constraint
  □ Battery constraint
  □ Unique task name (avoid duplicate)
  □ Backoff policy
  □ Top-level callback function

iOS BACKGROUND:
  □ BGTaskScheduler registered tasks
  □ BGTaskScheduler.submit() in correct lifecycle
  □ Background URLSession for uploads

GENERAL:
  □ Background isolate-এ Firebase re-initialize
  □ Database access (background isolate-এ)
  □ Token refresh কাজ করছে কিনা test
  □ Low battery scenario test
  □ Airplane mode → WiFi scenario test
  □ App kill → notification tap → correct screen test
```

### ✅ Common Mistakes এবং Solutions

```
┌─────────────────────────────────────────────────────────────┐
│  MISTAKE 1:                                                 │
│  Background handler class method হিসেবে define করা         │
│                                                             │
│  FIX: Top-level function (@pragma('vm:entry-point'))        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  MISTAKE 2:                                                 │
│  Background isolate-এ Firebase initialize না করা           │
│                                                             │
│  FIX: Background handler-এ সবসময় Firebase.initializeApp() │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  MISTAKE 3:                                                 │
│  FCM token একবার save করে আর update না করা                 │
│                                                             │
│  FIX: onTokenRefresh listener সবসময় active রাখো           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  MISTAKE 4:                                                 │
│  Android 13+ এ POST_NOTIFICATIONS runtime permission        │
│  না চাওয়া                                                   │
│                                                             │
│  FIX: App start-এ permission check ও request করো           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  MISTAKE 5:                                                 │
│  iOS-এ APNs key Firebase-এ upload না করা                   │
│                                                             │
│  FIX: Firebase Console > Project Settings >                 │
│       Cloud Messaging > Apple app > Upload .p8 key          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  MISTAKE 6:                                                 │
│  Large file একবারে upload করার চেষ্টা করা                  │
│                                                             │
│  FIX: Chunked upload + resume session implement করো         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  MISTAKE 7:                                                 │
│  Android 14-তে foregroundServiceType declare না করা        │
│                                                             │
│  FIX: AndroidManifest.xml-এ                                 │
│       android:foregroundServiceType="dataSync" যোগ করো      │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary — এক নজরে সবকিছু

```
┌─────────────────────────────────────────────────────────────┐
│                    QUICK REFERENCE                          │
├───────────────────────┬─────────────────────────────────────┤
│  Task                 │  Solution                           │
├───────────────────────┼─────────────────────────────────────┤
│ Appointment Push      │ FCM (high priority) +               │
│ Notification          │ firebase_messaging                  │
├───────────────────────┼─────────────────────────────────────┤
│ Appointment Reminder  │ flutter_local_notifications         │
│ (1hr before)          │ zonedSchedule()                     │
├───────────────────────┼─────────────────────────────────────┤
│ Foreground Push       │ firebase_messaging onMessage +      │
│ Display               │ flutter_local_notifications show()  │
├───────────────────────┼─────────────────────────────────────┤
│ Large File Upload     │ Chunked Upload +                    │
│ (Background)          │ flutter_background_service /        │
│                       │ workmanager                         │
├───────────────────────┼─────────────────────────────────────┤
│ Upload Progress       │ flutter_local_notifications         │
│ Notification          │ showProgress: true, ongoing: true   │
├───────────────────────┼─────────────────────────────────────┤
│ Periodic Background   │ workmanager                         │
│ Sync                  │ registerPeriodicTask                │
├───────────────────────┼─────────────────────────────────────┤
│ Token Refresh         │ FCM onTokenRefresh →                │
│                       │ API update                          │
└───────────────────────┴─────────────────────────────────────┘
```

---

*এই গাইড Telemedicine Flutter App-এর Production-ready notification এবং background task implementation-এর জন্য তৈরি করা হয়েছে। প্রতিটি concept real-world use case-এর উপর ভিত্তি করে ব্যাখ্যা করা হয়েছে।*

*Last updated: April 2026*

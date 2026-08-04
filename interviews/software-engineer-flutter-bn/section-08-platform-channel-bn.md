# Section 8 — Platform Channels & Native Integration

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-08-platform-channel.md](../software-engineer-flutter/section-08-platform-channel.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code দিয়ে ধাপে ধাপে পুরো ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর তার কঠিনতা (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তরটা** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন — "আরও গভীরে যেতে পারবেন?" সহজ আর পরিষ্কার করে বলাটাই একটা senior skill — remote আর BD দুই ধরনের কোম্পানিতেই এটা একইভাবে কাজ করে।

---


## <a id="toc"></a>সূচিপত্র

**A. মূল কথা — channel জিনিসটা কী**
1. [Platform Channel কী আর কেন দরকার?](#q1) · *Very common*
2. [Channel handler কোন thread-এ চলে?](#q2) · *Common*

**B. তিন ধরনের channel**
3. [MethodChannel — native call করে result নেওয়া (Dart + Kotlin + Swift)](#q3) · *Very common*
4. [MethodChannel vs EventChannel vs BasicMessageChannel](#q4) · *Very common*
5. [EventChannel — native থেকে একটানা stream](#q5) · *Very common*
6. [BasicMessageChannel — যেকোনো ধরনের message](#q6) · *Common*

**C. Bridge পার হওয়া error, data ও type**
7. [Codec আর `PlatformException` — data পাঠানো ও error সামলানো](#q7) · *Common*

**D. Native-এর দিকে — FFI, plugin, add-to-app**
8. [Dart FFI vs Platform Channels](#q8) · *Common*
9. [Flutter plugin package লেখা](#q9) · *Common*
10. [Pigeon — type-safe channel](#q10) · *Very common*
11. [Add-to-app — native app-এর ভেতরে Flutter বসানো](#q11) · *Common*
12. [যে native SDK-র কোনো plugin নেই, সেটা integrate করা](#q12) · *Common*

**E. Platform-aware Flutter**
13. [Platform-adaptive UI (Material vs Cupertino)](#q13) · *Common*
14. [Permission দেখা ও চাওয়া](#q14) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

১৪টা প্রশ্ন একসাথে পড়ার দরকার নেই। এই পর্যায়গুলো একটার পর একটা শেষ করুন — প্রতিটা আগেরটার উপর দাঁড়ানো। একটা পর্যায় তখনই টিক দিন যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন।

**পর্যায় ১ — মূল ভিত্তি (এখান থেকে শুরু)।** এগুলো প্রায় প্রতিটা interview-তে আসে।
→ [Q1 Platform Channel কী](#q1) · [Q3 MethodChannel](#q3) · [Q4 তিন ধরনের channel](#q4) · [Q5 EventChannel](#q5)

**পর্যায় ২ — Error আর data।** Data আর ব্যর্থতা কীভাবে bridge পার হয়।
→ [Q7 Codec ও PlatformException](#q7) · [Q2 কোন thread](#q2) · [Q6 BasicMessageChannel](#q6)

**পর্যায় ৩ — আধুনিক tooling (আপনি আপ-টু-ডেট আছেন, সেটা দেখায়)।**
→ [Q10 Pigeon](#q10) · [Q9 Plugin package](#q9)

**পর্যায় ৪ — বাস্তব integration।** Senior-রা কাজে আসলে যা করেন।
→ [Q12 Native SDK integrate করা](#q12) · [Q11 Add-to-app](#q11) · [Q13 Adaptive UI](#q13) · [Q14 Permission](#q14)

**পর্যায় ৫ — গভীরতা ও senior signal (সবার শেষে)।** এগুলো শক্ত senior-দের বাকিদের থেকে আলাদা করে।
→ [Q8 FFI vs channel](#q8) · তারপর আবার পড়ুন [Q2 threading](#q2) আর [Cheat Sheet](#cheatsheet)।

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই সাতটা দেখে নিন:
[Q1](#q1) · [Q3](#q3) · [Q4](#q4) · [Q5](#q5) · [Q7](#q7) · [Q8](#q8) · [Q10](#q10), তারপর পড়ুন [Cheat Sheet](#cheatsheet)।

---

# A. মূল কথা — channel জিনিসটা কী

---

## <a id="q1"></a>1. Platform Channel কী আর কেন দরকার?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Platform Channel হলো আমার Dart code আর native code-এর মাঝে একটা নাম দেওয়া টেলিফোন লাইন (Android-এ Kotlin/Java, iOS-এ Swift/Objective-C)। Flutter নিজের screen নিজে আঁকে আর Dart চালায় নিজের engine-এ। তাই এটা camera, Bluetooth বা battery-র মতো native জিনিস সরাসরি ছুঁতে পারে না। Channel দিয়ে Dart native দিকে একটা message পাঠায়, native দিক কাজটা করে, আর উত্তর ফিরে আসে — পুরোটাই asynchronously।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Flutter-এর একটা bridge কেন দরকার।**
Flutter platform-এর সাধারণ UI button আর view ব্যবহার করে না। এটা নিজের engine দিয়ে প্রতিটা pixel নিজে আঁকে, আর আপনার logic সেই engine-এর ভেতরে Dart হিসেবে চলে। দুই platform-এ এক codebase-এর জন্য এটা দারুণ, কিন্তু এতে একটা দেয়াল তৈরি হয়: `BatteryManager` (Android) বা `UIDevice` (iOS) call করার কোনো built-in উপায় Dart-এ নেই। ওগুলো দেয়ালের native পাশে থাকে।

**ধাপ ২ — টেলিফোন লাইনের তুলনা।**
Platform Channel-কে ভাবুন একটা টেলিফোন লাইন হিসেবে, যার গায়ে নাম লেখা — যেমন `com.example.app/battery`। Dart ফোন তুলে একটা প্রশ্ন করে। Native দিক **একই নামের** ফোন ধরে আছে, প্রশ্নটা শোনে, আসল কাজটা করে, আর উত্তর দেয়। নাম না মিললে কেউ ফোন ধরবে না।

```
  Dart (Flutter)                        Native (Android / iOS)
 +------------------+                  +----------------------+
 |                  |   method name    |                      |
 |  invokeMethod()  | ---------------> |  onMethodCall()      |
 |                  |   + arguments    |  (Kotlin / Swift)    |
 |                  |                  |                      |
 |  await result    | <--------------- |  result.success()    |
 |                  |   return value   |                      |
 +------------------+                  +----------------------+
           ^                                     ^
           +--------- Platform Channel ----------+
                  (named, async, binary)
```

**ধাপ ৩ — তিন ধরনের channel।**
তিন ধরনের channel আছে, প্রতিটা আলাদা ধরনের কথা বলার জন্য:

- **MethodChannel** — এক প্রশ্ন, এক উত্তর (request/reply)। সবচেয়ে বেশি ব্যবহার করা। দেখুন [Q3](#q3)।
- **EventChannel** — native থেকে Dart-এ একটানা broadcast (যেমন sensor data)। দেখুন [Q5](#q5)।
- **BasicMessageChannel** — দুই দিকেই যেকোনো ধরনের message, "method"-এর ধারণা নেই। দেখুন [Q6](#q6)।

**ধাপ ৪ — এটা device-এর ভেতরেই আর asynchronous, কোনো network call নয়।**
এটা গুরুত্বপূর্ণ। Message internet দিয়ে যায় না। এটা app-এর ভেতরে Flutter engine-এর মধ্য দিয়ে যায়, ছোট binary হিসেবে encode হয়ে। আর প্রতিটা call asynchronous — আপনি `await` করেন — তাই native কাজ করার সময় UI কখনো জমে যায় না।

```dart
// Battery level দেখা — শুধু Dart দিয়ে এটা করার কোনো উপায় নেই
final channel = MethodChannel('com.example.app/battery');
final int level = await channel.invokeMethod('getBatteryLevel');
```

**ধাপ ৫ — সাধারণত কখন আপনি নিজে channel লেখেন না।**
বেশিরভাগ সাধারণ দরকারের (camera, location, shared preferences) জন্য pub.dev-এ আগে থেকেই plugin আছে। সেই plugin-গুলো ভেতরে Platform Channel-ই ব্যবহার করে। নিজে channel তখনই লেখেন, যখন কোনো plugin নেই, বা আপনি নিজের plugin বানাচ্ছেন।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা নিশ্চিত হতে চান আপনি Flutter-এর architecture-এর দেয়ালটা বোঝেন। আপনি যদি ভাবেন Flutter সরাসরি Android/iOS API call করতে পারে, তাহলে senior-এর জন্য সেটা একটা গোড়ার ভুল ধারণা।

**সাধারণ ভুল:** বলা যে Platform Channel synchronous, বা এগুলো HTTP ব্যবহার করে। এগুলো asynchronous আর device-এর ভেতরেই — engine-এর মধ্য দিয়ে binary message, কোনো network নেই।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Call-গুলো async হতেই হবে কেন?"* → Native কাজে সময় লাগতে পারে। আর UI মসৃণ রাখতে Dart-এর একটা thread খালি থাকতে হয়। Async screen-কে সাড়া দেওয়ার মতো রাখে।
- *"Native দিকে কী চলে?"* → আপনার register করা একটা handler (`setMethodCallHandler` / একটা `StreamHandler`), যেটা একই channel নামে শোনে।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q4 — তিন ধরনের channel](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Platform Channel handler কোন thread-এ চলে? ভারী native কাজ কীভাবে করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Default-ভাবে native channel handler চলে platform-এর main (UI) thread-এ। তাই আমি যদি ঠিক সেখানেই ভারী কাজ করি, তাহলে native UI জমে যায় আর Dart-এ উত্তর দেরিতে যায়। সমাধান হলো ভারী কাজটা native দিকে একটা background thread-এ সরানো, তারপর শুধু `result.success(...)` call করার জন্য main thread-এ ফিরে আসা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এখানে দুটো main thread কাজ করছে।**
দুটো গুরুত্বপূর্ণ thread আলাদা করে বোঝা দরকার:

- **Dart-এর thread** (UI isolate) — যেখানে আপনার `await invokeMethod(...)` থাকে। `await` এটাকে কখনোই block করে না।
- **Platform main thread** — যেখানে native handler (`onMethodCall` / `handle`) default-ভাবে চলে।

টেলিফোন লাইনের message আসে platform main thread-এ। ছোট কাজের জন্য এটা ঠিক আছে, কিন্তু ধীর কাজের জন্য বিপজ্জনক।

**ধাপ ২ — Default thread কেন আপনার ক্ষতি করতে পারে।**
আপনার native handler যদি main thread-এই একটা বিশাল file পড়ে বা ভারী decryption করে, তাহলে native UI rendering block হয়ে যায়। আর উত্তর Dart-এ ফিরতে অনেক সময় লাগে। Dart দিক জমে যায় না, কিন্তু user অপেক্ষা করে আর native animation আটকে আটকে চলে।

**ধাপ ৩ — Android-এ সমাধান (Kotlin): কাজ background thread-এ, উত্তর main-এ।**
ভারী কাজটা main thread-এর বাইরে করুন। তারপর `result.success(...)` call করার আগে result-টা main thread-এ ফেরত পাঠান। Platform channel-এর result callback অবশ্যই main thread-এ call করতে হবে।

```kotlin
import android.os.Handler
import android.os.Looper
import java.util.concurrent.Executors

private val executor = Executors.newSingleThreadExecutor()
private val mainHandler = Handler(Looper.getMainLooper())

override fun onMethodCall(call: MethodCall, result: MethodChannel.Result) {
    if (call.method == "processBigFile") {
        executor.execute {
            val output = doHeavyWork()                 // background thread-এ
            mainHandler.post { result.success(output) } // উত্তর দিতে আবার main-এ
        }
    } else {
        result.notImplemented()
    }
}
```

**ধাপ ৪ — iOS-এ সমাধান (Swift): GCD দিয়ে একই ধারণা।**
কাজের জন্য একটা background queue ব্যবহার করুন, তারপর `result` callback call করতে main queue-তে ফিরে আসুন।

```swift
func handle(_ call: FlutterMethodCall, result: @escaping FlutterResult) {
    if call.method == "processBigFile" {
        DispatchQueue.global(qos: .userInitiated).async {
            let output = self.doHeavyWork()       // background queue-তে
            DispatchQueue.main.async {
                result(output)                    // উত্তর দিতে আবার main-এ
            }
        }
    } else {
        result(FlutterMethodNotImplemented)
    }
}
```

**ধাপ ৫ — Dart দিকে ভারী কাজ কোথায় রাখবেন।**
ভারী কাজটা যদি পুরোপুরি Dart-এর হয় (যেমন native দিক থেকে আসা বিশাল JSON parse করা), সেটাও UI isolate-এ করবেন না। `Isolate.run(...)` বা `compute(...)` দিয়ে একটা isolate-এ সরান। অর্থাৎ ভারী CPU কাজ সবসময় সেই main thread-এর বাইরে ঠেলে দিন, যেটা নাহলে block হতো।

**Interviewer কেন জিজ্ঞেস করে:** Threading-এই আসল native bug-গুলো লুকিয়ে থাকে। একজন senior-কে জানতে হবে channel handler default-ভাবে main thread-এ চলে, আর `result` callback অবশ্যই main thread-এ ফিরে আসতে হবে।

**সাধারণ ভুল:** Native handler-এর ভেতরে সরাসরি ভারী কাজ করা, বা background thread থেকে `result.success(...)` call করা। Result callback অবশ্যই platform main thread-এ call করতে হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Dart দিকে `await` কি UI block করে?"* → না। `await` শুধু ওই একটা function থামায়; Dart-এর UI চলতেই থাকে।
- *"যদি কোনো native SDK নিজের background thread-এ আপনাকে callback দেয়?"* → সেই result ধরে রাখুন, আর `result.success(...)` call করার আগে main thread-এ re-dispatch করুন।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q12 — native SDK integrate করা](#q12)

[↑ উপরে ফিরুন](#toc)

---

# B. তিন ধরনের channel

---

## <a id="q3"></a>3. MethodChannel কীভাবে কাজ করে? Native code call করে result ফেরত আনা দেখান (Dart, Kotlin, Swift)।

> Very common · Medium — channel নিয়ে সবচেয়ে বেশি আসা প্রশ্ন। · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"MethodChannel হলো একটা request/reply call। Dart একটা method name আর optional argument দিয়ে `invokeMethod` call করে। Native দিকে একটা handler register করা থাকে, যেটা method name মিলিয়ে কাজটা করে। তারপর `result.success(value)` বা `result.error(...)` দিয়ে উত্তর দেয়। দুই দিকেই channel name string হুবহু এক হতে হবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — request/reply ধারণাটা।**
MethodChannel অনেকটা help desk-এ call করার মতো: আপনি কী চান বলেন ("getBatteryLevel"), দরকার হলে বিস্তারিত দেন (arguments), আর তাঁরা একটা উত্তর দেন। এক call, এক reply।

```
Dart                     Engine                    Native
 |                         |                         |
 | invokeMethod("getX")    |                         |
 | ----------------------> | ----------------------> |
 |                         |  binary message         |
 |                         |                         | runs native code
 |                         |                         |
 |          result         | <---------------------- |
 | <---------------------- |  result.success(val)    |
 |                         |                         |
```

**ধাপ ২ — Dart দিক: call করা আর error handle করা।**
Call-টা `try/catch` দিয়ে মুড়ে দিন `PlatformException`-এর জন্য। কারণ native দিক error দিয়েও উত্তর দিতে পারে।

```dart
import 'package:flutter/services.dart';

class BatteryService {
  static const _channel = MethodChannel('com.example.app/battery');

  Future<int> getBatteryLevel() async {
    try {
      final int level = await _channel.invokeMethod('getBatteryLevel');
      return level;
    } on PlatformException catch (e) {
      throw Exception('Failed to get battery level: ${e.message}');
    }
  }
}
```

**ধাপ ৩ — Android দিক (Kotlin): একই নামে handler register করুন।**
Register করুন `configureFlutterEngine`-এর ভেতরে। `call.method` মিলিয়ে দেখুন, `result.success(...)` দিয়ে উত্তর দিন। আর অজানা method-এর জন্য সবসময় `result.notImplemented()` রাখুন।

```kotlin
package com.example.app

import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import android.os.BatteryManager
import android.content.Context

class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.example.app/battery"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
            .setMethodCallHandler { call, result ->
                when (call.method) {
                    "getBatteryLevel" -> {
                        val bm = getSystemService(Context.BATTERY_SERVICE) as BatteryManager
                        val level = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
                        if (level != -1) {
                            result.success(level)
                        } else {
                            result.error("UNAVAILABLE", "Battery level not available", null)
                        }
                    }
                    else -> result.notImplemented()
                }
            }
    }
}
```

**ধাপ ৪ — iOS দিক (Swift): `AppDelegate`-এ একই handler।**
উত্তর দিন `result(value)` দিয়ে, error দিন `FlutterError(...)` দিয়ে, আর অজানা method-এর জন্য `FlutterMethodNotImplemented`।

```swift
import Flutter
import UIKit

@main
@objc class AppDelegate: FlutterAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        let controller = window?.rootViewController as! FlutterViewController
        let channel = FlutterMethodChannel(
            name: "com.example.app/battery",
            binaryMessenger: controller.binaryMessenger
        )

        channel.setMethodCallHandler { (call: FlutterMethodCall, result: @escaping FlutterResult) in
            switch call.method {
            case "getBatteryLevel":
                UIDevice.current.isBatteryMonitoringEnabled = true
                let level = Int(UIDevice.current.batteryLevel * 100)
                if level >= 0 {
                    result(level)
                } else {
                    result(FlutterError(code: "UNAVAILABLE",
                                        message: "Battery level not available",
                                        details: nil))
                }
            default:
                result(FlutterMethodNotImplemented)
            }
        }

        GeneratedPluginRegistrant.register(with: self)
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }
}
```

**ধাপ ৫ — Argument পাঠানো।**
Dart থেকে একটা `Map` পাঠান। Native দিকে key দিয়ে সেটা পড়ুন।

```dart
await _channel.invokeMethod('setBrightness', {'value': 0.8});
```

```kotlin
"setBrightness" -> {
    val value = call.argument<Double>("value") ?: 1.0
    // value ব্যবহার করুন...
    result.success(null)
}
```

**Interviewer কেন জিজ্ঞেস করে:** এটা channel-এর সবচেয়ে গোড়ার দক্ষতা। তাঁরা দেখেন আপনি তিনটা layer ঠিকভাবে জোড়া লাগাতে পারেন কি না, error handle করেন কি না, আর channel name হুবহু মেলাতে হয় সেটা মনে রাখেন কি না।

**সাধারণ ভুল:** অজানা method-এর জন্য `notImplemented()` ভুলে যাওয়া, দুই দিকে আলাদা channel name ব্যবহার করা, অথবা Dart call-টা `PlatformException`-এর জন্য `try/catch` দিয়ে না মোড়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Argument কী কী type হতে পারে?"* → শুধু codec যা support করে: `null`, `bool`, `int`, `double`, `String`, `Uint8List`, `List`, `Map`। দেখুন [Q7](#q7)।
- *"Handler কোন thread-এ চলে?"* → default-এ platform main thread-এ। দেখুন [Q2](#q2)।

**সম্পর্কিত:** [Q4 — তিন ধরনের channel](#q4) · [Q7 — codec ও error](#q7) · [Q2 — threading](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. MethodChannel, EventChannel, আর BasicMessageChannel-এর মধ্যে পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"তিনটাই Dart আর native-এর মধ্যে টেলিফোন লাইন, কিন্তু কথা বলার ধরন আলাদা। MethodChannel মানে এক প্রশ্ন, এক উত্তর। EventChannel মানে native থেকে Dart-এ একটানা broadcast, অনেকটা radio station-এর মতো। BasicMessageChannel মানে দুই দিকেই যেকোনো ধরনের message, এখানে 'method'-এর কোনো ধারণা নেই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কথোপকথনের তিনটা ধরন।**
দুজন মানুষ তিনভাবে কথা বলতে পারে, সেটা কল্পনা করুন:

- **MethodChannel = একটা phone call।** আপনি একটা জিনিস জিজ্ঞেস করেন, একটা উত্তর পান, call শেষ। ([Q3](#q3))
- **EventChannel = একটা radio station।** আপনি একবার tune in করেন, তারপর native আপনাকে একের পর এক value পাঠাতে থাকে, যতক্ষণ না আপনি tune out করেন। ([Q5](#q5))
- **BasicMessageChannel = text message।** যেকোনো দিক যেকোনো সময় message পাঠাতে পারে। এখানে "method name" নেই, format আপনি ঠিক করেন। ([Q6](#q6))

**ধাপ ২ — একটা দ্রুত তুলনার তালিকা।**

| | MethodChannel | EventChannel | BasicMessageChannel |
|---|---|---|---|
| ধরন | request → reply (একবার) | stream (সময়ের সাথে অনেকবার) | যেকোনো ধরনের message |
| দিক | Dart native-কে call করে | native Dart-এ push করে | দুই দিকেই |
| Dart API | `invokeMethod()` | `receiveBroadcastStream()` | `send()` / `setMessageHandler()` |
| Native API | `setMethodCallHandler` | `StreamHandler` (`onListen`/`onCancel`) | `setMessageHandler` |
| কোন কাজে ভালো | একবার একটা OS API call করা | sensor, location, connectivity | custom protocol, সহজ data |

**ধাপ ৩ — দ্রুত কীভাবে বাছবেন।**
নিজেকে একটা প্রশ্ন করুন: *data কীভাবে প্রবাহিত হচ্ছে?*

- আমি চাইলে একটা value → **MethodChannel**।
- Native আমাকে একটানা stream পাঠাচ্ছে → **EventChannel**।
- আমার নিজের format-এ দুই দিকে message যাচ্ছে → **BasicMessageChannel**।

**ধাপ ৪ — তিনটার নিচের structure একই।**
ভেতরে তিনটাই একই binary messaging আর একই codec পরিবার ব্যবহার করে। EventChannel আর MethodChannel আসলে সেই basic messaging-এর উপরে বসানো সুবিধাজনক wrapper। BasicMessageChannel সেই basic messaging সরাসরি খুলে দেয়।

**Interviewer কেন জিজ্ঞেস করে:** অনেক candidate শুধু MethodChannel জানেন। তিনটাই জানা — আর কখন কোনটা লাগবে ঠিকভাবে বলতে পারা — channel নিয়ে সত্যিকারের গভীরতা দেখায়।

**সাধারণ ভুল:** Native যখন আগে থেকেই একটানা stream তৈরি করছে, তখন বারবার timer চালিয়ে MethodChannel দিয়ে polling করা। ওটার জন্য EventChannel হওয়া উচিত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কোনটা bidirectional?"* → BasicMessageChannel। MethodChannel হলো Dart→native (উত্তরসহ); EventChannel হলো native→Dart।
- *"Native কি MethodChannel দিয়ে Dart-কে call করতে পারে?"* → হ্যাঁ, Dart দিকেও handler বসানো যায়। তবে সাধারণ দিক হলো Dart native-কে call করা।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q5 — EventChannel](#q5) · [Q6 — BasicMessageChannel](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Native থেকে একটানা data stream-এর জন্য EventChannel কীভাবে কাজ করে? একটা use case দিন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"EventChannel হলো native থেকে Dart-এ একটা radio broadcast। Dart একটা `Stream` listen করে টিউন করে, আর native একটা event sink দিয়ে একের পর এক event পাঠাতে থাকে। Native দিকে আমি একটা `StreamHandler` implement করি — `onListen` (পাঠানো শুরু) আর `onCancel` (থামানো ও পরিষ্কার করা)। Sensor, GPS, বা connectivity পরিবর্তনের জন্য এটাই সঠিক পছন্দ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বারবার call-এর বদলে stream কেন।**
কিছু data কখনো থামে না — accelerometer-এর মান, location update, battery state পরিবর্তন। Timer দিয়ে বারবার MethodChannel call করা অপচয় আর ধীর। EventChannel একবার line বসিয়ে দেয়। তারপর native প্রতিটা নতুন মান ঘটার সাথে সাথে Dart-এ পাঠায়।

```
Dart                          Native
 |                              |
 |  stream.listen(...)          |
 | --------------------------->  | onListen() -> start producing events
 |                              |
 |  <-- event 1 ----------      | eventSink.success(data)
 |  <-- event 2 ----------      | eventSink.success(data)
 |  <-- event 3 ----------      | eventSink.success(data)
 |  ...                         |
 |                              |
 |  subscription.cancel()       |
 | --------------------------->  | onCancel() -> stop & clean up
 |                              |
```

**ধাপ ২ — Dart দিক: আর দশটা stream-এর মতোই listen করুন।**
`receiveBroadcastStream()` call করে একটা `Stream` নিন। তারপর raw event-টাকে একটা typed আকারে map করুন।

```dart
import 'package:flutter/services.dart';

class AccelerometerService {
  static const _channel = EventChannel('com.example.app/accelerometer');

  Stream<Map<String, double>> get events {
    return _channel.receiveBroadcastStream().map((event) {
      final data = Map<String, dynamic>.from(event as Map);
      return {
        'x': (data['x'] as num).toDouble(),
        'y': (data['y'] as num).toDouble(),
        'z': (data['z'] as num).toDouble(),
      };
    });
  }
}

// একটা widget-এ ব্যবহার:
// final sub = AccelerometerService().events.listen((d) {
//   print('x=${d['x']}, y=${d['y']}, z=${d['z']}');
// });
// ... আর dispose()-এ: sub.cancel();
```

**ধাপ ৩ — Android দিক (Kotlin): `StreamHandler` implement করুন।**
`onListen` উৎপাদন শুরু করে (sensor listener register করে)। `onCancel` উৎপাদন থামায় (unregister করে)। প্রতিটা মান `eventSink.success(...)` দিয়ে পাঠান।

```kotlin
import io.flutter.plugin.common.EventChannel
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager

class AccelerometerStreamHandler(private val sensorManager: SensorManager)
    : EventChannel.StreamHandler, SensorEventListener {

    private var eventSink: EventChannel.EventSink? = null

    override fun onListen(arguments: Any?, events: EventChannel.EventSink?) {
        eventSink = events
        val sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        sensorManager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_UI)
    }

    override fun onCancel(arguments: Any?) {
        sensorManager.unregisterListener(this) // sensor বন্ধ করে — battery বাঁচায়
        eventSink = null
    }

    override fun onSensorChanged(event: SensorEvent?) {
        event?.let {
            eventSink?.success(mapOf(
                "x" to it.values[0],
                "y" to it.values[1],
                "z" to it.values[2]
            ))
        }
    }

    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {}
}
```

`configureFlutterEngine`-এ এটা register করুন:

```kotlin
EventChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example.app/accelerometer")
    .setStreamHandler(AccelerometerStreamHandler(getSystemService(SENSOR_SERVICE) as SensorManager))
```

**ধাপ ৪ — iOS দিক (Swift): একই দুটো callback।**
iOS-এ আপনি `FlutterStreamHandler` implement করবেন `onListen` আর `onCancel` দিয়ে। মান পাঠাবেন `eventSink(data)` দিয়ে। কোনো error না থাকলে `nil` return করবেন।

```swift
class AccelerometerStreamHandler: NSObject, FlutterStreamHandler {
    private var eventSink: FlutterEventSink?

    func onListen(withArguments arguments: Any?,
                  eventSink events: @escaping FlutterEventSink) -> FlutterError? {
        eventSink = events
        // motion manager চালু করুন, তারপর প্রতিটা update-এ: eventSink?(["x": x, "y": y, "z": z])
        return nil
    }

    func onCancel(withArguments arguments: Any?) -> FlutterError? {
        // motion manager বন্ধ করুন
        eventSink = nil
        return nil
    }
}
```

**ধাপ ৫ — EventChannel-এর এক নম্বর bug: producer বন্ধ না করা।**
দুই জায়গায় পরিষ্কার করতে হবে। Dart-এ `dispose()`-এর ভেতরে subscription cancel করুন। Native-এ `onCancel`-এর ভেতরে sensor বা producer থামান। `onCancel` ভুলে গেলে sensor চিরকাল চলতে থাকবে — এটা battery আর memory leak।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা যাচাই করেন আপনি one-shot (MethodChannel) আর streaming (EventChannel)-এর পার্থক্য জানেন কি না। আর native producer পরিষ্কার করেন কি না।

**সাধারণ ভুল:** EventChannel ব্যবহার না করে MethodChannel দিয়ে polling করা। অথবা `onCancel`-এ native listener unregister করতে ভুলে যাওয়া, যা battery শেষ করে দেয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Single-subscription না broadcast?"* → `receiveBroadcastStream()` একটা broadcast stream দেয়। তাই একের বেশি Dart listener যুক্ত হতে পারে।
- *"Error event কীভাবে পাঠাবেন?"* → Android-এ `eventSink.error(code, message, details)`; iOS-এ একটা `FlutterError` return বা pass করুন।

**সম্পর্কিত:** [Q4 — তিন ধরনের channel](#q4) · [Q3 — MethodChannel](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. BasicMessageChannel কী? MethodChannel-এর বদলে কখন এটা ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"BasicMessageChannel হলো সবচেয়ে সহজ channel — এটা একটা codec দিয়ে শুধু raw message এদিক-ওদিক পাঠায়, 'method name' বলে কিছু জানে না। দুই দিকই পাঠাতে আর গ্রহণ করতে পারে। আমি এটা ব্যবহার করি যখন native-কে অবাধে Dart-এ message পাঠাতে হয়, যখন আমি JSON blob-এর মতো সহজ data পাঠাই, বা যখন আমি নিজের protocol চাই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Text message-এর ধারণা।**
MethodChannel হলো একটা গোছানো phone call ("এই argument দিয়ে method X call করো")। BasicMessageChannel হলো সাধারণ text messaging: আপনি একটা message পাঠান, অন্য দিক সেটা পায় এবং উত্তর দিতে পারে। Method name দিয়ে built-in routing নেই — message-এর মানে কী, সেটা আপনি ঠিক করেন।

```
   MethodChannel                    BasicMessageChannel
 +------------------+            +----------------------+
 | invokeMethod(    |            | send(message)        |
 |   'methodName',  |            |                      |
 |   arguments      |            | (any shape, no       |
 | )                |            |  method dispatch)    |
 |                  |            |                      |
 | Built-in method  |            | No routing. You      |
 | dispatch.        |            | parse it yourself.   |
 +------------------+            +----------------------+
```

**ধাপ ২ — তৈরির সময়েই একটা codec বেছে নিন।**
Codec ঠিক করে message কীভাবে encode হবে:

- `StringCodec` — সাধারণ text string।
- `BinaryCodec` — raw `ByteData`।
- `JSONMessageCodec` — JSON map বা list।
- `StandardMessageCodec` — Flutter-এর default binary codec (MethodChannel যে type গুলো সামলায়, সেগুলোই সামলায়)।

**ধাপ ৩ — Dart দিক: পাঠানো আর গ্রহণ করা।**
আপনি একদিকে `send(...)` দিয়ে message পাঠাতে পারেন। আবার native থেকে আসা message নিতে একটা handler বসাতে পারেন।

```dart
import 'package:flutter/services.dart';

final channel = BasicMessageChannel<String>(
  'com.example.app/config',
  StringCodec(),
);

// native-এ একটা message পাঠান, তারপর তার reply-এর জন্য await করুন
final String? reply = await channel.send('{"action": "getConfig"}');

// native আমাদের যে message পাঠায় সেগুলো গ্রহণ করুন
channel.setMessageHandler((String? message) async {
  print('Native says: $message');
  return 'acknowledged'; // native-কে ফিরতি উত্তর
});
```

**ধাপ ৪ — MethodChannel-এর বদলে কখন এটা বেছে নেবেন।**
BasicMessageChannel ব্যবহার করুন যখন:

1. Native-কেই প্রায়ই কথা শুরু করতে হয় (শুধু Dart-কে উত্তর দেওয়া নয়)।
2. আপনি সহজ data আদান-প্রদান করছেন (একটা config string, ছোট একটা JSON) এবং method routing লাগছে না।
3. আপনি নিজের custom protocol বা message format চান।
4. আপনি `BinaryCodec` দিয়ে বড় binary data পাঠাচ্ছেন, আর method call-এর বাড়তি খরচ চান না।

**ধাপ ৫ — এটা এখনো সচল (এবং Pigeon-কে চালায়)।**
এটা deprecated নয়। বরং Pigeon-এর generated code ভেতরে `BasicMessageChannel` আর `StandardMessageCodec` ব্যবহার করে। দেখুন [Q10](#q10)।

**Interviewer কেন জিজ্ঞেস করে:** যাচাই করতে যে আপনি শুধু MethodChannel নয়, পুরো channel পরিসরটা জানেন। BasicMessageChannel কোথায় মানানসই, সেটা জানা architectural গভীরতা দেখায়।

**সাধারণ ভুল:** এটাকে deprecated বা অকেজো বলা। এটা maintained, আর method-call semantics না লাগলে এটাই সঠিক জিনিস। আরেকটা ভুল — এটাকে EventChannel-এর সাথে গুলিয়ে ফেলা। BasicMessageChannel দুই-মুখী এবং message-ভিত্তিক, এক-মুখী stream নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"BasicMessageChannel বনাম EventChannel?"* → BasicMessageChannel হলো দুই-মুখী message; EventChannel হলো native থেকে Dart-এ এক-মুখী stream।
- *"Config blob-এর জন্য কোন codec?"* → `JSONMessageCodec` বা `StringCodec` — দুটোই ঠিক আছে।

**সম্পর্কিত:** [Q4 — তিন ধরনের channel](#q4) · [Q10 — Pigeon](#q10)

[↑ উপরে ফিরুন](#toc)

---

# C. Bridge পার হওয়া error, data ও type

---

## <a id="q7"></a>7. একটা channel দিয়ে কোন কোন data type পার হতে পারে? `PlatformException` দিয়ে error কীভাবে handle করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা codec Dart-এর value-গুলোকে byte-এ বদলায়, আবার ফিরিয়ে আনে। Standard codec সমর্থন করে `null`, `bool`, `int`, `double`, `String`, `Uint8List`, `List`, আর `Map` — আপনার নিজের custom class নয়। তাই আমি ওগুলোকে আগে map-এ বদলে ফেলি। Error-এর জন্য native side `result.error(code, message, details)` দিয়ে জবাব দেয়। Dart সেটা `PlatformException` হিসেবে পায়, আর আমি `try/catch` দিয়ে ধরি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Codec কেন দরকার।**
Dart আর native একই memory ভাগ করে না। তাই value-গুলোকে byte-এ প্যাক করে সীমা পার করাতে হয়, আর ওপারে গিয়ে খুলতে হয়। এই প্যাক করা আর খোলার কাজটাই **codec**। MethodChannel আর EventChannel-এর default হলো `StandardMethodCodec` (যেটা `StandardMessageCodec`-এর উপর তৈরি)।

**ধাপ ২ — যে type-গুলো সমর্থিত (এই তালিকাটা মুখস্থ রাখুন)।**
Standard codec এই type-গুলো দুই দিকেই বোঝে:

| Dart | Kotlin | Swift |
|---|---|---|
| `null` | `null` | `nil` |
| `bool` | `Boolean` | `NSNumber(bool)` |
| `int` | `Int` / `Long` | `NSNumber(int)` |
| `double` | `Double` | `NSNumber(double)` |
| `String` | `String` | `String` |
| `Uint8List` | `ByteArray` | `FlutterStandardTypedData` |
| `List` | `List` | `Array` |
| `Map` | `HashMap` | `Dictionary` |

এই তালিকার বাইরে যা আছে (আপনার নিজের `User` class, একটা `DateTime`) সেটা সরাসরি সমর্থিত **নয়**।

**ধাপ ৩ — Custom object কীভাবে পাঠাবেন।**
পাঠানোর আগে সেটাকে `Map`-এ বদলে নিন, আর ওপারে গিয়ে আবার তৈরি করুন। Date সাধারণত ISO string বা millisecond হিসেবে যায়।

```dart
// Dart: User object নয়, একটা Map পাঠান
await _channel.invokeMethod('saveUser', {
  'id': user.id,
  'name': user.name,
  'createdAt': user.createdAt.toIso8601String(),
});
```

এই typing-এর কাজটা নিজে থেকে হয়ে যাক চাইলে Pigeon ব্যবহার করুন ([Q10](#q10))।

**ধাপ ৪ — Error: native side একটা গোছানো failure পাঠায়।**
Crash না করে native একটা error দিয়ে জবাব দেয়, যার তিনটা অংশ থাকে: একটা `code` (ছোট string), একটা `message` (মানুষের পড়ার মতো লেখা), আর optional `details`।

```kotlin
// Android
result.error("PERMISSION_DENIED", "Camera permission was not granted", null)
```

```swift
// iOS
result(FlutterError(code: "PERMISSION_DENIED",
                    message: "Camera permission was not granted",
                    details: nil))
```

**ধাপ ৫ — Dart সেটা `PlatformException` হিসেবে ধরে।**
Native-এর তিনটা field আসে `e.code`, `e.message`, আর `e.details` হিসেবে। আপনি code দেখে আলাদা পথ নিতে পারেন।

```dart
try {
  await _channel.invokeMethod('openCamera');
} on PlatformException catch (e) {
  if (e.code == 'PERMISSION_DENIED') {
    showSettingsDialog();
  } else {
    showError(e.message ?? 'Unknown native error');
  }
} on MissingPluginException {
  // native side-এ method name পাওয়া যায়নি (প্রায়ই ভুলে যাওয়া notImplemented case)
  showError('This feature is not available on your device.');
}
```

**ধাপ ৬ — যে দুটো error type জানা দরকার।**
- **`PlatformException`** → native `result.error(...)` দিয়ে জবাব দিয়েছে। এটা expected, handle করা failure।
- **`MissingPluginException`** → ওই method name-এর জন্য native-এ কোনো handler ছিল না (ভুল নাম, বা `notImplemented()`)।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি type-এর সীমা জানেন কি না (custom class চলবে না)। আর app crash করতে না দিয়ে গোছানো `PlatformException` দিয়ে failure সামলান কি না।

**সাধারণ ভুল:** একটা Dart object সরাসরি channel দিয়ে পাঠানোর চেষ্টা করা। অথবা `PlatformException` বাদ দেওয়া, ফলে একটা native error unhandled crash হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`int` কখনো কখনো `Long` হয়ে আসে কেন?"* → বড় int Android-এ `Long`-এ map হয়। নিরাপদ থাকতে Dart side-এ `as num` দিয়ে পড়ুন।
- *"এই সব হাতে করা mapping কীভাবে এড়াবেন?"* → typed class আর serialization তৈরি করতে Pigeon ব্যবহার করুন। দেখুন [Q10](#q10)।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q10 — Pigeon](#q10)

[↑ উপরে ফিরুন](#toc)

---

# D. Native-এর দিকে — FFI, plugin, add-to-app

---

## <a id="q8"></a>8. Dart FFI (`dart:ffi`) কী? এটা Platform Channel থেকে কীভাবে আলাদা? কখন এটা ব্যবহার করবেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart FFI দিয়ে Dart সরাসরি ও synchronous ভাবে C/C++ function call করতে পারে, engine-এর message system-এ না ঢুকেই। Platform Channel serialize করা data নিয়ে Kotlin/Swift-এর সাথে async কথা বলে। FFI সরাসরি, প্রায় সঙ্গে সঙ্গেই function call আর raw memory দিয়ে C/C++-এর সাথে কথা বলে। আমি OS API-র জন্য channel ব্যবহার করি, আর ভারী computation library-র জন্য FFI — যেমন crypto, image processing, বা SQLite।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Native-এ যাওয়ার দুটো আলাদা দরজা।**
Dart থেকে বেরোনোর দুটো দরজা আছে:

- **Platform Channel** → **Kotlin/Swift**-এর দরজা, async, data প্যাক করে একটা codec। OS feature-এর জন্য চমৎকার।
- **Dart FFI** (Foreign Function Interface) → **C/C++**-এর দরজা, synchronous, function-টা সরাসরি call করে। দ্রুত, math-ভারী library-র জন্য চমৎকার।

```
  Platform Channels                          Dart FFI
 +-------------------------+    +------------------------------+
 | Dart <-> Engine <-> Kotlin/Swift | | Dart ---> C/C++ library    |
 |                         |    | (direct function call)        |
 | Async, message-based    |    | Synchronous, zero-copy        |
 | Talks to Kotlin/Swift   |    | Only C/C++ ABI                |
 | ~0.1ms overhead/call    |    | ~microsecond overhead         |
 +-------------------------+    +------------------------------+
```

**ধাপ ২ — পাশাপাশি একটা তুলনা।**

| দিক | Platform Channels | Dart FFI |
|---|---|---|
| যে ভাষা লক্ষ্য | Kotlin/Java, Swift/ObjC | C / C++ |
| যোগাযোগ | Async message | Sync function call |
| গতি | ভালো (প্রতি call-এ ~0.1ms) | চমৎকার (প্রতি call-এ ~microsecond) |
| Data পাঠানো | codec দিয়ে serialize করা | pointer, struct, raw memory |
| কোন কাজে ভালো | OS API, UI-layer-এর native code | Crypto, image processing, audio DSP |

**ধাপ ৩ — সবচেয়ে ছোট একটা FFI উদাহরণ।**
আপনি C function-এর গড়নটা দুইবার ঘোষণা করেন (native type-গুলো আর Dart type-গুলো), shared library খোলেন, function খুঁজে নেন, তারপর call করেন।

```dart
import 'dart:ffi';
import 'dart:io' show Platform;

// C signature, দুইভাবে বর্ণনা করা:
typedef NativeAdd = Int32 Function(Int32 a, Int32 b); // native-side type
typedef DartAdd = int Function(int a, int b);          // Dart-side type

void main() {
  final lib = Platform.isAndroid
      ? DynamicLibrary.open('libnative_math.so')
      : DynamicLibrary.process(); // iOS: statically link করা

  final add = lib.lookupFunction<NativeAdd, DartAdd>('add_numbers');

  final result = add(3, 7); // synchronous — কোনো await নেই
  print(result); // 10
}
```

এর সাথে মেলানো C code:

```c
// native_math.c
#include <stdint.h>

int32_t add_numbers(int32_t a, int32_t b) {
    return a + b;
}
```

**ধাপ ৪ — কখন FFI-ই সঠিক পছন্দ।**
FFI-এর দিকে যান যখন:

- আপনার প্রতি সেকেন্ডে অনেক call লাগে খুব কম latency-তে (audio DSP, physics, parsing)।
- আপনার হাতে আগে থেকেই একটা প্রমাণিত C/C++ library আছে, যেটা আবার ব্যবহার করবেন (SQLite, OpenCV, একটা TensorFlow Lite C API)।
- আপনার একটা synchronous result দরকার।
- আপনি একটাই native codebase সব platform-এ ভাগ করে ব্যবহার করতে চান, Kotlin আর Swift দুইবার না লিখে।

Tip: C header থেকে Dart binding নিজে থেকে তৈরি করতে `ffigen` package ব্যবহার করুন, তাহলে হাতে `typedef` লিখতে হবে না।

**ধাপ ৫ — বড় ফাঁদ: FFI যে isolate থেকে call হয় সেটাকে block করে।**
একটা FFI call synchronous, তাই লম্বা C function ওই isolate-কে জমিয়ে দেয়। কাজটা ভারী হলে আলাদা isolate-এ চালান (`Isolate.run`)। আর মনে রাখুন, FFI Kotlin বা Swift call করতে পারে না — শুধু C-ABI code।

**Interviewer কেন জিজ্ঞেস করে:** FFI দেখায় আপনি performance-এর trade-off বোঝেন আর সঠিক tool বাছতে পারেন: OS API-র জন্য channel, compute library-র জন্য FFI।

**সাধারণ ভুল:** বলা যে FFI, Platform Channel-এর বদলি। এটা নয় — FFI দিয়ে Kotlin/Swift-এর API-তে পৌঁছানো যায় না। আরেকটা ভুল হলো ভুলে যাওয়া যে ভারী FFI call isolate-কে block করে, তাই সেটা UI isolate-এর বাইরে চালানো উচিত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"C-তে একটা string কীভাবে পাঠাবেন?"* → সেটাকে native UTF-8 pointer-এ বদলান (যেমন `package:ffi`-র `toNativeUtf8()` দিয়ে), আর পরে free করে দিন।
- *"SQLite-এর জন্য channel না FFI?"* → FFI (`sqlite3` package FFI ব্যবহার করে)। এটা একটা C library, আর এর দ্রুত, synchronous call দরকার।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q4 — তিন ধরনের channel](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. একটা সহজ Flutter plugin package কীভাবে লিখবেন? structure, pubspec আর platform code বর্ণনা করুন।

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Plugin হলো এমন একটা package যা platform code (Kotlin/Swift) আর একটা পরিষ্কার Dart API একসাথে bundle করে। ভেতরে সেই API Platform Channel ব্যবহার করে। আধুনিক structure-এ তিনটা Dart অংশ থাকে: একটা public API class, একটা platform-interface abstract class, আর একটা MethodChannel implementation। এতে platform implementation বদলে দেওয়া যায়, যা test আর web-এর জন্য দারুণ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Plugin জিনিসটা কী।**
Plugin channel-এর জটিল কাজটা একটা সহজ Dart API-র পেছনে লুকিয়ে রাখে। App শুধু `MyPlugin().getDeviceName()` call করে। App কখনো channel দেখে না। ভেতরে plugin একটা MethodChannel দিয়ে native-এর সাথে কথা বলে।

**ধাপ ২ — সঠিক template দিয়ে তৈরি করুন।**

```bash
flutter create --template=plugin --platforms=android,ios my_plugin
```

Directory-র গঠন:

```
my_plugin/
+-- lib/
|   +-- my_plugin.dart                    <- Public Dart API
|   +-- my_plugin_method_channel.dart     <- MethodChannel implementation
|   +-- my_plugin_platform_interface.dart <- Abstract interface
+-- android/src/main/kotlin/.../MyPlugin.kt   <- Android implementation
+-- ios/Classes/MyPlugin.swift                <- iOS implementation
+-- test/                                  <- Dart unit tests
+-- example/                               <- Example app
+-- pubspec.yaml
```

**ধাপ ৩ — `pubspec.yaml` native entry point ঘোষণা করে।**

```yaml
name: my_plugin
description: A Flutter plugin for device info.
version: 1.0.0

environment:
  sdk: '>=3.0.0 <4.0.0'
  flutter: '>=3.10.0'

dependencies:
  flutter:
    sdk: flutter
  plugin_platform_interface: ^2.1.0

flutter:
  plugin:
    platforms:
      android:
        package: com.example.my_plugin
        pluginClass: MyPlugin
      ios:
        pluginClass: MyPlugin
```

**ধাপ ৪ — তিনটা Dart file (federated pattern)।**

Platform interface (যে contract প্রতিটা platform-কে মানতে হবে):

```dart
// lib/my_plugin_platform_interface.dart
import 'package:plugin_platform_interface/plugin_platform_interface.dart';
import 'my_plugin_method_channel.dart';

abstract class MyPluginPlatform extends PlatformInterface {
  MyPluginPlatform() : super(token: _token);
  static final Object _token = Object();
  static MyPluginPlatform _instance = MethodChannelMyPlugin();

  static MyPluginPlatform get instance => _instance;
  static set instance(MyPluginPlatform instance) {
    PlatformInterface.verifyToken(instance, _token);
    _instance = instance;
  }

  Future<String?> getDeviceName();
}
```

MethodChannel implementation (default আসল implementation):

```dart
// lib/my_plugin_method_channel.dart
import 'package:flutter/services.dart';
import 'my_plugin_platform_interface.dart';

class MethodChannelMyPlugin extends MyPluginPlatform {
  final _channel = const MethodChannel('my_plugin');

  @override
  Future<String?> getDeviceName() async {
    return await _channel.invokeMethod<String>('getDeviceName');
  }
}
```

Public API (app developer-রা যেটা call করেন):

```dart
// lib/my_plugin.dart
import 'my_plugin_platform_interface.dart';

class MyPlugin {
  Future<String?> getDeviceName() {
    return MyPluginPlatform.instance.getDeviceName();
  }
}
```

**ধাপ ৫ — Native implementation-গুলো।**

Android (`MyPlugin.kt`) — `onDetachedFromEngine`-এ clean-up-টা খেয়াল করুন:

```kotlin
class MyPlugin : FlutterPlugin, MethodCallHandler {
    private lateinit var channel: MethodChannel

    override fun onAttachedToEngine(binding: FlutterPlugin.FlutterPluginBinding) {
        channel = MethodChannel(binding.binaryMessenger, "my_plugin")
        channel.setMethodCallHandler(this)
    }

    override fun onMethodCall(call: MethodCall, result: MethodChannel.Result) {
        if (call.method == "getDeviceName") {
            result.success(android.os.Build.MODEL)
        } else {
            result.notImplemented()
        }
    }

    override fun onDetachedFromEngine(binding: FlutterPlugin.FlutterPluginBinding) {
        channel.setMethodCallHandler(null) // leak এড়াতে
    }
}
```

iOS (`MyPlugin.swift`):

```swift
public class MyPlugin: NSObject, FlutterPlugin {
    public static func register(with registrar: FlutterPluginRegistrar) {
        let channel = FlutterMethodChannel(name: "my_plugin",
                                           binaryMessenger: registrar.messenger())
        registrar.addMethodCallDelegate(MyPlugin(), channel: channel)
    }

    public func handle(_ call: FlutterMethodCall, result: @escaping FlutterResult) {
        if call.method == "getDeviceName" {
            result(UIDevice.current.name)
        } else {
            result(FlutterMethodNotImplemented)
        }
    }
}
```

**ধাপ ৬ — তিন file-এ ভাগ করা কেন জরুরি।**
Public API সরাসরি channel-এর সাথে কথা বলে না, বলে একটা interface-এর সাথে। তাই test-এ আপনি একটা fake implementation বসিয়ে দিতে পারেন। web-এর জন্য আলাদা একটা implementation দিতে পারেন। Flutter team এই "federated plugin" design-ই সুপারিশ করে।

**Interviewer কেন জিজ্ঞেস করে:** Plugin লেখা senior-দের একটা মূল দক্ষতা। তাঁরা দেখেন আপনি federated architecture বোঝেন কি না, আর concern আলাদা রাখেন কি না।

**সাধারণ ভুল:** Public API class-এর ভেতরেই সরাসরি channel call বসিয়ে দেওয়া, আর platform interface বাদ দেওয়া। আরেকটা ভুল — Android-এ `onDetachedFromEngine`-এ handler clear করতে ভুলে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Web কীভাবে support করবেন?"* → একটা web implementation যোগ করুন, যেটা `MyPluginPlatform` extend করে আর নিজেকে register করে; public API বদলায় না।
- *"Dart side কীভাবে test করবেন?"* → `MyPluginPlatform.instance`-এর জায়গায় একটা fake বসান, অথবা MethodChannel mock করুন।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q10 — Pigeon](#q10) · [Q7 — codec আর error](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. Pigeon কী? এটা Platform Channel-এর type safety কীভাবে উন্নত করে?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Pigeon হলো Flutter-এর official code-generation tool। আমি আসল type দিয়ে একটাই Dart schema লিখি। তারপর Pigeon আমার জন্য মিলে যাওয়া Dart, Kotlin আর Swift code generate করে দেয়। এতে channel-এর সবচেয়ে বড় দুটো ঝুঁকি চলে যায়: method-name string-এ ভুল লেখা, আর untyped argument হাতে cast করা। সবকিছু compile-time type-safe হয়ে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Pigeon কোন সমস্যা সমাধান করে।**
কাঁচা channel পুরোটাই string-নির্ভর। আপনি লিখলেন `invokeMethod('getUsr', {'id': 42})`। `'getUsr'`-এ typo হলে সেটা ধরা পড়বে শুধু runtime-এ। Reply আসে `dynamic` হিসেবে। তাই হাতে cast করে আশা করতে হয় সব ঠিক আছে। বড় API-তে এটা খুব ঠুনকো।

```
  Without Pigeon                       With Pigeon
 +--------------------+    +------------------------------+
 | invokeMethod(      |    | Define schema in Dart        |
 |   'getUser',       |    |           |                  |
 |    {'id': 42})     |    |     +-----v-----+            |
 |                    |    |     |  pigeon    |            |
 | result is dynamic  |    |     |  codegen   |            |
 | cast manually      |    |     +-----+-----+            |
 | typos -> runtime   |    |    +------+------+           |
 | errors             |    |    v      v      v           |
 +--------------------+    |  Dart  Kotlin  Swift          |
                           |  (typed classes & methods)    |
                           |  Compile-time type safety     |
                           +------------------------------+
```

**ধাপ ২ — Dart-এ schema লিখুন।**
আপনি data class আর একটা API define করেন। `@HostApi()` মানে native এটা implement করে আর Dart call করে। `@FlutterApi()` মানে Dart এটা implement করে আর native call করে।

```dart
// pigeons/messages.dart
import 'package:pigeon/pigeon.dart';

class UserRequest {
  late int userId;
}

class UserResponse {
  late String name;
  late String email;
  late int age;
}

@HostApi() // Native implement করে, Dart call করে
abstract class UserApi {
  UserResponse getUser(UserRequest request);
}

@FlutterApi() // Dart implement করে, Native call করে
abstract class UserNotificationApi {
  void onUserUpdated(UserResponse user);
}
```

**ধাপ ৩ — Code generation চালান।**

```bash
dart run pigeon \
  --input pigeons/messages.dart \
  --dart_out lib/src/generated/messages.g.dart \
  --kotlin_out android/src/main/kotlin/com/example/Messages.g.kt \
  --swift_out ios/Classes/Messages.g.swift
```

**ধাপ ৪ — Native-এ generated interface implement করুন।**
Pigeon `UserApi` interface-টা generate করে দেয়; আপনি শুধু body-টা লিখে দেন।

```kotlin
class UserApiImpl : UserApi {
    override fun getUser(request: UserRequest): UserResponse {
        return UserResponse(name = "Alice", email = "alice@example.com", age = 30)
    }
}

// configureFlutterEngine-এ register করুন:
UserApi.setUp(flutterEngine.dartExecutor.binaryMessenger, UserApiImpl())
```

**ধাপ ৫ — Dart থেকে call করুন, পুরো typed।**

```dart
final api = UserApi();
final response = await api.getUser(UserRequest(userId: 42));
print(response.name); // "Alice" — typed, cast নেই, magic string নেই
```

**ধাপ ৬ — আপনি কী কী পান।**
- Type না মিললে compile-time error।
- ভুল লেখার মতো কোনো method-name string নেই।
- Serialization নিজে থেকেই generate হয় — হাতে codec-এর কাজ নেই ([Q7](#q7))।
- `@HostApi` / `@FlutterApi` দিক পরিষ্কার করে বলে দেয়।
- Generated code-এ null safety ঠিকভাবে থাকে।

**Interviewer কেন জিজ্ঞেস করে:** বড় plugin-এর জন্য Pigeon officially সুপারিশ করা হয়। তাঁরা দেখতে চান আপনি আধুনিক tooling জানেন, আর জটিল API-র জন্য হাতে ভুলে ভরা channel লেখেন না।

**সাধারণ ভুল:** Pigeon-কে third-party package ভাবা (এটা Flutter team-এর, `package:pigeon`)। অথবা ভাবা যে এটা Platform Channel-এর জায়গা নেয়। এটা channel code-ই generate করে — generated code ভেতরে `BasicMessageChannel` আর `StandardMessageCodec` ব্যবহার করে ([Q6](#q6))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Pigeon ভেতরে কী ব্যবহার করে?"* → `BasicMessageChannel` + `StandardMessageCodec`।
- *"কাঁচা MethodChannel কখন এখনো ঠিক আছে?"* → এক-দুটো সহজ method-এর জন্য। API বড় হলে Pigeon-এর আসল সুবিধা বোঝা যায়।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q6 — BasicMessageChannel](#q6) · [Q7 — codec আর error](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. একটা আগে থেকে থাকা native Android বা iOS app-এ Flutter module কীভাবে যোগ করবেন (add-to-app)?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একে বলে 'add-to-app'। পুরো একটা Flutter app-এর বদলে আমি একটা Flutter module বানাই। তারপর সেটাকে আগে থেকে থাকা native project-এ dependency হিসেবে embed করি। এরপর native app একটা `FlutterActivity` (Android) বা `FlutterViewController` (iOS) চালু করে Flutter screen দেখায়। app-এর বাকি অংশ native-ই থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কোম্পানিগুলো কেন এটা করে।**
অনেক team-এর আগে থেকেই একটা বড় native app আছে। তাঁরা সব একসাথে rewrite করেন না। প্রথমে একটা feature-এর জন্য Flutter যোগ করেন (যেমন, নতুন একটা checkout screen), কাজ করছে প্রমাণ করেন, তারপর বাড়ান। এই ধীরে ধীরে এগোনোর পথটাই add-to-app। বড় কোম্পানিতে এটা খুব সাধারণ।

```
 Existing Native App
 +-------------------------------------+
 |  Native Activity / ViewController   |
 |  +-------------------------------+  |
 |  |  FlutterActivity /            |  |
 |  |  FlutterViewController        |  |
 |  |  +-------------------------+  |  |
 |  |  |   Flutter Module UI     |  |  |
 |  |  |   (Dart code)           |  |  |
 |  |  +-------------------------+  |  |
 |  +-------------------------------+  |
 |  Other native screens...           |
 +-------------------------------------+
```

**ধাপ ২ — একটা module বানান (app নয়)।**

```bash
flutter create --template module my_flutter_module
```

একটা module-এ লুকানো `.android/` আর `.ios/` wrapper থাকে (development-এর সময় ব্যবহার হয়)। আর Dart code-এর জন্য একটা `lib/` folder থাকে। এতে চেনা পুরো `android/` আর `ios/` folder থাকে না।

**ধাপ ৩ — Android: Gradle-এ যুক্ত করুন।**

native app-এর `settings.gradle`-এ:

```groovy
include ':app'

setBinding(new Binding([gradle: this]))
evaluate(new File(
    settingsDir.parentFile,
    'my_flutter_module/.android/include_flutter.groovy'
))
```

`app/build.gradle`-এ:

```groovy
dependencies {
    implementation project(':flutter')
}
```

তারপর একটা native Activity থেকে Flutter চালু করুন:

```kotlin
import io.flutter.embedding.android.FlutterActivity

// পুরো screen জুড়ে Flutter
startActivity(FlutterActivity.createDefaultIntent(this))

// অথবা নির্দিষ্ট একটা route-এ খুলুন
startActivity(
    FlutterActivity.withNewEngine().initialRoute("/settings").build(this)
)
```

**ধাপ ৪ — iOS: CocoaPods-এ যুক্ত করুন।**

native app-এর `Podfile`-এ:

```ruby
flutter_application_path = '../my_flutter_module'
load File.join(flutter_application_path, '.ios', 'Flutter', 'podhelper.rb')

target 'MyNativeApp' do
  install_all_flutter_pods(flutter_application_path)
end
```

`pod install` চালান, তারপর Swift-এ:

```swift
import Flutter

let flutterEngine = FlutterEngine(name: "my flutter engine")
flutterEngine.run()

let flutterVC = FlutterViewController(engine: flutterEngine, nibName: nil, bundle: nil)
present(flutterVC, animated: true)
```

**ধাপ ৫ — গতির জন্য engine আগেভাগে গরম করুন।**
ঠান্ডা অবস্থা থেকে একটা `FlutterEngine` চালু হতে একটু সময় লাগে। Flutter screen-টা যদি বারবার খোলা হয়, তাহলে app startup-এ একবারই engine বানিয়ে `run()` করুন (cache করে রাখুন)। তারপর সেটাই বারবার ব্যবহার করুন। এতে screen প্রথমবার দেখানোর সময় চোখে পড়া দেরিটা চলে যায়।

**Interviewer কেন জিজ্ঞেস করে:** অনেক কোম্পানি ধাপে ধাপে Flutter নেয়। তাঁরা জানতে চান আপনি একটা brownfield (আগে থেকে থাকা) app-এ integrate করতে পারেন কি না। শুধু নতুন greenfield app বানাতে পারা যথেষ্ট নয়।

**সাধারণ ভুল:** `--template module` আর `--template app` গুলিয়ে ফেলা। একটা module-এ লুকানো `.android/` আর `.ios/` wrapper থাকে, পুরো native folder নয়। আরেকটা ভুল — engine আগে গরম না করা, ফলে প্রথমবার খোলার সময় চোখে পড়া দেরি হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"native দিক module-এর সাথে কীভাবে কথা বলে?"* → Platform Channel দিয়ে, একদম সাধারণ app-এর মতোই। দেখুন [Q3](#q3)।
- *"একটা engine নাকি অনেকগুলো?"* → গতির জন্য একটা cache করা engine বারবার ব্যবহার করুন; কম খরচে কয়েকটা engine দরকার হলে `FlutterEngineGroup` কাজে লাগে।

**সম্পর্কিত:** [Q3 — MethodChannel](#q3) · [Q12 — native SDK integrate করা](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. যে native SDK-র (যেমন payment, maps) কোনো Flutter plugin নেই, সেটা কীভাবে integrate করবেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমার দুটো উপায় আছে। একটা app-এ একবারের কাজ হলে আমি native SDK যোগ করি আর app-এর ভেতরেই Platform Channel bridge code লিখি। বারবার ব্যবহারের জিনিস হলে আমি সেটাকে একটা ঠিকঠাক plugin package-এ মুড়ে দিই। SDK-টার যদি native view-ও দেখাতে হয়, যেমন একটা map বা card field, তাহলে আমি সেটা PlatformView (`AndroidView` / `UiKitView`) দিয়ে embed করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কৌশল বেছে নিন।**
দুটো পথ, মূল ধারণা একই (একটা channel bridge):

```
 Option A: In-App Channels              Option B: Plugin Package
 (quick, single project)                (reusable, publishable)
 +--------------------+                 +-------------------------+
 | Your Flutter App   |                 |  my_sdk_plugin/         |
 | +-- lib/           |                 |  +-- lib/  (Dart API)   |
 | +-- android/       |                 |  +-- android/ (native)  |
 | +-- ios/           |                 |  +-- ios/     (native)  |
 +--------------------+                 |  +-- example/           |
                                        +-------------------------+
```

একটামাত্র app-এর জন্য Option A দ্রুত। অনেক app-এ বারবার ব্যবহারের জন্য Option B (দেখুন [Q9](#q9))।

**ধাপ ২ — প্রতিটা platform-এ native SDK যোগ করুন।**

Android — `android/app/build.gradle`:

```groovy
dependencies {
    implementation 'com.payment.sdk:core:2.5.0'
}
```

iOS — `ios/Podfile`:

```ruby
target 'Runner' do
  pod 'PaymentSDK', '~> 2.5'
end
```

**ধাপ ৩ — native bridge লিখুন (এখানে Android দেখানো হলো)।**
bridge Dart-এর call নেয়, SDK-র সাথে কথা বলে, তারপর উত্তর দেয়। খেয়াল রাখুন, SDK-র callback background thread-এ আসতে পারে — উত্তর দেওয়ার আগে main thread-এ পাঠান (দেখুন [Q2](#q2))।

```kotlin
import com.payment.sdk.PaymentClient
import com.payment.sdk.PaymentResult

class PaymentBridge(private val activity: Activity) : MethodChannel.MethodCallHandler {

    private val client = PaymentClient(activity)

    override fun onMethodCall(call: MethodCall, result: MethodChannel.Result) {
        when (call.method) {
            "processPayment" -> {
                val amount = call.argument<Double>("amount") ?: run {
                    result.error("INVALID_ARG", "Amount required", null); return
                }
                val currency = call.argument<String>("currency") ?: "USD"

                client.processPayment(amount, currency) { paymentResult ->
                    // SDK callback background thread-এ আসতে পারে:
                    activity.runOnUiThread {
                        when (paymentResult) {
                            is PaymentResult.Success -> result.success(mapOf(
                                "transactionId" to paymentResult.transactionId,
                                "status" to "success"
                            ))
                            is PaymentResult.Failure -> result.error(
                                "PAYMENT_FAILED", paymentResult.message, null
                            )
                        }
                    }
                }
            }
            else -> result.notImplemented()
        }
    }
}
```

`MainActivity`-তে register করুন:

```kotlin
override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example.app/payment")
        .setMethodCallHandler(PaymentBridge(this))
}
```

**ধাপ ৪ — Dart API লিখুন।**
channel-টা একটা পরিষ্কার service-এর পেছনে লুকিয়ে রাখুন। result-কে একটা typed object-এ রূপ দিন। আর `PlatformException`-কে domain error-এ বদলে দিন।

```dart
class PaymentService {
  static const _channel = MethodChannel('com.example.app/payment');

  Future<PaymentResult> processPayment({
    required double amount,
    String currency = 'USD',
  }) async {
    try {
      final result = await _channel.invokeMethod<Map>(
        'processPayment',
        {'amount': amount, 'currency': currency},
      );
      final map = Map<String, dynamic>.from(result!);
      return PaymentResult(
        transactionId: map['transactionId'] as String,
        status: map['status'] as String,
      );
    } on PlatformException catch (e) {
      throw PaymentException(e.message ?? 'Unknown payment error');
    }
  }
}

class PaymentResult {
  final String transactionId;
  final String status;
  PaymentResult({required this.transactionId, required this.status});
}

class PaymentException implements Exception {
  final String message;
  PaymentException(this.message);
}
```

**ধাপ ৫ — iOS-এর জন্য (Swift) একই bridge আবার লিখুন**, **একই channel name** `com.example.app/payment` দিয়ে।

**ধাপ ৬ — SDK-র যখন native view দরকার: PlatformView।**
কিছু SDK নিজেদের UI নিজেরাই আঁকে (একটা map, একটা secure card field)। সেটা আপনি `AndroidView` / `UiKitView` দিয়ে Flutter widget tree-তে embed করেন।

```dart
Widget build(BuildContext context) {
  if (Platform.isAndroid) {
    return const AndroidView(
      viewType: 'payment-card-input',
      creationParams: {'theme': 'dark'},
      creationParamsCodec: StandardMessageCodec(),
    );
  }
  return const UiKitView(
    viewType: 'payment-card-input',
    creationParams: {'theme': 'dark'},
    creationParamsCodec: StandardMessageCodec(),
  );
}
```

প্রতিটা platform-এ একটা view factory register করুন: Android-এ `PlatformViewFactory` implement করুন; iOS-এ `FlutterPlatformViewFactory` implement করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা বাস্তব কাজের একটা দক্ষতা। অনেক enterprise app মালিকানাধীন SDK ব্যবহার করে, যার কোনো community plugin নেই। তাঁরা দেখতে চান আপনি নিজে সেই ফাঁকটা পূরণ করতে পারেন কি না।

**সাধারণ ভুল:** কোনো channel bridge ছাড়াই Dart থেকে সরাসরি native SDK-র method call করার চেষ্টা করা। আরেকটা ভুল — ভুলে যাওয়া যে SDK-র callback প্রায়ই background thread-এ চলে। `result.success(...)` call করার আগে আপনাকে main thread-এ যেতে হবে (দেখুন [Q2](#q2))। আর যে flow অন্য screen খোলে, তার জন্য `onActivityResult`-এর মতো Activity-lifecycle hook বাদ দিয়ে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"PlatformView-এর খরচ কত?"* → native view embed করা সাধারণ Flutter widget-এর চেয়ে ভারী। তাই SDK-র সত্যিই নিজের view দরকার হলে তবেই ব্যবহার করুন।
- *"এটাকে বারবার ব্যবহার করা যায় এমন কীভাবে বানাবেন?"* → platform-interface pattern দিয়ে একটা plugin-এ মুড়ে দিন। দেখুন [Q9](#q9)।

**সম্পর্কিত:** [Q9 — plugin package](#q9) · [Q2 — threading](#q2) · [Q3 — MethodChannel](#q3)

[↑ উপরে ফিরুন](#toc)

---

# E. Platform-aware Flutter

---

## <a id="q13"></a>13. Flutter-এ platform-specific UI পার্থক্য (adaptive design) কীভাবে handle করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Adaptive design মানে app প্রতিটা platform-এ native মনে হয় — Android-এ Material, iOS-এ Cupertino — কিন্তু logic আর বেশিরভাগ widget tree শেয়ার করা থাকে। আমি platform check করি `Theme.of(context).platform` দিয়ে (`dart:io` দিয়ে নয়, কারণ ওটা web-এ ভেঙে যায়)। আর শুধু সেই অংশগুলোই adapt করি যেগুলো সত্যিই আলাদা, যেমন dialog, switch আর navigation।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Adaptive মানে কী।**
User আশা করেন iOS app-কে iOS-এর মতো লাগবে, আর Android app-কে Android-এর মতো। Adaptive design কয়েকটা মূল widget-কে প্রতিটা platform-এর native চেহারা দেয়। বাকি সব শেয়ার করা থাকে। আপনি দুটো আলাদা app বানাচ্ছেন না।

**ধাপ ২ — উপায় ১: runtime-এ platform check।**

```dart
import 'dart:io' show Platform;

Widget buildButton() {
  if (Platform.isIOS) {
    return CupertinoButton(child: const Text('Tap me'), onPressed: _onTap);
  }
  return ElevatedButton(onPressed: _onTap, child: const Text('Tap me'));
}
```

**ধাপ ৩ — উপায় ২: built-in `.adaptive` constructor (সবচেয়ে সহজ)।**
কয়েকটা সাধারণ widget নিজেরাই adapt হয়ে যায়।

```dart
Switch.adaptive(value: _isOn, onChanged: _toggle);
Slider.adaptive(value: _volume, onChanged: _setVolume);
const CircularProgressIndicator.adaptive();

showAdaptiveDialog(
  context: context,
  builder: (_) => AlertDialog.adaptive(
    title: const Text('Confirm'),
    content: const Text('Are you sure?'),
    actions: [/* adaptive action-গুলো */],
  ),
);
```

**ধাপ ৪ — উপায় ৩: একটা adaptive wrapper widget।**
পার্থক্যটা একবার wrap করুন। তারপর সব জায়গায় ব্যবহার করুন।

```dart
class AdaptiveScaffold extends StatelessWidget {
  final String title;
  final Widget body;
  const AdaptiveScaffold({super.key, required this.title, required this.body});

  @override
  Widget build(BuildContext context) {
    final isIOS = Theme.of(context).platform == TargetPlatform.iOS;
    if (isIOS) {
      return CupertinoPageScaffold(
        navigationBar: CupertinoNavigationBar(middle: Text(title)),
        child: SafeArea(child: body),
      );
    }
    return Scaffold(appBar: AppBar(title: Text(title)), body: body);
  }
}
```

**ধাপ ৫ — উপায় ৪: `Theme.of(context).platform`-কেই বেছে নিন।**
এটাই senior choice। কারণ test আর widget preview-তে এটা override করা যায় (`dart:io Platform` দিয়ে যায় না)।

```dart
Widget build(BuildContext context) {
  switch (Theme.of(context).platform) {
    case TargetPlatform.iOS:
    case TargetPlatform.macOS:
      return _buildCupertinoLayout();
    default:
      return _buildMaterialLayout();
  }
}
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান আপনি একটা codebase দিয়েই দুই platform-এ native অনুভূতি দিতে পারেন কি না। এটা user experience আর app-store review-তে প্রভাব ফেলে।

**সাধারণ ভুল:** সব জায়গায় `dart:io Platform` ব্যবহার করা (এটা web-এ crash করে)। অথবা বেশি adapt করা — প্রতিটা platform-এর জন্য পুরো আলাদা widget tree লেখা, যেটা পুরো উদ্দেশ্যটাই নষ্ট করে। যা সত্যিই আলাদা শুধু সেটাই adapt করুন (navigation, dialog, switch)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`dart:io`-র বদলে `Theme.of(context).platform` কেন?"* → এটা testable, override করা যায়, আর web-এ নিরাপদ।
- *"Platform নয়, screen size-এর ক্ষেত্রে কী?"* → responsive layout-এর জন্য `LayoutBuilder` / `MediaQuery` ব্যবহার করুন; ওটা platform adaptation থেকে আলাদা একটা বিষয়।

**সম্পর্কিত:** [Q14 — permission](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. Flutter-এ permission (camera, location, notification) কীভাবে check আর request করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-08-platform-channel.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Flutter-এ built-in কোনো permission system নেই। তাই আমি একটা unified API-র জন্য `permission_handler` package ব্যবহার করি। Android manifest-এ permission declare করি, আর iOS Info.plist-এ usage-description string যোগ করি। এরপর Dart-এ status check করে request করি — এবং প্রতিটা state handle করি, বিশেষ করে `permanentlyDenied`, যার মানে আমাকে user-কে app settings-এ পাঠাতে হবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Package যোগ করুন।**

```yaml
# pubspec.yaml
dependencies:
  permission_handler: ^11.0.0
```

**ধাপ ২ — দুটো native project-ই configure করুন।**

Android — `android/app/src/main/AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

iOS — `ios/Runner/Info.plist` (description না থাকলে request-এর সময় app **crash** করে):

```xml
<key>NSCameraUsageDescription</key>
<string>We need camera access to take photos.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>We need your location to show nearby stores.</string>
```

**ধাপ ৩ — Check আর request করুন, প্রতিটা state handle করে।**
মূল senior পয়েন্ট হলো সব state handle করা, শুধু `granted` আর `denied` নয়।

```dart
import 'package:permission_handler/permission_handler.dart';

class PermissionService {
  Future<bool> requestCamera() async {
    final status = await Permission.camera.request();

    switch (status) {
      case PermissionStatus.granted:
        return true;
      case PermissionStatus.denied:
        // user না বলেছেন — পরে আবার জিজ্ঞেস করা যাবে
        return false;
      case PermissionStatus.permanentlyDenied:
        // user "don't ask again" বেছেছেন — শুধু Settings থেকেই বদলানো যাবে
        await openAppSettings();
        return false;
      case PermissionStatus.restricted:
        // শুধু iOS — parental control / MDM
        return false;
      case PermissionStatus.limited:
        // iOS 14+ — সীমিত photo access
        return false;
      default:
        return false;
    }
  }

  Future<void> requestMany() async {
    final statuses = await [
      Permission.camera,
      Permission.location,
      Permission.notification,
    ].request();
    statuses.forEach((p, s) => print('$p: $s'));
  }
}
```

**ধাপ ৪ — পুরো flow এক ছবিতে।**

```
  App needs a permission
         |
         v
  +--------------+     already granted?
  | Check status |------ YES --> use the feature
  +------+-------+
         | NO
         v
  +--------------+     user taps Allow?
  |  .request()  |------ YES --> use the feature
  +------+-------+
         | NO
         v
  +-------------------+
  | permanentlyDenied?|-- YES --> openAppSettings()
  +------+------------+
         | NO (just denied)
         v
  show a reason, try again later
```

**ধাপ ৫ — ভালো UX: প্রসঙ্গ অনুযায়ী চান।**
App চালু হওয়ার সময়েই সব permission একসাথে চাইবেন না। ঠিক যখন feature-টা ব্যবহার হচ্ছে তখনই চান (user "take photo" চাপলে camera চান)। আর আগে একটা ছোট কারণ দেখান। এতে accept rate বাড়ে আর ব্যাপারটা সম্মানজনক লাগে।

**Interviewer কেন জিজ্ঞেস করে:** প্রতিটা production app-এ permission লাগে। তাঁরা দেখেন আপনি সব state handle করেন কি না (বিশেষ করে `permanentlyDenied`), আর platform setup-এর পার্থক্য জানেন কি না (iOS usage string বনাম Android manifest)।

**সাধারণ ভুল:** শুধু `granted`/`denied` handle করা আর `permanentlyDenied` বাদ দেওয়া — Android-এ দ্বিতীয়বার deny করার পর dialog আর কখনোই দেখায় না, তাই আপনাকে settings খুলতে হবে। আরেকটা ভুল হলো iOS Info.plist string ভুলে যাওয়া, যেটা সুন্দরভাবে fail না হয়ে app crash করায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Permanently denied permission কীভাবে handle করেন?"* → `permanentlyDenied` ধরুন আর একটা পরিষ্কার message দিয়ে `openAppSettings()` call করুন।
- *"Permission আসলে কোথায় enforce হয়?"* → native side-এ; `permission_handler` Platform Channel দিয়ে সেখানে bridge করে।

**সম্পর্কিত:** [Q13 — adaptive UI](#q13) · [Q1 — channel কী](#q1)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার টেবিলগুলো, তারপর এক লাইনের মনে করিয়ে দেওয়া পয়েন্টগুলো।

## দ্রুত তুলনার টেবিল

**MethodChannel vs EventChannel vs BasicMessageChannel**

| | MethodChannel | EventChannel | BasicMessageChannel |
|---|---|---|---|
| ধরন | request → reply (একবার) | stream (সময়ের সাথে অনেকবার) | যেকোনো ধরনের message |
| দিক | Dart native-কে call করে | native Dart-এ push করে | দুই দিকেই |
| Dart API | `invokeMethod()` | `receiveBroadcastStream()` | `send()` / `setMessageHandler()` |
| Native API | `setMethodCallHandler` | `StreamHandler` | `setMessageHandler` |
| কোন কাজে ভালো | একবার কোনো OS API call করা | sensor, location | custom protocol, সহজ data |

**FFI vs Platform Channels**

| | Platform Channels | Dart FFI |
|---|---|---|
| কার সাথে কথা বলে | Kotlin/Java, Swift/ObjC | C / C++ |
| ধরন | async message | sync সরাসরি call |
| গতি | ভালো (~0.1ms/call) | চমৎকার (~microseconds) |
| Data | codec দিয়ে serialize করা | pointer, struct, raw memory |
| কোন কাজে ভালো | OS API, UI-layer native | crypto, image, audio DSP |

**Channel-এর data type (standard codec)**

| যেগুলো supported | যেগুলো supported নয় |
|---|---|
| `null`, `bool`, `int`, `double` | আপনার নিজের class |
| `String`, `Uint8List` | `DateTime` (string/millis হিসেবে পাঠান) |
| `List`, `Map` | enum (int/string হিসেবে পাঠান) |

**Channel-এর দুই ধরনের error**

| `PlatformException` | `MissingPluginException` |
|---|---|
| native `result.error(...)` পাঠিয়েছে | ওই method name-এর জন্য কোনো handler নেই |
| expected, handle করুন | নাম ভুল, বা `notImplemented` দিতে ভুলে গেছেন |

## এক লাইনের মনে করিয়ে দেওয়া

- একটা **Platform Channel** হলো Dart আর native-এর মধ্যে নাম দেওয়া, async, ডিভাইসের ভেতরের একটা টেলিফোন লাইন — কোনো network নেই। ([Q1](#q1))
- Channel handler চলে **platform main thread**-এ; ভারী কাজ background thread-এ করুন, reply দিন main thread থেকে। ([Q2](#q2))
- **MethodChannel** = এক প্রশ্ন, এক উত্তর; channel-এর নাম হুবহু মেলান আর `notImplemented` handle করুন। ([Q3](#q3))
- **তিন ধরন:** MethodChannel (reply), EventChannel (stream), BasicMessageChannel (free-form)। ([Q4](#q4))
- **EventChannel** = radio broadcast; native `onCancel`-এ producer সবসময় বন্ধ করুন আর Dart subscription cancel করুন। ([Q5](#q5))
- **BasicMessageChannel** = codec সহ দুই দিকের message; ভেতরে এটাই Pigeon-কে চালায়। ([Q6](#q6))
- **Standard codec** primitive, `List`, `Map`, `Uint8List` পাঠাতে পারে — custom object-কে map-এ বদলে নিন। ([Q7](#q7))
- Native error আসে **`PlatformException`** হিসেবে (`code`/`message`/`details`); এটা catch করুন, crash করতে দেবেন না। ([Q7](#q7))
- **FFI** সরাসরি ও synchronously C/C++ call করে; এটা compute-এর জন্য ব্যবহার করুন, Kotlin/Swift OS API-র জন্য নয়। ([Q8](#q8))
- **Plugin** federated pattern ব্যবহার করে: public API → platform interface → MethodChannel implementation। ([Q9](#q9))
- **Pigeon** একটা schema থেকে type-safe Dart/Kotlin/Swift generate করে — কোনো magic string নেই, হাতে cast করাও নেই। ([Q10](#q10))
- **Add-to-app** একটা native app-এর ভেতরে Flutter *module* বসায়; প্রথমবার দ্রুত খোলার জন্য engine আগে থেকে pre-warm করুন। ([Q11](#q11))
- **Plugin নেই এমন SDK**-র জন্য একটা channel bridge লিখুন; SDK-র callback-কে প্রায়ই main thread-এ একটা hop দিতে হয়। ([Q12](#q12))
- **Adaptive UI**: `Theme.of(context).platform` ব্যবহার করুন (web-safe, testable), শুধু যেটা সত্যিই আলাদা সেটাই adapt করুন। ([Q13](#q13))
- **Permission**: প্রতিটা state handle করুন, বিশেষ করে `permanentlyDenied` → `openAppSettings()`; iOS-এ Info.plist-এ string লাগে। ([Q14](#q14))

[↑ উপরে ফিরুন](#toc)

---

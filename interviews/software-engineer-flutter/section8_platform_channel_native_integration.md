# Section 8 — Platform Channels & Native Integration

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

**A. The basics — what a channel is**
1. [What is a Platform Channel and why is it needed?](#q1) · *Very common*
2. [Which thread do channel handlers run on?](#q2) · *Common*

**B. The three channel types**
3. [MethodChannel — call native and get a result (Dart + Kotlin + Swift)](#q3) · *Very common*
4. [MethodChannel vs EventChannel vs BasicMessageChannel](#q4) · *Very common*
5. [EventChannel — continuous streams from native](#q5) · *Very common*
6. [BasicMessageChannel — free-form messages](#q6) · *Common*

**C. Errors, data & types across the bridge**
7. [Codecs and `PlatformException` — passing data and handling errors](#q7) · *Common*

**D. Going native — FFI, plugins, add-to-app**
8. [Dart FFI vs Platform Channels](#q8) · *Common*
9. [Writing a Flutter plugin package](#q9) · *Common*
10. [Pigeon — type-safe channels](#q10) · *Very common*
11. [Add-to-app — embedding Flutter in a native app](#q11) · *Common*
12. [Integrating a native SDK that has no plugin](#q12) · *Common*

**E. Platform-aware Flutter**
13. [Platform-adaptive UI (Material vs Cupertino)](#q13) · *Common*
14. [Checking and requesting permissions](#q14) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 14 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — Core fundamentals (start here).** These come up in almost every interview.
→ [Q1 What is a Platform Channel](#q1) · [Q3 MethodChannel](#q3) · [Q4 The three channel types](#q4) · [Q5 EventChannel](#q5)

**Stage 2 — Errors and data.** How data and failures cross the bridge.
→ [Q7 Codecs & PlatformException](#q7) · [Q2 Which thread](#q2) · [Q6 BasicMessageChannel](#q6)

**Stage 3 — Modern tooling (shows you are up to date).**
→ [Q10 Pigeon](#q10) · [Q9 Plugin package](#q9)

**Stage 4 — Real-world integration.** What seniors actually do on the job.
→ [Q12 Integrating a native SDK](#q12) · [Q11 Add-to-app](#q11) · [Q13 Adaptive UI](#q13) · [Q14 Permissions](#q14)

**Stage 5 — Depth & senior signal (do last).** These separate strong seniors from the rest.
→ [Q8 FFI vs channels](#q8) · then re-read [Q2 threading](#q2) and the [Cheat Sheet](#cheatsheet).

**Short on time (1 hour before the interview)?** Just review these seven:
[Q1](#q1) · [Q3](#q3) · [Q4](#q4) · [Q5](#q5) · [Q7](#q7) · [Q8](#q8) · [Q10](#q10), then read the [Cheat Sheet](#cheatsheet).

---

# A. The basics — what a channel is

---

<a id="q1"></a>
## 1. What is a Platform Channel and why is it needed?

> Very common · Easy–Medium

**Short answer (say this):**
"A Platform Channel is a named phone line between my Dart code and the native code (Kotlin/Java on Android, Swift/Objective-C on iOS). Flutter draws its own screen and runs Dart in its own engine, so it cannot directly touch native things like the camera, Bluetooth, or battery. The channel lets Dart send a message to the native side, the native side does the work, and the answer comes back — all asynchronously."

**Let's understand it fully:**

**Step 1 — Why Flutter needs a bridge at all.**
Flutter does not use the platform's normal UI buttons and views. It paints every pixel itself with its own engine, and your logic runs as Dart inside that engine. This is great for one codebase on both platforms, but it creates a wall: Dart has no built-in way to call `BatteryManager` (Android) or `UIDevice` (iOS). Those live on the native side of the wall.

**Step 2 — The phone-line analogy.**
Think of a Platform Channel as a phone line with a name written on it, like `com.example.app/battery`. Dart picks up the phone and asks a question. The native side, holding a phone with the **same name**, hears the question, does the real work, and replies. If the names don't match, nobody answers.

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

**Step 3 — The three kinds of channel.**
There are three channel types, each for a different shape of talking:

- **MethodChannel** — one question, one answer (request/reply). The most common. See [Q3](#q3).
- **EventChannel** — a continuous broadcast from native to Dart (like sensor data). See [Q5](#q5).
- **BasicMessageChannel** — free-form messages either direction, no "method" idea. See [Q6](#q6).

**Step 4 — It is on-device and asynchronous, not a network call.**
This is important. The message does not go over the internet. It travels inside the app, through the Flutter engine, encoded as compact binary. And every call is asynchronous — you `await` it — so the UI never freezes while native does its work.

```dart
// Check battery level — there is no pure-Dart way to do this
final channel = MethodChannel('com.example.app/battery');
final int level = await channel.invokeMethod('getBatteryLevel');
```

**Step 5 — When you usually don't write channels yourself.**
Most common needs (camera, location, shared preferences) already have plugins on pub.dev. Those plugins use Platform Channels internally. You write a channel yourself only when no plugin exists, or you are building your own plugin.

**Why interviewers ask:** They want to confirm you understand Flutter's architecture wall. If you think Flutter can directly call Android/iOS APIs, that is a basic misunderstanding for a senior.

**Common mistake:** Saying Platform Channels are synchronous, or that they use HTTP. They are asynchronous and on-device — binary messages through the engine, no network.

**Follow-ups they may ask:**
- *"Why must calls be async?"* → Native work may take time, and Dart's single thread must stay free to keep the UI smooth. Async keeps the screen responsive.
- *"What runs on the native side?"* → A handler you register (`setMethodCallHandler` / a `StreamHandler`) that listens on the same channel name.

**Related:** [Q3 — MethodChannel](#q3) · [Q4 — the three channel types](#q4)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. Which thread do Platform Channel handlers run on? How do you do heavy native work?

> Common · Medium

**Short answer (say this):**
"By default, the native channel handler runs on the platform's main (UI) thread. So if I do heavy work right there, I freeze the native UI and delay the reply to Dart. The fix is to move heavy work to a background thread on the native side, then jump back to the main thread only to call `result.success(...)`."

**Let's understand it fully:**

**Step 1 — Two main threads are in play.**
There are two important threads to keep apart:

- **Dart's thread** (the UI isolate) — where your `await invokeMethod(...)` lives. It is never blocked by `await`.
- **The platform main thread** — where the native handler (`onMethodCall` / `handle`) runs by default.

The phone-line message arrives on the platform main thread. That is fine for quick work, but dangerous for slow work.

**Step 2 — Why the default thread can hurt you.**
If your native handler reads a giant file or does heavy decryption right on the main thread, you block native UI rendering and the reply takes a long time to come back to Dart. The Dart side is not frozen, but the user waits and native animations stutter.

**Step 3 — The fix on Android (Kotlin): work on a background thread, reply on main.**
Do the heavy work off the main thread, then post the result back to the main thread before calling `result.success(...)`. Platform channel result callbacks must be called on the main thread.

```kotlin
import android.os.Handler
import android.os.Looper
import java.util.concurrent.Executors

private val executor = Executors.newSingleThreadExecutor()
private val mainHandler = Handler(Looper.getMainLooper())

override fun onMethodCall(call: MethodCall, result: MethodChannel.Result) {
    if (call.method == "processBigFile") {
        executor.execute {
            val output = doHeavyWork()                 // background thread
            mainHandler.post { result.success(output) } // back on main to reply
        }
    } else {
        result.notImplemented()
    }
}
```

**Step 4 — The fix on iOS (Swift): same idea with GCD.**
Use a background queue for the work, then hop back to the main queue to call the `result` callback.

```swift
func handle(_ call: FlutterMethodCall, result: @escaping FlutterResult) {
    if call.method == "processBigFile" {
        DispatchQueue.global(qos: .userInitiated).async {
            let output = self.doHeavyWork()       // background queue
            DispatchQueue.main.async {
                result(output)                    // back on main to reply
            }
        }
    } else {
        result(FlutterMethodNotImplemented)
    }
}
```

**Step 5 — Where to put heavy work on the Dart side.**
If the heavy work is pure Dart (like parsing a huge JSON the native side sent back), don't do it on the UI isolate either. Move it to an isolate with `Isolate.run(...)` or `compute(...)`. So heavy CPU work is always pushed off whichever main thread it would otherwise block.

**Why interviewers ask:** Threading is where real native bugs live. A senior must know channel handlers default to the main thread and that the `result` callback must come back on the main thread.

**Common mistake:** Doing heavy work directly inside the native handler, or calling `result.success(...)` from a background thread. The result callback must be invoked on the platform main thread.

**Follow-ups they may ask:**
- *"Does `await` on the Dart side block the UI?"* → No. `await` only pauses that one function; the Dart UI keeps running.
- *"What if a native SDK calls you back on its own background thread?"* → Capture that result and re-dispatch to the main thread before calling `result.success(...)`.

**Related:** [Q3 — MethodChannel](#q3) · [Q12 — integrating native SDKs](#q12)

[↑ Back to top](#toc)

---

# B. The three channel types

---

<a id="q3"></a>
## 3. How does MethodChannel work? Show calling native code and returning a result (Dart, Kotlin, Swift).

> Very common · Medium — the single most common channel question.

**Short answer (say this):**
"MethodChannel is a request/reply call. Dart calls `invokeMethod` with a method name and optional arguments. The native side registers a handler that matches the method name, does the work, and replies with `result.success(value)` or `result.error(...)`. Both sides must use the exact same channel name string."

**Let's understand it fully:**

**Step 1 — The request/reply idea.**
MethodChannel is like calling a help desk: you say what you want ("getBatteryLevel") and maybe give details (arguments), and they reply with one answer. One call, one reply.

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

**Step 2 — Dart side: call and handle errors.**
Wrap the call in `try/catch` for `PlatformException`, because the native side can reply with an error.

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

**Step 3 — Android side (Kotlin): register a handler with the same name.**
Register inside `configureFlutterEngine`. Match `call.method`, reply with `result.success(...)`, and always handle unknown methods with `result.notImplemented()`.

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

**Step 4 — iOS side (Swift): the same handler in `AppDelegate`.**
Reply with `result(value)`, an error with `FlutterError(...)`, and unknown methods with `FlutterMethodNotImplemented`.

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

**Step 5 — Passing arguments.**
Send a `Map` from Dart; read it by key on the native side.

```dart
await _channel.invokeMethod('setBrightness', {'value': 0.8});
```

```kotlin
"setBrightness" -> {
    val value = call.argument<Double>("value") ?: 1.0
    // use value...
    result.success(null)
}
```

**Why interviewers ask:** This is the bread-and-butter channel skill. They check whether you can wire all three layers correctly, handle errors, and remember the channel name must match exactly.

**Common mistake:** Forgetting `notImplemented()` for unknown methods, using a different channel name on each side, or not wrapping the Dart call in `try/catch` for `PlatformException`.

**Follow-ups they may ask:**
- *"What types can arguments be?"* → Only what the codec supports: `null`, `bool`, `int`, `double`, `String`, `Uint8List`, `List`, `Map`. See [Q7](#q7).
- *"What thread does the handler run on?"* → The platform main thread by default. See [Q2](#q2).

**Related:** [Q4 — the three channel types](#q4) · [Q7 — codecs & errors](#q7) · [Q2 — threading](#q2)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. What is the difference between MethodChannel, EventChannel, and BasicMessageChannel?

> Very common · Medium

**Short answer (say this):**
"All three are phone lines between Dart and native, but they talk in different shapes. MethodChannel is one question and one answer. EventChannel is a continuous broadcast from native to Dart, like a radio station. BasicMessageChannel is free-form messages either direction, with no built-in 'method' idea."

**Let's understand it fully:**

**Step 1 — Three shapes of conversation.**
Picture three ways two people can talk:

- **MethodChannel = a phone call.** You ask one thing, you get one reply, the call ends. ([Q3](#q3))
- **EventChannel = a radio station.** You tune in once, then native keeps broadcasting values to you until you tune out. ([Q5](#q5))
- **BasicMessageChannel = text messages.** Either side can send a message any time; there is no "method name", you decide the format. ([Q6](#q6))

**Step 2 — A quick comparison table.**

| | MethodChannel | EventChannel | BasicMessageChannel |
|---|---|---|---|
| Shape | request → reply (once) | stream (many over time) | free-form messages |
| Direction | Dart calls native | native pushes to Dart | both directions |
| Dart API | `invokeMethod()` | `receiveBroadcastStream()` | `send()` / `setMessageHandler()` |
| Native API | `setMethodCallHandler` | `StreamHandler` (`onListen`/`onCancel`) | `setMessageHandler` |
| Best for | call an OS API once | sensors, location, connectivity | custom protocol, simple data |

**Step 3 — How to choose quickly.**
Ask yourself one question: *how does the data flow?*

- One value when I ask → **MethodChannel**.
- A continuous stream native pushes to me → **EventChannel**.
- Messages flowing both ways with my own format → **BasicMessageChannel**.

**Step 4 — They share the same plumbing.**
Under the hood, all three use the same binary messaging and the same codec family. EventChannel and MethodChannel are really convenient wrappers around the basic messaging that BasicMessageChannel exposes directly.

**Why interviewers ask:** Many candidates only know MethodChannel. Knowing all three — and exactly when to use each — shows real channel depth.

**Common mistake:** Using MethodChannel on a repeating timer (polling) when native already produces a continuous stream. That should be an EventChannel.

**Follow-ups they may ask:**
- *"Which is bidirectional?"* → BasicMessageChannel. MethodChannel is Dart→native (with a reply); EventChannel is native→Dart.
- *"Can native call Dart with MethodChannel?"* → Yes, you can set a handler on the Dart side too, but the common direction is Dart calling native.

**Related:** [Q3 — MethodChannel](#q3) · [Q5 — EventChannel](#q5) · [Q6 — BasicMessageChannel](#q6)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. How does EventChannel work for continuous data streams from native? Give a use case.

> Very common · Medium

**Short answer (say this):**
"EventChannel is a radio broadcast from native to Dart. Dart tunes in by listening to a `Stream`, and native keeps pushing events through an event sink. On the native side I implement a `StreamHandler` with `onListen` (start sending) and `onCancel` (stop and clean up). It is the right choice for sensors, GPS, or connectivity changes."

**Let's understand it fully:**

**Step 1 — Why a stream instead of repeated calls.**
Some data never stops — accelerometer values, location updates, battery state changes. Calling MethodChannel again and again on a timer is wasteful and laggy. EventChannel sets up the line once, and native pushes each new value to Dart as it happens.

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

**Step 2 — Dart side: listen like any stream.**
Call `receiveBroadcastStream()` to get a `Stream`, then map the raw event into a typed shape.

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

// Usage in a widget:
// final sub = AccelerometerService().events.listen((d) {
//   print('x=${d['x']}, y=${d['y']}, z=${d['z']}');
// });
// ... and in dispose(): sub.cancel();
```

**Step 3 — Android side (Kotlin): implement `StreamHandler`.**
`onListen` starts producing (register the sensor listener). `onCancel` stops producing (unregister it). Push each value with `eventSink.success(...)`.

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
        sensorManager.unregisterListener(this) // stop the sensor — saves battery
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

Register it in `configureFlutterEngine`:

```kotlin
EventChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example.app/accelerometer")
    .setStreamHandler(AccelerometerStreamHandler(getSystemService(SENSOR_SERVICE) as SensorManager))
```

**Step 4 — iOS side (Swift): same two callbacks.**
On iOS you implement `FlutterStreamHandler` with `onListen` and `onCancel`, push values with `eventSink(data)`, and return `nil` for no error.

```swift
class AccelerometerStreamHandler: NSObject, FlutterStreamHandler {
    private var eventSink: FlutterEventSink?

    func onListen(withArguments arguments: Any?,
                  eventSink events: @escaping FlutterEventSink) -> FlutterError? {
        eventSink = events
        // start the motion manager, then on each update: eventSink?(["x": x, "y": y, "z": z])
        return nil
    }

    func onCancel(withArguments arguments: Any?) -> FlutterError? {
        // stop the motion manager
        eventSink = nil
        return nil
    }
}
```

**Step 5 — The number one EventChannel bug: not stopping the producer.**
Two cleanups must happen. On Dart, cancel the subscription in `dispose()`. On native, stop the sensor/producer inside `onCancel`. Forgetting `onCancel` keeps the sensor running forever — a battery and memory leak.

**Why interviewers ask:** They test whether you know the difference between one-shot (MethodChannel) and streaming (EventChannel), and whether you clean up the native producer.

**Common mistake:** Polling with MethodChannel instead of using EventChannel, or forgetting to unregister the native listener in `onCancel`, which drains the battery.

**Follow-ups they may ask:**
- *"Single-subscription or broadcast?"* → `receiveBroadcastStream()` gives a broadcast stream, so multiple Dart listeners can attach.
- *"How do you send an error event?"* → `eventSink.error(code, message, details)` on Android; return/pass a `FlutterError` on iOS.

**Related:** [Q4 — the three channel types](#q4) · [Q3 — MethodChannel](#q3)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What is BasicMessageChannel? When would you use it instead of MethodChannel?

> Common · Medium

**Short answer (say this):**
"BasicMessageChannel is the simplest channel — it just sends raw messages back and forth using a codec, with no idea of 'method names'. Both sides can send and receive. I use it when native needs to push messages to Dart freely, when I am sending simple data like a JSON blob, or when I want my own protocol."

**Let's understand it fully:**

**Step 1 — The text-message idea.**
MethodChannel is a structured phone call ("call method X with these arguments"). BasicMessageChannel is plain text messaging: you send a message, the other side gets it and may reply. There is no built-in routing by method name — you decide what the message means.

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

**Step 2 — Pick a codec when you create it.**
The codec decides how the message is encoded:

- `StringCodec` — plain text strings.
- `BinaryCodec` — raw `ByteData`.
- `JSONMessageCodec` — JSON maps/lists.
- `StandardMessageCodec` — Flutter's default binary codec (handles the same types as a MethodChannel).

**Step 3 — Dart side: send and receive.**
You can both `send(...)` a message and set a handler to receive messages from native.

```dart
import 'package:flutter/services.dart';

final channel = BasicMessageChannel<String>(
  'com.example.app/config',
  StringCodec(),
);

// Send a message to native and await its reply
final String? reply = await channel.send('{"action": "getConfig"}');

// Receive messages that native sends to us
channel.setMessageHandler((String? message) async {
  print('Native says: $message');
  return 'acknowledged'; // reply back to native
});
```

**Step 4 — When to choose it over MethodChannel.**
Use BasicMessageChannel when:

1. Native needs to start the conversation often (not just answer Dart).
2. You are exchanging simple data (a config string, a small JSON) and don't need method routing.
3. You want a custom protocol or message format.
4. You are sending large binary data with `BinaryCodec`, and method-call overhead is unwanted.

**Step 5 — It is alive and well (and powers Pigeon).**
It is not deprecated. In fact, Pigeon's generated code uses `BasicMessageChannel` with `StandardMessageCodec` under the hood. See [Q10](#q10).

**Why interviewers ask:** To check you know the full channel spectrum, not just MethodChannel. Knowing when BasicMessageChannel fits shows architectural depth.

**Common mistake:** Saying it is deprecated or useless. It is maintained and is the right tool when you don't need method-call semantics. Also confusing it with EventChannel — BasicMessageChannel is two-way and message-based, not a one-way stream.

**Follow-ups they may ask:**
- *"BasicMessageChannel vs EventChannel?"* → BasicMessageChannel is bidirectional messages; EventChannel is a one-way stream from native to Dart.
- *"Which codec for a config blob?"* → `JSONMessageCodec` or `StringCodec` are both fine.

**Related:** [Q4 — the three channel types](#q4) · [Q10 — Pigeon](#q10)

[↑ Back to top](#toc)

---

# C. Errors, data & types across the bridge

---

<a id="q7"></a>
## 7. What data types can cross a channel? How do you handle errors with `PlatformException`?

> Common · Medium

**Short answer (say this):**
"A codec turns Dart values into bytes and back. The standard codec supports `null`, `bool`, `int`, `double`, `String`, `Uint8List`, `List`, and `Map` — not your custom classes, so I convert those to maps first. For errors, the native side replies with `result.error(code, message, details)`, and Dart receives it as a `PlatformException` I catch with `try/catch`."

**Let's understand it fully:**

**Step 1 — Why a codec exists.**
Dart and native don't share memory, so values must be packed into bytes to cross the line and unpacked on the other side. That packing/unpacking is the **codec**. The default for MethodChannel and EventChannel is `StandardMethodCodec` (built on `StandardMessageCodec`).

**Step 2 — The supported types (memorize this list).**
The standard codec understands these types both ways:

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

Anything outside this list (your own `User` class, a `DateTime`) is **not** supported directly.

**Step 3 — How to send a custom object.**
Convert it to a `Map` before sending, and rebuild it on the other side. Dates usually go as an ISO string or milliseconds.

```dart
// Dart: send a Map, not a User object
await _channel.invokeMethod('saveUser', {
  'id': user.id,
  'name': user.name,
  'createdAt': user.createdAt.toIso8601String(),
});
```

If you want this typing done for you automatically, use Pigeon ([Q10](#q10)).

**Step 4 — Errors: the native side sends a structured failure.**
Instead of crashing, native replies with an error that has three parts: a `code` (a short string), a `message` (human text), and optional `details`.

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

**Step 5 — Dart catches it as a `PlatformException`.**
The three native fields arrive as `e.code`, `e.message`, and `e.details`. You can branch on the code.

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
  // method name not found on native side (often a forgotten notImplemented case)
  showError('This feature is not available on your device.');
}
```

**Step 6 — Two error types to know.**
- **`PlatformException`** → native replied with `result.error(...)`. An expected, handled failure.
- **`MissingPluginException`** → native had no handler for that method name (wrong name, or `notImplemented()`).

**Why interviewers ask:** They want to see you know the type limits (no custom classes) and that you handle failures with structured `PlatformException` instead of letting the app crash.

**Common mistake:** Trying to pass a Dart object straight across the channel, or ignoring `PlatformException` so a native error becomes an unhandled crash.

**Follow-ups they may ask:**
- *"Why does `int` sometimes arrive as `Long`?"* → Large ints map to `Long` on Android; read with `as num` on the Dart side to be safe.
- *"How do you avoid all this manual mapping?"* → Use Pigeon to generate typed classes and serialization. See [Q10](#q10).

**Related:** [Q3 — MethodChannel](#q3) · [Q10 — Pigeon](#q10)

[↑ Back to top](#toc)

---

# D. Going native — FFI, plugins, add-to-app

---

<a id="q8"></a>
## 8. What is Dart FFI (`dart:ffi`)? How does it differ from Platform Channels? When would you use it?

> Common · Medium–Hard

**Short answer (say this):**
"Dart FFI lets Dart call C/C++ functions directly and synchronously, without going through the engine's message system. Platform Channels talk to Kotlin/Swift asynchronously with serialized data; FFI talks to C/C++ with direct, near-instant function calls and raw memory. I use channels for OS APIs, and FFI for heavy computation libraries like crypto, image processing, or SQLite."

**Let's understand it fully:**

**Step 1 — Two different doors to native.**
There are two doors out of Dart:

- **Platform Channels** → a door to **Kotlin/Swift**, async, with data packed by a codec. Great for OS features.
- **Dart FFI** (Foreign Function Interface) → a door to **C/C++**, synchronous, calling the function directly. Great for fast math-heavy libraries.

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

**Step 2 — A side-by-side comparison.**

| Aspect | Platform Channels | Dart FFI |
|---|---|---|
| Target language | Kotlin/Java, Swift/ObjC | C / C++ |
| Communication | Async messages | Sync function calls |
| Speed | Good (~0.1ms per call) | Excellent (~microseconds per call) |
| Data passing | Serialized via codecs | Pointers, structs, raw memory |
| Best for | OS APIs, UI-layer native code | Crypto, image processing, audio DSP |

**Step 3 — A minimal FFI example.**
You declare the C function's shape twice (the native types and the Dart types), open the shared library, look up the function, and call it.

```dart
import 'dart:ffi';
import 'dart:io' show Platform;

// The C signature, described two ways:
typedef NativeAdd = Int32 Function(Int32 a, Int32 b); // native-side types
typedef DartAdd = int Function(int a, int b);          // Dart-side types

void main() {
  final lib = Platform.isAndroid
      ? DynamicLibrary.open('libnative_math.so')
      : DynamicLibrary.process(); // iOS: statically linked

  final add = lib.lookupFunction<NativeAdd, DartAdd>('add_numbers');

  final result = add(3, 7); // synchronous — no await
  print(result); // 10
}
```

The matching C code:

```c
// native_math.c
#include <stdint.h>

int32_t add_numbers(int32_t a, int32_t b) {
    return a + b;
}
```

**Step 4 — When FFI is the right call.**
Reach for FFI when:

- You need many calls per second with tiny latency (audio DSP, physics, parsing).
- You already have a proven C/C++ library to reuse (SQLite, OpenCV, a TensorFlow Lite C API).
- You need a synchronous result.
- You want to share one native codebase across platforms without writing Kotlin and Swift twice.

Tip: use the `ffigen` package to auto-generate the Dart bindings from C headers, so you don't hand-write `typedef`s.

**Step 5 — The big catch: FFI blocks the calling isolate.**
An FFI call is synchronous, so a long C function freezes that isolate. If the work is heavy, run it on a separate isolate (`Isolate.run`). And remember FFI cannot call Kotlin or Swift — only C-ABI code.

**Why interviewers ask:** FFI shows you understand performance trade-offs and can pick the right tool: channels for OS APIs, FFI for compute libraries.

**Common mistake:** Saying FFI replaces Platform Channels. It does not — you can't reach Kotlin/Swift APIs through FFI. Also forgetting that a heavy FFI call blocks the isolate and should run off the UI isolate.

**Follow-ups they may ask:**
- *"How do you pass a string to C?"* → Convert it to a native UTF-8 pointer (e.g. with `package:ffi`'s `toNativeUtf8()`), and free it after.
- *"Channels or FFI for SQLite?"* → FFI (the `sqlite3` package uses FFI). It is a C library and needs fast, synchronous calls.

**Related:** [Q3 — MethodChannel](#q3) · [Q4 — the three channel types](#q4)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. How do you write a simple Flutter plugin package? Describe the structure, pubspec, and platform code.

> Common · Medium

**Short answer (say this):**
"A plugin is a package that bundles platform code (Kotlin/Swift) with a clean Dart API that uses Platform Channels inside. The modern structure has three Dart pieces: a public API class, a platform-interface abstract class, and a MethodChannel implementation. This lets platform implementations be swapped, which is great for tests and web."

**Let's understand it fully:**

**Step 1 — What a plugin is.**
A plugin hides the channel plumbing behind a friendly Dart API. The app just calls `MyPlugin().getDeviceName()` and never sees the channel. Inside, the plugin talks to native through a MethodChannel.

**Step 2 — Create it with the right template.**

```bash
flutter create --template=plugin --platforms=android,ios my_plugin
```

The directory layout:

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

**Step 3 — `pubspec.yaml` declares the native entry points.**

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

**Step 4 — The three Dart files (the federated pattern).**

The platform interface (the contract every platform must satisfy):

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

The MethodChannel implementation (the default real one):

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

The public API (what app developers call):

```dart
// lib/my_plugin.dart
import 'my_plugin_platform_interface.dart';

class MyPlugin {
  Future<String?> getDeviceName() {
    return MyPluginPlatform.instance.getDeviceName();
  }
}
```

**Step 5 — The native implementations.**

Android (`MyPlugin.kt`) — note the clean-up in `onDetachedFromEngine`:

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
        channel.setMethodCallHandler(null) // avoid leaks
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

**Step 6 — Why the three-file split matters.**
Because the public API talks to an interface (not directly to a channel), you can swap in a fake implementation in tests, or a different one for web. This is the "federated plugin" design the Flutter team recommends.

**Why interviewers ask:** Plugin authoring is a key senior skill. They check whether you understand the federated architecture and keep concerns separated.

**Common mistake:** Putting channel calls directly in the public API class and skipping the platform interface. Also forgetting to clear the handler in `onDetachedFromEngine` on Android.

**Follow-ups they may ask:**
- *"How would you support web?"* → Add a web implementation that extends `MyPluginPlatform` and registers itself; the public API doesn't change.
- *"How do you test the Dart side?"* → Swap `MyPluginPlatform.instance` with a fake, or mock the MethodChannel.

**Related:** [Q3 — MethodChannel](#q3) · [Q10 — Pigeon](#q10) · [Q7 — codecs & errors](#q7)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What is Pigeon? How does it improve Platform Channel type safety?

> Very common · Medium

**Short answer (say this):**
"Pigeon is an official Flutter code-generation tool. I write one Dart schema with real types, and Pigeon generates the matching Dart, Kotlin, and Swift code for me. This removes the two biggest channel risks: mistyped method-name strings and manual casting of untyped arguments. Everything becomes compile-time type-safe."

**Let's understand it fully:**

**Step 1 — The problem Pigeon solves.**
Raw channels are stringly-typed. You write `invokeMethod('getUsr', {'id': 42})` and a typo in `'getUsr'` only fails at runtime. The reply is `dynamic`, so you cast by hand and hope. On a big API this is fragile.

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

**Step 2 — Write the schema in Dart.**
You define data classes and an API. `@HostApi()` means native implements it and Dart calls it. `@FlutterApi()` means Dart implements it and native calls it.

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

@HostApi() // Native implements, Dart calls
abstract class UserApi {
  UserResponse getUser(UserRequest request);
}

@FlutterApi() // Dart implements, Native calls
abstract class UserNotificationApi {
  void onUserUpdated(UserResponse user);
}
```

**Step 3 — Run code generation.**

```bash
dart run pigeon \
  --input pigeons/messages.dart \
  --dart_out lib/src/generated/messages.g.dart \
  --kotlin_out android/src/main/kotlin/com/example/Messages.g.kt \
  --swift_out ios/Classes/Messages.g.swift
```

**Step 4 — Implement the generated interface on native.**
Pigeon generates the `UserApi` interface; you just fill in the body.

```kotlin
class UserApiImpl : UserApi {
    override fun getUser(request: UserRequest): UserResponse {
        return UserResponse(name = "Alice", email = "alice@example.com", age = 30)
    }
}

// Register in configureFlutterEngine:
UserApi.setUp(flutterEngine.dartExecutor.binaryMessenger, UserApiImpl())
```

**Step 5 — Call it from Dart, fully typed.**

```dart
final api = UserApi();
final response = await api.getUser(UserRequest(userId: 42));
print(response.name); // "Alice" — typed, no casting, no magic strings
```

**Step 6 — What you gain.**
- Compile-time errors when types don't match.
- No method-name strings to mistype.
- Auto-generated serialization — no manual codec work ([Q7](#q7)).
- `@HostApi` / `@FlutterApi` clearly state the direction.
- Correct null safety in the generated code.

**Why interviewers ask:** Pigeon is officially recommended for non-trivial plugins. They want to see you know the modern tooling and don't hand-roll error-prone channels for complex APIs.

**Common mistake:** Thinking Pigeon is a third-party package (it is by the Flutter team, `package:pigeon`), or thinking it replaces Platform Channels. It generates channel code — the generated code still uses `BasicMessageChannel` with `StandardMessageCodec` underneath ([Q6](#q6)).

**Follow-ups they may ask:**
- *"What does Pigeon use under the hood?"* → `BasicMessageChannel` + `StandardMessageCodec`.
- *"When is raw MethodChannel still fine?"* → For one or two simple methods. Pigeon shines as the API grows.

**Related:** [Q3 — MethodChannel](#q3) · [Q6 — BasicMessageChannel](#q6) · [Q7 — codecs & errors](#q7)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. How do you add a Flutter module to an existing native Android or iOS app (add-to-app)?

> Common · Medium

**Short answer (say this):**
"This is called 'add-to-app'. Instead of a full Flutter app, I create a Flutter module and embed it into the existing native project as a dependency. The native app then launches a `FlutterActivity` (Android) or `FlutterViewController` (iOS) to show the Flutter screen, while the rest of the app stays native."

**Let's understand it fully:**

**Step 1 — Why companies do this.**
Many teams already have a big native app. They don't rewrite everything at once. They add Flutter for one feature first (say, a new checkout screen), prove it works, then expand. That gradual path is add-to-app, and it is common at larger companies.

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

**Step 2 — Create a module (not an app).**

```bash
flutter create --template module my_flutter_module
```

A module has hidden `.android/` and `.ios/` wrappers (used during development) and a `lib/` folder for your Dart code. It does not have the usual full `android/` and `ios/` folders.

**Step 3 — Android: wire it into Gradle.**

In the native app's `settings.gradle`:

```groovy
include ':app'

setBinding(new Binding([gradle: this]))
evaluate(new File(
    settingsDir.parentFile,
    'my_flutter_module/.android/include_flutter.groovy'
))
```

In `app/build.gradle`:

```groovy
dependencies {
    implementation project(':flutter')
}
```

Then launch Flutter from a native Activity:

```kotlin
import io.flutter.embedding.android.FlutterActivity

// Full-screen Flutter
startActivity(FlutterActivity.createDefaultIntent(this))

// Or open at a specific route
startActivity(
    FlutterActivity.withNewEngine().initialRoute("/settings").build(this)
)
```

**Step 4 — iOS: wire it into CocoaPods.**

In the native app's `Podfile`:

```ruby
flutter_application_path = '../my_flutter_module'
load File.join(flutter_application_path, '.ios', 'Flutter', 'podhelper.rb')

target 'MyNativeApp' do
  install_all_flutter_pods(flutter_application_path)
end
```

Run `pod install`, then in Swift:

```swift
import Flutter

let flutterEngine = FlutterEngine(name: "my flutter engine")
flutterEngine.run()

let flutterVC = FlutterViewController(engine: flutterEngine, nibName: nil, bundle: nil)
present(flutterVC, animated: true)
```

**Step 5 — Pre-warm the engine for speed.**
Starting a `FlutterEngine` from cold takes a moment. If the Flutter screen opens often, create and `run()` the engine once at app startup (cache it), then reuse it. This removes the visible delay when the screen first appears.

**Why interviewers ask:** Many companies adopt Flutter incrementally. They want to know you can integrate into a brownfield (existing) app, not only build greenfield ones.

**Common mistake:** Confusing `--template module` with `--template app`. A module has hidden `.android/` and `.ios/` wrappers, not full native folders. Also not pre-warming the engine, causing a visible lag on first open.

**Follow-ups they may ask:**
- *"How does the native side talk to the module?"* → Through Platform Channels, just like a normal app. See [Q3](#q3).
- *"One engine or many?"* → Reuse a cached engine for speed; `FlutterEngineGroup` helps when you need several engines cheaply.

**Related:** [Q3 — MethodChannel](#q3) · [Q12 — integrating native SDKs](#q12)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. How do you integrate a native SDK (e.g. payment, maps) that has no Flutter plugin?

> Common · Medium–Hard

**Short answer (say this):**
"I have two options. For a one-off in one app, I add the native SDK and write Platform Channel bridge code directly in the app. For something reusable, I wrap it in a proper plugin package. If the SDK also needs to show a native view, like a map or a card field, I embed it with a PlatformView (`AndroidView` / `UiKitView`)."

**Let's understand it fully:**

**Step 1 — Pick the strategy.**
Two paths, same core idea (a channel bridge):

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

For a single app, Option A is faster. For reuse across apps, Option B (see [Q9](#q9)).

**Step 2 — Add the native SDK to each platform.**

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

**Step 3 — Write the native bridge (Android shown).**
The bridge receives the Dart call, talks to the SDK, and replies. Notice the SDK's callback may arrive on a background thread — re-dispatch to the main thread before replying (see [Q2](#q2)).

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
                    // SDK callback may be on a background thread:
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

Register it in `MainActivity`:

```kotlin
override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example.app/payment")
        .setMethodCallHandler(PaymentBridge(this))
}
```

**Step 4 — Write the Dart API.**
Keep the channel hidden behind a clean service, map the result into a typed object, and turn `PlatformException` into a domain error.

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

**Step 5 — Repeat the bridge for iOS (Swift)** with the **same channel name** `com.example.app/payment`.

**Step 6 — When the SDK needs a native view: PlatformView.**
Some SDKs render their own UI (a map, a secure card field). You embed it into the Flutter widget tree with `AndroidView` / `UiKitView`.

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

Register a view factory on each platform: on Android implement `PlatformViewFactory`; on iOS implement `FlutterPlatformViewFactory`.

**Why interviewers ask:** This is a practical, real-world skill. Many enterprise apps use proprietary SDKs with no community plugin, and they want to see you can bridge the gap yourself.

**Common mistake:** Trying to call native SDK methods straight from Dart with no channel bridge. Also forgetting that SDK callbacks often run on a background thread — you must hop to the main thread before calling `result.success(...)` (see [Q2](#q2)). And missing Activity-lifecycle hooks like `onActivityResult` for flows that open another screen.

**Follow-ups they may ask:**
- *"PlatformView cost?"* → Embedding native views is heavier than normal Flutter widgets, so use it only when the SDK truly needs its own view.
- *"How would you make this reusable?"* → Wrap it in a plugin with the platform-interface pattern. See [Q9](#q9).

**Related:** [Q9 — plugin package](#q9) · [Q2 — threading](#q2) · [Q3 — MethodChannel](#q3)

[↑ Back to top](#toc)

---

# E. Platform-aware Flutter

---

<a id="q13"></a>
## 13. How do you handle platform-specific UI differences (adaptive design) in Flutter?

> Common · Medium

**Short answer (say this):**
"Adaptive design means the app feels native on each platform — Material on Android, Cupertino on iOS — while sharing the same logic and most of the widget tree. I check the platform with `Theme.of(context).platform` (not `dart:io`, which breaks on web), and I only adapt the parts that genuinely differ, like dialogs, switches, and navigation."

**Let's understand it fully:**

**Step 1 — What adaptive means.**
Users expect iOS apps to feel like iOS and Android apps to feel like Android. Adaptive design gives each platform its native look for a few key widgets, while everything else stays shared. You do not build two whole apps.

**Step 2 — Approach 1: runtime platform check.**

```dart
import 'dart:io' show Platform;

Widget buildButton() {
  if (Platform.isIOS) {
    return CupertinoButton(child: const Text('Tap me'), onPressed: _onTap);
  }
  return ElevatedButton(onPressed: _onTap, child: const Text('Tap me'));
}
```

**Step 3 — Approach 2: built-in `.adaptive` constructors (easiest).**
Several common widgets already adapt themselves.

```dart
Switch.adaptive(value: _isOn, onChanged: _toggle);
Slider.adaptive(value: _volume, onChanged: _setVolume);
const CircularProgressIndicator.adaptive();

showAdaptiveDialog(
  context: context,
  builder: (_) => AlertDialog.adaptive(
    title: const Text('Confirm'),
    content: const Text('Are you sure?'),
    actions: [/* adaptive actions */],
  ),
);
```

**Step 4 — Approach 3: an adaptive wrapper widget.**
Wrap the difference once and reuse it everywhere.

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

**Step 5 — Approach 4: prefer `Theme.of(context).platform`.**
This is the senior choice, because it can be overridden in tests and widget previews (unlike `dart:io Platform`).

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

**Why interviewers ask:** They want to know you can ship one codebase that feels native on both platforms — which affects user experience and app-store reviews.

**Common mistake:** Using `dart:io Platform` everywhere (it crashes on web), or over-adapting by writing entirely separate widget trees per platform, which defeats the point. Adapt only what truly differs (navigation, dialogs, switches).

**Follow-ups they may ask:**
- *"Why `Theme.of(context).platform` over `dart:io`?"* → It is testable, overridable, and web-safe.
- *"What about screen size, not platform?"* → Use `LayoutBuilder` / `MediaQuery` for responsive layout; that is a separate axis from platform adaptation.

**Related:** [Q14 — permissions](#q14)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. How do you check and request permissions (camera, location, notifications) in Flutter?

> Common · Medium

**Short answer (say this):**
"Flutter has no built-in permission system, so I use the `permission_handler` package for a unified API. I declare the permission in the Android manifest and add a usage-description string in the iOS Info.plist, then in Dart I check the status and request it — handling every state, especially `permanentlyDenied`, which means I must send the user to app settings."

**Let's understand it fully:**

**Step 1 — Add the package.**

```yaml
# pubspec.yaml
dependencies:
  permission_handler: ^11.0.0
```

**Step 2 — Configure both native projects.**

Android — `android/app/src/main/AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

iOS — `ios/Runner/Info.plist` (a missing description **crashes** the app on request):

```xml
<key>NSCameraUsageDescription</key>
<string>We need camera access to take photos.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>We need your location to show nearby stores.</string>
```

**Step 3 — Check and request, handling every state.**
The key senior point is handling all states, not just `granted` and `denied`.

```dart
import 'package:permission_handler/permission_handler.dart';

class PermissionService {
  Future<bool> requestCamera() async {
    final status = await Permission.camera.request();

    switch (status) {
      case PermissionStatus.granted:
        return true;
      case PermissionStatus.denied:
        // user said no — you may ask again later
        return false;
      case PermissionStatus.permanentlyDenied:
        // user chose "don't ask again" — only Settings can change it
        await openAppSettings();
        return false;
      case PermissionStatus.restricted:
        // iOS only — parental controls / MDM
        return false;
      case PermissionStatus.limited:
        // iOS 14+ — limited photo access
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

**Step 4 — The flow in one picture.**

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

**Step 5 — Good UX: ask in context.**
Don't blast every permission at launch. Ask right when the feature is used (request camera when the user taps "take photo"), and show a short reason first. This raises the accept rate and feels respectful.

**Why interviewers ask:** Every production app needs permissions. They check that you handle all states (especially `permanentlyDenied`) and know the platform setup differences (iOS usage strings vs Android manifest).

**Common mistake:** Only handling `granted`/`denied` and ignoring `permanentlyDenied` — on Android, after a second denial the dialog never shows again, so you must open settings. Also forgetting iOS Info.plist strings, which crash the app instead of failing gracefully.

**Follow-ups they may ask:**
- *"How do you handle a permanently denied permission?"* → Detect `permanentlyDenied` and call `openAppSettings()` with a clear message.
- *"Where do permissions actually get enforced?"* → On the native side; `permission_handler` bridges to it via Platform Channels.

**Related:** [Q13 — adaptive UI](#q13) · [Q1 — what a channel is](#q1)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**MethodChannel vs EventChannel vs BasicMessageChannel**

| | MethodChannel | EventChannel | BasicMessageChannel |
|---|---|---|---|
| Shape | request → reply (once) | stream (many over time) | free-form messages |
| Direction | Dart calls native | native pushes to Dart | both directions |
| Dart API | `invokeMethod()` | `receiveBroadcastStream()` | `send()` / `setMessageHandler()` |
| Native API | `setMethodCallHandler` | `StreamHandler` | `setMessageHandler` |
| Best for | call an OS API once | sensors, location | custom protocol, simple data |

**FFI vs Platform Channels**

| | Platform Channels | Dart FFI |
|---|---|---|
| Talks to | Kotlin/Java, Swift/ObjC | C / C++ |
| Style | async messages | sync direct calls |
| Speed | good (~0.1ms/call) | excellent (~microseconds) |
| Data | serialized via codec | pointers, structs, raw memory |
| Best for | OS APIs, UI-layer native | crypto, image, audio DSP |

**Channel data types (standard codec)**

| Supported | Not supported |
|---|---|
| `null`, `bool`, `int`, `double` | your own classes |
| `String`, `Uint8List` | `DateTime` (send as string/millis) |
| `List`, `Map` | enums (send as int/string) |

**Two channel error types**

| `PlatformException` | `MissingPluginException` |
|---|---|
| native sent `result.error(...)` | no handler for that method name |
| expected, handle it | wrong name or forgot `notImplemented` |

## One-line reminders

- A **Platform Channel** is a named, async, on-device phone line between Dart and native — no network. ([Q1](#q1))
- Channel handlers run on the **platform main thread**; do heavy work on a background thread, reply on main. ([Q2](#q2))
- **MethodChannel** = one question, one answer; match the channel name exactly and handle `notImplemented`. ([Q3](#q3))
- **Three types:** MethodChannel (reply), EventChannel (stream), BasicMessageChannel (free-form). ([Q4](#q4))
- **EventChannel** = radio broadcast; always stop the producer in native `onCancel` and cancel the Dart subscription. ([Q5](#q5))
- **BasicMessageChannel** = two-way messages with a codec; it powers Pigeon under the hood. ([Q6](#q6))
- The **standard codec** moves primitives, `List`, `Map`, `Uint8List` — convert custom objects to maps. ([Q7](#q7))
- Native errors arrive as **`PlatformException`** (`code`/`message`/`details`); catch it, don't crash. ([Q7](#q7))
- **FFI** calls C/C++ directly and synchronously; use it for compute, not for Kotlin/Swift OS APIs. ([Q8](#q8))
- **Plugins** use the federated pattern: public API → platform interface → MethodChannel implementation. ([Q9](#q9))
- **Pigeon** generates type-safe Dart/Kotlin/Swift from one schema — no magic strings, no manual casts. ([Q10](#q10))
- **Add-to-app** embeds a Flutter *module* into a native app; pre-warm the engine for fast first open. ([Q11](#q11))
- For an **SDK with no plugin**, write a channel bridge; SDK callbacks often need a hop to the main thread. ([Q12](#q12))
- **Adaptive UI**: use `Theme.of(context).platform` (web-safe, testable), adapt only what truly differs. ([Q13](#q13))
- **Permissions**: handle every state, especially `permanentlyDenied` → `openAppSettings()`; iOS needs Info.plist strings. ([Q14](#q14))

[↑ Back to top](#toc)

---

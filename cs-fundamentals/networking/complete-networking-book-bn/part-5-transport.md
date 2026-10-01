# Part 5 — ট্রান্সপোর্ট লেয়ার

> TCP এবং UDP — ইন্টারনেটের দুই স্তম্ভ। একটি নির্ভরযোগ্য, অন্যটি দ্রুত।

---

## অধ্যায় ১৩: TCP — নির্ভরযোগ্য যোগাযোগের বিজ্ঞান

### ১৩.১ TCP কী ও কেন?

**TCP (Transmission Control Protocol)** হলো একটি connection-oriented, reliable প্রোটোকল।

```
TCP-এর গ্যারান্টি:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✅ Delivery:     প্যাকেট পৌঁছাবেই (না পৌঁছালে পুনরায়)
  ✅ Order:        সঠিক ক্রমে পৌঁছাবে
  ✅ Error Check:  নষ্ট ডেটা reject ও পুনরায় আনবে
  ✅ Flow Control: গ্রহীতা সামলাতে পারলে পাঠাবে
  ✅ Congestion:   নেটওয়ার্ক জ্যামে গতি কমাবে

ব্যবহার: HTTP, HTTPS, FTP, SMTP, SSH, Database
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.২ TCP 3-Way Handshake

TCP সংযোগ স্থাপনের আগে তিনটি বার্তা বিনিময় হয়।

```
TCP 3-Way Handshake:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Flutter App (Client)          API Server
        │                            │
        │──── SYN (Seq=100) ────────▶│  "সংযোগ করতে চাই"
        │                            │  Server: ঠিক আছে, প্রস্তুত
        │◀── SYN-ACK (Seq=200,       │
        │         Ack=101) ──────────│  "আমিও প্রস্তুত"
        │                            │
        │──── ACK (Ack=201) ─────────▶│  "বুঝেছি, শুরু করি"
        │                            │
        │═══════════ Data Transfer ══════════│
        │  HTTP GET /users           │
        │──────────────────────────▶│
        │◀────────────────────────── │
        │  HTTP 200 OK + JSON data   │

Flags বোঝা:
  SYN = Synchronize (সংযোগ শুরু)
  ACK = Acknowledgment (পেয়েছি)
  FIN = Finish (সংযোগ শেষ)
  RST = Reset (জরুরি বন্ধ)
  PSH = Push (অবিলম্বে উপরে পাঠাও)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.৩ TCP 4-Way Teardown (সংযোগ বন্ধ)

```
TCP Connection Close:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Client                        Server
    │                              │
    │──── FIN ────────────────────▶│  "আমার পাঠানো শেষ"
    │◀─── ACK ────────────────────│  "বুঝেছি"
    │                              │  (Server এখনো পাঠাতে পারে)
    │◀─── FIN ────────────────────│  "আমারও শেষ"
    │──── ACK ────────────────────▶│  "বুঝেছি"
    │                              │
    [2MSL Wait]                    [CLOSED]
    (TIME_WAIT state)

TIME_WAIT:
  Client 2×MSL (Maximum Segment Lifetime ≈ 60s) অপেক্ষা করে
  কারণ: Server-এর FIN-এ ACK হারিয়ে গেলে Server আবার পাঠাবে

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.৪ Sequence Number ও Acknowledgment

```
TCP Data Transfer:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  পাঠাই: "Hello World" (11 bytes)
  Seq=1000, Data="Hello World"

  Client                          Server
    │── Seq=1000, "Hello " ────────▶│  (6 bytes)
    │◀─ Ack=1006 ──────────────────│  "পেয়েছি, এরপর 1006 থেকে"
    │── Seq=1006, "World" ──────────▶│  (5 bytes)
    │◀─ Ack=1011 ──────────────────│  "সব পেয়েছি"

যদি হারিয়ে যায়:
    │── Seq=1000 ──────────────────▶│
    │   (হারিয়ে গেলো)              │
    │                              │
    [Timeout]
    │── Seq=1000 (পুনরায়) ──────────▶│  Retransmission!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.৫ Flow Control — Sliding Window

```
Sliding Window Protocol:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Receiver window size = 3 segments (বলুক)

  Sender পাঠায় (ACK পাওয়ার আগেই 3টি):
  [Seg 1][Seg 2][Seg 3] ──────────▶ Receiver

  ACK 1 পেলে window সরে:
  [Seg 2][Seg 3][Seg 4] ──────────▶

  Window Size = Receiver কতটুকু buffer করতে পারে

  যদি Receiver ব্যস্ত থাকে:
  Window Size = 0 পাঠায় → Sender থামে (Zero Window)
  পরে window খুললে: Window Update পাঠায়

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.৬ Congestion Control

নেটওয়ার্ক জ্যাম হলে TCP নিজে থেকে গতি কমায়।

```
TCP Congestion Control পর্যায়:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ① Slow Start:
     cwnd (Congestion Window) = 1 MSS থেকে শুরু
     প্রতিটি ACK-এ দ্বিগুণ হয়
     1 → 2 → 4 → 8 → 16 → ... (exponential growth)

  ② Congestion Avoidance (ssthresh পৌঁছালে):
     প্রতি RTT-এ 1 MSS বাড়ে (linear growth)

  ③ Packet Loss হলে:
     Timeout: cwnd = 1 MSS, slow start আবার
     3 Duplicate ACK: cwnd অর্ধেক (Fast Recovery)

  গ্রাফ:
  cwnd ↑
       │     ╭─
       │   ╭─╯ ╲ (timeout)
       │ ╭─╯    ╲  ╭─
       │╱         ╲╱
       └──────────────▶ সময়

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.৭ TCP States — সংযোগের জীবনচক্র

```
TCP State Machine:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  CLOSED ──SYN sent──▶ SYN_SENT ──SYN-ACK received──▶ ESTABLISHED
                                                          │
  CLOSE_WAIT ◀──FIN received──────────────────────────────┘
      │
      └──FIN sent──▶ LAST_ACK ──ACK received──▶ CLOSED

  ESTABLISHED ──FIN sent──▶ FIN_WAIT_1
                               │
                          FIN-ACK received
                               │
                          FIN_WAIT_2 ──FIN received──▶ TIME_WAIT
                                                         │
                                                    2MSL timeout
                                                         │
                                                       CLOSED

গুরুত্বপূর্ণ States:
  ESTABLISHED:  active connection (ডেটা transfer হচ্ছে)
  TIME_WAIT:    সংযোগ শেষ, কিন্তু port এখনো আটকা (~60s)
  CLOSE_WAIT:   Server পাঠানো শেষ করেনি
  SYN_RECEIVED: Server SYN পেয়েছে, SYN-ACK পাঠিয়েছে

netstat -an | grep ESTABLISHED  → active connections দেখুন

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.৮ TCP Segment গঠন

```
TCP Segment Header (20+ bytes):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ┌──────────────────┬──────────────────┐
  │  Source Port     │ Destination Port │  (32 bits)
  ├──────────────────┴──────────────────┤
  │         Sequence Number             │  (32 bits)
  ├─────────────────────────────────────┤
  │       Acknowledgment Number         │  (32 bits)
  ├────────┬────────────────────────────┤
  │ Header │ Flags: URG ACK PSH RST SYN FIN
  │ Length │ Window Size                │  (32 bits)
  ├────────┴────────────────────────────┤
  │  Checksum        │  Urgent Pointer  │  (32 bits)
  ├─────────────────────────────────────┤
  │          Options (variable)         │
  ├─────────────────────────────────────┤
  │              Data                   │
  └─────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৩.৯ Flutter-এ TCP

```dart
// Flutter-এ TCP socket সংযোগ
import 'dart:io';

Future<void> connectToServer() async {
  try {
    // TCP 3-way handshake এখানে হয়
    final socket = await Socket.connect('api.example.com', 80,
      timeout: Duration(seconds: 10),
    );

    // ডেটা পাঠানো
    socket.write('GET / HTTP/1.1\r\nHost: api.example.com\r\n\r\n');

    // ডেটা গ্রহণ
    socket.listen(
      (data) => print(String.fromCharCodes(data)),
      onError: (e) => print('Error: $e'),
      onDone: () {
        socket.destroy(); // TCP FIN পাঠানো হয়
        print('Connection closed');
      },
    );
  } catch (e) {
    // Connection timeout, refused, etc.
    print('Failed to connect: $e');
  }
}

// Dio ব্যবহার করলে TCP internally handle হয়:
final dio = Dio();
// এখানে DNS resolution → TCP connect → TLS handshake → HTTP সব হয়
final response = await dio.get('https://api.example.com/users');
```

---

### ১৩.১০ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  ✅ TCP = Reliable, ordered, connection-oriented       │
│  ✅ 3-way handshake: SYN → SYN-ACK → ACK             │
│  ✅ 4-way teardown: FIN → ACK → FIN → ACK             │
│  ✅ Sliding Window = Flow Control                      │
│  ✅ Congestion Control = Slow Start → CA               │
│  ✅ TIME_WAIT ≈ 60s → port reuse দেরি হয়              │
│  ✅ Dio/http = TCP internally ব্যবহার করে             │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)

---
---

## অধ্যায় ১৪: UDP — দ্রুত কিন্তু অনিশ্চিত

### ১৪.১ UDP কী?

**UDP (User Datagram Protocol)** হলো connectionless, unreliable কিন্তু অত্যন্ত দ্রুত প্রোটোকল।

```
TCP vs UDP তুলনা:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  TCP = রেজিস্টার্ড চিঠি
    • Post Office নিশ্চিত করে পৌঁছানো
    • স্বাক্ষর নেয়, receipt দেয়
    • ধীর কিন্তু নির্ভরযোগ্য

  UDP = সাধারণ পোস্টকার্ড
    • ফেলে দিলেই হয়, নিশ্চিত নেই
    • দ্রুত, ওজন কম
    • হারিয়ে গেলে জানবেও না

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Feature তুলনা:
┌──────────────────────┬────────────────┬────────────────┐
│ Feature              │ TCP            │ UDP            │
├──────────────────────┼────────────────┼────────────────┤
│ Connection           │ Connection-    │ Connectionless │
│                      │ oriented       │                │
│ Reliability          │ Guaranteed     │ No guarantee   │
│ Order                │ Ordered        │ No order       │
│ Speed                │ Slower         │ Faster         │
│ Header size          │ 20+ bytes      │ 8 bytes        │
│ Use case             │ HTTP, FTP, SSH │ DNS, Video, Game│
└──────────────────────┴────────────────┴────────────────┘
```

---

### ১৪.২ UDP কখন ব্যবহার করবেন?

```
UDP উপযুক্ত যখন:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ① Speed > Reliability:
     Video Streaming (Netflix, YouTube):
       একটি ফ্রেম হারালে ঠিক আছে, কিন্তু থামতে পারব না
       পুনরায় পাঠাতে গেলে পুরনো হয়ে যাবে

  ② Real-time:
     VoIP (ফোন কল):
       পুরনো কথা পুনরায় পেয়ে কী করব?
       Delay > Packet loss (better)

  ③ Frequent small queries:
     DNS lookup:
       32 bytes query → 100 bytes response
       TCP handshake করতেই 3 round trip লাগবে!
       UDP = 1 round trip

  ④ Broadcast/Multicast:
     DHCP (IP বরাদ্দ):
       Client-এর IP নেই, তাই Broadcast করতে হয়
       TCP connection-এর আগেই IP দরকার!

  ⑤ Online Gaming:
     Position update প্রতি 20ms:
       হারিয়ে গেলে পরেরটা আসবে
       Re-send-এর latency = game over

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৪.৩ QUIC — UDP-এর উপর HTTP

**QUIC (Quick UDP Internet Connections)** হলো Google-এর তৈরি প্রোটোকল, যা UDP-এর উপর TCP+TLS-এর সুবিধা নিয়ে আসে।

```
HTTP/1.1 (TCP):
  [TCP Handshake: 1 RTT]
  [TLS Handshake: 1-2 RTT]
  [HTTP Request: 1 RTT]
  মোট: 3-4 RTT

HTTP/2 (TCP):
  [TCP+TLS: 2 RTT]
  [HTTP: 1 RTT]
  মোট: 3 RTT (তবে multiplexing আছে)

HTTP/3 (QUIC over UDP):
  [QUIC: 0-1 RTT] ← সব একসাথে!
  [HTTP: 1 RTT]
  মোট: 1-2 RTT

QUIC এর সুবিধা:
  ① 0-RTT reconnection (আগে সংযুক্ত থাকলে)
  ② Head-of-line blocking নেই
  ③ Connection migration (Wi-Fi → 4G-তে সংযোগ অটুট)
  ④ Built-in encryption
  ⑤ Multiplexed streams

Flutter HTTP/3:
  dart:io এ সরাসরি এখনো limited
  Cronet engine দিয়ে HTTP/3 সম্ভব (Android)
```

---

### ১৪.৪ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  ✅ UDP = Connectionless, fast, no guarantee           │
│  ✅ 8 bytes header (TCP = 20+ bytes)                   │
│  ✅ DNS, VoIP, Video, Gaming = UDP                     │
│  ✅ QUIC = UDP + TCP-like reliability + built-in TLS   │
│  ✅ HTTP/3 = QUIC-এর উপর                              │
│  ✅ UDP যেখানে latency > reliability priority          │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)

---
---

## অধ্যায় ১৫: Port ও Socket — যোগাযোগের দরজা

### ১৫.১ Port কী?

একটি সার্ভারে অনেক সার্ভিস চলে। Port সংখ্যা দিয়ে ঠিক কোন সার্ভিস-এ কথা বলছি সেটা জানানো হয়।

```
Port তুলনা:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  IP Address = শহরের ঠিকানা (203.0.113.10)
  Port       = সেই বাড়ির ফ্ল্যাট নম্বর (:80, :443)

  একটি Server:
  IP: 203.0.113.10
  ┌─────────────────────────────────────────┐
  │  Port 80   → HTTP Server               │
  │  Port 443  → HTTPS Server              │
  │  Port 22   → SSH Server                │
  │  Port 3306 → MySQL Database            │
  │  Port 8080 → Development Server        │
  └─────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৫.২ Port-এর শ্রেণীবিভাগ

```
Port Ranges:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  0 – 1023:     Well-known Ports (IANA নিয়ন্ত্রিত)
                Root/Admin ছাড়া ব্যবহার করা যায় না

  1024 – 49151: Registered Ports
                Application-specific

  49152 – 65535: Ephemeral (Dynamic) Ports
                Client-side temporary ports

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
গুরুত্বপূর্ণ Well-known Ports:
┌──────┬──────────┬────────────────────────────────────┐
│ Port │ Protocol │ ব্যবহার                            │
├──────┼──────────┼────────────────────────────────────┤
│  20  │ FTP      │ FTP Data transfer                  │
│  21  │ FTP      │ FTP Control                        │
│  22  │ SSH      │ Secure Shell                       │
│  23  │ Telnet   │ Unsecure remote (avoid!)           │
│  25  │ SMTP     │ Email sending                      │
│  53  │ DNS      │ Domain Name System (UDP+TCP)       │
│  67  │ DHCP     │ DHCP Server                        │
│  68  │ DHCP     │ DHCP Client                        │
│  80  │ HTTP     │ Web                                │
│ 110  │ POP3     │ Email receive                      │
│ 143  │ IMAP     │ Email manage                       │
│ 443  │ HTTPS    │ Secure Web                         │
│ 587  │ SMTP     │ Email submission (TLS)             │
│ 993  │ IMAPS    │ Secure IMAP                        │
│ 995  │ POP3S    │ Secure POP3                        │
│3306  │ MySQL    │ MySQL Database                     │
│5432  │PostgreSQL│ PostgreSQL                         │
│5672  │ AMQP     │ RabbitMQ                           │
│6379  │ Redis    │ Redis Cache                        │
│9092  │ Kafka    │ Kafka Message Queue                │
│27017 │ MongoDB  │ MongoDB                            │
└──────┴──────────┴────────────────────────────────────┘
```

---

### ১৫.৩ Socket — সংযোগের সম্পূর্ণ ঠিকানা

**Socket = IP Address + Port Number + Protocol**

```
Socket Pair (একটি সংযোগের দুই পাশ):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Client Socket:  192.168.1.5:54321  (ephemeral port)
  Server Socket:  93.184.216.34:443  (well-known port)

  একটি সংযোগ = (Src IP, Src Port, Dst IP, Dst Port, Protocol)

  একই Client, বিভিন্ন সংযোগ:
  192.168.1.5:54321 → 93.184.216.34:443 (Google)
  192.168.1.5:54322 → 13.107.4.50:443  (Microsoft)
  192.168.1.5:54323 → 93.184.216.34:443 (Google আরেকটি)

  প্রতিটি সংযোগ আলাদা! (port number আলাদা)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ১৫.৪ Socket Programming — মূল ধারণা

```
Server Socket Life Cycle:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  1. socket()    → Socket তৈরি করো
  2. bind()      → Port-এ বাঁধো (port 8080)
  3. listen()    → সংযোগের জন্য অপেক্ষা করো
  4. accept()    → Client-এর সংযোগ গ্রহণ করো
  5. recv/send() → ডেটা আদান-প্রদান
  6. close()     → সংযোগ বন্ধ

Client Socket Life Cycle:
  1. socket()    → Socket তৈরি করো
  2. connect()   → Server-এ সংযোগ করো (3-way handshake)
  3. send/recv() → ডেটা আদান-প্রদান
  4. close()     → সংযোগ বন্ধ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```dart
// Flutter/Dart-এ TCP Server Socket
import 'dart:io';

Future<void> startServer() async {
  final server = await ServerSocket.bind('0.0.0.0', 8080);
  print('Server listening on port 8080');

  await for (final socket in server) {
    print('Client: ${socket.remoteAddress}:${socket.remotePort}');
    socket.listen(
      (data) {
        final message = String.fromCharCodes(data);
        socket.write('Echo: $message');
      },
      onDone: () => socket.close(),
    );
  }
}

// TCP Client
Future<void> connectToServer() async {
  final socket = await Socket.connect('localhost', 8080);
  socket.write('Hello Server!');
  socket.listen((data) => print(String.fromCharCodes(data)));
}
```

---

### ১৫.৫ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  ✅ Port = 0-65535; Well-known = 0-1023                │
│  ✅ HTTP=80, HTTPS=443, SSH=22, DNS=53                 │
│  ✅ Socket = IP + Port + Protocol (সংযোগের ঠিকানা)    │
│  ✅ Ephemeral Port = Client-এর temporary port          │
│  ✅ একটি সংযোগ = (Src IP, Src Port, Dst IP, Dst Port) │
│  ✅ MySQL=3306, Redis=6379, MongoDB=27017              │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)
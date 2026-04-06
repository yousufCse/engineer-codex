cat > /home/claude/book_part3.md << 'ENDOFPART3'
---

# Part 3 — ফিজিক্যাল ও ডেটা লিংক লেয়ার

> এখানে নেটওয়ার্কিং আক্ষরিক অর্থে মাটিতে নেমে আসে — তার, আলো, রেডিও তরঙ্গ।

---

## অধ্যায় ৬: ফিজিক্যাল মিডিয়া ও সিগন্যাল ট্রান্সমিশন

### ৬.১ তিনটি প্রধান মাধ্যম

```
নেটওয়ার্কিং মাধ্যমের তুলনা:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ① Copper Wire (তামার তার)
     ├── ধরন: Coaxial, Twisted Pair (UTP/STP)
     ├── গতি: 10 Mbps – 10 Gbps
     ├── দূরত্ব: সর্বোচ্চ 100 মিটার (Ethernet)
     ├── সুবিধা: সস্তা, সহজ installation
     └── অসুবিধা: EMI (electromagnetic interference)-এ প্রভাবিত

  ② Fiber Optic (আলোর তার)
     ├── ধরন: Single-mode, Multi-mode
     ├── গতি: 10 Gbps – 100 Tbps
     ├── দূরত্ব: 10 km – 10,000 km
     ├── সুবিধা: অত্যন্ত দ্রুত, EMI প্রভাব নেই
     └── অসুবিধা: ব্যয়বহুল, নাজুক

  ③ Wireless (বেতার)
     ├── ধরন: Wi-Fi, Bluetooth, 4G/5G, Satellite
     ├── গতি: 1 Mbps – 9.6 Gbps (Wi-Fi 6)
     ├── দূরত্ব: কয়েক মিটার – হাজার কিমি (Satellite)
     ├── সুবিধা: তার ছাড়া, নমনীয়
     └── অসুবিধা: নিরাপত্তা ঝুঁকি, interference

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ৬.২ Twisted Pair Cable — অফিসের তার

```
UTP (Unshielded Twisted Pair) ক্যাবলের ভেতরে:

  ┌────────────────────────────────────────────────┐
  │                                                │
  │   ╔══╗  ╔══╗  ╔══╗  ╔══╗   8টি তার           │
  │   ║  ║  ║  ║  ║  ║  ║  ║   (4 জোড়া)         │
  │   ╚══╝  ╚══╝  ╚══╝  ╚══╝                      │
  │  কমলা  নীল   সবুজ  বাদামি                     │
  │                                                │
  │  প্রতি জোড়া পেঁচানো → EMI কমায়              │
  └────────────────────────────────────────────────┘

Cat cable তুলনা:
┌──────────┬──────────────┬───────────────────────┐
│ Category │ সর্বোচ্চ গতি │ ব্যবহার               │
├──────────┼──────────────┼───────────────────────┤
│ Cat 5e   │ 1 Gbps       │ পুরনো অফিস, বাড়ি      │
│ Cat 6    │ 10 Gbps      │ আধুনিক অফিস           │
│ Cat 6a   │ 10 Gbps (55m)│ ডেটাসেন্টার           │
│ Cat 7    │ 10 Gbps      │ হাই-পারফরম্যান্স       │
│ Cat 8    │ 40 Gbps      │ ডেটাসেন্টার backbone  │
└──────────┴──────────────┴───────────────────────┘
```

---

### ৬.৩ Fiber Optic — আলোর গতিতে ডেটা

```
Fiber Optic কিভাবে কাজ করে:

  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │  LED/Laser ─→ ╔══════════════════════╗ ─→ Photo  │
  │  (আলো)        ║   Glass Core         ║   Detector│
  │  0/1 signal   ║ (পূর্ণ অভ্যন্তরীণ  ║   (0/1)   │
  │               ║  প্রতিফলন)          ║           │
  │               ╚══════════════════════╝           │
  │               └── Cladding (বাইরের স্তর) ──┘    │
  │                                                  │
  │  আলো সরল রেখায় চললে প্রতিফলিত হয়              │
  │  তাই তার বাঁক নিতে পারে!                        │
  └──────────────────────────────────────────────────┘

Single-mode vs Multi-mode:
  Single-mode: একটি আলোর পথ → দীর্ঘ দূরত্ব (10+ km)
  Multi-mode:  একাধিক পথ → কম দূরত্ব (< 2 km), বেশি গতি
```

**বাংলাদেশে Fiber:**
- BTCL-এর FTTH (Fiber to the Home) সংযোগ
- সমুদ্রের তলায় SEA-ME-WE 4/5 ক্যাবল
- BDIX-এর backbone fiber

---

### ৬.৪ Wi-Fi — বায়ুতে ডেটা

```
Wi-Fi কিভাবে কাজ করে:

  রাউটার             ফোন
  ┌─────┐            ┌─────┐
  │  📡 │~~~waves~~~~│ 📱 │
  │     │            │     │
  └─────┘            └─────┘
  2.4/5/6 GHz রেডিও তরঙ্গে ডেটা পাঠায়

CSMA/CA (Collision Avoidance):
Wi-Fi-তে একসাথে দুজন পাঠালে collision হয়।
তাই Wi-Fi আগে শোনে:
  • Channel ফাঁকা? → পাঠাও
  • ব্যস্ত? → র‍্যান্ডম সময় অপেক্ষা করো, আবার চেষ্টা

Wi-Fi Channel:
  2.4 GHz: 13টি channel, কিন্তু শুধু 1, 6, 11 non-overlapping
  5 GHz:   24+ non-overlapping channel → কম interference
```

---

### ৬.৫ 4G/5G — মোবাইল নেটওয়ার্ক

```
4G LTE আর্কিটেকচার:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  আপনার Phone
       │ Radio Wave (700 MHz – 2600 MHz)
  ┌────┴────┐
  │  eNodeB │  ← Cell Tower (বেস স্টেশন)
  └────┬────┘
       │ Fiber
  ┌────┴────┐
  │  EPC    │  ← Core Network (MME, SGW, PGW)
  └────┬────┘
       │
  ইন্টারনেট

5G:
  • আরও বেশি frequency (mmWave: 24-100 GHz)
  • 10x দ্রুত (1-10 Gbps)
  • Ultra-low latency (< 1 ms)
  • IoT devices সাপোর্ট (লক্ষ device/km²)
  • কিন্তু পরিধি কম, দেওয়াল ভেদ করতে পারে না

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flutter-এ নেটওয়ার্ক ধরন detect করা:
  import 'package:connectivity_plus/connectivity_plus.dart';
  final result = await Connectivity().checkConnectivity();
  if (result == ConnectivityResult.mobile) { ... }
  if (result == ConnectivityResult.wifi)   { ... }
```

---

### ৬.৬ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  ✅ Copper = সস্তা, সর্বোচ্চ 100m, 10Gbps            │
│  ✅ Fiber = দ্রুত, দূরপাল্লা, EMI-মুক্ত              │
│  ✅ Wi-Fi = CSMA/CA, 2.4GHz=পরিধি, 5GHz=গতি          │
│  ✅ 5G = Ultra-low latency, mmWave = কম পরিধি         │
│  ✅ Cat 6 = আধুনিক অফিসের জন্য যথেষ্ট                │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)

---
---

## অধ্যায় ৭: MAC Address ও Ethernet ফ্রেম

### ৭.১ MAC Address — হার্ডওয়্যারের পরিচয়

**MAC (Media Access Control) Address** হলো প্রতিটি নেটওয়ার্ক ডিভাইসের অনন্য শনাক্তকারী — এটি NIC (Network Interface Card)-এ hardcoded থাকে।

```
MAC Address গঠন:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  2C : 54 : 91 : 88 : C9 : E3
  │           │   │           │
  └── OUI ───┘   └── Device ─┘
  (3 bytes)        (3 bytes)
  Organizationally  ওই কোম্পানির
  Unique Identifier  নির্দিষ্ট ডিভাইস

  OUI থেকে জানা যায়:
  2C:54:91 → Apple Inc.
  00:1A:2B → Cisco Systems
  B8:27:EB → Raspberry Pi Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
বিশেষ MAC:
  FF:FF:FF:FF:FF:FF → Broadcast (সবাইকে পাঠাও)
  01:xx:xx:xx:xx:xx → Multicast
  00:00:00:00:00:00→ Invalid/Unset
```

**MAC vs IP:**

| বৈশিষ্ট্য | MAC Address | IP Address |
|-----------|-------------|-----------|
| স্তর | Layer 2 | Layer 3 |
| পরিবর্তন | সাধারণত স্থায়ী | গতিশীল (DHCP) |
| ব্যবহার | একই নেটওয়ার্কে | বিভিন্ন নেটওয়ার্কে |
| উদাহরণ | 2C:54:91:88:C9:E3 | 192.168.1.5 |

---

### ৭.২ ARP — IP থেকে MAC আবিষ্কার

আপনার ফোন 192.168.1.1 (Router)-এ পাঠাতে চায়, কিন্তু MAC জানে না। **ARP (Address Resolution Protocol)** এই সমস্যা সমাধান করে।

```
ARP প্রক্রিয়া:

  ┌──────────┐                              ┌──────────┐
  │  Phone   │                              │  Router  │
  │192.168.1.5│                             │192.168.1.1│
  │ MAC: AA  │                              │ MAC: BB  │
  └──────────┘                              └──────────┘
       │                                         │
       │──ARP Request (Broadcast)──────────────▶│
       │  "192.168.1.1-এর MAC কে জানে?"         │
       │  Dst MAC: FF:FF:FF:FF:FF:FF (সবাইকে)   │
       │                                         │
       │◀─ARP Reply (Unicast)───────────────────│
       │  "আমি! আমার MAC = BB:BB:BB:BB:BB:BB"   │
       │                                         │
       │  [ARP Cache-এ সংরক্ষণ করলো]            │
       │  192.168.1.1 → BB:BB:BB:BB:BB:BB        │
       │  (কিছুক্ষণ মনে রাখবে)                  │
```

**ARP Cache দেখুন:**
```bash
# Windows
arp -a

# Linux/Mac
arp -n

# Output example:
# 192.168.1.1   d4:3d:7e:aa:bb:cc  dynamic
# 192.168.1.102 2c:54:91:11:22:33  dynamic
```

---

### ৭.৩ Ethernet Frame গঠন

```
Ethernet II Frame (IEEE 802.3):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌────────┬──────┬──────┬───────────┬──────────┬─────┐
  │Preamble│Dst   │Src   │EtherType/ │ Payload  │ FCS │
  │        │MAC   │MAC   │Length     │ (Data)   │     │
  │8 bytes │6 bytes│6 bytes│2 bytes  │46-1500B  │4B   │
  └────────┴──────┴──────┴───────────┴──────────┴─────┘

  Preamble (8 bytes): 10101010...10101011
    → Receiver কে সতর্ক করে: "ডেটা আসছে!"
    → Synchronization

  Destination MAC: কে পাবে
  Source MAC:      কে পাঠিয়েছে

  EtherType: কোন Layer-3 Protocol?
    0x0800 → IPv4
    0x0806 → ARP
    0x86DD → IPv6
    0x8100 → VLAN tagged (802.1Q)

  Payload: আসল ডেটা (46–1500 bytes)
    ← MTU (Maximum Transmission Unit) = 1500 bytes

  FCS (Frame Check Sequence): Error detection (CRC-32)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**MTU ও Fragmentation:**
```
MTU = 1500 bytes মানে একটি Frame-এ সর্বোচ্চ 1500 bytes payload।
যদি IP packet > 1500 bytes হয়, তাহলে ভাগ করতে হয়।

উদাহরণ: 4000 bytes প্যাকেট:
  Fragment 1: 1480 bytes (+ 20 bytes IP header = 1500)
  Fragment 2: 1480 bytes
  Fragment 3: 1040 bytes

সমস্যা: Fragmentation = performance কমে
সমাধান: Path MTU Discovery — সর্বোচ্চ MTU খুঁজে নেওয়া
```

---

### ৭.৪ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  ✅ MAC = Hardware ID (6 bytes, hex)                   │
│  ✅ OUI = প্রথম 3 bytes (manufacturer)                │
│  ✅ ARP = IP → MAC mapping (broadcast করে জিজ্ঞেস)   │
│  ✅ ARP Cache = temporary MAC table                    │
│  ✅ Ethernet Frame = Preamble+MAC+Type+Data+FCS       │
│  ✅ MTU = 1500 bytes (বড় হলে fragment হয়)            │
│  ✅ FF:FF:FF:FF:FF:FF = Broadcast MAC                 │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)

---
---

## অধ্যায় ৮: Switch, Hub ও VLAN

### ৮.১ Hub vs Switch — পার্থক্য বোঝা

```
Hub (পুরনো, এখন প্রায় অব্যবহৃত):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  PC-A → Hub → PC-B, PC-C, PC-D সবাই পায়!
  (Broadcast domain = সব port)

  [PC-A]──┐
  [PC-B]──┤  [HUB]  ← সবাইকে কপি পাঠায়
  [PC-C]──┤
  [PC-D]──┘

  সমস্যা:
  • Collision: দুজন একসাথে পাঠালে ঝামেলা
  • Privacy: সবাই সবার ডেটা দেখে
  • Bandwidth ভাগ হয়ে যায়

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Switch (আধুনিক, বুদ্ধিমান):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  PC-A → Switch → শুধু PC-B (MAC table দেখে)

  [PC-A]──┐
  [PC-B]──┤  [Switch]  ← শুধু সঠিক port-এ পাঠায়
  [PC-C]──┤  MAC Table
  [PC-D]──┘  Port 1: PC-A (AA:AA)
             Port 2: PC-B (BB:BB)
             Port 3: PC-C (CC:CC)

  সুবিধা:
  • No collision (প্রতিটি port আলাদা Collision Domain)
  • Privacy (শুধু প্রাপক দেখে)
  • পূর্ণ Bandwidth প্রতিটি connection-এ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ৮.২ Switch কিভাবে MAC Table তৈরি করে

```
MAC Table Learning Process:

Step 1: শুরুতে MAC Table ফাঁকা
  MAC Table: (Empty)

Step 2: PC-A (port 1) থেকে PC-B-তে Frame আসলো
  Switch: "Port 1 থেকে এলো, Source MAC = AA → সংরক্ষণ"
  MAC Table:
  ┌──────────────┬──────┐
  │ MAC Address  │ Port │
  ├──────────────┼──────┤
  │ AA:AA:AA:AA  │  1   │
  └──────────────┴──────┘
  PC-B-এর MAC জানে না → সব port-এ flood করে (BB ছাড়া)

Step 3: PC-B reply দিলো
  MAC Table:
  ┌──────────────┬──────┐
  │ AA:AA:AA:AA  │  1   │
  │ BB:BB:BB:BB  │  2   │
  └──────────────┴──────┘

Step 4: পরের বার PC-A → PC-B পাঠালে
  Switch: MAC Table দেখে → সরাসরি Port 2-এ পাঠায়
  (আর flood করে না)
```

---

### ৮.৩ VLAN — একটি Switch-এ একাধিক নেটওয়ার্ক

**VLAN (Virtual Local Area Network)** একটি Physical Switch-কে একাধিক Virtual Switch-এ ভাগ করে।

```
একটি কোম্পানির ৩টি বিভাগ, কিন্তু একটি Switch:

  ┌───────────────────────────────────────────────┐
  │               Physical Switch                 │
  │  ┌──────────┐ ┌──────────┐ ┌──────────┐      │
  │  │ VLAN 10  │ │ VLAN 20  │ │ VLAN 30  │      │
  │  │ HR Dept  │ │ IT Dept  │ │ Finance  │      │
  │  │Port 1,2  │ │Port 3,4  │ │Port 5,6  │      │
  │  └──────────┘ └──────────┘ └──────────┘      │
  └───────────────────────────────────────────────┘

VLAN-এর সুবিধা:
  • বিভিন্ন বিভাগ আলাদা — HR Finance-এর ডেটা দেখতে পারে না
  • Broadcast traffic কমে (প্রতিটি VLAN-এ আলাদা)
  • নিরাপত্তা বাড়ে
  • কম খরচে নেটওয়ার্ক বিভাজন
```

**VLAN Tagging (802.1Q):**
```
VLAN Tag যোগ করা হয় Ethernet Frame-এ:

  ┌──────┬──────┬────────┬──────────┬──────┬─────┐
  │Dst   │Src   │ 8100   │ VLAN ID  │Type  │Data │
  │MAC   │MAC   │(tag)   │(1-4094)  │      │     │
  └──────┴──────┴────────┴──────────┴──────┴─────┘
                 ↑──── 802.1Q Tag (4 bytes) ────↑

Switch ports দুই ধরনের:
  Access Port: একটি VLAN-এর জন্য (PC সংযোগ)
  Trunk Port:  সব VLAN-এর ট্র্যাফিক বহন করে (Switch-to-Switch)
```

---

### ৮.৪ STP — Spanning Tree Protocol

একটি নেটওয়ার্কে যদি loop থাকে, Broadcast storm হয় — নেটওয়ার্ক ডাউন হয়ে যায়।

```
Loop সমস্যা:
  Switch A ──── Switch B
      │              │
      └──── Switch C ┘

এই loop-এ একটি Broadcast:
  A → B → C → A → B → C → ... (অসীম!)

STP সমাধান:
  ① Root Bridge নির্বাচন (সবচেয়ে ছোট Bridge ID)
  ② Redundant link block করে রাখে
  ③ Primary link বিকল হলে blocked link চালু হয়

  Switch A ──── Switch B
      │              X  ← Blocked
      └──── Switch C

  Network চলে! Bridge ভাঙলে:
  Switch A ──── Switch B
      │              │  ← এখন চালু হয়
      └──── Switch C
```

---

### ৮.৫ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  ✅ Hub = সবাইকে ডেটা পাঠায় (Collision Domain ১টি)   │
│  ✅ Switch = MAC Table দেখে সঠিক port-এ পাঠায়        │
│  ✅ MAC Table = MAC + Port mapping (শিখে নেয়)         │
│  ✅ VLAN = একটি switch-এ একাধিক virtual network       │
│  ✅ Trunk Port = একাধিক VLAN বহন করে (switch-switch) │
│  ✅ STP = Loop প্রতিরোধ করে, redundancy দেয়          │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)

---
ENDOFPART3
echo "Part 3 done: $(wc -l < /home/claude/book_part3.md) lines"
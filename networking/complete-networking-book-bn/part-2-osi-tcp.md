cat > /home/claude/book_part2.md << 'ENDOFPART2'
---
---

# Part 2 — নেটওয়ার্ক মডেল

> নেটওয়ার্কিং এত জটিল বিষয় যে এটিকে স্তরে স্তরে ভাগ করা হয়েছে। OSI ও TCP/IP মডেল সেই কাঠামো।

---

## অধ্যায় ৪: OSI মডেল — নেটওয়ার্কিংয়ের মানচিত্র

### ৪.১ OSI মডেল কেন দরকার হলো?

১৯৭০-এর দশকে বিভিন্ন কোম্পানির নেটওয়ার্ক সরঞ্জাম পরস্পরের সাথে কাজ করত না। IBM-এর কম্পিউটার Cisco-র রাউটারের সাথে কথা বলত না। ISO (International Organization for Standardization) ১৯৮৪ সালে **OSI (Open Systems Interconnection)** মডেল প্রকাশ করে — একটি সার্বজনীন কাঠামো।

```
OSI মডেলের ৭টি লেয়ার:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ┌─────────────────────────────────────────────────┐
  │   7. Application Layer   (অ্যাপ্লিকেশন)         │  ← ব্যবহারকারীর সবচেয়ে কাছে
  ├─────────────────────────────────────────────────┤
  │   6. Presentation Layer  (উপস্থাপনা)            │
  ├─────────────────────────────────────────────────┤
  │   5. Session Layer       (সেশন)                 │
  ├─────────────────────────────────────────────────┤
  │   4. Transport Layer     (পরিবহন)               │
  ├─────────────────────────────────────────────────┤
  │   3. Network Layer       (নেটওয়ার্ক)            │
  ├─────────────────────────────────────────────────┤
  │   2. Data Link Layer     (ডেটা লিংক)            │
  ├─────────────────────────────────────────────────┤
  │   1. Physical Layer      (ফিজিক্যাল)            │  ← হার্ডওয়্যারের সবচেয়ে কাছে
  └─────────────────────────────────────────────────┘

মনে রাখার কৌশল (উপর থেকে নিচে):
"All People Seem To Need Data Processing"
 A    P    S    T   N    D    P
App Pres Ses Trans Net Data Phys
```

---

### ৪.২ প্রতিটি লেয়ারের বিস্তারিত বর্ণনা

#### Layer 7 — Application Layer (অ্যাপ্লিকেশন লেয়ার)

```
কাজ: ব্যবহারকারীর অ্যাপ্লিকেশন এবং নেটওয়ার্কের মধ্যে সেতু

  ব্যবহারকারী
      │
  ┌───┴─────────────────────────────────────────────┐
  │  Application Layer                              │
  │  • HTTP/HTTPS  (ওয়েব ব্রাউজিং)                │
  │  • SMTP/IMAP   (ইমেইল)                          │
  │  • FTP         (ফাইল ট্রান্সফার)               │
  │  • DNS         (নাম রেজোলিউশন)                 │
  │  • SSH         (রিমোট অ্যাক্সেস)               │
  │  • WebSocket   (রিয়েল-টাইম যোগাযোগ)           │
  └─────────────────────────────────────────────────┘

Data Unit: Message / Data
Flutter উদাহরণ: Dio দিয়ে HTTP GET request করা
```

#### Layer 6 — Presentation Layer (প্রেজেন্টেশন লেয়ার)

```
কাজ: ডেটা ফরম্যাট রূপান্তর, এনক্রিপশন, কম্প্রেশন

  ┌─────────────────────────────────────────────────┐
  │  Presentation Layer                             │
  │                                                 │
  │  Encoding/Decoding:                             │
  │    "Hello" → 48 65 6C 6C 6F (ASCII→Hex)        │
  │                                                 │
  │  Compression:                                   │
  │    1000 bytes → gzip → 300 bytes               │
  │                                                 │
  │  Encryption/Decryption:                         │
  │    plaintext → TLS → ciphertext                │
  │                                                 │
  │  Format: JSON, XML, JPEG, MP4, PDF             │
  └─────────────────────────────────────────────────┘

Data Unit: Encoded/Encrypted Data
Flutter উদাহরণ: JSON serialize/deserialize, TLS encryption
```

#### Layer 5 — Session Layer (সেশন লেয়ার)

```
কাজ: দুটো অ্যাপ্লিকেশনের মধ্যে সেশন (যোগাযোগের পর্ব) তৈরি ও রক্ষণাবেক্ষণ

  ┌─────────────────────────────────────────────────┐
  │  Session Layer                                  │
  │                                                 │
  │  Session Management:                            │
  │  ┌──────────┐  Session ID  ┌──────────┐        │
  │  │ Flutter  │◄────────────►│ Server   │        │
  │  │  App     │              │          │        │
  │  └──────────┘              └──────────┘        │
  │                                                 │
  │  Checkpoint & Recovery:                         │
  │  বড় ফাইল ট্রান্সফার বাধাপ্রাপ্ত হলে           │
  │  শেষ checkpoint থেকে আবার শুরু করা             │
  │                                                 │
  │  Authentication: Login session                  │
  └─────────────────────────────────────────────────┘

Data Unit: Data
উদাহরণ: Netflix-এ একটি video session, banking session
```

#### Layer 4 — Transport Layer (ট্রান্সপোর্ট লেয়ার)

```
কাজ: End-to-end যোগাযোগ, error recovery, flow control

  ┌─────────────────────────────────────────────────┐
  │  Transport Layer                                │
  │                                                 │
  │  TCP (Transmission Control Protocol):           │
  │    ✅ নির্ভরযোগ্য                               │
  │    ✅ ক্রমানুসারে ডেলিভারি                      │
  │    ✅ Error detection ও correction              │
  │    ✅ Flow & Congestion control                 │
  │    ❌ ধীর গতি                                  │
  │    উদাহরণ: HTTP, FTP, SMTP, SSH               │
  │                                                 │
  │  UDP (User Datagram Protocol):                  │
  │    ✅ দ্রুত                                     │
  │    ✅ কম overhead                               │
  │    ❌ অনির্ভরযোগ্য (হারাতে পারে)               │
  │    উদাহরণ: DNS, Video Streaming, Gaming        │
  │                                                 │
  │  Port Number: কোন অ্যাপ্লিকেশন → কোনটি?       │
  └─────────────────────────────────────────────────┘

Data Unit: Segment (TCP) / Datagram (UDP)
```

#### Layer 3 — Network Layer (নেটওয়ার্ক লেয়ার)

```
কাজ: বিভিন্ন নেটওয়ার্কের মধ্যে ডেটা রাউটিং

  ┌─────────────────────────────────────────────────┐
  │  Network Layer                                  │
  │                                                 │
  │  IP Address: কোথায় যাবে?                       │
  │    Source IP:      192.168.1.100 (আপনার ফোন)   │
  │    Destination IP: 142.250.67.46 (Google)      │
  │                                                 │
  │  Routing: কোন পথে যাবে?                        │
  │    Phone → Router → ISP → Google               │
  │                                                 │
  │  Protocols: IP, ICMP, ARP, OSPF, BGP           │
  │  Devices: Router, Layer 3 Switch               │
  └─────────────────────────────────────────────────┘

Data Unit: Packet
```

#### Layer 2 — Data Link Layer (ডেটা লিংক লেয়ার)

```
কাজ: একই নেটওয়ার্কের মধ্যে node-to-node যোগাযোগ

  ┌─────────────────────────────────────────────────┐
  │  Data Link Layer                                │
  │                                                 │
  │  MAC Address: এই নেটওয়ার্কে কোথায়?            │
  │    Source MAC:      2C:54:91:88:C9:E3 (আপনার) │
  │    Destination MAC: FF:FF:FF:FF:FF:FF (Router) │
  │                                                 │
  │  ২টি Sub-layer:                                 │
  │  ┌──────────────────────────────────────┐      │
  │  │  LLC (Logical Link Control)          │      │
  │  │  error control, flow control         │      │
  │  ├──────────────────────────────────────┤      │
  │  │  MAC (Media Access Control)          │      │
  │  │  কে কখন মাধ্যম ব্যবহার করবে         │      │
  │  └──────────────────────────────────────┘      │
  │                                                 │
  │  Devices: Switch, Bridge, NIC (Network Card)   │
  │  Protocols: Ethernet, Wi-Fi (802.11), PPP      │
  └─────────────────────────────────────────────────┘

Data Unit: Frame
```

#### Layer 1 — Physical Layer (ফিজিক্যাল লেয়ার)

```
কাজ: বিটগুলো ফিজিক্যাল সিগন্যালে পরিণত করে পাঠানো

  ┌─────────────────────────────────────────────────┐
  │  Physical Layer                                 │
  │                                                 │
  │  Bits → Signal রূপান্তর:                       │
  │  1 → High voltage (5V) / Light pulse / High frequency │
  │  0 → Low voltage (0V)  / No light  / Low frequency  │
  │                                                 │
  │  Medium:                                        │
  │  • Copper wire (Ethernet)                       │
  │  • Fiber optic (আলোর সিগন্যাল)                │
  │  • Radio waves (Wi-Fi, Bluetooth, 4G/5G)       │
  │                                                 │
  │  Devices: Hub, Repeater, Cable, NIC (physical) │
  │  Concerns: voltage, frequency, distance         │
  └─────────────────────────────────────────────────┘

Data Unit: Bit
```

---

### ৪.৩ Data Encapsulation — লেয়ারে লেয়ারে মোড়ানো

প্রতিটি লেয়ার পাঠানোর সময় নিজের **header** (এবং কখনো trailer) যোগ করে। এটাকে **Encapsulation** বলে।

```
Data Encapsulation (পাঠানোর সময়):

Application:  [      DATA      ]
Presentation: [     DATA       ]  ← encode/encrypt
Session:      [    DATA        ]  ← session info
Transport:    [TCP Header][DATA]  ← port, seq no.
Network:      [IP Header][TCP Header][DATA]  ← IP address
Data Link:    [MAC][IP][TCP][DATA][FCS]  ← MAC, checksum
Physical:     0101011010001010101...  ← bits

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
চিঠির সাথে তুলনা:

চিঠির বিষয়বস্তু        = Data
খামে ভরা             = Encapsulation
খামে ঠিকানা লেখা     = Header যোগ
পোস্ট অফিসে দেওয়া   = Network-এ পাঠানো
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**De-encapsulation** (পাওয়ার সময়):
প্রতিটি লেয়ার নিজের header খুলে নিয়ে উপরের লেয়ারে দেয় — ঠিক উল্টো পদ্ধতিতে।

---

### ৪.৪ একটি HTTP Request-এর সম্পূর্ণ যাত্রা

```
Flutter App থেকে api.example.com-এ GET /users:

┌─────────────────────────────────────────────────────────┐
│ Flutter App (Sender)                                    │
│                                                         │
│ 7. App Layer:    GET /users HTTP/1.1                    │
│                  Host: api.example.com                  │
│                                                         │
│ 6. Pres Layer:   UTF-8 encode, TLS encrypt              │
│                                                         │
│ 5. Session:      TLS Session ID যোগ                     │
│                                                         │
│ 4. Transport:    [TCP Seg: SrcPort=54321, DstPort=443]  │
│                  Seq=1, Ack=0, Flags=SYN                │
│                                                         │
│ 3. Network:      [IP: Src=192.168.1.5, Dst=93.184.216.34]│
│                                                         │
│ 2. Data Link:    [MAC: Src=AA:BB:CC, Dst=Router MAC]    │
│                  [Ethernet Frame]                        │
│                                                         │
│ 1. Physical:     01011010110010101... (ওয়্যার বা Wi-Fi) │
└─────────────────────────────────────────────────────────┘
                        ↓↓↓ নেটওয়ার্কে ভ্রমণ
┌─────────────────────────────────────────────────────────┐
│ API Server (Receiver) — উল্টো দিকে de-encapsulate করে │
│                                                         │
│ 1. Physical:    বিট গ্রহণ                              │
│ 2. Data Link:   Frame খুলে IP packet বের করে           │
│ 3. Network:     IP প্যাকেট খুলে TCP segment বের করে   │
│ 4. Transport:   TCP segment খুলে HTTP data বের করে     │
│ 5-7:            HTTP request process করে response দেয় │
└─────────────────────────────────────────────────────────┘
```

---

### ৪.৫ OSI মডেলে ডিভাইস ও প্রোটোকল

```
লেয়ার অনুযায়ী ডিভাইস ও প্রোটোকল:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

L7 Application  │ HTTP, HTTPS, FTP, SMTP, DNS, SSH
                 │ Browser, Email Client, Flutter App
L6 Presentation │ SSL/TLS, JPEG, MPEG, ASCII, Unicode
L5 Session       │ NetBIOS, RPC, PPTP
L4 Transport     │ TCP, UDP, SCTP
                 │ (Port number এখানে)
L3 Network       │ IP (v4/v6), ICMP, ARP, OSPF, BGP
                 │ Router, Layer-3 Switch
L2 Data Link     │ Ethernet, Wi-Fi (802.11), PPP, ATM
                 │ Switch, Bridge, NIC
L1 Physical      │ Ethernet Cable, Fiber, Radio waves
                 │ Hub, Repeater, Modem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### ৪.৬ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  OSI মডেলের মূল কথা:                                  │
│                                                        │
│  ✅ ৭টি লেয়ার, প্রতিটি আলাদা কাজ করে                 │
│  ✅ Encapsulation = পাঠানোর সময় header যোগ            │
│  ✅ De-encapsulation = পাওয়ার সময় header খোলা        │
│  ✅ Physical = Bits; DataLink = Frames                 │
│  ✅ Network = Packets; Transport = Segments            │
│  ✅ Router = Layer 3; Switch = Layer 2                 │
│  ✅ OSI = তাত্ত্বিক মডেল (TCP/IP = বাস্তব)            │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)

---
---

## অধ্যায় ৫: TCP/IP মডেল — ইন্টারনেটের আসল ভিত্তি

### ৫.১ TCP/IP মডেলের ইতিহাস

TCP/IP মডেল OSI মডেলের আগে তৈরি হয়েছিল — ১৯৭০-এর দশকে ARPANET (ইন্টারনেটের পূর্বসূরি) এর জন্য। এটি বাস্তবমুখী এবং ইন্টারনেট এই মডেলেই কাজ করে।

```
TCP/IP মডেল — ৪টি লেয়ার:

  ┌─────────────────────────────────────────────────┐
  │  4. Application Layer                           │
  │     (OSI-র Application + Presentation + Session)│
  ├─────────────────────────────────────────────────┤
  │  3. Transport Layer                             │
  │     (OSI-র Transport)                           │
  ├─────────────────────────────────────────────────┤
  │  2. Internet Layer                              │
  │     (OSI-র Network)                             │
  ├─────────────────────────────────────────────────┤
  │  1. Network Access Layer                        │
  │     (OSI-র Data Link + Physical)                │
  └─────────────────────────────────────────────────┘
```

---

### ৫.২ OSI vs TCP/IP — বিস্তারিত তুলনা

```
OSI Model          TCP/IP Model        প্রোটোকল
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────┐  ┌─────────────────┐  HTTP, FTP
│ Application │  │                 │  SMTP, DNS
├─────────────┤  │  Application    │  SSH, DHCP
│Presentation │  │                 │  TLS/SSL
├─────────────┤  │                 │  WebSocket
│  Session    │  └─────────────────┘
├─────────────┤  ┌─────────────────┐  TCP, UDP
│  Transport  │  │   Transport     │  SCTP, QUIC
├─────────────┤  └─────────────────┘
│  Network    │  ┌─────────────────┐  IP (v4/v6)
│             │  │   Internet      │  ICMP, ARP
│             │  │                 │  OSPF, BGP
├─────────────┤  └─────────────────┘
│  Data Link  │  ┌─────────────────┐  Ethernet
├─────────────┤  │  Network Access │  Wi-Fi, PPP
│  Physical   │  │                 │  Fiber, Cable
└─────────────┘  └─────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
মূল পার্থক্য:
• OSI = তাত্ত্বিক রেফারেন্স মডেল (troubleshooting-এ ব্যবহৃত)
• TCP/IP = বাস্তব implementation (ইন্টারনেট এটিই ব্যবহার করে)
```

---

### ৫.৩ TCP/IP প্রতিটি লেয়ার বিস্তারিত

#### Layer 1 — Network Access Layer

```
কাজ: Physical hardware ও local network communication

  ┌─────────────────────────────────────────────────┐
  │  Network Access Layer                           │
  │                                                 │
  │  • আপনার NIC (Network Interface Card)           │
  │  • Ethernet frame তৈরি                          │
  │  • MAC address ব্যবহার                          │
  │  • Wi-Fi radio signal                           │
  │  • Fiber optic light pulse                      │
  │  • Copper cable electrical signal               │
  └─────────────────────────────────────────────────┘
```

#### Layer 2 — Internet Layer

```
কাজ: IP addressing ও routing

  ┌─────────────────────────────────────────────────┐
  │  Internet Layer — IP প্যাকেট                    │
  │                                                 │
  │  ┌────────────────────────────────────────┐    │
  │  │  IP Header (20-60 bytes)               │    │
  │  │  ├── Version (4 bits): IPv4 বা IPv6    │    │
  │  │  ├── Header Length (4 bits)            │    │
  │  │  ├── TTL (8 bits): জীবনকাল            │    │
  │  │  ├── Protocol (8 bits): TCP=6, UDP=17  │    │
  │  │  ├── Source IP (32 bits)               │    │
  │  │  └── Destination IP (32 bits)          │    │
  │  └────────────────────────────────────────┘    │
  │                                                 │
  │  TTL (Time To Live):                            │
  │  প্রতিটি router পার হলে TTL 1 কমে              │
  │  TTL=0 হলে প্যাকেট ফেলে দেওয়া হয়              │
  │  (infinite loop প্রতিরোধ)                      │
  └─────────────────────────────────────────────────┘
```

#### Layer 3 — Transport Layer

```
কাজ: End-to-end communication

  TCP Segment Structure:
  ┌──────┬──────┬──────────┬──────────┬───────────┐
  │Src   │Dst   │Sequence  │Ack       │ Data...   │
  │Port  │Port  │Number    │Number    │           │
  │16bit │16bit │32 bit    │32 bit    │           │
  └──────┴──────┴──────────┴──────────┴───────────┘

  UDP Datagram Structure:
  ┌──────┬──────┬────────┬──────────┬───────────┐
  │Src   │Dst   │Length  │Checksum  │ Data...   │
  │Port  │Port  │        │          │           │
  │16bit │16bit │16 bit  │16 bit    │           │
  └──────┴──────┴────────┴──────────┴───────────┘

  TCP vs UDP:
  TCP  = রেজিস্টার্ড ডাক (নিশ্চিত ডেলিভারি, স্বাক্ষর নেয়)
  UDP  = সাধারণ পোস্টকার্ড (দ্রুত, কিন্তু হারাতে পারে)
```

#### Layer 4 — Application Layer

```
কাজ: ব্যবহারকারীর অ্যাপ্লিকেশন সরাসরি এখানে কাজ করে

  প্রধান প্রোটোকল ও Port:
  ┌─────────────┬──────┬───────────────────────────┐
  │ Protocol    │ Port │ কাজ                       │
  ├─────────────┼──────┼───────────────────────────┤
  │ HTTP        │  80  │ ওয়েব                     │
  │ HTTPS       │ 443  │ নিরাপদ ওয়েব              │
  │ FTP         │  21  │ ফাইল ট্রান্সফার           │
  │ SSH         │  22  │ রিমোট অ্যাক্সেস           │
  │ SMTP        │  25  │ ইমেইল পাঠানো              │
  │ DNS         │  53  │ নাম রেজোলিউশন             │
  │ DHCP        │  67  │ IP বরাদ্দ                 │
  │ POP3        │ 110  │ ইমেইল গ্রহণ               │
  │ IMAP        │ 143  │ ইমেইল ম্যানেজমেন্ট         │
  │ HTTPS (alt) │8443  │ বিকল্প HTTPS port         │
  └─────────────┴──────┴───────────────────────────┘
```

---

### ৫.৪ একটি Flutter App-এর সম্পূর্ণ নেটওয়ার্ক যাত্রা

```
Flutter App → dio.get('https://api.example.com/users'):

TCP/IP স্তরে কী হয়:

  ╔═══════════════════════════════════════════════════╗
  ║  Application Layer                                ║
  ║  1. DNS Lookup: api.example.com → 93.184.216.34  ║
  ║  2. TLS Handshake (HTTPS বলে)                    ║
  ║  3. HTTP GET /users তৈরি                          ║
  ╠═══════════════════════════════════════════════════╣
  ║  Transport Layer                                  ║
  ║  4. TCP 3-way Handshake                           ║
  ║     SYN →, ← SYN-ACK, ACK →                     ║
  ║  5. HTTP data TCP segment-এ ভাগ                  ║
  ║     Port 54321 → Port 443                        ║
  ╠═══════════════════════════════════════════════════╣
  ║  Internet Layer                                   ║
  ║  6. IP header যোগ                                ║
  ║     192.168.1.5 → 93.184.216.34                  ║
  ║  7. TTL = 64 সেট                                 ║
  ╠═══════════════════════════════════════════════════╣
  ║  Network Access Layer                             ║
  ║  8. ARP: Router-এর MAC address খোঁজা             ║
  ║  9. Ethernet Frame তৈরি                          ║
  ║  10. Wi-Fi/Ethernet দিয়ে পাঠানো                  ║
  ╚═══════════════════════════════════════════════════╝

Server থেকে Response আসার সময় উল্টো পথে।
মোট সময়: ~50-200 ms (বাংলাদেশ → বিদেশী সার্ভার)
```

---

### ৫.৫ Wireshark দিয়ে TCP/IP দেখা (বাস্তব)

```
Wireshark-এ একটি HTTP request দেখতে কেমন লাগে:

Frame 1: 74 bytes
└── Ethernet II
    ├── Destination: Routerr_aa:bb:cc (84:d4:7e:aa:bb:cc)
    ├── Source: YourPhone_11:22:33 (2c:54:91:11:22:33)
    └── Type: IPv4 (0x0800)
        └── Internet Protocol Version 4
            ├── Source: 192.168.1.5
            ├── Destination: 93.184.216.34
            ├── Protocol: TCP (6)
            └── Transmission Control Protocol
                ├── Source Port: 54321
                ├── Destination Port: 443
                ├── Sequence Number: 0
                ├── Flags: SYN
                └── Hypertext Transfer Protocol
                    ├── GET /users HTTP/1.1
                    ├── Host: api.example.com
                    └── Authorization: Bearer eyJ...
```

---

### ৫.৬ অধ্যায় সারসংক্ষেপ

```
┌────────────────────────────────────────────────────────┐
│  TCP/IP মডেলের মূল কথা:                               │
│                                                        │
│  ✅ ৪টি লেয়ার — বাস্তব ইন্টারনেটের ভিত্তি            │
│  ✅ Application = HTTP/DNS/SMTP/SSH                    │
│  ✅ Transport = TCP (নির্ভরযোগ্য) / UDP (দ্রুত)       │
│  ✅ Internet = IP (routing), ICMP (ping)               │
│  ✅ Network Access = Ethernet, Wi-Fi (hardware)       │
│  ✅ OSI = তাত্ত্বিক; TCP/IP = বাস্তব                   │
│  ✅ প্রতিটি Flutter API call এই স্তরগুলো পার হয়       │
└────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র)

---
ENDOFPART2
echo "Part 2 done: $(wc -l < /home/claude/book_part2.md) lines"
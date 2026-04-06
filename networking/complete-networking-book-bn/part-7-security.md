# PART 7: নেটওয়ার্ক নিরাপত্তা
## Network Security — আপনার সিস্টেম রক্ষার বিজ্ঞান

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২১: TLS/SSL — ডেটা এনক্রিপশনের বিজ্ঞান

## ২১.১ কেন এনক্রিপশন দরকার?

```
এনক্রিপশন ছাড়া (HTTP):

আপনার Flutter App           ইন্টারনেট               সার্ভার
       │                        │                        │
       │──"password=12345"─────►│──"password=12345"────►│
       │                        │                        │
                     ▲
                     │
              যে কেউ এখানে
              বসে পড়তে পারছে!
              (Coffee shop Wi-Fi,
               ISP, Attacker)

এনক্রিপশন সহ (HTTPS/TLS):

আপনার Flutter App           ইন্টারনেট               সার্ভার
       │                        │                        │
       │──"xK9$mP@2qR#..."────►│──"xK9$mP@2qR#..."───►│
       │                        │                        │
                     ▲
                     │
              দেখছে কিন্তু
              বুঝতে পারছে না!
```

## ২১.২ Symmetric vs Asymmetric Encryption

```
Symmetric Encryption (একই চাবি):
                    ┌─────────┐
Plaintext ─(চাবি)──►│ Encrypt │──► Ciphertext
Ciphertext ─(চাবি)──►│ Decrypt │──► Plaintext
                    └─────────┘

সমস্যা: চাবিটা কিভাবে নিরাপদে পাঠাবো?
যদি চাবি চুরি হয়, সব চুরি হয়!

উদাহরণ: AES-256

Asymmetric Encryption (দুটো চাবি):
                   ┌─────────────────────────┐
                   │  Key Pair               │
                   │  Public Key (সবাইকে দাও) │
                   │  Private Key (লুকিয়ে রাখো)│
                   └─────────────────────────┘

Encrypt করি Public Key দিয়ে:
Plaintext ─(Public Key)──► Ciphertext

Decrypt করি Private Key দিয়ে:
Ciphertext ─(Private Key)──► Plaintext

Public Key দিয়ে Encrypt করলে শুধু Private Key দিয়ে Decrypt হবে।
তাই Public Key যে কাউকে দিলেও সমস্যা নেই!

উদাহরণ: RSA-2048, ECC

TLS উভয় ব্যবহার করে:
- Asymmetric: Key exchange-এ (নিরাপদ)
- Symmetric: Actual data transfer-এ (দ্রুত)
```

## ২১.৩ Digital Certificate ও PKI

```
Certificate কী?
┌──────────────────────────────────────────────────────┐
│              SSL/TLS Certificate                     │
├──────────────────────────────────────────────────────┤
│ Subject: api.myapp.com                               │
│ Issuer: Let's Encrypt Authority X3                  │
│ Valid From: 2025-01-01                               │
│ Valid Until: 2025-04-01                              │
│ Public Key: RSA 2048-bit [...]                       │
│ Signature: [CA-এর Digital Signature]                 │
│ Subject Alt Names: myapp.com, *.myapp.com            │
└──────────────────────────────────────────────────────┘

Certificate Chain of Trust:

Root CA (DigiCert, Let's Encrypt Root)
  └── Intermediate CA (Let's Encrypt R3)
        └── Your Certificate (api.myapp.com)

Browser → Your Cert → Intermediate CA → Root CA → ✓ Trusted!

Root CA-র Certificate আগে থেকেই OS/Browser-এ থাকে।
এজন্য Browser বিশ্বাস করে।
```

## ২১.৪ TLS Handshake — বিস্তারিত

```
TLS 1.3 Handshake (সরলীকৃত):

Client (Flutter App)              Server (api.myapp.com)
        │                                 │
        │ ① Client Hello                  │
        │──────────────────────────────►│
        │ TLS Version: 1.3               │
        │ Supported Ciphers: [AES-GCM..] │
        │ Client Random: [32 bytes]       │
        │ Supported Groups: [x25519..]   │
        │ Key Share: [DH Public Key]     │
        │                                 │
        │ ② Server Hello + Certificate    │
        │◄──────────────────────────────│
        │ Selected Cipher: AES-256-GCM   │
        │ Server Random: [32 bytes]       │
        │ Key Share: [DH Public Key]     │
        │ Certificate: [api.myapp.com]   │
        │ Certificate Verify: [Signature]│
        │ Finished: [Verify hash]        │
        │                                 │
        │ [Client Certificate যাচাই করে] │
        │ [Diffie-Hellman দিয়ে session   │
        │  key তৈরি করে — কেউ জানে না]  │
        │                                 │
        │ ③ Client Finished               │
        │──────────────────────────────►│
        │ Finished: [Verify hash]        │
        │                                 │
        │ ════ Encrypted Communication ══│
        │ Application Data (Encrypted)   │
        │──────────────────────────────►│
        │◄──────────────────────────────│
```

**TLS 1.2 vs TLS 1.3:**
| বিষয় | TLS 1.2 | TLS 1.3 |
|-------|---------|---------|
| Handshake RTT | 2 RTT | 1 RTT |
| 0-RTT | না | হ্যাঁ (Resumption) |
| Cipher Suites | অনেক (কিছু দুর্বল) | মাত্র ৫টি (সব শক্তিশালী) |
| Forward Secrecy | Optional | সবসময় |
| Performance | ধীর | দ্রুত |

## ২১.৫ Cipher Suites — এনক্রিপশনের রেসিপি

```
TLS_AES_256_GCM_SHA384 মানে কী?

TLS_    AES_256_GCM    _SHA384
 │          │              │
 │     Symmetric       Hash/HMAC
 │     Encryption     Algorithm
 │     Algorithm
 │     (AES, 256-bit key,
 │      GCM mode)
 │
TLS Protocol

পুরনো (TLS 1.2):
TLS_RSA_WITH_AES_256_CBC_SHA256
 │     │           │        │
 │   Key         Encrypt  Hash
 │  Exchange
 │
 └── RSA: ধীর, Forward Secrecy নেই!

নতুন (TLS 1.3):
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
(সবগুলোতে DHE/ECDHE — Forward Secrecy আছে)
```

## ২১.৬ Forward Secrecy — ভবিষ্যতের রক্ষা

```
Forward Secrecy ছাড়া:
আজকের Traffic রেকর্ড করে রাখো।
ভবিষ্যতে Server-এর Private Key চুরি করো।
তখন পুরনো সব traffic decrypt করো!

Forward Secrecy সহ (DHE/ECDHE):
প্রতিটি Session-এর জন্য আলাদা Ephemeral Key।
Session শেষে Key মুছে যায়।
Private Key চুরি হলেও পুরনো session decrypt হয় না!

Diffie-Hellman Key Exchange:
Alice                            Bob
  │                               │
  │ দুজন agree করলাম:            │
  │ g=5, p=23 (public)           │
  │                               │
  │ Alice secret: a=6             │
  │ Alice calculates: A = g^a mod p = 5^6 mod 23 = 8
  │                               │
  │ Bob secret: b=15              │
  │ Bob calculates: B = g^b mod p = 5^15 mod 23 = 19
  │                               │
  │──── A=8 ─────────────────────►│
  │◄─── B=19 ─────────────────────│
  │                               │
  │ Alice: K = B^a mod p = 19^6 mod 23 = 2
  │ Bob:   K = A^b mod p = 8^15 mod 23 = 2
  │                               │
  │ দুজনেই পেল K=2 (Shared Secret)│
  │ কিন্তু কেউ a বা b জানে না!   │
```

## ২১.৭ Flutter-এ Certificate Pinning

```dart
// Certificate Pinning — Man-in-the-Middle Attack প্রতিরোধ
import 'dart:io';
import 'package:dio/dio.dart';

class SecureHttpClient {
  static Dio createWithPinning() {
    final dio = Dio();
    
    // Custom HttpClient তৈরি
    (dio.httpClientAdapter as DefaultHttpClientAdapter).onHttpClientCreate = 
      (client) {
        client.badCertificateCallback = (cert, host, port) => false;
        
        // SHA-256 Fingerprint যাচাই
        client.badCertificateCallback = (X509Certificate cert, String host, int port) {
          // Certificate-এর SHA256 fingerprint
          final fingerprint = _sha256Fingerprint(cert.der);
          
          const expectedFingerprint = 
            'AA:BB:CC:DD:EE:FF:...'; // আপনার cert-এর fingerprint
          
          return fingerprint != expectedFingerprint; // ভুল হলে reject
        };
        
        return client;
      };
    
    return dio;
  }
  
  static String _sha256Fingerprint(List<int> der) {
    // SHA256 hash of certificate DER bytes
    // Implementation details...
    return 'fingerprint_here';
  }
}

// ব্যবহার:
// Certificate Pinning কেন?
// হ্যাকার যদি নকল certificate দেয়, pinning reject করবে

// মনে রাখুন:
// Certificate renew হলে app update করতে হবে
// তাই backup pin রাখুন সবসময়
```

## ২১.৮ mTLS — Mutual TLS

```
সাধারণ TLS:
Client → Server Certificate যাচাই করে
কিন্তু Server জানে না Client কে!

mTLS (Mutual TLS):
Client → Server Certificate যাচাই করে ✓
Server → Client Certificate যাচাই করে ✓
দুজনই প্রমাণিত!

mTLS কখন ব্যবহার:
- Microservice-to-Microservice communication
- API Authentication (API Key-এর বিকল্প)
- Zero Trust Architecture

mTLS Flow:
Client                              Server
  │                                   │
  │── ClientHello ───────────────────►│
  │◄─ ServerHello + Certificate ──────│
  │◄─ "Client Certificate চাই" ───────│
  │── Client Certificate ────────────►│
  │── ClientKeyExchange ─────────────►│
  │── CertificateVerify ─────────────►│
  │── Finished ──────────────────────►│
  │◄─ Finished ────────────────────── │
  │ ══════ Mutual Auth Complete ══════ │
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২২: Firewall, IDS/IPS ও Network Security

## ২২.১ Firewall — নেটওয়ার্কের দারোয়ান

```
Firewall = নেটওয়ার্কের প্রবেশদ্বারে নিরাপত্তা প্রহরী

ইন্টারনেট ──────► [ FIREWALL ] ──────► আপনার নেটওয়ার্ক
                       │
                   নিয়মের তালিকা:
                   Allow: TCP port 443 (HTTPS)
                   Allow: TCP port 80 (HTTP)
                   Allow: TCP port 22 from office IP
                   Deny: UDP port 1234
                   Deny: ALL others
```

**Firewall প্রকারভেদ:**

```
1. Packet Filter (Stateless):
প্রতিটি packet আলাদাভাবে দেখে।
Source IP, Destination IP, Port, Protocol দেখে।
Connection state মনে রাখে না।

Rule উদাহরণ:
ALLOW TCP 0.0.0.0/0 → 10.0.0.1:443    ← যেকোনো IP থেকে HTTPS
ALLOW TCP 203.0.113.5 → 10.0.0.1:22  ← শুধু office IP থেকে SSH
DENY  ALL                               ← বাকি সব বন্ধ

2. Stateful Firewall:
Connection state মনে রাখে।
Established connection-এর return traffic allow করে।

Example:
Client → Server: SYN (New connection — check rules)
Server → Client: SYN-ACK (Established — automatically allow)
Client → Server: ACK (Established — automatically allow)

3. Application Layer Firewall (WAF):
HTTP/HTTPS traffic বোঝে।
SQL Injection, XSS, CSRF detect করতে পারে।
```

## ২২.২ iptables — Linux Firewall

```bash
# iptables — Linux-এর firewall tool

# সব rules দেখি
iptables -L -v -n

# HTTPS allow করি (যেকোনো থেকে)
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# SSH শুধু office IP থেকে allow
iptables -A INPUT -p tcp --dport 22 -s 203.0.113.0/24 -j ACCEPT

# বাকি সব input বন্ধ
iptables -A INPUT -j DROP

# Established connection-এর return allow
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# DDoS Protection — প্রতি IP থেকে সর্বোচ্চ ২৫ connection
iptables -A INPUT -p tcp --dport 443 \
  -m connlimit --connlimit-above 25 -j DROP

# Rate Limiting — প্রতি মিনিটে সর্বোচ্চ ১০ SYN
iptables -A INPUT -p tcp --syn \
  -m limit --limit 10/minute -j ACCEPT
```

## ২২.৩ WAF — Web Application Firewall

```
WAF কী আটকায়?

SQL Injection:
GET /users?id=1 OR 1=1 --
         ↑ WAF detect করে, block করে

XSS (Cross-Site Scripting):
POST /comment
body: <script>steal_cookie()</script>
            ↑ WAF detect করে, sanitize করে

Path Traversal:
GET /files/../../../etc/passwd
              ↑ WAF detect করে, block করে

Common WAF Solutions:
- AWS WAF (Cloud)
- Cloudflare WAF (Cloud)
- ModSecurity (Self-hosted, Nginx/Apache)
- OWASP CRS (Rule set)
```

## ২২.৪ Common Network Attacks

```
1. DDoS (Distributed Denial of Service):
┌──────────────────────────────────────────────────────┐
│  Botnet (লক্ষ লক্ষ infected computer)               │
│                                                      │
│  Bot1 ──┐                                           │
│  Bot2 ──┤── লক্ষ লক্ষ Request ──► Your Server       │
│  Bot3 ──┤                         Server ডুবে যায়! │
│  ...    ┘                                           │
└──────────────────────────────────────────────────────┘

প্রতিকার:
- CDN (Cloudflare, AWS Shield)
- Rate Limiting
- IP Reputation blocking
- Anycast routing

2. Man-in-the-Middle (MITM):
Client ─────────────────────────────► Server
           ▲ Attacker এখানে বসে ▼
           ব্যবহার করছে ─────────────

প্রতিকার: TLS/HTTPS, Certificate Pinning

3. ARP Spoofing:
Attacker বলে: "আমিই Router! সব traffic আমার কাছে পাঠাও"
LAN-এর সব traffic Attacker-এর কাছে যায়!

প্রতিকার: Dynamic ARP Inspection (Switch feature)

4. DNS Poisoning:
Attacker বলে: "google.com = 1.2.3.4 (ভুয়া সাইট)"
DNS Cache-এ ঢুকে যায়!

প্রতিকার: DNSSEC, DoH/DoT
```

## ২২.৫ IDS vs IPS

```
IDS (Intrusion Detection System):
শুধু সন্দেহজনক activity দেখে Alert পাঠায়।
Traffic block করে না।

IPS (Intrusion Prevention System):
সন্দেহজনক activity দেখে সাথে সাথে block করে।

┌─────────────────────────────────────────────────────┐
│                                                     │
│  Internet ──► [Firewall] ──► [IPS] ──► Network     │
│                                │                   │
│                         Block করে!                 │
│                                                     │
│  Internet ──► [Firewall] ──► Network               │
│                                │                   │
│                         [IDS] ──► Alert            │
│                    (Copy of traffic দেখে)           │
└─────────────────────────────────────────────────────┘

IDS/IPS সনাক্ত করে:
- Port Scanning
- Brute Force Attacks
- Known Malware Patterns
- Unusual Traffic Spikes
- SQL Injection Attempts
```

## ২২.৬ Flutter App নিরাপত্তা Checklist

```
Flutter Network Security Checklist:

✅ HTTPS সবসময় (HTTP কখনো না)
✅ Certificate Pinning (Production-এ)
✅ Token Secure Storage (flutter_secure_storage)
✅ Request Timeout সেট করুন
✅ Sensitive data log করবেন না
✅ API Key কোডে লেখবেন না (Environment variable)
✅ Input validation (client + server উভয়ে)
✅ Rate limiting (server-side)
✅ JWT expiry check
✅ SSL/TLS version minimum 1.2

Code উদাহরণ — Sensitive data log না করা:
```

```dart
// ❌ খারাপ:
print('Sending request with token: ${token}');
print('User password: ${password}');

// ✅ ভালো:
if (kDebugMode) {
  // শুধু debug mode-এ, sensitive info ছাড়া
  print('API Request to: ${endpoint}');
}

// Token Secure Storage:
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

final storage = FlutterSecureStorage(
  aOptions: AndroidOptions(encryptedSharedPreferences: true),
  iOptions: IOSOptions(accessibility: KeychainAccessibility.first_unlock),
);

await storage.write(key: 'auth_token', value: token);
final token = await storage.read(key: 'auth_token');
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২৩: VPN — ভার্চুয়াল প্রাইভেট নেটওয়ার্ক

## ২৩.১ VPN কিভাবে কাজ করে?

```
VPN ছাড়া:
আপনি (বাসায়)  ──── ইন্টারনেট ────  Office Server
192.168.1.5          (Public)         10.0.0.10
                         │
                    সবাই দেখতে পাচ্ছে!

VPN সহ:
আপনি (বাসায়)  ════ VPN Tunnel ════  Office VPN Server  ─── Office Network
192.168.1.5         (Encrypted)       10.0.0.1               10.0.0.10
                                           │
                                   আপনি যেন Office-এ আছেন!
                                   Virtual IP পান: 10.0.0.50

টানেলিং:
┌─────────────────────────────────────────────────┐
│  Outer Packet (Public Internet)                  │
│  ┌─────────────────────────────────────────┐    │
│  │  Inner Packet (Original — Encrypted)    │    │
│  │  src: 10.0.0.50, dst: 10.0.0.10        │    │
│  │  [Your actual data — encrypted]         │    │
│  └─────────────────────────────────────────┘    │
│  src: 192.168.1.5, dst: VPN Server IP           │
└─────────────────────────────────────────────────┘
```

## ২৩.২ VPN Protocol তুলনা

```
IPsec VPN:
- Layer 3 (Network Layer)
- AH (Authentication Header) ও ESP (Encapsulating Security Payload)
- Site-to-Site VPN-এ সবচেয়ে বেশি ব্যবহার
- Complex configuration

OpenVPN:
- SSL/TLS-এর উপর
- TCP বা UDP ব্যবহার করতে পারে
- Cross-platform
- Firewall bypass ভালো করে (port 443)
- ধীর (CPU-intensive)

WireGuard (সবচেয়ে আধুনিক):
- শুধু ৪,০০০ লাইন code (OpenVPN: ১,০০,০০০+)
- UDP only (port 51820)
- State-of-the-art cryptography
- অনেক দ্রুত
- Simpler configuration
- Modern kernel-level implementation

Performance তুলনা:
WireGuard: ~1 Gbps throughput
OpenVPN:   ~100 Mbps throughput
IPsec:     ~500 Mbps throughput
```

## ২৩.৩ Site-to-Site vs Remote Access VPN

```
Site-to-Site VPN:
┌─────────────────┐              ┌─────────────────┐
│  ঢাকা Office    │════ VPN ════│  চট্টগ্রাম Office│
│  Network        │              │  Network        │
│  10.0.0.0/24    │              │  10.1.0.0/24    │
└─────────────────┘              └─────────────────┘
দুটো অফিসের নেটওয়ার্ক সংযুক্ত।
ঢাকা থেকে চট্টগ্রামের server-এ directly access।

Remote Access VPN:
┌──────────────┐         ┌──────────────────────┐
│ আপনি (বাসায়)│═══ VPN ═│  VPN Server (Office) │
│ 192.168.1.5  │         │  10.0.0.1            │
└──────────────┘         └──────────────────────┘
আপনি virtual IP পান: 10.0.0.50
এখন Office-এর সব resource access করতে পারবেন।

Split Tunneling:
┌─────────────────────────────────────────────────┐
│  Split Tunneling OFF:                           │
│  সব traffic → VPN Tunnel → Office → Internet   │
│                                                 │
│  Split Tunneling ON:                            │
│  Office IP → VPN Tunnel                         │
│  বাকি সব → Direct Internet (দ্রুত!)             │
└─────────────────────────────────────────────────┘
```

## ২৩.৪ WireGuard — আধুনিক VPN

```bash
# WireGuard Server Setup (Ubuntu):

# Install
apt install wireguard

# Key তৈরি
wg genkey | tee /etc/wireguard/private.key
cat /etc/wireguard/private.key | wg pubkey > /etc/wireguard/public.key

# Server Config (/etc/wireguard/wg0.conf):
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = <server_private_key>

[Peer]
# Client-এর তথ্য
PublicKey = <client_public_key>
AllowedIPs = 10.0.0.2/32

# Start VPN
wg-quick up wg0

# Client Config:
[Interface]
Address = 10.0.0.2/24
PrivateKey = <client_private_key>
DNS = 1.1.1.1

[Peer]
PublicKey = <server_public_key>
Endpoint = server.example.com:51820
AllowedIPs = 0.0.0.0/0  # সব traffic VPN দিয়ে
PersistentKeepalive = 25
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২৪: নেটওয়ার্কে Authentication ও Authorization

## ২৪.১ Authentication vs Authorization

```
Authentication = কে আপনি? (পরিচয় যাচাই)
Authorization  = আপনি কী করতে পারবেন? (অনুমতি যাচাই)

বাস্তব উদাহরণ:
আপনি অফিসে ID card দেখিয়ে ঢুকলেন → Authentication
কিন্তু Server Room-এ ঢুকতে পারলেন না → Authorization (আপনার permission নেই)
```

## ২৪.২ JWT — JSON Web Token

```
JWT Structure:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJ1c2VySWQiOjEsInJvbGUiOiJhZG1pbiIsImV4cCI6MTcwMDAwMH0.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

তিনটি অংশ (. দিয়ে আলাদা):

Header (Base64):          Payload (Base64):          Signature:
{                         {                          HMAC-SHA256(
  "alg": "HS256",           "userId": 1,               header + "." + payload,
  "typ": "JWT"              "role": "admin",            secret_key
}                           "exp": 1700000000          )
                          }

Header = Algorithm        Payload = Data             Signature = Verification
জানায়                     (claims)                   (tamper-proof)

JWT Verification:
সার্ভার Signature যাচাই করে।
যদি কেউ Payload পরিবর্তন করে, Signature মিলবে না।
কিন্তু Payload এনক্রিপ্টেড নয়! শুধু Base64।
তাই sensitive data JWT-তে রাখবেন না।
```

```dart
// Flutter-এ JWT handling:
import 'package:jwt_decoder/jwt_decoder.dart';

class AuthService {
  Future<bool> login(String email, String password) async {
    final response = await _dio.post('/auth/login', data: {
      'email': email,
      'password': password,
    });
    
    final token = response.data['access_token'];
    final refreshToken = response.data['refresh_token'];
    
    // Secure storage-এ রাখি
    await _storage.write(key: 'access_token', value: token);
    await _storage.write(key: 'refresh_token', value: refreshToken);
    
    return true;
  }
  
  Future<String?> getValidToken() async {
    final token = await _storage.read(key: 'access_token');
    if (token == null) return null;
    
    // Token expire হয়েছে?
    if (JwtDecoder.isExpired(token)) {
      return await _refreshToken();
    }
    
    // Token expire হওয়ার ৫ মিনিট আগে refresh করি
    final expiry = JwtDecoder.getExpirationDate(token);
    if (expiry.difference(DateTime.now()).inMinutes < 5) {
      return await _refreshToken();
    }
    
    return token;
  }
  
  Future<String?> _refreshToken() async {
    final refreshToken = await _storage.read(key: 'refresh_token');
    if (refreshToken == null) {
      await logout(); // Refresh token নেই, logout
      return null;
    }
    
    try {
      final response = await _dio.post('/auth/refresh', data: {
        'refresh_token': refreshToken,
      });
      
      final newToken = response.data['access_token'];
      await _storage.write(key: 'access_token', value: newToken);
      return newToken;
    } catch (e) {
      await logout();
      return null;
    }
  }
  
  Future<void> logout() async {
    await _storage.deleteAll();
    // Navigate to login screen
  }
}
```

## ২৪.৩ OAuth 2.0 — Third-party Authentication

```
OAuth 2.0 Flow (Authorization Code + PKCE):

User        Flutter App     Auth Server      Resource Server
  │              │                │                  │
  │ "Google Login"│                │                  │
  │──────────────►│                │                  │
  │               │                │                  │
  │               │ ① Auth Request │                  │
  │               │──────────────►│                  │
  │               │ /authorize     │                  │
  │               │ ?client_id=abc │                  │
  │               │ &redirect_uri= │                  │
  │               │ &code_challenge│ (PKCE)           │
  │               │                │                  │
  │ ② Login Page  │                │                  │
  │◄──────────────────────────────│                  │
  │               │                │                  │
  │ ③ Login করি  │                │                  │
  │──────────────────────────────►│                  │
  │               │                │                  │
  │               │ ④ Auth Code    │                  │
  │               │◄──────────────│                  │
  │               │                │                  │
  │               │ ⑤ Token Exchange│                 │
  │               │──────────────►│                  │
  │               │ /token         │                  │
  │               │ ?code=xyz      │                  │
  │               │ &code_verifier │ (PKCE verify)    │
  │               │                │                  │
  │               │ ⑥ Access Token │                  │
  │               │◄──────────────│                  │
  │               │                │                  │
  │               │ ⑦ API Request with Token          │
  │               │──────────────────────────────────►│
  │               │                │                  │
  │               │ ⑧ User Data    │                  │
  │               │◄──────────────────────────────────│

PKCE (Proof Key for Code Exchange):
code_verifier = random string (43-128 chars)
code_challenge = BASE64URL(SHA256(code_verifier))

এটি Authorization Code interception attack প্রতিরোধ করে।
```

```dart
// Flutter OAuth 2.0 with PKCE:
import 'package:flutter_appauth/flutter_appauth.dart';

class OAuthService {
  final _appAuth = FlutterAppAuth();
  
  Future<AuthorizationTokenResponse?> loginWithGoogle() async {
    try {
      return await _appAuth.authorizeAndExchangeCode(
        AuthorizationTokenRequest(
          'YOUR_CLIENT_ID',
          'com.myapp://callback',  // Redirect URI
          serviceConfiguration: AuthorizationServiceConfiguration(
            authorizationEndpoint: 'https://accounts.google.com/o/oauth2/auth',
            tokenEndpoint: 'https://oauth2.googleapis.com/token',
          ),
          scopes: ['openid', 'profile', 'email'],
          // PKCE স্বয়ংক্রিয়ভাবে handle হয়
        ),
      );
    } catch (e) {
      print('OAuth error: $e');
      return null;
    }
  }
}
```

## ২৪.৪ Zero Trust Network Architecture

```
Traditional (Castle-and-Moat):
"VPN-এর ভেতরে থাকলে বিশ্বাস করো"

সমস্যা:
যদি কেউ VPN credentials চুরি করে?
তাহলে সে ভেতরে ঢুকে সব access পাবে!

Zero Trust:
"কাউকে বিশ্বাস করো না — সব সময় verify করো"

Zero Trust নীতি:
1. Never Trust, Always Verify
2. Least Privilege Access
3. Assume Breach (ধরে নাও হয়েছে)
4. Explicit Verification (সব request verify)
5. Micro-segmentation (network ছোট অংশে ভাগ)

Zero Trust Flow:
User/Device → Identity Provider (Verify who)
           → Device Trust Check (Verify device)
           → Policy Engine (Allow what?)
           → Resource Access (মাত্র প্রয়োজনীয়)

Implementation:
- Google BeyondCorp
- AWS IAM + Security Groups
- Cloudflare Zero Trust
- Okta ZTNA
```

**Tech Lead টিপস:**
- JWT-তে sensitive information রাখবেন না
- Refresh Token-এর expiry দীর্ঘ রাখুন, Access Token-এর স্বল্প (15 মিনিট)
- OAuth-এ PKCE সবসময় ব্যবহার করুন mobile app-এ
- Zero Trust gradually implement করুন — একবারে সব নয়

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---
*PART 7 সম্পন্ন। পরবর্তী: PART 8 — Cloud ও Modern Architecture*
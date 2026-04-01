# নেটওয়ার্কিং — গভীর থেকে গভীরে
### বাইনারি থেকে ব্রাউজার পর্যন্ত সম্পূর্ণ যাত্রা

> **লেখকের কথা:** এই document টা তোমাকে ধরে নিয়ে যাবে একদম শূন্য থেকে — মানে `0` এবং `1` থেকে শুরু করে, সেটা কীভাবে বিদ্যুৎ হয়, তার ভেতর দিয়ে ছোটে, অন্য কম্পিউটারে পৌঁছায়, Socket তৈরি হয়, TCP handshake হয়, HTTP request যায় — সব কিছু। প্রতিটা concept-এর সাথে code আছে, diagram আছে, analogy আছে।

---

## সূচিপত্র

1. [সবকিছুর শুরু — Binary কি এবং কেন?](#১-সবকিছুর-শুরু--binary-কি-এবং-কেন)
2. [Bit থেকে Byte — Data-র একক](#২-bit-থেকে-byte--data-র-একক)
3. [Binary → Electric Signal — যাদুটা এখানেই](#৩-binary--electric-signal--যাদুটা-এখানেই)
4. [Signal Encoding — বিভিন্ন পদ্ধতি](#৪-signal-encoding--বিভিন্ন-পদ্ধতি)
5. [তার থেকে বেতার — Physical Medium](#৫-তার-থেকে-বেতার--physical-medium)
6. [Data কে ভাঙো — Framing ও Packets](#৬-data-কে-ভাঙো--framing-ও-packets)
7. [MAC Address ও Data Link Layer](#৭-mac-address-ও-data-link-layer)
8. [IP Address — নেটওয়ার্কের ঠিকানা ব্যবস্থা](#৮-ip-address--নেটওয়ার্কের-ঠিকানা-ব্যবস্থা)
9. [Port — দরজার নম্বর](#৯-port--দরজার-নম্বর)
10. [Socket — যোগাযোগের জানালা](#১০-socket--যোগাযোগের-জানালা)
11. [TCP — নির্ভরযোগ্যতার বিজ্ঞান](#১১-tcp--নির্ভরযোগ্যতার-বিজ্ঞান)
12. [UDP — গতির দর্শন](#১২-udp--গতির-দর্শন)
13. [HTTP — ওয়েবের ভাষা](#১৩-http--ওয়েবের-ভাষা)
14. [সম্পূর্ণ যাত্রা — google.com লিখলে কী হয়](#১৪-সম্পূর্ণ-যাত্রা--googlecom-লিখলে-কী-হয়)

---

## ১. সবকিছুর শুরু — Binary কি এবং কেন?

কম্পিউটার একটা বৈদ্যুতিক যন্ত্র। এর ভেতরে লক্ষ লক্ষ ছোট ছোট switch আছে — যেগুলোকে বলে **Transistor**। একটা transistor-এর শুধু দুটো অবস্থা থাকতে পারে: হয় current চলছে, নয়তো চলছে না।

এই দুটো অবস্থাকেই আমরা `1` এবং `0` দিয়ে represent করি।

```
Current আছে   →  1  (HIGH voltage, সাধারণত ~3.3V বা 5V)
Current নেই   →  0  (LOW voltage, সাধারণত ~0V)
```

**কেন binary?** কারণ মানুষের জন্য দশমিক (0-9) সহজ, কিন্তু মেশিনের জন্য সবচেয়ে সহজ হলো দুটো অবস্থা। একটা switch on না off — এটা নির্ধারণ করা অনেক সহজ এবং নির্ভরযোগ্য।

> **Real-life analogy:** কল্পনা করো তোমার ঘরের বাতির switch। হয় on নয়তো off — মাঝামাঝি কিছু নেই। কম্পিউটারের প্রতিটা transistor ঠিক এভাবেই কাজ করে।

### Binary সংখ্যা পদ্ধতি

আমরা দৈনন্দিন জীবনে Base-10 ব্যবহার করি। কম্পিউটার ব্যবহার করে Base-2।

```
দশমিক  →  Binary
  0    →  0000
  1    →  0001
  2    →  0010
  3    →  0011
  4    →  0100
  5    →  0101
  6    →  0110
  7    →  0111
  8    →  1000
  9    →  1001
 10    →  1010
```

**গণনার নিয়ম:**

দশমিকে প্রতিটা ঘর হলো 10-এর power। Binary-তে প্রতিটা ঘর হলো 2-এর power।

```
দশমিক 13 মানে:
  1 × 10¹  +  3 × 10⁰
= 10        +  3
= 13

Binary 1101 মানে:
  1 × 2³  +  1 × 2²  +  0 × 2¹  +  1 × 2⁰
= 8       +  4       +  0       +  1
= 13
```

```python
# Python দিয়ে binary conversion দেখো

number = 13

# Decimal থেকে Binary
binary_str = bin(number)          # '0b1101'
binary_clean = bin(number)[2:]    # '1101'  (0b prefix বাদ দিলাম)

print(f"Decimal {number} = Binary {binary_clean}")

# নিজে হাতে করে দেখাই
def decimal_to_binary(n):
    """
    Decimal সংখ্যাকে binary-তে রূপান্তর করো।
    পদ্ধতি: বারবার 2 দিয়ে ভাগ করো, ভাগশেষ রাখো।
    """
    if n == 0:
        return "0"
    
    bits = []
    while n > 0:
        remainder = n % 2    # 2 দিয়ে ভাগের ভাগশেষ হয় 0 নয়তো 1
        bits.append(str(remainder))
        n = n // 2           # integer division
    
    # ভাগশেষগুলো উল্টো ক্রমে সাজাও
    bits.reverse()
    return ''.join(bits)

# Test
for i in range(16):
    print(f"  {i:2d}  =  {decimal_to_binary(i):>4s}  (binary)")
```

**Output:**
```
   0  =     0  (binary)
   1  =     1  (binary)
   2  =    10  (binary)
   3  =    11  (binary)
   4  =   100  (binary)
   ...
  13  =  1101  (binary)
  15  =  1111  (binary)
```

---

## ২. Bit থেকে Byte — Data-র একক

একটা `0` বা `1` হলো একটা **bit** — এটাই তথ্যের সবচেয়ে ছোট একক।

কিন্তু একটা মাত্র bit দিয়ে খুব বেশি কিছু বলা যায় না। তাই আমরা `8টা bit` একসাথে নিই — এটাকে বলি **byte**।

```
1 bit    = 0 বা 1
8 bits   = 1 byte
1024 bytes    = 1 Kilobyte (KB)
1024 KB        = 1 Megabyte (MB)
1024 MB        = 1 Gigabyte (GB)
1024 GB        = 1 Terabyte (TB)
```

### Text কীভাবে Binary হয়?

প্রতিটা character-কে একটা number দিয়ে represent করা হয়। এই mapping-এর নাম **ASCII** (American Standard Code for Information Interchange)।

```
'A'  →  65  →  01000001
'B'  →  66  →  01000010
'a'  →  97  →  01100001
' '  →  32  →  00100000  (space)
'0'  →  48  →  00110000  (character শূন্য, number শূন্য না)
```

```python
# "HI" কীভাবে binary হয় দেখো

def text_to_binary(text):
    """
    প্রতিটা character-কে তার ASCII value খোঁজো,
    তারপর সেটাকে 8-bit binary-তে রূপান্তর করো।
    """
    result = []
    for char in text:
        ascii_value = ord(char)          # character → ASCII number
        binary_val = format(ascii_value, '08b')  # number → 8-bit binary string
        result.append(f"'{char}' = {ascii_value} = {binary_val}")
    return result

lines = text_to_binary("HI MOM")
for line in lines:
    print(line)
```

**Output:**
```
'H' = 72  = 01001000
'I' = 73  = 01001001
' ' = 32  = 00100000
'M' = 77  = 01001101
'O' = 79  = 01001111
'M' = 77  = 01001101
```

তাহলে "HI MOM" network-এ পাঠালে এই bit stream যাবে:

```
01001000 01001001 00100000 01001101 01001111 01001101
   H         I      (space)    M         O         M
```

### Unicode ও UTF-8

ASCII শুধু English এবং কিছু basic symbol handle করে (128টা character)। বাংলা, আরবি, চাইনিজ লেখার জন্য **Unicode** দরকার।

**UTF-8** হলো Unicode-এর সবচেয়ে জনপ্রিয় encoding। এটা variable-length — ASCII character-এ 1 byte, বাংলা character-এ 3 bytes।

```python
# বাংলা "সালাম" কীভাবে encode হয়?

word = "সালাম"

# UTF-8 encoding
encoded = word.encode('utf-8')
print(f"Text: {word}")
print(f"UTF-8 bytes (hex): {encoded.hex()}")
print(f"মোট bytes: {len(encoded)}")
print()

# প্রতিটা byte binary-তে
for i, byte in enumerate(encoded):
    print(f"  Byte {i+1}: {byte:3d}  =  {byte:08b}")
```

**Output:**
```
Text: সালাম
UTF-8 bytes (hex): e0a6b8e0a6bee0a6b2e0a6bee0a6ae
মোট bytes: 15

  Byte 1:  224  =  11100000   ← 'স' এর প্রথম byte
  Byte 2:  166  =  10100110
  Byte 3:  184  =  10111000   ← 'স' শেষ
  ...
```

---

## ৩. Binary → Electric Signal — যাদুটা এখানেই

এটাই সবচেয়ে মৌলিক প্রশ্ন: এই `0` আর `1` গুলো তারের ভেতর দিয়ে কীভাবে যায়?

উত্তর হলো **voltage**। তার দিয়ে বিদ্যুৎ পাঠানো হয়, এবং সেই বিদ্যুতের voltage-র স্তর দিয়ে 0 এবং 1 বোঝানো হয়।

```
Ethernet তারে:
    +2.5V  →  logic 1
    -2.5V  →  logic 0  (differential signaling)

TTL circuit-এ:
    +5V    →  logic 1
     0V    →  logic 0

LVDS (Low Voltage Differential Signaling)-এ:
    +350mV →  logic 1
    -350mV →  logic 0
```

### Voltage কীভাবে দেখতে হয়?

একটা oscilloscope (ওসিলোস্কোপ) দিয়ে তারের signal দেখলে এরকম দেখাবে:

```
Voltage
  |
5V|  ___     ___     _______
  | |   |   |   |   |
0V|_|   |___|   |___|
  |
  +----------------------------> সময় (Time)
     1     0     1      1
```

এই wave-কে বলে **Square Wave** বা **Digital Signal**। উঁচু মানে 1, নিচু মানে 0।

### Clock Signal — ছন্দ রক্ষা করে কে?

শুধু voltage উঁচু-নিচু করলেই হবে না। Receiver-কে জানতে হবে *কতক্ষণ পরপর* সে একটা bit পড়বে। এজন্য আলাদা একটা **clock signal** থাকে।

```
Clock:    ___ ___ ___ ___ ___ ___
         |   |   |   |   |   |   |
         |   |   |   |   |   |   |
_________|   |___|   |___|   |___|

Data:     _______ ___ ___________
         |       |   |           |
         |       |   |           |
_________|       |___|           |___

         1       0   1           0

প্রতিটা Clock-এর rising edge (↑)-এ Data পড়া হয়
```

> **Analogy:** Clock হলো একজন শিক্ষকের ঘণ্টা। ঘণ্টা বাজলে পরীক্ষার্থী পরের প্রশ্নে যায়। ঘণ্টা ছাড়া কেউ জানবে না কখন থামতে হবে।

### Baud Rate vs Bit Rate

**Baud Rate** = প্রতি সেকেন্ডে কতটা signal change হয়
**Bit Rate** = প্রতি সেকেন্ডে কতটা bit পাঠানো হয়

যদি প্রতিটা signal-এ শুধু 1 bit থাকে, তাহলে Baud Rate = Bit Rate। কিন্তু আধুনিক encoding-এ একটা signal-এ একাধিক bit থাকতে পারে।

```python
# Bandwidth calculation

def calculate_data_transfer(bandwidth_mbps, file_size_mb):
    """
    Bandwidth এবং file size থেকে transfer time বের করো।
    bandwidth_mbps = Megabits per second (লক্ষ্য করো, bits, bytes না)
    file_size_mb = Megabytes
    """
    # File size কে bits-এ রূপান্তর (1 byte = 8 bits)
    file_size_bits = file_size_mb * 8 * 1_000_000

    # bandwidth কে bits per second-এ রূপান্তর
    bandwidth_bps = bandwidth_mbps * 1_000_000

    time_seconds = file_size_bits / bandwidth_bps

    print(f"File size:  {file_size_mb} MB = {file_size_bits:,} bits")
    print(f"Bandwidth:  {bandwidth_mbps} Mbps")
    print(f"Transfer time: {time_seconds:.2f} seconds")

# উদাহরণ: 100Mbps connection-এ 50MB ফাইল
calculate_data_transfer(bandwidth_mbps=100, file_size_mb=50)
```

**Output:**
```
File size:  50 MB = 400,000,000 bits
Bandwidth:  100 Mbps
Transfer time: 4.00 seconds
```

---

## ৪. Signal Encoding — বিভিন্ন পদ্ধতি

শুধু voltage উঁচু-নিচু করাটা সবচেয়ে সহজ, কিন্তু সবচেয়ে ভালো পদ্ধতি না। বিভিন্ন সমস্যার সমাধানে বিভিন্ন encoding পদ্ধতি তৈরি হয়েছে।

### পদ্ধতি ১: NRZ (Non-Return to Zero)

সবচেয়ে সহজ। High voltage = 1, Low voltage = 0।

```
Data:    1  1  0  0  1  0  1  1

Signal:
5V  |‾‾‾‾‾‾‾‾‾|          |‾‾‾|     |‾‾‾‾‾‾‾‾‾|
    |         |          |   |     |         |
0V  |_________|__________|   |_____|         |___

     T1  T2   T3  T4  T5  T6  T7  T8
```

**সমস্যা:** যদি অনেক 1 বা অনেক 0 পরপর আসে, signal পরিবর্তন হয় না। Receiver sync হারিয়ে ফেলতে পারে।

### পদ্ধতি ২: Manchester Encoding (Ethernet ব্যবহার করে)

প্রতিটা bit-এর মাঝখানে একটা transition ঘটে।

```
নিয়ম:
  0 = Low → High (মাঝখানে উঠে যাওয়া)
  1 = High → Low (মাঝখানে নেমে আসা)

Data:    0          1          0          1

         ___        |  ___     ___        |  ___
        |   |       | |   |   |   |       | |   |
________|   |_______|_|   |___|   |_______|_|   |___

         ↑  ↑        ↑  ↑        ↑  ↑        ↑  ↑
       start mid    start mid  start mid    start mid
```

**সুবিধা:** প্রতিটা bit-এ অবশ্যই একটা transition আছে, তাই Receiver সহজে clock sync করতে পারে।

### পদ্ধতি ৩: 4B/5B Encoding (Fast Ethernet ব্যবহার করে)

4টা bit কে 5টা bit-এ রূপান্তর করা হয় — এমনভাবে যাতে পরপর বেশি 0 না আসে।

```python
# 4B/5B Encoding Table
ENCODING_4B5B = {
    '0000': '11110',   # data 0000 → encoded 11110
    '0001': '01001',
    '0010': '10100',
    '0011': '10101',
    '0100': '01010',
    '0101': '01011',
    '0110': '01110',
    '0111': '01111',
    '1000': '10010',
    '1001': '10011',
    '1010': '10110',
    '1011': '10111',
    '1100': '11010',
    '1101': '11011',
    '1110': '11100',
    '1111': '11101',
}

def encode_4b5b(data_bits):
    """
    4-bit data কে 5-bit encoded version-এ রূপান্তর করো।
    লক্ষ্য করো: প্রতিটা 5-bit pattern-এ কমপক্ষে দুটো 1 আছে।
    """
    if len(data_bits) % 4 != 0:
        # padding যোগ করো
        data_bits = data_bits.zfill(len(data_bits) + (4 - len(data_bits) % 4))

    encoded = []
    for i in range(0, len(data_bits), 4):
        nibble = data_bits[i:i+4]
        encoded_nibble = ENCODING_4B5B[nibble]
        print(f"  {nibble} → {encoded_nibble}")
        encoded.append(encoded_nibble)

    return ''.join(encoded)

print("4B/5B Encoding উদাহরণ:")
original = "10110100"   # 8 bits = 2 nibble
print(f"Original ({len(original)} bits): {original}")
encoded = encode_4b5b(original)
print(f"Encoded  ({len(encoded)} bits): {encoded}")
print(f"Overhead: {len(encoded) - len(original)} extra bits (25% বেশি)")
```

**Output:**
```
4B/5B Encoding উদাহরণ:
Original (8 bits): 10110100
  1011 → 10111
  0100 → 01010
Encoded  (10 bits): 1011101010
Overhead: 2 extra bits (25% বেশি)
```

### Signal Noise এবং Error

বাস্তব জীবনে signal সবসময় সুন্দর থাকে না। বিদ্যুৎ চৌম্বকীয় interference, তারের দূরত্ব, ইত্যাদি কারণে **noise** যোগ হয়।

```
পাঠানো signal:    ‾‾‾‾|____|‾‾‾‾|____|‾‾‾‾
                  1   0    1    0   1

প্রাপ্ত signal:   ‾‾~‾|_/\_|‾‾‾‾|_~__|‾‾~‾
                  noise যোগ হয়েছে!

Threshold দিয়ে সিদ্ধান্ত নেওয়া:
    > 2.5V  →  1
    < 2.5V  →  0
```

এজন্যই **Error Detection** (Checksum, CRC) এবং **Error Correction** (Hamming Code, Reed-Solomon) পদ্ধতি আছে।

```python
# Simple Parity Bit — Error Detection-এর সবচেয়ে সহজ রূপ

def add_parity_bit(data_bits, parity_type='even'):
    """
    Even Parity: মোট 1-এর সংখ্যা যাতে জোড় হয়।
    Odd Parity:  মোট 1-এর সংখ্যা যাতে বিজোড় হয়।
    
    একটা extra bit যোগ করি — যাতে 1-এর সংখ্যা
    আমাদের নিয়ম মেনে চলে। Receiver যদি দেখে
    নিয়ম ভাঙা, বুঝবে কোথাও error হয়েছে।
    """
    count_of_ones = data_bits.count('1')

    if parity_type == 'even':
        # জোড় সংখ্যক 1 চাই
        parity_bit = '0' if count_of_ones % 2 == 0 else '1'
    else:
        # বিজোড় সংখ্যক 1 চাই
        parity_bit = '1' if count_of_ones % 2 == 0 else '0'

    result = data_bits + parity_bit
    return result

def check_parity(received_bits, parity_type='even'):
    """Received data-তে error আছে কিনা পরীক্ষা করো।"""
    count_of_ones = received_bits.count('1')

    if parity_type == 'even':
        return count_of_ones % 2 == 0   # True মানে error নেই
    else:
        return count_of_ones % 2 != 0

# উদাহরণ
data = "1011001"
print(f"Original data:  {data}  (1-এর সংখ্যা: {data.count('1')})")

with_parity = add_parity_bit(data, 'even')
print(f"With parity:    {with_parity}")
print(f"Parity bit:     {with_parity[-1]}")
print()

# Transmission-এ error হলো (একটা bit flip হলো)
corrupted = list(with_parity)
corrupted[2] = '0' if corrupted[2] == '1' else '1'   # bit 2 flip!
corrupted = ''.join(corrupted)

print(f"Corrupted:      {corrupted}  ← bit 2 flip হয়েছে")
print(f"Error detected: {not check_parity(corrupted, 'even')}")
```

**Output:**
```
Original data:  1011001  (1-এর সংখ্যা: 4)
With parity:    10110010
Parity bit:     0

Corrupted:      10010010  ← bit 2 flip হয়েছে
Error detected: True
```

---

## ৫. তার থেকে বেতার — Physical Medium

Signal কীসের ভেতর দিয়ে যায় সেটাও গুরুত্বপূর্ণ।

### Copper Wire (তামার তার)

সবচেয়ে পুরনো এবং সবচেয়ে বেশি ব্যবহৃত। Voltage পরিবর্তন দিয়ে bit পাঠানো হয়।

```
Twisted Pair Cable (Ethernet-এ ব্যবহার হয়):
   ~~~~
  /    \    8টা তার = 4 pair
 /      \   Twist করা থাকে electromagnetic interference কমাতে
 \      /
  \    /
   ~~~~

CAT5e: 1Gbps পর্যন্ত, 100 মিটার
CAT6:  10Gbps পর্যন্ত, 55 মিটার (10Gbps-এ)
CAT6a: 10Gbps পর্যন্ত, 100 মিটার
```

### Fiber Optic Cable (আলোর তার)

তামার পরিবর্তে আলো ব্যবহার হয়। Bit represent হয় আলোর pulse দিয়ে।

```
1 = আলোর pulse আছে  💡
0 = আলোর pulse নেই  ∅

Glass core (কাচের কেন্দ্র) দিয়ে আলো যায়।
Total Internal Reflection-এর কারণে আলো বাঁকা পথেও যেতে পারে।

গতি: তামার তুলনায় অনেক বেশি, প্রায় আলোর গতির 2/3
দূরত্ব: কোনো amplification ছাড়া 100km পর্যন্ত
```

### Wireless (বেতার)

ইলেক্ট্রোম্যাগনেটিক তরঙ্গ ব্যবহার হয়।

```
Binary → Electric signal → Radio wave → Antenna থেকে broadcast
Receiver antenna → Radio wave → Electric signal → Binary

WiFi 2.4GHz বা 5GHz frequency ব্যবহার করে।
প্রতিটা '0' এবং '1' এর জন্য তরঙ্গের phase বা amplitude পরিবর্তন হয়।
```

```
BPSK (Binary Phase Shift Keying) — WiFi-এ ব্যবহৃত পদ্ধতি:

bit 0: ~~~  (0° phase)
bit 1: ~~~  (180° phase, উল্টো দিক)

Amplitude অপরিবর্তিত থাকে, কিন্তু wave উল্টে যায়।
Receiver phase পরীক্ষা করে 0 নাকি 1 বোঝে।
```

---

## ৬. Data কে ভাঙো — Framing ও Packets

এখন বুঝলাম bit কীভাবে যায়। কিন্তু যদি 1GB ফাইল পাঠাতে হয়? সেটাকে একসাথে পাঠানো যাবে না।

**সমস্যাগুলো:**
একটা বড় stream ভুল হলে পুরোটা আবার পাঠাতে হবে। অনেক user একই সময়ে পাঠাতে পারবে না। কোনো error correction সম্ভব না।

**সমাধান:** ছোট ছোট টুকরোয় ভাগ করো। এই টুকরোগুলোকে বলে **Frame** (Data Link Layer-এ) বা **Packet** (Network Layer-এ) বা **Segment** (Transport Layer-এ)।

### Ethernet Frame গঠন

```
┌─────────────┬──────────────┬──────────────┬──────┬─────────────┬─────┐
│  Preamble   │  Destination │    Source    │ Type │    Data     │ FCS │
│  7+1 bytes  │  MAC 6 bytes │  MAC 6 bytes │ 2 B  │ 46-1500 B   │ 4 B │
└─────────────┴──────────────┴──────────────┴──────┴─────────────┴─────┘

Preamble:     10101010... × 7 = "আমি data পাঠাতে শুরু করছি" signal
Preamble SFD: 10101011    = "এখন আসল frame শুরু হচ্ছে"
Destination:  কোথায় যাবে (MAC address)
Source:       কে পাঠাচ্ছে (MAC address)
Type:         ভেতরে কী আছে (IPv4=0x0800, IPv6=0x86DD, ARP=0x0806)
Data:         আসল payload
FCS:          Frame Check Sequence, error detection-এর জন্য
```

```python
import struct

def create_ethernet_frame(dest_mac, src_mac, ethertype, payload):
    """
    একটা Ethernet frame তৈরি করো।
    এটা conceptual demonstration — real network এই bytes পাঠায়।
    """
    # MAC address গুলো bytes-এ রূপান্তর করো
    # "AA:BB:CC:DD:EE:FF" → b'\xaa\xbb\xcc\xdd\xee\xff'
    dest_bytes = bytes(int(x, 16) for x in dest_mac.split(':'))
    src_bytes  = bytes(int(x, 16) for x in src_mac.split(':'))

    # EtherType bytes-এ
    type_bytes = struct.pack('!H', ethertype)  # '!H' = big-endian unsigned short

    payload_bytes = payload.encode('utf-8')

    # Frame জোড়া লাগাও
    frame = dest_bytes + src_bytes + type_bytes + payload_bytes

    return frame

def display_frame(frame):
    """Frame-এর hex dump দেখাও (Wireshark-এর মতো)।"""
    print("Ethernet Frame (Hex):")
    for i in range(0, len(frame), 16):
        chunk = frame[i:i+16]
        hex_part = ' '.join(f'{b:02x}' for b in chunk)
        ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f"  {i:04x}:  {hex_part:<48}  |{ascii_part}|")
    print(f"\nTotal size: {len(frame)} bytes")

# উদাহরণ frame তৈরি করো
frame = create_ethernet_frame(
    dest_mac="FF:FF:FF:FF:FF:FF",   # Broadcast — সবার কাছে যাবে
    src_mac="AA:BB:CC:DD:EE:01",    # আমার MAC
    ethertype=0x0800,                # IPv4
    payload="Hello!"
)

display_frame(frame)
```

**Output:**
```
Ethernet Frame (Hex):
  0000:  ff ff ff ff ff ff aa bb  cc dd ee 01 08 00 48 65  |..............He|
  0010:  6c 6c 6f 21                                        |llo!|

Total size: 20 bytes

        ┌──────────────────────┐  ┌──────────────────┐  ┌───────┐  ┌───────┐
        │ ff ff ff ff ff ff    │  │ aa bb cc dd ee 01│  │ 08 00 │  │48 65..│
        │   Destination MAC    │  │   Source MAC     │  │ IPv4  │  │ Data  │
        └──────────────────────┘  └──────────────────┘  └───────┘  └───────┘
```

### IP Packet গঠন

Ethernet Frame-এর Data অংশের ভেতরে থাকে **IP Packet**।

```
IPv4 Header (20 bytes minimum):
┌────┬────┬──────────────┬────────────────────────────────┐
│ VER│ IHL│     DSCP     │          Total Length           │
│ 4  │ 4  │     8 bits   │           16 bits               │
├────┴────┴──────────────┴────────────────────────────────┤
│         Identification          │Flags│  Fragment Offset │
│           16 bits               │ 3b  │     13 bits      │
├─────────────────────────────────┴─────┴──────────────────┤
│     TTL     │    Protocol    │      Header Checksum       │
│   8 bits    │    8 bits      │         16 bits            │
├─────────────┴────────────────┴────────────────────────────┤
│                   Source IP Address (32 bits)              │
├───────────────────────────────────────────────────────────┤
│                Destination IP Address (32 bits)            │
├───────────────────────────────────────────────────────────┤
│                    Data (Payload)                          │
└───────────────────────────────────────────────────────────┘

TTL (Time to Live): প্রতিটা router-এ 1 করে কমে। 0 হলে packet ফেলে দেওয়া হয়।
                    এতে করে হারানো packet অনন্তকাল ঘুরতে থাকে না।
Protocol: 6=TCP, 17=UDP, 1=ICMP (ping)
```

```python
import struct
import socket

def create_ip_header(src_ip, dest_ip, protocol, payload):
    """
    IPv4 header তৈরি করো।
    এই function টা বোঝায় header-এর প্রতিটা field কী কাজ করে।
    """
    version = 4          # IPv4
    ihl = 5              # Internet Header Length = 5 × 4 = 20 bytes
    tos = 0              # Type of Service (সাধারণত 0)
    total_length = 20 + len(payload)
    packet_id = 54321    # identification
    flags = 0            # fragmentation flags
    fragment_offset = 0
    ttl = 64             # Time to Live (Linux-এর default)
    checksum = 0         # প্রথমে 0, পরে calculate করব

    # IP address string থেকে 32-bit integer-এ রূপান্তর
    src_ip_packed  = socket.inet_aton(src_ip)
    dest_ip_packed = socket.inet_aton(dest_ip)

    # Header pack করো (checksum = 0 দিয়ে প্রথমে)
    # '!' = network byte order (big-endian)
    header = struct.pack(
        '!BBHHHBBH4s4s',
        (version << 4) | ihl,   # Version + IHL একসাথে
        tos,
        total_length,
        packet_id,
        (flags << 13) | fragment_offset,
        ttl,
        protocol,
        checksum,
        src_ip_packed,
        dest_ip_packed
    )

    return header

# উদাহরণ
src  = "192.168.1.10"
dest = "8.8.8.8"         # Google DNS
payload = b"Hello World"
protocol = 17            # UDP

header = create_ip_header(src, dest, protocol, payload)

print(f"IP Header size: {len(header)} bytes")
print(f"Source IP:      {src}")
print(f"Destination IP: {dest}")
print(f"Protocol:       {protocol} (UDP)")
print(f"TTL:            64")
print()
print("Hex dump:")
print(' '.join(f'{b:02x}' for b in header))
```

---

## ৭. MAC Address ও Data Link Layer

IP address হলো logical ঠিকানা। কিন্তু তার ভেতর দিয়ে signal পাঠাতে physical ঠিকানা দরকার — এটাই **MAC Address**।

```
MAC Address: AA:BB:CC:DD:EE:FF
             ├────────┤ ├──────┤
             OUI (3 bytes)  Device ID (3 bytes)
             manufacturer    unique number

OUI (Organizationally Unique Identifier):
AA:BB:CC = কোন কোম্পানি বানিয়েছে
DD:EE:FF = সেই কোম্পানির specific device

উদাহরণ:
00:1A:2B = Cisco
F4:5C:89 = Intel
3C:15:C2 = Apple
```

### ARP — MAC খোঁজার পদ্ধতি

তোমার computer যদি `192.168.1.5`-এ packet পাঠাতে চায়, সে জানে না তার MAC address কী। **ARP** (Address Resolution Protocol) এই কাজ করে।

```
তোমার PC                    Network-এর সবাই
192.168.1.10                192.168.1.x
AA:BB:CC:DD:EE:01

Step 1: Broadcast পাঠাও
"আমি AA:BB:CC:DD:EE:01।
192.168.1.5 এর MAC address কেউ জানো?"
→ পাঠানো হলো FF:FF:FF:FF:FF:FF-এ (সবার কাছে)

Step 2: সঠিক device reply করে
192.168.1.5 (MAC: 11:22:33:44:55:66):
"আমি 192.168.1.5! আমার MAC হলো 11:22:33:44:55:66"

Step 3: ARP Cache-এ সংরক্ষণ
192.168.1.5 → 11:22:33:44:55:66  (cache-এ রাখা হলো)
এখন সরাসরি সেই MAC-এ পাঠাতে পারবে।
```

```python
import time

class ARPCache:
    """
    ARP Cache — IP থেকে MAC mapping সংরক্ষণ করে।
    বাস্তব OS-এও এরকম cache থাকে।
    """

    def __init__(self, ttl_seconds=300):
        self.cache = {}           # {ip: (mac, timestamp)}
        self.ttl = ttl_seconds    # 5 মিনিট পর expire

    def add_entry(self, ip, mac):
        """নতুন entry যোগ করো।"""
        self.cache[ip] = (mac, time.time())
        print(f"ARP Cache: {ip} → {mac} (added)")

    def lookup(self, ip):
        """IP address দিয়ে MAC খোঁজো।"""
        if ip in self.cache:
            mac, timestamp = self.cache[ip]
            age = time.time() - timestamp

            if age < self.ttl:
                print(f"ARP Cache HIT: {ip} → {mac} (age: {age:.1f}s)")
                return mac
            else:
                # Cache expire হয়ে গেছে
                del self.cache[ip]
                print(f"ARP Cache EXPIRED: {ip} (age: {age:.1f}s)")

        print(f"ARP Cache MISS: {ip} → ARP broadcast পাঠাতে হবে")
        return None

    def display(self):
        """Cache-এর সব entry দেখাও।"""
        print("\nARP Cache:")
        print(f"{'IP Address':<18} {'MAC Address':<20} {'Age'}")
        print("-" * 50)
        for ip, (mac, ts) in self.cache.items():
            age = time.time() - ts
            print(f"{ip:<18} {mac:<20} {age:.1f}s")

# Simulation
arp = ARPCache()

# কিছু entry যোগ করো (যেমন ARP reply পেলে হতো)
arp.add_entry("192.168.1.1",  "AA:BB:CC:11:22:33")   # Router
arp.add_entry("192.168.1.5",  "DD:EE:FF:44:55:66")   # PC
arp.add_entry("192.168.1.10", "11:22:33:AA:BB:CC")   # Phone

arp.display()

print("\nLookup পরীক্ষা:")
arp.lookup("192.168.1.1")    # Cache hit হবে
arp.lookup("192.168.1.99")   # Cache miss — ARP broadcast লাগবে
```

---

## ৮. IP Address — নেটওয়ার্কের ঠিকানা ব্যবস্থা

### IPv4 গভীরে

IPv4 address হলো 32 bits। আমরা পড়ি dotted decimal notation-এ।

```
Binary:          11000000 . 10101000 . 00000001 . 00001010
Decimal:            192   .   168   .     1    .    10
Notation:                      192.168.1.10
```

### Subnet Mask — নেটওয়ার্ক ভাগ করা

Subnet mask দিয়ে address-এর কোন অংশ "network" অংশ আর কোন অংশ "host" অংশ সেটা নির্ধারণ করা হয়।

```
IP:      192.168.1.10    = 11000000.10101000.00000001.00001010
Mask:    255.255.255.0   = 11111111.11111111.11111111.00000000
                                                        ↑
                                              শেষ 8 bit = host অংশ
                                              বাকি 24 bit = network অংশ

AND করলে পাই:
Network: 192.168.1.0     (এই network-এর সব device-এর এই অংশ এক)
Host:    .10             (এই specific device)
```

```python
def ip_to_binary(ip_str):
    """IP string কে binary-তে রূপান্তর করো।"""
    parts = ip_str.split('.')
    binary_parts = [format(int(p), '08b') for p in parts]
    return '.'.join(binary_parts)

def subnet_info(ip, mask):
    """IP ও Subnet Mask থেকে network information বের করো।"""

    # IP ও mask কে integer-এ রূপান্তর
    ip_parts   = [int(x) for x in ip.split('.')]
    mask_parts = [int(x) for x in mask.split('.')]

    # Network address (IP AND Mask)
    network = [ip_parts[i] & mask_parts[i] for i in range(4)]

    # Broadcast address (Network OR NOT Mask)
    broadcast = [network[i] | (255 - mask_parts[i]) for i in range(4)]

    # Host range
    first_host = network.copy()
    first_host[3] += 1

    last_host = broadcast.copy()
    last_host[3] -= 1

    # CIDR notation (mask-এ কতটা 1 আছে)
    cidr = sum(bin(m).count('1') for m in mask_parts)

    # মোট usable host সংখ্যা
    host_bits = 32 - cidr
    total_hosts = (2 ** host_bits) - 2   # Network + Broadcast বাদ দিয়ে

    print(f"IP Address:        {ip}")
    print(f"Subnet Mask:       {mask}")
    print(f"CIDR Notation:     {ip}/{cidr}")
    print()
    print(f"Binary IP:         {ip_to_binary(ip)}")
    print(f"Binary Mask:       {ip_to_binary(mask)}")
    print()
    print(f"Network Address:   {'.'.join(map(str, network))}")
    print(f"Broadcast Address: {'.'.join(map(str, broadcast))}")
    print(f"First Host:        {'.'.join(map(str, first_host))}")
    print(f"Last Host:         {'.'.join(map(str, last_host))}")
    print(f"Usable Hosts:      {total_hosts:,}")

subnet_info("192.168.1.10", "255.255.255.0")
print()
subnet_info("10.0.0.50", "255.255.0.0")
```

**Output:**
```
IP Address:        192.168.1.10
Subnet Mask:       255.255.255.0
CIDR Notation:     192.168.1.10/24

Binary IP:         11000000.10101000.00000001.00001010
Binary Mask:       11111111.11111111.11111111.00000000

Network Address:   192.168.1.0
Broadcast Address: 192.168.1.255
First Host:        192.168.1.1
Last Host:         192.168.1.254
Usable Hosts:      254
```

### NAT — একটা IP দিয়ে অনেক device

তোমার বাড়িতে হয়তো 10টা device আছে, কিন্তু ISP তোমাকে দিয়েছে একটাই Public IP। **NAT** (Network Address Translation) এই magic করে।

```
Private network (তোমার বাড়ি):
192.168.1.10  ─┐
192.168.1.11  ─┤
192.168.1.12  ─┤── [Router / NAT] ── Public IP: 203.0.113.5 ── Internet
192.168.1.13  ─┤
192.168.1.14  ─┘

Router একটা NAT Table রাখে:
┌─────────────────┬────────┬─────────────────┬────────┐
│  Private IP     │ Prv Port│  Public IP      │Pub Port│
├─────────────────┼─────────┼─────────────────┼────────┤
│ 192.168.1.10    │  45231  │ 203.0.113.5     │  10001 │
│ 192.168.1.11    │  52108  │ 203.0.113.5     │  10002 │
│ 192.168.1.12    │  38901  │ 203.0.113.5     │  10003 │
└─────────────────┴─────────┴─────────────────┴────────┘

Reply আসলে Router দেখে Port দেখে কার কাছে পাঠাতে হবে।
```

---

## ৯. Port — দরজার নম্বর

Port হলো 16-bit সংখ্যা (0 থেকে 65535)।

```
Well-known ports (0-1023):   System দখল করে রেখেছে
Registered ports (1024-49151): Applications register করতে পারে
Dynamic/Private (49152-65535): OS ইচ্ছেমতো assign করে
```

### Port কীভাবে কাজ করে?

```
তোমার PC একসাথে তিনটা কাজ করছে:
  - Google.com দেখছো          Port 54001 (browser)
  - WhatsApp Web খোলা          Port 54002 (browser)
  - VS Code থেকে GitHub-এ push Port 54003 (git)

সব একই IP (তোমার) থেকে যাচ্ছে, কিন্তু port আলাদা।
Reply আসলে OS port দেখে সঠিক application-কে দিয়ে দেয়।

                                             ┌─→ Port 54001 → Browser Tab 1
তোমার IP:Port → Internet → তোমার IP:PORT ──┼─→ Port 54002 → Browser Tab 2
                                             └─→ Port 54003 → VS Code
```

```python
import socket

def scan_common_ports(host, ports):
    """
    কিছু common port scan করো — কোনগুলো open আছে দেখো।
    এটা educational purpose-এ নিজের machine-এ করো।
    """
    print(f"Port scan: {host}")
    print("-" * 40)

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)   # 1 second timeout

        result = sock.connect_ex((host, port))
        # connect_ex: 0 মানে success (port open), অন্য number মানে error (closed)

        status = "OPEN  ✓" if result == 0 else "closed"
        service = {
            80: "HTTP", 443: "HTTPS", 22: "SSH",
            21: "FTP", 25: "SMTP", 3306: "MySQL",
            5432: "PostgreSQL", 6379: "Redis", 27017: "MongoDB",
            8080: "HTTP-alt"
        }.get(port, "unknown")

        print(f"  Port {port:5d} ({service:<12}): {status}")
        sock.close()

# localhost scan (নিজের machine)
# scan_common_ports("127.0.0.1", [22, 80, 443, 3306, 5432, 6379, 8080])

# Port কীভাবে একটা server bind করে দেখাই
def demonstrate_port_binding():
    """Port binding concept দেখাও।"""
    print("\nPort Binding Demonstration:")

    # একটা socket তৈরি করো
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # SO_REUSEADDR: প্রোগ্রাম বন্ধ হওয়ার পরও port টা
    # আবার ব্যবহার করা যাবে (TIME_WAIT state এড়াতে)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    port = 9999
    server_sock.bind(('127.0.0.1', port))
    server_sock.listen(1)

    local_addr = server_sock.getsockname()
    print(f"  Server bound to: {local_addr[0]}:{local_addr[1]}")
    print(f"  OS-কে বললাম: Port {port}-এ আসা সব connection আমাকে দাও")
    print(f"  Status: LISTENING...")

    server_sock.close()
    print(f"  Socket closed, Port {port} মুক্ত হলো।")

demonstrate_port_binding()
```

---

## ১০. Socket — যোগাযোগের জানালা

Socket হলো OS-এর দেওয়া একটা interface — যেটা দিয়ে একটা program network-এ কথা বলতে পারে।

> **Analogy:** Socket হলো একটা বিশেষ ধরনের ফোন। তুমি OS-এর কাছ থেকে একটা ফোন চাও, একটা নম্বরে (IP:Port) লাগাও, তারপর কথা বলো। কথা শেষে ফোন রেখে দাও।

### Socket-এর জীবনচক্র

```
SERVER দিক:
socket() → bind() → listen() → accept() → recv()/send() → close()
   │          │         │          │
   │          │         │          └── Client-এর connection গ্রহণ
   │          │         └─────────── Connection আসার জন্য অপেক্ষা
   │          └───────────────────── Port-এ নিজেকে assign করো
   └──────────────────────────────── OS-এর কাছ থেকে socket তৈরি করো

CLIENT দিক:
socket() → connect() → send()/recv() → close()
   │           │
   │           └── Server-এর IP:Port-এ সংযোগ করো
   └────────── Socket তৈরি করো
```

```python
import socket
import threading
import time

def run_echo_server():
    """
    Echo Server: যা পাঠাবে তাই ফেরত দেবে।
    এটা Socket programming-এর সবচেয়ে সহজ উদাহরণ।
    """
    server = socket.socket(
        socket.AF_INET,    # Address Family: IPv4
        socket.SOCK_STREAM # Socket Type: TCP (stream)
    )
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 9876))
    server.listen(5)   # সর্বোচ্চ 5টা pending connection রাখতে পারবে

    print("[Server] Port 9876-এ শুনছি...")

    # একটাই client-এর জন্য
    conn, addr = server.accept()   # blocking call — client না আসা পর্যন্ত থামে
    print(f"[Server] {addr} থেকে connection পেলাম!")

    while True:
        data = conn.recv(1024)    # সর্বোচ্চ 1024 bytes পড়ো
        if not data:
            break   # Client চলে গেছে

        message = data.decode('utf-8')
        print(f"[Server] পেলাম: '{message}'")

        # Echo করে ফেরত দাও
        response = f"Echo: {message}"
        conn.send(response.encode('utf-8'))
        print(f"[Server] পাঠালাম: '{response}'")

    conn.close()
    server.close()
    print("[Server] বন্ধ হলাম।")


def run_echo_client(messages):
    """Client: Server-এ message পাঠাও।"""
    time.sleep(0.5)   # Server start হওয়ার জন্য অল্প অপেক্ষা

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9876))
    print(f"[Client] Server-এ connected!")

    for msg in messages:
        client.send(msg.encode('utf-8'))
        print(f"[Client] পাঠালাম: '{msg}'")

        response = client.recv(1024).decode('utf-8')
        print(f"[Client] পেলাম: '{response}'")
        time.sleep(0.3)

    client.close()
    print("[Client] Disconnected.")


# Server ও Client আলাদা thread-এ চালাও
server_thread = threading.Thread(target=run_echo_server)
client_thread = threading.Thread(
    target=run_echo_client,
    args=(["সালাম!", "কেমন আছো?", "ভালো থেকো!"],)
)

server_thread.start()
client_thread.start()
client_thread.join()
server_thread.join()
```

**Output:**
```
[Server] Port 9876-এ শুনছি...
[Client] Server-এ connected!
[Server] ('127.0.0.1', 49821) থেকে connection পেলাম!
[Client] পাঠালাম: 'সালাম!'
[Server] পেলাম: 'সালাম!'
[Server] পাঠালাম: 'Echo: সালাম!'
[Client] পেলাম: 'Echo: সালাম!'
[Client] পাঠালাম: 'কেমন আছো?'
[Server] পেলাম: 'কেমন আছো?'
[Server] পাঠালাম: 'Echo: কেমন আছো?'
[Client] পেলাম: 'Echo: কেমন আছো?'
...
```

### Socket Buffer — একটা গুরুত্বপূর্ণ detail

OS প্রতিটা socket-এর জন্য দুটো buffer রাখে:

```
Send Buffer:    তোমার program → [buffer] → Network
Receive Buffer: Network → [buffer] → তোমার program

কেন buffer দরকার?
→ তুমি হয়তো 1MB একসাথে send করলে, কিন্তু network হয়তো
  1460 bytes (MTU) করে নিতে পারে। Buffer এই পার্থক্য সামলায়।
→ Data আসলেই program সঙ্গে সঙ্গে read না করলেও হারায় না।
```

```python
# Buffer এর behavior দেখাই

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Buffer size জানো
send_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
recv_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

print(f"Default Send Buffer: {send_buf:,} bytes ({send_buf/1024:.0f} KB)")
print(f"Default Recv Buffer: {recv_buf:,} bytes ({recv_buf/1024:.0f} KB)")

# Buffer size পরিবর্তন করো
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)  # 64 KB
new_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print(f"New Send Buffer:     {new_buf:,} bytes ({new_buf/1024:.0f} KB)")

sock.close()
```

---

## ১১. TCP — নির্ভরযোগ্যতার বিজ্ঞান

TCP শুধু "reliable" — এই একটা কথায় শেষ না। এর পেছনে অনেক জটিল mechanism আছে।

### TCP Segment Structure

```
TCP Segment Header (20+ bytes):
┌─────────────────┬───────────────────────────────────┐
│  Source Port    │         Destination Port           │
│    16 bits      │           16 bits                  │
├─────────────────┴───────────────────────────────────┤
│              Sequence Number (32 bits)               │
│   পাঠানো data-র byte number (কোন byte থেকে শুরু)  │
├─────────────────────────────────────────────────────┤
│            Acknowledgment Number (32 bits)           │
│   পরের কোন byte-এর জন্য অপেক্ষা করছি             │
├────────┬───────────────────────────┬─────────────────┤
│Data    │ U│A│P│R│S│F│              │                 │
│Offset  │ R│C│S│S│Y│I│  Reserved   │   Window Size   │
│4 bits  │ G│K│H│T│N│N│             │   16 bits       │
├────────┴───────────────────────────┴─────────────────┤
│           Checksum          │      Urgent Pointer     │
│           16 bits           │         16 bits         │
├─────────────────────────────┴─────────────────────────┤
│                    Data (Payload)                      │
└───────────────────────────────────────────────────────┘

SYN = Synchronize (connection শুরু)
ACK = Acknowledge (পেয়েছি জানানো)
FIN = Finish (connection শেষ)
RST = Reset (জরুরি বন্ধ)
PSH = Push (তাড়াতাড়ি application-এ দাও)
```

### Sequence ও Acknowledgment — কীভাবে reliability আসে

```
Client পাঠাচ্ছে 3000 bytes:

Segment 1:  SEQ=1,    data: bytes 1-1000
Segment 2:  SEQ=1001, data: bytes 1001-2000
Segment 3:  SEQ=2001, data: bytes 2001-3000

Server reply করছে:
ACK=1001   → "1 থেকে 1000 পেয়েছি, এখন 1001 চাই"
ACK=2001   → "1001 থেকে 2000 পেয়েছি, এখন 2001 চাই"
ACK=3001   → "সব পেয়েছি!"

যদি Segment 2 হারিয়ে যায়:
Server: ACK=1001 পাঠাতেই থাকবে (duplicate ACK)
Client: বুঝবে 1001 হারিয়েছে, আবার পাঠাবে। এটাকে বলে Retransmission।
```

```python
import time
import random
from collections import OrderedDict

class TCPSimulator:
    """
    TCP-এর core reliability mechanism simulate করো।
    এটা একটা simplified version — বাস্তব TCP অনেক বেশি জটিল।
    """

    def __init__(self, packet_loss_rate=0.2):
        self.packet_loss_rate = packet_loss_rate  # 20% packet loss
        self.sender_window = OrderedDict()        # পাঠানো কিন্তু ACK না পাওয়া segments
        self.next_seq = 0
        self.received_data = {}
        self.expected_seq = 0

    def send_segment(self, seq_num, data):
        """একটা segment পাঠাও (simulated)।"""

        # Random packet loss simulate করো
        if random.random() < self.packet_loss_rate:
            print(f"  ✗ Segment SEQ={seq_num} হারিয়ে গেল! (simulated loss)")
            return False

        print(f"  → Segment SEQ={seq_num}, data='{data}' পাঠানো হলো")
        return True

    def receive_segment(self, seq_num, data):
        """একটা segment পেলাম।"""
        self.received_data[seq_num] = data

        # Cumulative ACK: in-order পাওয়া data পর্যন্ত ACK করো
        while self.expected_seq in self.received_data:
            self.expected_seq += 1

        ack_num = self.expected_seq
        print(f"  ← ACK={ack_num} পাঠাচ্ছি (expected next: {ack_num})")
        return ack_num

    def simulate_transfer(self, message):
        """একটা message TCP-style transfer simulate করো।"""
        print(f"\n{'='*55}")
        print(f"Transferring: '{message}'")
        print(f"Packet loss rate: {self.packet_loss_rate*100:.0f}%")
        print('='*55)

        # Message কে ছোট টুকরোয় ভাগ করো
        chunk_size = 3
        chunks = [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]

        seq = 0
        total_attempts = 0

        for chunk in chunks:
            success = False
            attempts = 0

            while not success:
                attempts += 1
                total_attempts += 1
                success = self.send_segment(seq, chunk)

                if success:
                    ack = self.receive_segment(seq, chunk)
                    seq = ack   # পরের SEQ number
                else:
                    # Retransmission
                    wait = 0.5 * attempts   # Exponential backoff
                    print(f"    ⏳ {wait:.1f}s পরে আবার চেষ্টা (attempt {attempts})...")
                    time.sleep(wait * 0.1)  # Simulation-এ ছোট করলাম

        print(f"\nTransfer সম্পূর্ণ!")
        print(f"Total segments sent: {total_attempts} ({total_attempts - len(chunks)} retransmissions)")
        reconstructed = ''.join(self.received_data[k] for k in sorted(self.received_data))
        print(f"Received message: '{reconstructed}'")

random.seed(42)   # Reproducible results
sim = TCPSimulator(packet_loss_rate=0.3)
sim.simulate_transfer("Hello World")
```

### TCP Flow Control — Receiver Overwhelm করবে না

```
Sender অনেক দ্রুত পাঠাচ্ছে, Receiver ধীরে process করছে।
Receiver-এর buffer ভরে যাচ্ছে!

Solution: Receiver তার Window Size জানায়।
Window Size = Receiver-এর বর্তমান buffer ফাঁকা জায়গা।

Receiver: "আমার buffer-এ এখন 16KB ফাঁকা আছে"
Sender: "ঠিক আছে, 16KB-র বেশি পাঠাবো না"
(Receiver কিছু process করলে আবার window size বাড়িয়ে জানায়)

Window Size = 0 হলে Sender থামে। এটাকে বলে Zero Window।
```

### TCP Congestion Control — Network ভিড় সামলানো

```
Slow Start:
    Connection শুরুতে cwnd (congestion window) = 1 MSS
    প্রতিটা ACK-এ cwnd দ্বিগুণ হয়
    1 → 2 → 4 → 8 → 16 → 32...

Congestion Avoidance:
    Threshold পেলে linear বৃদ্ধি পায়
    32 → 33 → 34 → 35...

Packet loss হলে:
    cwnd অর্ধেক করা হয় (TCP Reno)
    বা 1-এ ফিরে আসে (TCP Tahoe)

cwnd
 ^
 |          *
32|        *
 |       *
16|     *
 |    *
 8|   *
 |  *
 4| *
 | *
 2|*
 |*
 1|*
 +-------------------> time (RTT)
  Slow Start  Congestion
              Avoidance
```

---

## ১২. UDP — গতির দর্শন

UDP-র header মাত্র **8 bytes** — TCP-এর 20-এর তুলনায় অনেক কম।

```python
import struct
import socket

def create_udp_packet(src_port, dest_port, data):
    """
    UDP packet manually তৈরি করো।
    Header মাত্র 4টা field, মোট 8 bytes।
    """
    payload = data.encode('utf-8') if isinstance(data, str) else data

    # Length = header (8 bytes) + payload
    length = 8 + len(payload)

    # Checksum এর জন্য pseudo-header লাগে (src IP, dest IP, protocol, length)
    # এখানে আমরা checksum = 0 রাখছি (optional for UDP)
    checksum = 0

    # UDP Header: Source Port, Dest Port, Length, Checksum
    header = struct.pack('!HHHH', src_port, dest_port, length, checksum)

    packet = header + payload

    print(f"UDP Packet তৈরি হলো:")
    print(f"  Source Port:      {src_port}")
    print(f"  Destination Port: {dest_port}")
    print(f"  Length:           {length} bytes (8 header + {len(payload)} data)")
    print(f"  Checksum:         0x{checksum:04x}")
    print(f"  Data:             '{data}'")
    print(f"  Total:            {len(packet)} bytes")
    print()
    print("  Hex dump:")
    print("  " + ' '.join(f'{b:02x}' for b in header) + " | " +
          ' '.join(f'{b:02x}' for b in payload))
    print("  " + "─────────────────────────" + " | " + "─" * (len(payload)*3))
    print("  " + "      Header (8B)         | " + "    Payload")

    return packet

# DNS query packet simulate করো
create_udp_packet(
    src_port=54321,
    dest_port=53,      # DNS port
    data="google.com?"
)
```

### UDP Real-time Streaming কীভাবে কাজ করে

```
Video streaming (YouTube Live, Zoom):

Frame 1 → UDP packet 1 → পৌঁছালো ✓
Frame 2 → UDP packet 2 → হারিয়ে গেল ✗
Frame 3 → UDP packet 3 → পৌঁছালো ✓

TCP হলে: Frame 2-এর জন্য অপেক্ষা করতো। ততক্ষণ Frame 3 আটকে থাকতো।
UDP-তে: Frame 2 ignore করো, Frame 3 দেখাও। সামান্য glitch আসবে।

Real-time-এ সামান্য quality loss > কোনো delay
এই trade-off-ই UDP-কে streaming-এর জন্য পারফেক্ট করে।

RTP (Real-time Transport Protocol) UDP-র উপরে বসে
কিছু sequence number tracking যোগ করে (কিন্তু retransmit করে না)।
```

```python
import time
import random

def simulate_video_streaming(total_frames=20, packet_loss=0.15):
    """
    UDP-based video streaming simulate করো।
    দেখো TCP এবং UDP-তে কেমন ব্যবহারকারীর অভিজ্ঞতা হয়।
    """
    print(f"Video Streaming Simulation ({total_frames} frames, {packet_loss*100:.0f}% loss)")
    print("=" * 60)

    # UDP simulation
    print("\n[UDP Streaming]")
    udp_start = time.time()
    displayed = 0
    dropped = 0

    for frame_id in range(1, total_frames + 1):
        lost = random.random() < packet_loss

        if not lost:
            # Frame এখনই দেখাও
            print(f"  Frame {frame_id:2d}: ▶ দেখানো হলো (delay: ~0ms)")
            displayed += 1
        else:
            # Skip করো
            print(f"  Frame {frame_id:2d}: ✗ হারিয়ে গেল → skip")
            dropped += 1

    udp_time = time.time() - udp_start
    print(f"\n  মোট frames: {total_frames}")
    print(f"  দেখানো হলো: {displayed} ({displayed/total_frames*100:.0f}%)")
    print(f"  Drop হলো:   {dropped} ({dropped/total_frames*100:.0f}%)")
    print(f"  সময় লাগলো: {udp_time*1000:.0f}ms (simulated)")
    print(f"  অভিজ্ঞতা:  কিছু glitch কিন্তু real-time দেখা গেল ✓")

simulate_video_streaming()
```

---

## ১৩. HTTP — ওয়েবের ভাষা

HTTP শুধু একটা Protocol না, এটা একটা **text-based request-response protocol**। মানে HTTP message গুলো plain text — তুমি সেটা পড়তে পারবে।

### HTTP Request গভীরে

```
GET /search?q=bangladesh HTTP/1.1\r\n
Host: www.google.com\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n
Accept: text/html,application/xhtml+xml\r\n
Accept-Language: bn-BD,bn;q=0.9,en;q=0.8\r\n
Accept-Encoding: gzip, deflate, br\r\n
Connection: keep-alive\r\n
\r\n                         ← এই blank line মানে header শেষ
[Body — GET-এ সাধারণত খালি]

প্রতিটা line শেষ হয় \r\n (CRLF) দিয়ে — এটাই HTTP-র নিয়ম।
```

### HTTP Response গভীরে

```
HTTP/1.1 200 OK\r\n
Content-Type: text/html; charset=utf-8\r\n
Content-Length: 15243\r\n
Content-Encoding: gzip\r\n
Cache-Control: max-age=0\r\n
Set-Cookie: session=abc123; Path=/; HttpOnly\r\n
X-Frame-Options: SAMEORIGIN\r\n
\r\n
[Binary body — compressed HTML, CSS, JS]
```

```python
import socket

def http_get_request(host, path="/"):
    """
    Raw socket দিয়ে HTTP GET request করো।
    Browser যা করে ঠিক সেটাই manually করছি।
    """
    # TCP connection তৈরি করো (port 80 = HTTP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    print(f"TCP Connection: {host}:80...")
    sock.connect((host, 80))
    print("Connected!")

    # HTTP Request তৈরি করো (plain text)
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: MySimpleBrowser/1.0\r\n"
        f"Accept: text/html\r\n"
        f"Connection: close\r\n"
        f"\r\n"   # Header শেষের blank line
    )

    print(f"\nHTTP Request পাঠাচ্ছি:")
    print("-" * 40)
    print(request)

    # Request পাঠাও (bytes-এ encode করে)
    sock.send(request.encode('utf-8'))

    # Response পড়ো
    response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk

    sock.close()

    # Response parse করো
    response_text = response.decode('utf-8', errors='replace')
    header_end = response_text.find('\r\n\r\n')

    if header_end != -1:
        headers = response_text[:header_end]
        body = response_text[header_end+4:]

        print("HTTP Response Headers:")
        print("-" * 40)
        print(headers[:500])   # প্রথম 500 chars
        print("\nBody (প্রথম 200 chars):")
        print(body[:200])

    return response

# Example.com থেকে page আনো (simple test site)
# http_get_request("example.com", "/")
```

### HTTP/1.1 vs HTTP/2 vs HTTP/3

```
HTTP/1.1 (1997):
  - প্রতিটা request-এর জন্য আলাদা TCP connection (বা keep-alive)
  - Text-based headers (verbose)
  - Head-of-line blocking: একটা request শেষ না হলে পরেরটা আটকে
  
  Request 1: ──────────>
  Response 1:           <──────────
  Request 2:                       ──────────>
  Response 2:                                 <──────────

HTTP/2 (2015):
  - একটাই TCP connection, তার মধ্যে Multiplexing
  - Binary headers (HPACK compression)
  - Server Push (browser না চাইতেই CSS, JS পাঠাতে পারে)
  
  Request 1: ──────────>
  Request 2: ──────────>   (একসাথে!)
  Request 3: ──────────>
  Response 2: <──────────  (যেটা আগে ready সেটা আগে আসে)
  Response 1: <──────────
  Response 3: <──────────

HTTP/3 (2022):
  - TCP-র বদলে QUIC (UDP-র উপরে) ব্যবহার করে
  - Connection migration (WiFi থেকে 4G-তে গেলেও connection টিকে)
  - 0-RTT connection (আগে কথা হলে handshake ছাড়াই শুরু)
```

### Cookies, Sessions ও Authentication

```
HTTP stateless — মানে প্রতিটা request আলাদা, আগেরটার কথা মনে নেই।

তাহলে login কীভাবে কাজ করে?

Step 1: POST /login
        username=alice&password=secret123
        
Step 2: Server verify করে, response-এ cookie set করে:
        Set-Cookie: session_id=xK9mP2qR...; HttpOnly; Secure
        
Step 3: Browser পরের প্রতিটা request-এ cookie পাঠায়:
        Cookie: session_id=xK9mP2qR...
        
Step 4: Server cookie দেখে বোঝে এটা Alice
        
HttpOnly: JavaScript পড়তে পারবে না (XSS protection)
Secure:   শুধু HTTPS-এ পাঠাবে
SameSite: Cross-site request-এ পাঠাবে না (CSRF protection)
```

```python
def parse_http_response(raw_response):
    """
    HTTP Response parse করো। Browser যা করে।
    """
    # Header ও Body আলাদা করো
    if '\r\n\r\n' in raw_response:
        header_section, body = raw_response.split('\r\n\r\n', 1)
    else:
        header_section, body = raw_response, ""

    lines = header_section.split('\r\n')

    # Status line parse করো (যেমন: "HTTP/1.1 200 OK")
    status_line = lines[0]
    parts = status_line.split(' ', 2)
    version = parts[0]
    status_code = int(parts[1])
    reason = parts[2] if len(parts) > 2 else ""

    # Headers parse করো
    headers = {}
    for line in lines[1:]:
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip().lower()] = value.strip()

    # Status code মানে বোঝাও
    status_meanings = {
        200: "OK — সফল",
        201: "Created — নতুন resource তৈরি হয়েছে",
        301: "Moved Permanently — স্থায়ীভাবে সরানো হয়েছে",
        302: "Found — সাময়িকভাবে অন্যত্র",
        400: "Bad Request — ভুল request",
        401: "Unauthorized — login করো",
        403: "Forbidden — অনুমতি নেই",
        404: "Not Found — খুঁজে পাওয়া যায়নি",
        500: "Internal Server Error — server-এ সমস্যা",
        503: "Service Unavailable — server ব্যস্ত বা বন্ধ",
    }

    meaning = status_meanings.get(status_code, "অজানা status")

    print(f"HTTP Version:  {version}")
    print(f"Status Code:   {status_code} ({reason})")
    print(f"মানে:         {meaning}")
    print(f"\nHeaders ({len(headers)} টি):")
    for k, v in headers.items():
        print(f"  {k}: {v}")
    print(f"\nBody length: {len(body)} characters")

# Test করো
sample_response = """HTTP/1.1 200 OK\r
Content-Type: text/html; charset=utf-8\r
Content-Length: 13\r
Cache-Control: no-cache\r
Set-Cookie: session=abc123; HttpOnly\r
\r
Hello, World!"""

parse_http_response(sample_response)
```

---

## ১৪. সম্পূর্ণ যাত্রা — google.com লিখলে কী হয়

এখন সব একসাথে দেখি। তুমি browser-এ `https://www.google.com` enter চাপলে কী হয় — একেবারে bit level থেকে।

```
তোমার browser: "https://www.google.com"
     │
     ▼ Step 1: URL Parse
     │
     ├── Protocol: HTTPS
     ├── Host: www.google.com
     ├── Port: 443 (HTTPS default)
     └── Path: /

     │
     ▼ Step 2: DNS Resolution
     │
     ├── Browser DNS cache check → Miss
     ├── OS DNS cache check → Miss
     ├── Router cache check → Miss
     └── UDP packet → 8.8.8.8:53 (Google DNS)
         "www.google.com = কোন IP?"
         ↓
         DNS Reply: "142.250.77.46"

     │
     ▼ Step 3: TCP 3-Way Handshake (142.250.77.46:443)
     │
     ├── SYN    → Google Server (ISN=random, যেমন: 2847361920)
     ├── SYN-ACK← Google Server (ISN=1029384756, ACK=2847361921)
     └── ACK    → Google Server

     │
     ▼ Step 4: TLS 1.3 Handshake
     │
     ├── Client Hello (supported cipher suites, random bytes)
     ├── Server Hello (chosen cipher, certificate)
     ├── Certificate verify (Google-এর cert valid কিনা)
     ├── Key Exchange (Diffie-Hellman)
     └── Encrypted connection ready!

     │
     ▼ Step 5: HTTP/2 Request (encrypted)
     │
     ├── HEADERS frame:
     │   :method: GET
     │   :path: /
     │   :scheme: https
     │   :authority: www.google.com
     │   user-agent: Chrome/120...
     │   accept-language: bn-BD
     └── (Compressed with HPACK)

     │
     ▼ Step 6: Server Processing
     │
     ├── Google load balancer request receive করে
     ├── Appropriate server-এ forward করে
     ├── Search index থেকে data আনে
     ├── Personalization apply করে
     └── HTML generate করে

     │
     ▼ Step 7: HTTP/2 Response (encrypted)
     │
     ├── HEADERS frame: :status: 200
     ├── DATA frame: HTML (gzip compressed)
     └── বড় হলে multiple DATA frames

     │
     ▼ Step 8: Browser Rendering
     │
     ├── HTML parse → DOM tree
     ├── CSS parse → CSSOM
     ├── DOM + CSSOM → Render tree
     ├── Layout calculation
     ├── Paint → GPU-তে texture upload
     └── তুমি Google.com দেখতে পেলে! ✓
```

এই পুরো প্রক্রিয়া মাত্র **100-500 millisecond**-এ হয়ে যায়!

### কতটা Binary Data যায়?

```python
def estimate_google_load():
    """
    Google.com লোড করতে কতটা binary data যায় estimate করো।
    এই সংখ্যাগুলো approximate, real মান browser DevTools-এ দেখা যায়।
    """

    resources = [
        ("HTML (Main Page)",        45_000,  "text"),
        ("JavaScript (main bundle)", 250_000, "binary"),
        ("JavaScript (other)",       180_000, "binary"),
        ("CSS",                       30_000,  "text"),
        ("Images/Icons",              80_000,  "binary"),
        ("Fonts",                     60_000,  "binary"),
        ("XHR/API calls",             15_000,  "text"),
    ]

    print(f"{'Resource':<28} {'Size':>10} {'Bits':>14} {'Type'}")
    print("-" * 65)

    total_bytes = 0
    for name, size, rtype in resources:
        bits = size * 8
        total_bytes += size
        print(f"{name:<28} {size:>8,}B {bits:>13,} {rtype}")

    print("-" * 65)
    total_bits = total_bytes * 8
    print(f"{'TOTAL':<28} {total_bytes:>8,}B {total_bits:>13,}")
    print()
    print(f"মোট bytes: {total_bytes/1024:.1f} KB")
    print(f"মোট bits:  {total_bits:,}")
    print()
    print("এই পুরো data:")
    print(f"  100Mbps connection-এ: {total_bytes*8/100_000_000*1000:.0f}ms")
    print(f"  10Mbps connection-এ:  {total_bytes*8/10_000_000*1000:.0f}ms")
    print(f"  1Mbps connection-এ:   {total_bytes*8/1_000_000*1000:.0f}ms")
    print()
    print("Ethernet Frame-এ ভাগ করলে:")
    mtu = 1460  # TCP MSS (Maximum Segment Size) = 1500 - 20(IP) - 20(TCP)
    frames = -(-total_bytes // mtu)  # ceiling division
    print(f"  প্রতিটা frame সর্বোচ্চ {mtu} bytes data নিতে পারে")
    print(f"  মোট frames প্রয়োজন: ~{frames:,}")

estimate_google_load()
```

**Output:**
```
Resource                      Size          Bits  Type
-----------------------------------------------------------------
HTML (Main Page)           45,000B      360,000  text
JavaScript (main bundle)  250,000B    2,000,000  binary
JavaScript (other)        180,000B    1,440,000  binary
CSS                        30,000B      240,000  text
Images/Icons               80,000B      640,000  binary
Fonts                      60,000B      480,000  binary
XHR/API calls              15,000B      120,000  text
-----------------------------------------------------------------
TOTAL                     660,000B    5,280,000

মোট bytes: 644.5 KB
মোট bits:  5,280,000

এই পুরো data:
  100Mbps connection-এ: 422ms
  10Mbps connection-এ:  4224ms
  1Mbps connection-এ:   42240ms

Ethernet Frame-এ ভাগ করলে:
  প্রতিটা frame সর্বোচ্চ 1460 bytes data নিতে পারে
  মোট frames প্রয়োজন: ~452
```

---

## পরিশিষ্ট — সংক্ষিপ্ত সারাংশ

```
Physical Layer:  Bits = Voltage level = Electric Signal
                 0 → Low voltage (~0V)
                 1 → High voltage (~3.3V বা +2.5V)

Data Link Layer: MAC Address দিয়ে local delivery
                 Ethernet Frame: Preamble|Dst MAC|Src MAC|Type|Data|FCS

Network Layer:   IP Address দিয়ে global routing
                 IP Packet: Header (TTL, src, dst, protocol) + Data

Transport Layer: Port দিয়ে সঠিক Application-এ
                 TCP: Reliable, ordered, connection-oriented
                 UDP: Fast, unreliable, connectionless

Application:     HTTP, DNS, SMTP, FTP
                 Text-based request-response (HTTP)
```

### Cheat Sheet — মনে রাখার সহজ ছন্দ

```
Bit = সুইচ (on/off)
Byte = 8টা সুইচ
Encoding = বিদ্যুৎ সংকেত বানাওয়ার নিয়ম
Frame = Local delivery-র প্যাকেট (MAC address)
Packet = Internet delivery-র প্যাকেট (IP address)
Segment = Application delivery-র প্যাকেট (Port)
Socket = Program-এর network endpoint
TCP = নিশ্চিত, ধীর, ordered
UDP = অনিশ্চিত, দ্রুত, unordered
HTTP = ওয়েবের ভাষা (Request → Response)
HTTPS = HTTP + Encryption
```

---

> **শেষ কথা:** তুমি এখন জানো একটা `"H"` কীভাবে `01001000` হয়, সেটা কীভাবে `+2.5V` voltage pulse হয়, fiber-এ আলোর flash হয়, router পেরিয়ে যায়, TCP দিয়ে নির্ভরযোগ্যভাবে পৌঁছায়, HTTP দিয়ে browser-এ রেন্ডার হয়। এই পুরো জ্ঞানটা তুমি এখন বন্ধুকে বোঝাতে পারবে। নেটওয়ার্ক আর magic না — এটা physics, mathematics, আর carefully designed protocol-এর সমন্বয়।

---

*Document তৈরি: Bangla Networking Deep Dive | Binary → Signal → Protocol → Application*
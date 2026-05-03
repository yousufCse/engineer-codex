# 📘 CHAPTER 13 — File Upload ও Email
### "Binary Data ও Email Protocol — Multipart থেকে SMTP পর্যন্ত"
#### Progress: [██████████████░░░░░] 70%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 12](./chapter-12-nestjs.md) | [➡ Ch 14](./chapter-14-api-design.md)

---

## Multipart/form-data — কেন Special Encoding?

HTTP request-এর body সাধারণত JSON বা URL-encoded text। কিন্তু binary file (image, PDF, video) পাঠাতে হলে এই encodings কাজ করে না।

`multipart/form-data` encoding হলো file upload-এর জন্য তৈরি। এই encoding-এ request body multiple parts-এ বিভক্ত, প্রতিটা part একটা form field বা file। Parts-এর মাঝে একটা unique boundary string থাকে।

Browser এটা automatically করে — file input থেকে form submit করলে browser multipart/form-data encoding ব্যবহার করে। API client (Postman) এ manually `form-data` select করতে হয়।

---

## Streaming Upload vs Buffering

**Buffering:** পুরো file server-এর memory-তে load করা, তারপর process করা।

সমস্যা: 100MB file upload করলে 100MB RAM ব্যবহার। একসাথে অনেক upload হলে server out of memory।

**Streaming:** File আসার সাথে সাথে chunk করে process করা।

Streaming দিয়ে file disk-এ বা cloud-এ write করা যায় — RAM-এ পুরো file load না করে। Large file upload-এ streaming mandatory।

`multer` library Express-এ file upload handle করে। Memory storage (buffer) বা disk storage (file) — production-এ disk বা cloud storage।

---

## Local Storage vs Cloud Storage

**Local Storage:**

File server-এর disk-এ সংরক্ষণ। সহজ — filesystem API। সমস্যা:
- Multiple server থাকলে কোন server-এ file আছে?
- Server crash হলে file হারিয়ে যেতে পারে।
- CDN delivery কঠিন।
- Backup manually করতে হয়।

**Cloud Storage (S3, Cloudinary, GCS):**

File cloud-এ। Server stateless থাকে।
- Multiple server-এ একই file।
- High availability, redundancy।
- CDN integration সহজ।
- Backup automatic।

Production-এ সবসময় cloud storage।

---

## Cloudinary — কেন শুধু S3 নয়?

AWS S3 raw file storage — just store and serve। Cloudinary image ও video management platform:

**Image transformation on-the-fly:** URL parameter-এ resize, crop, format change। `https://res.cloudinary.com/demo/image/upload/w_300,h_300,c_fill/sample.jpg` — 300x300 crop।

**Automatic format optimization:** Browser WebP support করলে WebP, না করলে JPEG — automatically।

**CDN:** Global CDN-এ serve হয় — কাছের server থেকে fast।

**Smart cropping:** AI দিয়ে face detection করে crop।

**Lazy loading:** Blur placeholder, progressive loading।

Cloudinary-এর free tier ছোট project-এর জন্য যথেষ্ট।

---

## SMTP Protocol

Email পাঠানোর জন্য SMTP (Simple Mail Transfer Protocol) ব্যবহার হয়।

**SMTP Flow:**

Client SMTP server-এ connect করে। Sender address দেয়, recipient address দেয়, message দেয়। SMTP server email পাঠানোর দায়িত্ব নেয়।

**Ports:**
- 25: Original SMTP — ISP block করে spam কারণে।
- 465: SMTPS (SSL/TLS)।
- 587: SMTP with STARTTLS — modern standard।

**Gmail App Password:**

Google 2-Step Verification enable করলে third-party app-এ Gmail password সরাসরি কাজ করে না। App Password হলো Google-generated 16-character password শুধু সেই app-এর জন্য। Main password compromise না করে revoke করা যায়।

Production-এ SendGrid, AWS SES, Mailgun ব্যবহার করা উচিত — better deliverability, analytics।

---

## Email Deliverability — SPF, DKIM, DMARC

Email পাঠালেই spam folder-এ যাবে না — deliverability নিশ্চিত করতে হয়।

**SPF (Sender Policy Framework):**

DNS TXT record যেটা বলে কোন mail server-গুলো এই domain থেকে email পাঠাতে authorized। Receiving server check করে sending server SPF-এ আছে কিনা।

**DKIM (DomainKeys Identified Mail):**

Email-এ cryptographic signature যোগ করা। Receiving server verify করে email transit-এ modify হয়নি এবং declared domain থেকেই এসেছে। Private key দিয়ে sign, public key DNS-এ।

**DMARC (Domain-based Message Authentication, Reporting & Conformance):**

SPF বা DKIM fail করলে কী করবে — reject, quarantine (spam), none। Reports পাঠানো — কে আপনার domain ব্যবহার করছে।

এই তিনটা ছাড়া email spam folder-এ যাওয়ার সম্ভাবনা বেশি।

---

## Email Template Design Philosophy

Email HTML CSS সব browser-এর মতো নয় — email client (Gmail, Outlook) limited CSS support।

**Table-based layout:** Modern CSS grid/flexbox email-এ কাজ করে না। Table দিয়ে layout।

**Inline CSS:** External stylesheet email-এ strip হয়। Inline style।

**Responsive:** Mobile-first এখানেও।

**Template engine:** Handlebars, EJS, Mjml। Dynamic data যোগ করার জন্য।

**Plain text alternative:** HTML email-এর পাশাপাশি plain text version — accessibility এবং spam score।

Production-এ template rendering সহজ করতে `nodemailer` + template engine combination।

---

## মূল উপলব্ধি

File upload-এ buffering vs streaming বোঝা memory management-এর জন্য গুরুত্বপূর্ণ। Production-এ cloud storage mandatory। Email deliverability technical — SPF, DKIM, DMARC ছাড়া professional email service থেকেও spam folder-এ যেতে পারে। Cloudinary শুধু storage নয় — complete image pipeline।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 12](./chapter-12-nestjs.md) | [➡ Ch 14](./chapter-14-api-design.md)

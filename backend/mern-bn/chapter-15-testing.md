# 📘 CHAPTER 15 — Testing
### "Testing Pyramid থেকে TDD — গুণমানের নিশ্চয়তা"
#### Progress: [████████████████░░░] 80%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 14](./chapter-14-api-design.md) | [➡ Ch 16](./chapter-16-performance.md)

---

## কেন Test লিখবেন?

"Test লেখা সময় নষ্ট" — এই ধারণা ভুল। Test না লিখলে:

- Bug production-এ যায় — fix করা বেশি expensive।
- Feature যোগ করতে ভয় লাগে — পুরনো কিছু ভেঙে যাবে।
- Refactoring প্রায় অসম্ভব — কী break হবে জানা নেই।
- Documentation obsolete হয় — test নিজেই documentation।

Test লেখা short-term slow কিন্তু long-term fast।

---

## Testing Pyramid

Testing Pyramid হলো test strategy-র একটা visual model।

**Unit Tests (বেস — সবচেয়ে বেশি):**

একটা function বা class-এর একটা behavior test। Fast, isolated, cheap। হাজারো unit test মিলিয়ে পুরো codebase cover।

**Integration Tests (মাঝামাঝি):**

একাধিক component মিলে কাজ করে কিনা। Database-সহ service test, HTTP endpoint test। Slower এবং more complex।

**E2E Tests (শীর্ষ — সবচেয়ে কম):**

পুরো system — UI থেকে database পর্যন্ত। Browser automation (Playwright, Cypress)। Slowest, most brittle, most expensive।

**Ice Cream Cone Anti-pattern:** বেশি E2E, কম unit — এটা উল্টো। E2E slow এবং brittle — minor UI change-এ break করে।

---

## TDD vs BDD

**TDD (Test-Driven Development):**

Test আগে, code পরে। Red-Green-Refactor cycle:
1. **Red:** Failing test লেখো।
2. **Green:** Minimum code লেখো test pass করাতে।
3. **Refactor:** Code improve করো — test green রেখে।

TDD design improvement করে — testable code naturally loose coupling এবং single responsibility মানে।

**BDD (Behavior-Driven Development):**

TDD-এর extension। Test user behavior describe করে — technical implementation নয়। `describe`, `it`, `expect` syntax। "When user logs in with valid credentials, it should return a JWT token।"

---

## FIRST Principles — ভালো Unit Test-এর গুণাবলী

**Fast:** Unit test milliseconds-এ চলা উচিত। Slow test কেউ চালায় না।

**Independent:** Test-গুলো একে অপরের উপর নির্ভর করে না। যেকোনো order-এ চলে একই result।

**Repeatable:** যেকোনো environment-এ একই result। Time, random value-এর উপর নির্ভর করা উচিত নয় (mock করতে হবে)।

**Self-validating:** Test pass বা fail — manual inspection নয়।

**Timely:** Code লেখার সাথে সাথে test লেখা।

---

## Mocking, Stubbing, Faking — পার্থক্য

Unit test-এ real dependency (database, HTTP, filesystem) ব্যবহার করলে test slow হবে এবং external state-এর উপর নির্ভর করবে। Test double দিয়ে এই dependency replace করা হয়।

**Stub:** Fixed value return করে। Database stub সবসময় নির্দিষ্ট user return করে — query কী তাতে কিছু যায় আসে না।

**Mock:** Stub + verification। Mock verify করে নির্দিষ্ট method নির্দিষ্ট argument দিয়ে call হয়েছে কিনা।

**Fake:** Real implementation-এর সরলীকৃত version। In-memory database — real database-এর মতো কাজ করে কিন্তু file-এ লেখে না।

**Spy:** Real function-কে wrap করে call track করে — কিন্তু real behavior change করে না।

---

## Test Isolation

Test isolation মানে প্রতিটা test independent।

**Database isolation:**

Integration test-এ প্রতিটা test-এর আগে database clean করা — seed data দেওয়া, test শেষে rollback।

Transaction-based isolation: Test একটা transaction-এ চলে, test শেষে rollback — database আগের state-এ।

**Time isolation:**

`Date.now()` বা `new Date()` mock করা — test deterministic হয়।

**External API isolation:**

HTTP call mock করা — real API call না হলে test fast এবং reliable।

---

## Coverage Metrics

Code coverage measure করে কতটুকু code test-এ execute হয়েছে।

**Line Coverage:** কতটা line execute হয়েছে।

**Branch Coverage:** কতটা conditional branch (if/else) cover হয়েছে।

**Function Coverage:** কতটা function call হয়েছে।

**100% coverage = Bug-free নয়।**

Coverage দেখায় কোন code execute হয়েছে — কিন্তু সঠিকভাবে test হয়েছে কিনা দেখায় না। Wrong assertion দিলেও coverage 100%। Coverage একটা metric, goal নয়। Critical path-এ high coverage রাখো।

---

## Integration Test Strategy

Integration test database, HTTP, filesystem ব্যবহার করে — real interaction test।

**Supertest:** HTTP endpoint test-এর জন্য। Express app-কে actual server না করে in-process test।

**Test database:** Separate test database। Test-এর পরে cleanup।

**Transaction rollback:** প্রতিটা test একটা transaction-এ — শেষে rollback। Database state contamination নেই।

---

## মূল উপলব্ধি

Testing একটা skill — কোন test লিখতে হবে, কতটুকু mock করতে হবে, কতটা coverage দরকার — এগুলো judgment। Testing pyramid follow করলে fast এবং reliable test suite তৈরি হয়। TDD design improve করে। 100% coverage-এর পেছনে না দৌড়িয়ে meaningful test লেখো।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 14](./chapter-14-api-design.md) | [➡ Ch 16](./chapter-16-performance.md)

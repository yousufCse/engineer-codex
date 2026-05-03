# 📘 CHAPTER 12 — NestJS
### "Enterprise-grade Framework — Dependency Injection ও Modular Architecture"
#### Progress: [█████████████░░░░░░] 65%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 11](./chapter-11-security.md) | [➡ Ch 13](./chapter-13-file-upload-email.md)

---

## কেন NestJS?

Express unopinionated — কোনো structure নেই। ছোট project-এ এটা সুবিধা। কিন্তু বড় team-এ, enterprise application-এ এই freedom disorder হয়ে যায়। প্রতিটা developer নিজের মতো structure তৈরি করে, codebase inconsistent হয়।

NestJS এই সমস্যার সমাধান। Angular-এর architecture দেখে inspired — strongly opinionated, modular, TypeScript-first। Dependency Injection, Decorators, Modules — এই concepts দিয়ে maintainable এবং testable application structure enforce করে।

NestJS আসলে Express-এর উপরেই চলে (Fastify-তেও চালানো যায়) — কিন্তু উপরে একটা powerful abstraction layer যোগ করে।

---

## Dependency Injection — মূল ধারণা

Dependency Injection (DI) হলো একটা design pattern যেখানে একটা class তার dependency নিজে তৈরি না করে বাইরে থেকে পায়।

**DI ছাড়া:**

```typescript
class UserService {
  private db = new DatabaseConnection(); // UserService নিজে connection তৈরি করছে
}
```

সমস্যা: `UserService` এবং `DatabaseConnection` tightly coupled। Test করতে real database দরকার।

**DI সহ:**

```typescript
class UserService {
  constructor(private db: DatabaseConnection) {} // বাইরে থেকে দেওয়া হচ্ছে
}
```

এখন test করার সময় fake/mock `DatabaseConnection` দেওয়া যাবে।

---

## IoC Container

Inversion of Control (IoC) Container হলো DI-এর engine। এটা জানে কোন class কোন dependency চায়, সেই dependency কীভাবে তৈরি করতে হয়, এবং সব কিছু inject করে।

NestJS-এর IoC Container সব `@Injectable()` service track করে। কোনো controller বা service কোনো dependency চাইলে Container সেটা resolve করে দেয়।

**Lifecycle:** Container service-এর instance তৈরি করে। Default scope হলো Singleton — application lifetime-এ একটাই instance। Request scope-এ প্রতিটা request-এ নতুন instance।

---

## Decorators — TypeScript-এর Meta-programming

Decorator হলো TypeScript-এর (এবং upcoming JavaScript standard-এর) একটা feature — class, method, property, parameter-এ metadata attach করার mechanism।

**`@Controller('/users')`** — এই class একটা controller এবং `/users` route prefix handle করবে।

**`@Get('/:id')`** — এই method HTTP GET `/users/:id` handle করবে।

**`@Injectable()`** — এই class DI container-এ register হবে।

**`@Module()`** — NestJS module define করে।

Decorator-গুলো runtime-এ metadata যোগ করে (`reflect-metadata` library), NestJS এই metadata read করে behavior determine করে।

---

## Module System

NestJS application module-এর hierarchy দিয়ে organize হয়। প্রতিটা module একটা closely related feature-এর encapsulation।

একটা module-এ থাকে:
- **imports:** অন্য module যেটার service দরকার।
- **controllers:** HTTP request handle করার class।
- **providers:** Service, repository, factory — Injectable class।
- **exports:** অন্য module-এ share করা provider।

**Root Module:** `AppModule` — application-এর entry point। সব feature module এখানে import।

এই modular approach দিয়ে feature boundary স্পষ্ট। User feature এক module-এ, Product feature আরেক module-এ। Team আলাদা module-এ কাজ করতে পারে।

---

## Guards — Authorization

Guard হলো NestJS-এ authorization implement করার mechanism। Route handler execute হওয়ার আগে Guard চলে। Guard `true` return করলে execute হবে, `false` বা exception throw করলে না।

Express middleware দিয়ে authentication/authorization করা যায়, কিন্তু Guard semantic অর্থ বহন করে — এটা authorization-এর জন্য। Middleware request pipeline-এর part, Guard route-এর access control।

`@UseGuards(AuthGuard)` decorator দিয়ে controller বা specific route-এ apply করা যায়।

---

## Interceptors — Aspect-Oriented Programming

Interceptor হলো AOP (Aspect-Oriented Programming) concept-এর implementation। Cross-cutting concerns — logging, caching, response transformation — যেটা অনেক জায়গায় দরকার কিন্তু business logic নয়।

Interceptor আগে (`pre`) এবং পরে (`post`) response-এর উপর কাজ করতে পারে। Response format standardize করা — সব response `{ success: true, data: ... }` format-এ। Execution time log করা। Cache করা।

---

## Pipes — Validation ও Transformation

Pipe দুটো কাজ করে:

**Validation:** Request data validate করা। `ValidationPipe` + `class-validator` decorator দিয়ে DTO (Data Transfer Object) class-এ validation rules।

**Transformation:** Data type transform করা। URL parameter সবসময় string — `ParseIntPipe` দিয়ে integer-এ convert।

`@UsePipes(ValidationPipe)` দিয়ে globally বা specific route-এ apply।

---

## Exception Filters

NestJS-এ unhandled exception catch করে standardized error response পাঠানোর জন্য Exception Filter।

Built-in `HttpException` এবং subclass (`NotFoundException`, `BadRequestException`, `UnauthorizedException`) আছে। Custom exception তৈরি করা যায়।

Exception Filter সব unhandled exception catch করে — ধরা না পড়লে 500 Internal Server Error। বিভিন্ন exception type-এ আলাদা response।

---

## কেন TypeScript + NestJS?

TypeScript compile-time type checking দেয় — runtime error কমে। NestJS Decorator এবং DI TypeScript-এর type system-এর উপর নির্ভর করে।

TypeScript ছাড়া NestJS technically চলে কিন্তু অনেক সুবিধা হারায়। DI system type-based — TypeScript type দেখে injection করে।

---

## মূল উপলব্ধি

NestJS enterprise-grade application-এর জন্য একটা সম্পূর্ণ framework। Dependency Injection maintainability এবং testability নিশ্চিত করে। Module system feature isolation enforce করে। Guards, Interceptors, Pipes, Filters — প্রতিটার নির্দিষ্ট দায়িত্ব। Express-এর flexibility এবং NestJS-এর structure — দুটো জানলে যেকোনো project-এ সঠিক choice করা সম্ভব।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 11](./chapter-11-security.md) | [➡ Ch 13](./chapter-13-file-upload-email.md)

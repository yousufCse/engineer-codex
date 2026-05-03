
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 18 — Full E-commerce Project
# "NestJS + PostgreSQL + MongoDB — Production App"
# ⏱ ~120 মিনিট · Progress: [█████████████████░] 93%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Full NestJS project architecture
- ✅ Users + Auth module (PostgreSQL/Prisma)
- ✅ Products + Categories + Reviews (MongoDB/Mongoose)
- ✅ Orders + Payments module (PostgreSQL/Prisma)
- ✅ JWT Guard + Roles Guard
- ✅ Cloudinary image upload
- ✅ Complete Swagger documentation
- ✅ Production ready

---

## 📁 Project Structure

```
myshop-api/
├── src/
│   ├── main.ts
│   ├── app.module.ts
│   ├── common/
│   │   ├── decorators/
│   │   │   ├── current-user.decorator.ts
│   │   │   ├── public.decorator.ts
│   │   │   └── roles.decorator.ts
│   │   ├── guards/
│   │   │   ├── jwt-auth.guard.ts
│   │   │   └── roles.guard.ts
│   │   ├── interceptors/
│   │   │   └── transform.interceptor.ts
│   │   ├── filters/
│   │   │   └── http-exception.filter.ts
│   │   └── pipes/
│   │       └── parse-object-id.pipe.ts
│   ├── config/
│   │   └── configuration.ts
│   ├── prisma/
│   │   ├── prisma.module.ts
│   │   └── prisma.service.ts
│   ├── auth/
│   │   ├── auth.module.ts
│   │   ├── auth.service.ts
│   │   ├── auth.controller.ts
│   │   ├── dto/
│   │   │   ├── register.dto.ts
│   │   │   └── login.dto.ts
│   │   └── strategies/
│   │       └── jwt.strategy.ts
│   ├── users/
│   │   ├── users.module.ts
│   │   ├── users.service.ts
│   │   ├── users.controller.ts
│   │   └── dto/
│   │       └── update-user.dto.ts
│   ├── categories/
│   │   ├── categories.module.ts
│   │   ├── categories.service.ts
│   │   ├── categories.controller.ts
│   │   ├── schemas/
│   │   │   └── category.schema.ts
│   │   └── dto/
│   │       └── create-category.dto.ts
│   ├── products/
│   │   ├── products.module.ts
│   │   ├── products.service.ts
│   │   ├── products.controller.ts
│   │   ├── schemas/
│   │   │   └── product.schema.ts
│   │   └── dto/
│   │       ├── create-product.dto.ts
│   │       └── query-product.dto.ts
│   ├── reviews/
│   │   ├── reviews.module.ts
│   │   ├── reviews.service.ts
│   │   ├── reviews.controller.ts
│   │   ├── schemas/
│   │   │   └── review.schema.ts
│   │   └── dto/
│   │       └── create-review.dto.ts
│   ├── orders/
│   │   ├── orders.module.ts
│   │   ├── orders.service.ts
│   │   ├── orders.controller.ts
│   │   └── dto/
│   │       └── create-order.dto.ts
│   ├── payments/
│   │   ├── payments.module.ts
│   │   ├── payments.service.ts
│   │   └── payments.controller.ts
│   └── uploads/
│       ├── uploads.module.ts
│       ├── uploads.service.ts
│       └── uploads.controller.ts
├── prisma/
│   ├── schema.prisma
│   └── migrations/
├── .env
├── .env.example
├── nest-cli.json
├── package.json
└── tsconfig.json
```

---

## ⚙️ Setup

```bash
# New NestJS project
nest new myshop-api
cd myshop-api

# Packages install
npm install @nestjs/config @nestjs/passport @nestjs/jwt @nestjs/mongoose
npm install passport passport-jwt
npm install @prisma/client prisma
npm install mongoose
npm install bcryptjs class-validator class-transformer
npm install @nestjs/swagger swagger-ui-express
npm install helmet express-rate-limit
npm install cloudinary multer
npm install @nestjs/platform-express multer

npm install -D @types/passport-jwt @types/bcryptjs @types/multer prisma
```

---

## 🔧 Core Files

📄 File: `src/main.ts` · 🎯 উদ্দেশ্য: Application bootstrap

```typescript
import { NestFactory } from '@nestjs/core';
import { ValidationPipe, Logger } from '@nestjs/common';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { ConfigService } from '@nestjs/config';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import { AppModule } from './app.module';
import { HttpExceptionFilter } from './common/filters/http-exception.filter';
import { TransformInterceptor } from './common/interceptors/transform.interceptor';

async function bootstrap() {
  const app = await NestFactory.create(AppModule, {
    logger: ['log', 'error', 'warn', 'debug'],
  });

  const configService = app.get(ConfigService);
  const port = configService.get<number>('port') || 3000;
  const nodeEnv = configService.get<string>('nodeEnv');

  // Security
  app.use(helmet());
  app.enableCors({
    origin: configService.get<string>('frontendUrl'),
    credentials: true,
  });

  // Rate limiting
  app.use(
    rateLimit({
      windowMs: 15 * 60 * 1000,
      max: 100,
      standardHeaders: true,
      legacyHeaders: false,
    })
  );

  // API prefix
  app.setGlobalPrefix('api/v1');

  // Pipes
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
      transformOptions: { enableImplicitConversion: true },
    })
  );

  // Filters
  app.useGlobalFilters(new HttpExceptionFilter());

  // Interceptors
  app.useGlobalInterceptors(new TransformInterceptor());

  // Swagger
  if (nodeEnv !== 'production') {
    const config = new DocumentBuilder()
      .setTitle('MyShop E-commerce API')
      .setDescription('Complete e-commerce backend API')
      .setVersion('1.0')
      .addBearerAuth(
        { type: 'http', scheme: 'bearer', bearerFormat: 'JWT' },
        'JWT-auth'
      )
      .addTag('Auth', 'Authentication endpoints')
      .addTag('Users', 'User management')
      .addTag('Products', 'Product catalog')
      .addTag('Categories', 'Product categories')
      .addTag('Reviews', 'Product reviews')
      .addTag('Orders', 'Order management')
      .addTag('Payments', 'Payment processing')
      .addTag('Uploads', 'File uploads')
      .build();

    const document = SwaggerModule.createDocument(app, config);
    SwaggerModule.setup('api/docs', app, document, {
      swaggerOptions: { persistAuthorization: true },
    });

    Logger.log(`📚 Swagger: http://localhost:${port}/api/docs`, 'Bootstrap');
  }

  await app.listen(port);
  Logger.log(`🚀 Server running: http://localhost:${port}/api/v1`, 'Bootstrap');
}

bootstrap();
```

📄 File: `src/app.module.ts` · 🎯 উদ্দেশ্য: Root module

```typescript
import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { MongooseModule } from '@nestjs/mongoose';
import configuration from './config/configuration';
import { PrismaModule } from './prisma/prisma.module';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { ProductsModule } from './products/products.module';
import { CategoriesModule } from './categories/categories.module';
import { ReviewsModule } from './reviews/reviews.module';
import { OrdersModule } from './orders/orders.module';
import { PaymentsModule } from './payments/payments.module';
import { UploadsModule } from './uploads/uploads.module';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      load: [configuration],
      envFilePath: ['.env.local', '.env'],
    }),
    MongooseModule.forRootAsync({
      imports: [ConfigModule],
      useFactory: (config: ConfigService) => ({
        uri: config.get<string>('mongodbUri'),
        connectionFactory: (connection) => {
          connection.on('connected', () => console.log('✅ MongoDB connected'));
          connection.on('error', (err) => console.error('❌ MongoDB error:', err));
          return connection;
        },
      }),
      inject: [ConfigService],
    }),
    PrismaModule,
    AuthModule,
    UsersModule,
    ProductsModule,
    CategoriesModule,
    ReviewsModule,
    OrdersModule,
    PaymentsModule,
    UploadsModule,
  ],
})
export class AppModule {}
```

📄 File: `src/config/configuration.ts` · 🎯 উদ্দেশ্য: Typed configuration

```typescript
export default () => ({
  nodeEnv: process.env.NODE_ENV || 'development',
  port: parseInt(process.env.PORT || '3000', 10),
  frontendUrl: process.env.FRONTEND_URL || 'http://localhost:3001',
  databaseUrl: process.env.DATABASE_URL,
  mongodbUri: process.env.MONGODB_URI,
  jwt: {
    accessSecret: process.env.JWT_ACCESS_SECRET,
    refreshSecret: process.env.JWT_REFRESH_SECRET,
    accessExpiresIn: process.env.JWT_ACCESS_EXPIRES_IN || '15m',
    refreshExpiresIn: process.env.JWT_REFRESH_EXPIRES_IN || '7d',
  },
  cloudinary: {
    cloudName: process.env.CLOUDINARY_CLOUD_NAME,
    apiKey: process.env.CLOUDINARY_API_KEY,
    apiSecret: process.env.CLOUDINARY_API_SECRET,
  },
  email: {
    host: process.env.EMAIL_HOST,
    port: parseInt(process.env.EMAIL_PORT || '587', 10),
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});
```

---

## 🏪 Products Module (Complete)

📄 File: `src/products/schemas/product.schema.ts`

```typescript
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document, Types } from 'mongoose';

export type ProductDocument = Product & Document;

@Schema({ timestamps: true, toJSON: { virtuals: true }, toObject: { virtuals: true } })
export class Product {
  @Prop({ required: true, trim: true, maxlength: 200 })
  name: string;

  @Prop({ required: true, unique: true, trim: true, lowercase: true })
  sku: string;

  @Prop({ required: true, unique: true, trim: true, lowercase: true })
  slug: string;

  @Prop({ trim: true, maxlength: 2000 })
  description: string;

  @Prop({ required: true, min: 0 })
  price: number;

  @Prop({ min: 0 })
  compareAtPrice: number;

  @Prop({ required: true, min: 0, default: 0 })
  stock: number;

  @Prop({ trim: true })
  brand: string;

  @Prop({
    type: {
      publicId: { type: String, required: true },
      url: { type: String, required: true },
      isMain: { type: Boolean, default: false },
    },
    default: [],
  })
  images: { publicId: string; url: string; isMain: boolean }[];

  @Prop({
    type: Types.ObjectId,
    ref: 'Category',
    required: true,
  })
  categoryId: Types.ObjectId;

  @Prop({ default: true })
  isActive: boolean;

  @Prop({ default: false })
  isFeatured: boolean;

  @Prop({ type: [String], default: [] })
  tags: string[];

  @Prop({ default: 0, min: 0, max: 5 })
  avgRating: number;

  @Prop({ default: 0 })
  reviewCount: number;
}

export const ProductSchema = SchemaFactory.createForClass(Product);

ProductSchema.index({ slug: 1 });
ProductSchema.index({ sku: 1 });
ProductSchema.index({ categoryId: 1 });
ProductSchema.index({ price: 1 });
ProductSchema.index({ isActive: 1, isFeatured: -1 });
ProductSchema.index({ name: 'text', description: 'text', brand: 'text', tags: 'text' });

ProductSchema.virtual('discountPercentage').get(function () {
  if (this.compareAtPrice && this.compareAtPrice > this.price) {
    return Math.round(((this.compareAtPrice - this.price) / this.compareAtPrice) * 100);
  }
  return 0;
});

ProductSchema.virtual('inStock').get(function () {
  return this.stock > 0;
});
```

📄 File: `src/products/dto/create-product.dto.ts`

```typescript
import {
  IsString, IsNumber, IsOptional, IsBoolean,
  IsArray, IsMongoId, Min, MaxLength, MinLength,
} from 'class-validator';
import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';
import { Transform } from 'class-transformer';

export class CreateProductDto {
  @ApiProperty({ example: 'iPhone 15 Pro' })
  @IsString()
  @MinLength(2)
  @MaxLength(200)
  name: string;

  @ApiProperty({ example: 'APPL-IP15P-256-BLK' })
  @IsString()
  @Transform(({ value }) => value.toUpperCase())
  sku: string;

  @ApiProperty({ example: 'iphone-15-pro' })
  @IsString()
  @Transform(({ value }) => value.toLowerCase().replace(/\s+/g, '-'))
  slug: string;

  @ApiPropertyOptional({ example: 'Latest iPhone with titanium design' })
  @IsOptional()
  @IsString()
  @MaxLength(2000)
  description?: string;

  @ApiProperty({ example: 999.99 })
  @IsNumber()
  @Min(0)
  price: number;

  @ApiPropertyOptional({ example: 1199.99 })
  @IsOptional()
  @IsNumber()
  @Min(0)
  compareAtPrice?: number;

  @ApiProperty({ example: 50 })
  @IsNumber()
  @Min(0)
  stock: number;

  @ApiPropertyOptional({ example: 'Apple' })
  @IsOptional()
  @IsString()
  brand?: string;

  @ApiProperty({ example: '507f1f77bcf86cd799439011' })
  @IsMongoId()
  categoryId: string;

  @ApiPropertyOptional({ example: true })
  @IsOptional()
  @IsBoolean()
  isFeatured?: boolean;

  @ApiPropertyOptional({ example: ['smartphone', 'apple', 'ios'] })
  @IsOptional()
  @IsArray()
  @IsString({ each: true })
  tags?: string[];
}
```

📄 File: `src/products/products.service.ts`

```typescript
import { Injectable, NotFoundException, ConflictException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { Product, ProductDocument } from './schemas/product.schema';
import { CreateProductDto } from './dto/create-product.dto';

@Injectable()
export class ProductsService {
  constructor(
    @InjectModel(Product.name) private productModel: Model<ProductDocument>
  ) {}

  async create(createProductDto: CreateProductDto): Promise<Product> {
    const existing = await this.productModel.findOne({
      $or: [{ sku: createProductDto.sku }, { slug: createProductDto.slug }],
    });

    if (existing) {
      throw new ConflictException(
        existing.sku === createProductDto.sku
          ? 'Product with this SKU already exists'
          : 'Product with this slug already exists'
      );
    }

    const product = new this.productModel(createProductDto);
    return product.save();
  }

  async findAll(query: {
    page?: number;
    limit?: number;
    category?: string;
    brand?: string;
    minPrice?: number;
    maxPrice?: number;
    search?: string;
    featured?: boolean;
    sort?: string;
  }) {
    const {
      page = 1, limit = 10, category, brand,
      minPrice, maxPrice, search, featured, sort = '-createdAt',
    } = query;

    const filter: any = { isActive: true };
    if (category) filter.categoryId = category;
    if (brand) filter.brand = new RegExp(brand, 'i');
    if (minPrice || maxPrice) {
      filter.price = {};
      if (minPrice) filter.price.$gte = minPrice;
      if (maxPrice) filter.price.$lte = maxPrice;
    }
    if (search) filter.$text = { $search: search };
    if (featured) filter.isFeatured = true;

    const skip = (page - 1) * Math.min(limit, 100);
    const safeLimit = Math.min(limit, 100);

    const [data, total] = await Promise.all([
      this.productModel
        .find(filter)
        .populate('categoryId', 'name slug')
        .sort(sort)
        .skip(skip)
        .limit(safeLimit)
        .lean()
        .exec(),
      this.productModel.countDocuments(filter),
    ]);

    return {
      data,
      pagination: {
        total,
        page,
        limit: safeLimit,
        totalPages: Math.ceil(total / safeLimit),
        hasNextPage: page * safeLimit < total,
        hasPreviousPage: page > 1,
      },
    };
  }

  async findBySlug(slug: string): Promise<Product> {
    const product = await this.productModel
      .findOne({ slug, isActive: true })
      .populate('categoryId', 'name slug')
      .lean()
      .exec();

    if (!product) {
      throw new NotFoundException(`Product '${slug}' not found`);
    }

    return product;
  }

  async findById(id: string): Promise<ProductDocument> {
    const product = await this.productModel.findById(id).exec();
    if (!product) throw new NotFoundException('Product not found');
    return product;
  }

  async update(id: string, updateDto: Partial<CreateProductDto>): Promise<Product> {
    const product = await this.productModel
      .findByIdAndUpdate(id, { $set: updateDto }, { new: true, runValidators: true })
      .exec();

    if (!product) throw new NotFoundException('Product not found');
    return product;
  }

  async remove(id: string): Promise<void> {
    const product = await this.productModel
      .findByIdAndUpdate(id, { isActive: false })
      .exec();

    if (!product) throw new NotFoundException('Product not found');
  }

  async updateImages(id: string, images: { publicId: string; url: string; isMain: boolean }[]): Promise<Product> {
    const product = await this.productModel
      .findByIdAndUpdate(id, { $set: { images } }, { new: true })
      .exec();

    if (!product) throw new NotFoundException('Product not found');
    return product;
  }

  async updateRating(productId: string, avgRating: number, reviewCount: number): Promise<void> {
    await this.productModel.findByIdAndUpdate(productId, {
      $set: { avgRating: Math.round(avgRating * 10) / 10, reviewCount },
    });
  }
}
```

📄 File: `src/products/products.controller.ts`

```typescript
import {
  Controller, Get, Post, Patch, Delete,
  Body, Param, Query, UseGuards,
  HttpCode, HttpStatus,
} from '@nestjs/common';
import {
  ApiTags, ApiOperation, ApiResponse,
  ApiBearerAuth, ApiQuery,
} from '@nestjs/swagger';
import { ProductsService } from './products.service';
import { CreateProductDto } from './dto/create-product.dto';
import { JwtAuthGuard } from '../common/guards/jwt-auth.guard';
import { RolesGuard } from '../common/guards/roles.guard';
import { Roles } from '../common/decorators/roles.decorator';
import { Public } from '../common/decorators/public.decorator';
import { ParseObjectIdPipe } from '../common/pipes/parse-object-id.pipe';

@ApiTags('Products')
@ApiBearerAuth('JWT-auth')
@UseGuards(JwtAuthGuard, RolesGuard)
@Controller('products')
export class ProductsController {
  constructor(private readonly productsService: ProductsService) {}

  @Post()
  @Roles('admin', 'seller')
  @HttpCode(HttpStatus.CREATED)
  @ApiOperation({ summary: 'Create product (admin/seller)' })
  @ApiResponse({ status: 201, description: 'Product created' })
  create(@Body() createProductDto: CreateProductDto) {
    return this.productsService.create(createProductDto);
  }

  @Get()
  @Public()
  @ApiOperation({ summary: 'Get all products with filtering' })
  @ApiQuery({ name: 'page', required: false, type: Number })
  @ApiQuery({ name: 'limit', required: false, type: Number })
  @ApiQuery({ name: 'category', required: false, type: String })
  @ApiQuery({ name: 'brand', required: false, type: String })
  @ApiQuery({ name: 'minPrice', required: false, type: Number })
  @ApiQuery({ name: 'maxPrice', required: false, type: Number })
  @ApiQuery({ name: 'search', required: false, type: String })
  @ApiQuery({ name: 'featured', required: false, type: Boolean })
  findAll(
    @Query('page') page?: number,
    @Query('limit') limit?: number,
    @Query('category') category?: string,
    @Query('brand') brand?: string,
    @Query('minPrice') minPrice?: number,
    @Query('maxPrice') maxPrice?: number,
    @Query('search') search?: string,
    @Query('featured') featured?: boolean,
  ) {
    return this.productsService.findAll({
      page, limit, category, brand, minPrice, maxPrice, search, featured,
    });
  }

  @Get(':slug')
  @Public()
  @ApiOperation({ summary: 'Get product by slug' })
  findBySlug(@Param('slug') slug: string) {
    return this.productsService.findBySlug(slug);
  }

  @Patch(':id')
  @Roles('admin', 'seller')
  @ApiOperation({ summary: 'Update product' })
  update(
    @Param('id', ParseObjectIdPipe) id: string,
    @Body() updateDto: Partial<CreateProductDto>,
  ) {
    return this.productsService.update(id, updateDto);
  }

  @Delete(':id')
  @Roles('admin')
  @HttpCode(HttpStatus.NO_CONTENT)
  @ApiOperation({ summary: 'Delete product (admin only)' })
  remove(@Param('id', ParseObjectIdPipe) id: string) {
    return this.productsService.remove(id);
  }
}
```

---

## 🛒 Orders Module (Complete)

📄 File: `src/orders/dto/create-order.dto.ts`

```typescript
import { IsArray, IsString, IsNumber, IsOptional, Min, ValidateNested, IsMongoId } from 'class-validator';
import { Type } from 'class-transformer';
import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';

export class OrderItemDto {
  @ApiProperty({ example: '507f1f77bcf86cd799439011' })
  @IsMongoId()
  productId: string;

  @ApiProperty({ example: 2 })
  @IsNumber()
  @Min(1)
  quantity: number;
}

export class ShippingAddressDto {
  @ApiProperty({ example: '123 Main St' })
  @IsString()
  street: string;

  @ApiProperty({ example: 'Dhaka' })
  @IsString()
  city: string;

  @ApiProperty({ example: '1000' })
  @IsString()
  postalCode: string;

  @ApiProperty({ example: 'Bangladesh' })
  @IsString()
  country: string;
}

export class CreateOrderDto {
  @ApiProperty({ type: [OrderItemDto] })
  @IsArray()
  @ValidateNested({ each: true })
  @Type(() => OrderItemDto)
  items: OrderItemDto[];

  @ApiProperty({ type: ShippingAddressDto })
  @ValidateNested()
  @Type(() => ShippingAddressDto)
  shippingAddress: ShippingAddressDto;

  @ApiPropertyOptional({ example: 'SAVE10' })
  @IsOptional()
  @IsString()
  couponCode?: string;

  @ApiPropertyOptional({ example: 'Please handle with care' })
  @IsOptional()
  @IsString()
  notes?: string;
}
```

📄 File: `src/orders/orders.service.ts`

```typescript
import { Injectable, NotFoundException, BadRequestException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { PrismaService } from '../prisma/prisma.service';
import { CreateOrderDto } from './dto/create-order.dto';

@Injectable()
export class OrdersService {
  constructor(
    private prisma: PrismaService,
    @InjectModel('Product') private productModel: Model<any>,
  ) {}

  async create(userId: number, createOrderDto: CreateOrderDto) {
    const { items, shippingAddress, notes } = createOrderDto;

    // 1. MongoDB থেকে product info ও stock check করো
    const productIds = items.map((item) => item.productId);
    const products = await this.productModel
      .find({ _id: { $in: productIds }, isActive: true })
      .lean()
      .exec();

    if (products.length !== items.length) {
      throw new NotFoundException('One or more products not found');
    }

    // Stock check
    for (const item of items) {
      const product = products.find((p) => p._id.toString() === item.productId);
      if (!product) throw new NotFoundException(`Product ${item.productId} not found`);
      if (product.stock < item.quantity) {
        throw new BadRequestException(
          `Insufficient stock for "${product.name}". Available: ${product.stock}`
        );
      }
    }

    // 2. Order total calculate করো
    const orderItems = items.map((item) => {
      const product = products.find((p) => p._id.toString() === item.productId);
      return {
        productId: item.productId,
        productName: product.name,
        sku: product.sku,
        price: product.price,
        quantity: item.quantity,
        subtotal: product.price * item.quantity,
      };
    });

    const subtotal = orderItems.reduce((sum, item) => sum + item.subtotal, 0);
    const shippingCost = subtotal >= 1000 ? 0 : 60;  // Free shipping over 1000 BDT
    const total = subtotal + shippingCost;

    // 3. Prisma transaction-এ order create করো
    const order = await this.prisma.$transaction(async (tx) => {
      const newOrder = await tx.order.create({
        data: {
          userId,
          total,
          shippingCost,
          notes,
          shippingAddress: shippingAddress as any,
          status: 'pending',
          paymentStatus: 'pending',
          items: {
            create: orderItems.map((item) => ({
              productId: item.productId,
              productName: item.productName,
              sku: item.sku,
              price: item.price,
              quantity: item.quantity,
              subtotal: item.subtotal,
            })),
          },
        },
        include: {
          items: true,
          user: { select: { id: true, firstName: true, email: true } },
        },
      });

      return newOrder;
    });

    // 4. MongoDB-তে stock decrement করো (outside transaction - eventual consistency)
    for (const item of items) {
      await this.productModel.findByIdAndUpdate(item.productId, {
        $inc: { stock: -item.quantity },
      });
    }

    return order;
  }

  async findAll(userId: number, isAdmin: boolean) {
    const where = isAdmin ? {} : { userId };

    return this.prisma.order.findMany({
      where,
      include: {
        items: true,
        user: { select: { id: true, firstName: true, lastName: true, email: true } },
        payment: true,
      },
      orderBy: { createdAt: 'desc' },
    });
  }

  async findOne(id: number, userId: number, isAdmin: boolean) {
    const order = await this.prisma.order.findFirst({
      where: {
        id,
        ...(isAdmin ? {} : { userId }),
      },
      include: {
        items: true,
        user: { select: { id: true, firstName: true, lastName: true, email: true } },
        payment: true,
      },
    });

    if (!order) throw new NotFoundException('Order not found');
    return order;
  }

  async updateStatus(id: number, status: string) {
    return this.prisma.order.update({
      where: { id },
      data: { status },
    });
  }
}
```

---

## 💳 Payments Module

📄 File: `src/payments/payments.service.ts`

```typescript
import { Injectable, NotFoundException, BadRequestException } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class PaymentsService {
  constructor(
    private prisma: PrismaService,
    private config: ConfigService,
  ) {}

  async initiatePayment(orderId: number, userId: number) {
    const order = await this.prisma.order.findFirst({
      where: { id: orderId, userId, paymentStatus: 'pending' },
      include: {
        user: { select: { firstName: true, lastName: true, email: true, phone: true } },
      },
    });

    if (!order) throw new NotFoundException('Order not found or already paid');

    // Payment gateway integration point
    // SSLCommerz / bKash / Stripe etc.
    const transactionId = `TXN-${Date.now()}-${orderId}`;

    const payment = await this.prisma.payment.create({
      data: {
        orderId,
        userId,
        amount: order.total,
        method: 'online',
        transactionId,
        status: 'initiated',
        gateway: 'sslcommerz',
      },
    });

    // বাস্তব production-এ SSLCommerz API call এখানে
    return {
      paymentId: payment.id,
      transactionId,
      amount: order.total,
      redirectUrl: `https://payment.example.com/pay/${transactionId}`,
    };
  }

  async confirmPayment(transactionId: string, gatewayResponse: any) {
    const payment = await this.prisma.payment.findFirst({
      where: { transactionId },
    });

    if (!payment) throw new NotFoundException('Payment not found');

    // Verify with gateway (production-এ gateway SDK call করো)
    const verified = true;  // Simplified

    if (!verified) throw new BadRequestException('Payment verification failed');

    return this.prisma.$transaction(async (tx) => {
      const updatedPayment = await tx.payment.update({
        where: { id: payment.id },
        data: {
          status: 'completed',
          gatewayResponse,
          paidAt: new Date(),
        },
      });

      await tx.order.update({
        where: { id: payment.orderId },
        data: { paymentStatus: 'paid', status: 'confirmed' },
      });

      return updatedPayment;
    });
  }
}
```

---

## 📊 Prisma Schema (Final)

📄 File: `prisma/schema.prisma`

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

enum Role {
  customer
  seller
  admin
}

enum OrderStatus {
  pending
  confirmed
  processing
  shipped
  delivered
  cancelled
  refunded
}

enum PaymentStatus {
  pending
  initiated
  completed
  failed
  refunded
}

model User {
  id            Int       @id @default(autoincrement())
  firstName     String    @db.VarChar(50)
  lastName      String    @db.VarChar(50)
  email         String    @unique @db.VarChar(255)
  passwordHash  String
  phone         String?   @db.VarChar(20)
  role          Role      @default(customer)
  isEmailVerified Boolean @default(false)
  emailVerifyToken String?
  passwordResetToken String?
  passwordResetExpiry DateTime?
  lastLoginAt   DateTime?
  isActive      Boolean   @default(true)
  orders        Order[]
  payments      Payment[]
  refreshTokens RefreshToken[]
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt

  @@index([email])
}

model RefreshToken {
  id        Int      @id @default(autoincrement())
  token     String   @unique
  userId    Int
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  expiresAt DateTime
  createdAt DateTime @default(now())

  @@index([token])
  @@index([userId])
}

model Order {
  id              Int           @id @default(autoincrement())
  userId          Int
  user            User          @relation(fields: [userId], references: [id])
  total           Decimal       @db.Decimal(10, 2)
  shippingCost    Decimal       @default(0) @db.Decimal(10, 2)
  status          OrderStatus   @default(pending)
  paymentStatus   PaymentStatus @default(pending)
  shippingAddress Json
  notes           String?
  items           OrderItem[]
  payment         Payment?
  createdAt       DateTime      @default(now())
  updatedAt       DateTime      @updatedAt

  @@index([userId])
  @@index([status])
}

model OrderItem {
  id          Int     @id @default(autoincrement())
  orderId     Int
  order       Order   @relation(fields: [orderId], references: [id], onDelete: Cascade)
  productId   String  @db.VarChar(24)
  productName String
  sku         String
  price       Decimal @db.Decimal(10, 2)
  quantity    Int
  subtotal    Decimal @db.Decimal(10, 2)

  @@index([orderId])
}

model Payment {
  id              Int           @id @default(autoincrement())
  orderId         Int           @unique
  order           Order         @relation(fields: [orderId], references: [id])
  userId          Int
  user            User          @relation(fields: [userId], references: [id])
  amount          Decimal       @db.Decimal(10, 2)
  method          String
  gateway         String
  transactionId   String        @unique
  status          PaymentStatus @default(pending)
  gatewayResponse Json?
  paidAt          DateTime?
  createdAt       DateTime      @default(now())
  updatedAt       DateTime      @updatedAt

  @@index([transactionId])
  @@index([userId])
}
```

---

## 🚀 Final Run

```bash
# Development
npm run start:dev

# Build
npm run build

# Production
NODE_ENV=production npm run start:prod

# Prisma migrate
npx prisma migrate dev --name init
npx prisma generate

# API Docs
open http://localhost:3000/api/docs

# Health Check
curl http://localhost:3000/api/v1/health
```

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 18 — তুমি শিখলে                         ║
╠══════════════════════════════════════════════════════╣
║  • Full NestJS project structure                    ║
║  • Products/Categories/Reviews (MongoDB)            ║
║  • Orders/Payments (PostgreSQL/Prisma)              ║
║  • JWT Auth + Role Guards                           ║
║  • Swagger full documentation                       ║
║  • Production-ready bootstrap                       ║
║  • Complete Prisma schema (e-commerce)              ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 17](./chapter-17-deployment.md) | [➡ Appendix A](./appendix-a-sql.md)

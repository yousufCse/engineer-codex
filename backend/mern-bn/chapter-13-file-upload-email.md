
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 13 — File Upload & Email
# "Cloudinary + Multer + Nodemailer"
# ⏱ ~90 মিনিট · Progress: [████████████░] 70%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Multer দিয়ে file upload
- ✅ Cloudinary integration — image store ও transform
- ✅ Image validation (type, size)
- ✅ Multiple file upload
- ✅ Nodemailer setup
- ✅ HTML email templates
- ✅ Email verification + password reset emails

---

## ⚙️ Installation

```bash
npm install multer cloudinary multer-storage-cloudinary
npm install nodemailer
npm install @types/multer @types/nodemailer --save-dev
```

---

## ☁️ Cloudinary Setup

📄 File: `src/config/cloudinary.config.js` · 🎯 উদ্দেশ্য: Cloudinary configuration

```javascript
const cloudinary = require('cloudinary').v2;
const { CloudinaryStorage } = require('multer-storage-cloudinary');
const multer = require('multer');

// Cloudinary configure করো
cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
  secure: true,
});

// ============================================
// Product Image Storage
// ============================================
const productImageStorage = new CloudinaryStorage({
  cloudinary,
  params: async (req, file) => ({
    folder: 'ecommerce/products',
    allowed_formats: ['jpg', 'jpeg', 'png', 'webp'],
    transformation: [
      { width: 1200, height: 1200, crop: 'limit', quality: 'auto:good' },
      { fetch_format: 'auto' },
    ],
    public_id: `product_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
  }),
});

// ============================================
// Avatar Storage
// ============================================
const avatarStorage = new CloudinaryStorage({
  cloudinary,
  params: async (req, file) => ({
    folder: 'ecommerce/avatars',
    allowed_formats: ['jpg', 'jpeg', 'png', 'webp'],
    transformation: [
      { width: 400, height: 400, crop: 'fill', gravity: 'face' },
      { quality: 'auto' },
    ],
    public_id: `avatar_${req.user.id}_${Date.now()}`,
  }),
});

// ============================================
// File Filter — type ও size validation
// ============================================
const imageFileFilter = (req, file, cb) => {
  const allowedMimeTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];

  if (!allowedMimeTypes.includes(file.mimetype)) {
    return cb(new Error('Only JPEG, PNG, and WebP images are allowed'), false);
  }

  cb(null, true);
};

// ============================================
// Multer Upload Instances
// ============================================
const uploadProductImage = multer({
  storage: productImageStorage,
  fileFilter: imageFileFilter,
  limits: {
    fileSize: 5 * 1024 * 1024,  // 5MB
    files: 10,                    // maximum 10 files
  },
});

const uploadAvatar = multer({
  storage: avatarStorage,
  fileFilter: imageFileFilter,
  limits: {
    fileSize: 2 * 1024 * 1024,  // 2MB
    files: 1,
  },
});

// ============================================
// Direct Cloudinary Upload (Buffer-based)
// ============================================
const uploadToCloudinary = (buffer, options = {}) => {
  return new Promise((resolve, reject) => {
    const uploadStream = cloudinary.uploader.upload_stream(
      {
        folder: options.folder || 'ecommerce',
        transformation: options.transformation || [],
        ...options,
      },
      (error, result) => {
        if (error) reject(error);
        else resolve(result);
      }
    );

    uploadStream.end(buffer);
  });
};

// Delete image
const deleteFromCloudinary = async (publicId) => {
  return cloudinary.uploader.destroy(publicId);
};

module.exports = {
  cloudinary,
  uploadProductImage,
  uploadAvatar,
  uploadToCloudinary,
  deleteFromCloudinary,
};
```

---

## 📤 Upload Controller

📄 File: `src/controllers/upload.controller.js` · 🎯 উদ্দেশ্য: File upload endpoints

```javascript
const { uploadProductImage, deleteFromCloudinary } = require('../config/cloudinary.config');
const { AppError } = require('../middleware/error.middleware');
const ApiResponse = require('../utils/ApiResponse');
const prisma = require('../config/prisma');

// ============================================
// Single Product Image Upload
// ============================================
const uploadSingleImage = [
  uploadProductImage.single('image'),  // Multer middleware
  async (req, res, next) => {
    try {
      if (!req.file) {
        throw new AppError('Image file is required', 400);
      }

      // Cloudinary result from multer-storage-cloudinary
      const imageData = {
        url: req.file.path,           // Cloudinary URL
        publicId: req.file.filename,  // Cloudinary public_id
        width: req.file.width,
        height: req.file.height,
        format: req.file.format,
        size: req.file.size,
      };

      ApiResponse.created(res, imageData, 'Image uploaded successfully');
    } catch (error) {
      next(error);
    }
  },
];

// ============================================
// Multiple Product Images Upload
// ============================================
const uploadMultipleImages = [
  uploadProductImage.array('images', 10),  // max 10 images
  async (req, res, next) => {
    try {
      if (!req.files || req.files.length === 0) {
        throw new AppError('At least one image is required', 400);
      }

      const images = req.files.map((file, index) => ({
        url: file.path,
        publicId: file.filename,
        isPrimary: index === 0,
        sortOrder: index,
        size: file.size,
      }));

      ApiResponse.created(res, images, `${images.length} images uploaded`);
    } catch (error) {
      next(error);
    }
  },
];

// ============================================
// Product Images Upload + Save to DB
// ============================================
const uploadProductImages = [
  uploadProductImage.array('images', 10),
  async (req, res, next) => {
    try {
      const { productId } = req.params;

      if (!req.files || req.files.length === 0) {
        throw new AppError('At least one image required', 400);
      }

      // Product exists check
      const product = await prisma.product.findUnique({
        where: { id: parseInt(productId, 10) },
        include: { images: true },
      });

      if (!product) {
        // Uploaded files delete করো
        for (const file of req.files) {
          await deleteFromCloudinary(file.filename);
        }
        throw new AppError('Product not found', 404);
      }

      // Primary image — যদি product-এ কোনো image না থাকে
      const hasPrimary = product.images.some((img) => img.isPrimary);

      // DB-তে save করো
      const savedImages = await prisma.$transaction(
        req.files.map((file, index) =>
          prisma.productImage.create({
            data: {
              productId: parseInt(productId, 10),
              url: file.path,
              altText: product.name,
              isPrimary: !hasPrimary && index === 0,
              sortOrder: product.images.length + index,
            },
          })
        )
      );

      ApiResponse.created(res, savedImages, `${savedImages.length} images saved`);
    } catch (error) {
      // Cleanup on error
      if (req.files) {
        for (const file of req.files) {
          await deleteFromCloudinary(file.filename).catch(console.error);
        }
      }
      next(error);
    }
  },
];

// ============================================
// Delete Image
// ============================================
const deleteImage = async (req, res, next) => {
  try {
    const { imageId } = req.params;

    const image = await prisma.productImage.findUnique({
      where: { id: parseInt(imageId, 10) },
      include: { product: { select: { id: true } } },
    });

    if (!image) {
      throw new AppError('Image not found', 404);
    }

    // Cloudinary থেকে delete করো
    const publicId = image.url.split('/').slice(-2).join('/').split('.')[0];
    await deleteFromCloudinary(`ecommerce/products/${publicId}`).catch(console.error);

    // DB থেকে delete করো
    await prisma.productImage.delete({ where: { id: image.id } });

    ApiResponse.noContent(res);
  } catch (error) {
    next(error);
  }
};

// ============================================
// Error handling for multer errors
// ============================================
const handleMulterError = (err, req, res, next) => {
  if (err.code === 'LIMIT_FILE_SIZE') {
    return res.status(400).json({
      success: false,
      message: 'File too large. Maximum size is 5MB',
    });
  }
  if (err.code === 'LIMIT_FILE_COUNT') {
    return res.status(400).json({
      success: false,
      message: 'Too many files. Maximum 10 images allowed',
    });
  }
  if (err.message.includes('Only JPEG, PNG')) {
    return res.status(400).json({
      success: false,
      message: err.message,
    });
  }
  next(err);
};

module.exports = {
  uploadSingleImage,
  uploadMultipleImages,
  uploadProductImages,
  deleteImage,
  handleMulterError,
};
```

---

## 📧 Email Service (Nodemailer)

📄 File: `src/services/email.service.js` · 🎯 উদ্দেশ্য: Email sending service

```javascript
const nodemailer = require('nodemailer');

// ============================================
// Transporter setup
// ============================================
const createTransporter = () => {
  if (process.env.NODE_ENV === 'development') {
    // Development: Ethereal (fake SMTP, see emails in browser)
    return nodemailer.createTransport({
      host: 'smtp.ethereal.email',
      port: 587,
      secure: false,
      auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS,
      },
    });
  }

  // Production: Gmail
  return nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS,  // Gmail App Password (16 chars)
    },
  });
};

const transporter = createTransporter();

// Verify connection
transporter.verify((error) => {
  if (error) {
    console.error('❌ Email service error:', error);
  } else {
    console.log('✅ Email service ready');
  }
});

// ============================================
// Base Email Template
// ============================================
const baseTemplate = (content, title) => `
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} — MyShop</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
    .container { max-width: 600px; margin: 40px auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    .header { background: #1a1a2e; color: white; padding: 30px; text-align: center; }
    .header h1 { margin: 0; font-size: 24px; }
    .body { padding: 30px; color: #333; line-height: 1.6; }
    .button { display: inline-block; padding: 14px 28px; background: #e94560; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 20px 0; }
    .footer { background: #f9f9f9; padding: 20px; text-align: center; color: #888; font-size: 12px; border-top: 1px solid #eee; }
    .divider { border: none; border-top: 1px solid #eee; margin: 20px 0; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🛒 MyShop</h1>
    </div>
    <div class="body">
      ${content}
    </div>
    <div class="footer">
      <p>এই email স্বয়ংক্রিয়ভাবে পাঠানো হয়েছে। Reply করবেন না।</p>
      <p>&copy; ${new Date().getFullYear()} MyShop. All rights reserved.</p>
    </div>
  </div>
</body>
</html>
`;

// ============================================
// Email Templates
// ============================================
const templates = {
  verifyEmail: (firstName, verifyUrl) => ({
    subject: 'MyShop — আপনার Email ঠিকানা Verify করুন',
    html: baseTemplate(`
      <h2>স্বাগতম, ${firstName}!</h2>
      <p>MyShop-এ আপনার account তৈরি হয়েছে। নিচের button-এ click করে আপনার email verify করুন।</p>
      <div style="text-align: center;">
        <a href="${verifyUrl}" class="button">Email Verify করুন</a>
      </div>
      <hr class="divider">
      <p style="font-size: 12px; color: #888;">এই link ২৪ ঘণ্টা পর expire হবে। Button কাজ না করলে এই URL copy করুন:</p>
      <p style="word-break: break-all; font-size: 12px; color: #555;">${verifyUrl}</p>
    `, 'Email Verification'),
  }),

  passwordReset: (firstName, resetUrl) => ({
    subject: 'MyShop — Password Reset Request',
    html: baseTemplate(`
      <h2>Password Reset</h2>
      <p>প্রিয় ${firstName},</p>
      <p>আপনি password reset-এর request করেছেন। নিচের button-এ click করুন।</p>
      <div style="text-align: center;">
        <a href="${resetUrl}" class="button">Password Reset করুন</a>
      </div>
      <hr class="divider">
      <p>⚠️ এই link ৩০ মিনিট পর expire হবে।</p>
      <p>যদি আপনি এই request না করে থাকেন, এই email ignore করুন।</p>
    `, 'Password Reset'),
  }),

  orderConfirmation: (order) => ({
    subject: `MyShop — Order Confirmed #${order.orderNumber}`,
    html: baseTemplate(`
      <h2>Order Confirmed! ✅</h2>
      <p>আপনার order সফলভাবে placed হয়েছে।</p>
      <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
        <tr style="background: #f9f9f9;">
          <td style="padding: 10px; font-weight: bold;">Order Number</td>
          <td style="padding: 10px;">${order.orderNumber}</td>
        </tr>
        <tr>
          <td style="padding: 10px; font-weight: bold;">Total</td>
          <td style="padding: 10px;">৳${order.totalAmount}</td>
        </tr>
        <tr style="background: #f9f9f9;">
          <td style="padding: 10px; font-weight: bold;">Status</td>
          <td style="padding: 10px;">Pending</td>
        </tr>
      </table>
      <h3>Items:</h3>
      <table style="width: 100%; border-collapse: collapse;">
        <thead>
          <tr style="background: #1a1a2e; color: white;">
            <th style="padding: 10px; text-align: left;">Product</th>
            <th style="padding: 10px; text-align: center;">Qty</th>
            <th style="padding: 10px; text-align: right;">Price</th>
          </tr>
        </thead>
        <tbody>
          ${order.items.map((item) => `
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 10px;">${item.product.name}</td>
              <td style="padding: 10px; text-align: center;">${item.quantity}</td>
              <td style="padding: 10px; text-align: right;">৳${item.totalPrice}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `, 'Order Confirmation'),
  }),

  welcomeEmail: (firstName) => ({
    subject: `স্বাগতম MyShop-এ! 🎉`,
    html: baseTemplate(`
      <h2>স্বাগতম, ${firstName}! 🎉</h2>
      <p>আপনার email সফলভাবে verify হয়েছে। এখন আপনি MyShop-এর সব সুবিধা উপভোগ করতে পারবেন।</p>
      <ul>
        <li>✅ হাজারো Products Browse করুন</li>
        <li>✅ নিরাপদে Purchase করুন</li>
        <li>✅ Order Track করুন</li>
      </ul>
      <div style="text-align: center;">
        <a href="${process.env.FRONTEND_URL}" class="button">Shopping শুরু করুন</a>
      </div>
    `, 'Welcome'),
  }),
};

// ============================================
// Send Email Function
// ============================================
const sendEmail = async ({ to, subject, html, text }) => {
  try {
    const info = await transporter.sendMail({
      from: `"MyShop" <${process.env.EMAIL_USER}>`,
      to,
      subject,
      html,
      text: text || html.replace(/<[^>]*>/g, ''),  // Plain text fallback
    });

    console.log(`✅ Email sent to ${to}: ${info.messageId}`);

    // Development-এ preview URL দেখাও
    if (process.env.NODE_ENV === 'development') {
      console.log('Preview URL:', nodemailer.getTestMessageUrl(info));
    }

    return info;
  } catch (error) {
    console.error('❌ Email send failed:', error);
    throw error;
  }
};

// ============================================
// Exported Email Functions
// ============================================
const emailService = {
  sendVerificationEmail: async (user) => {
    const verifyUrl = `${process.env.FRONTEND_URL}/verify-email/${user.emailVerifyToken}`;
    const { subject, html } = templates.verifyEmail(user.firstName, verifyUrl);
    return sendEmail({ to: user.email, subject, html });
  },

  sendPasswordResetEmail: async (user) => {
    const resetUrl = `${process.env.FRONTEND_URL}/reset-password/${user.passwordResetToken}`;
    const { subject, html } = templates.passwordReset(user.firstName, resetUrl);
    return sendEmail({ to: user.email, subject, html });
  },

  sendOrderConfirmationEmail: async (user, order) => {
    const { subject, html } = templates.orderConfirmation(order);
    return sendEmail({ to: user.email, subject, html });
  },

  sendWelcomeEmail: async (user) => {
    const { subject, html } = templates.welcomeEmail(user.firstName);
    return sendEmail({ to: user.email, subject, html });
  },
};

module.exports = emailService;
```

---

## 🔗 Auth Controller Update — Email Integration

📄 File: `src/controllers/auth.controller.js` (update) · 🎯 উদ্দেশ্য: Add email sending

```javascript
const emailService = require('../services/email.service');

// register function-এ যোগ করো:
const register = async (req, res, next) => {
  try {
    // ... existing code ...

    // Email পাঠাও (async — user-কে wait করাবে না)
    emailService.sendVerificationEmail(user).catch((err) => {
      console.error('Failed to send verification email:', err);
    });

    ApiResponse.created(res, safeUser, 'Registration successful. Check your email.');
  } catch (error) {
    next(error);
  }
};

// verifyEmail function-এ:
const verifyEmail = async (req, res, next) => {
  try {
    // ... existing code ...

    // Welcome email পাঠাও
    emailService.sendWelcomeEmail(user).catch(console.error);

    ApiResponse.success(res, null, 'Email verified successfully');
  } catch (error) {
    next(error);
  }
};
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| File type check না করা | Malicious file upload | fileFilter + mimetype check |
| File size limit না দেওয়া | Server disk full | `limits.fileSize` set করো |
| Cloudinary credentials hardcode | Security breach | সবসময় env var ব্যবহার করো |
| Email block করা UI thread | Server hang করে | async/await, non-blocking |
| Gmail direct password | Google blocks | App Password ব্যবহার করো |
| Upload fail-এ cleanup না করা | Orphan files on Cloudinary | try/catch-এ deleteFromCloudinary |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 13 — তুমি শিখলে                         ║
╠══════════════════════════════════════════════════════╣
║  • Multer: file upload middleware                   ║
║  • Cloudinary: image store + transformation        ║
║  • multer-storage-cloudinary integration           ║
║  • File type + size validation                     ║
║  • Multiple file upload                             ║
║  • Nodemailer: transporter setup                   ║
║  • HTML email templates                            ║
║  • Verification + reset + order confirmation email ║
║  • Non-blocking email sending                      ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 12](./chapter-12-nestjs.md) | [➡ Chapter 14](./chapter-14-api-design.md)

# 🔗 کوتاه‌کننده لینک با FastAPI

یک پروژه ساده **کوتاه‌کننده لینک (URL Shortener)** که با استفاده از **FastAPI** و **SQLAlchemy** توسعه داده شده است.

این پروژه به کاربران اجازه می‌دهد لینک‌های بلند را به لینک‌های کوتاه تبدیل کنند و هنگام مراجعه به لینک کوتاه به صورت خودکار به لینک اصلی هدایت شوند.

---

# ✨ امکانات

- ایجاد لینک کوتاه
- هدایت (Redirect) به لینک اصلی
- اعتبارسنجی لینک‌ها با استفاده از Pydantic
- استفاده از پایگاه داده SQLite
- استفاده از ORM مربوط به SQLAlchemy
- توسعه یافته با FastAPI

---

# 📁 ساختار پروژه

```text
.
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── database/
│   │       ├── database.py
│   │       └── models.py
│   ├── routers/
│   │   └── link.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ پیش‌نیازها

- Python 3.11 یا بالاتر
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

---

# 📦 نصب پروژه

ابتدا مخزن پروژه را دریافت کنید:

```bash
git clone https://github.com/your-username/url-shortener.git

cd url-shortener
```

یک محیط مجازی ایجاد کنید:

```bash
python -m venv .venv
```

محیط مجازی را فعال کنید.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

سپس وابستگی‌های پروژه را نصب کنید:

```bash
pip install -r requirements.txt
```

---

# ▶️ اجرای پروژه

برای اجرای سرور FastAPI دستور زیر را اجرا کنید:

```bash
uvicorn app.main:app --reload
```

پس از اجرا، پروژه در آدرس زیر در دسترس خواهد بود:

```
http://127.0.0.1:8000
```

---

# 📖 مستندات API

رابط Swagger:

```
http://127.0.0.1:8000/docs
```

رابط ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# 🚀 مسیرهای API

## ایجاد لینک کوتاه

**POST**

```
/get-short
```

نمونه درخواست:

```json
{
    "link": "https://example.com"
}
```

نمونه پاسخ:

```json
{
    "your short url": "http://127.0.0.1:8000/1234567"
}
```

---

## هدایت به لینک اصلی

**GET**

```
/{short_code}
```

نمونه:

```
GET /1234567
```

سرور کاربر را به آدرس اصلی لینک هدایت می‌کند.

---

# 🛠 فناوری‌های استفاده‌شده

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# 📌 قابلیت‌های قابل اضافه شدن در آینده

- استفاده از Async SQLAlchemy
- استفاده از Dependency Injection (`Depends`)
- امکان انتخاب لینک کوتاه دلخواه توسط کاربر
- نمایش آمار و تعداد کلیک هر لینک
- تعیین تاریخ انقضا برای لینک‌ها
- سیستم ثبت‌نام و ورود کاربران
- پشتیبانی از PostgreSQL
- پشتیبانی از Docker
- نوشتن تست‌های واحد (Unit Tests)

---

# 📄 مجوز

این پروژه تحت مجوز **MIT License** منتشر شده است.

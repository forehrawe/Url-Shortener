# 🔗 URL Shortener / کوتاه‌کننده لینک

<div dir="ltr">

## 🌐 Choose Language / زبان را انتخاب کنید

### English
📖 [Read the English Documentation](./README.md)

A simple URL Shortener built with **FastAPI** and **SQLAlchemy**.

---

### فارسی
📖 [خواندن مستندات فارسی](./README-fa.md)

یک پروژه ساده **کوتاه‌کننده لینک (URL Shortener)** که با استفاده از **FastAPI** و **SQLAlchemy** توسعه داده شده است.

---

## 📋 Project Overview / نمای کلی پروژه

| Feature | توضیح |
|---------|--------|
| **Framework** | FastAPI |
| **Database** | SQLite |
| **ORM** | SQLAlchemy |
| **Validation** | Pydantic |
| **Server** | Uvicorn |

---

## 🚀 Quick Start / شروع سریع

### English
```bash
git clone https://github.com/forehrawe/Url-Shortener.git
cd Url-Shortener
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: `http://127.0.0.1:8000`

### فارسی
```bash
git clone https://github.com/forehrawe/Url-Shortener.git
cd Url-Shortener
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

مراجعه کنید به: `http://127.0.0.1:8000`

---

## 📚 Documentation Links / لینک‌های مستندات

### API Endpoints / نقاط انتهایی API

| Method | Endpoint | Description / توضیح |
|--------|----------|-----------------|
| POST | `/get-short` | Create short URL / ایجاد لینک کوتاه |
| GET | `/{short_code}` | Redirect to original URL / هدایت به لینک اصلی |

### Documentation / مستندات

- 📖 **[English README](./README.md)**
- 📖 **[Persian README / فارسی](./README-fa.md)**
- 🎯 **[Swagger UI](http://127.0.0.1:8000/docs)** - Interactive API Documentation
- 📋 **[ReDoc](http://127.0.0.1:8000/redoc)** - Alternative API Documentation

---

## 📄 License / مجوز

MIT License

---

**Made by** [@forehrawe](https://github.com/forehrawe)


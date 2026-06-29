# 🔗 FastAPI URL Shortener

A simple URL Shortener built with **FastAPI** and **SQLAlchemy**.

This project allows users to convert long URLs into short links and automatically redirects users to the original URL when the short link is visited.

---

# ✨ Features

- Generate short URLs
- Redirect to the original URL
- URL validation using Pydantic
- SQLite database
- SQLAlchemy ORM
- FastAPI framework

---

# 📁 Project Structure

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

# ⚙️ Requirements

- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/url-shortener.git

cd url-shortener
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# 🚀 Endpoints

## Create Short URL

**POST**

```
/get-short
```

Request Body

```json
{
    "link": "https://example.com"
}
```

Response

```json
{
    "your short url": "http://127.0.0.1:8000/1234567"
}
```

---

## Redirect

**GET**

```
/{short_code}
```

Example

```
GET /1234567
```

The server responds with an HTTP redirect to the original URL.

---

# 🛠 Technologies Used

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# 📌 Future Improvements

- Async SQLAlchemy
- Dependency Injection (`Depends`)
- Custom short codes
- Click analytics
- Expiration dates
- User authentication
- PostgreSQL support
- Docker support
- Unit tests

---

# 📄 License

This project is licensed under the MIT License.
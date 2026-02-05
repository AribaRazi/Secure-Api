# 🚀 Secure Flask Backend with Redis Caching & OTP Authentication

A backend API built using **Python Flask**, **MySQL**, and **Redis** that demonstrates:

- OTP based authentication system
- JWT protected APIs
- Redis caching for fast API responses
- Rate limiting using Redis
- Clean scalable project structure

This project is designed to showcase real-world backend concepts like authentication, caching, and performance optimization.

---

## 📸 Screenshots

### 🔐 OTP Generation & Verification
(Add screenshot here)

### 📦 JWT Token Response
(Add screenshot here)

### ⚡ Redis Cached API Response
(Add screenshot showing redis_cache source)

### 🚫 Rate Limiting Block Message
(Add screenshot here)

> 📌 Tip: Create a folder named `screenshots/` in your repo and store images there.  
Then use:


---

## 🛠 Tech Stack

- Python
- Flask
- MySQL
- Redis
- JWT Authentication
- Flask-JWT-Extended

---

## ✨ Features

✔ OTP-based login system  
✔ JWT authentication  
✔ Redis caching with TTL  
✔ User-based cache keys  
✔ Rate limiting to prevent spam  
✔ MySQL persistent storage  

---

## 📂 Project Structure

project/
│
├── app.py
├── db.py
├── redis_client.py
│
├── routes/
│ ├── auth.py
│ ├── quotes.py
│
├── requirements.txt
├── .env
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone repository

```bash
git clone https://github.com/your-username/project-name.git
cd project-name
2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Setup environment variables
Create .env file:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=yourdb

REDIS_HOST=localhost
REDIS_PORT=6379

JWT_SECRET=your-secret-key
5️⃣ Start Redis server
(make sure Redis is running)

6️⃣ Run Flask app
python app.py
📡 API Endpoints
🔹 Send OTP
POST /send-otp
Body:

{
  "email": "test@example.com"
}
🔹 Verify OTP
POST /verify-otp
Body:

{
  "email": "test@example.com",
  "otp": "123456"
}
🔹 Access Cached API (JWT required)
GET /quotes
Header:

Authorization: Bearer <your_token>

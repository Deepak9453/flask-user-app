# 🚀 Flask User Management App

## 📌 Project Overview
A simple Flask web application to manage users using a MySQL database with a clean Bootstrap UI.

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Deepak9453/flask-user-app.git
cd flask-user-app

2. Install dependencies
pip install flask
pip install mysql-connector-python
pip install python-dotenv

3. Create .env file
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=users

4. Run application
python app.py

http://127.0.0.1:5000/

---

## 🗄️ Database Setup

CREATE DATABASE users;

USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50)
);

---

## 🔧 Features

- View users
- Add user
- View user details
- Bootstrap UI
- Environment variables

---

## 🌿 Git Workflow

- Created branch: steptech_assignment
- Created Pull Request
- Merged into main

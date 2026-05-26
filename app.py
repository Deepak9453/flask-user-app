from flask import Flask, request, render_template, jsonify, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Home page
@app.route('/')
def home():
    return render_template("home.html")

# Hello route
@app.route('/hello')
def hello():
    return "Hello, World!"

# Users list
@app.route('/users')
def get_users():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        cursor.close()
        db.close()

        return render_template("users.html", users=users)

    except Exception:
        return "Error fetching users", 500


# User detail page ✅
@app.route('/users/<int:id>')
def get_user(id):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            return render_template("user_detail.html", user=user)
        else:
            return "User not found", 404

    except Exception:
        return "Error fetching user", 500


# Add new user
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            role = request.form.get('role')

            if not name or not email or not role:
                return "All fields are required"

            db = get_db_connection()
            cursor = db.cursor()

            query = "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, role))
            db.commit()

            cursor.close()
            db.close()

            return redirect(url_for('get_users'))

        except Exception:
            return "Error adding user", 500

    return render_template("new_user.html")


# Error handler
@app.errorhandler(404)
def not_found(error):
    return "Resource not found", 404


if __name__ == '__main__':
    app.run(debug=True)
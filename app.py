from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name,email) VALUES (?,?)",
        (name,email)
    )

    conn.commit()
    conn.close()

    return "Data Saved Successfully!"


if __name__ == "__main__":
    init_db()  # database check/create
    app.run(debug=True)

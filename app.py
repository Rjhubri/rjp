from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DB_NAME = "data.db"

# database create if not exists
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
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

    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        return render_template("index.html", message="Please fill all fields")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name,email) VALUES (?,?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    return render_template("index.html", message="Data Saved Successfully")


# database initialize
init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

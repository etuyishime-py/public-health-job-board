from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.before_request
def log_visit():
    ip = request.remote_addr
    with open("database/visitor_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {ip}\n")

@app.route("/", methods=["GET"])
def index():
    keyword = request.args.get("keyword", "")
    location = request.args.get("location", "")

    conn = sqlite3.connect("database/jobs.db")
    c = conn.cursor()
    query = "SELECT title, company, location, salary, link FROM jobs WHERE 1=1"
    params = []
    if keyword:
        query += " AND title LIKE ?"
        params.append(f"%{keyword}%")
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    c.execute(query, params)
    jobs = c.fetchall()

    c.execute("SELECT * FROM comments ORDER BY timestamp DESC")
    comments = c.fetchall()
    conn.close()

    return render_template("index.html", jobs=jobs, comments=comments, keyword=keyword, location=location)

@app.route("/comment", methods=["POST"])
def comment():
    name = request.form["name"]
    message = request.form["message"]
    conn = sqlite3.connect("database/jobs.db")
    c = conn.cursor()
    c.execute("INSERT INTO comments (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

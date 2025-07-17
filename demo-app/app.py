from flask import Flask, jsonify
import sqlite3, random

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, msg TEXT)")
    cur.execute("INSERT INTO logs (msg) VALUES ('Demo data')")
    conn.commit()
    cur.execute("SELECT msg FROM logs ORDER BY id DESC LIMIT 1")
    last_msg = cur.fetchone()[0]
    conn.close()
    return f"Hello from Demo-App! Last DB record: {last_msg}"

@app.route("/metrics")
def metrics():
    value = random.randint(1, 100)
    return jsonify({"random_metric": value})

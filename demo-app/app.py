from flask import Flask, jsonify
import sqlite3, random
import os

app = Flask(__name__)

@app.route("/")
def home():
    greeting = os.environ.get("GREETING_MESSAGE", "Demo-Uygulamasından Merhaba!")
    conn = sqlite3.connect('/data/db.sqlite')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, msg TEXT)")
    cur.execute("INSERT INTO logs (msg) VALUES ('Demo data')")
    conn.commit()
    cur.execute("SELECT msg FROM logs ORDER BY id DESC LIMIT 1")
    last_msg = cur.fetchone()[0]
    conn.close()
    return f"{greeting} Son DB kaydı: {last_msg}"

@app.route("/metrics")
def metrics():
    value = random.randint(1, 100)
    return f"# HELP random_metric A randomly generated number.\n" \
           f"# TYPE random_metric gauge\n" \
           f"random_metric {value}\n", 200, {'Content-Type': 'text/plain; charset=utf-8'} 


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

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
    return f"Demo-Uygulamasından Merhaba! Son DB kaydı: {last_msg}"

@app.route("/metrics")
def metrics():
    value = random.randint(1, 100)
    return jsonify({"rastgele_metrik": value})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

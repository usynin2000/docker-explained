from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)


def get_message():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )
    cur = conn.cursor()
    cur.execute("SELECT message FROM messages LIMIT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else "No data"

@app.route("/api/hello")
def hello():
    message = get_message()
    return jsonify(message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

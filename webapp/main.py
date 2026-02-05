from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.get("/")
def home():
    return "OK - webapp levantada"

@app.get("/db")
def db_check():
    url = os.environ.get("DATABASE_URL")
    if not url:
        return {"error": "DATABASE_URL no definido"}, 500

    with psycopg2.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM healthcheck;")
            n = cur.fetchone()[0]
    return {"healthcheck_rows": n}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

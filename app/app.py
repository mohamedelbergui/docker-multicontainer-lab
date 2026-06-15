from flask import Flask, jsonify, request
import os
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )
    return conn

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users", methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users;")
    rows = cur.fetchall()
    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })
    cur.close()
    conn.close()
    return jsonify(users)



@app.route("/users", methods=['POST'])
def set_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s,%s);",(name, email))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Utilisateur ajouté avec succès !"}), 201


app.run(host='0.0.0.0', port=5000)
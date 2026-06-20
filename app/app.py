from flask import Flask, jsonify, request
import os
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'db'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD')
        )
        return conn
    except Exception as e:
        return None

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users", methods=['GET'])
def get_users():
    conn = get_db_connection()
    if conn is not None:
        cur = conn.cursor()
        try:
            cur.execute("SELECT id, name, email FROM users;")
        except Exception as e:
            return jsonify({"message": str(e)}), 500
        else:
            rows = cur.fetchall()
            users = []
            for row in rows:
                users.append({
                    "id": row[0],
                    "name": row[1],
                    "email": row[2]
                })
            return jsonify(users) 
        finally:
            cur.close()
            conn.close()
    else :
        return jsonify({"message": "Connection to database failed!"}), 500



@app.route("/users", methods=['POST'])
def set_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"error": "name and email required"}), 400
    conn = get_db_connection()
    if conn is not None:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (name, email) VALUES (%s,%s);",(name, email))
            conn.commit()
        except Exception as e:
            conn.rollback()
            return jsonify({"message":str(e)}), 500
        else:
            return jsonify({"message": "Utilisateur ajouté avec succès !"}), 201
        finally:
            cur.close()
            conn.close()
    else :
        return jsonify({"message": "Connection to database failed!"}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
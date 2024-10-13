from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
  conn = mysql.connector.connect(
   host="db",
   user="myuser",
   password="mypassword",
   database="mydb"
  )
  return conn

@app.route('/')
def get_users():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute("SELECT * FROM users;")
  users = cur.fetchall()
  cur.close()
  conn.close()
  return jsonify(users)

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)

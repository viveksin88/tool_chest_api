from flask import Flask
from flask import jsonify
from flask import request
import sqlite3
import json
import jsonpickle
import model

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/transactions')
def get_transactions():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.commit()
    conn.close()
    return jsonify( [dict(transaction) for transaction in transactions] )

@app.route('/transactions', methods = ['POST'])
def add_transaction():
    request_data = request.get_json()
    conn = get_db_connection()
    transactions = conn.execute("INSERT INTO transactions (name, amount, transaction_type) VALUES (?, ?, ?)",(request.json.get("name"), request.json.get("amount"), request.json.get("transactionType"))).fetchall()
    conn.commit()
    conn.close()
    return request_data

if __name__ == '__main__':

    app.run(debug=True, port=3008, host='10.0.0.122')
from flask import Flask, jsonify, request
from flask_cors import CORS
from db_connection import connect, disconnect

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=["GET"])
def users():
    try:
        connection, cursor = connect

        query = 'SELECT * FROM users;'
        cursor.execute(query)
        respuesta = cursor.fetchall()
        disconnect(connection, cursor)

        return jsonify(respuesta)   
    

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
    
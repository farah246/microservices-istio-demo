from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/orders')
def get_orders():
    users = requests.get("http://user-service:5000/users").json()
    
    return jsonify({
        "orders": [
            {"id": 101, "user": users[0]["name"]},
            {"id": 102, "user": users[1]["name"]}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask Backend"})

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        
        # Process the data (you can add your logic here)
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        # Simple validation
        if not all([name, email, message]):
            return jsonify({"error": "All fields are required"}), 400
        
        # Process the data (example: just return it for now)
        result = {
            "status": "success",
            "data": {
                "name": name,
                "email": email,
                "message": message,
                "processed_at": "2023-11-02T18:00:00Z"
            }
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

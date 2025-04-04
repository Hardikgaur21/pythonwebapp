from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Azure Flask API!"})

@app.route('/api/data')
def get_data():
    return jsonify({
        "id": 1,
        "name": "Sample API",
        "status": "active"
    })

if __name__ == '__main__':
    app.run(debug=True)

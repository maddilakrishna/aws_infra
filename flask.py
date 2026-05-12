from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask Application!"

@app.route('/health')
def health():
    return jsonify({
        "status": "UP"
    })

@app.route('/api')
def api():
    return jsonify({
        "message": "Hello from Flask API"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

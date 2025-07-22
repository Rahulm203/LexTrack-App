from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Drip Mate backend is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    return jsonify({
        "message": "Received your data!",
        "your_input": data
    })

if __name__ == '__main__':
    app.run(debug=True)
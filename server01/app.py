from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    message = data.get('message')
    reply = "HELLO"  # Simple response
    return jsonify(reply=reply)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
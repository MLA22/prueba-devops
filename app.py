from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'

# Endpoint handler for /DevOps
@app.route('/DevOps', methods=['POST'])
def devops():
    # Verify API Key in headers
    api_key = request.headers.get('X-Parse-REST-API-Key')
    if api_key != API_KEY:
        return 'Unauthorized', 401

    # Get the request payload
    payload = request.get_json()
    if not payload:
        return 'Bad Request', 400

    # Extract the required fields from the payload
    message = payload.get('message')
    to = payload.get('to')
    from_ = payload.get('from')
    time_to_life_sec = payload.get('timeToLifeSec')

    if not message or not to or not from_ or not time_to_life_sec:
        return 'Bad Request', 400

    # Process the payload
    print(f"Received message: {message}")
    print(f"To: {to}")
    print(f"From: {from_}")
    print(f"Time to Life (sec): {time_to_life_sec}")

    # Prepare the response payload
    response = {
        'message': f"Hello {to} your message will be sent"
    }

    return jsonify(response)


# Handle other HTTP methods
@app.route('/DevOps', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def error():
    return 'ERROR', 405


# Run the Flask application
if __name__ == '__main__':
    app.run()

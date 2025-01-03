from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

normal = '1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvYyZz'
special = normal + '!@#$%^&*<>?'

def Password_generator(length=8, special_char='n'):
    length: int
    if not isinstance(length, int):
        return "Password length must be a number."
    elif length <= 0 or length > 20:
        return "Password length must be between 1 and 20."
    if special_char not in ['n', 'y']:
        return "Choose special characters: 'y' for yes or 'n' for no."

    password = random.sample(special if special_char == 'y' else normal, length)
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')  # This will render your HTML page


@app.route('/generate-password', methods=['POST'])
def generate_password():
    data = request.json
    length = data.get('length', 8)
    special_char = data.get('special_char', 'n')

    # Validate inputs
    if not isinstance(length, int) or length <= 0 or length > 20:
        return jsonify({"error": "Password length must be an integer between 1 and 20."}), 400

    if special_char not in ['n', 'y']:
        return jsonify({"error": "Choose special characters: 'y' for yes or 'n' for no."}), 400

    password = Password_generator(length, special_char)

    return jsonify({"Password": password}), 200

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Docker! Welcome to Flask"


# @app.route('/')
# def home():
#     return "Welcome to Docker!"


@app.route('/data')
def get_data():
    data = {"name": "John", "age": 30, "city": "New York"}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

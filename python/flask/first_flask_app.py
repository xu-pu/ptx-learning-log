from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello_view():
    return jsonify({'content': 'something'})

if __name__ == '__main__':
    app.run()

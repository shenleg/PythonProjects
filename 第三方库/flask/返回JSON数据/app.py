import json

from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/get_user1')
def get_user1():
    user = {"id": 1, "name": "张三1"}
    resp = make_response(user)
    return resp


@app.route('/get_user2')
def get_user2():
    user = {"id": 2, "name": "张三2"}
    return user


@app.route('/get_user3')
def get_user3():
    user = {"id": 3, "name": "张三3"}
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)

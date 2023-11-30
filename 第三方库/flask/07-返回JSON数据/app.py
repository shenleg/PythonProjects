from flask import Flask, make_response, jsonify

app = Flask(__name__)


# app.config['JSON_AS_ASCII'] = False

"""
以下方法都能设置相应头为 application/json
"""


@app.route('/data')
def data():
    user = {"id": 2, "name": "张三2"}
    return user


@app.route('/make_response')
def make_response1():
    user = {"id": 1, "name": "张三1"}
    resp = make_response(user)
    return resp


@app.route('/jsonify')
def jsonify1():
    user = {"id": 3, "name": "张三3"}
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)

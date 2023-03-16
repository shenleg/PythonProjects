from flask import Flask, make_response

app = Flask(__name__)


# 每个响应之前做处理
@app.before_request
def before_request():
    print("before_request")
    response = make_response()
    response.headers['Content-Type'] = 'application/json'
    response.headers['X-My-Ca'] = 'xiangpica'
    return response


@app.route('/a')
def index():
    print("index")
    return "Hello, 梦想橡皮擦!"


if __name__ == '__main__':
    app.run(debug=True)

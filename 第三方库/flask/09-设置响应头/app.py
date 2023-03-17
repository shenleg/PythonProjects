from flask import Flask, make_response

app = Flask(__name__)


@app.route('/get_user1')
def get_user1():
    # 创建一个响应对象
    resp = make_response("Hello Flask")  # 设置响应体
    # resp.status_code = 999  # 设置状态码
    resp.status = "888 fail"  # 设置状态码
    resp.headers['Content-Type'] = 'application/json'  # 设置响应头
    resp.headers['My-Mark'] = 'zxc'  # 设置响应头
    return resp


@app.route('/get_user2')
def get_user2():
    headers = {"Content-Type": "application/json", "My-Mark": "zyh"}
    return "Hello Flask", 777, headers


if __name__ == '__main__':
    app.run(debug=True)

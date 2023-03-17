from flask import Flask, make_response

app = Flask(__name__)


@app.route('/json')
def json():
    # 创建一个相应对象
    resp = make_response("Hello Flask!")  # 设置响应体
    # resp.status_code = 999  # 设置状态码
    resp.status = "888 fail"  # 设置状态码
    resp.headers['Content-Type'] = 'application/json'  # 设置响应头
    resp.headers['My-Mark'] = 'zxc'  # 设置响应头
    return resp


if __name__ == '__main__':
    app.run(debug=True)



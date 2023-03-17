from flask import Flask, make_response, request

app = Flask(__name__)


# 设置 cookie
@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置coolie, 默认有效期是临时cookie, 浏览器关闭就失效
    resp.set_cookie("item1", "Python1")
    resp.set_cookie("item2", "Python2")
    # max_age设置有效期，单位：秒
    resp.set_cookie("item3", "Python3", max_age=30)
    return resp


# 获取 cookie
@app.route("/get_cookie")
def get_cookie():
    c1 = request.cookies.get("item3")
    print(type(c1))  # 类型为：str
    return c1


# 删除 cookie
@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("item3")
    return resp


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)


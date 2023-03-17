import os
from datetime import timedelta

from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 生成过期日期

"""
session 是保存在服务器端的，用 session_id 来标识用户
"""


# 设置 session
@app.route("/set_session")
def set_session():
    session['username'] = '张三'
    session.permanent = True  # 设置有效期为 1 个月
    return "Session设置成功！"


# 获取 session
@app.route("/get_session")
def get_session():
    username = session.get("username")
    return username or "Session为空！"


# 删除 session
@app.route("/delete_session")
def delete_session():
    session.pop("username")
    return "session delete"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

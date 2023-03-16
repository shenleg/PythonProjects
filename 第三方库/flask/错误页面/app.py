from flask import Flask, render_template

app = Flask(__name__)


# 模板上下文处理函数，所有的模板都可以拿到此变量
@app.context_processor
def inject_user():
    user = {"name": "Grey Li"}
    return dict(user=user)


@app.route('/')
def index():
    return "hello", 200  # 默认状态码为200，可以不用写


# 注册一个错误处理函数
@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数

    return render_template('404.html'), 404

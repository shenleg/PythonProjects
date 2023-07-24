from flask import Flask

app = Flask(__name__)


# 定义路由规则，可为多个
@app.route('/hello')
# 定义响应函数
def hello():
    return 'Hello Flask!'


if __name__ == '__main__':
    # debug 模式兼具热启动功能
    app.run(host="127.0.0.1", port=5000, debug=True)


"""
命令行运行方式：flask run
> 文件名需要为：app.py
> 设置环境变量可以更改默认文件名：FLASK_APP=main.py
> 设置环境变量可以开启调试模式：FLASK_ENV=development
"""
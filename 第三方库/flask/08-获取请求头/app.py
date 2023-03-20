from flask import Flask, request

app = Flask(__name__)


@app.route('/request')
def request():
    header = request.headers  # 获取请求头
    form = request.form  # 获取表单参数
    args = request.args  # 获取查询参数
    cookies = request.cookies  # 获取 cookies
    data = request.data  # 包含了请求的数据，并转换为字符串
    files = request.files  # 上传文件
    method = request.method  # 请求方法
    environ = request.environ  # WSGI 隐含的环境配置
    json = request.json  # json 格式的数据

    # http://www.example.com/myapplication/page.html?x=y
    path = request.path  # /page.html
    script_root = request.script_root  # /myapplication
    base_url = request.base_url  # http://www.example.com/myapplication/page.html
    url = request.url  # http://www.example.com/myapplication/page.html?x=y
    url_root = request.url_root  # http://www.example.com/myapplication/
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

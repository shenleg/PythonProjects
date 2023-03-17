from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources="/*")  # 全局路由

"""
同源的意思就是，web 请求的接口的协议、域名、端口，有一个不同，就会出现跨域的情况

CORS 参数说明
参数	        类型	        Head字段          说明
resources   字典、迭代器或字符串  无全局配置允许跨域的 API 接口
origins     列表、字符串或正则表达式    Access-Control-Allow-Origin	配置允许跨域访问的源，* 表示全部允许
methods	    列表、字符串  Access-Control-Allow-Methods    配置跨域支持的请求方式，如：GET、POST
expose_headers  列表、字符串  Access-Control-Expose-Headers   自定义请求响应的 Head 信息
allow_headers   列表、字符串或正则表达式    Access-Control-Request-Headers  配置允许跨域的请求头
supports_credentials  布尔值	Access-Control-Allow-Credentials    是否允许请求发送 cookie，false 是不允许
max_age     整数、字符串  Access-Control-Max-Age  预检请求的有效时长
"""


# 定义路由规则，可为多个
@app.route('/')
@cross_origin(origins="*")  # 单行路由
# 定义响应函数
def hello():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)



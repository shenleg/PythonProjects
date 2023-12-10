import socket
from urllib import request, error

# URLError是OSError的子类，由request模块产生的异常都可以通过捕获这个类来处理
try:
    response = request.urlopen('https://www.baidu.com/404')
except error.URLError as e:
    print(e.reason)


# HTTPError是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等
# code属性就是返回状态码，reason属性是返回错误的原因, headers属性是返回请求头
try:
    response = request.urlopen('https://www.baidu.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")


# 由于URLError是HTTPError的父类，所以可以先捕获子类的错误，再捕获父类的错误
try:
    response = request.urlopen('https://www.baidu.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')


# 有时候reason属性返回的不一定是字符串，也可能是一个对象
# 这时候可以用isinstance()方法来判断
try:
    response = request.urlopen('https://www.baidu.com', timeout=0.01)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

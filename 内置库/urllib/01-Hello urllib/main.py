import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(type(response))  # 响应类型
print(response.status)  # 响应状态码
print(response.getheaders())  # 响应头信息
print(response.getheader('Server'))  # 获取响应头信息中的Server字段
print(response.read().decode('utf-8'))  # 响应体信息


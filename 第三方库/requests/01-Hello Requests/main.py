import requests

res = requests.get("https://www.baidu.com")
# 返回 HTTP 协议状态码
print(type(res.status_code), res.status_code)
# 以文本方式返回响应内容
print(type(res.text), res.text)
# 以二进制返回响应内容
print(type(res.content), res.content)

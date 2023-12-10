import requests

res = requests.get("https://httpbin.org/get")
# 获取响应头
print(type(res.headers), res.headers)
print(res.headers["Content-Type"])
print(res.headers.get("Content-Type"))
# 获取响应状态码
print(type(res.status_code), res.status_code)
print(res.status_code == requests.codes.ok)
# 获取响应状态码的原因
print(type(res.reason), res.reason)
# 从发送请求到收到响应所花费的时间
print(type(res.elapsed), res.elapsed)
# 获取响应编码
print(type(res.encoding), res.encoding)
# 获取重定向历史请求
print(type(res.history), res.history)
# 获取最终请求的 url
print(type(res.url), res.url)


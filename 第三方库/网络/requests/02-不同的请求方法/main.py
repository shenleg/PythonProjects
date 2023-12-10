import requests

# 不同的请求方法使用不同的函数
res = requests.get("https://httpbin.org/get")
print(res.status_code)
res = requests.post("https://httpbin.org/post")
print(res.status_code)
res = requests.put("https://httpbin.org/put")
print(res.status_code)
res = requests.delete("https://httpbin.org/delete")
print(res.status_code)
res = requests.patch("https://httpbin.org/patch")
print(res.status_code)

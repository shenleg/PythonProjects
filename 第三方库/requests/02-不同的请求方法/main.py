import requests

# 不同的请求方法使用不同的函数
res = requests.get("https://httpbin.org/get")
res = requests.post("https://httpbin.org/post")
res = requests.put("https://httpbin.org/put")
res = requests.delete("https://httpbin.org/delete")
res = requests.patch("https://httpbin.org/patch")


import requests

params1 = {
    "id": 1,
    "name": "张三"
}
params2 = {
    "hobby": ["eat", "烫头发"]
}

# data参数如果传入的是dict类型，自动设置 Content-Type为application/json

res = requests.post("https://httpbin.org/post", json=params1)
print(res.request.headers["Content-Type"])
print(res.text)

res = requests.post("https://httpbin.org/post", json=params2)
print(res.request.headers["Content-Type"])
print(res.text)

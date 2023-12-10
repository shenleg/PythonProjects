import requests

payload1 = {
    "id": 1,
    "name": "张三"
}
payload2 = {
    "hobby": ["eat", "烫头发"]
}
payload3 = (
    ("hobby", "eat"),
    ("hobby", "烫头发"),
)  # 解决一 key 多 value 情况

# data参数如果传入的是dict类型，自动设置 application/x-www-form-urlencoded

res = requests.post("https://httpbin.org/post", data=payload1)
print(res.request.headers["Content-Type"])
print(res.text)

res = requests.post("https://httpbin.org/post", data=payload2)
print(res.request.headers["Content-Type"])
print(res.text)


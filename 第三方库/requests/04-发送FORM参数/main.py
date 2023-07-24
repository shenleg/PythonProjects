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

# 根据参数的不同来变换请求头

# Content-Type: application/x-www-form-urlencoded
res = requests.post("http://127.0.0.1:5000/user", data=payload1)
print(res.request.headers["Content-Type"])
print(type(res.text), res.text)

# Content-Type: application/x-www-form-urlencoded
res = requests.post("http://127.0.0.1:5000/hobby", data=payload2)
print(res.request.headers["Content-Type"])
print(type(res.text), res.text)

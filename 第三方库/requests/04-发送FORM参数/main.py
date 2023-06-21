import requests

params1 = {
    "id": 1,
    "name": "张三"
}
params2 = {
    "hobby": ["eat", "烫头发"]
}

# 根据参数的不同来变换请求头

# Content-Type: application/x-www-form-urlencoded
res = requests.post("http://127.0.0.1:5000/user", data=params1)
print(res.request.headers["Content-Type"])
print(type(res.text), res.text)

# Content-Type: application/x-www-form-urlencoded
res = requests.post("http://127.0.0.1:5000/hobby", data=params2)
print(res.request.headers["Content-Type"])
print(type(res.text), res.text)

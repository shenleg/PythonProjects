import requests

params1 = {
    "id": 1,
    "name": "张三"
}
params2 = {
    "hobby": ["eat", "烫头发"]
}

# Content-Type: application/json
res = requests.post("http://127.0.0.1:5000/user", json=params1)
print(res.request.headers["Content-Type"])
print(type(res.text), res.text)

# Content-Type: application/json
res = requests.post("http://127.0.0.1:5000/hobby", json=params2)
print(res.request.headers["Content-Type"])
print(type(res.text), res.text)

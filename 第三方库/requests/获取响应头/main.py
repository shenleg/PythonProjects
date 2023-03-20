import requests


# Content-Type: application/json
res = requests.get("http://127.0.0.1:5000/get_user1")
print(res.headers["Content-Type"])
print(res.headers["MyMark"])
print(res.status_code)
print(type(res.text), res.text)

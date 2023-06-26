import requests


res = requests.get("http://127.0.0.1:5000/get_user2")
print(res.headers["Content-Type"])
print(res.headers["My-Mark"])
print(res.status_code)
print(res.reason)
print(type(res.text), res.text)

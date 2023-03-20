import requests

res = requests.get("http://127.0.0.1:5000/get_user1")
print(res.headers["Content-Type"])
print(type(res.json()), res.json())

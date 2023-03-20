import requests


# Content-Type: application/json
res = requests.get("http://127.0.0.1:5000/user")
res.request.headers["Content-Type"] = "application/json"
res.request.headers["MyMark"] = "zxc"
print(type(res.text), res.text)

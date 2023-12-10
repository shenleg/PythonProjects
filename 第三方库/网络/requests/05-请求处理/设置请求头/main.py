import requests

headers = {"Content-Type": "text/plain", "MyMark": "zxc"}
res = requests.get("http://127.0.0.1:5000/request", headers=headers)
print(type(res.text), res.text)

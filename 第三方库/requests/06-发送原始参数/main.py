import requests


data = "Hello Requests"

headers = {"Content-Type": "text/plain"}
res = requests.post("http://127.0.0.1:5000/data", data=data, headers=headers)
print(type(res.text), res.text)

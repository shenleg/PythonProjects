import requests


data = "Hello Requests"
byte_data = data.encode("utf-8")

headers = {"Content-Type": "text/plain"}
res = requests.post("http://127.0.0.1:5000/data", data=byte_data, headers=headers)
print(type(res.text), res.text)

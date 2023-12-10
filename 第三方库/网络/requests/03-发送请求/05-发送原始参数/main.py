import requests


data = "Hello Requests"
byte_data = data.encode("utf-8")

headers = {"Content-Type": "text/plain"}
res = requests.post("https://httpbin.org/post", data=byte_data, headers=headers)
print(res.request.headers["Content-Type"])
print(res.text)

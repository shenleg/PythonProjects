import requests

res = requests.get("https://httpbin.org/get")
print(res.status_code)
print(type(res.text), res.text)


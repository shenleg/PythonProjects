import requests


res = requests.get("https://httpbin.org/get")
print(res.request)
print(res.request.method)
print(res.request.path_url)
print(res.request.url)
print(res.request.headers)
print(res.request.body)

import requests


res = requests.get("http://127.0.0.1:5000/get_user2")
print(res.request)
print(res.request.method)
print(res.request.path_url)
print(res.request.url)
print(res.request.headers)
print(res.request.body)

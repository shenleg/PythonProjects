import urllib

import requests

params1 = {
    "id": 1,
    "name": "张三"
}
params2 = {
    "id": 1,
    "hobby": ["eat", "烫头发"]
}

# http://127.0.0.1:5000/user?id=1&name=张三
res = requests.get("http://127.0.0.1:5000/user", params=params1)
print(res.url)
print(type(res.text), res.text)

# http://127.0.0.1:5000/hobby?id=1&hobby=eat&hobby=烫头
res = requests.get("http://127.0.0.1:5000/hobby", params=params2)
print(urllib.parse.unquote(res.url))
print(type(res.text), res.text)

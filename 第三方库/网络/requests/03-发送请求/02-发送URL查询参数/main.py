from urllib.parse import unquote

import requests

params1 = {
    "id": 1,
    "name": "张三"
}
params2 = {
    "id": 1,
    "hobby": ["eat", "烫头发"]
}

# https://httpbin.org/get?id=1&name=张三
res = requests.get("https://httpbin.org/get", params=params1)
print(res.url)  # 自动编码
print(res.text)

# https://httpbin.org/get?id=1&hobby=eat&hobby=烫头
res = requests.get("https://httpbin.org/get", params=params2)
print(unquote(res.url))
print(res.text)

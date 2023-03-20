import requests

# 设置 cookie
cookies = {"key3": "value3"}
requests.get("http://127.0.0.1:5000/get_cookie", cookies=cookies)

# 获取 cookie
res = requests.get("http://127.0.0.1:5000/set_cookie")
for cookie in res.cookies:
    print(cookie)

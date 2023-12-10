import requests

# 设置 cookie
cookies = {"key": "value"}
requests.get("https://127.0.0.1:5000/set_cookie", cookies=cookies)
headers = {"Cookie": "key=value"}
requests.get("http://127.0.0.1:5000/set_cookie", headers=headers)

# 获取 cookie
res = requests.get("https://www.baidu.com/")
# 打印 cookie 属性值
for cookie in res.cookies:
    print(cookie.name, cookie.value, cookie.domain, cookie.expires, cookie.path)
for name, value in res.cookies.items():
    print(name, value)

# 打印出res.cookies字典
print(type(res.cookies.get_dict()), res.cookies.get_dict())
# 打印出res.cookies字典中BDORZ的值
print(res.cookies.get("BDORZ"))
print(res.cookies["BDORZ"])

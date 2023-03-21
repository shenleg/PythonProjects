import requests

res = requests.get("http://127.0.0.1:5000/get_user1")
print(res.content)
print(res.content.decode("utf-8"))
print(res.content.decode("unicode_escape"))
print(res.headers["Content-Type"])
print(type(res.json()), res.json())  # 自动解码 unicode 并转换为字典

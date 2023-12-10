import requests

res = requests.get("https://httpbin.org/get")

# 1.以二进制形式返回响应内容
print(type(res.content), res.content)
# 解码
print(res.content.decode("utf-8"))
print(res.content.decode("unicode_escape"))

# 2.以文本形式返回响应内容
# 设置可接收的编码为 utf-8
res.encoding = "utf-8"
print(type(res.text), res.text)

# 3.如果是 json 格式可以转换为字典
print(res.headers["Content-Type"])
print(type(res.json()), res.json())  # 自动解码 unicode 并转换为字典

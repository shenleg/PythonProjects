from urllib.parse import parse_qsl

# parse_qsl()方法将url的get请求参数转换为元组组成的列表
query = 'name=tom&age=22'
print(parse_qsl(query))
# [('name', 'tom'), ('age', '22')]

# 再转换为字典
d = dict(parse_qsl(query))
print(d)
# {'name': 'tom', 'age': '22'}

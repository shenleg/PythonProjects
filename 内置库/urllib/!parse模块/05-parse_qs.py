from urllib.parse import parse_qs

# parse_qs()方法将url的get请求参数转换为字典类型
query = 'name=tom&age=22'
print(parse_qs(query))
# {'name': ['tom'], 'age': ['22']}


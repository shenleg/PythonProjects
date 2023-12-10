from urllib.parse import urlencode

# urlencode()方法将字典数据转换为url的get请求参数

params = {
    'name': 'tom',
    'age': 22
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
# https://www.baidu.com?name=tom&age=22

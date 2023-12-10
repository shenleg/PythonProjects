from urllib import request, parse

url = 'https://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# 将字典数据转换为字符串，再转换为字节流
data = bytes(parse.urlencode({'name': 'tom'}), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')

response = request.urlopen(req)
print(response.read().decode('utf-8'))



import urllib.parse
import urllib.request

# 将字典数据转换为字符串，再转换为字节流
data = bytes(urllib.parse.urlencode({'name': 'tom'}), encoding='utf-8')
response = urllib.request.urlopen('https://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

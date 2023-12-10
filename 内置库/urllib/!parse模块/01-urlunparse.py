from urllib.parse import urlunparse

# urlunparse()方法将6个部分组合成一个完整的url
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
# http://www.baidu.com/index.html;user?a=6#comment

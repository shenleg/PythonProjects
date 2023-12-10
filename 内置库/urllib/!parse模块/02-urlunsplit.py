from urllib.parse import urlunsplit

# urlunsplit()方法将5个部分组合成一个完整的url
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))



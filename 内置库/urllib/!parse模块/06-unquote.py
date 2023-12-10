from urllib.parse import unquote

# quote()方法可以将内容转换为URL编码的格式
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
# https://www.baidu.com/s?wd=壁纸

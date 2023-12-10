from urllib.parse import quote

# quote()方法可以将内容转换为URL编码的格式
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
# https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8




import http.cookiejar
import urllib.request

# 获取网站 cookie
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)

# 将 cookie 保存到文件, MozillaCookieJar 可以保存成 Mozilla 浏览器的 cookie 格式
filename = 'cookie1.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 将 cookie 保存到文件, LWPCookieJar 可以保存成 libwww-perl 格式的 cookie
filename = 'cookie2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 从文件中读取 cookie
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))

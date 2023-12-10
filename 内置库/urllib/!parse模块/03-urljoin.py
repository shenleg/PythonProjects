from urllib.parse import urljoin

# urljoin()方法将base_url和new_url拼接成一个完整的url
print(urljoin('https://www.baidu.com', 'FAQ.html'))
# https://www.baidu.com/FAQ.html
print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# https://cuiqingcai.com/FAQ.html
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# https://cuiqingcai.com/FAQ.html
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# https://cuiqingcai.com/FAQ.html?question=2
print(urljoin('https://www.baidu.com/?wd=abc', 'https://cuiqingcai.com/index.html'))
# https://cuiqingcai.com/index.html
print(urljoin('https://www.baidu.com', '?category=2#comment'))
# https://www.baidu.com?category=2#comment
print(urljoin('www.baidu.com', '?category=2#comment'))
# www.baidu.com?category=2#comment
print(urljoin('www.baidu.com#comment', '?category=2'))
# www.baidu.com?category=2

# base_url 提供了三项内容：scheme、netloc、path，如果这3项在new_url里不存在，就予以补充；如果存在，就使用new_url里的部分

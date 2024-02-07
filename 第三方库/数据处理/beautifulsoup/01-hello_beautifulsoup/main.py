from bs4 import BeautifulSoup

# html 和 body 节点没有闭合
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="tom"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="https://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>'''

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())  # 格式化网页自动闭合
print(type(soup.title), soup.title)  # <class 'bs4.element.Tag'>
print(soup.head)  # 获取 head 标签
print(soup.p)  # 获取第一个 p 标签

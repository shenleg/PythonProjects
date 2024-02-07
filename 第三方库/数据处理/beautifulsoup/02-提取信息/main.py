from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
    <p class="story">
        Once upon a time there were three
        <a href="https://example.com/elsie" class="sister" id="link1">
            <span>Elsie</span>
        </a>
        <a href="https://example.com/elsie" class="sister" id="link1">Lacie</a>
        and
        <a href="https://example.com/elsie" class="sister" id="link1">Tillie</a>
    </p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')

print(soup.title.name)  # 获取标签名称
print(soup.title.string)  # 获取标签内的文本
print(soup.p.attrs)  # 获取标签属性
print(soup.p.attrs["class"])  # 获取标签属性
print(soup.p["name"])  # 获取标签属性

print(soup.head.title)  # 嵌套获取标签

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

print("获取直接子节点列表，既包含文本，又包含节点")
print(soup.p.contents)

# 节点列表包含空白节点信息！！！
print("获取直接子节点迭代器")
print(soup.p.children)
for index, child in enumerate(soup.p.children):
    print(index, type(child), child)


print("获取所有子孙节点迭代器")
print(soup.p.descendants)
for index, child in enumerate(soup.p.descendants):
    print(index, type(child), child)

print("获取父节点")
print(soup.a.parent)
print("获取所有祖先节点")
print(list(enumerate(soup.a.parents)))
# 兄弟节点会包含空白节点信息！！！
print("获取下一个兄弟节点")
print(soup.a.next_sibling)
print("获取上一个兄弟节点")
print(soup.a.previous_sibling)
print("获取后面所有兄弟节点")
print(list(enumerate(soup.a.next_siblings)))
print("获取前面所有兄弟节点")
print(list(enumerate(soup.a.previous_siblings)))
print("获取下一个节点")
print(soup.a.next_element)
print("获取上一个节点")
print(soup.a.previous_element)
print("获取后面所有节点")
print(list(enumerate(soup.a.next_elements)))
print("获取前面所有节点")
print(list(enumerate(soup.a.previous_elements)))

import re

from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
print("标签名查询")
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]), soup.find_all(name='ul')[0])

print("嵌套查询")
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

print("属性查询")
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'class': 'element'}))
print(soup.find_all(id='list-1'))  # 常用属性直接查询
print(soup.find_all(class_='element'))  # 常用属性直接查询

print("正则匹配节点的文本")
print(soup.find_all(string=re.compile("Foo")))

print("查找第一个节点")
print(soup.find(name='ul'))
print("查找父节点")
print(soup.find(name='ul').find_parent())
print("查找祖先节点")
print(soup.find(name='ul').find_parents())
print("查找取后面所有兄弟节点")
print(soup.find(name='ul').find_next_siblings())
print("查找前面所有兄弟节点")
print(soup.find(name='ul').find_previous_siblings())
print("查找后面所有节点")
print(soup.find(name='ul').find_all_next())
print("查找后面第一个节点")
print(soup.find(name='ul').find_next())
print("查找前面所有节点")
print(soup.find(name='ul').find_all_previous())
print("查找前面第一个节点")
print(soup.find(name='ul').find_previous())

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
print(soup.select(".panel .panel-heading"))
print(soup.select("ul li"))
print(soup.select("#list-2 .element"))
print(soup.select("ul")[0])

print("获取属性")
for ul in soup.select("ul"):
    print(ul.select("li"))  # 嵌套选择
    print(type(ul))
    print(ul["id"])
    print(ul.attrs["id"])
    print(ul.get("id"))
    print(ul.get("class"))
    print(ul.get("class", "default"))

print("获取文本")
for li in soup.select("li"):
    print("=======")
    print(li.get_text())
    print(li.string)
    print(li.get_text("|", strip=True))
    print(li.string.strip())

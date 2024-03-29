from pyquery import PyQuery as pq
import requests

html = """
<div>
<ul>
    <li class="item-0">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""

# 字符串初始化
doc = pq(html)
print(type(doc("li")), doc("li"))

# URL 初始化
doc = pq(url="https://cuiqingcai.com")
print(type(doc("title")), doc("title"))
doc = pq(requests.get("https://cuiqingcai.com").text)  # 等同于
print(type(doc("title")), doc("title"))

# 文件初始化
doc = pq(filename="demo.html")
print(type(doc("li")), doc("li"))


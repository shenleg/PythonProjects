from pyquery import PyQuery as pq

html = """
<div id="container">
<ul class="list">
    <li class="item-0">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""

doc = pq(html)
items = doc(".list")
print(type(items))
print(items)

print("查找子孙节点")
lis = items.find("li")
print(type(lis))
print(lis)

print("查找直接子节点")
lis = items.children("li")
print(type(lis))
print(lis)

print("加入选择器")
lis = items.children(".active")
print(type(lis))
print(lis)

print("查找直接父节点")
lis = items.parent()
print(type(lis))
print(lis)

print("查找祖先节点-分别返回")
lis = items.parents()
print(type(lis))
print(lis)

print("加入选择器")
lis = items.parents("#container")
print(type(lis))
print(lis)

print("查找所有兄弟节点")
li = doc(".list .item-0.active")
print(li.siblings())

print("遍历节点")
lis = doc(".list .item-0.active").siblings().items()
print(type(lis))
for li in lis:
    print(li)
    print(type(li))
    print(li.text())
    print(li.attr("class"))
    print("===")

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
print("节点 class 属性操作")
li = doc(".item-0.active")
print(li)

li.removeClass("active")
print(li)
li.addClass("active")
print(li)

print("节点一般属性操作")
li = doc(".item-0.active")
print(li)
li.attr("name", "link")  # 添加属性
print(li)
li.css("font-size", "14px")  # 添加行内样式
print(li)
li.text("changed item")  # 修改节点文本
print(li)
li.html("<span>changed item</span>")  # 修改节点内部 HTML
print(li)


print("节点删除")
li.find("span").remove()
print(li)

print("节点添加")
l = pq("<li>1</li>")  # 创建节点
ul = doc(".list")
ul.append(l)  # 添加到 ul 节点末尾
print(ul)
l = pq("<li>1</li>")  # 创建节点，已被添加的不能再被添加
ul.prepend(l)  # 添加到 ul 节点开头
print(ul)

print("清空节点")
ul = doc(".list")
ul.empty()
print(ul)


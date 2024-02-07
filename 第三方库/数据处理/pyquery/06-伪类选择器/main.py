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
print(doc("li:first-child"))  # li 第一个子元素
print(doc("li:last-child"))  # li 最后一个子元素
print(doc("li:nth-child(2)"))  # li 第二个子元素
print(doc("li:gt(2)"))  # li 第三个之后的子元素
print(doc("li:nth-child(2n)"))  # li 偶数位置的子元素
print(doc("li:contains(second)"))  # li 包含 second 文本的子元素

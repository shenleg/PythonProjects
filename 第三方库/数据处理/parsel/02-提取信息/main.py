from parsel import Selector

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

selector = Selector(html)
items = selector.css(".item-0")
for item in items:
    text = item.xpath("text()").get()
    print(text)

# result = selector.xpath("//li[@class='item-0']//text()").get()
# print(result)
#
# result = selector.xpath("//li[@class='item-0']//text()").getall()
# print(result)
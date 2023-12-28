from lxml import etree

html = etree.parse("index.html", etree.HTMLParser())
result = html.xpath("//li")
print(result)
print(result[0])

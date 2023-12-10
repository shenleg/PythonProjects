import httpx

client = httpx.Client(http2=True)
res = client.get("https://spa16.scrape.center")
print(res.http_version)  # 输出 HTTP 协议版本
print(res.text)


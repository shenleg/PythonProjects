import httpx

# 操作方法和 requests 类似

res = httpx.get("https://httpbin.org/get")
print(res.status_code)
print(type(res.text), res.text)

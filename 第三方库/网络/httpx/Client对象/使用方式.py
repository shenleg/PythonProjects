import httpx

with httpx.Client() as client:
    res = client.get("https://httpbin.org/get")
    print(res.text)

# 等价于
client = httpx.Client()
try:
    res = client.get("https://httpbin.org/get")
finally:
    client.close()



import requests

# 设置连接超时和读取超时总时间
res = requests.get("https://httpbin.org/get", timeout=1)

# 设置连接超时和读取超时时间
res = requests.get("https://httpbin.org/get", timeout=(1,2))

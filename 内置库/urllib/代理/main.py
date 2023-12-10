from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

proxy_handler = ProxyHandler({
    "http": "http://127.0.0.1:7890",
    "https": "https://127.0.0.1:7890",
})

opener = build_opener(proxy_handler)

try:
    result = opener.open("https://httpbin.org/get")
    print(result.read().decode("utf-8"))
except URLError as e:
    print(e.reason)


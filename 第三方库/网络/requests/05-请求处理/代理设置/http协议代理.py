import requests

proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "https://127.0.0.1:7890",
}
res = requests.get("https://httpbin.org/get", proxies=proxies)
print(res.status_code)

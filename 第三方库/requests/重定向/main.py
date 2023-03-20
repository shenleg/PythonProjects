import requests

# allow_redirects=False：阻止重定向
res = requests.get("http://127.0.0.1:5000/login", allow_redirects=True)
print(res.url)
print(res.status_code)
print(res.history)  # 如果重定向了，则会记录历史请求
print(res.text)


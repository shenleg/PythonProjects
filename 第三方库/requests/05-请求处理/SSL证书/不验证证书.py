import requests
import urllib3

# 忽略警告
urllib3.disable_warnings()
response = requests.get("https://ssr2.scrape.center/", verify=False)
print(response.status_code)

# 指定证书，key 必须是解密状态
response = requests.get("https://ssr2.scrape.center/", cert=("server.crt", "server.key"))
print(response.status_code)

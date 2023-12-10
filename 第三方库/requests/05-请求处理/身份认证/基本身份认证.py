import requests
from requests.auth import HTTPBasicAuth

username = "admin"
password = "admin"
url = "https://ssr3.scrape.center"

res = requests.get(url, auth=HTTPBasicAuth(username, password))
print(res.status_code)

res = requests.get(url, auth=(username, password))
print(res.status_code)

res = requests.get(f"https://{username}:{password}@ssr3.scrape.center")
print(res.status_code)

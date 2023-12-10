import httpx

url = "https://httpbin.org/headers"
headers = {"zyh": "zxc"}
with httpx.Client(headers=headers) as client:
    res = client.get(url)
    print(res.status_code)
    print(res.json()["headers"]["Zyh"])

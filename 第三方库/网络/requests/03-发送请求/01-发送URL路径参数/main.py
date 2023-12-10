import requests


res = requests.get("https://httpbin.org/get/book_name/词典")
print(type(res.text), res.text)

res = requests.get("https://httpbin.org/get/book_path/cook/sink")
print(type(res.text), res.text)

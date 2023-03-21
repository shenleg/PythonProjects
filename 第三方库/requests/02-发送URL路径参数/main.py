import requests


res = requests.get("http://127.0.0.1:5000/book_name/词典")
print(type(res.text), res.text)

res = requests.get("http://127.0.0.1:5000/book_path/cook/sink")
print(type(res.text), res.text)
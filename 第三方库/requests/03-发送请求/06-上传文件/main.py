import requests

# files 自动设置 Content-Type: multipart/form-data;

# 上传单个文件
files = {"filename": open("requests.txt", "rb")}
res = requests.post("https://httpbin.org/post", files=files)
print(res.request.headers["Content-Type"])
print(res.text)

# 上传多个文件
files = {
    "filename1": open("requests.txt", "rb"),
    "filename2": open("requests.txt", "rb")
}
res = requests.post("https://httpbin.org/post", files=files)
print(res.request.headers["Content-Type"])
print(res.text)

# 上传文件+表单数据
data = {
    "name": "张三",
    "age": 18
}
files = {"file": open("requests.txt", "rb")}
res = requests.post("https://httpbin.org/post", data=data, files=files)
print(res.request.headers["Content-Type"])
print(res.text)

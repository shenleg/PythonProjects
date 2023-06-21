import requests

# 上传单个文件
# files = {"filename": open("requests.txt", "rb")}
# requests.post("http://127.0.0.1:5000/upload", files=files)

# 上传多个文件
# files = {"filename1": open("requests.txt", "rb"), "filename2": open("requests.txt", "rb")}
# requests.post("http://127.0.0.1:5000/upload", files=files)

# 上传文件+表单数据
# data = {
#     "name": "张三",
#     "age": 18
# }
# files = {"file": open("requests.txt", "rb")}
# requests.post("http://127.0.0.1:5000/upload", data=data, files=files)


# 下载小文件
res = requests.get("http://127.0.0.1:5000/download")
with open("图片1.png", "wb") as f:
    f.write(res.content)

# 下载大文件
res = requests.get("http://127.0.0.1:5000/download", stream=True)
with open("图片2.png", "wb") as f:
    for chunk in res.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)



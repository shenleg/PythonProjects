import requests

# 上传文件，可上传多个文件
# files = {"file": open("requests.txt", "rb")}
# requests.post("http://127.0.0.1:5000/upload", files=files)


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



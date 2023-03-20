import requests

"""
手动处理 cookies、headers，状态保持
"""
res = requests.post("http://127.0.0.1:5000/login")
requests.post("http://127.0.0.1:5000/shop", cookies=res.cookies)  # 需要传入登录返回的 cookies

"""
自动处理 cookies、headers，状态保持
"""
session = requests.session()
session.post("http://127.0.0.1:5000/login")
session.post("http://127.0.0.1:5000/shop")  # 已经登录了，不需要再手动传 cookies

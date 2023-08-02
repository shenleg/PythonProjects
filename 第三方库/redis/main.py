import json
import time

import redis  # 导入redis 模块

user = {
    "id": 1,
    "name": "张三"
}

r = redis.Redis(host='10.30.0.11', port=6479, decode_responses=True, password="test123456")
r.hset('info', "user1", "45")  # 设置 name 对应的值
r.hset('info', "user2", json.dumps(user, ensure_ascii=True))  # 设置 name 对应的值
print(r.hget('info', "user1"))  # 取出键 name 对应的值
print(type(r.hget('info', "user1")))  # 查看类型

print(r.hgetall("info"))
print(type(r.hgetall("info")))

r.flushall()


"""
存入的统统为字符串，取出来也是字符串
"""
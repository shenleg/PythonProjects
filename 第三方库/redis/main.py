import json
import time

import redis  # 导入redis 模块

user = {
    "id": 1,
    "name": "张三"
}

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# r.hset('info', "user1", json.dumps(user, ensure_ascii=False))  # 设置 name 对应的值
# r.hset('info', "user2", json.dumps(user, ensure_ascii=True))  # 设置 name 对应的值
print(r.hget('info', "user1"))  # 取出键 name 对应的值
print(type(r.hget('info', "user1")))  # 查看类型

print(r.hgetall("info"))
print(type(r.hgetall("info")))

r.flushall()
from enum import Enum
from typing import Union, Optional

from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


class Name(str, Enum):
    satori = "古明地觉"
    koishi = "古明地恋"
    marisa = "雾雨魔理沙"


"""
3.8 3.9 3.10 区别
Optional[str] 和 str | None 等价
Union[int, str] 和 int | str 等价
这种写法 3.10 才开始引入，通过 from __future__ import annotations 也可以在 3.9 里面使用，而 3.8 是不支持的

Query 不支持给"路径参数"做校验！
"""


# 单个类型，默认是必传值
# http://127.0.0.1:5000/book_id?book_id=2
@app.get('/book_id')
def get_book_id(book_id: int):
    return f'book_id is {book_id}, type is {type(book_id)}!'


# 多选一类型，使用Union
# http://127.0.0.1:5000/user1?user_id=1
@app.get('/user1')
def get_user1(user_id: Union[int, str]):
    return f'user_id is {user_id}，type is {type(user_id)}!'


# 可选值，默认值，使用Query、Optional
# http://127.0.0.1:5000/user2
@app.get('/user2')
def get_user2(user_id: int = Query(12), user_name: Optional[str] = None):
    return f'user_id is {user_id} type is {type(user_id)} and ' \
           f'user_name is {user_name} type is {type(user_name)}!'


# 长度、匹配限制，使用Query
# http://127.0.0.1:5000/user3?user_name=atom
@app.get('/user3')
def get_user3(user_name: str = Query(min_length=2, max_length=4, pattern=r"^tom")):
    return f'user_name is {user_name}, type is {type(user_name)}!'


# 数值校验，使用Query
# http://127.0.0.1:5000/items?item1=6&item2=5&item3=10
@app.get('/items')
def get_items(item1: int = Query(gt=5), item2: int = Query(le=7), item3: int = Query(ge=10, le=10)):
    return {"item1": item1, "item2": item2, "item3": item3}


# 必传且限制
# http://127.0.0.1:5000/user4?user_name=aa
@app.get('/user4')
async def get_user4(user_name: str = Query(..., min_length=3)):
    return f'user_name is {user_name}, type is {type(user_name)}!'


# 枚举类型，定义好枚举类
# http://127.0.0.1:5000/user5?user_name=a
@app.get("/user5")
async def get_user5(user_name: Name):
    return {"user_name": user_name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

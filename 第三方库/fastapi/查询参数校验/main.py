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
例子：
1. http://127.0.0.1:5000/book_id/2
2. http://127.0.0.1:5000/users/a
3. http://127.0.0.1:5000/users2
4. http://127.0.0.1:5000/users3/tom444
5. http://127.0.0.1:5000/items

3.8 3.9 3.10 区别
Optional[str] 和 str | None 等价
Union[int, str] 和 int | str 等价
这种写法 3.10 才开始引入，通过 from __future__ import annotations 也可以在 3.9 里面使用，而 3.8 是不支持的

Query 不支持给"路径参数"做校验！
"""


# 单个类型，必传值
@app.get('/book_id/{book_id}')
def get_book_id(book_id: int):
    print("book_id type is", type(book_id))
    return f'book_id is {book_id}!'


# 多选一类型
@app.get('/users/{user_id}')
def get_user(user_id: Union[int, str]):
    print("user_id type is", type(user_id))
    return f'user_id is {user_id}!'


# 可选值
@app.get('/users2')
def get_user2(user_id: int = Query(12), user_name: Optional[str] = None):
    print("user_id type is", type(user_id))
    print("user_name type is", type(user_name))
    return f'user_id is {user_id} and user_name is {user_name}!'


# 长度、匹配限制
@app.get('/users3')
def get_user3(user_name: str = Query(min_length=2, max_length=4, pattern=r"^tom")):
    print("user_name type is", type(user_name))
    return f'user_name is {user_name}!'


# 数值校验
@app.get('/items')
def get_user3(item1: int = Query(gt=5), item2: int = Query(le=7), item3: int = Query(ge=10, le=10)):
    return {"item1": item1, "item2": item2, "item3": item3}


# 枚举类型
@app.get("/user/{user_name}")
async def get_user(user_name: Name):
    return {"user_name": user_name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

from enum import Enum
from typing import Union, Optional

from fastapi import FastAPI
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
3. http://127.0.0.1:5000/user/张三

3.8 3.9 3.10 区别
# Optional[str] 和 str | None 等价
>>> name: Optional[str] = "古明地觉"
>>> name: str | None = "古明地觉"

# Union[int, str] 和 int | str 等价
>>> age: Union[int, str] = 17
>>> age: int | str = 17
这种写法 3.10 才开始引入，通过 from __future__ import annotations 也可以在 3.9 里面使用，而 3.8 是不支持的
"""


# 单个类型
@app.get('/book_id/{book_id}')
def get_book_id(book_id: int):
    print("book_id type is", type(book_id))
    return f'book_id is {book_id}!'


# 多选一类型、默认值
@app.get('/users/{user_id}')
def get_user(user_id: Union[int, str], user_name: Optional[str] = None):
    print("user_id type is", type(user_id))
    print("user_name type is", type(user_name))
    return f'user_id is {user_id} and user_name is {user_name}!'


# 枚举类型
@app.get("/user/{user_name}")
async def get_user(user_name: Name):
    return {"user_name": user_name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

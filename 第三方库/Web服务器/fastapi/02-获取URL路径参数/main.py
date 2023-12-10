from enum import Enum

from fastapi import FastAPI
import uvicorn

app = FastAPI()

"""
路由解析顺序从上至下
例子：
1. http://127.0.0.1:5000/book_name/词典
2. http://127.0.0.1:5000/book_id/2
4. http://127.0.0.1:5000/book_path/cook/sink
"""


# 支持中文，返回也是中文
@app.get("/book_name/{book_name}")
def get_book_name(book_name):
    print("book_name type is", type(book_name))
    return f'book_name is {book_name}!'


# 参数类型预定义，默认为 str，支持 str、int、float、path
# bool 1 True on yes 会被解释成 True
# bool 0 False off no 会被解释成 False
# 不能转换会报错
@app.get('/book_id/{book_id}')
def get_book_id(book_id: int):
    print("book_id type is", type(book_id))
    return f'book_id is {book_id}!'


# 路径参数带斜杆
@app.get('/book_path/{book_path:path}')
def get_book_path(book_path: str):
    print(type(book_path))
    return f'book_path is {book_path}!'


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

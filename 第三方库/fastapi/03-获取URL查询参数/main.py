from fastapi import FastAPI
import uvicorn

app = FastAPI()

"""
例子：
1. http://127.0.0.1:5000/user/1?name=张三&age=18
2. http://127.0.0.1:5000/hobby?id=1&hobby=eat&hobby=烫头
"""

# 和路径参数混用
@app.get("/user/{user_id}")
def get_user(user_id: int, name: str, age: int):
    print("user_id type is", type(user_id))
    print("name type is", type(name))
    print("age type is", type(age))
    return f'id is {user_id} and name is {name} and age is {age}!'

# 查询参数默认值，可以不用传
@app.get("/user/{user_id}")
def get_user(user_id: int, name: str, age: int = 0):
    print("user_id type is", type(user_id))
    print("name type is", type(name))
    print("age type is", type(age))
    return f'id is {user_id} and name is {name} and age is {age}!'

@app.get('/hobby')
def get_hobby(user_id: int, hobby: list):
    print("user_id type is", type(user_id))
    print("hobby type is", type(hobby))  # list 类型
    return f'id is {user_id} and name is {hobby}!'


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

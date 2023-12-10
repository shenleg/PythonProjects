from fastapi import FastAPI
import uvicorn

# 1.创建核心app
app = FastAPI()


# 2.定义路由规则，可为多个
@app.get("/hello")
# 3.定义响应函数
def hello():
    return "Hello, FastAPI"


if __name__ == "__main__":
    # 启动服务，因为我们这个文件叫做 main.py
    # 所以需要启动 main.py 里面的 app
    # 第一个参数 "main:app" 就表示这个含义
    # reload 模式兼具热启动功能
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)

"""
Swagger 文档：http://127.0.0.1:5000/docs
Swagger 文档：http://127.0.0.1:5000/docs
"""

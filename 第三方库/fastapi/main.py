from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def hello():
    return {"code": 0, "msg": "TOKEN 验证失败！", "data": "success"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9001, reload=True)

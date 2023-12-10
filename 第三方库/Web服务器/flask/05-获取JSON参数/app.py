from flask import Flask, request

app = Flask(__name__)

"""
例子：
Content-Type: application/json
1. {"id": 1, "name": "张三"}
2. {"id": 1, "hobby": ["eat", "烫头"]}
"""


@app.route('/user', methods=["POST"])
def get_user():
    # 获取类型根据传入json来决定
    data = request.json
    id = data.get("id", 0)
    name = data["name"]
    print("id type is", type(id))
    print("name type is", type(name))
    return f'id is {id} and name is {name}!'


@app.route('/hobby', methods=["POST"])
def get_hobby():
    hobby = request.json
    print("hobby type is", type(hobby))  # dict 类型
    return f'hobby is {hobby}!'


# 强制编码转换，非 Content-Type: application/json
@app.route('/text', methods=["POST"])
def get_text():
    hobby = request.get_json(force=True)
    print("content_type:", request.headers.get("content_type"))
    print("hobby type is", type(hobby))
    return f'hobby is {hobby}!'


if __name__ == '__main__':
    app.run(debug=True)


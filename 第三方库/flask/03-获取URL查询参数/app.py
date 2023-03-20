from flask import Flask, request

app = Flask(__name__)

"""
例子：
1. http://127.0.0.1:5000/user?id=1&name=张三
2. http://127.0.0.1:5000/hobby?id=1&hobby=eat&hobby=烫头
"""


@app.route('/user')
def get_user():
    # 默认获取到的都是字符串类型
    id = request.args.get("id", 0)
    name = request.args["name"]
    print("id type is", type(id))
    print("name type is", type(name))
    return f'id is {id} and name is {name}!'


@app.route('/hobby')
def get_hobby():
    id = request.args.get("id", 0)
    hobby = request.values.getlist("hobby")
    print("id type is", type(id))
    print("hobby type is", type(hobby))  # list 类型
    return f'id is {id} and name is {hobby}!'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

"""
例子：
"""


@app.route('/user', methods=["POST"])
def get_user():
    # 默认获取到的都是字符串类型
    id = request.data
    print("id type is", type(id))
    return f'id is {id}!'


@app.route('/hobby', methods=["POST"])
def get_hobby():
    hobby = request.form.getlist("hobby")
    print("hobby type is", type(hobby))  # list 类型
    return f'name is {hobby}!'


if __name__ == '__main__':
    app.run(debug=True)

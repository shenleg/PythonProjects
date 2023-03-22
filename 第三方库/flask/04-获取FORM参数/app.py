from flask import Flask, request

app = Flask(__name__)

"""
例子：
<form method="post" action="/test">
    id: <input type="input" name="id"> <br>
    name: <input type="input" name="name"> <br>
    hobby: <input type="checkbox" name="hobby"> eat
    <input type="checkbox" name="hobby"> 烫头 <br>
    <input type="submit" value="提交">
</form>

<form method="post" action="/test" enctype="multipart/form-data">
    file: <input type="file" name="file"> <br>
    hobby: <input type="checkbox" name="hobby"> eat
    <input type="checkbox" name="hobby"> 烫头 <br>
    <input type="submit" value="提交">
</form>

支持 Content-Type: application/x-www-form-urlencoded  # form 默认
    Content-Type: multipart/form-data  # form 文件上传
"""


@app.route('/user', methods=["POST"])
def get_user():
    # 默认获取到的都是字符串类型
    id = request.form.get("id", "0")
    name = request.form["name"]
    print("id type is", type(id))
    print("name type is", type(name))
    return f'id is {id} and name is {name}!'


@app.route('/hobby', methods=["POST"])
def get_hobby():
    hobby = request.form.getlist("hobby")
    print("hobby type is", type(hobby))  # list 类型
    return f'name is {hobby}!'


if __name__ == '__main__':
    app.run(debug=True)

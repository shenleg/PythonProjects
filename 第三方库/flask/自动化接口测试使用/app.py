from flask import Flask, request, make_response

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False


# 获取URL路径参数
# http://127.0.0.1:5000/user/张三
@app.route('/user/<name>')
def get_name(name):
    return {"name": name}


# 获取URL查询参数
# http://127.0.0.1:5000/hobby1?hobby=eat&hobby=烫头
@app.route('/hobby1')
def get_hobby1():
    hobby = request.values.getlist("hobby")
    return {"hobby": hobby}
    # id = request.args.get("id", 0)
    # name = request.args["name"]
    # return {"id": id, "name": name}


# 获取URL查询参数
# http://127.0.0.1:5000/hobby2?id=1&name=张三
@app.route('/hobby2')
def get_hobby2():
    id = request.args.get("id", 0)
    name = request.args["name"]
    return {"id": id, "name": name}


# 获取FROM参数
@app.route('/form', methods=["post"])
def get_form():
    id = request.form.get("id", "0")
    name = request.form["name"]
    return {"id": id, "name": name}


# 获取JSON参数
@app.route('/json', methods=["post"])
def get_json():
    data = request.json
    id = data.get("id", 0)
    name = data["name"]
    return {"id": id, "name": name}


if __name__ == '__main__':
    app.run(debug=True)

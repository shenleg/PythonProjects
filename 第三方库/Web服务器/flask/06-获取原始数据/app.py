from flask import Flask, request

app = Flask(__name__)

"""
例子：
"""


@app.route('/data', methods=["POST"])
def get_data():
    # 字节数据
    data = request.data
    print("data type is", type(data))
    print("data type is", type(data.decode("utf-8")))
    return f'data is {data.decode("utf-8")}!'


if __name__ == '__main__':
    app.run(debug=True)

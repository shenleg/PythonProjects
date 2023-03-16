from flask import Flask

app = Flask(__name__)

"""
例子：
1. http://localhost:5000/book_name/词典
2. http://localhost:5000/book_path/cook/sink
"""


# 支持中文，返回也是中文
# 默认就是 get 请求
@app.route('/book_name/<book_name>', methods=["GET"])
def get_book_name(book_name):
    print("book_name type is", type(book_name))
    return f'book_name is {book_name}!'


# 参数类型预定义，支持 string、int、float、path
# 不能转换会报错
@app.route('/book_id/<int:book_id>')
def get_book_id(book_id):
    print("book_id type is", type(book_id))
    return f'book_id is {book_id}!'


@app.route('/book_path/<path:book_path>')
def get_book_path(book_path):
    print(type(book_path))
    return f'book_path is {book_path}!'


if __name__ == '__main__':
    app.run(debug=True)

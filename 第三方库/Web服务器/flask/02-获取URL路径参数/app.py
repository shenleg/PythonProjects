from flask import Flask

app = Flask(__name__)

"""
路由解析顺序从上至下
例子：
1. http://127.0.0.1:5000/book_name/词典
2. http://127.0.0.1:5000/book_id/2
3. http://127.0.0.1:5000/book_path/cook/sink
"""


# 支持中文，返回也是中文
# 默认就是 get 请求
@app.route('/book_name/<book_name>', methods=["GET"])
def get_book_name(book_name):
    print("book_name type is", type(book_name))
    return f'book_name is {book_name}!'


# 参数类型预定义，默认为 str，支持 str、int、float、path
# 不能转换会报错
@app.route('/book_id/<int:book_id>')
def get_book_id(book_id):
    print("book_id type is", type(book_id))
    return f'book_id is {book_id}!'


# 路径参数带斜杆
@app.route('/book_path/<path:book_path>')
def get_book_path(book_path):
    print(type(book_path))
    return f'book_path is {book_path}!'


if __name__ == '__main__':
    app.run(debug=True)

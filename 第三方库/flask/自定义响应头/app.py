from flask import Flask, make_response

app = Flask(__name__)


@app.route('/json')
def json():
    # 创建一个相应对象
    resp = make_response("Hello Flask!")
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    resp.headers['My-Mark'] = 'zxc'
    return resp


if __name__ == '__main__':
    app.run(debug=True)



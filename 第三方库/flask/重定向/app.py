from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return 'Hello Flask!'


@app.route('/login')
def login():
    return redirect(url_for("index"))


@app.route('/baidu')
def baidu():
    return redirect("https://www.baidu.com")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

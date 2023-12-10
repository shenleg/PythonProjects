from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask!'


@app.route('/book/<name>')
def book(name):
    return f'Hello {name}!'


@app.route('/test_url_for')
def test_url_for():
    print(url_for('hello'))  # /
    print(url_for('book', name='词典'))  # /book/%E8%AF%8D%E5%85%B8
    print(url_for('test_url_for'))  # /test_url_for
    return f'Hello'


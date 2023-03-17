from flask import Flask, render_template

app = Flask(__name__)


# 模板上下文处理函数，所有的模板都可以拿到此变量
@app.context_processor
def inject_user():
    user = {"name": "Grey Li"}
    return dict(user=user)


movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
def index():
    return render_template('index.html', movies=movies)


@app.route('/sub1')
def sub1():
    return render_template('sub1.html')


@app.route('/sub2')
def sub2():
    return render_template('sub2.html')


if __name__ == '__main__':
    app.run(debug=True)

"""
查看所有过滤器：https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters
"""

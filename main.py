from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import Blueprint

from todo import main as todo_routes


app = Flask(__name__)
app.secret_key = 'random string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 注册蓝图
app.register_blueprint(todo_routes, url_prefix='/todo')

# 默认端口是 5000
if __name__ == '__main__':
    app.run(debug=True)

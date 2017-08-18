from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __repr__(self):
        return u'<ToDo {} {}>'.format(self.id, self.task)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, form):
        self.task = form.get('task', '')
        self.created_time = int(time.time())


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    print('rebuild database')

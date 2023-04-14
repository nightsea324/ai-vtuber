import os
import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init(flaskApp):
    flaskApp.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRESQL_URL")
    flaskApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(flaskApp)
    with flaskApp.app_context():
        db.create_all()
    return flaskApp


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    messages = db.Column(db.ARRAY(db.JSON))

    def __init__(self, id, messages):
        self.id = id
        self.messages = messages

    def to_dict(self):
        return {
            "id": self.id,
            "messages": self.messages
        }


def get_all_users():
    users = User.query.all()
    print([user.to_dict() for user in users])


def create_user(id, messages):
    user = User(id, messages)
    db.session.merge(user)
    db.session.commit()

    return 201

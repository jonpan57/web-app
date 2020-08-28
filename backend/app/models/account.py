from datetime import datetime
from ...app import db

'''
GET, POST, PUT, PATCH, DELETE
'''

class AbstractDatetime(db.Model):
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 更新时间

class User(AbstractDatetime):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))


class UserInfo(AbstractDatetime):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))


class Role(AbstractDatetime):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))


class Permission(AbstractDatetime):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))


class Workshop(AbstractDatetime):  # 工作站
    __tablename__ = 'group_workshop'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

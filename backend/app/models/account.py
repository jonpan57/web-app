from ...app import db

'''
GET, POST, PUT, PATCH, DELETE
'''


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))


class Workshop(db.Model):  # 工作站
    __tablename__ = 'group_workshop'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

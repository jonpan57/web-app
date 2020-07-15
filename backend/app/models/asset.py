from app import db


class IDC(db.Model):
    __tablename__ = 'asset_idc'
    id = db.Column('id', db.Integer, primary_key=True, auto_increment=True)
    name = db.Column('name', db.String(255), unique=True, nullable=False)

from ...app import db


class Station(db.Model):
    __tablename__ = 'group_station'
    id = db.Column('id', db.Integer, primary_key=True, auto_increment=True)  # 车站id自增长
    name = db.Column('name', db.String(100), unique=True, nullable=False)  # 车站名称
    addr = db.Column('addr', db.String(100))  # 车站地址
    coord = db.Column('coord', db.String(100))  # 车站坐标
    type = db.Column('tpye', db.String(100))  # 车站类型
    spell = db.Column('spell', db.String(100))  # 车站简拼
    code = db.Column('code', db.String(100))  # 车站代码
    idc = db.relationship('IDC', backref='station', lazy='dynamic')


class IDC(db.Model):
    __tablename__ = 'asset_idc'
    id = db.Column('id', db.Integer, primary_key=True, auto_increment=True)  # 机房id自增长
    name = db.Column('name', db.String(255), unique=True, nullable=False)  # 机房名称
    addr = db.Column('addr', db.String(100))  # 机房地址
    coord = db.Column('coord', db.String(100))  # 机房坐标
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))


class Cabinet(db.Model):
    __tablename__ = 'asset_cabinet'
    id = db.Column('id', db.Integer, primary_key=True, auto_increment=True)
    name = db.Column('name', db.String(255), unique=True, nullable=False)  # 机房名称

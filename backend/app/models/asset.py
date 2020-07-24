from ...app import db


class Station(db.Model):
    __tablename__ = 'group_station'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)  # 车站标识，自增长
    name = db.Column(db.String(100), unique=True, nullable=False)  # 车站名称
    address = db.Column(db.String(100))  # 车站地址
    coord = db.Column(db.String(100))  # 车站坐标
    type = db.Column(db.String(100))  # 车站类型
    spell = db.Column(db.String(100))  # 车站简拼
    code = db.Column(db.String(100))  # 车站代码
    idc = db.relationship('IDC', backref='station', lazy='dynamic')


class Idc(db.Model):  # 机房
    __tablename__ = 'asset_idc'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)  # 机房标识，自增长
    name = db.Column(db.String(255), unique=True, nullable=False)  # 机房名称
    address = db.Column(db.String(100))  # 机房地址
    coord = db.Column(db.String(100))  # 机房坐标
    contact = db.column(db.String(100))
    bandwidth = db.Column(db.String(100))  # 机房带宽
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))


class Cabinet(db.Model):
    __tablename__ = 'asset_cabinet'
    id = db.Column('id', db.Integer, primary_key=True, auto_increment=True)
    name = db.Column('name', db.String(255), unique=True, nullable=False)  # 机房名称

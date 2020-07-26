from ...app import db


class Station(db.Model):  # 车站
    __tablename__ = 'asset_station'  # 如果不指定表名，默认以类名小写作为表名
    id = db.Column(db.Integer, primary_key=True)  # 车站标识
    name = db.Column(db.String(100), unique=True, nullable=False)  # 车站名称
    address = db.Column(db.String(100))  # 车站地址
    latitude = db.Column(db.Float)  # 车站经度
    longitude = db.Column(db.Float)  # 车站纬度
    type = db.Column(db.String(100))  # 车站类型
    spell = db.Column(db.String(100))  # 车站简拼
    code = db.Column(db.String(100))  # 车站代码
    idc = db.relationship('Idc', backref='station', lazy='True')


class Idc(db.Model):  # 机房
    __tablename__ = 'asset_idc'
    id = db.Column(db.Integer, primary_key=True)  # 机房标识
    name = db.Column(db.String(255), nullable=False)  # 机房名称
    address = db.Column(db.String(100))  # 机房地址
    latitude = db.Column(db.Float)  # 机房经度
    longitude = db.Column(db.Float)  # 机房纬度
    contact = db.Column(db.String(100))  # 联系人
    telephone = db.Column(db.String(100))  # 联系电话
    bandwidth = db.Column(db.String(100))  # 机房带宽
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)


class Cabinet(db.Model):  # 机房
    __tablename__ = 'asset_cabinet'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), unique=True, nullable=False)  # 机房名称

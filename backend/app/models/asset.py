from ...app import db

tag_station = db.Table('tag_station',
                       db.Column('line_id', db.Integer, db.ForeignKey('line.id')),
                       db.Column('station_id', db.Integer, db.ForeignKey('station_id')),
                       db.Column('order_no'), db.Integer)


class Line(db.Model):  # 线路
    __tablename__ = 'asset_line'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 线路标识
    name = db.Column(db.String(8), unique=True, nullable=False)  # 线路名称
    active_time = db.Column(db.Date)  # 开通时间
    length = db.Column(db.Float)  # 线路长度
    design_speed = db.Column(db.Integer)  # 设计速度
    operation_speed = db.Column(db.Integer)  # 运营速度
    count = db.Column(db.Integer)  # 车站数量


class Station(db.Model):  # 车站
    __tablename__ = 'asset_station'  # 如果不指定表名，默认以类名小写作为表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 车站标识
    name = db.Column(db.String(6), unique=True, nullable=False)  # 车站名称
    active_time = db.Column(db.Date)  # 投用时间
    grade = db.Column(db.Integer)  # 车站等级————特等站：0、一等站：1、二等站：2、三等站：3、四等站：4、五等站：5
    business = db.Column(db.Integer)  # 车站类型———— 主要业务分类：客运站、货运站、编组站
    '''
    照作业性质：客运站、货运站、客货运站、工业站、联轨站、港湾站、国境站、换装站、线路所。
    按技术作业：编组站、区段站、技术站、中间站、会让站、越行站。

    业务性质：客运站、货运站、客货运站、不办理客货运的站（包括会让站、越行站、线路所等）
    普速/高速：普速车站、高铁车站、普速高铁共用车站
    技术性质：中间站、技术站（区段站、编组站）
    车场配置方式：横列式、纵列式、混合式
    '''
    address = db.Column(db.String(32))  # 车站地址
    latitude = db.Column(db.Float)  # 车站经度
    longitude = db.Column(db.Float)  # 车站纬度

    line = db.relationship('Line', secondary=tag_station, backref=db.backref('stations'))
    idc = db.relationship('Idc', backref='station')


class Idc(db.Model):  # 机房
    __tablename__ = 'asset_idc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 机房标识
    name = db.Column(db.String(255), nullable=False)  # 机房名称

    contact = db.Column(db.String(6))  # 联系人
    telephone = db.Column(db.String(11))  # 联系电话
    network = db.Column(db.String(100))  # 机房网络
    ip_range = db.Column(db.Text())  # ip范围
    bandwidth = db.Column(db.String(100))  # 机房带宽
    remark = db.Column(db.String(255))  # 备注信息

    address = db.Column(db.String(32))  # 机房地址
    latitude = db.Column(db.Float)  # 机房经度
    longitude = db.Column(db.Float)  # 机房纬度

    station = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    cabinet = db.relationship('Cabinet', backref='idc')


class Cabinet(db.Model):  # 机房
    __tablename__ = 'asset_cabinet'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), unique=True, nullable=False)  # 机房名称

    idc = db.Column(db.Integer, db.ForeignKey('idc.id'))

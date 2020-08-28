from datetime import datetime
from ...app import db


class AbstractDate(db.Model):
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 更新时间


line_station = db.Table('line_station',
                        db.Column('line_id', db.Integer, db.ForeignKey('asset_line.id')),
                        db.Column('station_id', db.Integer, db.ForeignKey('asset_station.id')),
                        db.Column('order_no'), db.Integer)

'''
server：服务器
    physical：物理机
    virtual：虚拟机
    container：容器
    storage：存储设备
network：网络设备
    repeater:中继
        hub:集线器
        fiber converter:光纤收发器
    bridge:网桥
    route：路由器
    gateway:网关
    firewall：防火墙
    switch：交换机
    
综合布线
    语音配线架
    网络配线架
    网络理线架
    光纤配线架
'''

'''
设备状态
    启用
    停用
    故障
    其他
'''


class Line(AbstractDate):  # 线路
    __tablename__ = 'asset_line'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 线路标识
    name = db.Column(db.String(8), unique=True, nullable=False)  # 线路名称
    enable_date = db.Column(db.Date)  # 开通时间
    length = db.Column(db.Float)  # 线路长度
    design_speed = db.Column(db.Integer)  # 设计速度
    operation_speed = db.Column(db.Integer)  # 运营速度

    station = db.relationship('Station', secondary=line_station)


class Station(AbstractDate):  # 车站
    __tablename__ = 'asset_station'  # 如果不指定表名，默认以类名小写作为表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 车站标识
    name = db.Column(db.String(8), unique=True, nullable=False)  # 车站名称
    enable_date = db.Column(db.Date)  # 投用时间
    grade = db.Column(db.Enum('特等站', '一等站', '二等站', '三等站', '四等站', '五等站'))  # 车站等级
    type = db.Column(db.Enum('客货运站', '客运站', '货运站', '其他站'))  # 车站类型
    speed = db.Column(db.Enum('高铁站', '共用站', '普速站'))  # 车站速度
    '''
    根据上述的三个维度，判断车站故障处理的轻重缓急,影响故障显示的优先级顺序
    '''
    address = db.Column(db.String(32))  # 车站地址
    latitude = db.Column(db.DECIMAL(9, 6))  # 车站经度
    longitude = db.Column(db.DECIMAL(8, 6))  # 车站纬度

    idc = db.relationship('Idc')


class Idc(AbstractDate):  # 机房
    __tablename__ = 'asset_idc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 机房标识
    name = db.Column(db.String(16), nullable=False)  # 机房名称

    contact = db.Column(db.String(6))  # 联系人
    telephone = db.Column(db.String(11))  # 联系电话
    network = db.Column(db.String(100))  # 机房网络
    ip_range = db.Column(db.Text())  # ip范围
    bandwidth = db.Column(db.String(5))  # 机房带宽
    remark = db.Column(db.String(255))  # 备注信息

    address = db.Column(db.String(32))  # 机房地址
    latitude = db.Column(db.Float)  # 机房经度
    longitude = db.Column(db.Float)  # 机房纬度

    station_id = db.Column(db.Integer, db.ForeignKey('asset_station.id'))
    cabinet = db.relationship('AssetCabinet', backref='idc')


class Cabinet(AbstractDate):  # 机柜
    __tablename__ = 'asset_cabinet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 机柜标识
    name = db.Column(db.String(3), nullable=False)  # 机柜名称

    brand = db.Column(db.String(8))  # 机柜品牌
    model = db.Column(db.String(8))  # 机柜型号
    unit_height = db.Column(db.Integer)  # 机柜Unit高度，单位为U
    standard_width = db.Column(db.Integer)  # 机柜标准宽度，单位为英寸

    height = db.Column(db.Integer)  # 机柜高度，单位为mm
    width = db.Column(db.Integer)  # 机柜宽度，单位为mm
    depth = db.Column(db.Integer)  # 机柜深度，单位为mm

    idc_id = db.Column(db.Integer, db.ForeignKey('asset_idc.id'))


class AssetHost(AbstractDate):  # 主机
    __tablename__ = 'asset_host'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String(8), unique=True, nullable=False)
    status = db.Column(db.Integer)
    interface = db.relationship('AssetHost', backref='host')


class AssetHostInterface(db.Model):  # 主机接口
    __tablename__ = 'asset_host_interface'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dns = db.Column(db.String(8))
    ip = db.Column(db.String(15))
    port = db.Column(db.String(5))
    type = db.Column(db.Integer)
    useip = db.Column(db.Integer)

    host = db.Column(db.Integer, db.ForeignKey('host.id'))


class AssetServer(db.Model):
    __tablename__ = 'asset_server'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class AssetNetwork(db.Model):
    __tablename__ = 'asset_network'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

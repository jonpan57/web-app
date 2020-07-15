import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 默认的本地数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

# mssql：佛山西的指纹数据库，oracle：原来的指纹数据库
SQLALCHEMY_BINDS = {}

# 数据库信息反馈关闭
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 启用CSSRP和密匙
CSPR_ENABLED = True
SECRET_KEY = 'Devil_never_cry'

DEBUG = True

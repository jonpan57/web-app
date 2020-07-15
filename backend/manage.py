from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand

import config


def _make_context():
    return dict(app=app, db=db)


app = create_app(config)
manager = Manager(app)
manager.add_command('shell', Shell(_make_context=_make_context()))
manager.add_command('db', MigrateCommand)
'''
启动命令：
    runserver
数据库命令：
    install    创建数据库文件
    migrate    迁移数据库操作 
    upgrade    更新数据库内容
    downgrade  撤销数据库操作
'''
if __name__ == '__main__':
    manager.run()

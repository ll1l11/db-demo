# -*- coding: utf-8 -*-

from flask_script import Manager

from demo import create_app
from demo.database import db


manager = Manager(create_app)


@manager.command
def create_all():
    # 只重新创建默认数据库的表
    db.drop_all(bind=None)
    db.create_all(bind=None)


if __name__ == '__main__':
    manager.run()

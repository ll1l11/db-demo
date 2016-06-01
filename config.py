# -*- coding: utf-8 -*-
DEBUG = False
SECRET_KEY = 'thisissecretkey'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@dbhost/db_demo'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_BINDS = {
        'demo2': 'mysql+pymysql://root:root@dbhost/db_demo2',
}

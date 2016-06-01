# -*- coding: utf-8 -*-
import json
from sqlalchemy import PickleType
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StringPickleType(PickleType):
    impl = db.String(255)

    def __init__(self, pickler=json, **kwargs):
        super(StringPickleType, self).__init__(pickler=pickler, **kwargs)


db.StringPickleType = StringPickleType

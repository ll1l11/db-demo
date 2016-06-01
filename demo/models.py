# -*- coding: utf-8 -*-
import json
from sqlalchemy.schema import Index
from demo.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gym_id = db.Column(db.Integer)
    tags = db.Column(db.StringPickleType, default=dict)
    insert_time = db.Column(db.DateTime)


class User2(db.Model):
    __bind_key__ = 'demo2'
    id = db.Column(db.Integer, primary_key=True)
    name2 = db.Column(db.String(100))


class UserPost(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)
    insert_time = db.Column(db.DateTime)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'post_id', name='uix_user_post_user_id_post_id'),
        db.Index('ix_user_post_user_id_insert_time', 'user_id', 'insert_time'),
    )

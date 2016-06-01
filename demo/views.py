# -*- coding: utf-8 -*-

from flask import Blueprint

from .models import User

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    User.query.all()
    return 'a'

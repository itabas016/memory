#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from memory.extensions.flasksqlalchemy import db
from memory.models.base import Base

class Comment(Base):

    __tablename__ = 'm_comment'
    
    name            = db.Column(db.String(256), nullable=False)
    email           = db.Column(db.String(128), nullable=False)
    content         = db.Column(db.Text, nullable=True)
    post_id         = db.Column(db.Integer, nullable=False)
    external_id     = db.Column(db.Integer, nullable=True)
    external_addr   = db.Column(db.String(512), nullable=True)
    external_date   = db.Column(db.DateTime,  default=db.func.current_timestamp())
    via             = db.Column(db.String(128), nullable=False)
    ext_1           = db.Column(db.String(256), nullable=False)
    ext_2           = db.Column(db.String(512), nullable=False)
    status          = db.Column(db.SmallInteger, default=1)
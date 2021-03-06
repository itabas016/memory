#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from memory.extensions.flasksqlalchemy import db
from memory.models.base import Base

class Source(Base):

    __tablename__ = 'm_source'
    
    name     = db.Column(db.String(128), nullable=False)
    account  = db.Column(db.String(64), nullable=False)
    icon_url = db.Column(db.String(256), nullable=True)
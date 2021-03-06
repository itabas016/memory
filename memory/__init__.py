#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from flask import Flask

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    from memory.extensions.flasksqlalchemy import db
    db.init_app(app)

    from memory.logger import init_logger
    init_logger(app)

    from memory.controllers.admin import bp_admin
    app.register_blueprint(bp_admin)

    from memory.controllers.post import bp_post
    app.register_blueprint(bp_post)

    from memory.controllers.twitter import bp_twitter
    app.register_blueprint(bp_twitter)

    from memory.controllers.hollow import bp_hollow
    app.register_blueprint(bp_hollow)

    from memory.controllers.error import bp_error
    app.register_blueprint(bp_error)

    with app.app_context():
        db.create_all()
    return app

# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import logging
from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/anteater/api")

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    app.logger.info("Anteater startup")

    return app

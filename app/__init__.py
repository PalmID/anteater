# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import logging
from flask import Flask
from flasgger import Swagger


def create_app():
    app = Flask(__name__)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/anteater/api")

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    app.logger.info("Anteater startup")

    Swagger(
        app,
        config={
            "headers": [],
            "specs": [{"endpoint": "apispec", "route": "/anteater/apispec.json"}],
            "swagger_ui_bundle_js": "//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js",
            "swagger_ui_standalone_preset_js": "//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js",
            "jquery_js": "//unpkg.com/jquery@2.2.4/dist/jquery.min.js",
            "swagger_ui_css": "//unpkg.com/swagger-ui-dist@3/swagger-ui.css",
            "static_url_path": "/anteater/flasgger_static",
            "swagger_ui": True,
            "uiversion": 3,
            "specs_route": "/anteater/apidocs",
            "openapi": "3.0.1",
        },
    )

    return app

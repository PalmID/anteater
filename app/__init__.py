# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import os
import sys
import inspect
from flask import Flask

from werkzeug.utils import import_string


class App(Flask):
    def _register_extension(self, name, ext):
        ext.init_app(self)
        if name not in self.extensions:
            self.extensions[name] = ext

    def load_extensions(self):
        def is_ext(ext):
            return not inspect.isclass(ext) and hasattr(ext, "init_app")

        module = import_string("app.extensions")
        for name, ext in inspect.getmembers(module, is_ext):
            self._register_extension(name, ext)
        return self.extensions

    def register_blueprints(self):
        from app.api import bp as api_bp

        self.register_blueprint(api_bp, url_prefix="/anteater/api")


def create_app(root_path=None):
    if root_path is None:
        root_path = os.getcwd()
    sys.path.append(root_path)
    env = os.getenv("FLASK_ENV", "development")
    config = import_string("configs.{}".format(env))
    app_cls = import_string("app:App")

    app = app_cls(__name__, root_path=root_path)
    app.config.from_object(config)

    app.load_extensions()
    app.register_blueprints()
    app.app_context().push()
    return app

# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import os
from functools import wraps

from flasgger import Swagger as SwaggerBase
from flasgger import swag_from


class Swagger(SwaggerBase):
    def init_app(self, app, *args, **kwargs):
        super().init_app(app, *args, **kwargs)
        self.docs_root = os.path.join(
            self.app.root_path, self.app.config["SWAGGER_DOCS_ROOT"]
        )

    def swag_from(self, doc_name, **swag_kwargs):
        def decorator(view_func):
            abs_doc_path = os.path.join(self.docs_root, doc_name)
            wrap_func = swag_from(specs=abs_doc_path, **swag_kwargs)

            @wraps(view_func)
            def wrapper(*args, **kwargs):
                return wrap_func(*args, **kwargs)

            return wrapper

        return decorator

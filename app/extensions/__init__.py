# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from peeweext.flask import Peeweext

from .swagger import Swagger

pwx = Peeweext()
swagger = Swagger(template_file="docs/openapi_template.yaml")

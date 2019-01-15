# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import json

from flask import Response


def JsonResponse(data=None, code=200):
    return Response(json.dumps(data or {}), status=code, mimetype="application/json")

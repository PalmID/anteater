# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import json

from flask import Response


def JsonResponse(data=None, code=200, msg=None):
    if data is not None:
        payload = {"objects": data} if isinstance(data, list) else data
    else:
        payload = {"errors": {}, "msg": msg} if msg else {}
    return Response(json.dumps(payload), status=code, mimetype="application/json")


def enum2choices(enum):
    return tuple((f.value, f.name) for f in enum)

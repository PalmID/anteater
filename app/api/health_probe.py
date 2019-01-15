# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import request
from flask.views import MethodView

from app.utils import JsonResponse


class HealthProbeView(MethodView):
    def get(self):
        probe_type = request.args.get("type")
        if probe_type in ["liveness", "readiness"]:
            return JsonResponse()
        else:
            return JsonResponse(code=404)

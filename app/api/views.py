# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import json
import time

from flasgger import swag_from
from flask import Response, render_template, request, send_file
from flask.views import MethodView


class ApiRootView(MethodView):
    def get(self):
        return render_template("fine_uploader/index.html")


class PalmDetectionView(MethodView):
    """Detect if there is a palm in the image."""

    @swag_from("../../docs/api/palm_detection_post.yml")
    def post(self):
        """Create a palm detection job."""
        # palm = request.files["palmimage"]
        # if palm:
        #     current_app.logger.info(request.files)
        #     pass
        # TODO: 创建手掌检测异步任务，获取job_id，异步启动处理
        time.sleep(5)
        return Response(json.dumps({}), status=200, mimetype="application/json")

    def get(self):
        """Query the status of detection job by job id."""
        return "detection get"


class ROIExtractionView(MethodView):
    @swag_from("../../docs/api/roi_extraction_post.yml")
    def post(self):
        palm = request.files.get("palm_image")
        if palm:
            return send_file(
                "../../../../../Desktop/left_palm_left_rotating.jpg", "image/png"
            )
        return Response({"success": True}, status=200, mimetype="application/json")

    def get(self):
        return "extraction get"

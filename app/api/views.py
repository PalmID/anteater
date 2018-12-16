# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import current_app, request
from flask.views import MethodView


class PalmDetectionView(MethodView):
    """Detect if there is a palm in the image."""

    def post(self):
        """Create a palm detection job."""
        palm = request.files["palmimage"]
        if palm:
            current_app.logger.info(request.files)
            pass
            # TODO: 创建手掌检测异步任务，获取job_id，异步启动处理
        return "detection job id"

    def get(self, job_id):
        """Query the status of detection job by job id."""
        return "detection get"


class ROIExtractionView(MethodView):
    def post(self):
        return "extraction job id"

    def get(self, job_id):
        return "extraction get"

# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import request
from flask.views import MethodView

from app.extensions import swagger
from app.utils import JsonResponse


class PalmDetectionJobsView(MethodView):
    """Detect if there is a palm in the image."""

    @swagger.swag_from("api/palm_detection_jobs_post.yaml")
    def post(self):
        palm = request.files.get("palm_image")
        if not palm:
            # TODO: 创建手掌检测异步任务，获取job_id，异步启动处理
            return JsonResponse(msg="must provide palm image", code=400)
        return JsonResponse()


class PalmDetectionJobView(MethodView):
    @swagger.swag_from("api/palm_detection_job_get.yaml")
    def get(self, job_id):
        """Query the status of detection job by job id."""
        # TODO: 根据job_id去数据库查任务状态
        return JsonResponse()

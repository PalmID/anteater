# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import json
import time

from flask import Response, request, send_file
from flask.views import MethodView

from app.extensions import swagger


class PalmDetectionJobsView(MethodView):
    """Detect if there is a palm in the image."""

    @swagger.swag_from("api/palm_detection_jobs_post.yaml")
    def post(self):
        """Create a palm detection job."""
        # palm = request.files["palmimage"]
        # if palm:
        #     current_app.logger.info(request.files)
        #     pass
        # TODO: 创建手掌检测异步任务，获取job_id，异步启动处理
        time.sleep(5)
        return Response(json.dumps({}), status=200, mimetype="application/json")


class PalmDetectionJobView(MethodView):
    @swagger.swag_from("api/palm_detection_job_get.yaml")
    def get(self, job_id):
        """Query the status of detection job by job id."""
        return "detection get"


class RoiExtractionJobsView(MethodView):
    @swagger.swag_from("api/roi_extraction_jobs_post.yaml")
    def post(self):
        palm = request.files.get("palm_image")
        if palm:
            return Response(
                {"job_id": "123", "state": 0, "errmsg": "", "roi_image": palm},
                status=200,
                mimetype="multipart/form-data",
            )


class RoiExtractionJobView(MethodView):
    @swagger.swag_from("api/roi_extraction_job_get.yaml")
    def get(self, job_id):
        return "extraction get"


class RoiExtractionImageView(MethodView):
    @swagger.swag_from("api/roi_extraction_image_get.yaml")
    def get(self, job_id):
        return send_file(
            "../EDCC-Palmprint-Recognition/database/Tongji/ROI/session1/00001.bmp"
        )

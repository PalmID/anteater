# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import request
from flask.views import MethodView

from app.extensions import swagger
from app.utils import JsonResponse


class RoiExtractionJobsView(MethodView):
    @swagger.swag_from("api/roi_extraction_jobs_post.yaml")
    def post(self):
        palm = request.files.get("palm_image")
        if not palm:
            # TODO: 异步任务提取roi
            return JsonResponse(data={"errmsg": "Must provide palm image"}, code=400)
        return JsonResponse(data={})


class RoiExtractionJobView(MethodView):
    @swagger.swag_from("api/roi_extraction_job_get.yaml")
    def get(self, job_id):
        return JsonResponse()

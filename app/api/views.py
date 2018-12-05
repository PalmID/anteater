# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask.views import MethodView
from flask import request, current_app

class PalmDetectionView(MethodView):

    def post(self):
        palm = request.files['palm_image']
        if palm:
            current_app.logger.info(request.files)
            pass
            # TODO: 创建手掌检测异步任务，获取job_id，异步启动处理
        return 'detection job id'

    def get(self, job_id):
        return 'detection get'


class PalmExtractionView(MethodView):

    def post(self):
        return 'extraction job id'

    def get(self, job_id):
        return 'extraction get'

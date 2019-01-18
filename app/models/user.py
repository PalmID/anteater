# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import enum

import peewee as pw

from app.extensions import pwx
from app.utils import enum2choices


@enum.unique
class JobState(enum.IntEnum):
    Submitted = 0
    Processing = 1
    ProcessFail = 2
    ProcessSuccess = 3


class UserJobModelMixin(pwx.Model):
    id = pw.BigAutoField(primary_key=True)
    user_id = pw.BigIntegerField()
    src_palm_oss = pw.CharField()
    state = pw.SmallIntegerField(
        choices=enum2choices(JobState), default=JobState.Submitted
    )
    errmsg = pw.CharField(max_length=128, default="")

    @classmethod
    def pre_run(cls, palm_image):
        # TODO: 上传oss，并返回url
        return ""

    @classmethod
    def run(cls, user_id, palm_image):
        palm_oss = cls.pre_run(palm_image)
        job = cls.create(user_id=user_id, src_palm_oss=palm_oss)
        job.process()

    def process(self):
        raise NotImplementedError


class UserDetectionJob(UserJobModelMixin):
    score = pw.SmallIntegerField(default=0)  # 0-100

    class Meta:
        table_name = "user_detection_jobs"

    def process(self):
        pass


class UserExtractionJob(UserJobModelMixin):
    class Meta:
        table_name = "user_extraction_jobs"

    def process(self):
        pass

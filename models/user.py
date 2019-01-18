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


class UserJobModelMixin(object):
    id = pw.BigAutoField(primary_key=True)
    user_id = pw.BigIntegerField()
    state = pw.SmallIntegerField(
        choices=enum2choices(JobState), default=JobState.Submitted
    )
    errmsg = pw.CharField(max_length=128, default="")


class UserDetectionJob(pwx.Model, UserJobModelMixin):
    score = pw.FloatField(default=0.0)

    class Meta:
        table_name = "user_detection_jobs"


class UserExtractionJob(pwx.Model, UserJobModelMixin):
    class Meta:
        table_name = "user_extraction_jobs"

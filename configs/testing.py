# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from configs.default import *  # noqa

TESTING = True

DB_NAME = "anteater_test"
PW_DB_URL = "mysql+pool://{user}:{password}@{host}/{db_name}".format(
    host=DB_HOST, db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD  # noqa
)

CELERY_TASK_ALWAYS_EAGER = True

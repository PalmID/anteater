# flake8: noqa

from configs.default import *

TESTING = True

DB_NAME = "anteater_test"
PW_DB_URL = "mysql+pool://{user}:{password}@{host}/{db_name}".format(
    host=DB_HOST, db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD  # noqa
)

CELERY_TASK_ALWAYS_EAGER = True

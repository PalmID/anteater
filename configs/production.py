# flake8: noqa

import os

from configs.default import *

DEBUG = False

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
PW_DB_URL = "mysql+pool://{user}:{password}@{host}/{name}".format(
    host=DB_HOST, name=DB_NAME, user=DB_USER, password=DB_PASSWORD
)

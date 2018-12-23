# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import os

# logging
loglevel = os.getenv("GUNICORN_LOG_LEVEL", "warning")

# server socket
bind = "0.0.0.0:5000"

# worker processes
workers = os.getenv("GUNICORN_WORKER_NUM", 4)

# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import os

# logging
if os.environ.get("FLASK_ENV") != "production":
    accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("GUNICORN_LOG_LEVEL", "warning")

# process naming
proc_name = "anteater"

# server socket
bind = "0.0.0.0:5000"

# worker processes
workers = int(os.environ.get("GUNICORN_WORKER_NUM", 2))
# **shouldn't** call `patch_all()` by ourselves when use `gevent`
# https://github.com/benoitc/gunicorn/issues/1056#issuecomment-115409307
worker_class = "gevent"
threads = int(os.environ.get("GUNICORN_THREAD_NUM", 4))
keepalive = int(os.environ.get("GUNICORN_KEEPALIVE_TIMEOUT", 30))

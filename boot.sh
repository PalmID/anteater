#!/bin/sh
# this script is used to boot a Docker container
# source venv/bin/activate
exec gunicorn -c gunicorn.py anteater:app

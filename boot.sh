#!/bin/sh
# this script is used to boot a Docker container
source venv/bin/activate
exec gunicorn -b :5000 --access-logfile - --error-logfile - anteater:app

#!/bin/bash

# start
uwsgi --ini /usr/local/yunweipingtai01/scripts/uwsgi.ini

# stop
uwsgi --stop /usr/local/yunweipingtai01/scripts/uwsgi.pid

# collect static files
python manage.py collectstatic --noinput



#!/bin/sh

set -e

#python3 backend/manage.py migrate 
# python3 graph_maker/manage.py runserver 0.0.0.0:3000


exec "$@"

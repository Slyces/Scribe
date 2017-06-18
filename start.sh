#!/usr/bin/env bash

# Start Gunicorn processes
echo Scribes -- Starting Gunicorn.
cd Django
exec gunicorn scribes.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
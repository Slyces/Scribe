#!/usr/bin/env bash

# Start Gunicorn processes
echo Scribe -- Starting Gunicorn.
exec gunicorn scribe.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
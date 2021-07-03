#!/bin/bash
set -e

if [ "$ENV" = "development" ] ; then
    pip install -r requirements.txt
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
else
    mkdir -p /api/docker/db/logs
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --log-config docker/web/logs.ini
fi

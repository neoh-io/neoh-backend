#! /usr/bin/env bash
set -e

python /app/neoh_backend/celeryworker_pre_start.py

celery worker -A neoh_backend.worker -l info -Q main-queue -c 1
#! /usr/bin/env bash
set -e

python /app/neoh_backend/tests_pre_start.py

bash ./scripts/test-stop-fail.sh "$@"
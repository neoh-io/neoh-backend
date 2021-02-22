#! /usr/bin/env bash

# Let the DB start
python /app/neoh_backend/backend_pre_start.py

# Run migrations
alembic upgrade head
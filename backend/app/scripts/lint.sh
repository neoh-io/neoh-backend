#! /usr/bin/env bash

set -x

mypy neoh_backend
black neoh_backend --check
isort --recursive --check-only neoh_backend
flake8 --exclude=venv/,__init__.py,alembic/ 
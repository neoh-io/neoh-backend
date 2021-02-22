#! /usr/bin/env bash

set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place neoh_backend --exclude=__init__.py
black neoh_backend tests
isort --recursive --apply neoh_backend
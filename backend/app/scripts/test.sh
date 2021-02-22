#! /usr/bin/env bash

set -e
set -x

pytest --cov=neoh_backend --cov-report=term-missing tests "${@}"
#! /usr/bin/env bash

set -e
set -x


pytest -x --cov=neoh_backend --cov-report=term-missing tests "${@}"
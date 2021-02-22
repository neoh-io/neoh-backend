#! /usr/bin/env bash

# Exit in case of error
set -e

cp $ENV_GITLAB .env
TAG=${TAG?Variable not set} \
sh ./scripts/build.sh
docker-compose -f docker-compose.yml push
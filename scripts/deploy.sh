#! /usr/bin/env bash

# Exit in case of error
set -e

cp $ENV_GITLAB .env

DOMAIN=${DOMAIN?Variable not set} \
TAG=${TAG?Variable not set} \
STACK_NAME=${STACK_NAME?Variable not set} \
docker-compose -f docker-compose.yml config > docker-stack.yml

docker-auto-labels docker-stack.yml

docker stack deploy -c docker-stack.yml --with-registry-auth "${STACK_NAME?Variable not set}"
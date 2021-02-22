#! /usr/bin/env bash

# Exit in case of error
set -e

cp env-example .env

docker-compose -f docker-compose.yml config > docker-stack.yml
docker-compose -f docker-stack.yml build
docker-compose -f docker-stack.yml down -v --remove-orphans # Remove possibly broken previous stacks left hanging
docker-compose -f docker-stack.yml up -d
docker-compose -f docker-stack.yml exec -T backend bash /app/scripts/lint.sh "$@"
docker-compose -f docker-stack.yml down -v --remove-orphans
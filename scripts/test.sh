#! /usr/bin/env bash

# Exit in case of error
set -e

cp env-example .env

docker-compose up -d
docker-compose exec -T backend bash /app/tests-start.sh "$@"
docker-compose down -v --remove-orphans
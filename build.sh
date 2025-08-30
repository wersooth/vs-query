#!/usr/bin/sh
COMMIT=$(git rev-parse --short HEAD)
BRANCH=$(git rev-parse --abbrev-ref HEAD)

docker build --build-arg=COMMIT=$COMMIT --build-arg=BRANCH=$BRANCH -t docker.local/docker/vs-query:dev .
docker push docker.local/docker/vs-query:dev

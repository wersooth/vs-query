#!/bin/sh

DOCKER_TAG=docker.local/docker/vs-query
if [[ ! -f tag ]]; then
	echo "0" > tag
fi
TAG=$(cat tag)
NEXTTAG=$(($TAG+1))
echo "building next tag: $NEXTTAG"



COMMIT=$(git rev-parse --short HEAD)
BRANCH=$(git rev-parse --abbrev-ref HEAD)

docker build --build-arg=COMMIT=$COMMIT --build-arg=BRANCH=$BRANCH -t $DOCKER_TAG:$NEXTTAG -t $DOCKER_TAG:latest .
docker push $DOCKER_TAG:$NEXTTAG
docker push $DOCKER_TAG:latest
echo $NEXTTAG > tag

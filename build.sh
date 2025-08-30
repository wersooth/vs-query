#!/usr/bin/sh

if [[ ! -f tag ]]; then
	echo "0" > tag
fi
TAG=$(cat tag)
NEXTTAG=$(($TAG+1))
echo "building next tag: $NEXTTAG"



COMMIT=$(git rev-parse --short HEAD)
BRANCH=$(git rev-parse --abbrev-ref HEAD)

docker build --build-arg=COMMIT=$COMMIT --build-arg=BRANCH=$BRANCH -t docker.local/docker/vs-query:$NEXTTAG -t docker.local/docker/vs-query:latest .
docker push docker.local/docker/vs-query:$NEXTTAG
docker push docker.local/docker/vs-query:latest

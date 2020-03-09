#!/bin/bash
set -e

docker login -u $DOCKER_USERID -p $DOCKER_PASS docker.io
docker build -t travis_test .
docker tag travis_test sumeetp1991/travis_test:version1
docker push sumeetp1991/travis_test:version1 

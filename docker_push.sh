#!/bin/bash
set -e

docker build -t travis_test .
docker login -u "sumeetp1991" -p "Clueless@123" docker.io
docker tag travis_test sumeetp1991/travis_test:version1
docker push sumeetp1991/travis_test:version1 


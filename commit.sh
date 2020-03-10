#!/bin/bash

set -e 
git add $1
git commit -m "test"
git push origin master
git tag $2
git push origin $2

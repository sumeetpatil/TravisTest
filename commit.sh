#!/bin/bash

set -e 
git add $1
git commit -m "test"
git push origin master

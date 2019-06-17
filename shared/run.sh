#!/bin/sh
rm -rf /home/dist
cd /home
make build
cd dist
spark-submit --py-files jobs.zip,libs.zip main.py
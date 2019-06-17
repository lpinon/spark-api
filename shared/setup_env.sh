#!/bin/sh
apt-get -q update
apt-get -q install -y build-essential
apt-get -q install -y zip
pip install -r /home/requirements.txt -t /home/libs --upgrade
sh /home/run.sh
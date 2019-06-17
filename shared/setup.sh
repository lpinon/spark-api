#!/bin/sh
sh /home/setup_env.sh &
bin/spark-class org.apache.spark.deploy.master.Master -h master
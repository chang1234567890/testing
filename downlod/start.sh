#! /bin/bash

ps -ef|grep python |awk '{print $2}'|xargs kill -9
basedir=`cd $(dirname $0); pwd -P`
cd $basedir
nohup python -u dow_file.py &

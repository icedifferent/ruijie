#!/bin/bash
tasks=`ps -ef|grep ruijie.py|wc -l`
if [ $tasks -lt 2 ]; then
	echo "exec"
	cd /home/ice/Desktop/repositories\ /ruijie && nohup python3 ./ruijie.py &
fi



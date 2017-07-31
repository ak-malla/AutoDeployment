#!/bin/bash

#
# This Shell Script helps to remotely update/run all the list of the Selenium IP's with latest builds and restarting Applications
# Featuring:
# 1. Updating of the AutoIt Library versions
# 2. Restarting all of the Applications
#
#
#
#echo $PATH

# The Local WBXTF Server need to be Started, If not the scripts fails
LOCAL_SERVER_STATUS=`wbxtfclient localhost wbxtf.util.GetVersion`
echo $LOCAL_SERVER_STATUS 
if($LOCAL_SERVER_STATUS -ne "hr:-100 Cannot connect the server"); then

	#Copying of the AutoIt Library
	python /home/ak/Documents/webex-systemtest-performance-pylib/deploy/deployAutoIT.py

	echo "Copied and Zip extracted all the files remotely"
	echo "Sleeping for 10"
	sleep 10
	# Starting the AutoIt Application
	wbxtfclient 10.22.160.88 process.Run\(java -jar C:\\AutoItWebexClient\\AutoItWebexClient31.0\\webexclient-1.0.jar\)

	echo "Sleeping for 2"
	sleep 2
	#Starting the Node and Hub
	#Hub
	echo "Starting the Hub"
	wbxtfclient 10.22.160.88 process.Run\(C:\\Users\\admin\\selenium\\start-hub.bat\)

	echo "Sleeping for 2"
	sleep 2
	#Node 
	echo "Starting the Node"
	wbxtfclient 10.22.160.88 process.Run\(C:\\Users\\admin\\selenium\\start-node.bat\)

	echo "Sleeping for 2"
	sleep 2
	#Starting the restclient jar
	echo "Starting the Restclient jar"
	wbxtfclient 10.22.160.88 process.Run\(java -jar C:\\AutoItWebexClientT32.4\\restclient-1.0.jar\)
else
	# Failure Case, The Script won't work if the local demon server is not working
	echo "Script Failed to Run, Local WBXTF Server Not Running "$LOCAL_SERVER_STATUS
fi

__author__ = "AK"

from wbxtf import WBXTF
import time

#
# This Python Script helps to remotely update/run all the list of the Selenium IP's with latest builds
# and restarting Applications
# Featuring:
# 1. Updating of the AutoIt Library versions
# 2. Restarting all of the Applications
#
#

print '~ AK ~'

cmd = "calc"

vmList = ["10.22.160.85"]
for vm in vmList:
    WBXTF.WBXTFExecCmd(vm,cmd)
    #Copying of the AutoIt Library
    #python /home/ak/Documents/webex-systemtest-performance-pylib/deploy/deployAutoIT.py
    print "Copied and Zip extracted all the files remotely"
    print "Sleeping for 10"
    time.sleep(10)
    # Starting the AutoIt Application
    #wbxtfclient 10.22.160.88 process.Run\(java -jar C:\\AutoItWebexClient\\AutoItWebexClient31.0\\webexclient-1.0.jar\)
    WBXTF.WBXTFExecCmd(vm,"java -jar C:\\AutoItWebexClient\\AutoItWebexClient31.0\\webexclient-1.0.jar")
    print "Sleeping for 2"
    time.sleep(2)
    #Starting the Node and Hub
    #Hub
    print "Starting the Hub"
    #wbxtfclient 10.22.160.88 process.Run\(C:\\Users\\admin\\selenium\\start-hub.bat\)
    print "Sleeping for 2"
    time.sleep(2)
    #Node
    print "Starting the Node"
    #wbxtfclient 10.22.160.88 process.Run\(C:\\Users\\admin\\selenium\\start-node.bat\)
    echo "Sleeping for 2"
    time.sleep(2)
    #Starting the restclient jar
    print "Starting the Restclient jar"
    #wbxtfclient 10.22.160.88 process.Run\(java -jar C:\\AutoItWebexClientT32.4\\restclient-1.0.jar\)


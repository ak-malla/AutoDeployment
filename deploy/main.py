__author__ = "AK"

from wbxtf import WBXTF
from AutoUtil import getIPs
#from subprocess import call
#import time


#
# This Python Script helps to remotely update/run all the list of the Selenium IP's with latest builds
# and restarting Applications
# Featuring:
# 1. Updating of the AutoIt Library versions
# 2. Restarting all of the Applications
#
#

print '~ AK ~'

def copyUpdatedAutoIt(resourceIP, type):
    vmList = getIPs(resourceIP, type)
    for vm in vmList:
        #WBXTF.WBXTFExecCmd(vm,cmd)
        #Copying of the AutoIt Library
        #python /home/ak/Documents/webex-systemtest-performance-pylib/deploy/deployAutoIT.py
        #print "Copied and Zip extracted all the files remotely"
        #print "Sleeping for 10"
        #time.sleep(10)
        # Starting the AutoIt Application
        #res = WBXTF.WBXTFExecCmdWithDir(vm,"java -jar webexclient-1.0.jar","",r"C:\AutoItWebexClient\AutoItWebexClient 31.0")
        #print "%s : %s " % (vm, res)
        #print "Sleeping for 2"
        #time.sleep(2)
        #Starting the Node and Hub
        #Hub
        #print "Starting the Hub"
        #res = WBXTF.WBXTFExecCmdWithDir(vm,"start-hub.bat","",r"C:\Users\admin\selenium")
        #print "%s : %s " % (vm, res)
        print vm
        #print "Sleeping for 2"
        #time.sleep(2)
        #Node
        #print "Starting the Node"
        #res = WBXTF.WBXTFExecCmdWithDir(vm,"start-node.bat","",r"C:\Users\admin\selenium")
        #print "%s : %s " % (vm, res)
        #print "Sleeping for 2"
        #time.sleep(2)
        #Starting the restclient jar
        #print "Starting the Restclient jar"
        #res = WBXTF.WBXTFExecCmdWithDir(vm,"java -jar restclient-1.0.jar","","C:\AutoItWebexClient T32.4")
        #print "%s : %s " % (vm, res)

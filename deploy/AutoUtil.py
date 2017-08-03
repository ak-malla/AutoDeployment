import json
import urllib2

from wbxtf import WBXTF
from wbxtf.WBXTFActionPool import *
from wbxtf.WBXTFLogex import *

__author__ = "AK"

'''
 This Python Script helps to remotely update/run all the list of the Selenium IP's with latest builds
 and restarting Applications
 Featuring:
 1. Updating of the AutoIt Library versions
 2. Restarting all of the Applications
 3. Monitoring all the Java Application to the idle count value 4
 4. Monitoring all the Selenium and End Point IP's
 5. Checking and Updating the Windows

'''


# The Below Method takes 2 Parameters one Pool IP and Other is Selenium or EndPoint
def getIPs(IP, type):
    print 'Getting the ' + type + ' IPs from the ' + IP + ' resource pool'
    # Below are the 4 Different URIs to get the List of Seleniums and EndPoint IP's from .39 and .76 pool each
    URL = '';
    if (type.upper() == 'SEL'):
        URL = 'http://' + IP + ':9000/edptManage/getSelSipInfo';
    elif (type.upper() == "EP"):
        URL = 'http://' + IP + ':9000/edptManage/getEndpointInfo';
    else:
        return None
    outLst = []
    response = urllib2.urlopen(URL)
    json_array = json.load(response)
    for jObject in json_array:
        outLst.append(jObject['ip'])
    return outLst


def executeCmdNotify(result):
    nTotalTask = len(result)
    nSuccess = 0
    nFailed = 0
    nRunning = nTotalTask
    for key in result:
        if result[key]["finish"] == True:
            if result[key]["result"] == True:
                nSuccess += 1
                nRunning -= 1
            else:
                nFailed += 1
                nRunning -= 1

    outputString = "Total:%d Success:%d Failed:%d Running:%s"
    loginfo = outputString % (nTotalTask, nSuccess, nFailed, nRunning)
    WBXTFLogInfo(loginfo)


# Support Multithreading
def executeCmdByThread(machineList, function, *args):
    actionPool = WBXTFActionPool(8)
    actionPool.setthreadFinishedNotifyFunc(executeCmdNotify)
    for machine in machineList:
        actionPool.putAction(None, function, machine, *args)
    actionPool.waitComplete()


# Ping Test all the IPs and return IP list not reachable
def pingTestMonitor(IP, type):
    outList = getIPs(IP, type)
    returnList = []
    for vm in outList:
        if os.system("ping -c 1 "+vm) == 0:
            print "Host "+vm+" appears to be up"
        else:
            returnList.append(vm)
    return returnList

# This Method helps to copy the latest AutoIt Library files into the remote windows system
def copyZipPackageAndUnZip(vm, *args):
    fileName = args[0]
    target = "C:\AutoItWebexClient\\" + fileName
    unzipFolder = r"C:\AutoItWebexClient"
    cmd = r"if exist "+target+" echo file exists"
    res = WBXTF.WBXTFExecCmdReturn(vm, cmd)
    print res
    result = res["result"]["Result"]["fileList"][0]["data"]
    if (result.lower() == ""):
        print "Copying on %s ...." % vm
        cpRet = WBXTF.WBXTFCopyFileToFile("local", fileName, vm, target)
        if cpRet:
            print "copy zip success on %s. will unzip it" % vm
            cmd = r"7z.exe x -aoa -r %s  -o%s * " % (target, unzipFolder)
            print WBXTF.WBXTFExecCmdWithDir(vm, cmd, "", r"C:\Program Files\7-Zip")
        else:
            print "copy failed on %s" % vm


# This Method will help to copy the VB Script which helps to update the windows remotely
def copyWindows(vm):
    cmd = r"if exist C:\AutoItWebexClient\WUA_DownloadInstall.vbs echo file exists"
    res = WBXTF.WBXTFExecCmdReturn(vm, cmd)
    print res
    result = res["result"]["Result"]["fileList"][0]["data"]
    print result
    if (result.lower() == ""):
        print 'Files Does not exists, Copying to remote VM ' + vm
        WBXTF.WBXTFCopyFileToFile("local", "WUA_DownloadInstall.vbs", vm,
                                  "C:\AutoItWebexClient\\WUA_DownloadInstall.vbs")

def updateWindows(vm):
    copyWindows(vm)
    res = WBXTF.WBXTFExecCmdWithDir(vm, "cscript WUA_DownloadInstall.vbs", "", r"C:\AutoItWebexClient")
    print "%s : %s " % (vm, res)

# Get Count of all the Java Process currently running
def getJavaProcessCount(vm):
    cmd = "tasklist | find /C \"java.exe\""
    res = WBXTF.WBXTFExecCmdReturn(vm, cmd)
    return res["result"]["Result"]["fileList"][0]["data"]


# This method will help in kill and restart all the java application
def startApplications(vm):
    # Killing all the java process if any active
    res = WBXTF.WBXTFExecCmdReturn(vm, r"taskkill /F /IM java.exe")
    print res
    time.sleep(2)
    # Starting the AutoIt Application
    res = WBXTF.WBXTFExecCmdWithDir(vm, "java -jar webexclient-1.0.jar", "",
                                    r"C:\AutoItWebexClient\AutoItWebexClient 31.0")
    print "%s : %s " % (vm, res)
    print "Sleeping for 2"
    time.sleep(2)
    # Starting the Node and Hub
    # Hub
    print "Starting the Hub"
    res = WBXTF.WBXTFExecCmdWithDir(vm, "start-hub.bat", "", r"C:\Users\admin\selenium")
    print "%s : %s " % (vm, res)
    print vm
    print "Sleeping for 2"
    time.sleep(2)
    # Node
    print "Starting the Node"
    res = WBXTF.WBXTFExecCmdWithDir(vm, "start-node.bat", "", r"C:\Users\admin\selenium")
    print "%s : %s " % (vm, res)
    print "Sleeping for 2"
    time.sleep(2)
    # Starting the restclient jar
    print "Starting the Restclient jar"
    res = WBXTF.WBXTFExecCmdWithDir(vm, "java -jar restclient-1.0.jar", "", "C:\AutoItWebexClient T32.4")
    print "%s : %s " % (vm, res)


# This method will run as cron Job monitor the IP, if there is any drop in Application count, and restart if needed
def monitorJavaProcessCount(vm):
    count = getJavaProcessCount(vm)
    if (count < "4"):
        print "Java Process Count miss match for VM " + vm + " ,Restarting all Java Applications"
        startApplications(vm)
    else:
        print "All the process are in idle count " + count + " state ,VM " + vm

'''
if __name__ == '__main__':
    executeCmdByThread(["10.22.160.85","10.22.160.88"],copyZipPackageAndUnZip, "AutoItWebexClient31.0.zip")
    time.sleep(8)
    executeCmdByThread(["10.22.160.85","10.22.160.88"],monitorJavaProcessCount)
    time.sleep(5)
    for vm in pingTestMonitor("10.22.136.39", "SEL"):
        print "\n\n\n\n IP not reachable ..."
        print vm
    time.sleep(5)
    executeCmdByThread(["10.22.160.85","10.22.160.88"],updateWindows)
'''

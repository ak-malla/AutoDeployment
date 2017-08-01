from wbxtf import WBXTF
import urllib2
import json

__author__ = "AK"


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


# This Method helps to copy the latest AutoIt Library files into the remote windows system
def copyZipPackageAndUnZip(source, fileName, vm):
    target = "C:\AutoItWebexClient\\" + fileName
    source += fileName
    unzipFolder = r"C:\AutoItWebexClient"
    print "Copying on %s ...." % vm
    cpRet = WBXTF.WBXTFCopyFileToFile("local", source, vm, target)
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
        WBXTF.WBXTFCopyFileToFile("local", "/home/ak/PythonScript/AutoDeployment/deploy/WUA_DownloadInstall.vbs", vm,
                                  "C:\AutoItWebexClient\\WUA_DownloadInstall.vbs")


def startApplications(vm):
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

def checkApplicationCount(vm):

if __name__ == '__main__':
    # vmObject = getIPs("10.22.136.39", "SEL")
    # for vm in vmObject:
    # print vm
    # copyZipPackageAndUnZip("/home/ak/Downloads/", "AutoItWebexClient31.0.zip" , "10.22.160.85")
    copyWindows("10.22.160.85")

from wbxtf import WBXTF
from wbxtf.WBXTFActionPool import *


def copyThreadFunc(sourcePath,Machine,targetPath):
    ret = WBXTF.WBXTFCopyFileToFile("local", sourcePath, Machine, targetPath)
    if ret == False:
        print "vm:%s copy file failed" % Machine
    else:
        print "vm:%s copy file success" % Machine

def copyZipPackageAndUnZip(vmList):
    sourcePath = r"/home/ak/Downloads/AutoItWebexClient31.0.zip"
    targetPath = r"C:\AutoItWebexClient\AutoItWebexClient31.0.zip"
    #sourceZipFilePath = r"C:\PF_Tools\wbxtfLoadTestNode.zip"
    #targetPath = r"C:\PF_Tools\wbxtfLoadTestNode.zip"
    unzipFolder = r"C:\AutoItWebexClient"
    #for vm in vmList:
    print "Copying on %s ...." % vmList
    cpRet = WBXTF.WBXTFCopyFileToFile("local", sourcePath, vmList, targetPath)
    if cpRet:
        print "copy zip success on %s. will unzip it" % vmList
        cmd = r"7z.exe x -aoa -r %s  -o%s * " % (targetPath, unzipFolder)
        print WBXTF.WBXTFExecCmdWithDir(vmList, cmd, "", r"C:\Program Files\7-Zip")
    else:
        print "copy failed on %s" % vmList


def copyFile(vmList):
    #targetPath = r"/home/ak/Desktop/AutoItWebexClient31.0.zip"
    targetPath = r"C:\Users\admin\Desktop\TESTING\AutoItWebexClient31.0.zip"
    sourcePath = r"/home/ak/Downloads/AutoItWebexClient31.0.zip"

    actionPool = WBXTFActionPool(1)
    for vm in vmList:
        #actionPool.putAction(None,copyThreadFunc,sourcePath,vm,targetPath)
        actionPool.putAction(None,copyZipPackageAndUnZip,vm)
        #WBXTF.WBXTFRun(vm,r"c:\tmp\7z.exe /S", "", 1)
    actionPool.waitComplete()

def killSplitCam(vmList):
    for vm in vmList:
        WBXTF.WBXTFExecCmd(vm,"taskkill /F /IM SplitCam.exe")


if __name__ == '__main__':
    vmList = []
    param_testVMListFile = r"C:\Git\webex-systemtest-performance-pylib\deploy\ClientPool4Test.txt"
    #fn = open(param_testVMListFile)
    #while 1:
    #    machineIP = fn.readline()
    #    if not machineIP:
    #        break
    #    machineIP = machineIP.strip()
    #    vmList.append(machineIP)

    vmList = ["10.22.160.88"]
    copyFile(vmList)
    # killSplitCam(vmList)


    # vmList = []
    # for i in range(0,22):
    #     vmList.append("10.1.9.%s" % i)
    # print vmList
    # copyZipPackageAndUnZip(vmList)







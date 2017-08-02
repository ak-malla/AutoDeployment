__author__ = "AK"

from AutoUtil import *
import time

'''
    Main Class supporting the AutoDeployment and Monitoring
'''
print '~ AK ~'

if __name__ == '__main__':
    executeCmdByThread(["10.22.160.85", "10.22.160.88"], copyZipPackageAndUnZip, "AutoItWebexClient31.0.zip")
    time.sleep(8)
    executeCmdByThread(["10.22.160.85", "10.22.160.88"], monitorJavaProcessCount)
    time.sleep(5)
    for vm in pingTestMonitor("10.22.136.39", "SEL"):
        print "\n\n\n\n IP not reachable ..."
        print vm
    time.sleep(5)
    executeCmdByThread(["10.22.160.85", "10.22.160.88"], updateWindows)

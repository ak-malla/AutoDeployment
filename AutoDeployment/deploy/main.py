__author__ = "AK"

from AutoUtil import *
import time

'''
    Main Class supporting the AutoDeployment and Monitoring
'''
print '~ AK ~'

if __name__ == '__main__':
    print 'Copying the AutoItWebexClient Libraries to remote systems'
    executeCmdByThread(["10.22.160.85", "10.22.160.88"], copyZipPackageAndUnZip, "AutoItWebexClient31.0.zip")
    time.sleep(8)
    print 'Monitoring the Java Application'
    executeCmdByThread(["10.22.160.85", "10.22.160.88"], monitorJavaProcessCount)
    time.sleep(10)
    print 'Monitoring Java Application again'
    executeCmdByThread(["10.22.160.85", "10.22.160.88"], monitorJavaProcessCount)
    time.sleep(10)
    print 'Ping Test the Selenium IP'
    for vm in pingTestMonitor("10.22.136.39", "SEL"):
        print "\n\n\n\n IP not reachable ..."
        print vm
    time.sleep(10)
    print 'Windowsn update ....'
    executeCmdByThread(["10.22.160.85", "10.22.160.88"], updateWindows)

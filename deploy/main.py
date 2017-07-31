__author__ = "AK"

from wbxtf import WBXTF

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
testVMList = ["10.1.8.11"]
WBXTF.WBXTFExecCmd(testVMList,cmd)
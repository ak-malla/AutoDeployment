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

vmList = ["10.22.160.85"]
for vm in vmList:
	WBXTF.WBXTFExecCmdReturn(vm,cmd)

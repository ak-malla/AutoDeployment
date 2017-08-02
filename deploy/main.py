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

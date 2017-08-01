
from wbxtf import WBXTF
import urllib2
import json

__author__ = "AK"

# The Below Method takes 2 Parameters one Pool IP and Other is Selenium or EndPoint
def getIPs(IP, type):
	print 'Getting the '+type+' IPs from the '+IP+' resource pool'
	#Below are the 4 Different URIs to get the List of Seleniums and EndPoint IP's from .39 and .76 pool each
	URL = '';
	if (type.upper() == 'SEL'):
		URL = 'http://'+IP+':9000/edptManage/getSelSipInfo';
	elif (type.upper() == "EP"):
		URL = 'http://'+IP+':9000/edptManage/getEndpointInfo';
	else:
		return None
	outLst = []
	response = urllib2.urlopen(URL)
	json_array = json.load(response)
	for jObject in json_array:
		outLst.append(jObject['ip'])
	return outLst

def copyZipPackageAndUnZip(source, fileName, vm):
	target = "C:\AutoItWebexClient\\"+fileName
    unzipFolder = r"C:\AutoItWebexClient"
    print "Copying on %s ...." % vm
    cpRet = WBXTF.WBXTFCopyFileToFile("local", source, vm, target)
    if cpRet:
        print "copy zip success on %s. will unzip it" % vm
        cmd = r"7z.exe x -aoa -r %s  -o%s * " % (targetPath, unzipFolder)
        print WBXTF.WBXTFExecCmdWithDir(vm, cmd, "", r"C:\Program Files\7-Zip")
    else:
        print "copy failed on %s" % vm


if __name__ == '__main__':
	vmObject = getIPs("10.22.136.39", "SEL")
	for vm in vmObject:
		print vm
	copyZipPackageAndUnZip("")
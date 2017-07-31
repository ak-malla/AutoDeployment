__author__ = 'AK'

import json
import urllib2
import sys

print "Getting the Selenium IPs from the 39 resource pool"

print sys.argv[1]

#Below are the 4 Different URIs to get the List of Seleniums and EndPoint IP's from .39 and .76 pool each
URL = '';
if (sys.argv[1] == '39' and sys.argv[2].upper() == 'SEL'):
	URL = 'http://10.22.136.39:9000/edptManage/getSelSipInfo';
elif (sys.argv[1] == '76' and sys.argv[2].upper() == "SEL"):
	URL = 'http://10.22.136.76:9000/edptManage/getSelSipInfo';
elif (sys.argv[1] == '39' and sys.argv[2].upper() == "EP"):
	URL = 'http://10.22.136.39:9000/edptManage/getEndpointInfo';
elif (sys.argv[1] == '76' and sys.argv[2].upper() == "EP"):
	URL = 'http://10.22.136.76:9000/edptManage/getEndpointInfo';

response = urllib2.urlopen(URL)
json_array = json.load(response)
#print json_array
for jObject in json_array:
	print jObject['ip']
#print '\n'

#! /usr/bin/env python
#coding=utf-8
import sys
import os
import time
import simplejson as json



#ipadd = sys.argv[1]
try:
        
        ipadd = sys.argv[1]
        data=os.popen("curl -s http://%s:60010/jmx > /var/www/html/resource/snmp_queries/masterdata.txt" % ipadd).readlines()
        f = file('/var/www/html/resource/snmp_queries/masterdata.txt')
        source=f.read().strip()
        ddata=json.JSONDecoder().decode(source)
        target=ddata['beans']
        f.close()
except Exception,e:
        print "Execution timeout!" 
        sys.exit(0)
    

str_nameAsString=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt |grep nameAsString|sed -e 's/\"//g'|awk '{print $3}'|sed -e 's/\.,//g'").readlines()
str_readRequestsCount=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep readRequestsCount|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_requestsCount=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep requestsCount|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_rootIndexSizeKB=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep rootIndexSizeKB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_storefileIndexSizeMB=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep storefileIndexSizeMB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_storefileSizeMB=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep storefileSizeMB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_storefiles=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep storefiles|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_stores=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep stores|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_totalCompactingKVs=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep totalCompactingKVs|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_totalStaticBloomSizeKB=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep totalStaticBloomSizeKB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_totalStaticIndexSizeKB=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep totalStaticIndexSizeKB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_writeRequestsCount=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep writeRequestsCount|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_currentCompactedKVs=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep currentCompactedKVs|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
str_memStoreSizeMB=os.popen("cat /var/www/html/resource/snmp_queries/masterdata.txt|grep memStoreSizeMB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()

inti=0
while inti < len(str_nameAsString):
    nameAsString = str_nameAsString[inti].strip()
    readRequestsCount = str_readRequestsCount[inti].strip()
    requestsCount = str_requestsCount[inti].strip()
    rootIndexSizeKB = str_rootIndexSizeKB[inti].strip()
    storefileIndexSizeMB = str_storefileIndexSizeMB[inti].strip()
    storefileSizeMB = str_storefileSizeMB[inti].strip()
    storefiles = str_storefiles[inti].strip()
    stores = str_stores[inti].strip()
    totalCompactingKVs = str_totalCompactingKVs[inti].strip()
    totalStaticBloomSizeKB = str_totalStaticBloomSizeKB[inti].strip()
    totalStaticIndexSizeKB = str_totalStaticIndexSizeKB[inti].strip()
    writeRequestsCount = str_writeRequestsCount[inti].strip()
    currentCompactedKVs = str_currentCompactedKVs[inti].strip()
    memStoreSizeMB = str_memStoreSizeMB[inti].strip()
    
    
    mydata = open('/var/www/html/resource/snmp_queries/test.txt','a+')
    
    mydata.writelines("nameAsString")
    mydata.writelines(": ")
    mydata.writelines(nameAsString)
    mydata.writelines("  ")
    
    mydata.writelines("readRequestsCount")
    mydata.writelines(":")
    mydata.writelines(readRequestsCount)
    mydata.writelines("  ")
    
    mydata.writelines("requestsCount")
    mydata.writelines(":")
    mydata.writelines(requestsCount)
    mydata.writelines("  ")
    
    mydata.writelines("rootIndexSizeKB")
    mydata.writelines(":")
    mydata.writelines(rootIndexSizeKB)
    mydata.writelines("  ")

    mydata.writelines("storefileIndexSizeMB")
    mydata.writelines(":")
    mydata.writelines(storefileIndexSizeMB)
    mydata.writelines("  ")

    mydata.writelines("storefileSizeMB")
    mydata.writelines(":")
    mydata.writelines(storefileSizeMB)
    mydata.writelines("  ")

    mydata.writelines("storefiles")
    mydata.writelines(":")
    mydata.writelines(storefiles)
    mydata.writelines("  ")

    mydata.writelines("stores")
    mydata.writelines(":")
    mydata.writelines(stores)
    mydata.writelines("  ")

    mydata.writelines("totalCompactingKVs")
    mydata.writelines(":")
    mydata.writelines(totalCompactingKVs)
    mydata.writelines("  ")

    mydata.writelines("totalStaticBloomSizeKB")
    mydata.writelines(":")
    mydata.writelines(totalStaticBloomSizeKB)
    mydata.writelines("  ")

    mydata.writelines("totalStaticIndexSizeKB")
    mydata.writelines(":")
    mydata.writelines(totalStaticIndexSizeKB)
    mydata.writelines("  ")

    mydata.writelines("writeRequestsCount")
    mydata.writelines(":")
    mydata.writelines(writeRequestsCount)
    mydata.writelines("  ")

    mydata.writelines("currentCompactedKVs")
    mydata.writelines(":")
    mydata.writelines(currentCompactedKVs)
    mydata.writelines("  ")

    mydata.writelines("memStoreSizeMB")
    mydata.writelines(":")
    mydata.writelines(memStoreSizeMB)
    mydata.writelines('\r\n')

    inti = inti + 1
    
try:
    
    if (sys.argv[2] == "index"):
        cacti_index=os.popen("cat /var/www/html/resource/snmp_queries/test.txt|awk '{print $2}'").readlines()
        for line in cacti_index:
            print line.strip()
    
    elif (sys.argv[2] == "query" and sys.argv[3] == "index"):
        cacti_index=os.popen("cat /var/www/html/resource/snmp_queries/test.txt|awk '{print $1 $2}'").readlines()
        for line in cacti_index:
            print line.strip()
except Exception,e: 
    print Exception,":",e 
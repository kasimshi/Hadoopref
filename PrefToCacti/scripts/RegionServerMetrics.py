#by kasim&Mango 20131010
#qq:13218778

import sys
import os
import time
import simplejson as json



#ipadd = sys.argv[1]
if len(sys.argv) != 2:
    print "Please enter the ip" 
    sys.exit(0)
else:
    try:
        
        ipadd = sys.argv[1]
        data=os.popen("curl -s http://%s:60030/jmx > ./regiondata.txt" % ipadd).readlines()
        f = file('regiondata.txt')
        source=f.read().strip()
        ddata=json.JSONDecoder().decode(source)
        target=ddata['beans']
        f.close()
    except:
        print "Execution timeout!" 
        sys.exit(0)
    
int_ThreadCount = target[8]["ThreadCount"]
int_totalStaticIndexSize = target[15]["totalStaticIndexSizeKB"]
float_blockCacheFree = float(target[15]["blockCacheFree"])/1024
int_memstoreSizeMB= target[15]["memstoreSizeMB"]
int_blockCacheCount = target[15]["blockCacheCount"]
int_blockCacheHitRatio = target[15]["blockCacheHitRatio"]
int_blockCacheHitCachingRatio = target[15]["blockCacheHitCachingRatio"]
int_blockCacheHitCount = target[15]["blockCacheHitCount"]
int_hdfsBlocksLocalityIndex = target[15]["hdfsBlocksLocalityIndex"]
int_writeRequestsCount = target[15]["writeRequestsCount"]
int_compactionTimeMinTime = target[15]["compactionTimeMinTime"]
int_compactionTimeMaxTime = target[15]["compactionTimeMaxTime"]
float_blockCacheSize = float(target[15]["blockCacheSize"])/1024
int_readRequestsCount = target[15]["readRequestsCount"]
int_rootIndexSize = target[15]["rootIndexSizeKB"]
int_blockCacheMissCount = target[15]["blockCacheMissCount"]
int_blockCacheHitRatioPastNPeriods = target[15]["blockCacheHitRatioPastNPeriods"]
int_blockCacheHitCachingRatioPastNPeriods = target[15]["blockCacheHitCachingRatioPastNPeriods"]
int_storefiles = target[15]["storefiles"]
int_blockCacheEvictedCount = target[15]["blockCacheEvictedCount"]
int_stores = target[15]["stores"]
int_requests = round(target[15]["requests"])


print "ThreadCount:%d" % int_ThreadCount,
print "totalStaticIndexSizeKB:%d" % int_totalStaticIndexSize,
print "blockCacheFree:%f" % float_blockCacheFree,
print "memstoreSizeMB:%d" % int_memstoreSizeMB,
print "blockCacheCount:%d" % int_blockCacheCount,
print "blockCacheHitRatio:%d" % int_blockCacheHitRatio,
print "blockCacheHitCachingRatio:%d" % int_blockCacheHitCachingRatio,
print "blockCacheHitCount:%d" % int_blockCacheHitCount,
print "hdfsBlocksLocalityIndex:%d" % int_hdfsBlocksLocalityIndex,
print "writeRequestsCount:%d" % int_writeRequestsCount,
print "compactionTimeMinTime:%d" % int_compactionTimeMinTime,
print "compactionTimeMaxTime:%d" % int_compactionTimeMaxTime,
print "blockCacheSize:%f" % float_blockCacheSize,
print "readRequestsCount:%d" % int_readRequestsCount,
print "rootIndexSizeKB:%d" % int_rootIndexSize,
print "blockCacheMissCount:%d" % int_blockCacheMissCount,
print "blockCacheHitRatioPastNPeriods:%d" % int_blockCacheHitRatioPastNPeriods,
print "blockCacheHitCachingRatioPastNPeriods:%d" % int_blockCacheHitCachingRatioPastNPeriods,
print "storefiles:%d" % int_storefiles,
print "blockCacheEvictedCount:%d" % int_blockCacheEvictedCount,
print "stores:%d" % int_stores,
print "requests:%d" % int_requests

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
        data=os.popen("curl -s http://%s:50075/jmx > ./datanode.txt" % ipadd).readlines()
        f = file('datanode.txt')
        source=f.read().strip()
        ddata=json.JSONDecoder().decode(source)
        target=ddata['beans']
        f.close()
    except:
        print "Execution timeout!" 
        sys.exit(0)
    
float_G_written = float(target[5]["bytes_written"])/(1024*1024*1024)
float_G_read = float(target[5]["bytes_read"])/(1024*1024*1024)
    
int_blocks_written = target[5]["blocks_written"]
int_blocks_read = target[5]["blocks_read"]
    
int_blocks_replicated = target[5]["blocks_replicated"]
int_bblocks_removed = target[5]["blocks_removed"]

int_blocks_verified = target[5]["blocks_verified"]
int_block_verification_failures = target[5]["block_verification_failures"]
    
int_blocks_get_local_pathinfo = target[5]["blocks_get_local_pathinfo"]
    
int_reads_from_local_client = target[5]["reads_from_local_client"]
int_reads_from_remote_client = target[5]["reads_from_remote_client"]
    
int_writes_from_local_client = target[5]["writes_from_local_client"]
int_writes_from_remote_client = target[5]["writes_from_remote_client"]
    
int_readBlockOp_num_ops = target[5]["readBlockOp_num_ops"]
float_readBlockOp_avg_time = target[5]["readBlockOp_avg_time"]
    
int_writeBlockOp_num_ops = target[5]["writeBlockOp_num_ops"]
float_writeBlockOp_avg_time = target[5]["writeBlockOp_avg_time"]
    
int_ThreadCount = target[15]["ThreadCount"]


float_memNonHeapUsedM = target[18]["memNonHeapUsedM"]
float_memNonHeapCommittedM = target[18]["memNonHeapCommittedM"]

float_memHeapUsedM = target[18]["memHeapUsedM"]
float_memHeapCommittedM = target[18]["memHeapCommittedM"]

int_gcCount = target[18]["gcCount"]
int_gcTimeMillis = target[18]["gcTimeMillis"]

int_threadsNew = target[18]["threadsNew"]
int_threadsRunnable = target[18]["threadsRunnable"]

int_threadsBlocked = target[18]["threadsBlocked"]
int_threadsWaiting = target[18]["threadsWaiting"]

int_threadsTimedWaiting = target[18]["threadsTimedWaiting"]
int_threadsTerminated = target[18]["threadsTerminated"]

print "G_written:%f" % float_G_written,
print "G_read:%f" % float_G_read,
print "blocks_written:%d" % int_blocks_written,
print "blocks_read:%d" % int_blocks_read,
print "blocks_replicated:%d" % int_blocks_replicated,
print "blocks_removed:%d" % int_bblocks_removed,
print "blocks_verified:%d" % int_blocks_verified,
print "block_verification_failures:%d" % int_block_verification_failures,
print "blocks_get_local_pathinfo:%d" % int_blocks_get_local_pathinfo,
print "reads_from_local_client:%d" % int_reads_from_local_client,
print "reads_from_remote_client:%d" % int_reads_from_remote_client,
print "writes_from_local_client:%d" % int_writes_from_local_client,
print "writes_from_remote_client:%d" % int_writes_from_remote_client,
print "readBlockOp_num_ops:%d" % int_readBlockOp_num_ops,
print "readBlockOp_avg_time:%f" % float_readBlockOp_avg_time,
print "writeBlockOp_num_ops:%d" % int_writeBlockOp_num_ops,
print "writeBlockOp_avg_time:%f" % float_writeBlockOp_avg_time,
print "ThreadCount:%d" % int_ThreadCount,

print "memNonHeapUsedM:%f" % float_memNonHeapUsedM,
print "memNonHeapCommittedM:%f" % float_memNonHeapCommittedM,
print "memHeapUsedM:%f" % float_memHeapUsedM,
print "memHeapCommittedM:%f" % float_memHeapCommittedM,
print "gcCount:%d" % int_gcCount,
print "gcTimeMillis:%d" % int_gcTimeMillis,
print "threadsNew:%d" % int_threadsNew,
print "threadsRunnable:%d" % int_threadsRunnable,
print "threadsBlocked:%d" % int_threadsBlocked,
print "threadsWaiting:%d" % int_threadsWaiting,
print "threadsTimedWaiting:%d" % int_threadsTimedWaiting,
print "threadsTerminated:%d" % int_threadsTerminated
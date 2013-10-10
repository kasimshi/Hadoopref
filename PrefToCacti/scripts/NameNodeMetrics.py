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
        data=os.popen("curl -s http://%s:50070/jmx > ./namedata.txt" % ipadd).readlines()
        f = file('namedata.txt')
        source=f.read().strip()
        ddata=json.JSONDecoder().decode(source)
        target=ddata['beans']
        f.close()
    except:
        print "Execution timeout!" 
        sys.exit(0)
    
int_FilesTotal = target[2]["FilesTotal"]
int_BlocksTotal = target[2]["BlocksTotal"]
int_CapacityTotalGB = target[2]["CapacityTotalGB"]
int_CapacityUsedGB = target[2]["CapacityUsedGB"]
float_NonDfsUsedSpaceGB = target[20]["NonDfsUsedSpace"]
int_NonDfsUsedSpaceGB = float_NonDfsUsedSpaceGB/(1024*1024*1024)
int_CapacityRemainingGB = target[2]["CapacityRemainingGB"]
int_TotalLoadB = target[2]["TotalLoad"]
int_CorruptBlocks = target[2]["CorruptBlocks"]
int_ExcessBlocks = target[2]["ExcessBlocks"]
int_MissingBlocks = target[2]["MissingBlocks"]   
int_UnderReplicatedBlocks = target[2]["UnderReplicatedBlocks"]      
pre_DFS_PercentUsed = 100 - target[20]["PercentRemaining"]
list_livenodes = target[20]["LiveNodes"]
json_livenodes = json.loads(list_livenodes)
int_LiveNodes = len(json_livenodes)
list_DeadNodes = target[20]["DeadNodes"]
json_DeadNodes = json.loads(list_DeadNodes)
int_DeadNodes = len(json_DeadNodes)


int_delete_num_ops = target[5]["delete_num_ops"]
float_delete_avg_time = target[5]["delete_avg_time"]
int_mkdirs_num_ops = target[5]["mkdirs_num_ops"]
float_Rmkdirs_avg_time = target[5]["mkdirs_avg_time"]
int_create_num_ops = target[5]["create_num_ops"]
float_create_avg_time = target[5]["create_avg_time"]
int_addBlock_num_ops = target[5]["addBlock_num_ops"]
float_addBlock_avg_time = target[5]["addBlock_avg_time"]
int_blockReceived_num_ops = target[5]["blockReceived_num_ops"]
float_blockReceived_avg_time = target[5]["blockReceived_avg_time"]
int_getBlockLocations_num_ops = target[5]["getBlockLocations_num_ops"]
float_getBlockLocations_avg_time = target[5]["getBlockLocations_avg_time"]
int_fsync_num_ops = target[5]["fsync_num_ops"]
float_fsync_avg_time = target[5]["fsync_avg_time"]
int_RpcQueueTime_num_ops = target[7]["RpcQueueTime_num_ops"]
float_RpcQueueTime_avg_time = target[7]["RpcQueueTime_avg_time"]
int_RpcProcessingTime_num_ops = target[7]["RpcProcessingTime_num_ops"]
float_RpcProcessingTime_avg_time = target[7]["RpcProcessingTime_avg_time"]

float_memNonHeapUsedM = target[8]["memNonHeapUsedM"]
float_memNonHeapCommittedM = target[8]["memNonHeapCommittedM"]
float_memHeapUsedM = target[8]["memHeapUsedM"]
float_memHeapCommittedM = target[8]["memHeapCommittedM"]
int_gcCount = target[8]["gcCount"]
int_gcTimeMillis = target[8]["gcTimeMillis"]
int_threadsNew = target[8]["threadsNew"]
int_threadsRunnable = target[8]["threadsRunnable"]
int_threadsBlocked = target[8]["threadsBlocked"]
int_threadsWaiting = target[8]["threadsWaiting"]
int_threadsTimedWaiting = target[8]["threadsTimedWaiting"]
int_threadsTerminated = target[8]["threadsTerminated"]

print "FilesTotal:%d" % int_FilesTotal,
print "BlocksTotal:%d" % int_BlocksTotal,
print "CapacityTotalGB:%d" % int_CapacityTotalGB,
print "CapacityUsedGB:%d" % int_CapacityUsedGB,
print "NonDfsUsedSpaceGB:%d" % int_NonDfsUsedSpaceGB,
print "CapacityRemainingGB:%d" % int_CapacityRemainingGB,
print "TotalLoad:%d" % int_TotalLoadB,
print "CorruptBlocks:%d" % int_CorruptBlocks,
print "ExcessBlocks:%d" % int_ExcessBlocks,
print "MissingBlocks:%d" % int_MissingBlocks,
print "UnderReplicatedBlocks:%d" % int_UnderReplicatedBlocks,
print "PercentRemaining:%d" % pre_DFS_PercentUsed,
print "LiveNodes:%d" % int_LiveNodes,
print "DeadNodes:%d" % int_DeadNodes,
print "gcCount:%d" % int_gcCount,
print "gcTimeMillis:%d" % int_gcTimeMillis,
print "memNonHeapUsedM:%f" % float_memNonHeapUsedM,
print "memNonHeapCommittedM:%f" % float_memNonHeapCommittedM,
print "memHeapUsedM:%f" % float_memHeapUsedM,
print "memHeapCommittedM:%f" % float_memHeapCommittedM,
print "threadsNew:%d" % int_threadsNew,
print "threadsRunnable:%d" % int_threadsRunnable,
print "threadsBlocked:%d" % int_threadsBlocked,
print "threadsWaiting:%d" % int_threadsWaiting,
print "threadsTimedWaiting:%d" % int_threadsTimedWaiting,
print "threadsTerminated:%d" % int_threadsTerminated,
print "delete_num_ops:%d" % int_delete_num_ops,
print "delete_avg_time:%f" % float_delete_avg_time,
print "mkdirs_num_ops:%d" % int_mkdirs_num_ops,
print "mkdirs_avg_time:%f" % float_Rmkdirs_avg_time,
print "create_num_ops:%d" % int_create_num_ops,
print "create_avg_time:%f" % float_create_avg_time,
print "addBlock_num_ops:%d" % int_addBlock_num_ops,
print "addBlock_avg_time:%f" % float_addBlock_avg_time,
print "blockReceived_num_ops:%d" % int_blockReceived_num_ops,
print "blockReceived_avg_time:%f" % float_blockReceived_avg_time,
print "getBlockLocations_num_ops:%d" % int_getBlockLocations_num_ops,
print "getBlockLocations_avg_time:%f" % float_getBlockLocations_avg_time,
print "fsync_num_ops:%d" % int_fsync_num_ops,
print "fsync_avg_time:%f" % float_fsync_avg_time,
print "RpcProcessingTime_avg_time:%f" % float_RpcProcessingTime_avg_time,
print "RpcQueueTime_num_ops:%d" % int_RpcQueueTime_num_ops,
print "RpcQueueTime_avg_time:%f" % float_RpcQueueTime_avg_time,
print "RpcProcessingTime_num_ops:%d" % int_RpcProcessingTime_num_ops
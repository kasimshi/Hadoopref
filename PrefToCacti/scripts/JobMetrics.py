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
        data=os.popen("curl -s http://%s:50030/jmx > ./jobdata.txt" % ipadd).readlines()
        f = file('jobdata.txt')
        source=f.read().strip()
        ddata=json.JSONDecoder().decode(source)
        target=ddata['beans']
        f.close()
    except:
        print "Execution timeout!" 
        sys.exit(0)
    

int_maps_launched = target[12]["maps_launched"]
int_maps_completed = target[12]["maps_completed"]
int_maps_failed = target[12]["maps_failed"]
int_reduces_launched = target[12]["reduces_launched"]
int_reduces_completed = target[12]["reduces_completed"]
int_reduces_failed = target[12]["reduces_failed"]
int_jobs_submitted = target[12]["jobs_submitted"]
int_jobs_completed = target[12]["jobs_completed"]
int_waiting_maps = target[12]["waiting_maps"]
int_waiting_reduces = target[12]["waiting_reduces"]
int_jobs_failed = target[12]["jobs_failed"]
int_jobs_killed = target[12]["jobs_killed"]
int_ThreadCount = target[16]["ThreadCount"]
str_SummaryJson = target[5]["SummaryJson"]
json_SummaryJson = json.loads(str_SummaryJson)
int_nodes = json_SummaryJson["nodes"]
int_alive = json_SummaryJson["alive"]
int_deadnodes = int_nodes - int_alive
int_reduce_slots = json_SummaryJson["slots"]["reduce_slots"]
int_reduce_slots_used = json_SummaryJson["slots"]["reduce_slots_used"]
per_reduce_slots_used = float(int_reduce_slots_used)*100/int_reduce_slots
int_map_slots = json_SummaryJson["slots"]["map_slots"]
int_map_slots_used = json_SummaryJson["slots"]["map_slots_used"]
per_map_slots_used = float(int_map_slots_used)*100/int_map_slots

int_RpcQueueTime_num_ops = target[3]["RpcQueueTime_num_ops"]
float_RpcQueueTime_avg_time = target[3]["RpcQueueTime_avg_time"]
int_RpcProcessingTime_num_ops = target[3]["RpcProcessingTime_num_ops"]
float_RpcProcessingTime_avg_time = target[3]["RpcProcessingTime_avg_time"]
int_getSystemDir_num_ops = target[8]["getSystemDir_num_ops"]
float_getSystemDir_avg_time = target[8]["getSystemDir_avg_time"]
int_getStagingAreaDir_num_ops = target[8]["getStagingAreaDir_num_ops"]
float_getStagingAreaDir_avg_time = target[8]["getStagingAreaDir_avg_time"]
int_getNewJobId_num_ops = target[8]["getNewJobId_num_ops"]
float_getNewJobId_avg_time = target[8]["getNewJobId_avg_time"]
int_submitJob_num_ops = target[8]["submitJob_num_ops"]
float_submitJob_avg_time = target[8]["submitJob_avg_time"]
int_getTaskCompletionEvents_num_ops = target[8]["getTaskCompletionEvents_num_ops"]
float_getTaskCompletionEvents_avg_time = target[8]["getTaskCompletionEvents_avg_time"]
int_getJobCounters_num_ops = target[8]["getJobCounters_num_ops"]
float_getJobCounters_avg_time = target[8]["getJobCounters_avg_time"]

float_memNonHeapUsedM = target[17]["memNonHeapUsedM"]
float_memNonHeapCommittedM = target[17]["memNonHeapCommittedM"]
float_memHeapUsedM = target[17]["memHeapUsedM"]
float_memHeapCommittedM = target[17]["memHeapCommittedM"]
int_gcCount = target[17]["gcCount"]
int_gcTimeMillis = target[17]["gcTimeMillis"]
int_threadsNew = target[17]["threadsNew"]
int_threadsRunnable = target[17]["threadsRunnable"]
int_threadsBlocked = target[17]["threadsBlocked"]
int_threadsWaiting = target[17]["threadsWaiting"]
int_threadsTimedWaiting = target[17]["threadsTimedWaiting"]
int_threadsTerminated = target[17]["threadsTerminated"]


print "ThreadCount:%d" % int_ThreadCount,
print "maps_launched:%d" % int_maps_launched,
print "maps_completed:%d" % int_maps_completed,
print "maps_failed:%d" % int_maps_failed,
print "reduces_launched:%d" % int_reduces_launched,
print "reduces_completed:%d" % int_reduces_completed,
print "reduces_failed:%d" % int_reduces_failed,
print "jobs_submitted:%d" % int_jobs_submitted,
print "jobs_completed:%d" % int_jobs_completed,
print "waiting_maps:%d" % int_waiting_maps,
print "waiting_reduces:%d" % int_waiting_maps,
print "jobs_failed:%d" % int_jobs_failed,
print "jobs_killed:%d" % int_jobs_killed,
print "alivenode:%d" % int_alive,
print "reduce_slots_used:%d" % per_reduce_slots_used,
print "map_slots_used:%d" % per_map_slots_used,

print "getSystemDir_num_ops:%d" % int_getSystemDir_num_ops,
print "getSystemDir_avg_time:%f" % float_getSystemDir_avg_time,
print "getStagingAreaDir_num_ops:%d" % int_getStagingAreaDir_num_ops,
print "getStagingAreaDir_avg_time:%f" % float_getStagingAreaDir_avg_time,
print "getNewJobId_num_ops:%d" % int_getNewJobId_num_ops,
print "getNewJobId_avg_time:%f" % float_getNewJobId_avg_time,
print "submitJob_num_ops:%d" % int_submitJob_num_ops,
print "submitJob_avg_time:%f" % float_submitJob_avg_time,
print "getTaskCompletionEvents_num_ops:%d" % int_getTaskCompletionEvents_num_ops,
print "getTaskCompletionEvents_avg_time:%f" % float_getTaskCompletionEvents_avg_time,
print "getJobCounters_num_ops:%d" % int_getJobCounters_num_ops,
print "getJobCounters_avg_time:%f" % float_getJobCounters_avg_time,
print "RpcQueueTime_num_ops:%d" % int_RpcQueueTime_num_ops,
print "RpcQueueTime_avg_time:%f" % float_RpcQueueTime_avg_time,
print "RpcProcessingTime_num_ops:%d" % int_RpcProcessingTime_num_ops,
print "RpcProcessingTime_avg_time:%f" % float_RpcProcessingTime_avg_time,

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
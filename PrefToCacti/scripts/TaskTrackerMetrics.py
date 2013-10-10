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
        data=os.popen("curl -s http://%s:50060/jmx > ./taskdata.txt" % ipadd).readlines()
        f = file('taskdata.txt')
        source=f.read().strip()
        ddata=json.JSONDecoder().decode(source)
        target=ddata['beans']
        f.close()
    except:
        print "Execution timeout!" 
        sys.exit(0)
    
int_RpcQueueTime_num_ops = target[7]["RpcQueueTime_num_ops"]
float_RpcQueueTime_avg_time = target[7]["RpcQueueTime_avg_time"]
int_RpcProcessingTime_num_ops = target[7]["RpcProcessingTime_num_ops"]
float_RpcProcessingTime_avg_time = target[7]["RpcProcessingTime_avg_time"]
int_getTask_num_ops = target[8]["getTask_num_ops"]
float_getTask_avg_time = target[8]["getTask_avg_time"]
int_getMapCompletionEvents_num_ops = target[8]["getMapCompletionEvents_num_ops"]
float_getMapCompletionEvents_avg_time = target[8]["getMapCompletionEvents_avg_time"]
int_commitPending_num_ops = target[8]["commitPending_num_ops"]
float_commitPending_avg_time = target[8]["commitPending_avg_time"]
int_ThreadCount = target[15]["ThreadCount"]
int_tasks_completed = target[17]["tasks_completed"]
int_tasks_failed_timeout = target[17]["tasks_failed_timeout"]
int_tasks_failed_ping = target[17]["tasks_failed_ping"]

float_memNonHeapUsedM = target[19]["memNonHeapUsedM"]
float_memNonHeapCommittedM = target[19]["memNonHeapCommittedM"]
float_memHeapUsedM = target[19]["memHeapUsedM"]
float_memHeapCommittedM = target[19]["memHeapCommittedM"]
int_gcCount = target[19]["gcCount"]
int_gcTimeMillis = target[19]["gcTimeMillis"]
int_threadsNew = target[19]["threadsNew"]
int_threadsRunnable = target[19]["threadsRunnable"]
int_threadsBlocked = target[19]["threadsBlocked"]
int_threadsWaiting = target[19]["threadsWaiting"]
int_threadsTimedWaiting = target[19]["threadsTimedWaiting"]
int_threadsTerminated = target[19]["threadsTerminated"]



print "RpcQueueTime_num_ops:%d" % int_RpcQueueTime_num_ops,
print "RpcQueueTime_avg_time:%f" % float_RpcQueueTime_avg_time,
print "RpcProcessingTime_num_ops:%d" % int_RpcProcessingTime_num_ops,
print "RpcProcessingTime_avg_time:%f" % float_RpcProcessingTime_avg_time,
print "getTask_num_ops:%d" % int_getTask_num_ops,
print "getTask_avg_time:%f" % float_getTask_avg_time,
print "getMapCompletionEvents_num_ops:%d" % int_getMapCompletionEvents_num_ops,
print "getMapCompletionEvents_avg_time:%f" % float_getMapCompletionEvents_avg_time,
print "commitPending_num_ops:%d" % int_commitPending_num_ops,
print "commitPending_avg_time:%f" % float_commitPending_avg_time,
print "ThreadCount:%d" % int_ThreadCount,
print "tasks_completed:%d" % int_tasks_completed,
print "tasks_failed_timeout:%d" % int_tasks_failed_timeout,
print "tasks_failed_ping:%d" % int_tasks_failed_ping,

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

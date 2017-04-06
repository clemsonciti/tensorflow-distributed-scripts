import tensorflow as tf
import sys
import numpy as np

pbs_nodefile = sys.argv[1]
index = int(sys.argv[2])

tasks = []
task_count = 0
for pbs_node in open(pbs_nodefile, 'r'):
    tasks.append("{}:{}".format(pbs_node.strip(), 2222+(task_count%2)))
    task_count += 1 

cluster = tf.train.ClusterSpec({"worker": tasks})

server = tf.train.Server(cluster, job_name="worker", task_index=index)
if index == 0:
    server.start()
server.join()

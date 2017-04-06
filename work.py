import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float64, 10000000)

with tf.device("/job:worker/task:0/gpu:1"):
    first_batch = tf.slice(x, [0], [5000000])
    mean1 = tf.reduce_mean(first_batch)

with tf.device("/job:worker/task:1/gpu:1"):
    second_batch = tf.slice(x, [5000000], [-1])
    mean2 = tf.reduce_mean(second_batch)
    mean = (mean1 + mean2) / 2

with tf.Session("grpc://localhost:2222", config=tf.ConfigProto(log_device_placement=True)) as sess:
    print("Starting....")
    result = sess.run(mean, feed_dict={x: np.random.random(10000000)})
    print(result)

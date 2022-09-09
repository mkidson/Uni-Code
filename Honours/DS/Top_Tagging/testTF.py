#!/usr/bin/python3
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
tf.print(hello)
tf.print('Using TensorFlow version: ' + tf.__version__)
with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)
tf.print(c)
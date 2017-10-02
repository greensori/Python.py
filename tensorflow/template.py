# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import cv2
from PIL import ImageGrab
import serial
import os


def feed_dict():
    a = tf.placeholder(tf.float32, shape = [3])
    b = tf.constant([5, 5, 5], tf.float32)
    print (a)
    print (b)
    c = a + b
    print (c)
    with tf.Session() as sess:
        print (sess.run(c, {a: [1, 2, 3]}))
    a = tf.add(2, 5)
    b = tf.multiply(a, 3)
    with tf.Session() as sess:
        replace_dict = { a: 15}
        print (sess.run(b, feed_dict = replace_dict))
        
def simple_tf():
    a = tf.constant(2)
    b = tf.constant(3)
    print (a)
    print (b)
    x = tf.add(a, b)
    with tf.Session() as sess:
     	writer = tf.summary.FileWriter('./graphs', sess.graph) 
    print(sess.run(x))
    writer.close() # close the writer when you’re done using it
    a = tf.constant([2, 2], name='a')
    b = tf.constant([[0, 1], [2, 3]], name='b')
    x = tf.multiply(a, b, name='dot_product')
    with tf.Session() as sess:
        print(sess.run(x))


if __name__ == '__main__':
    simple_tf()


#tf.zeros(shape, dtype = tf.float32, anme=None)

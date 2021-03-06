#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: yejun
@file: test7.py
@time: 15/12/16
"""

import redis

class Task(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(host='localhost', db = 5)
        self.queue = 'task:prodcons:queue'

    def listen_task(self):
        while True:
            task = self.rcon.blpop(self.queue, 0)[1]
            print "Task get", task

if __name__ == '__main__':
    print 'listen task queue'
    Task().listen_task()
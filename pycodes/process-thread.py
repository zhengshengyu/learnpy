#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 进程(Process): == 任务: 打开一个浏览器就是启动一个浏览器进程, 打开两个记事本就启动了两个记事本进程 
## 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响

# 线程(Thread): 在一个进程(Process)内部，同时干的多件事，同时运行的多个“子任务”, 比如Word，它可以同时进行打字、拼写检查、打印等事情
## 多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改

## 写的所有的Python程序，都是执行单任务的进程，也就是只有一个线程
## 执行多个任务怎么办？
    # 多进程模式；
    # 多线程模式；
    # 多进程+多线程模式。

## 多进程（multiprocessing）
import os
# print 'Process (%s) start...' % os.getpid()
# pid = os.fork() # fork()调用一次，返回两次, Windows没有fork调用
# print 'return back'
# if pid==0:
#     print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

# multiprocessing跨平台版本的多进程模块
## Process类来代表一个进程对象，并启动一个子进程
from multiprocessing import Process
### 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Process(target=run_proc, args=('test',))
#     print 'Process will start.'
#     p.start()
#     p.join()
#     print 'Process end.'

# pool启动大量的子进程
from multiprocessing import Pool
import time, random
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'

# 进程间通信：Queue、Pipes等多种方式来交换数据
from multiprocessing import Process, Queue
# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()


# 多线程模块thread和threading
import threading
# 新线程执行的代码:
def loop():
    print 'loop thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'loop thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'loop thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name

# Lock: WHY? HOW?
# 假定这是你的银行存款:
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        change_it(n)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance # 每次输出结果不一致

balance = 0
lock = threading.Lock() # 创建一个锁
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire() # 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release() # 一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance # 每次结果一致

# ThreadLocal
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name # 每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。 
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
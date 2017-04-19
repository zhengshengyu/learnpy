#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 进程(Process): == 任务: 打开一个浏览器就是启动一个浏览器进程, 打开两个记事本就启动了两个记事本进程 
# 线程(Thread): 在一个进程(Process)内部，同时干的多件事，同时运行的多个“子任务”, 比如Word，它可以同时进行打字、拼写检查、打印等事情
## 写的所有的Python程序，都是执行单任务的进程，也就是只有一个线程
## 执行多个任务怎么办？
    # 多进程模式；
    # 多线程模式；
    # 多进程+多线程模式。

## 多进程（multiprocessing）
import os
print 'Process (%s) start...' % os.getpid()
pid = os.fork() # fork()调用一次，返回两次
print 'return back'
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

from multiprocessing import Process
# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',)) #Process类来代表一个进程对象
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'

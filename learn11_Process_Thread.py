#多进程
"""
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
而子进程只需要调用getppid()就可以拿到父进程的ID。

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
"""
"""
import os
print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('i am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('i (%s) just created a child process (%s).' % (os.getpid(), pid))
"""
#由于Windows没有fork调用，上面的代码在Windows上无法运行。
#由于Mac系统是基于BSD（Unix的一种）内核，
#所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！


"""
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args = ('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
"""
#在IDE中直接运行，看不到子进程的运行结果，
#这是因为multiprocessing模块在交互模式是不支持的，
#在 cmd 里头输入 python xxx.py 来运行起来，就可以看到子进程的执行了。
"""
输出结果：
Parent process 10480.
Child process will start.
Run child process test (10268)...
Child process end.

"""


#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
"""
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(1)       #睡1秒
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocess done.')
"""
#代码解读：
#对Pool对象调用join()方法会等待所有子进程执行完毕，
#调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
#这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。
#这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
#p = Pool(5)
#就可以同时跑5个进程

"""
在命令行下运行
输出结果：
Parent process 11084.
Waiting for all subprocesses done...
Run task 0 (10880)...
Run task 1 (10792)...
Run task 2 (11160)...
Run task 3 (10328)...
Task 0 runs 1.00 seconds.
Run task 4 (10880)...
Task 1 runs 1.00 seconds.
Task 2 runs 1.00 seconds.
Task 3 runs 1.00 seconds.
Task 4 runs 1.00 seconds.
All subprocess done.

"""






#多线程
#Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
#threading是高级模块，对_thread进行了封装。
#绝大多数情况下，我们只需要使用threading这个高级模块。
import time, threading

#新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
#由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
#Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
#主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
#名字仅仅在打印时用来显示，完全没有其他意义，
#如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

"""
输出结果：
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
"""
print('\n')



#Lock

#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
#互不影响，而多线程中，所有变量都由所有线程共享，
#所以，任何一个变量都可以被任何一个线程修改，
#因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
import time, threading
balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    # 先存后取，结果应该为0:

def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
## 最终balance不一定为0
"""
t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：

初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

结果 balance = -8


"""
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        #先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
## 最终balance一定为0

#当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，
#然后继续执行代码，其他线程就继续等待直到获得锁为止。

#获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
#所以我们用try...finally来确保锁一定会被释放
print('\n')





#多核CPU
"""
用Python代码启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。

但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

"""






























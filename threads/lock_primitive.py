"""This is the most basic synchronization primitive"""

import threading as th
import time

lock = th.Lock()

string = ''


def write_hello(locked=True):
    global string  # use globals only for education purpose
    hello_lst = list('hello')
    if locked:
        lock.acquire()
    for ch in hello_lst:
        string += ch
        print(ch)
        time.sleep(0.5)
    if locked:
        lock.release()


def write_world(locked=True):
    global string
    world_lst = list(' world')
    if locked:
        lock.acquire()
    for ch in world_lst:
        string += ch
        print(ch)
        time.sleep(0.5)
    if locked:
        lock.release()

if __name__ == '__main__':
    """Let's do no_lock first, we see, that variable string got messed"""
    thread_pool = [th.Thread(target=target, kwargs={'locked': False}) for target in (write_hello, write_world)]
    for thread in thread_pool:
        thread.start()
    for thread in thread_pool:
        thread.join()
    print(string)

# if __name__ == '__main__':
#     """No with lock everything came to order"""
#     thread_pool = [th.Thread(target=target, kwargs={'locked': True}) for target in (write_hello, write_world)]
#     for thread in thread_pool:
#         thread.start()
#     for thread in thread_pool:
#         thread.join()
#     print(string)

"""
Join method is used to stop the execution of the thread we call this method from(usually main thred) until the thread we call this method to is finished.
"""

import threading as th
import time


def countdown(n, sleep_time, name):
    for i in range(n):
        print(n-i-1, name)
        time.sleep(sleep_time)

t = th.Thread(target=countdown, args=(10, 1, 'left'))


def run_two_threads_no_join(daemon=False):
    """
    This function doesn't have join() method, so it doesn't block
    the main thread and it executes along with left thread.
    You can play with sleep_time argument to see how it influences
    execution order. Guess why?
    """
    t.daemon = daemon
    t.start()
    countdown(10, 0.5, 'main')


def run_two_threads_join(daemon=False):
    """
    This function has join() method, so it blocks
    the main thread and waits for left thread to finish.
    """
    t.daemon = daemon
    t.start()
    t.join()
    countdown(10, 0.5, 'main')


# threads run in rotation
if __name__ == '__main__':
    run_two_threads_no_join()


# # first executes left, than main
# if __name__ == '__main__':
#     run_two_threads_join()
#
#
# # when using daemon=True, left process is stopped, when main is done
# if __name__ == '__main__':
#     run_two_threads_no_join(daemon=True)
#
#
# # but using daemon=True with join finishes both threads, because it blocks main until left is finished
# if __name__ == '__main__':
#     run_two_threads_join(daemon=True)

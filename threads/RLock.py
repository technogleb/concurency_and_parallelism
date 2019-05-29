"""RLock is the same that lock with the exception, that RLock can be acquired more then once without freezing."""

import threading as th

lock = th.Lock()
rlock = th.RLock()


def lock_twice(locker=None):
    a = 1
    locker.acquire()
    a += 1
    locker.acquire()
    a += 2
    locker.release()


if __name__ == '__main__':
    lock_twice(rlock)
    lock_twice(lock)  # freezes forever

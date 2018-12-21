"""
Python doesn't have any built-in method to force stop thread execution.
So, one good way is to create the following class
"""
import time
import threading as th


class Job:
    def __init__(self, n, sleep_time, name):
        self._is_alive = True  # our flag
        self.n = n
        self.sleep_time = sleep_time
        self.name = name

    def kill(self):
        """Calling this method would kill the thread"""
        self._is_alive = False

    def task(self):
        while self._is_alive:
            for i in range(self.n):
                print(self.n-i-1, self.name)
                time.sleep(self.sleep_time)

    def __call__(self):
        self.task()


if __name__ == '__main__':
    target = Job(n=10, sleep_time=1, name='left')
    target.kill()
    t = th.Thread(target=target)
    t.start()

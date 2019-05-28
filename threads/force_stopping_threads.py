"""
Python doesn't have any built-in method to force stop thread execution.
So, one good way is to create the following class
"""
import time
import threading as th


class Job:
    """This is old example of how this wouldn't work"""
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


class JobKillable(th.Thread):
    """This is the right way to create stoppable threads"""
    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n = n
        self._is_alive = True

    def kill(self):
        """Calling this method would kill the thread"""
        self._is_alive = False

    def run(self):
        i = 0
        while self._is_alive:
            print(self.n - i - 1, 'left')
            time.sleep(1)
            i -= 1


if __name__ == '__main__':
    # wouldn't work
    target = Job(n=10, sleep_time=1, name='left')
    t = th.Thread(target=target)
    t.start()
    target.kill()

    # work
    t = JobKillable(n=100)
    t.start()
    time.sleep(4)
    t.kill()

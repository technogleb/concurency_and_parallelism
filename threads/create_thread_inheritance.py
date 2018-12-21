"""
Another way to create thread - worse then native, because of no code reuse.
"""

import time
import threading as th


class CountdownThread(th.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.n - i - 1, 'left')
            time.sleep(1)

t = CountdownThread(3)

t.start()

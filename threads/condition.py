"""Condition is best explained on producer-consumer pattern"""

import threading as th
import time
import random


class Producer(th.Thread):
    def __init__(self, condition, data):
        super().__init__()
        self.condition = condition
        self.data = data
        self.name = 'Producer'

    def run(self):
        while True:
            self.condition.acquire()
            obj = random.randint(1, 10)
            self.data.append(obj)
            self.condition.notify()
            self.condition.release()


class Consumer(th.Thread):
    def __init__(self, condition, data):
        super().__init__()
        self.condition = condition
        self.data = data
        self.name = 'Consumer'

    def run(self):
        while True:
            self.condition.acquire()
            while True:
                pass

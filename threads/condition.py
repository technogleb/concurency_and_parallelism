"""Condition is best explained on producer-consumer pattern"""

import time
import threading as th
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
            print(f'Producer created resource {obj}')
            self.condition.notifyAll()
            self.condition.release()
            time.sleep(1)


class Consumer(th.Thread):
    def __init__(self, condition, data):
        super().__init__()
        self.condition = condition
        self.data = data
        self.name = 'Consumer'

    def run(self):
        while True:
            self.condition.acquire()
            print('Consumer is waiting for producer to create resources')
            self.condition.wait()
            while self.data:
                res = self.data.pop()
                print(f'Consumer processed resource - {res}')
            self.condition.release()


if __name__ == "__main__":
    condition = th.Condition()
    data = []
    producer = Producer(condition, data=data)
    consumer = Consumer(condition, data=data)

    consumer.start()
    producer.start()

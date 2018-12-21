"""This is the most natural way of creating thread in python."""

import time
import threading as th


def countdown(n):
    for i in range(n):
        print(n-i-1, 'left')
        time.sleep(1)


t = th.Thread(target=countdown, args=(3, ))

t.start()
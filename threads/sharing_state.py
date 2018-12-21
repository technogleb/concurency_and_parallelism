"""
If we need to pass the state into the thread and don't want to use args keyword argument,
just create the class, keep any state you want in it, then define your run method inside
__call__ method, and pass an instance of the class as target when creating Thread object.
"""

import threading as th


class Target:
    def __init__(self, state):
        self.state = state

    def __call__(self):
        self.run()

    def run(self):
        """Our function, that uses state"""
        print('Here is our shared state: {}'.format(self.state))


target = Target('I am the state')

t = th.Thread(target=target, args=())

t.start()
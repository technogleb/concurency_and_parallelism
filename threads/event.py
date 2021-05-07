"""Example, showing the use of event primitive"""

import time
import threading as th

e = th.Event()

nulevki = ['1b', '13', '5b', '23e']


def do_matan(nulevki):
    for nulevka in nulevki:
        print(f"Solved problem {nulevka}")
        time.sleep(0.5)


def do_english(hours):
    for i in range(hours):
        print("London is the capital of Great Britain")
        time.sleep(0.5)


def wait(e):
    print("Waiting student starts waiting for matan to come")
    e.wait()
    print("Doing matan")
    do_matan(nulevki)


def do_not_wait(e, timeout):
    while True:
        print('Non blocking starts waiting for an event')
        is_set = e.wait(timeout)
        if is_set:
            print("Do matan")
            do_matan(nulevki)
            break
        else:
            print("Doing some other staff")
            do_english(5)


if __name__ == "__main__":
    e = th.Event()
    virgin_stud = th.Thread(target=wait, args=(e,))
    chad_abramovets = th.Thread(target=do_not_wait, args=(e, 1))
    virgin_stud.start()
    chad_abramovets.start()
    print("Matan prepod is preparing tasks")
    time.sleep(5)
    e.set()
    print("Matan tasks are ready!")

from time import sleep

def executer(fn, interval):
    while 1:
        fn()
        sleep(interval)
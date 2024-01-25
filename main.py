from time import sleep
from app import app

def executer(fn, interval):
    while 1:
        fn()
        sleep(interval)

executer(app, 3)
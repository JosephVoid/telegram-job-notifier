import os
from time import sleep
from dotenv import load_dotenv
from app import djinni, upwork

load_dotenv()


def executer(fns, interval):
    while 1:
        for fn in fns:
            fn()
        sleep(interval)


executer([upwork], int(os.environ["MINS"]) * 60)

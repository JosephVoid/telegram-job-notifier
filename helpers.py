import os
import requests

def getURLs ():
    urls = dict()
    urls.setdefault('NoKey', 'NoValue')
    with open('.config', 'r') as f:
        for line in f.readlines():
            key = line.split(" ; ")[0]
            value = line.split(" ; ")[1]
            urls[key] = value
    return urls

def getNotifiedId () -> list[str]:
    notified = []
    with open('notified_jobs.txt', 'r') as f:
        for _id in f.readlines():
            notified.append(_id.rstrip('\n'))
    return notified

def setNotifiedId (_id):
    with open('notified_jobs.txt', 'a') as f:
        f.writelines(_id+'\n')
    return True

def check_bot ():
    response = requests.get("https://api.telegram.org/bot"+os.environ['TOKEN']+"/getMe")
    if (response.status_code == 200):
        return True
    else:
        return False

def notify (text):
    response = requests.get("https://api.telegram.org/bot"+os.environ['TOKEN']+"/sendMessage", 
                            params={
                                "chat_id": os.environ['CHAT'],
                                "text": text
                            })
    if (response.status_code == 200):
        return True
    else:
        return False
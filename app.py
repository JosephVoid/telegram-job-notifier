import time
import requests
import feedparser
from djinni_parser import Job, parser as dj_parser
from helpers import getNotifiedId, getURLs, notify, setNotifiedId
from dotenv import load_dotenv

def djinni ():
    urls = getURLs()
    try:
        resp = requests.get(
            str(urls.get("DJINNI")) , 
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            })

        if (resp.status_code == 200) :
            djinni_jobs = dj_parser(resp.content.decode())
            for job in djinni_jobs:
                if (job.id not in getNotifiedId() and notify(job.title+'\n'+job.link)):
                    print(time.ctime(time.time())+" : "+job.id)
                    setNotifiedId(job.id)
                    time.sleep(1)
        else :
            print("Request Error")
    except:
        print("Network Error: Request")

def upwork ():
    feed = feedparser.parse(getURLs().get("UPWORK"))
    if (not feed.bozo):
        for job in feed['entries']:
            job_id = job['title'].lower().replace(" ", "")
            if (job_id not in getNotifiedId() and notify(job['title']+'\n'+job['link'])):
                    print(time.ctime(time.time())+" : "+job_id)
                    setNotifiedId(job_id)
                    time.sleep(1)
    else:
        print("Network Error: Feedparser")


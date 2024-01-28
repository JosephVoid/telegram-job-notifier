# Telegram Job Notifier

### Description
This python application helps poll job sites (Djinni & Upwork) for relevant jobs

### Installation
1. Create `notified_jobs.txt`, `exec.log`, `.config` & `.env` files
2. Insert your links (with appopriate query params and page) or rss in the .config file in the following format
```
    DJINNI ; https:\\djinni.com?job_type=remote&....
    UPWORK_RSS ; https:\\upwork.com\rss
```
3. Insert your token, chatid, and Polling minutes in the following format
```
    TOKEN=<bot-token>
    CHAT=<chat-id>
    MINS=<minutes-to-check-sites>
```
* your chat-id can be found on the @RawDataBot from telegram (you must start your bot btw)
4. Install dependencies from the requirements.txt file by
```
    pip install -r requirements.txt
```
5. Then start the bot in the background with logging
```
    pythonw main.pyw >> exec.log
```
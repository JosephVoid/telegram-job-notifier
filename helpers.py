import os
import requests
import re
import random


def getURLs():
    urls = dict()
    urls.setdefault("NoKey", "NoValue")
    with open(".config", "r") as f:
        for line in f.readlines():
            key = line.split(" ; ")[0]
            value = line.split(" ; ")[1]
            urls[key] = value
    return urls


def getNotifiedId() -> list[str]:
    notified = []
    with open("notified_jobs.txt", "r", encoding="utf-8") as f:
        for _id in f.readlines():
            notified.append(_id.rstrip("\n"))
    return notified


def setNotifiedId(_id):
    with open("notified_jobs.txt", "a", encoding="utf-8") as f:
        f.writelines(_id + "\n")
    return True


def getScrapedId() -> list[str]:
    scraped = []
    with open("scraped_jobs.txt", "r", encoding="utf-8") as f:
        for _id in f.readlines():
            scraped.append(_id.rstrip("\n"))
    if len(scraped) > 50:
        clearFirst(40)
    return scraped


def setScrapedId(_id):
    with open("scraped_jobs.txt", "a", encoding="utf-8") as f:
        f.writelines(_id + "\n")
    return True


def storeScrape(id, job):
    jb_title = job["title"].replace(",", " ")
    jb_category = getContent(job["content"], "CATEGORY")
    jb_skills = getContent(job["content"], "SKILLS")
    jb_houry = getContent(job["content"], "HOURLY")
    jb_fixed = getContent(job["content"], "BUDGET")
    jb_country = str(getContent(job["content"], "COUNTRY")).replace(",", " ")
    jb_post_date = job["published"].replace(",", " ")
    with open("job_store.txt", "a", encoding="utf-8") as f:
        f.writelines(
            str(id[:6])
            + str(random.randint(100000, 999999))
            + "^"
            + jb_title
            + "^"
            + jb_category
            + "^"
            + jb_country
            + "^"
            + jb_skills
            + "^"
            + str(jb_houry)
            + "^"
            + str(jb_fixed)
            + "^"
            + jb_post_date
            + "\n"
        )

    return True


def getContent(data, target):
    desc_str = data[0].value
    if target == "SKILLS":
        # Extract Skills
        skills_pattern = re.compile(r"<b>Skills</b>:(.*?)<br />")
        skills_matches = skills_pattern.findall(desc_str)
        skills_set = set()
        for match in skills_matches:
            skills_set.update(skill.strip() for skill in match.split(","))

        skills = ", ".join(sorted(skills_set))
        return skills

    elif target == "CATEGORY":
        # Extract Category
        category_pattern = re.compile(r"<b>Category</b>:\s*(\w+)")
        category_match = category_pattern.search(desc_str)
        category = category_match.group(1) if category_match else None
        return category
    elif target == "BUDGET":
        # Extract Budget
        budget_pattern = re.compile(r"<b>Budget<\/b>:\s*\$([0-9,]+)")
        budget_match = budget_pattern.search(desc_str)
        budget = budget_match.group(1) if budget_match else None
        return budget
    elif target == "HOURLY":
        # Extract Hourly
        hourly_pattern = re.compile(
            r"<b>Hourly Range<\/b>:\s*\$([0-9,.]+)-\$([0-9,.]+)"
        )
        hourly_match = hourly_pattern.search(desc_str)
        hourly_min = hourly_match.group(1) if hourly_match else None
        hourly_max = hourly_match.group(2) if hourly_match else None
        return str(hourly_min) + "-" + str(hourly_max)
    elif target == "COUNTRY":
        # Extract Hourly
        country_pattern = re.compile(r"<b>Country<\/b>:\s*(\w[\w\s]*)")
        country_match = country_pattern.search(desc_str)
        country = country_match.group(1) if country_match else None
        return str(country).strip()


def clearFirst(n):
    with open("scraped_jobs.txt", "r") as src:
        lines = src.readlines()
    remaining_lines = lines[n:]
    with open("scraped_jobs.txt", "w") as src:
        src.writelines(remaining_lines)


def check_bot():
    response = requests.get(
        "https://api.telegram.org/bot" + os.environ["TOKEN"] + "/getMe"
    )
    if response.status_code == 200:
        return True
    else:
        return False


def notify(text):
    response = requests.get(
        "https://api.telegram.org/bot" + os.environ["TOKEN"] + "/sendMessage",
        params={"chat_id": os.environ["CHAT"], "text": text},
    )
    if response.status_code == 200:
        return True
    else:
        return False

from bs4 import BeautifulSoup

class Job:
    def __init__(self, id, title, link):
        self.id = id
        self.title = title
        self.link = link

def parser(html_input):
    loaded_jobs = []

    if (not isinstance(html_input, str)) :
        raise Exception("Not of String type")

    soup = BeautifulSoup(html_input, 'html.parser')
    jobs = soup.findAll('a', class_ ='h3 job-list-item__link')

    if jobs:
        for job in jobs:
            key = job.text.strip().lower().replace(" ", "")
            value = job.text.strip()
            link = "https://djinni.co"+job['href']
            loaded_jobs.append(Job(key, value, link))

    return loaded_jobs
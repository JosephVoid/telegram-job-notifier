from bs4 import BeautifulSoup

def parser(html_input):
    loaded_jobs = dict()

    if (not isinstance(html_input, str)) :
        raise Exception("Not of String type")

    soup = BeautifulSoup(html_input, 'html.parser')
    jobs = soup.findAll('a', class_ ='h3 job-list-item__link')

    if jobs:
        for job in jobs:
            key = job.text.strip().lower().replace(" ", "")
            value = job.text.strip()
            loaded_jobs[key] = value

    return loaded_jobs
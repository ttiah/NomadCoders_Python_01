import requests
from bs4 import BeautifulSoup
import job

keywords = [
    'flutter',
    'python',
    'golang',
]

# https://remoteok.com/remote-python-jobs
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

job_list = []

for keyword in keywords:
    url = f'https://remoteok.com/remote-{keyword}-jobs'
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    job_tr = soup.find('table', id='jobsboard').find_all('tr', class_='job')
    for job_item in job_tr:
        td = job_item.find('td', class_='company')
        locations = td.find_all('div', class_='location')
        positions = []
        for location in locations:
            location = location.text.strip()
            positions.append(location)
        title = td.find('h2').text.strip()
        company = td.find('h3').text.strip()
        locations = positions
        link = f"https://remoteok.com/{td.find('a', class_='preventLink')['href']}"
        # job = {
        #     'title': td.find('h2').text.strip(),
        #     'company': td.find('h3').text.strip(),
        #     'locations': positions,
        #     'link': f"https://remoteok.com/{td.find('a', class_='preventLink')['href']}"
        # }
        # job_list.append(job)
        job_list.append(job.Job(title, company, location, link))

print(job_list[-1])
print(len(job_list))
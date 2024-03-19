import requests
from bs4 import BeautifulSoup

url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# jobs = soup.find('section', id='category-2')
jobs = soup.find('section', class_='jobs').find_all('li')[1:-1]

all_jobs = []

for job in jobs:
    title = job.find('span', class_='title').text.strip()
    # region = job.find('span', class_='region').text.strip()
    company, position, region = job.find_all('span', class_='company')
    url = job.find('div', class_='tooltip--flag-logo').next_sibling['href']
    # if url:
    #     url = url['href']
    job_data = {
        'title': title,
        'company': company.text,
        'position': position.text,
        'region': region.text,
        'url': f'https://weworkremotely.com{url}'
    }
    all_jobs.append(job_data)

print(all_jobs)

import requests
import csv
from bs4 import BeautifulSoup


base_url = 'https://berlinstartupjobs.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://berlinstartupjobs.com'
}

job_list = []

def get_job_list(url):
    print(f'Scrapping {url} ...')
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('ul', class_='jobs-list-items').find_all('li', class_='bjs-jlid')

    for job in jobs:
        job_data = {
            'title': job.find('h4', class_='bjs-jlid__h').find('a').text.strip(),
            'company': job.find('a', class_='bjs-jlid__b').text.strip(),
            'description': job.find('div', class_='bjs-jlid__description').text.strip(),
            'link': job.find('a')['href']
        }
        job_list.append(job_data)

def get_pages(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    pagination = soup.find('ul', class_='bsj-nav').find_all('a')[:-1]
    if pagination:
        pages = len(pagination) + 1
    return pages

print('전체 Job List를 수집하려는 경우: ENTER')
print('스킬 검색 하려면 스킬을 입력하세요: 예)python')
skill = input('INPUT: ')

if len(skill) == 0:
    search_url = f'{base_url}engineering/'
    total_pages = get_pages(search_url)
    for i in range(1, total_pages+1):
        job_url = f'{base_url}engineering/page/{i}/'
        get_job_list(job_url)
else:
    command = skill.lower().strip()
    search_url = f'{base_url}skill-areas/{skill}/'
    get_job_list(search_url)


fields = ['title', 'company', 'description', 'link']
filename = f'{skill}_jobs.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for job in job_list:
        writer.writerow(job)

print(f'{filename} 파일에 데이터가 성공적으로 저장되었습니다.')

print(f'LENGTH: {len(job_list)}')
print(job_list[-1])

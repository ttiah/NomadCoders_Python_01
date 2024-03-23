import requests
from bs4 import BeautifulSoup


base_url = 'https://berlinstartupjobs.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://berlinstartupjobs.com'
}

job_list = []

def get_job_list(url):
    # print(f'Scrapping {url} ...')
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        jobs = soup.find('ul', class_='jobs-list-items').find_all('li', class_='bjs-jlid')
        for job in jobs:
            job_data = {
                'title': job.find('h4', class_='bjs-jlid__h').find('a').text.strip(),
                'company': job.find('a', class_='bjs-jlid__b').text.strip(),
                'description': job.find('div', class_='bjs-jlid__description').text.strip(),
                'link': job.find('a')['href']
            }
            job_list.append(job_data)
    except:
        pass

def extract_berlinstartup_jobs(keyword):
    # jobs = [{'title': 'Python 트레이딩 플랫폼 엔지니어 for VegaX', 'company': '콘스텔레이션코리아', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/193356'}]
    # return jobs
    search_url = f'{base_url}skill-areas/{keyword}/'
    get_job_list(search_url)
    return job_list

import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://weworkremotely.com'
}

job_list = []

def extract_weworkremotely_jobs(keyword):
    # jobs = [{'title': 'Python 트레이딩 플랫폼 엔지니어 for VegaX', 'company': '콘스텔레이션코리아', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/193356'}]
    # return jobs
    url = f'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    sections = soup.find_all('section', class_='jobs')
    if sections:
        for section in sections:
            jobs = section.find_all('li')
            for job in jobs:
                if job.find('div', class_='tooltip--flag-logo'):
                    anchor = job.find('div', class_='tooltip--flag-logo').find_next_sibling('a')
                    job_data = {
                        'title': anchor.find('span', class_='title').text,
                        'company': anchor.find('span', class_='company').text,
                        'description': anchor.find('span', class_='region').text,
                        'link': 'https://weworkremotely.com' + anchor['href']
                    }
                    job_list.append(job_data)
    else:
        return job_list
    return job_list

def main(keyword):
    print(extract_weworkremotely_jobs(keyword=keyword))

if __name__ == '__main__':
    keyword = 'java'
    main(keyword)


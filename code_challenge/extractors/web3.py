import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://web3.career'
}

job_list = []

def extract_web3_jobs(keyword):
    # jobs = [{'title': 'Python 트레이딩 플랫폼 엔지니어 for VegaX', 'company': '콘스텔레이션코리아', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/193356'}]
    # return jobs
    url = f'https://web3.career/{keyword}-jobs'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        # jobs = soup.find('tbody', class_='tbody').find_all('tr', class_='table_row')
        jobs = soup.find('tbody', class_='tbody').find_all(lambda tag: tag.name == 'tr' and 'table_row' in tag.get('class', []) and 'border-paid-table' not in tag.get('class', []))
        for job in jobs:
            # for title
            title = job.find('h2', class_='fs-6 fs-md-5 fw-bold my-primary').text
            # for company
            company = job.find('h3').text
            # for description
            description = ''
            location = job.find('td', class_='job-location-mobile').find_next_sibling('td', class_='job-location-mobile')
            locs = location.find_all('a')
            if locs:
                for loc in locs:
                    description = description + loc.text + ','
            else:
                description = location.find('span').text + ','
            description += job.find('p', class_='ps-0 mb-0 text-salary').text
            link = job.find('div', class_='mb-auto align-middle job-title-mobile').find('a')['href']
            link = f'https://web3.career{link}'
            job_data = {
                'title': title,
                'company': company,
                'description': description.strip(),
                'link': link,
            }
            job_list.append(job_data)
    except:
        pass
    return job_list

def main(keyword):
    print(extract_web3_jobs('python'))

if __name__ == '__main__':
    keyword = 'python'
    main(keyword=keyword)

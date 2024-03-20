import time
import csv
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def get_jobs_list(keyword) -> list:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    # browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # 메인 사이트 접속
    page.goto('https://www.wanted.co.kr')
    time.sleep(1)

    # 검색 버튼 클릭
    page.click('button.Aside_searchButton__Xhqq3')
    # page.locator('button.Aside_searchButton__Xhqq3').click()
    time.sleep(1)

    # 검색 키워드 입력
    page.get_by_placeholder('검색어를 입력해 주세요.').fill(keyword)
    time.sleep(1)
    page.keyboard.down('Enter')
    time.sleep(1)

    # 포지션 클릭
    page.click('a#search_tab_position')
    time.sleep(1)

    # 스크롤다운 3번
    for _ in range(3):
        page.keyboard.down('End')
        time.sleep(1)

    # 전체 html 저장
    content = page.content()
    # print(content)

    # playwright 종료
    playwright.stop()

    # html 파싱 시작
    soup = BeautifulSoup(content, 'html.parser')
    jobs_db = []
    jobs = soup.find_all('div', class_='JobCard_container__FqChn')
    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
        title = job.find('strong', class_='JobCard_title__ddkwM').text
        company = job.find('span', class_='JobCard_companyName__vZMqJ').text
        reward = job.find('span', class_='JobCard_reward__sdyHn').text
        job_data = {
            'title': title,
            'company': company,
            'reward': reward,
            'link': link,
        }
        jobs_db.append(job_data)

    return jobs_db

# csv 파일로 저장
def save_csv_file(keyword, jobs) -> None:
    fields = ['title', 'company', 'reward', 'link']
    file_name = f'{keyword}_jobs.csv'
    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        for job in jobs:
            print(job)
            writer.writerow(job.values())

# code challenge
def main():
    keywords =[
        'flutter',
        'python',
        'kotlin',
    ]

    for keyword in keywords:
        jobs = get_jobs_list(keyword)
        save_csv_file(keyword=keyword, jobs=jobs)

if __name__ == '__main__':
    main()

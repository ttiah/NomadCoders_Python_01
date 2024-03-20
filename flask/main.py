# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs
# from file import save_to_file


# keyword = input('What do you want to search for? ')

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs=jobs)

from flask import Flask, render_template, request, redirect, send_file
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from dynamic_scraper.main import get_jobs_list
from file import save_to_file


app = Flask('JobScrapper')

db = {}

@app.route('/')
def home():
    return render_template('home.html')

# jobs = [{'title': 'Python 트레이딩 플랫폼 엔지니어 for VegaX', 'company': '콘스텔레이션코리아', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/193356'}, {'title': 'python 개발자(5년 이상)', 'company': '자이온아이티에스', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/209422'}, {'title': 'Python 서버개발자', 'company': '크로스이엔에프', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/153489'}, {'title': 'Back-End 개발자(Python/4년 이상)', 'company': '제로엑스플로우', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/100701'}, {'title': '[Python] 백엔드 테크 리드 / 핀테크', 'company': '얼리페이', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/206123'}, {'title': '백엔드 개발자 (Python/Django) - 서울', 'company': '비프로컴퍼니(Bepro)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/200403'}, {'title': '[1500억↑투자] Senior Backend Engineer - Python', 'company': '트릿지', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/96146'}, {'title': 'Python Developer (Product)', 'company': '비바리퍼블리카(토스)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/172779'}, {'title': 'Python 트레이딩 플랫폼 엔지니어 for VegaX', 'company': '콘스텔레이션코리아', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/193356'}, {'title': 'python 개발자(5년 이상)', 'company': '자이온아이티에스', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/209422'}, {'title': 'Python 서버개발자', 'company': '크로스이엔에프', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/153489'}, {'title': 'Back-End 개발자(Python/4년 이상)', 'company': '제로엑스플로우', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/100701'}, {'title': '[Python] 백엔드 테크 리드 / 핀테크', 'company': '얼리페이', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/206123'}, {'title': '백엔드 개발자 (Python/Django) - 서울', 'company': '비프로컴퍼니(Bepro)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/200403'}, {'title': '[1500억↑투자] Senior Backend Engineer - Python', 'company': '트릿지', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/96146'}, {'title': 'Python Developer (Product)', 'company': '비바리퍼블리카(토스)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/172779'}, {'title': 'C#, C++, Python, IoT MCU(아두이노,RPi) 개발자', 'company': '아이티로그', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/187186'}, {'title': '[전문연구요원 가능] C/C++, Python 로봇 제어 개발자', 'company': '메디인테크', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/100407'}, {'title': '명품이커머스 python 백엔드 개발자', 'company': '비씨디코퍼레이션', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/211437'}, {'title': 'Python application & Algorithm 개발자', 'company': '메디픽셀', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/190006'}, {'title': '[전문연구요원 가능] C/C++, Python 로봇 제어 개발자 (신입)', 'company': '메디인테크', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/147487'}, {'title': '백엔드 개발자(Python, Django)(1년 이상)', 'company': '수거봇', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/211644'}, {'title': '백엔드 개발자 Node.js, Python/5년 이상', 'company': '딥세일즈', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/211459'}, {'title': '[200억↑투자] 백엔드 개발자(Python)', 'company': '바로팜', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/66521'}, {'title': 'Frontend 및 Backend(python) 개발자', 'company': '마인즈앤컴퍼니', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/156436'}, {'title': '[인텔리전스랩스] MLOps팀 백엔드 개발자 (Python/Go)', 'company': '넥슨코리아(NEXON)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/151721'}, {'title': '웹개발자(Python, Django) 3년이상', 'company': '리걸테크', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/148349'}, {'title': 'Python Developer', 'company': '사이버메드', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/148605'}, {'title': '[200억↑투자] 백엔드 개발자 (Spring, Python, MSA,주니어)', 'company': '페이타랩(패스오더)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/45650'}, {'title': '백엔드(Python) 엔지니어', 'company': '액스', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/209122'}, {'title': '백엔드 엔지니어 (Python)', 'company': '버핏서울', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/197592'}, {'title': '[플레이오][신입] Python 백엔드 개발', 'company': '지엔에이컴퍼니', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/193602'}, {'title': '[200억↑투자] 백엔드 개발자 (Spring, Python, MSA)', 'company': '페이타랩(패스오더)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/196993'}, {'title': '이커머스 솔루션 Python Backend 개발자', 'company': '샐러드랩', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/209397'}, {'title': '백엔드 개발자(Python, Django) (2년차 이상)', 'company': '와이피랩스(커넥팅)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/169285'}, {'title': '[100억↑투자] 백엔드(Python) 개발자 (QUAT)', 'company': '엔라이즈(NRISE)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/190204'}, {'title': '백엔드 엔지니어 (Python)', 'company': '아이네블루메(채티)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/60926'}, {'title': 'Python 백엔드 개발자', 'company': '패스트파이브', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/203425'}, {'title': '오픈업 데이터 엔지니어 (Python)', 'company': '핀다(FINDA)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/180080'}, {'title': '코박(Cobak) 백앤드 개발자[3년 이상] (Python, Django)', 'company': '판도라티비', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/209286'}, {'title': '백엔드 엔지니어 (Python)', 'company': '피클플러스', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/172732'}, {'title': '개발자 (JAVA,Python,AI,IoT)', 'company': '펀진', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/161900'}, {'title': 'Python Django 기반 서버 개발', 'company': '블리몽키즈', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/184372'}, {'title': '웹/앱 백엔드개발자(Python)', 'company': '에임비랩', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/204586'}, {'title': '[인텔리전스랩스] 소셜메이킹팀 백엔드 개발자 (Python)', 'company': '넥슨코리아(NEXON)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/205855'}, {'title': '백엔드 엔지니어 (Python/Django)', 'company': '뮤즈라이브(Muzlive)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/18295'}, {'title': '풀스택 웹 개발자 (Python/Django)', 'company': '웜블러드', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/142233'}, {'title': 'Data Engineer (Python, SQL)', 'company': '이랜드이노플', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/184348'}, {'title': '백엔드 개발자(Python, Django)', 'company': '테일크루(Talecrew)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/207366'}, {'title': '백엔드 엔지니어 (Python)', 'company': '엘리스', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/57878'}, {'title': 'Python 백엔드 개발자 (B2B 서비스, 3년 이상)', 'company': '마이플레이컴퍼니', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/206202'}, {'title': 'Python Developer (Platform)', 'company': '비바리퍼블리카(토스)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/176110'}, {'title': '[인텔리전스랩스] 게임 이상탐지 백엔드 개발자 (Python)', 'company': '넥슨코리아(NEXON)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/202474'}, {'title': 'Python Back-end Engineer', 'company': '올거나이즈코리아(Allganize Korea)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/160068'}, {'title': '파이썬(Python) 개발자', 'company': '에잇퍼센트(8PERCENT)', 'reward': '합격보상금 100만원', 'link': 'https://www.wanted.co.kr/wd/181863'}]

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword:
        keyword = keyword.lower()
        if keyword in db.keys():
            jobs = db[keyword]
        else:
            jobs = get_jobs_list(keyword)
            db[keyword] = jobs
        return render_template('search.html', keyword=keyword, jobs=jobs)
    else:
        return redirect('/')

@app.route('/export')
def export():
    keyword = request.args.get('keyword')
    if keyword == None:
        return redirect('/')
    else:
        keyword = keyword.lower()
    if keyword not in db.keys():
        return redirect('/search?keyword={keyword}')
    save_to_file(keyword, jobs=db[keyword])
    return send_file(f'{keyword}.csv', as_attachment=True)

app.run('0.0.0.0')

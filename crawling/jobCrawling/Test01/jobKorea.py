import requests
from bs4 import BeautifulSoup

URL = "http://www.jobkorea.co.kr/Search/?stext=java&local=K000%2CB170%2CB160%2CB150%2CB125&careerType=1"


# &Page_No=2


def get_last_pages():
    # 페이지 정보 가져오기 (string)
    result = requests.get(URL)

    # 페이지 정보 soup에 담기
    soup = BeautifulSoup(result.text, "html.parser")
    # div 태그에 class명 pagination 찾아 담기
    tplPagination = soup.find("div", {"class": "tplPagination"})
    # a태그(페이지뷰어 링크) ->리스트 형태로 담기
    links = tplPagination.find_all('a')
    # pages변수에 페이지번호 int형으로 담기
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
        # print(link)

    # 페이지 마지막 번호 변수에 담기
    max_page = pages[-1]
    return max_page


def extract_job(html):

    title = html.find("div", {"class": "post-list-info"})
    # a 태그 안에 tilte 속성 가져오기
    anchor = title.find("a").get("title")

    company_anchor = ""
    location = ""
    link = ""
    if anchor is not None:
        #print("title = ", anchor)
        company = html.find("div", {"class": "post-list-corp"})
        company_anchor = company.find("a")["title"]
        # 회사명에 링크가 달린 경우오 ㅏ아닌 경우로 나눠져있음
        # if문으로 구분하여 링크가 있으면 링크도 빼오기

        #print("company = ", company_anchor)

        # 회사 위치 가져오기 1. 기본적인 방법(장소가 none인 경우가 없을 경우))
        location = html.find("span", {"class": "loc long"}).string
        #print("location : ", location)

        # 링크가져오기
        link = html.find("div", {"class": "post-list-info"}).find('a')["href"]
        #print("link : ", link)

    return {'title': anchor, 'company': company_anchor, 'location': location,
            'link': f"http://www.jobkorea.co.kr/{link}"}


def extract_jobs(last_page):
    jobs = []
    # 19개의 requests만들기
    # 페이지마다 url이나 페이지변환이 다름
    for page in range(last_page):
        #print(f"scrapping page {page}")
        result = requests.get(f"{URL}&Page_No={page+1}")
        # 작동확인 .status_code
        # print(result.status_code)

        # soup으로 각 일자리관련 정보 뽑아오기
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "post"})
        for result in results:
            # extract_job() 함수로 빼기
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_pages()
    jobs = extract_jobs(last_page)
    return jobs
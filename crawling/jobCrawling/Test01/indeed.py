import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=java&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"

def get_last_pages():

  #페이지 정보 가져오기 (string)
  result = requests.get(URL)

  #페이지 정보 soup에 담기
  soup = BeautifulSoup(result.text, "html.parser")
  #div 태그에 class명 pagination 찾아 담기
  paginatrion = soup.find("div", {"class":"pagination"})
  #a태그(페이지뷰어 링크) ->리스트 형태로 담기
  links = paginatrion.find_all('a')
  #pages변수에 페이지번호 int형으로 담기
  #마지막은 next(문자열)이라 -1 처리하여 빼줌
  pages = []
  for link in links[:-1]:
    emt = link.find("span").string
    if emt != "«\xa0이전":
      pages.append(int(emt))

  #페이지 마지막 번호 변수에 담기
  max_page = pages[-1]
  return max_page


# 글 제목과, 회사이름을 리턴해주는 함수
def extract_job(html): # soup을 인자로 받는 함수
  title = html.find("div",{"class":"title"})
    #a 태그 안에 tilte이 있어서 그걸 가져올 것
  anchor = title.find("a")["title"]
    #print("title:",anchor)
  company = html.find("span",{"class":"company"})
  company_anchor = company.find("a")
    #회사명에 링크가 달린 경우오 ㅏ아닌 경우로 나눠져있음
    #if문으로 구분하여 링크가 있으면 링크도 빼오기
  if company_anchor is not None :
    company = str(company_anchor.string)
  else:
    company = str(company.string)
  company = company.strip()

  # 회사 위치 가져오기 1. 기본적인 방법(장소가 none인 경우가 없을 경우))
  #location = html.find("span", {"class":"location"}).string
  #print(location)

  #회사 위치 none이 존재할 경우 위 코드 에러!!
  #페이지 코드를 보면 div로 숨겨진 location 속성이 있다 그걸 불러오기~~
  location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
  #print("장소: ", location)

  #링크를 위한 회사 고유id 출력하기
  job_id = html["data-jk"]

  return {'title':anchor, 'company':company, 'location':location, 'link':f"https://kr.indeed.com/viewjob?jk={job_id}"}


#한 회사의 정보(리스트에 뿌려지는)를 가지고 있는 함수
def extract_jobs(last_page):
  jobs = []
#19개의 requests만들기
#페이지마다 url이나 페이지변환이 다름

  for page in range(last_page):
    #print(f"****scrapping page {page}***")
    result = requests.get(f"{URL}&start={page*LIMIT}")
      #작동확인 .status_code
      #print(result.status_code)

      #soup으로 각 일자리관련 정보 뽑아오기
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
      #extract_job() 함수로 빼기
      job = extract_job(result)
      jobs.append(job)
  return jobs


  ###########  ###########

def get_jobs():
  last_page = get_last_pages()
  jobs = extract_jobs(last_page)
  return jobs


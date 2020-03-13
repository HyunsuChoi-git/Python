
'''
# requests (urllib.request와 비슷)
    : 파이썬에서 HTTP 요청을 보낼 때 많이 사용되는 모듈
     requset로 HTTP요청을 하면 응답에 관련된 정보들을 함께 응답객체로 반환해줌
     라이브러리 추가 설치 필요함
# BeautifulSoup
    : HTML의 태그를 파싱해서 필요한 데이터만 추출하는 함수를 제공하는 라이브러리
    * 파싱 : 문자열을 분석하여 의미있는 토큰으로 분해해서 파스 트리를 만드는 과정
        문자열을 일정한 포맷에 맞게 구조화(변경) 해줌

    urllib + bs
    requests + bs  이렇게 혼합하여 많이 쓴다.


    CRUD : 클라이언트가 서버에 데이터를 요청할 때 크게 4가지 타입이 있다
        Create -> POST  : 데이터 추가 요청 메소드
        Read   -> GET   : 서버에 데이터를 요청할 때 사용하는 메소드
        Update -> PUT   --->거의안ㅆ므
        Delete -> DELETE ---> 거의안ㅆ므

'''

#1. 라이브러리 임포트
import requests

url = "http://www.naver.com"
#요청! 응답을 리턴해줌
res = requests.get(url)
print(res.status_code) #//응답코드
print(res.headers)  #//딕셔너리타입으로 리턴
print(res.cookies)
print(list(res.cookies))
#// 사이트의 여러코드정보를 볼 수 있다~~


#html 코드보기
print(res.text)
print(res.content) #//바이너리타입으로 리턴
print(res.encoding)

#요청시 데이터를 보내는 방법
#GET    : .get()
response = requests.get(url)
#POST   : .post()
url = "http://www.naver.com"
response = requests.post(url, data={"key1":"value1"})
print(response.url)

'''
request 예외
HTTPError
ConnectionError
ProxyError
SSLError  (http)
Timeout
ConnectionTimeout
URLRequired
TooMayRedirects
MissingSchema
InvalidURL

'''

#예외처리
try:
    url = "naver.com"   #// --> http가 생략되어 missimgSchema 에러 뜸
    response = requests.get(url)
    print(response.url)
except requests.exceptions.HTTPError:
    print("http 에러 발생")
except requests.exceptions.Timeout:
    print("timeout 에러 발생!")
except requests.exceptions.MissingSchema:
    print("missingSchema 에러 발생!!")


'''
BeautifulSoup 파싱 모듈
'''

from bs4 import BeautifulSoup
html="""    
"""
#//파서 parser : 원시코드인 순수 문자열 객체를 해석할 수 있도록 분석하는 것
#//파이썬에서 사용되는 파서는 lxml, html5lib, html.parser 가 있다.

html = """<p>test</p>"""
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print(soup.prettify())
print(type(soup))


#// res = requests.get(url)---> res.text or res.content
html = """<html>
<head><title class="t a b">test title</title></head>
<body> <p>hahaha</p> <p>haahaha2</p> <p>hahahaha3</p> </body>
</html>"""

soup = BeautifulSoup(html, "html.parser")
print(soup.title)       #//<title>test title</title>
print(type(soup.title)) #//<class 'bs4.element.Tag'>

#//해당태그 내부의 모든 텍스트를 전부 리턴
print(soup.title.text)  #//text title
#//string : 태그 내부의 텍스트 : 정확하게 해당 태그에 대한 값만 가져온다.
print(soup.title.string)  #//test title
#//태그 이름가져오기
print(soup.title.name) #//title

#//타이틀 태그만 가져오기
title_tag = soup.title
print(title_tag.attrs) #// {'class': ['t', 'a', 'b']}
print(title_tag['class']) #// ['t', 'a', 'b']
print(title_tag.get('name'))


###//원하는 요소 정확히 접근하기
html = """<html>
<head><title class="t a b">test title</title></head>
<body> <p>hahaha</p> <p id='a'>haahaha2</p> <p>hahahaha3</p> </body>
</html>"""

soup = BeautifulSoup(html, "html.parser")
##// find_all() : 원하는 태그들을 리스트 형태로 얻어올 수 있다.
#//1. 태그명으로 가져오기
print(soup.find_all('title'))
print(soup.find_all('p'))
#//2. id속성으로 가져오기
print(soup.find_all(id='a'))
from urllib.request import Request, urlopen

url = "https://www.naver.com"

#// 2. 요청
#// url 주면서 요청 객체를 만들고
# req = Request(url)
# #// 만들어진 요청 객체를 이용하여 페이지 요청 : urlopen()은 요청 후 응답을 객체로 리턴
#
# page = urlopen(req)
#
# #//3. 응답 결과 객체 정보를 출력
# print(page)
# print(page.code)   #//응답코드
# print(page.headers) #//헤더정보만 추출
# print(page.url)     #//url 추출
# print(page.info().get_content_charset())  #//인토딩형태 추출
#
# #//4. html 꺼내기
# print(page.read())   #.read() 는 html문서를 바이너리형태로 가져온다.

#////////////////////////////////////////////////////

#//5. POST 요청
#//5-1. post 요청 시 보낼 데이터 만들기 : 데이터를 만들 때는 바이너리 형태로 인코딩해서 보내야한다.
import urllib
data = {"key1" : "value1", "key2" : "value2"}
data = urllib.parse.urlencode(data)  #//딕셔너리를 쿼리스트링의 형태로 바꿔주기. (url이 인식할 수 있는 형태로 인코딩)
data = data.encode("utf-8")     #// 쿼리스트링처럼 표현된 문자열을 UTF-8로 인코딩하여 바이너리형태로 바꿔준다.
print(data)   #// b'key1=value1&key2=value2'   --> b 붙은것 : 바이너리형태이다.

#//5-2. post요청
# 요청 객체 만들기 : url, 요청시 던져줄 데이터,  headers
req_post = Request(url, data=data, headers={})
#요청
page = urlopen(req_post)

#응답 출력해보기
print(page)
print(page.url)


#6. GET 요청
# urllib의 Request 객체 생성 시, 두번째 인자값이 존재하면 Post요청,
# 두번째 인자가 None 이거나 생략하면 DET요청이다.
req_get = Request(url+"?key1=value&key2=value2", None, headers={})
page = urlopen(req_get)
print(page)
print(page.url)
print("code", page.code)

#7. 파일 다운로드 : urlretrieve 함수를 사용해 직접 다운 가능.
from urllib.request import urlretrieve

#웹브라우저에서 원하는 이미지주소를 가져온다. (구글로고이미지)
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"

#저장할 이미지 경로 + 이름 만들어놓기
name = "googleLogo.png"     #확장자명은 본래 이미지파일과 동일해야한다.

#이미지 다운로드 : 인자 : (다운받을 데이터 url, 저장할 파일 경로)
urlretrieve(url, name)


#//라이브러리 임포트하기
from selenium import webdriver

#//1. (드라이버 던져주어)브라우저 띄우기
driver = webdriver.Chrome('chromedriver.exe')
                    #//같은 폴더에 있기 때문에 파일명만 적어도 됨.
url = "https://www.naver.com/"
driver.get(url)

'''
*** selenium 으로 브라우저 DOM에 접근하는 함수들 ***
# 리턴타입 : 단일 객체 (BS find())
find_element_by_id
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
find_element_by_xpath           : xml 문서 접근하기 위한 문법
find_element_by_link_text
find_element_by_name

# 리턴타입 : 리스트 (BS find_all())
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
find_elements_by_xpath           : xml 문서 접근하기 위한 문법
find_elements_by_link_text
find_elements_by_name


*** xpath : XML Path Language ***
W3C 표준으로 XML 문서의 구조를 통해 경로(path)위에,
지정한 구문을 사용하여, 항목을 배치하고 처리하는 언어

/   : 절대경로
//  : 문서내에서 검색
//@href : href 속성이 있는 모든 태그
    //a[@href="http://www.google.com]   어떤 태그인데 href의 속성은 = 의 내용일 경우 많이 사용
(//a)[3]    : 문서의 세번째 링크(a태그)
(//table)[last()]   : 문서의 마지막 테이블 선택
(//a)[position() < 3 ]  : 문서의 처음 두 a태그
//table/tr/*    : 모든 테이블에서 모든 자식 tr
//div[@*]   : 속성이 하나라도 있는 div태그 선택
    //div[@data="test"]


'''
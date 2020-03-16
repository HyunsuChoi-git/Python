#//라이브러리 임포트하기
from selenium import webdriver

#//1. (드라이버 던져주어)브라우저 띄우기
driver = webdriver.Chrome('chromedriver.exe')
                    #//같은 폴더에 있기 때문에 파일명만 적어도 됨.
url = "https://www.naver.com/"
driver.get(url)

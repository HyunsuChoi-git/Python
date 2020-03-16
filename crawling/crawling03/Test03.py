import requests
from bs4 import BeautifulSoup
from pprint import  pprint

url = "https://movie.naver.com/movie/point/af/list.nhn"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
# print(soup)
# 영화명
title = soup.select('a.movie.color_b')
score = soup.select('td.title > div > em')
br = soup.select('td.title > br')
print('br=',br)

lists = []
for i in range(10):
    print("제목 : ", title[i].text, "평점 : ",score[i].text)
    print("리뷰 : ",br[i].next_sibling.strip())
    li = [title[i].text,score[i].text,br[i].next_sibling.strip()]
    lists.append(li)
pprint(lists)
'''
영화제목
#old_content > table > tbody > tr:nth-child(1) > td.title > a.movie.color_b
#old_content > table > tbody > tr:nth-child(2) > td.title > a.movie.color_b
#old_content > table > tbody > tr:nth-child(3) > td.title > a.movie.color_b

평점
#old_content > table > tbody > tr:nth-child(1) > td.title > div > em
#old_content > table > tbody > tr:nth-child(2) > td.title > div > em

리뷰(<br>)
#old_content > table > tbody > tr:nth-child(1) > td.title > br
#old_content > table > tbody > tr:nth-child(2) > td.title > br
'''
html = """<html>
<head><title>타이틀</title></head>
<body><p><span>1111</span><span>2222</span></p></body>
</html>
"""
soup = BeautifulSoup(html,'html.parser')
p_contents = soup.p.contents
print(p_contents)

p_children = soup.p.children
for child in p_children:
    print(p_children)
'''
#BeautifulSoup 파싱한 데이터(soup)에서 추출
#함수 : find(), find_all(), select()
#태그 : soup.태그명
#자식태그 : contents, children
        soup.p.contents : 자식태그들을 list가져옴.
        soup.p.children : 이터레이터 object 반환.
#부모태그 : parent, parents
#형제태그 : next_sibling, previous_sibling (단수)
            next_siblings, previous_siblings (복수)
#다음, 이전 요소 : next_element(s), previous_element(s) (단수 / 복수)            


'''
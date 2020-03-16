import requests
from bs4 import BeautifulSoup


#네이버 영화 랭킹 가져오기
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20200315"

html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

mv_names = soup.find_all('td','title')
mv_points = soup.find_all('td','point')

# for i in range(len(mv_names)):
#     print(f"제목 : {mv_names[i].text.strip()}\t\t평점 : {mv_points[i].text.strip()}")



# 리뷰 가져오기기
# 1페이지
# url = 'https://movie.naver.com/movie/point/af/list.nhn?'
# html = requests.get(url)
# soup = BeautifulSoup(html.content, 'html.parser')
#
# title = soup.select('a.movie.color_b')
# score = soup.select('td.title > div > em')
# br = soup.select('td.title > br')
#
# for i in range(10):
#     print(f"제목 : {title[i].text}\t/평점 :  {score[i].text}")
#     print(f"리뷰 : {br[i].next_sibling.strip()}")
#     print()

#4페이지까지
# for i in range(1,5):
#     url = 'https://movie.naver.com/movie/point/af/list.nhn?&page='+str(i)
#
#     html = requests.get(url)
#     soup = BeautifulSoup(html.text, 'html.parser')
#
#     anc = soup.find_all('td','title')
#     br = soup.select('td.title > br')
#
#     for i in range(len(anc)):
#         mv_names = anc[i].find('a',{'class':'movie color_b'}).text.strip()
#         mv_points = anc[i].find('em').text.strip()
#
#         print(f"제목 : {mv_names}\t/평점 :  {mv_points}")
#         print(f"리뷰 : {br[i].next_sibling.strip()}")


html = """<html>
<head><title>타이틀</title></head>
<body><p><span>1111</span><span>2222</span></p></body>
</html>
"""
soup = BeautifulSoup(html,'html.parser')
p_contents = soup.p.contents
print(p_contents)
#//[<span>1111</span>, <span>2222</span>]


p_children = soup.p.children
for child in p_children:
    print(p_children)
    #//<list_iterator object at 0x00000000038080D0>
    #//<list_iterator object at 0x00000000038080D0>


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
html = """<html>
<head>
    <title>타이틀</title>
</head>
<body>
    <p>
        <span>1111</span>
        <span>2222</span>
    </p>
</body>
</html>"""
soup = BeautifulSoup(html, 'html.parser')
p_contents = soup.p.contents
print(p_contents)
#//['\n', <span>1111</span>, '\n', <span>2222</span>, '\n']
p_children = soup.p.children

for child in p_children:
    print(child)
#//<span>1111</span>
#//<span>2222</span>
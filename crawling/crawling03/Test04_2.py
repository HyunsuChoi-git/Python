import requests
from bs4 import BeautifulSoup
from pprint import pprint

#네이버 웹툰 썸내일(이미지) 가져오기
#(안될 경우도 종종 있음)

url = 'https://comic.naver.com/webtoon/weekday.nhn?order=StarScore'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

#요일별 웹툰 영역 추출
data = soup.find_all('div', {'class':'col_inner'})
#pprint(data)

'''
하나의 요일 구조
<div class='col'>
    <div class='col_inner'>
        <h4>월요 웹툰...</h4>
        <ul>
            <li></li>  //한 웹툰의 썸네일
            <li></li>  //한 웹툰의 썸네일 
            <li></li>  //한 웹툰의 썸네일
            ....
        </ul>
    </div>
</div>
'''
#전체 웹툰 리스트에 넣기
li_list = []
for d in data:
    li_list.extend(d.find_all('li'))  # li태그들을 리스트에 담기

#pprint(li_list)


'''
한 요일의 구조
<li>
    <div class="thumb">
		<a href="/webtoon/list.nhn?titleId=183559&amp;weekday=mon" onclick="nclk_v2(event,'thm*m.img','','1')">
		    <img onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/blank.gif' "
		     src="https://shared-comic.pstatic.net/thumb/webtoon/183559/thumbnail/thumbnail_IMAG10_5e13c29c-f451-4430-a84a-a46495fb8cc3.jpg" 
		     width="83" height="90" title="신의 탑" alt="신의 탑"><span class="mask"></span>
	        <em class="ico_updt"></em>
		</a>
    </div>
	<a href="/webtoon/list.nhn?titleId=183559&amp;weekday=mon" onclick="nclk_v2(event,'thm*m.tit','','1')"
	 class="title" title="신의 탑">신의 탑</a>
</li>

'''

#제목과 이미지 링크
'''
for li in li_list:
    img = li.find('img')  #이미지 태그 추출
    title = img['title']  #이미지 태그에서 title 속성값(웹툰제목) 추출
    img_src = img['src']  #이미지 태그에서 image 링크 추출
    print(title, img_src)
'''

#이미지 저장하기

##-urlretrieve 라이브러리 추가

##-이미지 저장할 폴더 생성
'''
파이썬은 os 패키지 기본제공 import 시켜서 사용하기
errono  :  에러발생시 코드로 지정해 놓은 모듈이 존재함.
re : 정규표현식을 사용할 때 사용하는 패키지. (기본제공)
'''
from urllib.request import urlretrieve
import os, errno, re

try:
    if not(os.path.isdir('image')):
        #'image' 이름을 가진 폴더가 존재하지 않다면 폴더를 만들 것
        os.makedirs(os.path.join('image'))
        #os.path.join() : 입력으로 들어온 문자열까지 합쳐서 새로운 경로를 생성시킨다.
except OSError as e:
    if e.errno != errno.EECIST:
        print("폴더생성 실패!!!")
        exit()  #시스템을 중지시킴

#제목과 이미지 링크
for li in li_list:
    img = li.find('img')  #이미지 태그 추출
    title = img['title']  #이미지 태그에서 title 속성값(웹툰제목) 추출
    img_src = img['src']  #이미지 태그에서 image 링크 추출
    print(title, img_src)

    # 저장
    title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title)
    #정해놓은 표현식 이외의 문자열을 ''로 치환하겠다.

    urlretrieve(img_src, 'image/'+title+'.jpg')

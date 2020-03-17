#인스타그램
from selenium import webdriver
import urllib
import time

keyword = input("키워드 입력 : ")
keyword = urllib.parse.quote(keyword)

driver = webdriver.Chrome("chromedriver.exe")
url = "https://www.instagram.com/explore/tags/"+str(keyword)+"/?hl=ko"
########

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
driver.implicitly_wait(3)

instar_tags = []

# 이미지 클릭 > 해쉬태그 긁기 > ">" 눌러서 다음 포스트로 가서 해쉬태그 긁기
#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1)
driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()  #클래스명
driver.implicitly_wait(3)
tags = driver.find_elements_by_css_selector('a.xil3i')
for i in range(6):
    #해쉬태그 긁기
    print(i)
    for t in tags:   # 해쉬태그들을 반복해서 각각 접근
        raw = t.text        #해쉬태그기호 삭제
        raw = raw.replace('#','')       #리스트에 추가
        instar_tags.append(raw)


    #다음 포스트로 넘어가기 버튼 > 클릭
    driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow')
    #driver.implicitly_wait(3)
    time.sleep(3)

print(instar_tags)

# 불필요한 해시태그 삭제하기
stop_word = ['스타벅스', '스벅', 'starbucks']
instargram_tag = [word for word in instar_tags if word not in stop_word]


#워드 클라우드 만들기!
# wordcloud,matplotlib  설치하기

import matplotlib.pyplot as pyplot
from wordcloud import WordCloud

# wordcloud = WordCloud().generate(' '.join(instargram_tag))  ---> 한글이라 깨짐
wordcloud = WordCloud(font_path='C:\Windows\Fonts\gulim.ttc', background_color='white', max_words=1000).generate(' '.join(instargram_tag))
#generate(' '.join(instargram_tag)) 로 워드클라우드를 만드는 것
#' ' --> 배열(instargram_tag)에 담긴 워드들을 띄어쓰기 구분자로 인식하도록 한 것.

# pyplot 이용하여 만든 wordcloud 보여주기.
pyplot.imshow(wordcloud, interpolation='bilinear')
                            #이미지 부드러운 정도, 옵션
pyplot.axis("off")
pyplot.show()
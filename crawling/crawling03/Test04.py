import requests
from bs4 import BeautifulSoup


#네이버 웹툰 제목 가져오기

url = 'https://comic.naver.com/webtoon/weekday.nhn?order=StarScore'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

#res.close()
#요일 한 기둥
#content > div.list_area.daily_all > div.col.col_selected > div.col.inner
# div = soup.find('div', {'class':'col_inner'}) # 첫번째 col_inner div 태그만 가져옴
# titles = div.find_all('a','title')  # 첫번쨰 요일 기둥에서 a.title 태그들만 가져옴.
# title_list = []
# for t in titles:
#     title_list.append(t.text) # a태그와 text만 뽑아서 리스트에 저장.
# pprint(title_list)

# t_list = [t.text for t in titles]
# pprint(t_list)
#
# lst = [1,2,3,4,5]
# a_lst = [i for i in lst]
# print(a_lst)
#content > div.list_area.daily_all > div:nth-child(2) > div


div = soup.find_all('div', {'class':'col_inner'})
#print(div)

week_list = []
for d in div:
    #하나의 요일에서 제목들 추출
    titles = d.find_all('a','title')
    title_list = [t.text for t in titles]
    week_list.append(title_list)

print(week_list)


import requests
from bs4 import BeautifulSoup

#네이버 실시간 검색어 가져오기


# copy element : class속성값
# <span class="item_title">김미균</span>
# <span class="item_title">미스터트롯 진</span>

# copy selector :
# #content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul:nth-child(1) > li:nth-child(1) > div > span.item_title_wrap > span
# #content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul:nth-child(1) > li:nth-child(2) > div > span.item_title_wrap > span

#헤더정보 가져오기 http://www.useragentstring.com/
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.content, "html.parser")

data = soup.find_all('span', 'item_title')
print(data)
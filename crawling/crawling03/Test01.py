import requests
from bs4 import BeautifulSoup


##네이버 속보 헤드라인 가져오기

url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"

news = requests.get(url)
soup = BeautifulSoup(news.content, 'html.parser')

'''
#copy selector로 헤드라인의 태그 경로 알아보기 (세~네개 정도)

main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(2) > dl > dt:nth-child(2) > a
main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(3) > dl > dt:nth-child(2) > a


#ul.type06_headline 까지 짜르기 (그 뒤부터 순서대로 태그가 바뀜)
ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
ul.type06_headline > li:nth-child(2) > dl > dt:nth-child(2) > a
ul.type06_headline > li:nth-child(3) > dl > dt:nth-child(2) > a
'''

data1 = soup.select('ul.type06_headline > li > dl > dt:nth-child(2) > a')
# for i in data1 :
#     print(i.text.strip())


'''
main_content > div.list_body.newsflash_body > ul.type06 > li:nth-child(1) > dl > dt:nth-child(2) > a
main_content > div.list_body.newsflash_body > ul.type06 > li:nth-child(2) > dl > dt:nth-child(2) > a
'''
data2 = soup.select('ul.type06 > li > dl > dt:nth-child(2) > a')
# for i in data2:
#     print(i.text.strip())

data = data1 + data2
for i in data:
    print(i.text.strip())


'''
1~5페이지 까지 긁어오기

main_content > div.paging > a:nth-child(2)
main_content > div.paging > a:nth-child(3)
main_content > div.paging > a:nth-child(4)

'''
for i in range(1,6):
    i = i.__str__()
    url2 = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20200316&page='+i
    news = requests.get(url2)
    soup = BeautifulSoup(news.content, 'html.parser')

    data1 = soup.select('ul.type06_headline > li > dl > dt:nth-child(2) > a')
    data2 = soup.select('ul.type06 > li > dl > dt:nth-child(2) > a')

    data = data1 + data2

    print(f'----{i}page----')
    for i in data:
        print(i.text.strip())


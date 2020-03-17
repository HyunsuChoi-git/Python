'''
CSV 파일 - 데이터 저장/읽기
CSV (Comma-Seperated Values)
    형식 : 각 열은 콤마(,)로 구분, 각 행은 줄바꿈 문자로 구분
    라이브러리 : csv
'''

import csv

#//1. csv 파일 저장
with open('test01.csv', 'w', encoding='UTF-8', newline='') as writer_csv:
    #// ㄴ> 파일정보들
    writer = csv.writer(writer_csv, delimiter=',')
                #// ㄴ>    파일 객체,   구분자 (콤마)
    writer.writerow(['a','b','c','d'])
    writer.writerow(['aa','bb','cc','dd'])
    writer.writerow(['a2','b2','c2','d2'])
    writer.writerow(['hera']*3 + ['hi'])



#2. csv 파일 읽기
with open('test01.csv', 'r', encoding='UTF-8') as reader_csv:
    reader = csv.reader(reader_csv, delimiter=",")
    for row in reader:
        print(row)


# #3. 사전타입으로 저장
# with open('test02.csv', 'w', encoding='UTF-8') as writer_csv:
#     name_list = ['first name', 'last name']
#     writer = csv.DictWriter(writer_csv, fieldnames=name_list)
#     writer.writeheader()
#     writer.writerow({'first name':'iron','last name' : 'man'})
#     writer.writerow({'first name':'ant','last name' : 'man'})
#     writer.writerow({'first name':'captain','last name' : 'america'})
#     writer.writerow({'first name':'black','last name' : 'widow'})


#4. 사전타입으로 읽기
with open('test02.csv', 'r', encoding='UTF-8') as reader_csv:
    reader = csv.DictReader(reader_csv)
    for row in reader:
        print(row['first name'], row['last name'])
        #한 줄이 dict 타입 : 데이터는 dict의 키 값으로 추출한다.
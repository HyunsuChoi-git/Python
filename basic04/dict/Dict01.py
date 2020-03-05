# dic = {}
# print(dic)
# print(type(dic))
#
#
# #//
# dic = {"런던":"영국", "서울":"한국", "파리":"프랑스"}
# print(dic)
#
# print(dic["런던"])
# print(dic["서울"])
# print(dic["파리"])
#
# # key를 꺼내오는 함수 : keys()
# key_list = dic.keys()
# print(key_list)
#
# # value를 꺼내오는 함수 : values()
# value_lsit = dic.values()
# print(value_lsit)
#
# # key와 value 를 쌍으로 꺼내오는 함수 : items()
# item_list = dic.items()
# print(item_list)
#
# info = {"mob":"1010-111-222","age":20,"name":"아이언맨"}
# print(info)
# # key값을 이용해서 value를 꺼내오는 함수 : get()
# mob = info.get("mob")
# city = info.get("cidksa")
# print(city) #없는 key를 꺼내면 none으로 처리
#
# # 인덱스에 key값을 주고 value를 꺼내오기
# #mob1 = info["mob"]
# #city1 = info["cidsadty"]
# #print(city1)  # 없는 key값 넣으면 에러발생!!
#
# #딕셔너리에 해당 키값이 존재하는지 알아보기 : in
# result = "age" in info
# print(result)
# print(type(result))
#
# #딕셔너리에 요소 추가하기 : update()
# info.update({"city":"seoul"})
# print(info)
# #기존에 키값이 존재하면 value만 update()
# info.update({"city":"busan"})
# print(info)
#
# #키값이 존재하지 않으면 요소 추가
# info["gender"] = "Female"
# print(info)
# #키값이 존재하면 value만 업데이트
# info["gender"] = "Male"
# print(info)
#
# #요소제거하기 : __delitem__(키값)
# info.__delitem__("gender")
# print(info)



#문제1.성적처리 프로그램
menu="""
*** 글로벌 학원 ***
1.학생정보 출력
2.학생정보 입력
3.학생정보 수정
4.학생정보 삭제
5.학생정보 검색
6.총점,평균
7.종료
"""

scores = {"이형우":100,"이근동":100,"조소연":98,"이근호":97,"허웅":96}

def stuInfoSys(scores):
    num = 0
    while True:
        print(menu)
        num = int(input("메뉴를 선택하세요."))
        if num == 1:
            infoPrint(scores)
        elif num ==2:
            infoInput(scores)
        elif num ==3:
            infoModify(scores)
        elif num ==4:
            infoDelete(scores)
        elif num ==5:
            infoSearch(scores)
        elif num ==6:
            totNavg(scores)
        elif num ==7:
            print("성적처리 프로그램을 종료합니다.")
            break

def infoPrint(scores):
     for i,j in scores.items():
         print("이름 : %s\t ㅣ\t점수 : %d" %(i,j))
     print()
def infoInput(scores):
    name = input("이름 입력 :")
    score = int(input("점수 입력 :"))
    scores.update({name:score})
    print("%s의 정보가 등록되었습니다." %name)
    print("이름 : %s\t ㅣ\t점수 : %d" %(name,scores[name]))
    print()
def infoModify(scores):
    name = input("이름 입력 :")
    if name in scores:
        score = int(input("수정할 점수 입력 :"))
        scores.update({name:score})
        print("%s의 점수가 %d로 수정되었습니다." % (name,scores[name]))
        print()
    else:
        print("학생 정보가 없습니다. 다시 입력해주세요.")
        print()
        infoModify(scores)
def infoDelete(scores):
    name = input("이름 입력 :")
    if name in scores:
        scores.__delitem__(name)
        print("%s의 정보가 삭제되었습니다." % name)
        print()
    else:
        print("학생 정보가 없습니다. 다시 입력해주세요.")
        print()
        infoDelete(scores)
def infoSearch(scores):
    name = input("이름을 입력하세요.")
    if name in scores:
        print("%s의 점수는 %d 입니다." %(name, scores[name]))
        print()
    else:
        print("%s의 정보를 찾을 수 없습니다." % name)
        print()
        infoSearch(scores)
def totNavg(scores):
    tot = 0
    avg = 0
    for i in scores:
        tot += scores[i]
    avg = tot/len(scores)
    print("총점: %d ㅣ 평균: %d" %(tot,avg))
    print()

stuInfoSys(scores)
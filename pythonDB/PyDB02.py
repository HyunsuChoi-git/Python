'''
*** 파이썬 - Oracle DB 연동 ***
# 라이브러리
    cx-Oracle(pycharm)
    cx_Oracle(pip)
'''
import cx_Oracle
#1. 전체 데이터 조회
def selectAll():
    connenction = cx_Oracle.connect("java17/java17@nullmaster.iptime.org:3000/orcl")
    cursor = connenction.cursor()

    sql = "select * from test"
    cursor.execute(sql)

    for record in cursor:
        print(record)

    cursor.close()
    connenction.close()

# 회원조회
def selectOne(tup):
    connenction = cx_Oracle.connect("java17/java17@nullmaster.iptime.org:3000/orcl")
    cursor = connenction.cursor()
    sql = "select * from test where id = :1"
    cursor.execute(sql,tup)
    print(cursor.fetchone())
    cursor.close()
    connenction.close()



#회원추가
def insertUser(tup):    #매개변수로 받을것, 회원정보 tuple 타입으로 넘겨받기
    connenction = cx_Oracle.connect("java17/java17@nullmaster.iptime.org:3000/orcl")
    cursor = connenction.cursor()
    sql = "insert into test values(:1, :2, :3, :4)" # 쿼리문자: place-holder ':숫자'
    cursor.execute(sql,tup)

    cursor.close()
    connenction.commit()    # 수동 커밋
    connenction.close()     #


#3. 데이터 개수 조회
connenction = cx_Oracle.connect("java17/java17@nullmaster.iptime.org:3000/orcl")
cursor = connenction.cursor()

sql = "select count(*) from test"
cursor.execute(sql)

count = cursor.fetchone()
print(type(count))
print(count[0])

#4. 비밀번호 수정
def updatePw(tup):
    conn = cx_Oracle.connect("java17/java17@nullmaster.iptime.org:3000/orcl")
    cursor = conn.cursor()

    sql = "update test set pw=:1 where id = :2"
    cursor.execute(sql,tup)

    # cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

#5. 데이터 삭제
def deleteUser(tup):
    conn = cx_Oracle.connect("java17/java17@nullmaster.iptime.org:3000/orcl")
    cursor = conn.cursor()

    sql = "delete from test where id = :1"
    cursor.execute(sql,tup)

    cursor.close()
    conn.commit()
    conn.close()
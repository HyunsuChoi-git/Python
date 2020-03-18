import cx_Oracle


#1. 전체 데이터 조회

connection = cx_Oracle.connect("java17/java17@nullmaster.iptime.org:3000/orcl")
cursor = connection.cursor()

sql = "select * from test"
cursor.execute(sql)

for record in cursor:
    print(record)

cursor.close()
connection.close()


#2. 1개 데이터 삽입

# import datetime
# connection = cx_Oracle.connect('java17/java17@nullmaster.iptime.org:3000/orcl')
# cursor = connection.cursor()
#
# sql = "insert into test values(:1, :2, :3, :4)"
# # 쿼리문자: place-holder ':숫자'
# data = ('test1', '1234', 10, datetime.datetime.now())
# # 매핑시킬 데이터는 튜플 형태로!
#
# cursor.execute(sql, data)
# cursor.close()
# connection.commit()
# connection.close()

#3.




import cx_Oracle
import sys

print("버전",sys.version)
#print(os.environ['ORACLE_HOME'])
import os
print("패치", os.environ['path'])

con = cx_Oracle.connect('java17/java17@nullmaster.iptime.org:3000/orcl')
print (con.version)

con.close()
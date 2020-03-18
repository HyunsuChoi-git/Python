from pythonDB import PyDB02 as dao
import datetime


#전체 조회
dao.selectAll()
#1명 조회
dao.selectOne(('test',)) #데이터를 tuple 형태로 던져주기
#회원 추가
#dao.insertUser(('python','1111',10,datetime.datetime.now()))
#dao.selectAll()
#회원 비번 수정
# dao.updatePw(('2222','python'))
# dao.selectOne(('python',))

dao.deleteUser(('python',))
dao.selectAll()
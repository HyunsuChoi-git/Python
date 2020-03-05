#﻿**kwargs

#packing : 낱개로 던져주는 키=벨류 형태의 데이터들을
#딕셔너리로 패킹해서 받아주는 형태
def packer(name=None,**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    for i , j in kwargs.items():
        print("%s는 %s입니다." %(i,j))


packer("피카츄",age="30",mob="010-1111-2222",city="seoul")

#unpacking : 딕셔너리를 던져주면 변수에 unpacking해서 받는 형태
def unpacker(name,score):
    print(name)
    print(score)

unpacker(**{"name":"피카츄", "score":30})
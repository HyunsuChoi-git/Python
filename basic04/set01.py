if __name__ == '__main__':
    sayHello()
    s1 = set([1,1,1,1,1,2,3,4,5,6,7])
    print(s1)
    s2 = set([3,6,8,9])

    #//교집합 :  &, intersection()
    print(s1 & s2)
    print(s1.intersection(s2))
    #// {3, 6}


    #//합집합 : |, union()
    print(s1 | s2)
    print(s1.union(s2))
    #//중복은 제거하고 두 집합을 묶는다.
    #//{1, 2, 3, 4, 5, 6, 7, 8, 9}

    #//차집합 : - , difference()
    print(s1 - s2)
    print(s1.difference(s2))
    #//{1, 2, 4, 5, 7}
    print(s2 - s1)
    print(s2.difference(s1))
    #//{8, 9}

    #//추가하기 : add()
    s3 = set([1,2,3])
    s3.add(4)
    print(s3)
    #//{1, 2, 3, 4}

    #//삭제하기 : remove(값)
    s3.remove(4)
    print(s3)

    #//{1, 2, 3}
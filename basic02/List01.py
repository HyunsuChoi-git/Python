'''
자료형
    숫자형     : int, float
    참/거짓형  : bool
    군집자료형 : str, list, tuple, dist, set
*** 리스트



'''

nums = [1,2,3,4,5]
print(nums) #[1, 2, 3, 4, 5]

strs = ["python", "class"]
print(strs) #['python', 'class']

suff = [1,2,"python","c",3.14]
print(suff) #[1, 2, 'python', 'c', 3.14]

#빈리스트
a = []
b = list()

print(type(a)) #<class 'list'>


#리스트는 인덱스 번호를 가지고 있다.
nums = [1,2,3,4,5]
print(nums)   # [1, 2, 3, 4, 5]
print(nums[0])  # 1
print(nums[3])  # 4
print(nums[-1]) # 5
#print(nums[10]) #IndexError: list index out of range

#리스트 안에 리스트를 넣을 수 있다.
num2 = [ [1,2,3], [4,5,6], [7,8,9] ]
print(num2[0]) # [1, 2, 3]
print(num2[0][0]) # 1

num3 = [1,2,3,[4,5,6],7]
print(num3[3][0]) #4
print(num3[2]) #3
print(num3[4]) #7


num4 = [1,2,3,["a","b","c"],4,5]
# [3,["a","b","c"],4] 출력
# ["a", "b"] 출력

print('[{},{},{}]'.format(num4[2],num4[3],num4[4]))
print('["{}","{}"]'.format(num4[3][0],num4[3][1]))

print(num4[2:5])
print(num4[3][0:2])


#list 는 수정이 용이하다

lst = [1,2,3]
lst[0] = 10
print(lst)  # [10, 2, 3]

lst = [1,2,3]
#인덱스 번호 1번의 요소를 'a','b','c'로 바꿔보자
lst[1] = ['a','b','c']
print(lst) # [1, ['a', 'b', 'c'], 3]

lst[1:2] = ['a','b','c']
print(lst) # [1, 'a', 'b', 'c', 3]

lst = [1,2,3]
lst[1] = 'a','b','c'
print(lst) # [1, ('a', 'b', 'c'), 3]
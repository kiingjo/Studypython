#자료형

from operator import truediv
from turtle import color


print(None)
print(type(None))

print(0==None)
a = None
print(a)
print(type(a))

#숫자형
금액 = '12_345_666'
print(type(금액))
print(금액)


#문자형
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)

bruce_eckel = 'Life is short, \n You need Python' # 줄바꾸기(새로운줄에 나옴)

bruce_eckel = '''Life is short, 
You need Python
배고파
머해''' #계속 줄바꾸기 하고싶을 때는 ''' 이걸로 !

#불형
val_sum = 1000
print(val_sum == 1000)
print(val_sum ==999)

bl_true = True
print(type(bl_true))
print(bl_true == True) # True
print(bl_true is True) # True

print(a is None) # True
print(val_sum is 1000) # True

# 의미가 있는 bool
print(bool(1)) # bool에서 1은 참,true
print(bool(0)) # 0은 거짓, false

# list
b = [1,2,3,4,5,6,7,8,9]
print(b)

arr2 = ['Life','is','short','U','need','Python',3] #들어가 값을 반복적으로 사용해야할 때!
print(arr2[0])

arr3 = [[1,2,3],[4,5,6]] #2x3행렬로 나타남
print(arr3)

arr4 = list() #빈리스트 생성 none이 아니다!!!
print(arr4)

# 튜플 : 튜플 내의 값은 수정, 추가 불가!! 리스트는 가능
tuple1 = (1,2,3,4,5)
print(tuple1)

# 딕셔너리
spiderman = {'name' : '피터파커',
            'age' : 18,
            'weapon' : '웹슈터'}
print(spiderman)
print(type(spiderman))
print(spiderman['name'])





                
color = ['red', 'green', 'yellow']
color.append('white') #추가되는것
print(color)
print (color[0]) #인덱스주소
color.insert(0,'orange') #특정주소에 추가하는 법
print(color)
color.remove('green')
print(color)


# 행렬식으로 나타내서 주소 사용해서 나타낼 수 있다.
kor = [60,70,80,90]
eng = [53,77,90,92]
math = [26,45,85]

시험점수 = [kor,eng,math]
print(시험점수)
print(시험점수[0][0] + 시험점수[1][0])



    
    


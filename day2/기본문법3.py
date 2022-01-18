#파이썬의 변수 : 파이썬의 변수에는 제약이 거의 없다.
a = '헬로우'
print(a)

a = 3.141592
print(a)

a = 10
print(a)

a = 9999999999
print(a)

# 변수값을 지정(할당) - assign방법
# 변수는 값을 담을 수 있는 통, 단 숫자는 변수로 지정할 수 없다.
a = 3
b = 3.141592
c = 'python'
d = (1,2,3) #튜플
e = [1,2,3,4]
f = [7, '8', '$', a] #파이썬의 장점 뭐든지 담을수 있다!

# 변수명 지정 불가
val = 10
val2 = 2
val12 = 20
val14 = 30
#4val = 40 #숫자로 시작하는 변수 안된다
#* =  5 #특수문자 변수 안된다
var_of_chane = 99
#val& = 15 #특수문자는 어디에도 들어가면 안된다
val = 999
Val = 9080 #대소문자 구분한다 서로 다른 변수

print(val)
print(Val)

My_Account_Of_Bank = 100
은행계좌금액 = 1

#변수 위치 확인
print(id(val))
print(id(Val))

#변수타입 확인
print(type(val)) #int
print(type(c)) # str
print(type(d)) # tuple
print(type(e)) #list
print(type(f)) # list



#예제)
print("변환하고 싶은 섭씨온도를 입력해주세요")
a=float(input())
화씨 = float(1.8*a +38)

print("화씨온도 :", 화씨)


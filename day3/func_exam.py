# 함수 선언 및 사용

# 더하기 함수 선언
def add(a, b):
    res = a + b

    return res

# 함수 사용
print(add(24786, 4324))

mid_val = add(3, 4)
print(mid_val * 3)

# 함수종류
# 매개변수(입력값) 없는 형태
def say_hello(): #return 으로 되돌려서 say_hello가 Hello~로 바꾼다
    return 'Hello~'

print(say_hello())
print(say_hello(), 'my friend')

# 결과값이 없는 형태
def say_hello(name):
    print(f'Hello~ {name}')
    return none
# 둘 다 없는 경우
def say_goodbye():
    print('Bye bye~')
say_goodbye()

# 매개변수 지정
def multi(a,b): #함수를 사용하기위한 타이틀
    return a * b #함수가 어떻게 사용되는지
print(multi(8,9))

#매개변수 개수가 가변적일 때
def plus(*args):
    res = 0
    for i in args:
            res += 1

    return res

print(plus(1,2,3))


# 리턴값이 두개이상
def mul_and_div(x,y):
    mul = x*y
    div = x/y

    return (mul, div) #튜플

(res1, res2) = mul_and_div(7, 8)
print(res1, res2)

#한번에 계산 가능한 사칙연산
def 사칙연산(x,y):
    return(x+y, x-y, x*y, x/y)

res1, res2, res3, res4= 사칙연산(9,5)

print(res1, res2, res3, res4)

print(type(사칙연산(1,2)))



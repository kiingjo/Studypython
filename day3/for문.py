# 기본 for 문 : for는 계속 반복문

arr = [1,2,3,4,5]

for i in arr:
    print(f'{i:0.2f}') #2는 소숫점 둘째자리까지 나타내는 것 


print('---따로 형식 안주고 바로 쓰는법')
for i in range(1,6): # i는 item 이라는 뜻 그냥 줄여 쓰는것
    print(f'{i:0.2f}입니다') #형식 주는 방법

# 튜플로 for 문
arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2:
    print(f'{item:>10}') # 우측정렬 하는법

# 합계 for 문
numbers = list(range(1,101)) #1~100 까지 즉 홀,짝수 계산도 가능
res = 0
for i in numbers:
    res += i
print(f'{numbers[-1]}까지의총 합은 {res} 입니다.')

#짝수 합계 출력
numbers = list(range(2,21,2)) #1~20까지 짝수
res = 0
for i in numbers:
    res += i
print(f'{numbers[-1]}까지의총 합은 {res} 입니다.')



# 홀수 짝수 구분
numbers = list(range(1,21)) #1~20까지

for i in numbers:
    if i % 2 == 1: # 홀수
        print(f'{i}는 홀수입니다')

# 13이상이면 탈출(break), 계속(continue)
numbers = list(range(1,21)) #1~20까지
for i in numbers:
    if i >12: 
        break #중단하고 싶다 #break는 웬만하면 먼저 1차 방어선처럼 걸러줘라 #for문자체를 빠져나가는것

    if i % 2 == 1: # 홀수
        print(f'{i}는 홀수입니다')

numbers = list(range(1,21)) #1~20까지
for i in numbers:
    if i ==15: 
        continue #하위의 if 수행하지않고 위로 올라가서 다음 for 문 실행

    if i % 2 == 1: # 홀수
        print(f'{i}는 홀수입니다')


# # 구구단 만들기
# print('구구단 몇단을 실행할까요?') 
# a = int(input())
# while a<=0 or a>10:
#     a = int(input('0~9까지 숫자를 입력해주세요'))

# for i in range(1,10):
#     print(f'{a}X{i}={a*i}')
    
# 구구단 프로그램
for i in range(1,10): #1~9
    print(f'{i}단')
    for j in range(1,10):
        print(f'{i}X{j}={i*j:2d}',end='  ')
    print('')






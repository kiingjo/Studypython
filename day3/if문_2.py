# 중첩 if
x = int(input())

if x > 0: #if 만족하는 문 내에서 if를 하나 더 생성
    print('양수')
    if x >9:
        print('10보다 큰수')
    else :
        print('10보다 작은수')

elif x == 0:
    print('0')
else:
    print('음수')


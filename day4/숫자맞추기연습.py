# 숫자맞추기

import random
a = random.randint(1,100)
b = int(input('숫자를 알아맞춰보세요.'))
while b < 1 or b >100:
    b = int(input('1~100중의 정수만 입력해주세요.'))
while a is not b:
    if a > b:
        print('숫자가 너무 작습니다')
    elif a < b:
         print('숫자가 너무 큽니다')
    b = int(input('숫자를 다시 입력해주세요'))
if a == b:
    print(f'정답입니다. 숫자는 {a}입니다.')

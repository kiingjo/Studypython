import random
a = random.randint(1,100)

b = int(input('숫자를 알아맞춰보세요(1~100)'))
while a is not b:
    if a>b:
        print('숫자가 너무 큽니다')
    else:
        print('숫자가 너무 작습니다')
    b = int(input(''))
else:
    print(f'정답입니다. 숫자는 {a} 입니다.')





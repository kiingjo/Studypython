# exception_handle.py
# 예외처리!! 가장중요!!!

from logging import exception

## 얘네들은 그냥 함수선언이다.
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return a / b

print('사칙연산 시작')
a, b = 4, 1
numbers = [3,6,9] #리스트 생성

try: # 예외발생
    print(f'나누기 결과 : {divide(a, b)}') # 예외는 실행을 해야 나오는 것이다. 빨간 밑줄이랑은 다르다
    res = int(numbers[1]) * 8
    num = int(input('수를 입력하세요'))
except ZeroDivisionError as e: # Exception # 걍 예외 될거같은애들 전부 예외로 둔다.
    print(f'나누기 예외. 추가처리1 {e}') # try,except 짝지
except IndexError as e:
    print(f'인덱스 예외. 추가처리2{e}')
except ValueError as e:
    print(f'제발! 숫자만 넣으라고!!')

except Exception as e:
    print(f'알수없는 예외. 추가처리{e}')
finally:
    print(f'곱하기 결과 : {multi(a, b)}')
    print(f'빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')
print('사칙연산 종료')


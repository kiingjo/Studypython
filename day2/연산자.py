#연산자 숫자는 사칙연산 다 된다
a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) #몫만 출력
print(a % b) # 나머지만 출력

#문자열 연산
stat1 = 'Hello'
stat2 = 'World'

print(stat1,stat2) # 콤마(,)는 두개를 나열할 것으로 한칸 띄어서 나옴.
print(stat1 + stat2) # 문자열 두개를 합친 것이다.
#print(stat1-stat2) #문자열엔 빼기 없음
print(stat1 *4)
#print(stat1/stat2) #나누기 없다.
#print(stat1/3) #역시 없다.

# 문자열 길이
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스, 리스트와 동일한 작업
print(stat3[0])
print(stat3[1])
print(stat3[2])
print(stat3[3])
print(stat3[4])
    #print(stat3[5]) ##예외발생 stat3 = 안녕하세요 즉 인덱스 [0,4]까지!
print(stat3[-1]) #역으로 본다
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])

#문자열 자르기
일시 = '2022-01-17 14:39:25'
print(일시[:4], '년') #다음 범위에 겹칠수도있으니까 4가 아니고 3까지다
print(일시[5:7], '월')
print(일시[8:10], '일')
print(일시[11:],'시간') #11부터 끝까지
print(일시[-5:-3]+ '분')

stat4 = '저리가' + stat3[3:]
print(stat4)

list_a = [1,2,3,4,5]
list_a[1] = 19
print(list_a)

color = ['red', 'green', 'blue']
color.extend(['black','smoke gray']) #리스트 자체를 추가 해줄 수 있다.
color.insert(0,'yellow') # 인덱스 0번 주소에 yellow 삽입
print(color)

##문자열 포맷팅 ##항상 쓰는 패턴을 효율적으로 쓸 수 있도록!
첫째 = 2
둘째 = 'you'
str1 = "I'm so happy {0} U. aren't {1}?".format(첫째,둘째)
print(str1)
str1 = f"I'm so happy {첫째} U. aren't {둘째}?" # 현재 가장 효율적인 포맷팅 방법
print(str1)

#천단위 기호 넣는법
money = 100000000000000
print(format(money,',d')) 

from datetime import datetime

now = datetime.now() # 현재일시 생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S')) #포맷형식 기억!!!

import math

Mypi = math.pi
print(Mypi)

print('{0}'.format(Mypi))
print('{0:0.2f}'.format(Mypi)) #소숫점 두번째까지 Mypi가 들어간다!
print(f'{Mypi:0.2f}') # 현재 사용되는 포맷팅 스타일

full_name = 'hugo mg sung'
age = 47
greeting = '''안녕하세요. 저는 {0}입니다. 
나이는 {1}살이구요.'''.format(full_name,age) #문자열포맷팅

print(greeting)

greeting = f'''안녕하세요. 저는 {full_name}입니다.
나이는 {age:0.2f}살이구요''' # 최근 포맷팅

print(greeting)

# 문자열 자르기
part_name = full_name.split(',') # 콤마로 나누는 거 
part_name = full_name.split('|') # |로 나누는것

print(type(part_name))
print(part_name)

# 단어교체 replace
print(full_name.replace('hugo mg', 'kwangjo'))

# strip == oracle TRIM과 동일
aaa = '     Hello, world     '
print(aaa.lstrip()) # 좌측 공백 없애주는거 
print(aaa.rstrip()) # 우측 공백
print(aaa.strip()) # 전체공백

print(full_name.index('h')) #0
print(full_name.index('u')) #1
print(full_name.index('g')) #2
print(full_name.index('o')) #3

# print(full_name.index('x')) #full_name 내에 x가 존재하지 않는다

print(full_name.find('X'))
print(full_name.find('mg')) #mg가 시작되는 첫 인덱스 주소는 5

print(full_name.upper()) # 전부 대문자로
print(full_name.lower()) # 전부 소문자 #오라클에 concat은 없다





























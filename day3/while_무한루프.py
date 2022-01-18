# #무한루프
# val = 0
# while 1==1: #조건을 무조건 맞는 논리식을 써준다 or while True
#     val +=1
#     print(val)



##회원정보 프로그램 간편화(무한루프)

print('회원정보프로그램')

while True:
    print(''' 작업할 번호를 입력하세요
    1. 회원입력
    2. 회원검색
    3. 회원수정
    4. 회원삭제
    5. 종료

    숫자입력 : ''',end='')

    val = int(input()) #input의 기본은 str이다 숫자여야하니까 int
    while val > 5:
        val = int(input('1~5숫자만 입력해주세요'))
    if val ==1:
        print('회원정보화면으로 전환')
    elif val==2:
        print('회원검색화면으로 전환')
    elif val==3:
        print('회원수정화면으로 전환')
    elif val==4:
        print('회원수정화면으로 전환')
    elif val==5:
        break
print('회원정보프로그램 종료')


            



    


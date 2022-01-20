# 커서에 접근하는 코드를 함수로 작성
import cx_Oracle as ora

def myconn(): 
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') #dsn(매개변수 소스)이 길어서 미리 만들어주고 
    conn = ora.connect(user = 'scott', password = 'tiger', dsn=dsn, encoding = 'utf-8')
    return conn # '오라클에 접속해라'라는 함수 선언


def getALLData(conn): # conn객체를 매개변수 받아서 쿼리를 실행할 함수
    cur = conn.cursor() # 커서 생성
    query = 'select * from emp' # emp 테이블에서 데이터 모두 가져와라
    for row in cur.execute(query): # emp테이블의 최상단에 커서 위치하고 모든데이터를 
        print(row) # 한줄씩 출력


def getNameAndJobData(conn): # ename, job 두개 컬럼만 쿼리 실행하는 함수
    cur = conn.cursor()
    query = 'select ename, job from emp' # enp테이블에서 2개의 컬럼 가져와라
    for row in cur.execute(query):
        print(row)

def getNameAndJobData2(conn): 
    cur = conn.cursor()
    query = 'select ename, job from emp' # enp테이블에서 2개의 컬럼 가져와라
    cur.execute(query) #실행
    while True: # 위의 함수선언에서 for문을 While문으로 바꾼 것!
        row = cur.fetchone() # fetchone : 한 row(레코드) 읽기 #while문 거치면 break 되기 전까지 쭉 읽어온다.
        if row is None:
            break
        else:
            print(row)

def getDeptName(conn, num): # 원하는 부서번호에 한정된 데이터를 뽑는 함수
    cur = conn.cursor()
    query = f'Select * from dept where deptno = {num}' # :1 (1번이 아니고 매개변수) 적는 이유는 그냥 파이썬의 문법이다.
    cur.execute(query)
    row = cur.fetchone() # 원하는 한줄만 가지고 온다.
    print(row)


def getDeptName2(conn, num, loc): #원하는 부서번호, 지역 두가지 다 만족하는 데이터를 뽑는 함수
    cur = conn.cursor()
    query = f"Select * from dept where deptno = {num} and loc = '{loc}'" # loc형식이 문자이기 때문에 따옴표 붙여줘야 한다.
    cur.execute(query)
    row = cur.fetchone() 
    print(row)

def getDeptName3(conn, tup): # num, loc, a, b, c 이렇게 많을 경우 튜플(tup)을 이용해서 간편화
    cur = conn.cursor()
    query = f"Select * from dept where deptno = {tup[0]} and loc = '{tup[1]}'"  # loc는 문자이기에 따옴표 적어야 한다.
    cur.execute(query)
    row = cur.fetchone() 
    print(row)

def getDeptName4(conn, tup): ###끝판왕
    cur = conn.cursor()
    query = 'Select * from dept where deptno = :1 and loc = :2' # type 구분할 필요도 없고 그냥 할당만 해주면 된다. 오라클 인덱스 number순으로 생각해준다
    cur.execute(query,tup) 
    row = cur.fetchone() 
    print(row)






if __name__ =='__main__' : # 언더바 2개씩 ####서로간의 약속: 위에 아무리 코드가 많아도 프로그램 실행은 여기부터 시작!
    print('프로그램 시작')
    # 함수 호출
    scott_con = myconn() # dsn, connect() 후 접속객체 conn 리턴 

    print('emp 테이블 전체 조회(select *)')
    getALLData(scott_con) # conn이 매개변수 scott_con이다

    print('emp 2개 컬럼 조회')
    getNameAndJobData(scott_con)

    num = input('검색할 부서번호를 입력하세요.')
    print(f'{num} 번호의 부서명')
    getDeptName(scott_con, num)

    num = input('검색할 부서번호를 입력하세요:')
    loc = input('지역명을 입력하세요:')
    print(f'부서번호 : {num}, 지역 : {loc}')
    getDeptName2(scott_con, num, loc.upper()) # 지역명을 소문자로 적었더라도 대문자로 바껴서 선언한 함수로 들어간다!

    num = input('검색할 부서번호를 입력하세요:')
    loc = input('지역명을 입력하세요:').upper() # 애초에 input에서 upper 적으면 input 받은다음 변환해서 함수로 들어감
    tup = (num, loc)
    print(f'부서번호 : {num}, 지역 : {loc}')
    getDeptName3(scott_con, tup)

    num = input('검색할 부서번호를 입력하세요:')
    loc = input('지역명을 입력하세요:').upper() 
    tup = (num, loc)
    print(f'부서번호 : {num}, 지역 : {loc}')
    getDeptName4(scott_con, tup)



    print('프로그램 종료')
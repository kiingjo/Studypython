# bookrentalshop
# divtbl, membertbl

import cx_Oracle as ora

def myconn(): 
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') 
    conn = ora.connect(user = 'scott', password = 'tiger', dsn=dsn, encoding = 'utf-8')
    return conn

def getalldata_from_divtbl(conn):
    cur = conn.cursor() # 커서생성
    query = 'select * from divtbl' # 원하는 쿼리
    
    for row in cur.execute(query): # 쿼리 제일 위에 커서 두고 데이터를
        print(row) # 한줄씩 읽어온다.

def setdata_into_divtbl(conn,tup): # SQL에서 insert하는 것을 파이썬에서 조작하기 위한 함수
    cur = conn.cursor()
    query = '''INSERT INTO divtbl (division, names) 
                VALUES (:1, :2) '''
    cur.execute(query, tup)
    cur.close()
    conn.commit() # insert작업해줬으면 commit 동반자 필수!!!!!


def getsomedata_from_membertbl(conn): # 데이터 가지오 온다
    cur = conn.cursor() # 커서생성
    query = '''SELECT names, levels, addr, mobile, email 
            FROM membertbl
            WHERE addr LIKE '서울%'
            AND UPPER(email) LIKE '%@NAVER.COM'
            ORDER BY idx DESC'''
    
    for row in cur.execute(query): # 쿼리 제일 위에 커서 두고 데이터를
        print(row) # 한줄씩 읽어온다.

    cur.close() # 원래는 커서 실행한다음에는 cur.close()해줘야 한다

def setnewmember_into_membertbl(conn,tup):
    cur = conn.cursor() # 실행하기 위해서 필요한 것: 커서
    query = '''SELECT ROWNUM, idx
            FROM (
                SELECT idx FROM membertbl
                ORDER BY idx DESC  
                    ) 
            WHERE ROWNUM = 1'''
    cur.execute(query)
    idx = cur.fetchone() # 한줄씩 받아온다.
    if idx is None:
        idx = 0
    else:
        idx = idx[1] # 인덱스 1은 오라클이니까!

    intup = (idx +1, tup[0], tup[1], tup[2], tup[3]) # 얘들은 input으로 받는다 
    
    query = '''INSERT INTO membertbl 
            (idx, names, levels, userid, password)
        VALUES (:1, :2, :3, :4, :5)'''
    cur.execute(query, intup)
    
    conn.commit()

def setchangemember_from_membertbl(conn,tup): #업데이트
    cur = conn.cursor()
    query = '''UPDATE membertbl 
            SET addr = :1
                , mobile = :2
                , email = :3
            WHERE idx = :4''' # 조건문에 idx가 들어가니까 튜플 가장 마지막에 적는다.
    cur.execute(query,tup)
    conn.commit()

def delete_division(conn, division):
    cur = conn.cursor()
    query = 'Delete from divtbl where division = :1'
    cur.execute(query,(division,))
    # 데이터가 하나면 튜플로 변경 ,(콤마) 반드시 추가할것!!!
    conn.commit()

def delete_division2(conn, division): # 위의 delete 의 다른표현 매개변수가 한개일때는 !!!
    cur = conn.cursor()
    query = f"Delete from divtbl where division = '{division}'"
    cur.execute(query)
    # 데이터가 하나면 튜플로 변경 ,(콤마) 반드시 추가할것!!!
    conn.commit()
    




if __name__=='__main__':
    
    # 함수 호출하기
    scott_con = myconn()

    # 1. divtbl에서 데이터 조회
    
    print('책 장르 정보조회')
    getalldata_from_divtbl(scott_con)
    
    # 2. divtbl에 새로운 데이터 입력
    print('책 장르 정보입력')

    division = input('구분코드 입력:')
    names = input('장르명 입력:')
    tup = (division,names)
    setdata_into_divtbl(scott_con,tup)

    print('정보 입력 성공')


     # 3. membertbl에서 데이터 조회

    print('회원정보 조회')
    getsomedata_from_membertbl(scott_con)

    # 4. membertbl에 새 데이터 입력
    print('신규회원 입력')
    names = input('회원이름 입력:')
    levels = input('레벨입력(A~D)')
    userid = input('id입력(최대 20자):')
    password = input('패스워드입력(최대 20자):')
    tup = (names, levels, userid, password)

    setnewmember_into_membertbl(scott_con,tup)

    print('성공!')

    # 5. membertbl 새 데이터를 수정

    print('기존회원 수정')
    idx = input('변경회원 번호:')
    addr = input('주소입력 :')
    mobile = input('폰번호입력(-포함):')
    email = input('이메일 입력:').upper()
    
    tup = (addr, mobile, email, idx) # idx를 가장 마지막에 넣는다
    setchangemember_from_membertbl(scott_con,tup)
    print('기존 회원 수정완료')


    # 6. divtbl에 임의 데이터 삭제

    print('책장르 정보 삭제')

    division = input('삭제 할 장르코드 입력:')
    delete_division(scott_con,division)
    print('삭제완료')

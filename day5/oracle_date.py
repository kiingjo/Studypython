# oracle date
# cx_oracle 설치 : pip install cx-oracle
import cx_Oracle as ora 

# makedsn('호스트명/ip주소', 포트번호, '서비스명')
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')

# connect(user, password, dsn, encoding )
conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')

cur = conn.cursor() #원하는 데이터(테이블)의 가장 위에 커서 존재

try:
    for row in cur.execute('select * from emp:'): #세미콜론 들어가면 안되는데 들어갔다 예외처리해서 오류를 정상화시키자.
        print(row) # for문은 범위를 싹다 때리고 빠져나간다
    # cur.execute('select count(*), \'sample\' from emp') # 확인하기 위해 한줄만 가지고 오는 것
    # result = cur.fetchone()
    # print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 14번라인 확인요 : {e}')
finally:
    cur.close()  # 커서 닫고
    conn.close() # 접속 닫음
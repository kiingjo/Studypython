# # 파일 입출력

# # 파일 출력
# f = open('newfile.txt', 'w') # w : write r : read
# f.close() # open 했으면 무조건 close 해야한다!!!!!!

# 특정경로에 파일 생성
f = open('C:\\Sources\\Sample/test2','w') # 왜 \두번하지?
f.close()
print('파일이 생성되었습니다')

# newfile.txt 파일입력(읽어오기) -> 출력이 아니라 입력이다!!!
f = open('newfile.txt','r',encoding = 'utf-8') #newfile을 읽어오는데 인코딩을 utf-8로 한다
while True: #무한반복
    line = f.readline() # f의 내용을 한줄씩 읽어오는 것을 line에 할당
    if not line: ### 이 문법을 사용하자 
        break


    print(line)
f.close()

# print(line)
lines = f.readlines()
for line in lines:
        print(line)

f.close()
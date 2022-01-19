# 부산버스 노선별 이용건수 
# 파일 불러오는 방법
import csv
from encodings import utf_8

file_name = '부산버스정보.csv'
f = open('부산버스정보.csv', mode = 'r', encoding = 'utf_8')

reader = csv.reader(f, delimiter =',')
next(reader) # 헤더를 없애는 역할

for line in reader:
    print(line)

f.close()


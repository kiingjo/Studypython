# 리스트 연산
arr = list(range(5)) # 0부터 4까지
print(arr)

arr = list(range(1,6)) # 1부터 5까지
print(arr)

arr = list(range(2,101,2)) #원하는 숫자부터, 숫자+1까지, 텀
print(arr)

print(arr[0] + arr[5]) # 2 + 12

# 2차원 배열(리스트)
arr2 = [1,2,['HI', 'My', 'Friend']]
print(arr2[0])
print(arr2[1])
print(arr2[2])
print(arr2[2][1]) # 첫번째 2번째 인덱스중 1번째니까 My
print(arr2[2][1][0]) # My 단어중 인덱스 0주소니까 M


arr3 = list(range(1,4))
print(arr3)
print(arr3*3) #배열 3번 더 한다

# 리스트 함수
del(arr3[1]) # 인덱스 주소값으로 지우는 것
print(arr3)
arr3.remove(1) # 요소 자체를 없애는 것(최초의 요소만 없애줌)
print(arr3)

arr3.append(4) #요소 추가해주는 것
print(arr3)

arr3.extend([5,6,7]) # 리스트를 추가해주는 것
print(arr3)

del(arr3[3]) # 인덱스번호 3에 지워진다
print(arr3)

arr4 = [4,2,6,9,12,16,7,1,3,3,5]
arr4.sort() #작->큰 순서로
print(arr4)

arr4.reverse()
print(arr4)

arr4.insert(2,10) #두번째 인덱스 주소에 10 넣는다
print(arr4)

tup1 = tuple(range(1,6))
print(tup1)

#tup1[0] = 108 #tuple은 값을 할당하거나 안된다
print(tup1)

# 딕셔너리
dic1 = {1:'a'}
dic1[2] = 'b' #딕셔너리는 요소를 계속 추가할 수 있다
print(dic1)

dic1['name'] = '광조' #키요소를 이름으로 해줘도 상관없다 굳이 숫자 아니어도 됨!
print(dic1)         # 리스트에는 어떤문자 타입이 들어오든 상관없다

del dic1['name'] # 삭제할 때는 인덱스주소가 아닌 키요소를 적어준다
print(dic1)  

print(dic1.keys()) # 키요소
print(dic1.values()) # 키에 대한 value 요소
print(dic1.items()) # 키, 요소 둘다!

# 리스트를 튜플로 변환
print('---리스트를 튜플로 변경')
print(arr4) #이건 리스트타입
tup2 = tuple(arr4) #튜플로 변환
print(tup2) #튜플로 변환

arr5 = list(tup2)
print(arr5)
arr5.append(100) #리스트로 변환하고 나서는 수정이나 추가 할 수 있다!! 이를 활용
print(arr5)
tup5 = tuple(arr5)
print(tup5)






















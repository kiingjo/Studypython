# List comprehensions
#기존 List를 사용하여 간단히 다른 List를 만드는 기법 (for문 없이 새로운 list 생성 가능)

# for문 사용해서 리스트 만들기 # 로또번호 res에 넣고싶다면 []하고 생성
res = []

for i in range(10):
    res.append(i)

# 바로 리스트 만들기
res = list(range(10))
print(res)


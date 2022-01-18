# while문
hit = 0

while hit < 10: #이 while문의 값이 참인 동안
    
    hit += 1 # hit= hit +1 이랑 같은 문법

    if hit>10:
        break
    
    print(f'나무를 {hit}번 찍었습니다.')
print(f'{hit}번 찍혔으므로 넘어갔습니다.')

#for문으로 변경

for hit in range(1,101):
    if hit > 9:
        break

    print(f'나무를 {hit}번 찍었습니다.')
print(f'{hit}번 찍었기에 넘어갔습니다.')


    


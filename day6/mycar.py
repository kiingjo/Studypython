# mycar.py

from vehicle import Car

if __name__ == '__main__':
    mycar = Car('98하 5678', '흰색')
    # mycar.차량번호 = '98하 5678'
    # mycar.색상 = '흰색'
    mycar.연료 = '경유'
    mycar.__제조사 = '쌍용'
    mycar.출고년도 = 2018
    
    mycar.set제조사('쌍용')
    mycar.제조사확인()

    mycar.전진한다()
    print(mycar)


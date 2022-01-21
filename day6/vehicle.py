# vehicle.py

class Car:
    차량번호 = '22나 1956'
    __제조사 = '현대'
    색상 = '흰색'
    연료 = '가솔린'
    출고년도 = '1990년'

    def __init__(self, 차량번호, 색상) -> None: # 업데이트를 위한 장치라고 생각
        self.차량번호 = 차량번호
        self.색상 = 색상

    def __str__(self) -> str: # print(car) 했을 때 나오는 것에 대한 함수
        return f'제 차는 {self.출고년도}년도에 만들어진 {self.연료}차량입니다.'


    # private(__제조사 이건 다른 페이지에는 쓸수 없다.) 이 과정을 거쳐줘야지 다른페이지에서도 사용가능
    def set제조사(self, 제조사):
        self.__제조사 = 제조사

    def 제조사확인(self):
        print(f'제조사 {self.__제조사}')





    def 전진한다(self):
        print(f'{self.색상}차가 앞으로 달린다.')

    def 후진한다(self):
        print('뒤로 달린다')

    
    def 죄회전한다(self):
        print('왼쪽으로 달린다')


    def 우회전한다(self):
        print('오른쪽으로 달린다')


    def 멈춘다(self):
        print('멈춘다')


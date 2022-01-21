# Person.py
# Person 클래스

from imp import new_module


class Person:  # Person의 특성을 나타냄 (클래스)
    
    name = ''
    age = 0 
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''
    
    # 생성자 # __init__을 통해서 하나의 객체 즉 kkj를 만들었다.
    def __init__(self, name, age, height, gender) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        print('Person이 생성되었습니다.')

    # 동사로 시작할 때는 무조건 self가 있어야한다!!
    def 소개한다(self): 
        greeting = f'''안녕하세요. 저는 {self.name} 입니다.
        {self.gender}이구요. {self.age}살입니다.'''

        print(greeting)



    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다.')

    def 일한다(self, drink): # 행위를 나타낼 때는 self 붙여줘야 한다.
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다')

    #pass # 일단 패스 넘긴다는 뜻 오류가 발생되진 않는다.


if __name__ == '__main__':
    # p = Person() # p라는 이름의 Person 객체 생성
    # print(type(p))
    # print(id(p)) # id 값

    # p2 = Person() # p2 객체 생성
    # print(type(p2))
    # print(id(p2))
    kkj = Person('김광조', 46,174, '남') # == __init__(self, name, age):
    # kkj.name = '김광조'
    # kkj.age = 27
    # kkj.height = 174
    # kkj.gender = '남'
    kkj.feetsize = 270
    kkj.bloodtype = 'O형'

    kkj.소개한다()
    kkj.먹는다('본죽')
    kkj.일한다('핫식스')



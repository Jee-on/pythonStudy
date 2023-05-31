"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

""" 
자바인 경우 
class Sample {
     String data = "Hello";
     String name;
     Sample(String name){
          this.name = name;
     }
}
Sameple s = new Sample("홍길동");
"""

class Sample:
     data = 'Hello'
     # 생성자
     def __init__(self, name):
          self.name = name
          print('__init__호출')
     # 소멸자 함수
     def __del__(self):
          self.name = ''
          print('__del__호출')

s = Sample('홍길동')
print(s.data)
print(s.name)
del s
print('프로그램 종료')


"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
"""

class Book:
     cnt = 0
     def __init__(self, title):
          self.title = title #멤버변수 따로 선언해줄 필요없음
          self.cnt   += 1
     
     def output(self):
          print('제목: ' ,self.title)
          print('총 개수:', self.cnt)
     
     @classmethod
     def output2(cls):
          cls.cnt += 1
          print('총 개수:', cls.cnt)
          
     
b1 = Book('행복이란')
b2 = Book('먹고살자')

b1.output()
b2.output()
print('-'*100)

b1.output2()
b2.output2()



'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''

class Animal:
     def move(self):
          print('동물은 움직인다')

class Wolf(Animal): # 상속관계
     def move(self): # 부모와 같은 이름의 함수를 쓰면 오버라이딩
          print('늑대는 4발로 뛴다')

wolf = Wolf()
wolf.move()

class Human(Animal):
     def move(self):
          print('인간은 2발로 걷는다') 

hu = Human()
hu.move()

class WolfHuman(Human, Wolf): # 부모를 둘 지정해줄수 있다, 
     pass                     # 둘다 같은 함수가 있을땐 먼저 기술된 부모의 함수 이용

wh = WolfHuman()
wh.move()

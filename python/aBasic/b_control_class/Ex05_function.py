"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

# (1) 인자도 리턴값도 없는 함수
def func():
    print('inside func')
    return 'OK'

func()
result = func()
print(result)

# (2) 위치인자 ( positional argument)
def func(greeting, name):
    print(name,'님',greeting,'!!!')
func('하이','철수')
func('영희','안녕')

# (3) 키워드인자 (keyword argument)
func(name='영희',greeting='안녕')

# (4) 매개변수의 기본값
# func('헬로우') 에러 인자 개수 따짐
# func('헬로우','홍길동','안녕') 에러

def func(greeting, name='아무개'):
    print(name,'님',greeting,'!!!')
func('헬로우')
func('안녕','홍길동')

def temp(a=0,b=0,c=0):
    return a*2+b*3+c*4

print(temp(1,2,3))
print(temp(c=1,a=2,b=3))
print(temp(1,2))
print(temp(1))


'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''
def func(a,b,c=0, *args):
    sum =a + b + c
    for i in args:
        sum += i
    print(args)
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))

"""
(6)
"""
def func(a,b,c=0, *args,**kwargs):
    sum =a + b + c
    for i in args:
        sum += i
    for k in kwargs:
        sum += kwargs[k]
    print(args)
    print(kwargs)
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
print(func(4, 5, 6, java=100,kor=50, math=60))
print(func(4, 5, 6, 7,8,java=50,kor=70))


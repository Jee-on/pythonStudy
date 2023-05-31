"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            pass #실행할 코드가 없을떈 pass를 적어줘야함 , 공백 X
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None


print(type(i))

a = 0
if a :
    print('T')
else :
    print('F')
    

a= 10
b= -1
c= 0
if a and b:
    print('True2')
    
if a or b:
    print('True3')  

print( a and b) # and는 앞 값이 true -> 뒷값에 의해 결정되므로 -1 
print( a or b ) # or는 앞 값이 true -> 앞의 값에 의해 결정되므로 10
print( c and a )

a = 100
if a:
    z = 1
else:
    z = -1
    print('z',z)   #

a = 10
if a:
    print('A')
print('B')
print('C')

word = 'korea'
# 'korea' 단어 중에 'k' 글자가 있으면 'ok' 출력 없으면 'no' 출력
""" if word.find('')==0:
    print('ok')
else:
    print('no')
print(word.find('g')) """


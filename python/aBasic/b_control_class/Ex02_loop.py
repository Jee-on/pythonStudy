
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e.items(): # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry[0], '-' , entry[1])
else:
    print('끝')

for key, value in e.items(): # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(key, '-' , value)
else:
    print('끝')


li = ['z','y','x']
while li:
    data = li.pop()
    print(data)
    #[java] if( ) break; 필요
    if data == 'y':
        break #중간에 직접 break 하면 else문 실행되지 않음
else:
    print('끝')
    
"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
a = [1,2,3,4,5,6,7,8,9]
for i in a[1:]:
    for y in a:
        print('[',i,'단]',i,'X',y,'=',i*y)
else:
    print('끝')
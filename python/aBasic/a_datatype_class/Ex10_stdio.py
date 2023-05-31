"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""


#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력

""" name = input('이름 입력->')
age = int(input('나이 입력 -> '))
tall = float(input('키 입력 -> ')) # eval float 둘다가능

print('당신의 이름은 {}, 나이는 {}살 이고, 키는 {}cm입니다'.format(name,age+1,tall))

print(type(age))
print(type(tall))

print(eval('1+2')) # 문자열도 실행시킴 """

#----------------------------------
# 단을 입력받아 구구단을 구하기
""" dan = int(input('단수를 입력하세요->'))

for i in range(1,10):
    print('{}*{}={}'.format(dan,i,dan*i)) """

#-----------------------------------------
# print() 함수
""" print('안녕' + '친구')
print('안녕','친구')
print('안녕' '친구') """

for i in range(5):
    print(i,end='+' if i<4 else '') # print함수는 자동으로 개행되므로 end로 마지막값을 정해주면 된다, if문도 가능


# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3

import sys
args = sys.argv[1:]
print(args)
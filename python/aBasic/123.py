# 숫자 찾기 게임
""" import random

rnum = random.randrange(1,101)
num = int(input('숫자를 입력하세요 -> '))
result = True

while result:
    if rnum < num :
        print('숫자가 너무 큽니다')
    elif rnum > num :
        print('숫자가 너무 작습니다')  
    elif rnum == num:
        print('정답입니다. 입력한 숫자는', num, '입니다.')
        result = False
    num = int(input('숫자를 입력하세요 -> ')) """
    
# 연속적인 구구단 계산기
""" result = True
while result:
    num = int(input("구구단 몇 단을 계산할까요(1~9)? "))
    if num != 0:
        print(num,"단을 시작합니다.")
        for i in range(1,10):
            print(num,'x',i,'=',num*i)
        continue
    elif num == 0:
        print("구구단을 종료합니다")
        break """

# 평균 구하기
kor  = [49,80,20,100,80]
math = [43,60,85,30,90]
eng  = [49,82,48,50,100]
li = [kor]+[math]+[eng]

list = []
for j in range(5):
    sum = 0
    for i in kor,math,eng:
        sum += int(i[j])
    list.append(sum/3)
print(list)
# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False
print(not hungry)
print(type(hungry))

print( hungry & sleepy)
print( hungry | sleepy)



"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False


"""
if '아':
    print('True') 
else:
    print('False')

if []:
    print('True2')
else:
    print('False2')
if -1: # True ********
    print('True3')
else:
    print('False3')

msg = '행복합시다'
if msg.find('가'): #'행' 이 있지만 0번째 값이므로 0이 출력 -> 결국 False
    print('True4') #'가' 가 없지만 없으므로 -1이 출력 -> True 
else:
    print('False4')


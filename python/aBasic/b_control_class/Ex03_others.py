msg = '행복해'            # 문자열
li = ['행','복','하다']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# (1) unpacking : 요소분해
a, b, c = di.items()
print(a)
print(b)
print(c)

alist = [(1,2),(3,4),(5,6)]

for f, s in alist:
    print('{} + {} = {}'.format(f, s, f+s))
    
# (2) enumerate() : 각 요소에 인덱스를 추가하고자 할 때
user_list = ['개발자','코더','전문가','분석가']
for value in user_list:
    print(value)
    
for value in enumerate(user_list):
    print(value)

for idx, value in enumerate(user_list):
    print(idx, ":",value)


# (3)  zip()    :
days = ['월','화','수']
doit = ['잠자기','공부','놀기','밥먹기']

print(list(zip(days,doit)))
print(dict(zip(days,doit)))
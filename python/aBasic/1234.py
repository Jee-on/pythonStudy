
data = ['안녕하세요', '감사합니다', '행복합니다']

# 첫번째 요소에서 '다' 글자가 있으면 '성공' 출력

if data[1].find('다')>=0:
    print('성공')

# for 이용하여 각 요소를 출력 끝나면 '끝' 출력
for i in data:
    print(i,end=" ")
else:
    print('끝')

# while 이용하여 각 요소 출력하여 끝나면 '끝' 출력
while data:
    print(data.pop(),end=" ")
print('끝')

data = ['안녕하세요', '감사합니다', '행복합니다']
name = ['홍길동','박길동','최길동']
# 각 요소를 z, y, x 변수에 지정
z,y,x = data

# 각각 요소를 출력 인덱스 추가
for idx, i in enumerate(data):
    print(idx,"-",i)

print(list(zip(data,name)))




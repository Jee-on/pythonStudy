import cx_Oracle as orc

#1. Connection 얻어오기
Conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
print('연결성공')

#2. sql 문장
sql = 'Select * From emp'

#3. cursor 객체 얻어오기
cursor = Conn.cursor()

#4. sql 문장 실행
cursor.execute(sql)

#[5]. 결과처리 ~ 없음말고
for row in cursor:
    print(row)

##6. cursor 닫기
cursor.close()

#7. Connection 끊기
Conn.close()
import pymysql as pym

def createTable():
    conn = pym.connect(host='localhost', user='root', password='722500', db='sys', charset='utf8')
    print("연결성공")
    cur = conn.cursor()
    
    sql = 'create table test(id char(100),name char(100),job char(100),deptno char(100))'
    cur.execute(sql)
    conn.commit()
    conn.close()
#createTable()

def insert():
    conn = pym.connect(host='localhost', user='root', password='722500', db='sys', charset='utf8')
    cur = conn.cursor()
    
    sql = "insert into test values('1000','홍길동','IT','20')"
    cur.execute(sql)
    conn.commit()
    conn.close()
#insert()

print("1.사원정보 입력\n 2.사원정보 출력 \n 3.사원정보 삭제 \n 4.종료")
result = True
while result:
    num = input("번호를 입력하세요")
    if num == 1:
        id = input('사번 입력->')
        name = input('이름 입력->')
        job = input('업무 입력->')
        deptno = input('부서번호 입력->')
        

    


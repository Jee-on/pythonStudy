import cx_Oracle as orcl
import csv

def createTable():
    Conn = orcl.connect('scott/tiger@127.0.0.1:1521/xe')
    
    sql ='CREATE TABLE supply(id integer primary key,Supplier_Name varchar2(100),Invoice_Number varchar2(30),Part_Number varchar2(30),Cost integer,Purchase_Date date)'
        
    cur = Conn.cursor()
    cur.execute(sql)
    
    sql2 = '''
        create sequence seq_supply_id
    '''
    cur.execute(sql2)
    cur.close()
    Conn.close()
    
    
def insertTable(data):
    Conn = orcl.connect('scott/tiger@127.0.0.1:1521/xe')
    cur = Conn.cursor()
    sql ='''
        INSERT into supply
        values
        (seq_supply_id.nextval,:0,:1,:2,:3,:4)
    '''
    cur.execute(sql,data)
    Conn.commit()
    cur.close()
    Conn.close()

def viewTable(tableName):
    Conn = orcl.connect('scott/tiger@127.0.0.1:1521/xe')
    cur = Conn.cursor()
    sql = 'select * from {}'.format(tableName)
    cur.execute(sql)
   
    for row in cur:
        print(row)

    cur.close()
    Conn.close()
    
if __name__ == '__main__':
    # (1) DB에 테이블 만들기
    #createTable()
    
    # (2) 데이터 입력
    imsi = ['KOSMO', '9999','8888',1000, '2023-05-25']
    #insertTable(imsi)
    
    # (3) 지정된 테이블명의 데이터 검색
    
    
    #파일 읽기
    file = open('aBasic/z_db/files/supply.csv')
    datas = csv.reader(file, delimiter=',')
    #print(datas)
    header = next(datas,None)
    
    
    for row in datas:
        insertTable(row)
        
    viewTable('supply')
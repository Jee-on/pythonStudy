
<pre>
<code>
import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import json
import re
import folium


###디비연동 시작

#전역변수 선언부
conn = None
cur = None

data1 = ""
sql = ""

try:
    conn = pymysql.connect(host='localhost', user='root', password='722500', db='hollys', charset='utf8')
    cur = conn.cursor()
except Exception as e:
    print(e)

###크롤링 시작

driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

page_no = 2
bol = True
while(bol):
    try:
        driver.get('https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page_no)
        page_no +=1
    except Exception as e:
        print(e)
        break
    
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    store = []
    for i in soup.select("tbody>tr"):
        try:
            name  = i.select_one("td:nth-child(2)").text
            tel   = i.select_one("td:last-child").text
            x  = i.select_one("td:nth-child(4)").text
        except Exception as e:
            print(e)
            bol=False
        
        #re.sub으로 괄호안의 값 제거, split으로 주소가 두개인곳 한개 제거
        #replace로 '.' 제거, rstrip으로 우 공백제거
        pattern = r'\([^)]*\)'
        addr = re.sub(pattern=pattern, repl='', string=x).split(',')[0].replace('.',"").rstrip()
        
        #딕셔너리 선언후 각 키에 맞는 값 넣어줌
        store_dict = {'name': name, 'tel':tel, 'addr':addr}
        #리스트 store에 append
        store.append(store_dict)    
     # 데이터 입력 시작
    for i in store:
        try:
            sql = "INSERT INTO hollys(매장명,전화번호,주소) VALUES('{}','{}','{}')".format(i['name']
                                                                                  ,i['tel']
                                                                                  ,i['addr'])
            cur.execute(sql)
            print(sql)
            conn.commit()
        except Exception as e:
            print(e)
            

api= '115d822f80eb6f46749c998bf47d3b5c'
sql = 'select 매장명,주소 from hollys'
cur.execute(sql)
dbAddr = cur.fetchall()
m = folium.Map(location=[37.559819, 126.963895]
               ,zoom_start=10
               ,tiles='cartodbpositron')

for i in dbAddr:
    url = f"https://dapi.kakao.com/v2/local/search/address.json?query={i[1]}"
    result = requests.get(urlparse(url).geturl(),
                          headers={"Authorization": "KakaoAK 115d822f80eb6f46749c998bf47d3b5c"}).json()
    print(json.dumps(result, indent=4, ensure_ascii=False))
    try:
        lat = result["documents"][0]["x"]
        lng = result["documents"][0]["y"]
        folium.Marker([lng,lat]
                      ,popup="{}".format(i[0])
                      ,tooltip="{}".format(i[0])).add_to(m)
        sql = "update hollys set 위도='{}',경도='{}' where 매장명='{}'".format(lat,lng,i[0])
        print(sql)
        cur.execute(sql)
        conn.commit()
        print("매장명:",i[0],"위도:",lat,"경도:",lng)
        
    except Exception as e:
        print(e)
        pass
    


m.save('./holymoly.html')

conn.commit()
cur.close()
conn.close() 

</code>
</pre>
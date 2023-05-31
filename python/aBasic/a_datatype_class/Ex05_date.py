'''
import datetime
today = datetime.date.today();
print('today is ', today)
'''

from datetime import date
today = date.today()
print('today is', today)

# 년, 월, 일
print(today.year ,'년', today.month,'월',today.day,'일')

# 요일
print(today.isoweekday(),'요일')

# 날짜계산
from datetime import datetime,date,timedelta,time
today = date.today()
print('어제:', today + timedelta(days=-1))
print('일주일 전 :', today + timedelta(weeks=-1))
print('일주일 후 :', today + timedelta(weeks=+1))
print('10일 후   :', today + timedelta(days=+10))

# month 계산
# dateutil 라이브러리 이용 

from dateutil.relativedelta import *
print('한달후', today + relativedelta.relativedelta(month=3))


# 날짜형과 문자형 형식
print(today)
print(today.strftime('%m/%d/%y'))


# 문자열(DB에서 얻으면)에서 날짜형 변환 : strptime
nalljja = '2023-08-25 12:25:22'
print(type(nalljja))
mydate = datetime.strptime(nalljja, '%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))
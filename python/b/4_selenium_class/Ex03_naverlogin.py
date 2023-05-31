"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = 
myPW = '

# 1. webdriver 객체생성

driver = webdriver.Chrome('./webdriver/chromdriver.exe')
driver.implicitly_wait(2)
driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys(myID)
driver.find_element_by_name('pw').send_keys(myPW)
driver.find_element_by_id('log.login').click()

# 다음
# 페이스북
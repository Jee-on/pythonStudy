'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# [1]
driver = webdriver.Chrome('./webdriver/chromdriver.exe')
driver.implicitly_wait(2)
driver.get('https://www.google.com/')


#----------------------------------------------
# [2]

search_input = driver.find_element(By.CSS_SELECTOR,'[name="q"]')
search_input.send_keys('가산 맛집')
search_input.submit()

print(search_input)
myID = '01039008905'
myPW = 'hy722500!!'

"""
    [연습] 페이스북에 접속해서 로그인 하기

        로그인 후에 보안창은 없는데 안 넘어가서

        from selenium.webdriver.common.keys import Keys

        아이디와 패스워드 지정후에
        elem.send_keys(Keys.RETURN)

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./webdriver/chromdriver.exe')
driver.implicitly_wait(2)
driver.get('https://www.facebook.com/')


driver.find_element(By.ID,'email').send_keys(myID)
driver.find_element(By.ID,'pass').send_keys(myPW)

driver.find_element(By.NAME,'login').click()



print("close 방지용",dddddd)
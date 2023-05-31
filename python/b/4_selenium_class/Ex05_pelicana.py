from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

store_name = []
store_tel  = []

for page_no in range(1,3):
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d' %page_no)
    html = driver.page_source
    time.sleep(4)
    soup = BeautifulSoup(html,'html.parser')
    for i in soup.select("tr > td.t_center:nth-child(1)"):
        store_name.append(i.text)
    for j in soup.select("tr > td.t_center:nth-child(3)"):
        store_tel.append(j.text)
    

for name,tel in zip(store_name,store_tel):
    print('[매장명]:', name," [전화번호]:",tel.replace('\n','').replace('\t',''))
    


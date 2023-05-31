from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from html_table_parser import parser_functions
from bs4 import BeautifulSoup
import time



driver = webdriver.Chrome('./webdriver/chromdriver.exe')
driver.implicitly_wait(3)

page_tables = []
get_table_text = []
store_name = []
store_tel  = []
page_no = 1

req_url = 'https://paikdabang.com/store'
""" driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) """


driver.get(req_url)
element = WebDriverWait(driver,10)

while True:
    
    page_no = page_no + 1
    page_xpath = '//*[@id="pagination"]/li[{}]/a'.format(page_no)
    print(page_xpath)
    time.sleep(4)
    try:
        xpath_test = driver.find_element(By.XPATH, page_xpath).click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        """ table = soup.select_one(".td_shop")
        print(table)
        page_tables.append(table) """
        
    except Exception as e:
        pass
    
        
    for result in page_tables:
        get_tables = parser_functions.make2d(result)  # table parsing
        get_table_text.append(get_tables)



total = len(get_table_text)  # 6
inlineTotal = len(get_table_text[0])  # 21
'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("https://search.kyobobook.co.kr/search?keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC&gbCode=TOT&target=total")

soup = BeautifulSoup(html, "html.parser")
page = soup.select("ul.prod_list > li.prod_item")

for info in page:
    title = info.select('span.prod_name')
    for i in title:
        print(i.text)


page = soup.select("span.img_box > img.prod_img_load")
for i in page:
    print(i['data-src'])
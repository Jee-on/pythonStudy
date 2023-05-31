from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib import parse


""" html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

page = BeautifulSoup(html,'html.parser')

info = page.select("span.green")

for i in info:
    print(i.text,end="")
     """
    
    
""" html = urlopen('http://www.pythonscraping.com/pages/page3.html')
page = BeautifulSoup(html,'html.parser')
info = page.select("tr.gift > td")
a = 0
for i in info:
    if a%2 == 0:
        print(i.text, end="")
    a +=1 """

baseUrl = "https://wikidocs.net"
html = urlopen('https://wikidocs.net/')
page = BeautifulSoup(html,'html.parser')
info = page.select("div.media > div.media-left .book-image-box img")
infoTitle = page.select("div.media-body")

list = []
for i in infoTitle:
    info3 = i.select("h4.media-heading > a")
    for j in info3:
        list.append(j.text)
    info2 = i.select("div.book-detail > div > a.menu_link")
    for y in info2:
        list.append(y.text)

a = 2   
for i in info:
    list.insert(a,parse.urljoin(baseUrl, parse.quote(i['src'])))
    a +=2

a = 0
b = 1
c = 2

for i in range(10):
    urlretrieve(list[c], 'b/3_beautifulsoup_class/Ex04_imgs/'+list[a] +'.jpg' )
    a +=2
    c +=2


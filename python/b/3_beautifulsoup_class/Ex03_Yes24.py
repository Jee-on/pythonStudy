from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from pathlib import Path

html = urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC')

soup = BeautifulSoup(html,'html.parser')

page = soup.select("em.img_bdr > img")

p1 = Path('imgs')
p1.mkdir(exist_ok=True)

for i in page:
    print(i['data-original'],i['alt'])
    imgPath = i['data-original']
    bookTitle = i['alt'].replace(':','-')
    urlretrieve(imgPath, 'imgs/' + bookTitle+ ".jpg")
from urllib import request
from urllib import error

url = 'http://www.google2.com'
try:
    site = request.urlopen(url)
except error.URLError as e:
    print('페이지가 존재하지 않습니다.',e )
else: 
    page = site.read()
    print(page)

""" headers = site.getheaders()

for a,b in headers:
    print("[{}]: {}".format(a,b)) """
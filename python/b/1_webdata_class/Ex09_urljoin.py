"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""
from urllib import request as req
from urllib import parse

baseUrl = 'http://www.example.com/html/a.html'

print(parse.urljoin(baseUrl, 'b.html'))

print(parse.urljoin(baseUrl, 'sub/c.html'))
print(parse.urljoin(baseUrl, '/sub/d.html'))
print(parse.urljoin(baseUrl, '../sub/f.html'))
print(parse.urljoin(baseUrl, '../temp/g.html'))
print(parse.urljoin(baseUrl, 'http://www.daum.net'))
print(parse.urljoin(baseUrl, '//www.naver.com'))
print(parse.urljoin(baseUrl, 'www.naver2.com'))
"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url)
    #print('1>',p)
    savepath = "./" + p.netloc + p.path
    print('2>', savepath)

    if re.search('/$', savepath):
        savepath += 'index.html'
        #print('3>', savepath)
        
    if os.path.exists(savepath):
        return savepath
    
    # 다운받을 폴더 생성
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir,exist_ok=True)
    
    # 다운받기
    try:
        print('Download:', url)
        request.urlretrieve(url, savepath)
        time.sleep(2) # 웹서버 이용 시 지연시간이 발생할수 있으므로 대기시간을 줌 / 초 단위
        return savepath
    
    except Exception as e:
        print('fail download', url, e)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)




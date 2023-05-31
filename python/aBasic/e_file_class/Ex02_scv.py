import csv

""" data = [
    [1,'김','책임']
    ,[2,'이','선임']
    ,[3,'박','연구원']
        ]

with open('aBasic/e_file_class/data/imsi.csv','w',encoding='utf-8') as f: #t 는 디폴트 값
    cout = csv.writer(f)
    cout.writerows(data)
    
"""  

result = []

with open('aBasic/e_file_class/data/imsi.csv','rt',encoding='utf-8') as f:
    cin = csv.reader(f)
    result = [n for n in cin if n] # n값이 있으면 true 이므로 공백값이 제거됨

print(result)
    
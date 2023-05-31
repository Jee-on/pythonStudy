""" 
 sample.json 파일을 읽어서
 과일별 총 금액을 출력
"""

import json

with open('aBasic/e_file_class/data/sample.json','rt',encoding='utf-8') as f:
    item = json.loads(f.read())
    for k,v in item.items():
        print('{}의 개수는 {}개 이고 가격은 {}입니다. 총 가격은 {}원 입니다'.format(k,v['count'],v['price'],int(v['count'])*int(v['price'])))
import json

with open('aBasic/e_file_class/data/temp.json','rt',encoding='utf-8') as f:
    data = f.read()
    print(data)
    
    items = json.loads(data)
    print(items)
    
    print(type(data))
    print(type(items))

    for k,v in items.items():
        print(k, ">", v['Job'])
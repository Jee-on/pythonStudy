"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path

#p = Path('c:\WindowsTemp') # 존재하는 경로인지는 안잡아줌
p = Path('..')
print(p)
print(p.resolve())

# (1) 해당 경로와 하위 목록들 확인

child = []

for x in p.iterdir():
    if x.is_dir():
        child.append(x.resolve())

child = [x.resolve() for x in p.iterdir() if x.is_dir() ]

print(child)
print('-'*100)

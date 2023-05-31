from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home())

p1 = Path('.')
print(p1.stat())

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기

from datetime import datetime
tm = p1.stat()
print(tm.st_ctime)
print(datetime.fromtimestamp(tm.st_ctime))

# ------------------------------------------------
# 3. 디렉토리 생성
p2 = Path('imsi')
p2.mkdir(exist_ok=True)

p3 = Path('temp2/temp3/abc')
p3.mkdir(parents=True,exist_ok=True)

# ------------------------------------------------
# 4. 파일 생성
""" 
with open('imsi/1.txt','w') as f:
    f.write('Hello')
 """

#p4 = Path('imsi/1.txt')
#p4.write_text("우리밥먹자", encoding="utf-8")
#p4.rename('temp.txt')

# ------------------------------------------------
#  5. 경로 제거

p5 = Path('imsi')
p5.rmdir()

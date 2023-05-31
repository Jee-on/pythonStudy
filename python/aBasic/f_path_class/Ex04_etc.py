"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""

import shutil

#shutil.copytree('/aBasic/imsi','../copytemp')
#shutil.rmtree('/aBasic/imsi')

import os
from pathlib import Path

print(os.environ["JAVA_HOME"])
print(os.environ["TOMCAT_HOME"])

f = Path('abc.txt')
f.touch()
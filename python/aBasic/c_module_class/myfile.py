""" import mymodule as my """
# 모듈 별칭도 가능 , 별칭 부여되면 별칭으로만 써야함
""" print('오늘의 날씨는', my.get_weather())
print('오늘의 요일은', my.get_date()) """


from mypackage.mymodule import *
print('오늘 날씨는', get_weather())
print('오늘 날씨는', get_date())
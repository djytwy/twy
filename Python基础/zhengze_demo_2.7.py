import re
str1 = 'dssa 676534074@qq.comasl22334 6765491jjf@gmai.comjocker163fjow12567'
reg = re.compile('[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com')
obj = reg.findall(str1)
print(obj)


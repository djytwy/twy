# !/usr/bin/env python
# coding:utf-8
import re

text = 'klajflkjefejiwetujd href=<jfieot902j>end 见佛诶我放假哦微积分围殴if降温哦ijlkfjeiofjwe class="kknoshow>"dfjalkfjalkfjal '
result = re.findall('href=<(.*?)>end.* class="(.*?)>"', text)
temp = result[0]
print temp[0]



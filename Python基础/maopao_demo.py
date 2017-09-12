#!/usr/bin/env python
#coding:utf-8
import random
def bubble_sort(data):
  for i in range(len(data) - 1):
   for j in range(len(data) - 1-i):
    if (data[j] > data[j + 1]):
        tmp = data[j]
        data[j] = data[j + 1]
        data[j + 1] = tmp
r = random.Random()
data = []
for n in range(0, 20):
  data.append(r.randint(1, 300))
print data
bubble_sort(data)
print data
#!/usr/bin/env python
#coding:utf-8

class Box:
     def __init__(self):
         self.__color = 'green'

     def get_color(self):
         print self.__color

     @property
     def color(self):
         return self.__color

     @color.setter
     def color(self, color):
        if self.__color != 'red':
            self.__color = color

if __name__ == '__main__':
    box = Box()
    box.get_color()
    print box.color
    box.color = 'red'
    print box.color
    box.get_color()

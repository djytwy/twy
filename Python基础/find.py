#!/usr/bin/env python
#coding:utf-8

class Find:
    def __init__(self):
        self.str1 = 'this is str1'
        self.str2 = 'this is str2'
        self.start_positions_str1 = 0
        self.start_positions_str2 = 0
        self.res = []
        self.__length = 0

    def input_str(self):
        self.str1 = 'Enter string1:'
        self.str2 = 'string2:'

    def find_string(self):
            for i in self.str1:
                if i in self.str2:
                    if self.start_positions_str1 == 0:
                        self.start_positions_str1 = i[0]
                    elif self.start_positions_str2 == 0:
                        self.start_positions_str2 = self.str2[0]
                    self.__length += 1
                    self.res.append(i)
                        #for k in (0, (len(self.str1)-i[0])):
                         #   if self.str1[i[0]+1] == self.str2[j[0]]:
                          #      self.__length += 1

    def pr_str(self):
        print self.res

    def run(self):
        self.input_str()
        self.find_string()
        self.pr_str()

if __name__ == '__main__':
    f = Find()
    f.run()





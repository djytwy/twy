#!/usr/bin/env python
#coding:utf-8
import random
import os
import time
import sys
class Shuangseqiu:

    def __init__(self):
        self.caipiao = [0, 0, 0, 0, 0, 0, 0, 0]
        self.shijian_N = '2017-7-31 17:52'
        self.haoma_n = '12345678'

    def chan_sheng(self):
        self.haoma_n = ''
        caipiao_hong = random.sample(range(1, 33), 7)
        caipiao_lan = random.sample(range(1, 16), 1)
        self.caipiao = caipiao_hong+caipiao_lan
        return self.caipiao

    def pai_xu(self, caipiao):
        for i in range(len(caipiao)-2):
            for j in range(len(caipiao)-2):
                if caipiao[j]>caipiao[j+1]:
                    temp = caipiao[j]
                    caipiao[j] = caipiao[j+1]
                    caipiao[j+1] = temp
        print caipiao

    def shijian(self):
        shijian_N = time.strftime("%Y-%m-%d %X", time.localtime())
        return shijian_N

    def bao_cun(self, haoma, shijian, paths):
        for i in haoma:
            temp =str(i)
            self.haoma_n = self.haoma_n+temp
        if not os.path.exists(paths):
           os.makedirs(paths)
        file_paths = paths + '/' + u'number'+'.txt'
        f = open(file_paths, 'a+')
        f.writelines('双色球号码为：' + self.haoma_n +' 时间：'+ shijian +'\n')
        f.close()

    def kaishi(self):
        haoma = self.chan_sheng()
        self.pai_xu(haoma)
        Shijian = self.shijian()
        self.bao_cun(haoma, Shijian, 'shuangseqiu')

if __name__ == '__main__':
    shuangseqiu = Shuangseqiu()
    shuangseqiu.kaishi()




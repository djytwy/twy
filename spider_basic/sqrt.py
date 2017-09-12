# coding:utf-8
import math


class App:

    def __init__(self):
        self.number = 1

    def run(self):
        for self.number in range(10000):
            # 判断一个数是否是完全平方数，用到的主要是.is_integer()
            if math.sqrt(self.number+100).is_integer() and math.sqrt(self.number+268).is_integer():
                print self.number

if __name__ == '__main__':
    app = App()
    app.run()


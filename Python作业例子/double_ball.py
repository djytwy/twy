import random
import os
import time
class red():
    def __init__(self,red,blue):
        self.red = red
        self.blue = blue
    def order(self):
        red_ball_list= random.sample(range(1,self.red+1), 6)
        blue_ball_list = random.sample(range(1, self.blue+1), 1)
        red_ball_list=sorted(red_ball_list)
        double=red_ball_list+ blue_ball_list
        # path='test'
        # file_path = path + '/' + str(time.time()) + '.txt'
        # f = open(file_path, 'w')
        # f.write(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) + '+')
        # f.write(str(double))
        # f.close()
        print (double)

ball=red(33,16)
ball.order()

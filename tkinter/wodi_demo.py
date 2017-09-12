#coding:utf-8
import random
class Wodi:
    def __init__(self):
        self.wodinum = 1
        self.wodicihui = '毛衣'

    def show_num(self):
        print('卧底数量：%d'%self.wodinum)

    def kill_wodi(self):
        self.wodinum -= 1

class Pingmin(Wodi):
    def __init__(self):
        super(Pingmin, self).__init__()
        self.pingmingnum = 3
        self.pingmincihui = '风衣'

    def show_num(self):
        print('平民数量：%d' % self.pingmingnum)

    def kill_pingmin(self):
        self.pingmingnum -= 1


class Game(Pingmin):
    def __init__(self):
        super(Game, self).__init__()
        self.player = 4
        self.items = {}
        self.piaoshu = {}

    def player_num(self):
        self.player = input('请输入玩家数量（玩家数量应大于等于3人）:')
        self.player = int(self.player)
        self.pingmingnum = self.player-1

    def panduan_player(self):
        if self.player < 3:
            print('玩家人数过少，无法开始游戏！')
            exit()
        else:
            print('开始游戏！')

    def chansheng_renwu(self):
        wodi = random.randint(1, self.player + 1)
        for i in range(1, self.player + 1):
            self.items[i] = self.pingmincihui
        self.items[wodi] = self.wodicihui
        print(self.items)

    def show_renwu(self):
        for i in range(self.player):
            haoma = input('输入你的号码:')
            haoma = int(haoma)
            print(self.items[haoma])

    def init_piaoshu(self):
        for i in self.items:
            self.piaoshu[i] = 0

    def tou_piao(self):
        for i in self.items:
            toupiao = input('请输入你的号码：')
            toupiao = int(toupiao)
            sharen = input('请输入你投的玩家号码：')
            sharen = int(sharen)
            if sharen in self.items:
                self.piaoshu[sharen] += 1
        print(self.piaoshu)

    def panduan(self):
        temp = []
        temp2 = []
        zuida = 0
        for i in self.piaoshu:
            temp.append(self.piaoshu[i])
            zuida = max(temp)
        for i in self.piaoshu:
            if self.piaoshu[i] == zuida:
                temp2.append(i)
        if len(temp2) != 1:
            print('票数相同：')
            for i in range(len(temp2)):
                print(temp2[i])
            for i in temp2:
                self.piaoshu[i] = 0
        else:
            if self.items[temp2[0]] == self.pingmincihui:
                self.kill_pingmin()
            else:
                self.kill_wodi()
            self.player -= 1
            #self.items.pop(temp2[0])
            del self.items[temp2[0]]
            del self.piaoshu[temp2[0]]
            if self.player <= 2 and self.wodinum != 0:
                    self.victory_wodi()
                    exit()
            elif self.wodinum == 0 and self.player >= 2:
                    self.victory_pingmin()
                    exit()
            else:
                for i in self.items:
                    self.piaoshu[i] = 0
        print(self.items)

    def victory_pingmin(self):
        print('平民获胜！')

    def victory_wodi(self):
        print('卧底获胜！')

    def yunxing(self):
        self.player_num()
        self.panduan_player()
        self.chansheng_renwu()
        self.show_renwu()
        self.init_piaoshu()
        while 1:
            self.tou_piao()
            self.panduan()

if __name__ == '__main__':
    game = Game()
    game.yunxing()

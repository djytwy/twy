#coding:utf-8
import random
import tkinter as tk
from tkinter import messagebox

#卧底的类
class Wodi:
    def __init__(self):
        self.wodinum = 1
        self.wodicihui = '毛衣'

    def kill_wodi(self):
        self.wodinum -= 1
#平民的类
class Pingmin(Wodi):
    def __init__(self):
        super(Pingmin, self).__init__()
        self.pingmingnum = 3
        self.pingmincihui = '风衣'

    def kill_pingmin(self):
        self.pingmingnum -= 1

#整个游戏的类
class Game(Pingmin):
    def __init__(self):
        super(Game, self).__init__()
        self.player = 4
        self.haoma = 0
        self.items = {}
        self.piaoshu = {}

    def player_num(self):  #游戏的人数判断，后面在tkinter的可视化界面中重写
        self.player = input('请输入玩家数量（玩家数量应大于等于3人）:')
        self.player = int(self.player)
        self.pingmingnum = self.player-1

    def chansheng_renwu(self):#用于产生游戏里的人物，将对应的人物编号
        wodi = random.randint(1, self.player + 1)
        for i in range(1, self.player + 1):
            self.items[i] = self.pingmincihui
        self.items[wodi] = self.wodicihui
        print(self.items)

    def show_renwu(self):#显示人物，即你输入自己的号码，就显示相应的词汇
        for i in range(self.player):
            self.haoma = input('输入你的号码:')
            self.haoma = int(self.haoma)
            print(self.items[self.haoma])

    def init_piaoshu(self):#初始化每个号码的得票数
        for i in self.items:
            self.piaoshu[i] = 0

    def panduan(self):#判断玩家是否出局，平民/卧底 获胜？后面会重写
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

    def victory_pingmin(self):#平民获胜，后面会重写
        print('平民获胜！')

    def victory_wodi(self):#卧底获胜，后面也会重写
        print('卧底获胜！')

class APP(Game):#基于tkinter的APP类，继承上面所有的类的方法，属性

    def __init__(self, master):#初始化界面
        super(APP, self).__init__()
        self.temp = 0
        self.temp2 = 0

        top = tk.Label(master, text='谁是卧底', fg='blue', bg='yellow', font=('Tempus Sans ITC', 20))
        top.grid(row=0, column=0, padx=15, pady=2)

        bottom = tk.LabelFrame(master, fg='green', bg='blue', font=('Tempus Sans ITC', 20))
        bottom.grid(row=1, column=0, padx=15, pady=2)

        self.label_enter_renshu = tk.Label(bottom, text='玩家人数', padx=15, pady=2)
        self.label_enter_who = tk.Label(bottom, text='号码', padx=15, pady=2)
        self.label_beitouren = tk.Label(bottom, text='被投票人', padx=5, pady=2)
        self.label_toupiaoren = tk.Label(bottom, text='投票人', padx=5, pady=2)

        self.label_enter_renshu.grid(row=1, column=0, padx=15, pady=2)
        self.label_enter_who.grid(row=2, column=0, padx=15, pady=2)
        self.label_toupiaoren.grid(row=3, column=0, padx=15, pady=2)
        self.label_beitouren.grid(row=4, column=0, padx=15, pady=2)

        renshu = tk.IntVar()    #这一句将renshu这个量设置为tk.IntVar()型，若要使用它的具体值则要使用get(),即renshu.get()
        self.enter_renshu = tk.Entry(bottom, textvariable=renshu)   #这一句决定输入框布置到哪一层上面
        self.enter_renshu.grid(row=1, column=1, padx=15, pady=2)
        self.temp2 = renshu

        who = tk.IntVar()
        self.enter_who = tk.Entry(bottom, textvariable=who)
        self.enter_who.grid(row=2, column=1, padx=15, pady=2)
        self.haoma = who

        toupiaoren = tk.IntVar()
        self.enter_toupiaoren = tk.Entry(bottom, textvariable=toupiaoren)
        self.enter_toupiaoren.grid(row=3, column=1, padx=15, pady=2)
        self.toupiaoren = toupiaoren

        beitouren = tk.IntVar()
        self.enter_beitouren = tk.Entry(bottom, textvariable=beitouren)
        self.enter_beitouren.grid(row=4, column=1, padx=15, pady=2)
        self.beitouren = beitouren

        self.show_cihui = tk.Text(bottom, height=10, width=30)      #这一句的作用是决定文本框建立在哪一层上面，并设置大小
        self.show_cihui.insert(tk.END, '')                          #这一句是将文本框初始化，并插入空字符
        self.show_cihui.grid(row=5, column=1, padx=15, pady=2)

        self.button1 = tk.Button(bottom, text='开始游戏', fg='red', command=self.player_num)
        self.button1.grid(row=1, column=3, padx=15, pady=2)

        self.button2 = tk.Button(bottom, text='查看词汇', fg='red', command=self.show_renwu)
        self.button2.grid(row=2, column=3, padx=15, pady=2)

        self.button3 = tk.Button(bottom, text='投票', fg='red', command=self.panduan)
        self.button3.grid(row=4, column=3, padx=15, pady=2)

    def show_renwu(self):
        self.show_cihui.delete(0.0, tk.END)
        self.show_cihui.insert(tk.END, self.items[self.haoma.get()]+'\n')
        print(self.items[self.haoma.get()])

    def player_num(self):
        self.player = self.temp2.get()
        if self.player <= 3:
            self.show_cihui.insert(tk.END, '人数过少，无法开始游戏\n')
        else:
            self.show_cihui.insert(tk.END, '开始游戏！！！\n')
            self.chansheng_renwu()
            self.init_piaoshu()
            self.pingmingnum = self.player-1

    def panduan(self):
        temp = []
        temp2 = []
        zuida = 0
        self.show_cihui.insert(tk.END, '%d' % self.toupiaoren.get()+'号玩家投票给：'+'%d' % self.beitouren.get()+'号玩家'+'\n')
        if self.beitouren.get() in self.items:
            self.piaoshu[self.beitouren.get()] += 1
            self.temp += 1
        if self.temp == len(self.items):
            for i in self.piaoshu:
                temp.append(self.piaoshu[i])
                zuida = max(temp)
            for i in self.piaoshu:
                if self.piaoshu[i] == zuida:
                    temp2.append(i)
            if len(temp2) != 1:
                self.show_cihui.insert(tk.END, '票数相同：\n')
                for i in range(len(temp2)):
                    self.show_cihui.insert(tk.END, '%d' % temp2[i]+'\n')
                for i in temp2:
                    self.piaoshu[i] = 0
            else:
                if self.items[temp2[0]] == self.pingmincihui:
                    self.kill_pingmin()
                else:
                    self.kill_wodi()
                self.show_cihui.insert(tk.END, '%d' % temp2[0]+'号玩家得票最多，出局\n')
                self.player -= 1
                del self.items[temp2[0]]
                del self.piaoshu[temp2[0]]
                if self.player <= 2 and self.wodinum != 0:
                        self.victory_wodi()
                elif self.wodinum == 0 and self.player >= 2:
                        self.victory_pingmin()
                else:
                    for i in self.items:
                        self.piaoshu[i] = 0
            self.temp = 0

    def closeWindow(self):
        if messagebox.askokcancel('Quit', '确定退出游戏？'):
            root.destroy()

    def victory_pingmin(self):
        if messagebox.showinfo('游戏结局', '平民获胜！！！'):
            root.destroy()

    def victory_wodi(self):
        if messagebox.showinfo('游戏结局', '卧底获胜！！！'):
            root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('谁是卧底')
    app = APP(root)
    root.protocol('WM_DELETE_WINDOW', app.closeWindow)
    root.mainloop()





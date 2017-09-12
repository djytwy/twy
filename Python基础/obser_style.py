#encoding=utf-8

#被观察的对象：邮局
class Postoffice():
    def __init__(self):
        self.observes=[]
        self.kanwu=''
    def attach(self,observe):
        self.observes.append(observe)
    def notify(self):
        for observe in self.observes:
            observe.update()

#观察对象：出版社
class Press():
    def __init__(self, name, postoffice):
        self.name = name
        self.postoffice = postoffice
    def update(self):
        print '邮局收到订阅信息：%s,杂志社向%s寄送订阅的刊物'%(self.postoffice.kanwu,self.name)

if __name__=='__main__':
    postoffice1 = Postoffice()
    postoffice2 = Postoffice()
    user1 = Press('小明', postoffice1)
    user2 = Press('小红', postoffice2)
    postoffice1.attach(user1)
    postoffice2.attach(user2)
    postoffice1.kanwu = '杂志'
    postoffice2.kanwu = '报纸'
    postoffice1.notify()
    postoffice2.notify()

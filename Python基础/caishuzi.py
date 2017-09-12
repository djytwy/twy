import random
xingming = input('请输入姓名:')
shangxian = input('请输入猜数字范围的上限:')
xiaxian = input('请输入猜数字范围的下限:')
shangxian = int(shangxian)
xiaxian = int(xiaxian)
daan = random.randint(xiaxian, shangxian)
cishu = 1
while cishu <= 5:
    temp = '还有%d机会，加油噢！' % (6-cishu)
    print(temp)
    shuzi = input('请输入你所猜的数字:')
    with open('caishuzi.txt', 'a', encoding='utf-8') as j:
        j.write(xingming+'猜的内容:'+shuzi+'\n')
    if shuzi in ['exit', 'quit']:
        print('退出游戏')
        exit()
    else: shuzi = int(shuzi)
    if shuzi == daan:
        print('恭喜你，猜中啦！')
        exit()
    else:
        if cishu == 5:
            print('正确的数字是：%d。真遗憾没猜中真遗憾，下次再来吧！' % daan)
            exit()
        else: pass
        shangxian_xin = random.randint(daan, shangxian)
        xiaxian_xin = random.randint(xiaxian, daan)
        shangxian = shangxian_xin
        xiaxian = xiaxian_xin
        tishi = '提示一个新的范围：%d——%d' % (xiaxian_xin, shangxian_xin)
        print(tishi)
    cishu += 1


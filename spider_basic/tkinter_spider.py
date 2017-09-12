# !/usr/bin/env python
# coding:utf-8
import requests
import re
import os
import threading
import Tkinter
import tkMessageBox

gImageList = []
gCondition = threading.Condition()
gurl = '0'

# 生产者类，负责将界面上的所有用户的url生成


class Producer_url(threading.Thread):
    def run(self):
        global gImageList
        global gCondition
        global gurl

        print('%s started' % threading.current_thread())
        urls = user_urls()

        gCondition.acquire()
        for url in urls:
            if url != '?id=00000000#stipsign':        # 将界面上的一个莫名其妙的url过滤掉
                gImageList.append(url)
        print('%s: produced %d urls. Left %d urls.' % (threading.current_thread(), len(urls) - 1, len(gImageList)))
        gCondition.notify_all()
        gCondition.release()

# 消费者类，负责将生产者产生的url进行连接并进入这个url下载用户的头像


class Consumer_url(threading.Thread):
    def __init__(self, folder='wallpaper', group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(Consumer_url, self).__init__(group, target, name, args, kwargs, verbose)
        self.folder = folder

    def run(self):
        global gImageList
        global gCondition

        print('%s started' % threading.current_thread())
        while True:
            gCondition.acquire()
            print('%s: trying to download image. Queue length is %d' % (threading.current_thread(), len(gImageList)))
            while len(gImageList) == 0:
                gCondition.wait()
                print('%s: waken up. Queue length is %d' % (threading.current_thread(), len(gImageList)))
            url = gImageList.pop()
            gCondition.release()
            _download_user_image(url, self.folder)
            while len(gImageList) == 0:                   # 负责停止程序，当所有的头像被下载完了之后停止整个程序
                print('全部的头像已经下载完了，线程%s停止工作' % threading.current_thread())
                break

# 负责获取百度贴吧里所有的用户的url


def user_urls():
    global gurl
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    tieba_web = requests.get(gurl, headers=headers)
    tieba_message = tieba_web.content
    hrefs = re.findall('href="/home/main(.*?)"', tieba_message)
    return hrefs

# 负责下载对应用户主页的用户头像


def _download_user_image(url_user, folder):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    user_message = requests.get('http://tieba.baidu.com/home/main'+url_user)
    user_name = re.findall('<span class="user_name">用户名:(.*?)<', user_message.content)
    user_image_temp = re.findall('class="userinfo_head"><img src="(.*?)"/></a>', user_message.content)
    image = requests.get(user_image_temp[0], headers=headers)
    #################################################
    # 注意文件的写入与文件路径建立的方法！！！
    if not os.path.isdir(folder):
        os.mkdir(folder)
    image_path = folder + '/' + user_name[0].decode('utf-8') + '.jpg'
    #################################################
    print('downloading post cover from %s' % user_image_temp[0])
    with open(image_path, 'wb') as f:
        f.write(image.content)
    f.close()


class APP:
    def __init__(self, master):
        global gurl

        self.label_enter_renshu = Tkinter.Label(master, text='输入网址：', padx=15, pady=2)
        self.label_enter_renshu.grid(row=0, column=0, padx=15, pady=2)

        self.url = Tkinter.StringVar()
        self.enter_url = Tkinter.Entry(master, textvariable=self.url, width=80)
        self.enter_url.grid(row=0, column=1, padx=15, pady=2)

        self.start = Tkinter.Button(master, text='开始获取数据', padx=15, pady=2, command=self.run)
        self.start.grid(row=0, column=2, padx=15, pady=2)


    def run(self):
        global gurl
        gurl = self.url.get()
        user_urls()
        Producer_url().start()
        for i in range(5):
            Consumer_url(folder='user_images').start()

if __name__ == '__main__':
    root = Tkinter.Tk()
    app = APP(root)
    root.mainloop()




#!/usr/bin/env python
#coding:utf-8

import re
import os
import urllib2

class Spider(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.num = 0

    def get_web(self, index):
        headers = {'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url=self.url % str(index), headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print e
        except urllib2.URLError as e:
            print e

    def poccess_web(self, content):
        pattern = re.compile('<div class="teacherListR">.*?<p class="font20 color00 marginB14 t3out p">(.*?)<a href="/u/\d+/" class="go font12">查看他的课程</a></p>.*?<p class="color66 marginB14"><span class="color99">.*?</span></p>.*?<p class="color66"><span class="color99">简介：</span>(.*?)</p>.*?</div>', re.S)
        message = re.findall(pattern, content)
        return message

    def save(self, message, path):
        for item in message:
            item_new = item[1].replace('\n', '')
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + u'maizi_techers' + '.txt'
            if item_new == '':
                f = open(file_path, 'a+')
                f.writelines(item[0] + ':' + ' ' + '无' + '\n')
                f.close()
            else:
                f = open(file_path, 'a+')
                f.writelines(item[0] + ':' + ' ' + item_new + '\n')
                f.close()
            self.num += 1

    def run(self):
        print '开始抓取信息......'
        for i in range(1, 29):
            content = self.get_web(i)
            message = self.poccess_web(content)
            self.save(message, 'maizi_techers')
        print '信息抓取结束，一共%d老师的信息！' % (self.num)

if __name__ == '__main__':
    spider = Spider()
    spider.run()
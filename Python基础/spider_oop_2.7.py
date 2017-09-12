#!/usr/bin/env python
#coding:utf-8

import re
import os
import urllib2
import urllib

class Spider (object):
        def __init__(self):
            self.url = 'https://www.qiushibaike.com/text/page/%s/?s=5002956'
            self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'

        def get_web(self, index):
            headers = {'User-Agent': self.user_agent}
            try:
                request = urllib2.Request(url=self.url % str(index), headers=headers)
                response = urllib2.urlopen(request)
                content = response.read()
                return content
            except urllib2.HTTPError as e:
                print e
                exit()
            except urllib2.URLError as e:
                print e
                exit()

        def poccess_wed(self, content):
            pattern = re.compile('<div class="content">.*?</div>', re.S)
            items = re.findall(pattern, content)
            return items

        def save(self, items, path, j):
            for i in enumerate(items):
                path = 'qiubai'
                if not os.path.exists(path):
                    os.makedirs(path)
                filepath = path + '/' + 'duanzi' + str(j) + str(i[0]) + '.txt'
                f = open(filepath, 'w')
                item_new = i[1].replace('\n', '').replace('<div class="content">', '').replace('</div>', '').replace('<span>','').replace('</span>', '').replace('<br/>', '\n')
                f.write(item_new)
                f.close()
                self.temp = i[0]


        def run(self):
            print '开始抓取数据了。。。。'
            for i in range(1, 35):
                content = self.get_web(i)
                items = self.poccess_wed(content)
                self.save(items, 'qiubai', i)
            print '数据抓取结束了！一个抓取%d个数据！' % (i*self.temp)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
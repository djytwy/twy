#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib2
import re
import os
if __name__ == '__main__':
    print '开始抓取信息。。。。'
    for j in range(1, 35):
        url = 'https://www.qiushibaike.com/text/page/%d/?s=5002956' % j
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
        headers = {'User-Agent':user_agent}
        try:
            request = urllib2.Request(url=url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            pattern = re.compile('<div class="content">.*?</div>', re.S)
            items = re.findall(pattern, content)
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()
        for i in enumerate(items):
            path = 'qiubai'
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = path +'/'+'duanzi'+str(j)+str(i[0])+'.txt'
            f = open(filepath, 'w')
            item_new = i[1].replace('\n', '').replace('<div class="content">', '').replace('</div>', '').replace('<span>', '').replace('</span>', '').replace('<br/>', '\n')
            f.write(item_new)
            f.close()
    print '信息抓取结束！一共抓取了%d个段子' % (j*i[0])

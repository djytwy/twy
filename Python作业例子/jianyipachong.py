#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib2
import os
import re

class Spiter(object):
	def __init__(self):
		self.url = 'http://www.maiziedu.com/course/teachers/?page=%d'
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'

	def get_page(self,page_index):
		'''此方法访问网页并且返回网页内容'''
		try:
			headers = {'User-Agent': self.user_agent}
			request = urllib2.Request(url=self.url%int(page_index), headers=headers)
			response = urllib2.urlopen(request)
			content = response.read()
			return content
		except urllib2.URLError:
			print '抱歉没有网络哦'
			exit()

	def analysis(self,content):
		'''此方法对网页内容进行处理提取操作'''
		pattern = re.compile('''<div class="teacherListR">.*?<p class="font20 color00 marginB14 t3out p">(.*?)<a href="/u/\d+/" class="go font12">查看他的课程</a></p>.*?<p class="color66 marginB14"><span class="color99">.*?</span></p>.*?<p class="color66"><span class="color99">简介：</span>(.*?)</p>.*?</div>''', re.S)
		items = re.findall(pattern, content)
		return items

	def save(self,items,path):
		'''此方法对提取出来的内容进行处理并且保存'''
		for item in items:
			item_new = item[1].replace('\n', '')
			if not os.path.exists(path):
				os.makedirs(path)
			file_path = path + '/' + u'麦子学院老师信息'+ '.txt'
			if item_new == '':
				f = open(file_path, 'a+')
				f.writelines(item[0] + ':' + ' ' + '此老师暂无个人简介。' + '\n')
				f.close()
			else:
				f = open(file_path,'a+')
				f.writelines(item[0] + ':' + ' ' + item_new + '\n')
				f.close()

	def run(self):
		print '开始抓取内容了哟。。'
		for i in xrange(1,29):
			content = self.get_page(i)
			items = self.analysis(content)
			self.save(items,'maizi')

		print '好累，终于抓取完了。。'

if __name__ == '__main__':
	s = Spiter()
	s.run()
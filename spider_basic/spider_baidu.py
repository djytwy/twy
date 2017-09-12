# !/usr/bin/env python
# coding:utf-8
import requests
import re
import os


def _download_poster_cover(url_img, fname, folder):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    if not os.path.isdir(folder):
        os.mkdir(folder)
    image_path = folder + '/' + fname.decode('utf-8') + '.jpg'
    print('downloading post cover from %s' % url_img)
    image = requests.get(url_img, headers=headers)
    with open(image_path, 'wb') as f:
        f.write(image.content)
    f.close()

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    s = requests.get(url, headers=headers)
    c = s.content
    hrefs = re.findall('href="/home(.*?)"', c)
    l = len(hrefs)
    for i in range(1, l):
        image_src = requests.get('http://tieba.baidu.com/home'+hrefs[i])
        user_name = re.findall('<span class="user_name">用户名:(.*?)<', image_src.content)
        user_image_temp = re.findall('class="userinfo_head"><img src="(.*?)"/></a>', image_src.content)
        user_image = requests.get(user_image_temp[0])
        _download_poster_cover(user_image_temp[0], user_name[0], 'user_image')



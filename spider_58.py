# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import threading


img_list = []
gCondition = threading.Condition()

# 产生所有地区的URL
def produce_sum_url(url,headers):
    url = 'http://www.58.com/ershoufang/changecity/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
    }
    url_list = []
    entry = requests.get(url, headers=headers)
    soup = BeautifulSoup(entry.content,'lxml')
    for href in soup.find_all('a'):
        url_list.append(href['href'])
    url_list = url_list[1:425]
    return url_list


# 产生该地区的所有房源的URL
def produce_zone_url(url,headers):
    url_list = produce_sum_url(url,headers)
    url_list_room = []
    page = 1
    # 产生所有的URL
    for url in url_list:
        url = url + 'pn%d'% page
        entry = requests.get(url, headers=headers)
        soup2 = BeautifulSoup(entry.content, 'lxml')
        index = soup2.select('.pager > a > span')
        page_num = index[2].get_text()
        # 实现翻页功能
        for page in range(int(page_num)):
            url = url_list[0] + 'pn%d' % (page+1)
            entry = requests.get(url, headers=headers)
            soup2 = BeautifulSoup(entry.content, 'lxml')
            url_room = soup2.select('.title > a')
            # 产生所有的
            for url_temp in url_room:
                url_list_room.append(url_temp.get('href'))
    return url_list_room


def spider_58(url_room):
    global img_list
    room_page = requests.get(url_room[0].get('href'))
    soup3 = BeautifulSoup(room_page.content, 'lxml')
    # 房源标题
    title = soup3.select('.house-title > h1')[0].get_text()
    # 房源描述
    descs = soup3.select('.genaral-pic-desc > p')
    for desc in descs:
        print desc.get_text().strip()
    # 房源经纪人
    agent = soup3.select('.agent-name > a')[0].get_text()
    # 房源的联系方式
    phone = soup3.select('.phone-num')[0].get_text()
    # 住房的面积
    main = soup3.select('.main')[0].get_text()
    # 住房的总价
    sum_price = soup3.select('.price')[0].get_text()
    # 住房的单价
    unit_price = soup3.select('.unit')[0].get_text().strip()
    # 房源的楼盘
    items = soup3.select('.c_000 > a')
    local = items[0].get_text().strip() + '-' + items[1].get_text().strip()
    # 房源的小区
    housing = items[2].get_text().strip() + '-' + items[3].get_text().strip()
    # 房源的图片
    img_urls = soup3.select('.general-pic-list > li > img')
    for img in img_urls:
        img_list.append(img.get('data-src'))


if __name__== '__main__':
    url = 'http://www.58.com/ershoufang/changecity/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
    }




# print '楼盘：'
# print soup3.select('.xiaoqu-name > a')[0].get_text()

# for desc in descs.stripped_strings:
#     print desc[0].get_text()
# print desc


# for url in url_list:
#     s = requests.get(url, headers=headers)
#     soup = BeautifulSoup(s.content, 'lxml')
#     p


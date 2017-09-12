#!/usr/bin/env python
#coding:utf-8
import urllib
import urllib2
if __name__ == '__main__':
    url = 'https://www.oschina.net/action/user/hash_login?from='
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    values = {'email': '62234com', 'pwd': '2234531'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url=url,data=data, headers=headers)
    response = urllib2.urlopen(request)
    print response.read()


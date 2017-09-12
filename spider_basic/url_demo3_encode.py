# coding utf-8
import urllib
import urlparse

def parse_qs():
    url = 'https://www.baidu.com/s?wd=%40import&rsv_spt=1&rsv_iqid=0xeb1e039800019c3d&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=93380420_hao_pg&rsv_enter=1&rsv_n=2&rsv_sug3=1'
    result = urlparse.urlparse(url)
    print result

if __name__ == '__main__':
    parse_qs()

# -*- coding: utf-8 -*-
import requests

def get_json():
    r = requests.get('https://api.github.com/events')
    print(r.status_code)
    print(r.headers)
    print(r.content)
    print(r.text)
    print(r.json())

def get_querystring():
    url = 'http://httpbin.org/get'
    params = {'qsl': 'valuel', 'qs2': 'value2'}
    r = requests.get(url, params=params)
    print(r.status_code)
    print(r.content)

def get_custom_headers():
    url = 'http://httpbin.org/get'
    headers = {'x-header1': 'value1', 'x-header2': 'value2'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.content)

if __name__ == '__main__':
    get_custom_headers()

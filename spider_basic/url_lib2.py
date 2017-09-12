import urllib2

def urlopen():
    url='http://blog.kamidox.com/no-exist'
    try:
        s = urllib2.urlopen(url,timeout=2)
    except urllib2.HTTPError,e:
        print(e)
    else:
        print(s.read(100))
        s.close()

def request():
    headers = {'User-Agent': 'Mozilla/5.0', 'x-my-header': 'my value'}
    req = urllib2.Request('http://blog.kamidox.com',headers=headers)
    s = urllib2.urlopen(req)
    print(s.read(100))
    print(req.headers)
    s.close()

if __name__ == '__main__':
    request()

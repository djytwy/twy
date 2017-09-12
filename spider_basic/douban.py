# -*- coding: utf-8 -*-
import urllib2
from HTMLParser import HTMLParser

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs, 'data-category') == 'upcoming':
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['duration'] = _attr(attrs, 'data-duration')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print('电影名称：%(title)s | 电影时长：%(duration)s | 导演：%(director)s | 演员：%(actors)s' % movie)

def nowplaying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    s = urllib2.urlopen(req)
    parser = MovieParser()
    parser.feed(s.read())
    s.close()
    return parser.movies

if __name__ == '__main__':
    url = 'http://movie.douban.com/nowplaying/chengdu/'
    movies = nowplaying_movies(url)

    # import json
    # print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))

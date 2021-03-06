import urllib.request
import io
__author__ = 'Jacob'


def get_robots_txt(url):
    print('Getting Robots.txt')
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + 'robots.txt', data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

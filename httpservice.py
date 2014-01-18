#!/usr/bin/env python
#_*_coding:utf-8 _*_

__filename__ = 't.py'
__author__ = 'CuiJing'
__email__ = 'cuijing@jcrdb.com'
__created__ = '2013-01-18 22:06'
__description__ = ''

WX_TOKEN = 'jcr'

import web

urls = (
    '/wx/callback', 'callback')

import hashlib

def sha1_digest(s):
    m = hashlib.sha1()
    m.update(s)
    return m.hexdigest()



class callback:
    def POST(self):
        print 'hello'
        return 'hell'

    def GET(self):
        i = web.input()
        signature = i['signature']
        timestamp = i['timestamp']
        nonce = i['nonce']
        echostr = i['echostr']
        
        a = [WX_TOKEN, timestamp, nonce]
        a.sort()
        a_str = ''.join(a)
        if signature != sha1_digest(a_str):
            return 'not from wx'
        return echostr


if __name__ == '__main__':
    app = web.application(urls, globals())
    #app.wsgifunc()
    app.run()

#!/usr/bin/env python
#_*_coding:utf-8 _*_

__filename__ = 't.py'
__author__ = 'CuiJing'
__email__ = 'cuijing@jcrdb.com'
__created__ = '2013-01-18 22:06'
__description__ = ''

import web

urls = (
    '/wx/callback', 'callback')


app = web.application(urls, globals())


class callback:
    def POST(self):
        print 'hello'
        return 'hell'

    def GET(self):
        return 'OK'


if __name__ == '__main__':
    app.run()


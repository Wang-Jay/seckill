# -*- coding:utf-8 -*-


def saveCookie(cookie):
    file = open('../db/cookie', 'w')
    for key in cookie.keys():
        value = cookie.get(key)
        file.write(key + '=' + value + ';')


def getCookie(cookie):
    cookie.clear()
    file = open('../db/cookie', 'r')
    for line in file.read().split(';'):
        if line.strip() != '':
            key, value = line.strip().split('=', 1)
            cookie.set(key, value, domain='.taobao.com')


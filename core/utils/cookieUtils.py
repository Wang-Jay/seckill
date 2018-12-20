# -*- coding:utf-8 -*-
from core.utils import  constant
from requests.cookies import RequestsCookieJar


def saveLoginCookie(cookie):
    file = open('../db/loginCookie', 'w')
    for key in cookie.keys():
        value = cookie.get(key)
        file.write(key + '=' + value + ';')


def getLoginCookie():
    cookie = RequestsCookieJar()
    file = open('../db/loginCookie', 'r')
    for line in file.read().split(';'):
        if line.strip() != '':
            key, value = line.strip().split('=', 1)
            cookie.set(key, value, domain=constant.domain)
    return cookie


def saveMainCookie(cookie):
    file = open('../db/mainCookie', 'w')
    for key in cookie.keys():
        value = cookie.get(key)
        file.write(key + '=' + value + ';')


def getMainCookie():
    cookie = RequestsCookieJar()
    file = open('../db/mainCookie', 'r')
    for line in file.read().split(';'):
        if line.strip() != '':
            key, value = line.strip().split('=', 1)
            if key == 'lc' or key == 'lid' or key == 'log':
                cookie.set(key, value, domain=constant.loginDomain)
            else:
                cookie.set(key, value, domain=constant.domain)
    return cookie

# -*- coding:utf-8 -*-
from core.utils import constant, fileUtils
from requests.cookies import RequestsCookieJar


def saveLoginCookie(cookie):
    cookieStr = ''
    for key in cookie.keys():
        value = cookie.get(key)
        cookieStr += key + '=' + value + ';'
    fileUtils.saveDbFile('loginCookie', cookieStr)


def getLoginCookie():
    cookie = RequestsCookieJar()
    for line in fileUtils.readDbFile('loginCookie').split(';'):
        if line.strip() != '':
            key, value = line.strip().split('=', 1)
            cookie.set(key, value, domain=constant.domain)
    return cookie


def saveMainCookie(cookie):
    cookieStr = ''
    for key in cookie.keys():
        value = cookie.get(key)
        cookieStr += key + '=' + value + ';'
    fileUtils.saveDbFile('mainCookie', cookieStr)


def getMainCookie():
    cookie = RequestsCookieJar()
    for line in fileUtils.readDbFile('mainCookie').split(';'):
        if line.strip() != '':
            key, value = line.strip().split('=', 1)
            if key == 'lc' or key == 'lid' or key == 'log':
                cookie.set(key, value, domain=constant.loginDomain)
            else:
                cookie.set(key, value, domain=constant.domain)
    return cookie

# -*- coding:utf-8 -*-
import json
import time
import requests
from core.utils import cookieUtils, requestUtils, constant


# 初始化页面，获取cookie
def openLogin():
    result = requests.get(constant.loginUrl)
    cookieUtils.saveLoginCookie(result.cookies)


# 获取二维码链接
def getQrCodeUrl(ks, call):
    result = requests.get(constant.qrCodeUrl % (ks, call, requestUtils.generateUmidToken()), headers=constant.qrHeaders, cookies=cookieUtils.getLoginCookie())
    qrJson = json.loads(requestUtils.extractJson(result.text, call))
    requestUtils.saveQrLgToken(qrJson['lgToken'])
    return qrJson['url']


# 获取二维码状态
def getQrStatus(ks, call, isg):
    cookie = cookieUtils.getLoginCookie()
    cookie.set('isg', isg, domain='.taobao.com')
    result = requests.get(constant.qrLoginUrl % (requestUtils.getQrLgToken(), ks, call), headers=constant.qrHeaders, cookies=cookie)
    print(result.text)
    obj = json.loads(requestUtils.extractJson(result.text, call))
    code = obj['code']
    if '10006' == code:
        return 1, obj['url']
    return 0, 0


# 完成登录
def completeLogin(mainUrl):
    result = requests.get(mainUrl + '&umid_token=' + requestUtils.getUmidToken(), headers=constant.loginHeaders, cookies=cookieUtils.getLoginCookie(), allow_redirects=False)
    cookieUtils.saveMainCookie(result.cookies)
    print(result)
    print(result.headers)


if __name__ == '__main__':
    openLogin()

    v1, v2 = requestUtils.getKsTsAndCallBack()
    print('https:' + getQrCodeUrl(v1, v2))

    while 1 > 0:
        v1, v2 = requestUtils.getKsTsAndCallBack()
        flag, url = getQrStatus(v1, v2, requestUtils.getIsg())
        if flag == 1:
            completeLogin(url)
            break
        time.sleep(2)

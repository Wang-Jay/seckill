# -*- coding:utf-8 -*-
import json
import requests
from core.request import home
from core.utils import cookieUtils, requestUtils, constant


# 初始化页面，获取cookie
def openLogin():
    result = requests.get(constant.loginUrl)
    cookieUtils.saveLoginCookie(result.cookies)


# 获取二维码链接
def getQrCodeUrl():
    ks, call = requestUtils.getKsTsAndCallBack()
    result = requests.get(constant.qrCodeUrl % (ks, call, requestUtils.generateUmidToken()), headers=constant.qrHeaders, cookies=cookieUtils.getLoginCookie())
    qrJson = json.loads(requestUtils.extractJson(result.text, call))
    requestUtils.saveQrLgToken(qrJson['lgToken'])
    return qrJson['url']


# 获取二维码状态
def getQrStatus():
    cookie = cookieUtils.getLoginCookie()
    ks, call = requestUtils.getKsTsAndCallBack()
    cookie.set('isg', requestUtils.getIsg(), domain='.taobao.com')
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
    home.openMain()

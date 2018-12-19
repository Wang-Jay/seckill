# -*- coding:utf-8 -*-
import json
import time
import requests
from requests.cookies import RequestsCookieJar

# ksTs
from core.utils import cookieUtils, requestUtils, constant

cookie_jar = RequestsCookieJar()


# 初始化页面，获取cookie
def openLogin():
    global cookie_jar
    result = requests.get(constant.loginUrl)
    cookie_jar = result.cookies
    cookieUtils.saveCookie(cookie_jar)
    print(result)


# 获取二维码链接
def getQrCodeUrl(ks, call):
    result = requests.get(constant.qrCodeUrl % (ks, call), headers=constant.headers, cookies=cookie_jar)
    qrJson = json.loads(requestUtils.extractJson(result.text, call))
    requestUtils.saveQrLgToken(qrJson['lgToken'])
    return qrJson['url']


# 获取二维码状态
def getQrStatus(ks, call, isg):
    global cookie_jar
    if len(cookie_jar) == 0:
        cookieUtils.getCookie(cookie_jar)
    cookie_jar.set('isg', isg, domain='.taobao.com')
    result = requests.get(constant.qrLoginUrl % (requestUtils.getQrLgToken(), ks, call), headers=constant.headers, cookies=cookie_jar)
    print(result.text)
    obj = json.loads(requestUtils.extractJson(result.text, call))
    code = obj['code']
    print(result.cookies)
    if '10006' == code:
        return 1, obj['url']
    return 0, 0


# 完成登录
def completeLogin(mainUrl):
    result = requests.get(mainUrl, headers=constant.mainHeaders, cookies=cookie_jar, allow_redirects=False)
    print(result)
    print(result.cookies)
    print(result.text)
    print(result.headers)


openLogin()

v1, v2 = requestUtils.getKsTsAndCallBack()
print('https:' + getQrCodeUrl(v1, v2))

while 1 > 0:
    v1, v2 = requestUtils.getKsTsAndCallBack()
    flag, url = getQrStatus(v1, v2, requestUtils.getIsg())
    if flag == 1:
        completeLogin(url)
        break
    time.sleep(1.5)

# completeLogin("https://login.taobao.com/member/loginByIm.do?uid=cntaobaoqq292796135&token=3e9aff3deee4a16f8eac821539522b78&time=1545038494200&asker=qrcodelogin&ask_version=1.0.0&defaulturl=https%3A%2F%2Fwww.taobao.com&webpas=7d56bbc871bc64b79985d82f97eeda951508713642")

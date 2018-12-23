# -*- coding:utf-8 -*-
import json
import requests
from core.utils import cookieUtils, requestUtils, constant


# 初始化首页
def openMain():
    result = requests.get(constant.mainUrl, headers=constant.mainHeaders, cookies=cookieUtils.getMainCookie())
    print(result)


# 获取当前登录状态
def getLoginStatus():
    ks, call = requestUtils.getKsTsAndCallBack()
    result = requests.get(constant.vipUrl % (ks, call), headers=constant.vipHeaders, cookies=cookieUtils.getMainCookie())
    print(result.text)


# 获取迷你购物车
def getMiniCart():
    print(cookieUtils.getMainCookie())
    result = requests.get(constant.miniCartUrl % (constant.cartCallback, requestUtils.getTs()), headers=constant.cartHeaders, cookies=cookieUtils.getMainCookie())
    print(result.text)
    print(result.cookies)


if __name__ == '__main__':
    # getLoginStatus()
    getMiniCart()
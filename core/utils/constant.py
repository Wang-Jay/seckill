# -*- coding:utf-8 -*-
from copy import deepcopy

loginUrl = 'https://login.taobao.com/member/login.jhtml'

qrCodeUrl = 'https://qrlogin.taobao.com/qrcodelogin/generateQRCode4Login.do?from=tb&appkey=00000000&_ksTS=%s&callback' \
            '=jsonp%s&umid_token=%s'

qrLoginUrl = 'https://qrlogin.taobao.com/qrcodelogin/qrcodeLoginCheck.do?lgToken=%s&_ksTS=%s&callback=jsonp%s'

baseHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'DNT': '1',
    'TE': 'Trailers'
}

qrHeaders = deepcopy(baseHeaders)
qrHeaders.update({'Accept': '*/*', 'Host': 'qrlogin.taobao.com', 'Referer': 'https://login.taobao.com/'})

loginHeaders = deepcopy(baseHeaders)
loginHeaders.update({'Host': 'login.taobao.com', 'Referer': 'https://login.taobao.com/member/login.jhtml', 'Upgrade-Insecure-Requests': '1'})

mainHeaders = deepcopy(baseHeaders)
mainHeaders.update({'Host': 'www.taobao.com', 'Referer': 'https://login.taobao.com/', 'Upgrade-Insecure-Requests': '1'})

domain = '.taobao.com'

loginDomain = '.login.taobao.com'

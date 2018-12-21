# -*- coding:utf-8 -*-
import time
from core.request import login

if __name__ == '__main__':
    login.openLogin()
    print('https:' + login.getQrCodeUrl())

    while 1 > 0:
        flag, url = login.getQrStatus()
        if flag == 1:
            login.completeLogin(url)
            break
        time.sleep(2)

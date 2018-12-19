# -*- coding:utf-8 -*-
import time
import uuid
import random

index = 888


def getKsTsAndCallBack():
    global index
    index += int(random.random() * 50)
    ts = int(round(time.time() * 1000))
    return str(ts) + '_' + str(index), index + 1


def extractJson(text, call):
    return str(text)[18 + len(str(call)):-7]


def lgToken():
    return str(uuid.uuid4()).replace('-', '')


def getQrLgToken():
    file = open('../db/qrLgToken', 'r')
    return file.read()


def saveQrLgToken(token):
    file = open('../db/qrLgToken', 'w')
    file.write(token)


def getIsg():
    f = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    i, isg = 0, 'B'
    while i < len(f):
        i += 1
        isg += f[int(random.random() * len(f))]
    return isg

# -*- coding:utf-8 -*-
import time
import uuid
import random
from core.utils import fileUtils

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
    return fileUtils.readDbFile('qrLgToken')


def saveQrLgToken(token):
    fileUtils.saveDbFile('qrLgToken', token)


def getIsg():
    f = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    i, isg = 0, 'B'
    while i < len(f):
        i += 1
        isg += f[int(random.random() * len(f))]
    return isg


def generateUmidToken():
    ts = str(round(time.time() * 1000))
    token = 'C' + ts + '9' + getRandomIntForNumber(10) + ts + getRandomIntForNumber(3)
    fileUtils.saveDbFile('umidToken', token)
    return token


def getUmidToken():
    return fileUtils.readDbFile('umidToken')


def getRandomIntForNumber(number):
    r = ''
    while number > 0:
        r += str(random.choice('0123456789'))
        number -= 1
    return r


if __name__ == '__main__':
    print(generateUmidToken())

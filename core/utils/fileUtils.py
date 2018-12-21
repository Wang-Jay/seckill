# -*- coding:utf-8 -*-
import sys

dbPath = str(sys.path[1]) + '\\db\\'


def readDbFile(fileName):
    file = open(dbPath + fileName, 'r')
    return file.read()


def saveDbFile(fileName, value):
    file = open(dbPath + fileName, 'w')
    file.write(value)
    file.close()

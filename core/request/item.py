# -*- coding:utf-8 -*-
import re
import json
import requests
from bs4 import BeautifulSoup
from core.utils import cookieUtils, requestUtils, constant


# 初始化首页
def getDetail(itemId):
    # result = requests.get(constant.itemUrl % itemId, headers=constant.itemHeaders, cookies=cookieUtils.getMainCookie(), allow_redirects=False)
    result = requests.get(constant.itemUrl % itemId, headers=constant.itemHeaders, allow_redirects=False)
    # print(result)
    # print(result.headers)
    joinData(result.text, itemId)


def confirmOrder(data):
    header = constant.buyHeaders
    # header['Referer'] = header['Referer'] % data['item_id']
    result = requests.post(constant.orderUrl % (data['item_id'], cookieUtils.getMainCookieByName('unb')), headers=header, cookies=cookie, allow_redirects=False)
    print(result)
    print(result.headers)
    print(result.text)


def joinData(html, itemId):
    data = {}
    soup = BeautifulSoup(html, 'html.parser')
    quantity = str(re.findall(r'quantity":(\d+),"', html)[0])
    sellerId = str(re.findall(r'sellerId:"(\d+)",shopId', html)[0])
    skuArr = json.loads(str(re.findall(r'skuList":(.+),"defSelected', html)[0]))
    lines = re.findall(r'name="(.+)" type="hidden" value="(.+)"', str(soup.find(id='J_FrmBid')).replace('input', '\r\n'))
    for k, v in lines:
        data[k] = v
    data['seller_num_id'] = sellerId
    data['skuId'] = skuArr[0]['skuId']
    data['item_url_refer'] = 'https://www.tmall.com/'
    data['allow_quantity'] = quantity
    data['buy_param'] = itemId + '_1_' + skuArr[0]['skuId']
    data['quantity'] = 1
    data['_tb_token_'] = cookieUtils.getMainCookieByName('_tb_token_')
    data['skuInfo'] = skuArr[0]['names']
    data['use_cod'] = 'false'
    data['_input_charset'] = 'UTF-8'
    data['destination'] = '110100'
    data['item_id_num'] = itemId
    data['item_id'] = itemId
    data['auction_id'] = itemId
    data['seller_rank'] = 0
    data['seller_rate_sum'] = 0
    data['is_orginal'] = 'no'
    data['point_price'] = 'false'
    data['secure_pay'] = 'true'
    data['pay_method'] = '款到发货'
    data['from'] = 'item_detail'
    data['buy_now'] = 2998.00
    data['current_price'] = 2998.00
    data['auction_type'] = 'b'
    data['buyer_from'] = 'ecity'
    print(data)
    confirmOrder(data)
    # cna、isg、l、lgc、login、otherx\ubn


if __name__ == '__main__':
    # getDetail('528056263932')
    getDetail('569351931533')

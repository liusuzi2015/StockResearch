#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from importlib import reload
import re
import sys

def getStockName(stockNum):
    response = urllib.request.urlopen('http://quote.eastmoney.com/stocklist.html')
    content = response.read().decode("gbk")

    pattern = re.compile('<li><a.*?href=.*?html">(.*?)\((.*?)\).*?</li>', re.S)
    items = re.findall(pattern, content)

    f = open('stocklist.txt', 'w')
    print(type(items[0][1]))
    for item in items:
        f.write(item[1] + ',' + item[0] + '\n')
        if(item[1] == stockNum):
            result = item[0]
    f.close()

    print(result)
    return result


# if __name__ == '__main__':
#     getStockName("000063")
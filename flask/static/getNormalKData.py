#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tushare as ts
import matplotlib.pyplot as pt
from matplotlib.font_manager import FontManager, FontProperties
import sys
import configparser

from getStockNameByNum import getStockName

def readCfgData():
    conf = configparser.ConfigParser()
    conf.read('StockConfig.ini')
    sections = conf.sections()
    print(sections)

    items = conf.items("stock")
    print(items)
    return items

def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

def generateStockPic(stockId):

    print("stockId " + stockId)
    print(type(stockId))
    name = getStockName(stockId)

    pt.title(stockId + " " + name, fontproperties=getChineseFont())

    data = ts.get_k_data(stockId, start='2017-01-01', end='2019-02-25')

    pt.plot(data['high'], c='g', )
    pt.plot(data['low'], c='r', )
    pt.savefig(stockId+ '.png')

    pt.close()
    # pt.show()

#fund = ts.fund_holdings(2018, 1)

#fund = fund[fund.nlast > 10]

#fund = fund.sort_values(by='nlast', ascending=False)

#fund = fund[0:40]

#print(fund)


def main():

    stockItems = readCfgData()
    for item in stockItems:
        print(item[1])
        generateStockPic(item[1])

if __name__ == '__main__':
    main()
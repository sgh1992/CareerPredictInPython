#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tool.LoadData as Data
from pandas import Series,DataFrame
import scipy
import scipy.stats
from scipy.stats import chisquare
import numpy as np


class ConsumePlaceAnalysize:
    """
    分析不同的消费地点对学生毕业去向的影响.
    即分析不同群体的学生在各个不同的消费地点的行为上是否存在着差异性.
    主要是从两个方面来进行分析:
    1.在不同地点的平均消费金额在不同就业群体中差异性.
    做法就是通过卡方检验来进行验证,并用图形来进行验证.
    2.不同地点的消费频率在不同就业群体中的差异性.
    其验证的思路也就是通过卡方的检验来进行分析的.并用图形化地方式来进行验证.
    """

    def __init__(self, fileName, classAttribute):
        self.chunks = Data.loadData(fileName).chunkData()
        self.classAttribute = classAttribute

    def placeAnalysize(self, placeAttribute, amountAttribute):
        placeAttributeDict = dict()
        classAttributeDict = dict()
        for piece in self.chunks:
            for work, df in piece[piece['type'] == '消费'].groupby(self.classAttribute):
                classAttributeDict.setdefault(work, Series([]))
                classAttributeDict[work] = classAttributeDict[work].add(df.groupby('studentID')[amountAttribute].sum(),fill_value = 0)
            for (place, work), df in piece[piece['type'] == '消费'].groupby([placeAttribute, self.classAttribute]):
                placeAttributeDict.setdefault((place, work), Series([]))
                placeAttributeDict[(place, work)] = placeAttributeDict[(place, work)].add(df.groupby('studentID')[amountAttribute].sum(),fill_value=0)

        #获得每类群体的实际观测值.
        dfObs = Series(placeAttributeDict).apply(lambda x:x.mean()).unstack(fill_value=0)

        #获得每类群体的消费金额占总体消费金额的实际比例.相当于先验概率.
        placeAttributeExp = Series(classAttributeDict).apply(lambda x:x.sum())
        placeAttributeExp = placeAttributeExp/placeAttributeExp.sum()
        placeAttributeExp.fillna(0)

        #根据每类群体的理论分布值来计算其每类群体的理论观测值.
        dfExp = DataFrame([], index=dfObs.index, columns=dfObs.columns)
        df = Series(placeAttributeDict).apply(lambda x:x.sum()).unstack(fill_value=0)
        for index in dfObs.index:
            dfExp.ix[index] = df.ix[index].sum()
        dfExp = dfExp.mul(placeAttributeExp).fillna(0)/(Series(placeAttributeDict).apply(lambda x:x.size)).unstack(fill_value=0)

        #注意理解卡方的计算方式,期望值为0时，则所计算出的卡方值是会有问题的.
        dfExp = dfExp.replace([np.inf, -np.inf], np.nan).fillna(0.000001)

        #返回其计算的卡方值,pvalue值,其期望的值与实际观测的值.
        return chisquare(dfObs.stack(), dfExp.stack()), dfExp, dfObs
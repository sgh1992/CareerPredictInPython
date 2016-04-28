#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from pandas import Series

import tool.LoadData as Data


class simpleAnalysize:

    """
    分析单个因素对消费金额的影响.
    """
    def __init__(self, fileName, attribute):
        self.chunks = Data.loadData(fileName).chunkData()
        self.attribute = attribute

    def analysize(self):
        """
        分析每个不同因素中，各类群体平均总的消费金额.
        """
        attributeSeries = Series([])
        attributeDict = dict()
        for piece in self.chunks:

            attributeSeries = attributeSeries.add(piece.groupby(self.attribute).amount.sum(), fill_value=0.0)

            #注意以下语句的使用方式.经过民族分组之后的学号可能不一定是唯一的.因此还需要通过nunique即返回唯一的大小.
            #attributeCount = attributeCount.add(piece.groupby(self.attribute).studentID.nunique(), fill_value=0.0)

            for attribute,idArray in piece.groupby(self.attribute).studentID.unique().iteritems():
                attributeDict.setdefault(attribute, np.array([]))
                attributeDict[attribute] = np.union1d(attributeDict[attribute], idArray)
        return (attributeSeries/(Series(attributeDict).apply(lambda x : len(x)))).sort_values()

    def plotPicture(self, location):
        seriesData = self.analysize()
        plt.figure(figsize=(16,12))
        seriesData.plot(kind='barh', title=self.attribute)
        plt.savefig('%s/%s.pdf' % (location, self.attribute), dpi=199, bbox_inches='tight')
        plt.close()
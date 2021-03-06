#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tool.LoadData as Data
import numpy as np
from pandas import Series,DataFrame
import scipy
import scipy.stats
from scipy.stats import chisquare
import matplotlib.pyplot as plt


class ChiSquare:

    def __init__(self, fileName,classAttribute):
        """
        全局属性的初始化.
        """
        self.fileName = fileName
        self.chunks = Data.loadData(fileName).chunkData()
        self.classAttribute = classAttribute

    def chi(self, customattribute):
        """
        计算其卡方值.
        """
        attributeDict = dict()
        classAttributeDict = dict()
        for piece in self.chunks:
            for (attribute, classAttribute), arrays in piece.groupby([customattribute, self.classAttribute]).studentID.unique().iteritems():
                attributeDict.setdefault((attribute, classAttribute), np.array([]))
                attributeDict[(attribute, classAttribute)] = np.union1d(attributeDict[(attribute, classAttribute)], arrays)

            for classAttribute, arrays in piece.groupby(self.classAttribute).studentID.unique().iteritems():
                classAttributeDict.setdefault(classAttribute, np.array([]))
                classAttributeDict[classAttribute] = np.union1d(classAttributeDict[classAttribute], arrays)

        #各个类别的毕业去向群体中所占的比例.
        classSeries = Series(classAttributeDict).apply(lambda x:len(x))
        classSeries /= classSeries.sum()

        #在各个attribute上的实际观测值.
        attributeObs = Series(attributeDict).apply(lambda x:len(x)).unstack(fill_value=0)

        attributeExp = DataFrame(index=attributeObs.index, columns=attributeObs.columns)

        #设置初始值.
        for index in attributeExp.index:
            attributeExp.ix[index] = attributeObs.ix[index].sum()
        #根据各个目标类别中的比例来获得其期望值.
        attributeExp = attributeExp.mul(classSeries).fillna(0)
        #根据实际观测值与期望值来计算其卡方值，并返回p-value值.
        return chisquare(attributeObs.stack(), attributeExp.stack()), attributeObs


    def plotComparePictures(self,attributeList,location):
        for attribute in attributeList:
            attributeObs = ChiSquare(self.fileName, self.classAttribute).chi(attribute)[1]
            attributeObs = attributeObs.div(attributeObs.sum(1).astype(float),axis = 0)
            attributeObs.plot(kind='barh', figsize=(16, 16))
            plt.savefig('%s/%s_chi.pdf' % (location, attribute))
            plt.close()
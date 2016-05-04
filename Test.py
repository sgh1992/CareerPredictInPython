#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dataPrepare.consume.SimpleAnalysize as Analysize
import tool.ChiSquare as Chi
import dataPrepare.consume.ConsumePlaceAnalysize as CPA

class Test:
    """
    测试.
    """
    def __init__(self,fileName):
        self.fileName = fileName

    def plotPictures(self, attributeList,location):
        """
        测试单因素分析结果
        """
        for attribute in attributeList:
            Analysize.simpleAnalysize(self.fileName, attribute).plotPicture(location)

    def chiTest(self,attributeList,classAttribute):

        for attribute in attributeList:
            x2,pvalue = Chi.ChiSquare(self.fileName, attribute, classAttribute).chi()
            print '%s and %s chisquare value is:%f\tpvalue:%f' % (attribute,classAttribute, x2, pvalue)

    def ConsumePlaceTest(self, placeAttribute,amountAttribute, classAttribute):
        print CPA.ConsumePlaceAnalysize(self.fileName,classAttribute).placeAnalysize(placeAttribute,amountAttribute)



fileName = '/home/sghipr/graduateStudentsForConsumeAndBasicInfo.csv'
classAttribute='work'
placeAttribute='kind'
amountAttribute='amount'
Test(fileName).ConsumePlaceTest(placeAttribute,amountAttribute,classAttribute)
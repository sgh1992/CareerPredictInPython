#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tool.LoadData as Data
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
class TimeSeries:

    """
    分析不同群体的学生在其一天之中的行为规律性.
    主要方法就是将一天划分为60 * 24 ＝ 1440分钟.
    统计不同群体的学生在每一分钟内的刷卡次数
    """

    def __init__(self, fileName, classAttribute):
        self.chunks = Data.loadData(fileName).chunkData()
        self.classAttribute = classAttribute

    def timeAnalysize(self, timeAttribute,rankYear = '2010',startTime = '20100901',endTime = '20110201'):

        """
        rankYear:针对这个年级
        startTime - endTime 在这个时间段内
        """
        timeDict = dict()
        for piece in self.chunks:
            piece['rank'] = np.where(piece['studentID'].astype(np.string_).str.startswith('2010'), '2010', '2009')
            piece.dti = pd.DatetimeIndex(piece[timeAttribute])
            piece['minute'] = piece.dti.hour * 60 + piece.dti.minute

            for (minute, work), df in piece[(piece.rank == rankYear) & (piece.dti >= pd.Timestamp(startTime)) & (piece.dti <= pd.Timestamp(endTime))].groupby(['minute', self.classAttribute]):
                timeDict.setdefault((minute, work), 0.0)
                timeDict[(minute, work)] += len(df.index)
        return Series(timeDict).unstack(fill_value=0)
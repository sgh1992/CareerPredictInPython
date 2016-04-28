#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame

fileName = '/home/sghipr/graduateStudentsForConsumeAndBasicInfo.csv'
class loadData:

    def __init__(self, fileName):
        """
        初始化数据源
        """
        self.fileName = fileName

    def chunkData(self, chunkSize = 500000):
        """
        分片读取数据.
        """
        chunks = pd.read_csv(self.fileName, header=None,
                             names=['studentID', 'nation', 'gender', 'political', 'college', 'major', 'type', 'transferPlace',
                                    'kind', 'position', 'deviceID', 'time', 'amount', 'balance', 'work'],
                             chunksize=chunkSize)
        return chunks

    def allData(self):
        """
        导出所有的数据.不用分片.
        """
        return pd.read_csv(self.fileName, header=None,
                             names=['studentID', 'nation', 'gender', 'political', 'college', 'major', 'type',
                                    'transferPlace',
                                    'kind', 'position', 'deviceID', 'time', 'amount', 'balance', 'work'])
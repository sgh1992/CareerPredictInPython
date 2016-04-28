#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

fileName = '/home/sghipr/graduateStudentsForConsumeAndBasicInfoTemp.csv'
data = pd.read_csv(fileName,names=['StudentID','nation','gender','political','college','major','transferPlace','kind','position','deviceID','time','amount','balance','work'])
data.ix[0,'nation']
data.groupby()



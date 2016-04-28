#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

step = np.random.randint(0,2,size= (5000,1000))
print step.shape
walk = np.where(step > 0,1,-1)
walkcum = walk.cumsum(1)
print walkcum
index = np.where(np.abs(walkcum) > 30, 1, -1)
index = np.any(index,axis=1)

index = (np.abs(walkcum) > 30).any(1)
print index.sum()
print index

#每次随机散步中，最早离原点距离30时是在第几次漫步.
print np.argmax(walkcum[index],axis=1)
print np.mean(np.argmax(walkcum[index],axis=1))
pd.Index

obj = Series([1,2,3])

obj.reindex()

data = DataFrame([[1,2,3],[4,5,6]])
data.drop()

np.argsort()

obj.rank()

obj.sort_values()


data.tail()

data.cov()

data.cov()

data.corr()

data.dropna()

data.loc


data.fillna()

data.unstack()


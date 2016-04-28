#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import matplotlib.pyplot as plt

import numpy as np

walk = []

for i in xrange(1000):
    walk.append(1 if random.randint(0,1) else -1)
print walk
walkcum = np.array(walk).cumsum()

plt.plot(walkcum)
plt.show()
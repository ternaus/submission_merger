from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs softmax regression
Right now it works for Wallmart competition
'''

import os
import sys
import pandas as pd
import time
import math
import numpy as np
import decimal

def logit(p):
  return -math.log(p/(1-p))

def inv_logit(p):
  return 1 / (1 + decimal.Decimal(p).exp())


files = sys.argv[1:]

try:
  files.remove('softmax_merger.py')
except:
  pass

data = [pd.read_csv(fName) for fName in files]
ids = data[0]['id']

result  = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['units'].apply(inv_logit)
  ind += 1

submission['units'] = result.mean(axis=1)

submission['units'] = submission['units'].apply(logit)

submission['id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
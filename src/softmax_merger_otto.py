from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs softmax regression for otto competition
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
  # return 1.0 / (1.0 +   p)


files = sys.argv[1:]

try:
  files.remove('softmax_merger_otto.py')
except:
  pass



data = [pd.read_csv(fName) for fName in files]
ids = data[0]['id']

columns_names = list(data[0].columns)

columns_names.remove('id')
result = pd.DataFrame()
submission = pd.DataFrame()

eps = 1e-15

for column in columns_names:
  ind = 0
  temp = pd.DataFrame()
  temp[ind] = data[0][column].apply(lambda x: x + eps).apply(math.log)
  ind += 1
  for df in data[1:]:
    temp[ind] = df[column].apply(lambda x: x + eps).apply(math.log, 1)
    ind += 1

  submission[column] = temp.mean(axis=1).apply(math.exp)


submission = submission.div(submission.sum(axis=1), axis=0)

submission['id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
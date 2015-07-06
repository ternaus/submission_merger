from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs average regression
Right now it works for search competition
'''

import os
import sys
import pandas as pd
import time

files = sys.argv[1:]
try:
  files.remove('mean_merger_search.py')
except:
  pass


data = [pd.read_csv(fName) for fName in files]
ids = data[0]['id']

result  = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['prediction']
  ind += 1

submission['prediction'] = result.mean(axis=1).apply(lambda x: round(x), 1).astype(int)
submission['id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs average regression
Right now it works for Wallmart competition
'''

import os
import sys
import pandas as pd
import time

files = sys.argv[1:]
try:
  files.remove('mean_merger_facebook.py')
except:
  pass


data = [pd.read_csv(fName) for fName in files]
ids = data[0]['bidder_id']

result  = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['prediction']
  ind += 1

submission['prediction'] = result.mean(axis=1)
submission['bidder_id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
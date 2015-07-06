from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs average regression
'''

import os
import sys
import pandas as pd
import time

files = sys.argv[1:]
try:
  files.remove('mean_merger_nile.py')
except:
  pass


data = [pd.read_csv(fName) for fName in files]
ids = data[0]['Id']

result  = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['WnvPresent']
  ind += 1

submission['WnvPresent'] = result.mean(axis=1)
submission['Id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
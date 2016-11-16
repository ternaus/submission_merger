from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs average for https://www.kaggle.com/c/allstate-claims-severity
'''

import sys
import pandas as pd
import time

files = sys.argv[1:]
try:
  files.remove('mean_merger_allstate.py')
except:
  pass


data = [pd.read_csv(fName).sort_values(by='id') for fName in files]
ids = data[0]['id'].values

result = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['loss']
  ind += 1

submission['loss'] = result.mean(axis=1).values
submission['id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
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
import math

files = sys.argv[1:]
try:
  files.remove('geometric_mean_merger_search.py')
except:
  pass


data = [pd.read_csv(fName) for fName in files]
ids = data[0]['id']

result  = pd.DataFrame()
submission = pd.DataFrame()

ind = 0

submission['id'] = ids

submission['prediction'] = 1

for df in data:
  submission['prediction'] = submission['prediction'] * df['prediction']
  
power = 1.0 / len(data)

submission['prediction'] = submission['prediction'].apply(lambda x: round(math.pow(x, power))).astype(int)


submission['id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
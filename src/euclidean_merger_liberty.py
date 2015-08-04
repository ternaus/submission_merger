from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs average
'''

import os
import sys
import pandas as pd
import time
import math

files = sys.argv[1:]
try:
  files.remove('euclidean_merger_liberty.py')
except:
  pass

data = [pd.read_csv(fName) for fName in files]
ids = data[0]['Id']

result = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['Hazard'].apply(lambda x: x**2, 1)
  ind += 1

submission['Hazard'] = result.mean(axis=1)
submission['Id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
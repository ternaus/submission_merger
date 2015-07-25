from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs geometric average regression
Right now it works for avito competition
'''

import os
import sys
import pandas as pd
import time
import math

files = sys.argv[1:]
try:
  files.remove('geometric_mean_merger_avito.py')
except:
  pass


data = [pd.read_csv(fName) for fName in files]
ids = data[0]['ID']

result = pd.DataFrame()
submission = pd.DataFrame()

ind = 0

submission['ID'] = ids

submission['IsClick'] = 1

for df in data:
  submission['IsClick'] = submission['IsClick'] * df['IsClick']
  
power = 1.0 / len(data)

submission['IsClick'] = submission['IsClick'].apply(lambda x: math.pow(x, power))


submission['ID'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
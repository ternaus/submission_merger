from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs geometric average regression
Right now it works for diabetic competition
'''

import os
import sys
import pandas as pd
import time
import math

files = sys.argv[1:]
try:
  files.remove('geometric_mean_merger_diabetic.py')
except:
  pass


data = [pd.read_csv(fName) for fName in files]
ids = data[0]['image']

result  = pd.DataFrame()
submission = pd.DataFrame()

ind = 0

submission['image'] = ids

submission['level'] = 1

for df in data:
  submission['level'] = submission['level'] * df['level']
  
power = 1.0 / len(data)

submission['level'] = submission['level'].apply(lambda x: math.pow(x, power))


submission['image'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)
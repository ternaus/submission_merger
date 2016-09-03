"""
This scripts merges several csv files that are used to perform Kaggle submission

for competition https://www.kaggle.com/c/talkingdata-mobile-user-demographics
"""
from __future__ import division

import sys
import pandas as pd
import time


files = sys.argv[1:]
try:
  files.remove('mean_merger_talkingdata.py')
except:
  pass

data = [pd.read_csv(fName).sort_values(by='device_id') for fName in files]
ids = data[0]['device_id']


columns_names = list(data[0].columns)

columns_names.remove('device_id')
result = pd.DataFrame()
submission = pd.DataFrame()

for column in columns_names:
  ind = 0
  temp = pd.DataFrame()
  temp[ind] = data[0][column]
  ind += 1
  for df in data[1:]:
    temp[ind] = df[column]
    ind += 1

  submission[column] = temp.mean(axis=1)


submission = submission.div(submission.sum(axis=1), axis=0)

submission['device_id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)

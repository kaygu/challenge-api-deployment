'''
This python module will contain all the code to preprocess your data. Make sure to think about what will be the format of your data to fit the model. Also, be sure to know which information HAVE to be there and which one can be empty (NAN).


will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the NaN values, handle text data, etc...).

This file should contain a function called preprocess() that will take a new house's data as input and return those data preprocessed as output.

If your data doesn't contain the required information, you should return an error to the user.
'''

from typing import Union
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess(raw_data: dict, scaler: StandardScaler = None) -> Union[pd.DataFrame, None]:
  '''
  Return all the params or error if param is missing
  '''
  # Transform dict to df, then fill empty columns with zeros, also fill dummies
  dummy_df = pd.read_csv('preprocessing/dummy.csv')
  data = pd.DataFrame(raw_data, index=[0, ])
  # Check for mandatory feature, return None if some is missing
  mandatory = ['living_surface', 'type', 'bedroom_count', 'postal_code']
  for m in mandatory:
    if m not in data.columns:
      return None
  data.replace(False, 0, inplace=True)
  data.replace(True, 1, inplace=True)
  data = pd.get_dummies(data, columns=['type', 'postal_code'])
  if 'condition' in data.columns:
    data = pd.get_dummies(data, columns=['condition'])

  # Return None if one column is not supposed to exist (not in dummy df)
  for c in data.columns:
    if c not in dummy_df.columns:
      return None

  # Override dummy df with user data, and keed defaults for missing info
  dummy_df[data.columns] = data[data.columns]
  
  return dummy_df
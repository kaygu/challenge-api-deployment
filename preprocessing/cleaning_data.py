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

# bedroom_count,bathroom_count,postal_code,facades,living_surface,garden_surface,terrace,swimming_pool,fireplace,type,condition

def preprocess(raw_data: dict, scaler: StandardScaler = None) -> Union[pd.DataFrame, None]:
  '''
  Return all the params or error if param is missing
  '''
  # Check for mandatory feature
  # Transform dict to df, then fill empty columns with zeros, also fill dummies

  # Set features
  features = np.zeros(19)
  features[0] = np.float64(raw_data['bedroom_count'] or 0) # bedroom_count

  return features
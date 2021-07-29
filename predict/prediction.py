from typing import Union
import pandas as pd
from sklearn.linear_model import LinearRegression


def predict(model: LinearRegression, df: pd.DataFrame) -> Union[float, None]:
  try:
    result = model.predict(df)
    result = result[0]
  except:
    return None
  return result
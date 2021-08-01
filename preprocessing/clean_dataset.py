import pandas as pd


if __name__ == '__main__':
  df = pd.read_csv('immo.csv')

  df.drop(['Unnamed: 0', 'url', 'id', 'transaction_type', 'subtype', 'attic', 'basement', 'fitness_room', 'tennis_court', 'sauna', 'jacuzzi', 'hammam', 'construction_year'], axis=1, inplace=True)

  # Surfaces
  df['living_surface'] = df['living_surface'].fillna(0)
  df['garden_surface'] = df['garden_surface'].fillna(0)
  df['terrace_surface'] = df['terrace_surface'].fillna(0)
  df.loc[df["terrace_surface"] > 1, "terrace_surface"] = 1
  df.rename(columns={"terrace_surface": "terrace"}, inplace=True)

  # Pool & fireplace
  df['swimming_pool'] = df['swimming_pool'].fillna(0)
  df['fireplace'] = df['fireplace'].fillna(0)

  # Rooms
  df['bedroom_count'] = df['bedroom_count'].fillna(0)
  df['bathroom_count'] = df['bathroom_count'].fillna(0)
  df['showerroom_count'] = df['showerroom_count'].fillna(0)
  df['bathroom_count'] = df['bathroom_count'] + df['showerroom_count']
  del df['showerroom_count']

  # Change booleans to numerical values
  df.replace(False, 0, inplace=True)
  df.replace(True, 1, inplace=True)

  # remove adresses
  df.drop(['region', 'province', 'district', 'locality', 'street_name', 'street_number'], axis=1, inplace=True)
  # Transform categories to booleans
  df = pd.get_dummies(df, columns=['type', 'postal_code', 'condition'])
  df.dropna(inplace=True)
  df = df.astype('int32')

  # Create default dataframe to fill with all the 
  dummy_df = pd.DataFrame(df.iloc[0,:])
  dummy_df = dummy_df.T
  dummy_df[df > 0] = 0
  dummy_df = dummy_df.astype('int32')
  dummy_df.drop("price", axis=1, inplace=True)

  df.to_csv('model/dataset.csv', index=False)
  dummy_df.to_csv('preprocessing/dummy.csv', index=False)

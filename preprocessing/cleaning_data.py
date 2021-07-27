'''
This python module will contain all the code to preprocess your data. Make sure to think about what will be the format of your data to fit the model. Also, be sure to know which information HAVE to be there and which one can be empty (NAN).


will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the NaN values, handle text data, etc...).

This file should contain a function called preprocess() that will take a new house's data as input and return those data preprocessed as output.

If your data doesn't contain the required information, you should return an error to the user.
'''

# Missing: kitchen type, house equiped / unequiped

import pandas as pd

df = pd.read_csv('../immo.csv')

df.drop(['Unnamed: 0', 'url', 'id', 'transaction_type', 'subtype', 'attic', 'basement', 'fitness_room', 'tennis_court', 'sauna', 'jacuzzi', 'hammam', 'construction_year'], axis=1, inplace=True)
print(df.columns)

df['living_surface'] = df['living_surface'].fillna(0)
df['garden_surface'] = df['garden_surface'].fillna(0)
df['terrace_surface'] = df['terrace_surface'].fillna(0)
df['swimming_pool'] = df['swimming_pool'].fillna(0)
df['fireplace'] = df['fireplace'].fillna(0)

df['bedroom_count'] = df['bedroom_count'].fillna(0)
df['bathroom_count'] = df['bathroom_count'].fillna(0)
df['showerroom_count'] = df['showerroom_count'].fillna(0)


df.replace(False, 0, inplace=True)
df.replace(True, 1, inplace=True)

print(df.shape)
no_addr = df.drop(['region', 'province', 'district', 'locality', 'street_name', 'street_number'], axis=1)
df.dropna(inplace=True)
no_addr.dropna(inplace=True)

print(no_addr.shape) # Around 10k rows without adresses (do not remove rows if adress is incomplete
print(df.shape) # Around 6k rows with the adresses (drop incomplete adresses)
print(df.head())

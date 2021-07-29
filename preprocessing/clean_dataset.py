import pandas as pd

df = pd.read_csv('immo.csv')

df.drop(['Unnamed: 0', 'url', 'id', 'transaction_type', 'subtype', 'attic', 'basement', 'fitness_room', 'tennis_court', 'sauna', 'jacuzzi', 'hammam', 'construction_year'], axis=1, inplace=True)

df['living_surface'] = df['living_surface'].fillna(0)
df['garden_surface'] = df['garden_surface'].fillna(0)
df['terrace_surface'] = df['terrace_surface'].fillna(0)

df['swimming_pool'] = df['swimming_pool'].fillna(0)
df['fireplace'] = df['fireplace'].fillna(0)

df['bedroom_count'] = df['bedroom_count'].fillna(0)
df['bathroom_count'] = df['bathroom_count'].fillna(0)
df['showerroom_count'] = df['showerroom_count'].fillna(0)
df['bathroom_count'] = df['bathroom_count'] + df['showerroom_count']
del df['showerroom_count']

# df['condition'] = df['condition'].fillna('undefined')

# Change booleans to numerical values
df.replace(False, 0, inplace=True)
df.replace(True, 1, inplace=True)

# remove adresses
df.drop(['province', 'district', 'locality', 'street_name', 'street_number'], axis=1, inplace=True)
df = pd.get_dummies(df, columns=['type'])
df = pd.get_dummies(df, columns=['region'], drop_first=True)
df = pd.get_dummies(df, columns=['condition'], dummy_na=True)
df.dropna(inplace=True)

df.to_csv('dataset.csv', index=False)

import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

if __name__ == '__main__':
  df = pd.read_csv('model/dataset.csv')

  Y_feature = df["price"]
  X_features = df.drop("price", axis=1)


  x_train, x_test, y_train, y_test = train_test_split(X_features, Y_feature, test_size=0.20, random_state=13)

  # scaler = StandardScaler()

  # normalized_x_train = pd.DataFrame(scaler.fit_transform(x_train), columns = x_train.columns)
  regressor = LinearRegression()
  regressor.fit(x_train, y_train) # fit(normalized_x_train, y_train)

  # normalized_x_test = pd.DataFrame(scaler.transform(x_test), columns = x_test.columns)

  score = regressor.score(x_test, y_test) # score(normalized_x_test, y_test)
  print(score)

  with open('model/model.pkl', 'wb') as io: 
    pickle.dump(regressor, io)
    # pickle.dump(scaler, io)
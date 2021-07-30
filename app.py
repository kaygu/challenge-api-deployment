import pickle
from flask import Flask, request

from predict.prediction import predict
from preprocessing.cleaning_data import preprocess

app = Flask(__name__)
with open('model/model.pkl', 'rb') as io:
  model = pickle.load(io)
  # scaler = pickle.load(io)

@app.route('/')
def home():
  return {'ping': 'alive'}

@app.route('/predict', methods=['GET', 'POST'])
def predict_prices():
  if request.method == 'POST':
    try:
      data = request.get_json()
      data = data['data']
      assert data != None
    except:
      return {"error": "Invalid data"}, 400
    df = preprocess(data)
    if df is not None:
      prediction = predict(model, df)
      if prediction:
        return {"result": prediction}
      else:
        return {"error": "An unexpected error happend when predicting the price"}, 400
    else:
      return {"error": "Given data is incorrect or required data is missing"}, 400
    
  else:
    return {"usage": "send format here"}


if __name__ == '__main__':
  app.run(port=8080, host='0.0.0.0')
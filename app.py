import os
import pickle
from flask import Flask, request
from flask_cors import CORS

from predict.prediction import predict
from preprocessing.cleaning_data import preprocess

app = Flask(__name__)
cors = CORS(app)
port = int(os.environ.get("PORT", 8080))
with open('model/model.pkl', 'rb') as io:
  model = pickle.load(io)
  # scaler = pickle.load(io)

@app.route('/')
def home():
  return {'status': 'alive'}

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
        return {"prediction": prediction}
      else:
        return {"error": "An unexpected error happend when predicting the price"}, 400
    else:
      return {"error": "Given data is incorrect or required data is missing"}, 400
    
  else:
    return {"usage": "send format here"}


if __name__ == '__main__':
  app.run(port=port, host='0.0.0.0')
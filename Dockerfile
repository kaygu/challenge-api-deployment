FROM ubuntu:18.04
FROM python:3.8
COPY requirements.txt .
RUN pip3 install --upgrade -r requirements.txt

RUN mkdir /app

COPY model /app/model
COPY predict /app/predict
COPY preprocessing /app/preprocessing
COPY app.py /app/app.py
COPY immo.csv /app/immo.csv

WORKDIR /app

RUN python3 ./preprocessing/clean_dataset.py
RUN python3 ./model/model.py

EXPOSE 8080

CMD ["python3", "app.py"]
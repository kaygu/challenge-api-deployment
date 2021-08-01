# challenge-api-deployment

## Description

In that project we have created a prediction model to predict properties prices.<br />
The real estate data has been scrapped, celeaned and analysed in our previous projects. In this project we create a model to predict prices and we serve it with a flask API.<br />
The API is wrapped in a Docker container and deployed by Heroku.

## Installation

```bash
git clone git@github.com:kaygu/challenge-api-deployment.git
cd challenge-api-deployment
pip install -r requirements.txt 
```

## Usage

Run the flask app localy

```bash
python3 app.py
```

## Docker

Build Docker image

```bash
docker build . -t predict_api:latest
```

Run container

```bash
docker run -it -p 8080:8080 predict_api:latest
```

## API

You can access the application at https://predict-immo.herokuapp.com/

### /

* GET

```json
{"status": "alive"}
```

### /predict

* POST

Input

```json
{
  "data": {
    "type": "APARTMENT" | "HOUSE" | "OTHERS",
    "living_surface": int,
    "bedroom_count": int,
    "postal_code": int,
    "bathroom_count": Optional[int],
    "facades": Optional[int],
    "garden_surface": Optional[int],
    "swimming_pool": Optional[bool],
    "fireplace": Optional[bool],
    "terrace": Optional[bool],
    "condition": Optional[
      "AS_NEW" | "GOOD" | "JUST_RENOVATED" | "TO_BE_DONE_UP" | "TO_RENOVATE" | "TO_RESTORE"
    ]
  }
}
```

Output

```json
{
    "prediction": float
}
```

or

```json
{
    "error": str
}
```

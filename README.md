# Customer Churn Prediction API

This is a FastAPI-based web service for predicting customer churn using a trained logistic regression model.

## Usage

- `POST /predict_churn` with a JSON body:
```json
{
  "features": [45, 60.5, 12, 1, 0, 3, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
}
```

Returns:
```json
{
  "churn": true,
  "probability": 0.82
}
```

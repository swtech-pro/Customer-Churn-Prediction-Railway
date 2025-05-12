# 🧠 Customer Churn Prediction API – Railway Deployment

This FastAPI project predicts customer churn using a logistic regression model. It’s fully compatible with Railway.app and uses a local `.pkl` model file.

## 🚀 How to Deploy on Railway

1. Push this folder to a GitHub repo
2. Go to [https://railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
5. That's it! Your API will be live at a Railway-generated URL

## 🧪 API Usage

**POST** `/predict_churn`

Request body:
```json
{
  "features": [45, 60.5, 12, 1, 0, 3, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
}
```

Response:
```json
{
  "churn": true,
  "probability": 0.78
}
```

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import joblib
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Customer Churn Prediction API is running."}

# Load model safely
try:
    model = joblib.load("churn_model.pkl")
except Exception as e:
    model = None
    print("❌ Error loading model:", e)

@app.post("/predict_churn")
async def predict_churn(request: Request):
    try:
        data = await request.json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        return {"churn": bool(prediction), "probability": round(float(probability), 3)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

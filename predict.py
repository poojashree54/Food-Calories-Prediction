from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Create app
app = FastAPI(
    title="Indian Food Calorie Predictor API",
    description="Predict calories of food items using a trained ML model",
    version="1.0"
)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("dv.pkl", "rb") as f_in:
    dv = pickle.load(f_in)


# Health check
@app.get("/")
def home():
    return {"status": "Indian Food Calorie Predictor API is running"}


# Predict endpoint
@app.post("/predict")
def predict(data: dict):
    X = dv.transform([data])
    prediction = model.predict(X)[0]
    return {"Nutrition predictions": round(float(prediction), 2)}
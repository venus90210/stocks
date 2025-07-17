from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

# Reemplace esto con su implementación:
class ApiInput(BaseModel):
    features: List[float]

# Reemplace esto con su implementación:
class ApiOutput(BaseModel):
    forecast: float

app = FastAPI()
model = joblib.load("model.joblib")


# Reemplace esto con su implementación:
@app.post("/predict")
async def predict(data: ApiInput) -> ApiOutput:
      ### ESCRIBA SU CÓDIGO AQUÍ ###
  prediction = ApiOutput(forecast=model.predict([data.features])[0])
  return prediction

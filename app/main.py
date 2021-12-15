from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# define base model
class ModelInput(BaseModel):
    temperature: int


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health/")
def health():
    return {"Status": "healthy"}


@app.post("/score/")
def score(input_values: ModelInput):

    # your anomaly model here
    anomaly = input_values.temperature > 25

    return {"anomaly": anomaly}
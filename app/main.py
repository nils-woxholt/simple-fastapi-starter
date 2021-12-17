# imported
from fastapi import FastAPI
# local
from interface import ModelInput, ModelOutput 
from score import run_model

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health/")
def health():
    return {"Status": "healthy"}

@app.post("/score/", response_model=ModelOutput)
def score_func(input_values: ModelInput):

    # your anomaly model here
    output = run_model(input_values.temperature)

    return output
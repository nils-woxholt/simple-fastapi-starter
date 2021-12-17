"""
imitates a model score file
"""
from interface import ModelOutput

def run_model(temperature: int):
    """
    dummy model
    """
    anomaly = temperature < 10 or temperature > 25
    return {"anomaly": anomaly}

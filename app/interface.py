from pydantic import BaseModel

# define base model
class ModelInput(BaseModel):
    temperature: int

class ModelOutput(BaseModel):
    anomaly: bool

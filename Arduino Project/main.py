from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class SensorData(BaseModel):
    sensor: str
    temperature: float
    humidity: Optional[float] = None  # koska LM35 ei sisällä kosteutta

@app.post("/sensor")  
async def receive_sensor_data(data: SensorData):
    print(f"Received data: {data}")
    return {"message": "Data received successfully"}

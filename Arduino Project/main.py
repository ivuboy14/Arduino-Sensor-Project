from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from collections import deque
import time

app = FastAPI()

# HTML ja staattiset tiedostot
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tietomalli
class SensorData(BaseModel):
    sensor: str
    temperature: float
    humidity: Optional[float] = None

# Tallennetaan viimeisin data ja historia
latest_data = {
    "DHT11": {},
    "LM35": {}
}

sensor_history = {
    "DHT11": deque(maxlen=20),
    "LM35": deque(maxlen=20)
}

# Reitit
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/sensor")
async def receive_sensor_data(data: SensorData):
    latest_data[data.sensor] = data.dict()
    sensor_history[data.sensor].append({
        "timestamp": time.time(),
        "temperature": data.temperature,
        "humidity": data.humidity
    })
    return {"message": "Data received successfully"}

@app.get("/data")
async def get_latest_data():
    return JSONResponse(content=latest_data)

@app.get("/history")
async def get_history():
    return JSONResponse(content={
    "DHT11": list(sensor_history["DHT11"]),
    "LM35": list(sensor_history["LM35"])
})


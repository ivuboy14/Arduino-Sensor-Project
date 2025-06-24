import serial
import requests
import time

PORT = "COM3"  
BAUD = 9600
URL = "http://127.0.0.1:8000/sensor"

ser = serial.Serial(PORT, BAUD)
time.sleep(2)  # Odotetaan sarjayhteyden alustusta

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        print("Received:", line)

        if "DHT11" in line:
            # DHT11: temperature: 21.90°C , humidity: 51.00%
            parts = line.split(":")
            temp_str = parts[2].split("°")[0].strip()
            humidity_str = parts[3].split("%")[0].strip()

            data = {
                "sensor": "DHT11",
                "temperature": float(temp_str),
                "humidity": float(humidity_str)
            }

        elif "LM35" in line:
            # LM35: temperature: 31.28°C
            parts = line.split(":")
            temp_str = parts[2].split("°")[0].strip()

            data = {
                "sensor": "LM35",
                "temperature": float(temp_str)
            }
        else:
            continue  # Ohitetaan tyhjät tai tunnistamattomat rivit

        # Lähetetään data
        response = requests.post(URL, json=data)
        print("Sent:", data, "Status:", response.status_code)

    except Exception as e:
        print("Error:", e)
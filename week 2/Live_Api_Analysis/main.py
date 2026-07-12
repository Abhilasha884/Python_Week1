from fastapi import FastAPI
import requests
import pandas as pd

app=FastAPI()

@app.get('/')

def home():
    return{"Weather Analysis"}


def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=18.5204&longitude=73.8567&current=temperature_2m,relative_humidity_2m,wind_speed_10m,apparent_temperature"
    response=requests.get(url)
    return response.json()

def create_dataframe(data):

    current = data["current"]

    weather = {
        "Temperature":[current["temperature_2m"]],
        "Humidity":[current["relative_humidity_2m"]],
        "Wind Speed":[current["wind_speed_10m"]],
        "Feels Like":[current["apparent_temperature"]]
    }

    df = pd.DataFrame(weather)

    return df

def analyze(df):

    result = {
        "Temperature (°C)": float(df["Temperature"].iloc[0]),
        "Humidity (%)": int(df["Humidity"].iloc[0]),
        "Wind Speed (km/h)": float(df["Wind Speed"].iloc[0]),
        "Feels Like (°C)": float(df["Feels Like"].iloc[0])
    }

    return result


@app.get("/weather")
def weather():

    data = fetch_weather()

    df = create_dataframe(data)

    result = analyze(df)

    return result
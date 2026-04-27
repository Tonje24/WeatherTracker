import requests
from dataclasses import dataclass
from db import WeatherDB

@dataclass
class WeatherObservation:
    city: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    elevation: float
    windspeed: float
    observation_time: str

geo = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": "Chicago", "count": 1})
result = geo.json()["results"][0]
lat = result["latitude"]
lon = result["longitude"]
country = result["country_code"]

weather = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": lat, "longitude": lon, "current_weather": "true"})
current = weather.json()["current_weather"]

obs = WeatherObservation("Chicago", country, lat, lon, current["temperature"], weather.json()["elevation"], current["windspeed"], current["time"])

db = WeatherDB()

db.insert(obs)
print(db.get_all())
print(db.get_by_id(1))
db.update_location(1, 42.0, -88.0)
db.delete(1)
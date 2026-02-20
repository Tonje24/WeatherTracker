import requests
from dataclasses import dataclass


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



geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {
    "name": "Chicago",
    "country": "US",
    "count": 1
}

geo_response = requests.get(geo_url, params = geo_params)
geo_data = geo_response.json()

result = geo_data["results"][0]
lat = result["latitude"]
lon = result["longitude"]
city = result["name"]
country = result["country_code"]



weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": "true"
}

weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()

current = weather_data["current_weather"]

temperature = current["temperature"]
windspeed = current["windspeed"]
observation_time = current["time"]
elevation = weather_data["elevation"]


obs = WeatherObservation(
    city,
    country,
    lat,
    lon,
    temperature,
    elevation,
    windspeed,
    observation_time
)

print(obs)

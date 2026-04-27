import requests
import psycopg2

conn = psycopg2.connect(dbname="weathertracker", user="postgres", password="Fotball2004", host="localhost")
cur = conn.cursor()

cities = [
    "Chicago",
    "New York",
    "Los Angeles",
    "Bergen",
    "Paris",
    "Oslo",
    "Stockholm",
    "Sydney",
    "Alicante",
    "Madrid",
]

for city in cities:
    geo = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": city, "count": 1})
    result = geo.json()["results"][0]
    lat = result["latitude"]
    lon = result["longitude"]
    country = result["country_code"]

    weather = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": lat, "longitude": lon, "current_weather": "true"})
    current = weather.json()["current_weather"]

    cur.execute(f"INSERT INTO observations (city, country, latitude, longitude, temperature_c, windspeed_kmh, observation_time) VALUES ('{city}', '{country}', {lat}, {lon}, {current['temperature']}, {current['windspeed']}, '{current['time']}')")
    print(f"Added {city}")

conn.commit()
conn.close()
print("Done!")



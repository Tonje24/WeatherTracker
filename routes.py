from flask import request, jsonify, render_template
from db import WeatherDB
import requests

def init_routes(app):
    db = WeatherDB()

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/search")
    def search():
        city = request.args.get("city")
        rows = db.get_all()
        results = [r for r in rows if r[1].lower() == city.lower()]
        return render_template("index.html", rows=results)

    @app.route("/observations/all")
    def all_observations():
        rows = db.get_all()
        return render_template("index.html", rows=rows)

    @app.route("/ingest", methods=["POST"])
    def ingest():
        city = request.args.get("city")
        country = request.args.get("country")
        geo = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": city, "count": 1})
        result = geo.json()["results"][0]
        lat = result["latitude"]
        lon = result["longitude"]
        weather = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": lat, "longitude": lon, "current_weather": "true"})
        current = weather.json()["current_weather"]
        db.insert_raw(city, country, lat, lon, current["temperature"], current["windspeed"], current["time"])
        return jsonify({"city": city, "temperature_c": current["temperature"]})

    @app.route("/observations", methods=["GET"])
    def list_observations():
        return jsonify(db.get_all())

    @app.route("/observations/<id>", methods=["GET"])
    def get_observation(id):
        return jsonify(db.get_by_id(id))

    @app.route("/observations/<id>", methods=["PUT"])
    def update_observation(id):
        data = request.get_json()
        db.update_notes(id, data["notes"])
        return jsonify({"id": id, "notes": data["notes"]})

    @app.route("/observations/<id>", methods=["DELETE"])
    def delete_observation(id):
        db.delete(id)
        return jsonify({"deleted": id})
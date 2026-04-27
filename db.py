import psycopg2

class WeatherDB:

    def __init__(self):
        self.conn = psycopg2.connect(dbname="weathertracker", user="postgres", password="Fotball2004", host="localhost")
        self.cur = self.conn.cursor()

    def insert(self, obs):
        self.cur.execute(f"INSERT INTO observations (city, country, latitude, longitude, temperature_c, windspeed_kmh, observation_time) VALUES ('{obs.city}', '{obs.country}', {obs.latitude}, {obs.longitude}, {obs.temperature}, {obs.windspeed}, '{obs.observation_time}')")
        self.conn.commit()

    def get_all(self):
        self.cur.execute("SELECT * FROM observations")
        return self.cur.fetchall()

    def get_by_id(self, id):
        self.cur.execute(f"SELECT * FROM observations WHERE id = {id}")
        return self.cur.fetchone()

    def update_location(self, id, lat, lon):
        self.cur.execute(f"UPDATE observations SET latitude = {lat}, longitude = {lon} WHERE id = {id}")
        self.conn.commit()

    def delete(self, id):
        self.cur.execute(f"DELETE FROM observations WHERE id = {id}")
        self.conn.commit()

    def insert_raw(self, city, country, lat, lon, temperature, windspeed, observation_time):
        self.cur.execute(f"INSERT INTO observations (city, country, latitude, longitude, temperature_c, windspeed_kmh, observation_time) VALUES ('{city}', '{country}', {lat}, {lon}, {temperature}, {windspeed}, '{observation_time}')")
        self.conn.commit()

    def update_notes(self, id, notes):
        self.cur.execute(f"UPDATE observations SET notes = '{notes}' WHERE id = {id}")
        self.conn.commit()    
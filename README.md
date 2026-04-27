# Tonje's Weather Tracker 

A Python application that fetches real-time weather data and stores it in a database. Built for CSIS 1230 - Programming for Everyone II.

## Features
- Fetches weather data from Open-Meteo API
- Stores data in PostgreSQL database
- RESTful API endpoints with Flask

## Installation
1. Clone this repository:
```bash
   git clone https://github.com/Tonje24/WeatherTracker.git
   cd WeatherTracker
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Set up your PostgreSQL database and run populate.py

## Usage
```bash
python app.py
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | View all observations |
| POST | /ingest?city=&country= | Add new observation |
| GET | /observations | Get all observations |
| GET | /observations/id | Get by ID |
| PUT | /observations/id | Update notes |
| DELETE | /observations/id | Delete observation |

## Technologies Used
- Python 3
- PostgreSQL
- Flask
- Open-Meteo API
from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-weather")
def get_weather():
    city = request.args.get("city")
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data=response.json()
    return jsonify({
    "name": data["location"]["name"],
    "region": data["location"]["region"],
    "country": data["location"]["country"],
    "temperature": data["current"]["temp_c"],
    "humidity": data["current"]["humidity"],
    "description": data["current"]["condition"]["text"],
    "windSpeed": data["current"]["wind_kph"]
})

    


if __name__ == "__main__":
    app.run(debug=True)

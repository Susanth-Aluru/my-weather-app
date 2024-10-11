
import requests
from flask import Flask,request, render_template
from json import dumps

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=["POST","GET"])
def index_data():
        city=request.form["city"]
        with open("apikey","r") as f:
            api_key = f.read()
        url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['current']['temperature']
            desc = data['current']["weather_descriptions"]
            pressure = data['current']["pressure"]
            humidity = data['current']["humidity"]
            wind_speed = data['current']["wind_speed"]
            date_time = data["location"]["localtime"]
            date = date_time[:-5]
            time = date_time[-5] + date_time[-4] + date_time[-3] + date_time[-2] + date_time[-1]
            weather_list = [temp, desc, pressure, humidity, wind_speed, date, time]
            list_json = dumps(weather_list)
            print(list_json)
            return render_template("index.html", temp=temp, desc=desc, pressure=pressure,humidity=humidity, wind_speed=wind_speed,date=date,time=time)

        else:
            return render_template("error.html")

app.run(host="0.0.0.0", port=5000)







import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import requests
from datetime import datetime, timedelta

class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root", 
            password="password",
            host="db", # name of the db service in docker-compose.yml
            port=3306,
            database="EnvironmentMonitor",
            auth_plugin='caching_sha2_password'
        )
        self.cursor = self.connection.cursor()
    
    def query_db(self):
        self.cursor.execute('SELECT * FROM SensorData')
        rec = []
        for c in self.cursor:
            rec.append(','.join(str(x) for x in c))
        return rec

app = Flask(__name__)
CORS(app)
conn = None

@app.route('/api/local', methods=['GET'])
def local():
    global conn
    if not conn:
        conn = DBManager()
    db_data = conn.query_db()
    response = {}
    response['hoursInfo'] = []
    for c in db_data:
        rec = c.split(',')
        response['hoursInfo'].append({
            'temperature': rec[1],
            'pressure': rec[2],
            'humidity': rec[3],
            'reducing': rec[4],
            'oxidising': rec[5],
            'nh3': rec[6],
            'pm1': rec[7],
            'pm2_5': rec[8],
            'pm10': rec[9],
            'timestamp': rec[10]
        })
    return response

@app.route('/api/global', methods=['GET'])
def hello():
    start_time = datetime.now() - timedelta(hours=72)
    end_time = datetime.now() - timedelta(hours=1)
    iso_start_time = start_time.isoformat() + "Z"
    iso_end_time = end_time.isoformat() + "Z"

    lat = request.args.get('lat', default = os.environ['MELB_CBD_LAT'], type = str)
    lng = request.args.get('lng', default = os.environ['MELB_CBD_LNG'], type = str)

    url = "https://airquality.googleapis.com/v1/history:lookup"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0",
        "Content-Type": "application/json",
    }
    params = {
        'key': os.environ['MAPS_API_KEY']
    }
    data = {
        "period": {
            "startTime": iso_start_time,
            "endTime": iso_end_time
        },
        "location": {
            "latitude": lat,
            "longitude": lng
        },
        "extraComputations": [
            "POLLUTANT_CONCENTRATION"
        ]
    }
    inner_response = requests.post(url=url, headers=headers, json=data, params=params)

    if not inner_response.ok:
        return "Invalid API call"

    response = {}
    response['hoursInfo'] = []
    for hourInfo in inner_response.json()['hoursInfo']:
        pollutants = hourInfo.get('pollutants')
        if pollutants == None or pollutants == []:
            continue

        hour = {}
        date_object = datetime.strptime(hourInfo['dateTime'], '%Y-%m-%dT%H:%M:%SZ')
        hour['timestamp'] = date_object.strftime('%Y-%m-%d %H:%M:%S')

        for pollutant in pollutants:
            code = pollutant['code']
            match code:
                case 'no2':
                    hour['no2'] = pollutant['concentration']['value']
                case 'so2':
                    hour['so2'] = pollutant['concentration']['value']
                case 'co':
                    hour['co'] = pollutant['concentration']['value']
                case 'o3':
                    hour['o3'] = pollutant['concentration']['value']
                case 'pm10':
                    hour['pm10'] = pollutant['concentration']['value']
                case 'pm25':
                    hour['pm2_5'] = pollutant['concentration']['value']
        response['hoursInfo'].append(hour)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
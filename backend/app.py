import os
from flask import Flask, request
import mysql.connector
import requests
from datetime import datetime, timedelta

class DBManager:
    def __init__(self, database='db', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password="",
            host=host, # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='caching_sha2_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,3)])
        self.connection.commit()
    
    def query_titles(self):
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

app = Flask(__name__)
conn = None

@app.route('/', methods=['GET'])
def hello_world():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response  + '<div>   Hello  ' + c + '</div>'
    return response

@app.route('/api/local', methods=['GET'])
def local():
    return "TODO: replace with db query"

@app.route('/api/global', methods=['GET'])
def hello():
    lat = request.args.get('lat', default = os.environ['MELB_CBD_LAT'], type = str)
    lng = request.args.get('lng', default = os.environ['MELB_CBD_LNG'], type = str)

    start_time = datetime.now() - timedelta(hours=72)
    end_time = datetime.now() - timedelta(hours=1)
    iso_start_time = start_time.isoformat() + "Z"
    iso_end_time = end_time.isoformat() + "Z"

    url = f"https://airquality.googleapis.com/v1/history:lookup"
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
    response = requests.post(url=url, headers=headers, json=data, params=params)
    return response.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
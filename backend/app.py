from flask import Flask, request
# from flask_mysqldb import MySQL
import requests

app = Flask(__name__)
# app.config["MYSQL_USER"] = "admin"
# app.config["MYSQL_PASSWORD"] = "password"
# app.config["MYSQL_DB"] = "db"

@app.route('/')
def hello_world():
    return 'Hello, World!!'

@app.route('/db', methods = ['GET', 'POST'])
def db():
    url = 'https://gateway.api.epa.vic.gov.au/environmentMonitoring/v1/sites/parameters?environmentalSegment=air&X-API-Key=b495d25375ed45789b915bc9c0a705b1'
    params = {'environmentalSegment': 'air'}
    headers = {'X-API-Key': 'b495d25375ed45789b915bc9c0a705b1'}
    response = requests.get(url=url)
    return url

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
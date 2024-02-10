import time
import mysql.connector
from enviroplus import gas
from bme280 import BME280
from pms5003 import PMS5003

class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root", 
            password="password",
            host="192.168.8.107", # name of the mysql service as set in the docker compose file
            port=3306,
            database="EnvironmentMonitor",
            auth_plugin='caching_sha2_password'
        )
        self.cursor = self.connection.cursor()
    
    def insert_data(self, data):
        self.cursor.execute('''
            INSERT INTO SensorData
            (
                temperature,
                pressure,
                humidity,
                reducing,
                oxidising,
                nh3,
                pm1,
                pm2_5,
                pm10
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''',
            (
                data['temperature'],
                data['pressure'],
                data['humidity'],
                data['reducing'],
                data['oxidising'],
                data['nh3'],
                data['pm1'],
                data['pm2_5'],
                data['pm10']
            ))
        self.connection.commit()
    
    def query_ids(self):
        self.cursor.execute('SELECT id FROM SensorData')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec
    
conn = DBManager()
bme280 = BME280()
bme280.setup(mode="forced")
pms5003 = PMS5003()

def read_data():
    gases = gas.read_all()
    particles = pms5003.read()
    return {
        "temperature": round(bme280.get_temperature(), 1), # °C
           "pressure": round(bme280.get_pressure(), 1),    # hPa
           "humidity": round(bme280.get_humidity(), 1),    # %
           "reducing": round(gases.reducing / 1000, 1),    # reducing gases kOhm
          "oxidising": round(gases.oxidising / 1000, 1),   # oxidising gases kOhm
                "nh3": round(gases.nh3 / 1000, 1),         # ammonia kOhm
                "pm1": particles.pm_ug_per_m3(1.0),        # particulate matter µg/m³
              "pm2_5": particles.pm_ug_per_m3(2.5),        # particulate matter µg/m³
               "pm10": particles.pm_ug_per_m3(10.0)        # particulate matter µg/m³
    }

while True:
    data = read_data()
    print(data)

    conn.insert_data(data)
    rec = conn.query_ids()
    response = ''
    for c in rec:
        response += str(c) + ' '
    print(response)
    
    time.sleep(2)

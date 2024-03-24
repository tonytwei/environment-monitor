from datetime import datetime, timedelta
import time
import mysql.connector
from bme280 import BME280
from pms5003 import PMS5003

class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root", 
            password="password",
            host="192.168.8.107", # db host's ip address
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
    
    def get_last_timestamp(self):
        self.cursor.execute('SELECT MAX(timestamp) FROM SensorData')
        result = self.cursor.fetchone()
        return result[0] if result else None
    
conn = DBManager()
bme280 = BME280()
bme280.setup(mode="forced")
pms5003 = PMS5003()

def read_data():
    particles = pms5003.read()
    return {
        "temperature": round(bme280.get_temperature(), 1), # °C
           "pressure": round(bme280.get_pressure(), 1),    # hPa
           "humidity": round(bme280.get_humidity(), 1),    # %
                "pm1": particles.pm_ug_per_m3(1.0),        # particulate matter µg/m³
              "pm2_5": particles.pm_ug_per_m3(2.5),        # particulate matter µg/m³
               "pm10": particles.pm_ug_per_m3(10.0)        # particulate matter µg/m³
    }

last_time = conn.get_last_timestamp()
while True:
    data = read_data()
    curr_time = datetime.now()
    
    if last_time is None or (curr_time - last_time) >= timedelta(seconds=10):
        conn.insert_data(data)
        last_time = curr_time

    time.sleep(2)

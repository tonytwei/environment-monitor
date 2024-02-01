import mysql.connector
from enviroplus import gas
from bme280 import BME280
from pms5003 import PMS5003

class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root", 
            password="password",
            host="192.168.8.125", # name of the mysql service as set in the docker compose file
            port=3306,
            database="db",
            auth_plugin='caching_sha2_password'
        )
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
    
conn = DBManager()
rec = conn.query_titles()
response = ''
for c in rec:
    response = response + '<div>   Hello  ' + c + '</div>'
print(response)


bme280 = BME280()
pms5003 = PMS5003()

def read_local():
    temp = bme280.get_temperature()
    pres = bme280.get_pressure()
    humi = bme280.get_humidity()

    gases = gas.read_all()

    particles = pms5003.read()

    return {
        "temperature": temp,
        "pressure": pres,
        "humidity": humi,
        "reducing": gases.reducing,
        "oxidising": gases.oxidising,
        "nh3": gases.nh3
    }

particles = None
try:
    while True:
        particles = pms5003.read()
        break
except:
    pass
print(particles)

print(read_local())

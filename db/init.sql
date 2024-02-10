DROP TABLE IF EXISTS SensorData;

CREATE TABLE IF NOT EXISTS SensorData (
    id INT AUTO_INCREMENT,
    temperature DECIMAL(6,2),
    pressure DECIMAL(6,2),
    humidity DECIMAL(6,2),
    reducing DECIMAL(6,2),
    oxidising DECIMAL(6,2),
    nh3 DECIMAL(6,2),
    pm1 SMALLINT,
    pm2_5 SMALLINT,
    pm10 SMALLINT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
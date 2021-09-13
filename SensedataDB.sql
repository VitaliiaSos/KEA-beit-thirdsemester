-- SHOW DATABASES;
USE sensedata;
SHOW TABLES;

CREATE TABLE hatdata (
	hatdataId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    DateandTime DATETIME DEFAULT CURRENT_TIMESTAMP,
    Temperature FLOAT,
    Humidity FLOAT,
    BarometricPressure FLOAT
)

SELECT * FROM hatdata;

-- SELECT Temperature, Humidity, BarometricPressure FROM hatdata
-- ORDER BY DateandTime DESC
-- LIMIT 1;
    
-- DROP TABLE hatdata;

-- INSERT INTO hatdata (DateandTime, Temperature, Humidity, BarometricPressure) VALUES ("1", "23.5", "25.7", "23.6");

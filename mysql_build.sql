-- CREATE APPLICATION DATABASE AND ITS USER
CREATE DATABASE IF NOT EXISTS oasd_devDB;

CREATE USER IF NOT EXISTS 'oasd_dev'@'localhost'
    IDENTIFIED BY '12345oasd';

GRANT ALL PRIVILEGES ON oasd_devDB.* TO 'oasd_dev'@'localhost';
-- GRANT SELECT on performance.* FOR oasd_dev;
-- PREPARES MYSQL SERVER 

-- CREATE THE APP DATABASE
CREATE USER IF NOT EXISTS 'oasd_admin'@'localhost'
        IDENTIFIED BY 'oasd_admin_password';
-- CREATE APPLICATION DATABASE ADMIN USER 
CREATE DATABASE IF NOT EXISTS 'oasd_db';
-- GRANT ALL PRIVELAGES ON APP DATABASE FOR THE ADMIN USER
GRANT  ALL ON oasd_db.* TO 'oasd_admin'@'localhost';
-- GRANT SELECT PRIVELAGE ON THE PERFORMANCE_SCHEMA DATABASE
-- FOR THE ADMIN USER
GRANT SELECT ON performance_schema.* TO 'oasd_admin'@'localhost';
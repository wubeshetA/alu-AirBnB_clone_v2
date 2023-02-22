-- CREATE USER CALLED HBTN_DEV IF EXISTS
CREATE USER IF NOT EXISTS 'hbtn_dev'@'localhost' IDENTIFIED BY 'hbtn_dev_pwd';
-- CREATE DATABASE CALLED HBTN_DEV_DB it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_dev_db;
-- GRANT ALL PRIVILEGES TO HBTN_DEV on hbtn_dev_db
GRANT ALL PRIVILEGES ON hbtn_dev_db.* TO 'hbtn_dev'@'localhost';
-- grant select privileges to hbtn_dev on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbtn_dev'@'localhost'; 

-- a script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS foodie_db;
CREATE USER IF NOT EXISTS 'foodie_dev'@'localhost' IDENTIFIED BY 'foodie_pwd';
GRANT ALL PRIVILEGES ON foodie_db.* TO 'foodie_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'foodie_dev'@'localhost';

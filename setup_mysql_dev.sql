-- Create a DATABASE
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- give hbnb_dev user ALL PRIVILEGES on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- give hbnb_dev user SELECT PRIVILEGE on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

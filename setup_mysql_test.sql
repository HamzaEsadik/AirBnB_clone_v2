-- Create a DATABASE
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- give hbnb_dev user ALL PRIVILEGES on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- give hbnb_dev user SELECT PRIVILEGE on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

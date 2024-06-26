-- Create a new user 'hbnb_test' with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Create the database 'hbnb_test_db' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Grant all privileges on 'hbnb_test_db' to 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on 'performance_schema' to 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;

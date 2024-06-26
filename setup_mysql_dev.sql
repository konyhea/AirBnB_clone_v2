-- Create a new user 'hbnb_test' with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Create the database 'hbnb_test_db' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Grant all privileges on 'hbnb_test_db' to 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on 'performance_schema' to 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;

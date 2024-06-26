/**
 * This script creates a MySQL server with the following:
 * - Database: hbnb_dev_db
 * - User: hbnb_dev with password hbnb_dev_pwd in localhost
 * - Grants all privileges for hbnb_dev on hbnb_dev_db
 * - Grants SELECT privilege for hbnb_dev on performance
 * 
 * The script performs the following steps:
 * 1. Creates the database hbnb_dev_db if it doesn't exist
 * 2. Creates the user 'hbnb_dev'@'localhost' if it doesn't exist
 * 3. Grants all privileges on hbnb_dev_db to 'hbnb_dev'@'localhost'
 * 4. Grants SELECT privilege on performance_schema to 'hbnb_dev'@'localhost'
 * 5. Flushes privileges to apply changes
 */

-- Create a new database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Give all privileges whats on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Give all privileges whats on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
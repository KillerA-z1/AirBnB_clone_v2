/**
 * Creates a MySQL server with the following:
 * - Database hbnb_test_db.
 * - User hbnb_test with password hbnb_test_pwd in localhost.
 * - Grants all privileges for hbnb_test on hbnb_test_db.
 * - Grants SELECT privilege for hbnb_test on performance_schema.
 * 
 * The script performs the following steps:
 * 1. Creates the database hbnb_test_db if it doesn't already exist.
 * 2. Creates the user 'hbnb_test'@'localhost' if it doesn't already exist, with the password 'hbnb_test_pwd'.
 * 3. Grants all privileges on hbnb_test_db to the user 'hbnb_test'@'localhost'.
 * 4. Grants SELECT privilege on performance_schema to the user 'hbnb_test'@'localhost'.
 * 5. Flushes privileges to apply the changes.
 */

-- Create a new database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Give all privileges whats on hbnb_test_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Give all privileges whats on performance_schema to hbnb_test 
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
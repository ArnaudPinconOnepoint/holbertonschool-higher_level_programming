-- Create the user if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Reload the privilege tables to ensure that the changes take effect
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Creates the table force_name if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the newly created database
USE hbtn_0d_usa;

-- Create the table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,           -- Unique, auto-generated ID
    state_id INT NOT NULL,                    -- Foreign key referencing states
    name VARCHAR(256) NOT NULL,               -- City name cannot be NULL
    PRIMARY KEY (id),                         -- Set id as the primary key
    FOREIGN KEY (state_id) REFERENCES states(id)  -- Define foreign key
);
